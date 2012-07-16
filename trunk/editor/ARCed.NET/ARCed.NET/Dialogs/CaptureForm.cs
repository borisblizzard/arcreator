#region Using Directives

using System;
using System.Drawing;
using System.IO;
using System.Reflection;
using System.Windows.Forms;
using ARCed.Core.Win32;

#endregion

namespace ARCed.Dialogs
{
    /// <summary>
    /// Invisible form that is used as an overlay of the screen for capturing color data under the mouse.
    /// </summary>
	public sealed partial class CaptureForm : Form
    {
        #region Private Fields

        private Color _capturedColor;
        private Bitmap _screenCapture;

        #endregion

        #region Public Properties

        /// <summary>
		/// Gets the color under the mouse where the user clicked
		/// </summary>
		public Color CaptureColor { get { return _capturedColor; } }

        #endregion

        #region Constructor

        /// <summary>
		/// Default constructor
		/// </summary>
		public CaptureForm()
		{
			InitializeComponent();
			Cursor = LoadCursorFromResource("ARCed.Files.CustomCross.cur");
			_capturedColor = Color.Black;
		}

        #endregion

        #region Private Methods

        private static Cursor LoadCursorFromResource(string resourceName)
		{
			Cursor result;
			try
			{
				var tempFile = Path.GetTempFileName();
				using (Stream s =
					Assembly.GetExecutingAssembly().GetManifestResourceStream(resourceName))
				using (var resourceFile = new FileStream(tempFile, FileMode.Create))
				{
				    if (s != null)
				    {
				        var b = new byte[s.Length + 1];
				        s.Read(b, 0, Convert.ToInt32(s.Length));
				        resourceFile.Write(b, 0, Convert.ToInt32(b.Length - 1));
				    }
				    resourceFile.Flush();
				}
				result = new Cursor(NativeMethods.LoadCursorFromFile(tempFile));
				File.Delete(tempFile);
			}
			catch 
			{
				result = Cursors.Cross;
			}
			return result;
		}

		internal void TakeSnapShot()
		{
			var bounds = Screen.GetBounds(Point.Empty);
			this._screenCapture = new Bitmap(bounds.Width, bounds.Height);
			using (Graphics g = Graphics.FromImage(this._screenCapture))
				g.CopyFromScreen(Point.Empty, Point.Empty, bounds.Size);
			BackgroundImage = this._screenCapture;
		}

		private void CaptureFormClicked(object sender, EventArgs e)
		{
			Close();
		}

		private void CaptureFormMouseMoved(object sender, MouseEventArgs e)
		{
			_capturedColor = this._screenCapture.GetPixel(MousePosition.X, MousePosition.Y);
        }

        #endregion
    }
}
