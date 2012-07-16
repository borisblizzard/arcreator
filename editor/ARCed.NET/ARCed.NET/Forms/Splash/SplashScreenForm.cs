#region Using Directives

using System.Drawing;
using System.Windows.Forms;

#endregion

namespace ARCed.Forms.Splash
{
	public partial class SplashScreenForm : Form
	{
		delegate void StringParameterDelegate(string Text);
		delegate void StringParameterWithStatusDelegate(string Text, TypeOfMessage tom);
		delegate void SplashShowCloseDelegate();

	    /// <summary>
	    /// To ensure splash screen is closed using the API and not by keyboard or any other things
	    /// </summary>
	    private bool CloseSplashScreenFlag;

		/// <summary>
		/// Base constructor
		/// </summary>
		public SplashScreenForm()
		{
			InitializeComponent();
			this.labelStatus.Parent = this.pictureBoxSplash;
			this.labelStatus.BackColor = Color.Transparent;
			labelStatus.ForeColor = Color.AntiqueWhite;
		}

		/// <summary>
		/// Displays the splashscreen
		/// </summary>
		public void ShowSplashScreen()
		{
			if (InvokeRequired)
			{
				// We're not in the UI thread, so we need to call BeginInvoke
				BeginInvoke(new SplashShowCloseDelegate(ShowSplashScreen));
				return;
			}
			this.Show();
			Application.Run(this);
		}

		/// <summary>
		/// Closes the SplashScreen
		/// </summary>
		public void CloseSplashScreen()
		{
			if (InvokeRequired)
			{
				// We're not in the UI thread, so we need to call BeginInvoke
				BeginInvoke(new SplashShowCloseDelegate(CloseSplashScreen));
				return;
			}
			CloseSplashScreenFlag = true;
			this.Close();
		}

		/// <summary>
		/// Update text message
		/// </summary>
		/// <param name="Text">Message</param>
		public void UdpateStatusText(string Text)
		{
			if (InvokeRequired)
			{
				// We're not in the UI thread, so we need to call BeginInvoke
				BeginInvoke(new StringParameterDelegate(UdpateStatusText), new object[] { Text });
				return;
			}
			labelStatus.ForeColor = Color.AntiqueWhite;
			labelStatus.Text = Text;
		}


		/// <summary>
		/// Update text with message color defined as white/yellow/red/ for success/warning/failure
		/// </summary>
		/// <param name="Text">Message</param>
		/// <param name="tom">Type of Message</param>
		public void UdpateStatusTextWithStatus(string Text, TypeOfMessage tom)
		{
			if (InvokeRequired)
			{
				// We're not in the UI thread, so we need to call BeginInvoke
				BeginInvoke(new StringParameterWithStatusDelegate(UdpateStatusTextWithStatus), new object[] { Text, tom });
				return;
			}
			switch (tom)
			{
				case TypeOfMessage.Error:
					labelStatus.ForeColor = Color.Red;
					break;
				case TypeOfMessage.Warning:
					labelStatus.ForeColor = Color.Yellow;
					break;
				case TypeOfMessage.Success:
					labelStatus.ForeColor = Color.AntiqueWhite;
					break;
			}
			labelStatus.Text = Text;

		}

		/// <summary>
		/// Prevents the closing of form other than by calling the CloseSplashScreen function
		/// </summary>
		/// <param name="sender"></param>
		/// <param name="e"></param>
		private void SplashForm_FormClosing(object sender, FormClosingEventArgs e)
		{
			if (CloseSplashScreenFlag == false)
				e.Cancel = true;
		}
	}
}
