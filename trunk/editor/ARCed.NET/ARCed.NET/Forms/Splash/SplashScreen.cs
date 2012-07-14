using System;
using System.Collections.Generic;
using System.ComponentModel;

using System.Drawing;
using System.Text;
using System.Windows.Forms;

namespace ARCed.Forms.Splash
{
	/// <summary>
	/// Defined types of messages: Success/Warning/Error.
	/// </summary>
	public enum TypeOfMessage
	{
		Success,
		Warning,
		Error,
	}
	/// <summary>
	/// Initiate instance of SplashScreen
	/// </summary>
	public static class SplashScreen
	{
		static SplashScreenForm sf = null;

		/// <summary>
		/// Displays the splashscreen
		/// </summary>
		public static void ShowSplashScreen()
		{
			if (sf == null)
			{
				sf = new SplashScreenForm();
				sf.ShowSplashScreen();
			}
		}

		/// <summary>
		/// Closes the SplashScreen
		/// </summary>
		public static void CloseSplashScreen()
		{
			if (sf != null)
			{
				sf.CloseSplashScreen();
				sf = null;
			}
		}

		/// <summary>
		/// Update text in default green color of success message
		/// </summary>
		/// <param name="Text">Message</param>
		public static void UdpateStatusText(string Text)
		{
			if (sf != null)
				sf.UdpateStatusText(Text);

		}

		/// <summary>
		/// Update text with message color defined as green/yellow/red/ for success/warning/failure
		/// </summary>
		/// <param name="Text">Message</param>
		/// <param name="tom">Type of Message</param>
		public static void UdpateStatusTextWithStatus(string Text, TypeOfMessage tom)
		{

			if (sf != null)
				sf.UdpateStatusTextWithStatus(Text, tom);
		}
	}

}
