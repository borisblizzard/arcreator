#region Using Directives

using System;
using System.Collections;
using System.Collections.Specialized;
using System.Diagnostics;
using System.Drawing;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Reflection;
using System.Resources;
using System.Runtime.InteropServices;
using System.Text.RegularExpressions;
using System.Windows.Forms;
using Microsoft.Win32;

#endregion

namespace ARCed.Dialogs
{

	/// <summary>
	/// Generic, self-contained About Box dialog
	/// </summary>
	public partial class AboutBox : Form
    {
        #region Private Fields

        private bool _isPainted;
        private string _entryAssemblyName;
        private string _callingAssemblyName;
        private string _executingAssemblyName;
        private Assembly _entryAssembly;
        private NameValueCollection _entryAssemblyAttribCollection;
        private int _minWindowHeight;

        #endregion

        #region Constructor

        /// <summary>
		/// Creates a new instance of the custom AboutBox object
		/// </summary>
		public AboutBox()
		{
			this.InitializeComponent();
		}

        #endregion

        #region Public Properties

        /// <summary>
		/// Returns the entry assembly for the current application domain
		/// </summary>
		/// <remarks>
		/// This is usually read-only, but in some weird cases (Smart Client apps) 
		/// you won't have an entry assembly, so you may want to set this manually.
		/// </remarks>
		public Assembly AppEntryAssembly
		{
			get { return this._entryAssembly; }
			set
			{
				this._entryAssembly = value;
			}
		}

		/// <summary>
		/// Single line of text to show in the application title section of the about box dialog
		/// </summary>
		/// <remarks>
		/// defaults to "%title%" 
		/// %title% = Assembly: AssemblyTitle
		/// </remarks>
		public string AppTitle
		{
			get
			{
				return this.AppTitleLabel.Text;
			}
			set
			{
				this.AppTitleLabel.Text = value;
			}
		}

		/// <summary>
		/// single line of text to show in the description section of the about box dialog
		/// </summary>
		/// <remarks>
		/// defaults to "%description%"
		/// %description% = Assembly: AssemblyDescription
		/// </remarks>
		public string AppDescription
		{
			get
			{
				return this.AppDescriptionLabel.Text;
			}
			set
			{
				if (value == "")
				{
					this.AppDescriptionLabel.Visible = false;
				}
				else
				{
					this.AppDescriptionLabel.Visible = true;
					this.AppDescriptionLabel.Text = value;
				}
			}
		}

		/// <summary>
		/// single line of text to show in the version section of the about dialog
		/// </summary>
		/// <remarks>
		/// defaults to "Version %version%"
		/// %version% = Assembly: AssemblyVersion
		/// </remarks>
		public string AppVersion
		{
			get
			{
				return this.AppVersionLabel.Text;
			}
			set
			{
				if (value == "")
				{
					this.AppVersionLabel.Visible = false;
				}
				else
				{
					this.AppVersionLabel.Visible = true;
					this.AppVersionLabel.Text = value;
				}
			}
		}

		/// <summary>
		/// Single line of text to show in the copyright section of the about dialog
		/// </summary>
		/// <remarks>
		/// defaults to "Copyright © %year%, %company%"
		/// %company% = Assembly: AssemblyCompany
		/// %year% = current 4-digit year
		/// </remarks>
		public string AppCopyright
		{
			get
			{
				return this.AppCopyrightLabel.Text;
			}
			set
			{
				if (value == "")
				{
					this.AppCopyrightLabel.Visible = false;
				}
				else
				{
					this.AppCopyrightLabel.Visible = true;
					this.AppCopyrightLabel.Text = value;
				}
			}
		}

		/// <summary>
		/// Intended for the default 32x32 application icon to appear in the upper left of the about dialog
		/// </summary>
		/// <remarks>
		/// If you open this form using .ShowDialog(Owner), the icon can be derived from the owning form
		/// </remarks>
		public Image AppImage
		{
			get
			{
				return this.ImagePictureBox.Image;
			}
			set
			{
				this.ImagePictureBox.Image = value;
			}
		}

		/// <summary>
		/// multiple lines of miscellaneous text to show in rich text box
		/// </summary>
		/// <remarks>
		/// defaults to "%product% is %copyright%, %trademark%"
		/// %product% = Assembly: AssemblyProduct
		/// %copyright% = Assembly: AssemblyCopyright
		/// %trademark% = Assembly: AssemblyTrademark
		/// </remarks>
		public string AppMoreInfo
		{
			get
			{
				return this.MoreRichTextBox.Text;
			}
			set
			{
				if (String.IsNullOrEmpty(value))
				{
					this.MoreRichTextBox.Visible = false;
				}
				else
				{
					this.MoreRichTextBox.Visible = true;
					this.MoreRichTextBox.Text = value;
				}
			}
		}

        /// <summary>
        /// Determines if the "Details" (advanced assembly details) button is shown
        /// </summary>
        public bool AppDetailsButton
        {
            get { return this.DetailsButton.Visible; }
            set { this.DetailsButton.Visible = value; }
        }

        #endregion

        #region Private Methods

        private static DateTime AssemblyLastWriteTime(Assembly a)
		{
			try
			{
				if (String.IsNullOrEmpty(a.Location))
					return DateTime.MaxValue;
				try
				{
					return File.GetLastWriteTime(a.Location);
				}
				catch (Exception)
				{
					return DateTime.MaxValue;
				}
			}
			catch
			{
				return DateTime.Now;
			}
		}

		private static DateTime AssemblyBuildDate(Assembly a, bool forceFileDate)
		{
			var assemblyVersion = a.GetName().Version;
			DateTime dt;

			if (forceFileDate)
			{
				dt = AssemblyLastWriteTime(a);
			}
			else
			{
				dt = DateTime.Parse("01/01/2000").AddDays(assemblyVersion.Build).AddSeconds(assemblyVersion.Revision * 2);
				if (TimeZone.IsDaylightSavingTime(dt, TimeZone.CurrentTimeZone.GetDaylightChanges(dt.Year)))
				{
					dt = dt.AddHours(1);
				}
				if (dt > DateTime.Now || assemblyVersion.Build < 730 || assemblyVersion.Revision == 0)
				{
					dt = AssemblyLastWriteTime(a);
				}
			}

			return dt;
		}


		private NameValueCollection AssemblyAttribs(Assembly a)
		{
			string typeName;
			string name;
		    string value = "";
			var nvc = new NameValueCollection();
			var r = new Regex(@"(\.Assembly|\.)(?<Name>[^.]*)Attribute$", RegexOptions.IgnoreCase);
			foreach (object attrib in a.GetCustomAttributes(false))
			{
				typeName = attrib.GetType().ToString();
				name = r.Match(typeName).Groups["Name"].ToString();
				switch (typeName)
				{
					case "System.CLSCompliantAttribute":
						value = ((CLSCompliantAttribute)attrib).IsCompliant.ToString(); break;
					case "System.Diagnostics.DebuggableAttribute":
						value = ((DebuggableAttribute)attrib).IsJITTrackingEnabled.ToString(); break;
					case "System.Reflection.AssemblyCompanyAttribute":
						value = ((AssemblyCompanyAttribute)attrib).Company; break;
					case "System.Reflection.AssemblyConfigurationAttribute":
						value = ((AssemblyConfigurationAttribute)attrib).Configuration; break;
					case "System.Reflection.AssemblyCopyrightAttribute":
						value = ((AssemblyCopyrightAttribute)attrib).Copyright; break;
					case "System.Reflection.AssemblyDefaultAliasAttribute":
						value = ((AssemblyDefaultAliasAttribute)attrib).DefaultAlias; break;
					case "System.Reflection.AssemblyDelaySignAttribute":
						value = ((AssemblyDelaySignAttribute)attrib).DelaySign.ToString(); break;
					case "System.Reflection.AssemblyDescriptionAttribute":
						value = ((AssemblyDescriptionAttribute)attrib).Description; break;
					case "System.Reflection.AssemblyInformationalVersionAttribute":
						value = ((AssemblyInformationalVersionAttribute)attrib).InformationalVersion; break;
					case "System.Reflection.AssemblyKeyFileAttribute":
						value = ((AssemblyKeyFileAttribute)attrib).KeyFile; break;
					case "System.Reflection.AssemblyProductAttribute":
						value = ((AssemblyProductAttribute)attrib).Product; break;
					case "System.Reflection.AssemblyTrademarkAttribute":
						value = ((AssemblyTrademarkAttribute)attrib).Trademark; break;
					case "System.Reflection.AssemblyTitleAttribute":
						value = ((AssemblyTitleAttribute)attrib).Title; break;
					case "System.Resources.NeutralResourcesLanguageAttribute":
						value = ((NeutralResourcesLanguageAttribute)attrib).CultureName; break;
					case "System.Resources.SatelliteContractVersionAttribute":
						value = ((SatelliteContractVersionAttribute)attrib).Version; break;
					case "System.Runtime.InteropServices.ComCompatibleVersionAttribute":
						{
							var x = ((ComCompatibleVersionAttribute)attrib);
							value = x.MajorVersion + "." + x.MinorVersion + "." + x.RevisionNumber + "." + x.BuildNumber; break;
						}
					case "System.Runtime.InteropServices.ComVisibleAttribute":
						value = ((ComVisibleAttribute)attrib).Value.ToString(); break;
					case "System.Runtime.InteropServices.GuidAttribute":
						value = ((GuidAttribute)attrib).Value; break;
					case "System.Runtime.InteropServices.TypeLibVersionAttribute":
						{
						    var x = ((TypeLibVersionAttribute)attrib);
							value = x.MajorVersion + "." + x.MinorVersion; break;
						}
					case "System.Security.AllowPartiallyTrustedCallersAttribute":
						value = "(Present)"; break;
					default:
						// debug.writeline("** unknown assembly attribute '" + TypeName + "'")
						value = typeName; break;
				}

				if (nvc[name] == null)
				{
					nvc.Add(name, value);
				}
			}
			try
			{
				nvc.Add("CodeBase", a.CodeBase.Replace("file:///", ""));
			}
			catch (NotSupportedException)
			{
				nvc.Add("CodeBase", "(not supported)");
			}
			// build date
			var dt = AssemblyBuildDate(a, false);
		    nvc.Add("BuildDate", dt == DateTime.MaxValue ? "(unknown)" : 
                dt.ToString("yyyy-MM-dd hh:mm tt"));
		    // location
			try
			{
				nvc.Add("Location", a.Location);
			}
			catch (NotSupportedException)
			{
				nvc.Add("Location", "(not supported)");
			}
			// version
			try
			{
				if (a.GetName().Version.Major == 0 && a.GetName().Version.Minor == 0)
				{
					nvc.Add("Version", "(unknown)");
				}
				else
				{
					nvc.Add("Version", a.GetName().Version.ToString());
				}
			}
			catch (Exception)
			{
				nvc.Add("Version", "(unknown)");
			}

			nvc.Add("FullName", a.FullName);

			return nvc;
		}

		private static string RegistryHklmValue(string keyName, string subKeyRef)
		{
			RegistryKey rk;
			try
			{
			    rk = Registry.LocalMachine.OpenSubKey(keyName);
			    if (rk != null) return (string)rk.GetValue(subKeyRef, "");
			}
			catch (Exception)
			{
				return "";
			}
		    return "";
		}

		private void ShowSysInfo()
		{
			var strSysInfoPath = "";
			strSysInfoPath = RegistryHklmValue(@"SOFTWARE\Microsoft\Shared Tools Location", "MSINFO");
			if (strSysInfoPath == "")
			{
				strSysInfoPath = RegistryHklmValue(@"SOFTWARE\Microsoft\Shared Tools\MSINFO", "PATH");
			}
			if (strSysInfoPath == "")
			{
				MessageBox.Show("System Information is unavailable at this time." +
					Environment.NewLine +
					Environment.NewLine +
					"(couldn't find path for Microsoft System Information Tool in the registry.)",
					Text, MessageBoxButtons.OK, MessageBoxIcon.Warning);
				return;
			}

			try
			{
				Process.Start(strSysInfoPath);
			}
			catch (Exception)
			{
				MessageBox.Show("System Information is unavailable at this time." +
					Environment.NewLine +
					Environment.NewLine +
					"(couldn't launch '" + strSysInfoPath + "')",
					Text, MessageBoxButtons.OK, MessageBoxIcon.Stop);
			}

		}

		private static void Populate(ListView lvw, string key, string value)
		{
			if (value == "")
				return;
			var lvi = new ListViewItem
			{
			    Text = key
			};
		    lvi.SubItems.Add(value);
			lvw.Items.Add(lvi);
		}

		private void PopulateAppInfo()
		{
			var d = AppDomain.CurrentDomain;
			Populate(this.AppInfoListView, "Application Name", d.SetupInformation.ApplicationName);
			Populate(this.AppInfoListView, "Application Base", d.SetupInformation.ApplicationBase);
			Populate(this.AppInfoListView, "Cache Path", d.SetupInformation.CachePath);
			Populate(this.AppInfoListView, "Configuration File", d.SetupInformation.ConfigurationFile);
			Populate(this.AppInfoListView, "Dynamic Base", d.SetupInformation.DynamicBase);
			Populate(this.AppInfoListView, "Friendly Name", d.FriendlyName);
			Populate(this.AppInfoListView, "License File", d.SetupInformation.LicenseFile);
			Populate(this.AppInfoListView, "private Bin Path", d.SetupInformation.PrivateBinPath);
			Populate(this.AppInfoListView, "Shadow Copy Directories", d.SetupInformation.ShadowCopyDirectories);
			Populate(this.AppInfoListView, " ", " ");
			Populate(this.AppInfoListView, "Entry Assembly", this._entryAssemblyName);
			Populate(this.AppInfoListView, "Executing Assembly", this._executingAssemblyName);
			Populate(this.AppInfoListView, "Calling Assembly", this._callingAssemblyName);
		}

		private void PopulateAssemblies()
		{
			foreach (Assembly a in AppDomain.CurrentDomain.GetAssemblies())
			{
				this.PopulateAssemblySummary(a);
			}
			this.AssemblyNamesComboBox.SelectedIndex = this.AssemblyNamesComboBox.FindStringExact(this._entryAssemblyName);
		}

		private void PopulateAssemblySummary(Assembly a)
		{
			var nvc = this.AssemblyAttribs(a);
			var strAssemblyName = a.GetName().Name;
			var lvi = new ListViewItem
			{
			    Text = strAssemblyName,
			    Tag = strAssemblyName
			};
		    if (strAssemblyName == this._callingAssemblyName)
			{
				lvi.Text += " (calling)";
			}
			if (strAssemblyName == this._executingAssemblyName)
			{
				lvi.Text += " (executing)";
			}
			if (strAssemblyName == this._entryAssemblyName)
			{
				lvi.Text += " (entry)";
			}
			lvi.SubItems.Add(nvc["version"]);
			lvi.SubItems.Add(nvc["builddate"]);
			lvi.SubItems.Add(nvc["codebase"]);
			this.AssemblyInfoListView.Items.Add(lvi);
			this.AssemblyNamesComboBox.Items.Add(strAssemblyName);
		}

		private string EntryAssemblyAttrib(string strName)
		{
		    if (this._entryAssemblyAttribCollection[strName] == null)
			{
				return "<Assembly: Assembly" + strName + "(\"\")>";
			}
		    return this._entryAssemblyAttribCollection[strName];
		}

	    private void PopulateLabels()
		{
			this._entryAssemblyAttribCollection = this.AssemblyAttribs(this._entryAssembly);
			if (Owner == null)
			{
				this.ImagePictureBox.Visible = false;
				this.AppTitleLabel.Left = this.AppCopyrightLabel.Left;
				this.AppDescriptionLabel.Left = this.AppCopyrightLabel.Left;
			}
			else
			{
				Icon = Owner.Icon;
				this.ImagePictureBox.Image = Icon.ToBitmap();
			}
			Text = this.ReplaceTokens(Text);
			this.AppTitleLabel.Text = this.ReplaceTokens(this.AppTitleLabel.Text);
			if (this.AppDescriptionLabel.Visible)
			{
				this.AppDescriptionLabel.Text = this.ReplaceTokens(this.AppDescriptionLabel.Text);
			}
			if (this.AppCopyrightLabel.Visible)
			{
				this.AppCopyrightLabel.Text = this.ReplaceTokens(this.AppCopyrightLabel.Text);
			}
			if (this.AppVersionLabel.Visible)
			{
				this.AppVersionLabel.Text = this.ReplaceTokens(this.AppVersionLabel.Text);
			}
			if (this.AppDateLabel.Visible)
			{
				this.AppDateLabel.Text = this.ReplaceTokens(this.AppDateLabel.Text);
			}
			if (this.MoreRichTextBox.Visible)
			{
				this.MoreRichTextBox.Text = this.ReplaceTokens(this.MoreRichTextBox.Text);
			}
		}

		private string ReplaceTokens(string s)
		{
			s = s.Replace("%title%", this.EntryAssemblyAttrib("title"));
			s = s.Replace("%copyright%", this.EntryAssemblyAttrib("copyright"));
			s = s.Replace("%description%", this.EntryAssemblyAttrib("description"));
			s = s.Replace("%company%", this.EntryAssemblyAttrib("company"));
			s = s.Replace("%product%", this.EntryAssemblyAttrib("product"));
			s = s.Replace("%trademark%", this.EntryAssemblyAttrib("trademark"));
			s = s.Replace("%year%", DateTime.Now.Year.ToString(CultureInfo.InvariantCulture));
			s = s.Replace("%version%", this.EntryAssemblyAttrib("version"));
			s = s.Replace("%builddate%", this.EntryAssemblyAttrib("builddate"));
			return s;
		}

		private void PopulateAssemblyDetails(Assembly a, ListView lvw)
		{
			lvw.Items.Clear();
			Populate(lvw, "Image Runtime Version", a.ImageRuntimeVersion);
			Populate(lvw, "Loaded from GAC", a.GlobalAssemblyCache.ToString());
			NameValueCollection nvc = this.AssemblyAttribs(a);
			foreach (string strKey in nvc)
			{
				Populate(lvw, strKey, nvc[strKey]);
			}
		}

		private static Assembly MatchAssemblyByName(string assemblyName)
		{
		    return AppDomain.CurrentDomain.GetAssemblies().FirstOrDefault(a => a.GetName().Name == assemblyName);
		}

	    private void AboutBoxLoad(object sender, EventArgs e)
		{
			if (this._entryAssembly == null)
			{
				this._entryAssembly = Assembly.GetEntryAssembly();
			}
			if (this._entryAssembly == null)
			{
				this._entryAssembly = Assembly.GetExecutingAssembly();
			}
			this._executingAssemblyName = Assembly.GetExecutingAssembly().GetName().Name;
			this._callingAssemblyName = Assembly.GetCallingAssembly().GetName().Name;
			try
			{
				this._entryAssemblyName = Assembly.GetEntryAssembly().GetName().Name;
			}
			catch (Exception)
			{
			}
			this._minWindowHeight = this.AppCopyrightLabel.Top + this.AppCopyrightLabel.Height + this.OKButton.Height + 30;
			this.TabPanelDetails.Visible = false;
			if (!this.MoreRichTextBox.Visible)
			{
				Height = Height - this.MoreRichTextBox.Height;
			}
		}

		private void AboutBoxPaint(object sender, PaintEventArgs e)
		{
		    if (this._isPainted) return;
		    this._isPainted = true;
		    Application.DoEvents();
		    Cursor.Current = Cursors.WaitCursor;
		    this.PopulateLabels();
		    Cursor.Current = Cursors.Default;
		}

		private void DetailsButtonClick(object sender, EventArgs e)
		{
			Cursor.Current = Cursors.WaitCursor;
			this.DetailsButton.Visible = false;
			SuspendLayout();
			MaximizeBox = true;
			FormBorderStyle = FormBorderStyle.Sizable;
			SizeGripStyle = SizeGripStyle.Show;
			Size = new Size(580, Size.Height + 200);
			this.MoreRichTextBox.Visible = false;
			this.TabPanelDetails.Visible = true;
			this.SysInfoButton.Visible = true;
			this.PopulateAssemblies();
			this.PopulateAppInfo();
			CenterToParent();
			ResumeLayout();
			Cursor.Current = Cursors.Default;
		}

		private void SysInfoButtonClick(object sender, EventArgs e)
		{
			this.ShowSysInfo();
		}

		private void AssemblyInfoListViewDoubleClick(object sender, EventArgs e)
		{
			string strAssemblyName;
			if (this.AssemblyInfoListView.SelectedItems.Count > 0)
			{
				strAssemblyName = Convert.ToString(this.AssemblyInfoListView.SelectedItems[0].Tag);
				this.AssemblyNamesComboBox.SelectedIndex = this.AssemblyNamesComboBox.FindStringExact(strAssemblyName);
				this.TabPanelDetails.SelectedTab = this.TabPageAssemblyDetails;
			}
		}

		private void AssemblyNamesComboBoxSelectedIndexChanged(object sender, EventArgs e)
		{
			var strAssemblyName = Convert.ToString(this.AssemblyNamesComboBox.SelectedItem);
			this.PopulateAssemblyDetails(MatchAssemblyByName(strAssemblyName), this.AssemblyDetailsListView);
		}

		private void AssemblyInfoListViewColumnClick(object sender, ColumnClickEventArgs e)
		{
			int intTargetCol = e.Column + 1;

			if (this.AssemblyInfoListView.Tag != null)
			{
				if (Math.Abs(Convert.ToInt32(this.AssemblyInfoListView.Tag)) == intTargetCol)
				{
					intTargetCol = -Convert.ToInt32(this.AssemblyInfoListView.Tag);
				}
			}
			this.AssemblyInfoListView.Tag = intTargetCol;
			this.AssemblyInfoListView.ListViewItemSorter = new ListViewItemComparer(intTargetCol, true);
		}

		private void MoreRichTextBoxLinkClicked(object sender, LinkClickedEventArgs e)
		{
			try
			{
				Process.Start(e.LinkText);
			}
			catch (Exception)
			{
			}
		}

        private void TabPanelDetailsSelectedIndexChanged(object sender, EventArgs e)
        {
            if (this.TabPanelDetails.SelectedTab == this.TabPageAssemblyDetails)
                this.AssemblyNamesComboBox.Focus();
        }

        #endregion

        /// <summary>
        /// Class used for comparing <see cref="ListViewItem"/> objects. 
        /// </summary>
		class ListViewItemComparer : IComparer
        {
            #region Private Fields

            private readonly int _intCol;
			private readonly bool _isAscending = true;

            #endregion

            #region Constructor

            /// <summary>
            /// Default constructor
            /// </summary>
			public ListViewItemComparer()
			{
				this._intCol = 0;
				this._isAscending = true;
			}

            /// <summary>
            /// Default constructor
            /// </summary>
            /// <param name="column">Column index</param>
            /// <param name="ascending">Flag if sort method should be ascending or descending</param>
			public ListViewItemComparer(int column, bool ascending)
            {
                this._isAscending = column >= 0 && @ascending;
                this._intCol = Math.Abs(column) - 1;
            }

            #endregion

            /// <summary>
            /// Compares to objects and returns the result of the comparison.
            /// </summary>
            /// <param name="x">First object to compare</param>
            /// <param name="y">Second object to compare.</param>
            /// <returns>Result of comparison.</returns>
            public int Compare(object x, object y)
			{
				var intResult = String.CompareOrdinal(((ListViewItem)x).SubItems[this._intCol].Text, 
                    ((ListViewItem)y).SubItems[this._intCol].Text);
                return (this._isAscending) ? intResult : -intResult;
			}
		}
	}
}