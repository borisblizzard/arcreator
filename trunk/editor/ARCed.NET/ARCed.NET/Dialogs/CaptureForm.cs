using System;
using System.Drawing;
using System.IO;
using System.Reflection;
using System.Runtime.InteropServices;
using System.Windows.Forms;

namespace ARCed.Dialogs
{
	public sealed partial class CaptureForm : Form
	{

		private Color _capturedColor;
		/// <summary>
		/// Gets the color under the mouse where the user clicked
		/// </summary>
		public Color CaptureColor { get { return _capturedColor; } }

		private Bitmap ScreenCapture;

		/// <summary>
		/// Default constructor
		/// </summary>
		public CaptureForm()
		{
			InitializeComponent();
			Cursor = LoadCursorFromResource("ARCed.Files.CustomCross.cur");
			_capturedColor = Color.Black;
		}

		private static Cursor LoadCursorFromResource(string resourceName)
		{
			Cursor result;
			try
			{
				string tempFile = Path.GetTempFileName();
				using (Stream s =
					Assembly.GetExecutingAssembly().GetManifestResourceStream(resourceName))
				using (FileStream resourceFile = new FileStream(tempFile, FileMode.Create))
				{
					byte[] b = new byte[s.Length + 1];
					s.Read(b, 0, Convert.ToInt32(s.Length));
					resourceFile.Write(b, 0, Convert.ToInt32(b.Length - 1));
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
			Rectangle bounds = Screen.GetBounds(Point.Empty);
			ScreenCapture = new Bitmap(bounds.Width, bounds.Height);
			using (Graphics g = Graphics.FromImage(ScreenCapture))
				g.CopyFromScreen(Point.Empty, Point.Empty, bounds.Size);
			this.BackgroundImage = ScreenCapture;
		}

		private void captureForm_Clicked(object sender, EventArgs e)
		{
			this.Close();
		}

		private void captureForm_MouseMoved(object sender, MouseEventArgs e)
		{
			_capturedColor =
				ScreenCapture.GetPixel(MousePosition.X, MousePosition.Y);
			//RGBForm.SetSampleColor(_capturedColor);
		}
	}
}
