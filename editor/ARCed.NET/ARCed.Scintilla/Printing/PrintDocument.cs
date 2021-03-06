#region Using Directives

using System.ComponentModel;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Drawing.Printing;

#endregion


namespace ARCed.Scintilla
{
	/// <summary>
	///     ARCed.Scintilla derived class for handling printing of source code from a Scintilla control.
	/// </summary>
	[TypeConverter(typeof(ExpandableObjectConverter))]
	public class PrintDocument : System.Drawing.Printing.PrintDocument
	{
		#region Fields

		private int _iCurrentPage;
		private int _iPosition;
		private int _iPrintEnd;
		private readonly Scintilla _oScintillaControl;

		#endregion Fields


		#region Methods

		private void DrawCurrentPage(Graphics oGraphics, Rectangle oBounds)
		{
			Point[] oPoints = {
                new Point(oBounds.Left, oBounds.Top),
                new Point(oBounds.Right, oBounds.Bottom)
                };
			oGraphics.TransformPoints(CoordinateSpace.Device, CoordinateSpace.Page, oPoints);

			var oPrintRectangle = new PrintRectangle(oPoints[0].X, oPoints[0].Y, oPoints[1].X, oPoints[1].Y);

			var oRangeToFormat = new RangeToFormat();
			oRangeToFormat.hdc = oRangeToFormat.hdcTarget = oGraphics.GetHdc();
			oRangeToFormat.rc = oRangeToFormat.rcPage = oPrintRectangle;
			oRangeToFormat.chrg.cpMin = this._iPosition;
			oRangeToFormat.chrg.cpMax = this._iPrintEnd;

			this._iPosition = this._oScintillaControl.NativeInterface.FormatRange(true, ref oRangeToFormat);

		}


		private Rectangle DrawFooter(Graphics oGraphics, Rectangle oBounds, PageInformation oFooter)
		{
			if (oFooter.Display)
			{
				int iHeight = oFooter.Height;
				var oFooterBounds = new Rectangle(oBounds.Left, oBounds.Bottom - iHeight, oBounds.Width, iHeight);

				oFooter.Draw(oGraphics, oFooterBounds, this.DocumentName, this._iCurrentPage);

				return new Rectangle(
					oBounds.Left, oBounds.Top,
					oBounds.Width, oBounds.Height - oFooterBounds.Height - oFooter.Margin
					);
			}
			else
			{
				return oBounds;
			}
		}


		private Rectangle DrawHeader(Graphics oGraphics, Rectangle oBounds, PageInformation oHeader)
		{
			if (oHeader.Display)
			{
				var oHeaderBounds = new Rectangle(oBounds.Left, oBounds.Top, oBounds.Width, oHeader.Height);

				oHeader.Draw(oGraphics, oHeaderBounds, this.DocumentName, this._iCurrentPage);

				return new Rectangle(
					oBounds.Left, oBounds.Top + oHeaderBounds.Height + oHeader.Margin,
					oBounds.Width, oBounds.Height - oHeaderBounds.Height - oHeader.Margin
					);
			}
			else
			{
				return oBounds;
			}
		}


		/// <summary>
		///     Method called after the Print method is called and before the first page of the document prints
		/// </summary>
		/// <param name="e">A PrintPageEventArgs that contains the event data</param>
		protected override void OnBeginPrint(PrintEventArgs e)
		{
			base.OnBeginPrint(e);

			this._iPosition = 0;
			this._iPrintEnd = this._oScintillaControl.TextLength;
			this._iCurrentPage = 1;
		}


		/// <summary>
		///     Method called when the last page of the document has printed
		/// </summary>
		/// <param name="e">A PrintPageEventArgs that contains the event data</param>
		protected override void OnEndPrint(PrintEventArgs e)
		{
			base.OnEndPrint(e);
		}


		/// <summary>
		///     Method called when printing a page
		/// </summary>
		/// <param name="e">A PrintPageEventArgs that contains the event data</param>
		protected override void OnPrintPage(PrintPageEventArgs e)
		{
			base.OnPrintPage(e);

			PageSettings oPageSettings = null;
			HeaderInformation oHeader = ((PageSettings)DefaultPageSettings).Header;
			FooterInformation oFooter = ((PageSettings)DefaultPageSettings).Footer;
			Rectangle oPrintBounds = e.MarginBounds;
			bool bIsPreview = PrintController.IsPreview;

			// When not in preview mode, adjust graphics to account for hard margin of the printer
			if (!bIsPreview)
			{
				e.Graphics.TranslateTransform(-e.PageSettings.HardMarginX, -e.PageSettings.HardMarginY);
			}

			// Get the header and footer provided if using Scintilla.Printing.PageSettings
			if (e.PageSettings is PageSettings)
			{
				oPageSettings = (PageSettings)e.PageSettings;

				oHeader = oPageSettings.Header;
				oFooter = oPageSettings.Footer;

				this._oScintillaControl.NativeInterface.SetPrintMagnification(oPageSettings.FontMagnification);
				this._oScintillaControl.NativeInterface.SetPrintColourMode((int)oPageSettings.ColorMode);
			}

			// Draw the header and footer and get remainder of page bounds
			oPrintBounds = this.DrawHeader(e.Graphics, oPrintBounds, oHeader);
			oPrintBounds = this.DrawFooter(e.Graphics, oPrintBounds, oFooter);

			// When not in preview mode, adjust page bounds to account for hard margin of the printer
			if (!bIsPreview)
			{
				oPrintBounds.Offset((int)-e.PageSettings.HardMarginX, (int)-e.PageSettings.HardMarginY);
			}
			this.DrawCurrentPage(e.Graphics, oPrintBounds);

			// Increment the page count and determine if there are more pages to be printed
			this._iCurrentPage++;
			e.HasMorePages = (this._iPosition < this._iPrintEnd);
		}


		private void ResetDocumentName()
		{
			this.DocumentName = "document";
		}


		private void ResetOriginAtMargins()
		{
			this.OriginAtMargins = false;
		}


		internal bool ShouldSerialize()
		{
			return base.DocumentName != "document" || this.OriginAtMargins;
		}


		private bool ShouldSerializeDocumentName()
		{
			return this.DocumentName != "document";
		}


		private bool ShouldSerializeOriginAtMargins()
		{
			return this.OriginAtMargins;
		}

		#endregion Methods


		#region Properties

		public new string DocumentName
		{
			get
			{
				return base.DocumentName;
			}
			set
			{
				base.DocumentName = value;
			}
		}


		public new bool OriginAtMargins
		{
			get
			{
				return base.OriginAtMargins;
			}
			set
			{
				base.OriginAtMargins = value;
			}
		}

		#endregion Properties


		#region Constructors

		/// <summary>
		///     Default Constructor
		/// </summary>
		/// <param name="oScintillaControl">Scintilla control being printed</param>
		public PrintDocument(Scintilla oScintillaControl)
		{
			this._oScintillaControl = oScintillaControl;
			DefaultPageSettings = new PageSettings();
		}

		#endregion Constructors
	}
}
