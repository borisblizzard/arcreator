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
			InitializeComponent();
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
				return AppTitleLabel.Text;
			}
			set
			{
				AppTitleLabel.Text = value;
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
				return AppDescriptionLabel.Text;
			}
			set
			{
				if (value == "")
				{
					AppDescriptionLabel.Visible = false;
				}
				else
				{
					AppDescriptionLabel.Visible = true;
					AppDescriptionLabel.Text = value;
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
				return AppVersionLabel.Text;
			}
			set
			{
				if (value == "")
				{
					AppVersionLabel.Visible = false;
				}
				else
				{
					AppVersionLabel.Visible = true;
					AppVersionLabel.Text = value;
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
				return AppCopyrightLabel.Text;
			}
			set
			{
				if (value == "")
				{
					AppCopyrightLabel.Visible = false;
				}
				else
				{
					AppCopyrightLabel.Visible = true;
					AppCopyrightLabel.Text = value;
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
				return ImagePictureBox.Image;
			}
			set
			{
				ImagePictureBox.Image = value;
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
				return MoreRichTextBox.Text;
			}
			set
			{
				if (String.IsNullOrEmpty(value))
				{
					MoreRichTextBox.Visible = false;
				}
				else
				{
					MoreRichTextBox.Visible = true;
					MoreRichTextBox.Text = value;
				}
			}
		}

        /// <summary>
        /// Determines if the "Details" (advanced assembly details) button is shown
        /// </summary>
        public bool AppDetailsButton
        {
            get { return DetailsButton.Visible; }
            set { DetailsButton.Visible = value; }
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

		private DateTime AssemblyBuildDate(Assembly a, bool forceFileDate)
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
			Populate(AppInfoListView, "Application Name", d.SetupInformation.ApplicationName);
			Populate(AppInfoListView, "Application Base", d.SetupInformation.ApplicationBase);
			Populate(AppInfoListView, "Cache Path", d.SetupInformation.CachePath);
			Populate(AppInfoListView, "Configuration File", d.SetupInformation.ConfigurationFile);
			Populate(AppInfoListView, "Dynamic Base", d.SetupInformation.DynamicBase);
			Populate(AppInfoListView, "Friendly Name", d.FriendlyName);
			Populate(AppInfoListView, "License File", d.SetupInformation.LicenseFile);
			Populate(AppInfoListView, "private Bin Path", d.SetupInformation.PrivateBinPath);
			Populate(AppInfoListView, "Shadow Copy Directories", d.SetupInformation.ShadowCopyDirectories);
			Populate(AppInfoListView, " ", " ");
			Populate(AppInfoListView, "Entry Assembly", this._entryAssemblyName);
			Populate(AppInfoListView, "Executing Assembly", this._executingAssemblyName);
			Populate(AppInfoListView, "Calling Assembly", this._callingAssemblyName);
		}

		private void PopulateAssemblies()
		{
			foreach (Assembly a in AppDomain.CurrentDomain.GetAssemblies())
			{
				PopulateAssemblySummary(a);
			}
			AssemblyNamesComboBox.SelectedIndex = AssemblyNamesComboBox.FindStringExact(this._entryAssemblyName);
		}

		private void PopulateAssemblySummary(Assembly a)
		{
			var nvc = AssemblyAttribs(a);
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
			AssemblyInfoListView.Items.Add(lvi);
			AssemblyNamesComboBox.Items.Add(strAssemblyName);
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
			this._entryAssemblyAttribCollection = AssemblyAttribs(this._entryAssembly);
			if (Owner == null)
			{
				ImagePictureBox.Visible = false;
				AppTitleLabel.Left = AppCopyrightLabel.Left;
				AppDescriptionLabel.Left = AppCopyrightLabel.Left;
			}
			else
			{
				Icon = Owner.Icon;
				ImagePictureBox.Image = Icon.ToBitmap();
			}
			Text = ReplaceTokens(Text);
			AppTitleLabel.Text = ReplaceTokens(AppTitleLabel.Text);
			if (AppDescriptionLabel.Visible)
			{
				AppDescriptionLabel.Text = ReplaceTokens(AppDescriptionLabel.Text);
			}
			if (AppCopyrightLabel.Visible)
			{
				AppCopyrightLabel.Text = ReplaceTokens(AppCopyrightLabel.Text);
			}
			if (AppVersionLabel.Visible)
			{
				AppVersionLabel.Text = ReplaceTokens(AppVersionLabel.Text);
			}
			if (AppDateLabel.Visible)
			{
				AppDateLabel.Text = ReplaceTokens(AppDateLabel.Text);
			}
			if (MoreRichTextBox.Visible)
			{
				MoreRichTextBox.Text = ReplaceTokens(MoreRichTextBox.Text);
			}
		}

		private string ReplaceTokens(string s)
		{
			s = s.Replace("%title%", EntryAssemblyAttrib("title"));
			s = s.Replace("%copyright%", EntryAssemblyAttrib("copyright"));
			s = s.Replace("%description%", EntryAssemblyAttrib("description"));
			s = s.Replace("%company%", EntryAssemblyAttrib("company"));
			s = s.Replace("%product%", EntryAssemblyAttrib("product"));
			s = s.Replace("%trademark%", EntryAssemblyAttrib("trademark"));
			s = s.Replace("%year%", DateTime.Now.Year.ToString(CultureInfo.InvariantCulture));
			s = s.Replace("%version%", EntryAssemblyAttrib("version"));
			s = s.Replace("%builddate%", EntryAssemblyAttrib("builddate"));
			return s;
		}

		private void PopulateAssemblyDetails(Assembly a, ListView lvw)
		{
			lvw.Items.Clear();
			Populate(lvw, "Image Runtime Version", a.ImageRuntimeVersion);
			Populate(lvw, "Loaded from GAC", a.GlobalAssemblyCache.ToString());
			NameValueCollection nvc = AssemblyAttribs(a);
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
			this._minWindowHeight = AppCopyrightLabel.Top + AppCopyrightLabel.Height + OKButton.Height + 30;
			TabPanelDetails.Visible = false;
			if (!MoreRichTextBox.Visible)
			{
				Height = Height - MoreRichTextBox.Height;
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
			DetailsButton.Visible = false;
			SuspendLayout();
			MaximizeBox = true;
			FormBorderStyle = FormBorderStyle.Sizable;
			SizeGripStyle = SizeGripStyle.Show;
			Size = new Size(580, Size.Height + 200);
			MoreRichTextBox.Visible = false;
			TabPanelDetails.Visible = true;
			SysInfoButton.Visible = true;
			PopulateAssemblies();
			PopulateAppInfo();
			CenterToParent();
			ResumeLayout();
			Cursor.Current = Cursors.Default;
		}

		private void SysInfoButtonClick(object sender, EventArgs e)
		{
			ShowSysInfo();
		}

		private void AssemblyInfoListViewDoubleClick(object sender, EventArgs e)
		{
			string strAssemblyName;
			if (AssemblyInfoListView.SelectedItems.Count > 0)
			{
				strAssemblyName = Convert.ToString(AssemblyInfoListView.SelectedItems[0].Tag);
				AssemblyNamesComboBox.SelectedIndex = AssemblyNamesComboBox.FindStringExact(strAssemblyName);
				TabPanelDetails.SelectedTab = TabPageAssemblyDetails;
			}
		}

		private void AssemblyNamesComboBoxSelectedIndexChanged(object sender, EventArgs e)
		{
			var strAssemblyName = Convert.ToString(AssemblyNamesComboBox.SelectedItem);
			PopulateAssemblyDetails(MatchAssemblyByName(strAssemblyName), AssemblyDetailsListView);
		}

		private void AssemblyInfoListViewColumnClick(object sender, ColumnClickEventArgs e)
		{
			int intTargetCol = e.Column + 1;

			if (AssemblyInfoListView.Tag != null)
			{
				if (Math.Abs(Convert.ToInt32(AssemblyInfoListView.Tag)) == intTargetCol)
				{
					intTargetCol = -Convert.ToInt32(AssemblyInfoListView.Tag);
				}
			}
			AssemblyInfoListView.Tag = intTargetCol;
			AssemblyInfoListView.ListViewItemSorter = new ListViewItemComparer(intTargetCol, true);
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
            if (TabPanelDetails.SelectedTab == TabPageAssemblyDetails)
                AssemblyNamesComboBox.Focus();
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
				_intCol = 0;
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
                _intCol = Math.Abs(column) - 1;
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