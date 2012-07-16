﻿namespace ARCed.Dialogs
{
	partial class AboutBox
	{
		/// <summary>
		/// Required designer variable.
		/// </summary>
		private System.ComponentModel.IContainer components = null;

		/// <summary>
		/// Clean up any resources being used.
		/// </summary>
		/// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
		protected override void Dispose(bool disposing)
		{
			if (disposing && (components != null))
			{
				components.Dispose();
			}
			base.Dispose(disposing);
		}

		#region Windows Form Designer generated code

		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		private void InitializeComponent()
		{
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(AboutBox));
            this.DetailsButton = new System.Windows.Forms.Button();
            this.ImagePictureBox = new System.Windows.Forms.PictureBox();
            this.AppDateLabel = new System.Windows.Forms.Label();
            this.SysInfoButton = new System.Windows.Forms.Button();
            this.AppCopyrightLabel = new System.Windows.Forms.Label();
            this.AppVersionLabel = new System.Windows.Forms.Label();
            this.AppDescriptionLabel = new System.Windows.Forms.Label();
            this.GroupBox1 = new System.Windows.Forms.GroupBox();
            this.AppTitleLabel = new System.Windows.Forms.Label();
            this.OKButton = new System.Windows.Forms.Button();
            this.MoreRichTextBox = new System.Windows.Forms.RichTextBox();
            this.TabPanelDetails = new System.Windows.Forms.TabControl();
            this.TabPageApplication = new System.Windows.Forms.TabPage();
            this.AppInfoListView = new System.Windows.Forms.ListView();
            this.colKey = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colValue = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.TabPageAssemblies = new System.Windows.Forms.TabPage();
            this.AssemblyInfoListView = new System.Windows.Forms.ListView();
            this.colAssemblyName = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colAssemblyVersion = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colAssemblyBuilt = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.colAssemblyCodeBase = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.TabPageAssemblyDetails = new System.Windows.Forms.TabPage();
            this.AssemblyDetailsListView = new System.Windows.Forms.ListView();
            this.ColumnHeader1 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.ColumnHeader2 = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
            this.AssemblyNamesComboBox = new System.Windows.Forms.ComboBox();
            ((System.ComponentModel.ISupportInitialize)(this.ImagePictureBox)).BeginInit();
            this.TabPanelDetails.SuspendLayout();
            this.TabPageApplication.SuspendLayout();
            this.TabPageAssemblies.SuspendLayout();
            this.TabPageAssemblyDetails.SuspendLayout();
            this.SuspendLayout();
            // 
            // DetailsButton
            // 
            resources.ApplyResources(this.DetailsButton, "DetailsButton");
            this.DetailsButton.Name = "DetailsButton";
            this.DetailsButton.Click += new System.EventHandler(this.DetailsButton_Click);
            // 
            // ImagePictureBox
            // 
            resources.ApplyResources(this.ImagePictureBox, "ImagePictureBox");
            this.ImagePictureBox.Name = "ImagePictureBox";
            this.ImagePictureBox.TabStop = false;
            // 
            // AppDateLabel
            // 
            resources.ApplyResources(this.AppDateLabel, "AppDateLabel");
            this.AppDateLabel.Name = "AppDateLabel";
            // 
            // SysInfoButton
            // 
            resources.ApplyResources(this.SysInfoButton, "SysInfoButton");
            this.SysInfoButton.Name = "SysInfoButton";
            this.SysInfoButton.Click += new System.EventHandler(this.SysInfoButton_Click);
            // 
            // AppCopyrightLabel
            // 
            resources.ApplyResources(this.AppCopyrightLabel, "AppCopyrightLabel");
            this.AppCopyrightLabel.Name = "AppCopyrightLabel";
            // 
            // AppVersionLabel
            // 
            resources.ApplyResources(this.AppVersionLabel, "AppVersionLabel");
            this.AppVersionLabel.Name = "AppVersionLabel";
            // 
            // AppDescriptionLabel
            // 
            resources.ApplyResources(this.AppDescriptionLabel, "AppDescriptionLabel");
            this.AppDescriptionLabel.Name = "AppDescriptionLabel";
            // 
            // GroupBox1
            // 
            resources.ApplyResources(this.GroupBox1, "GroupBox1");
            this.GroupBox1.Name = "GroupBox1";
            this.GroupBox1.TabStop = false;
            // 
            // AppTitleLabel
            // 
            resources.ApplyResources(this.AppTitleLabel, "AppTitleLabel");
            this.AppTitleLabel.Name = "AppTitleLabel";
            // 
            // OKButton
            // 
            resources.ApplyResources(this.OKButton, "OKButton");
            this.OKButton.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            this.OKButton.Name = "OKButton";
            // 
            // MoreRichTextBox
            // 
            resources.ApplyResources(this.MoreRichTextBox, "MoreRichTextBox");
            this.MoreRichTextBox.BackColor = System.Drawing.SystemColors.ControlLight;
            this.MoreRichTextBox.Name = "MoreRichTextBox";
            this.MoreRichTextBox.ReadOnly = true;
            this.MoreRichTextBox.LinkClicked += new System.Windows.Forms.LinkClickedEventHandler(this.MoreRichTextBox_LinkClicked);
            // 
            // TabPanelDetails
            // 
            resources.ApplyResources(this.TabPanelDetails, "TabPanelDetails");
            this.TabPanelDetails.Controls.Add(this.TabPageApplication);
            this.TabPanelDetails.Controls.Add(this.TabPageAssemblies);
            this.TabPanelDetails.Controls.Add(this.TabPageAssemblyDetails);
            this.TabPanelDetails.Name = "TabPanelDetails";
            this.TabPanelDetails.SelectedIndex = 0;
            this.TabPanelDetails.SelectedIndexChanged += new System.EventHandler(this.TabPanelDetails_SelectedIndexChanged);
            // 
            // TabPageApplication
            // 
            this.TabPageApplication.Controls.Add(this.AppInfoListView);
            resources.ApplyResources(this.TabPageApplication, "TabPageApplication");
            this.TabPageApplication.Name = "TabPageApplication";
            // 
            // AppInfoListView
            // 
            this.AppInfoListView.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.colKey,
            this.colValue});
            resources.ApplyResources(this.AppInfoListView, "AppInfoListView");
            this.AppInfoListView.FullRowSelect = true;
            this.AppInfoListView.HeaderStyle = System.Windows.Forms.ColumnHeaderStyle.Nonclickable;
            this.AppInfoListView.Name = "AppInfoListView";
            this.AppInfoListView.UseCompatibleStateImageBehavior = false;
            this.AppInfoListView.View = System.Windows.Forms.View.Details;
            // 
            // colKey
            // 
            resources.ApplyResources(this.colKey, "colKey");
            // 
            // colValue
            // 
            resources.ApplyResources(this.colValue, "colValue");
            // 
            // TabPageAssemblies
            // 
            this.TabPageAssemblies.Controls.Add(this.AssemblyInfoListView);
            resources.ApplyResources(this.TabPageAssemblies, "TabPageAssemblies");
            this.TabPageAssemblies.Name = "TabPageAssemblies";
            // 
            // AssemblyInfoListView
            // 
            this.AssemblyInfoListView.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.colAssemblyName,
            this.colAssemblyVersion,
            this.colAssemblyBuilt,
            this.colAssemblyCodeBase});
            resources.ApplyResources(this.AssemblyInfoListView, "AssemblyInfoListView");
            this.AssemblyInfoListView.FullRowSelect = true;
            this.AssemblyInfoListView.MultiSelect = false;
            this.AssemblyInfoListView.Name = "AssemblyInfoListView";
            this.AssemblyInfoListView.Sorting = System.Windows.Forms.SortOrder.Ascending;
            this.AssemblyInfoListView.UseCompatibleStateImageBehavior = false;
            this.AssemblyInfoListView.View = System.Windows.Forms.View.Details;
            this.AssemblyInfoListView.ColumnClick += new System.Windows.Forms.ColumnClickEventHandler(this.AssemblyInfoListView_ColumnClick);
            this.AssemblyInfoListView.DoubleClick += new System.EventHandler(this.AssemblyInfoListView_DoubleClick);
            // 
            // colAssemblyName
            // 
            resources.ApplyResources(this.colAssemblyName, "colAssemblyName");
            // 
            // colAssemblyVersion
            // 
            resources.ApplyResources(this.colAssemblyVersion, "colAssemblyVersion");
            // 
            // colAssemblyBuilt
            // 
            resources.ApplyResources(this.colAssemblyBuilt, "colAssemblyBuilt");
            // 
            // colAssemblyCodeBase
            // 
            resources.ApplyResources(this.colAssemblyCodeBase, "colAssemblyCodeBase");
            // 
            // TabPageAssemblyDetails
            // 
            this.TabPageAssemblyDetails.Controls.Add(this.AssemblyDetailsListView);
            this.TabPageAssemblyDetails.Controls.Add(this.AssemblyNamesComboBox);
            resources.ApplyResources(this.TabPageAssemblyDetails, "TabPageAssemblyDetails");
            this.TabPageAssemblyDetails.Name = "TabPageAssemblyDetails";
            // 
            // AssemblyDetailsListView
            // 
            this.AssemblyDetailsListView.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.ColumnHeader1,
            this.ColumnHeader2});
            resources.ApplyResources(this.AssemblyDetailsListView, "AssemblyDetailsListView");
            this.AssemblyDetailsListView.FullRowSelect = true;
            this.AssemblyDetailsListView.HeaderStyle = System.Windows.Forms.ColumnHeaderStyle.Nonclickable;
            this.AssemblyDetailsListView.Name = "AssemblyDetailsListView";
            this.AssemblyDetailsListView.Sorting = System.Windows.Forms.SortOrder.Ascending;
            this.AssemblyDetailsListView.UseCompatibleStateImageBehavior = false;
            this.AssemblyDetailsListView.View = System.Windows.Forms.View.Details;
            // 
            // ColumnHeader1
            // 
            resources.ApplyResources(this.ColumnHeader1, "ColumnHeader1");
            // 
            // ColumnHeader2
            // 
            resources.ApplyResources(this.ColumnHeader2, "ColumnHeader2");
            // 
            // AssemblyNamesComboBox
            // 
            resources.ApplyResources(this.AssemblyNamesComboBox, "AssemblyNamesComboBox");
            this.AssemblyNamesComboBox.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.AssemblyNamesComboBox.Name = "AssemblyNamesComboBox";
            this.AssemblyNamesComboBox.Sorted = true;
            this.AssemblyNamesComboBox.SelectedIndexChanged += new System.EventHandler(this.AssemblyNamesComboBox_SelectedIndexChanged);
            // 
            // AboutBox
            // 
            resources.ApplyResources(this, "$this");
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.CancelButton = this.OKButton;
            this.Controls.Add(this.DetailsButton);
            this.Controls.Add(this.ImagePictureBox);
            this.Controls.Add(this.AppDateLabel);
            this.Controls.Add(this.SysInfoButton);
            this.Controls.Add(this.AppCopyrightLabel);
            this.Controls.Add(this.AppVersionLabel);
            this.Controls.Add(this.AppDescriptionLabel);
            this.Controls.Add(this.GroupBox1);
            this.Controls.Add(this.AppTitleLabel);
            this.Controls.Add(this.OKButton);
            this.Controls.Add(this.MoreRichTextBox);
            this.Controls.Add(this.TabPanelDetails);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "AboutBox";
            this.SizeGripStyle = System.Windows.Forms.SizeGripStyle.Hide;
            this.Load += new System.EventHandler(this.AboutBox_Load);
            this.Paint += new System.Windows.Forms.PaintEventHandler(this.AboutBox_Paint);
            ((System.ComponentModel.ISupportInitialize)(this.ImagePictureBox)).EndInit();
            this.TabPanelDetails.ResumeLayout(false);
            this.TabPageApplication.ResumeLayout(false);
            this.TabPageAssemblies.ResumeLayout(false);
            this.TabPageAssemblyDetails.ResumeLayout(false);
            this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.Button DetailsButton;
		private System.Windows.Forms.PictureBox ImagePictureBox;
		private System.Windows.Forms.Label AppDateLabel;
		private System.Windows.Forms.Button SysInfoButton;
		private System.Windows.Forms.Label AppCopyrightLabel;
		private System.Windows.Forms.Label AppVersionLabel;
		private System.Windows.Forms.Label AppDescriptionLabel;
		private System.Windows.Forms.GroupBox GroupBox1;
		private System.Windows.Forms.Label AppTitleLabel;
		private System.Windows.Forms.Button OKButton;
		internal System.Windows.Forms.RichTextBox MoreRichTextBox;
		internal System.Windows.Forms.TabControl TabPanelDetails;
		internal System.Windows.Forms.TabPage TabPageApplication;
		internal System.Windows.Forms.ListView AppInfoListView;
		internal System.Windows.Forms.ColumnHeader colKey;
		internal System.Windows.Forms.ColumnHeader colValue;
		internal System.Windows.Forms.TabPage TabPageAssemblies;
		internal System.Windows.Forms.ListView AssemblyInfoListView;
		internal System.Windows.Forms.ColumnHeader colAssemblyName;
		internal System.Windows.Forms.ColumnHeader colAssemblyVersion;
		internal System.Windows.Forms.ColumnHeader colAssemblyBuilt;
		internal System.Windows.Forms.ColumnHeader colAssemblyCodeBase;
		internal System.Windows.Forms.TabPage TabPageAssemblyDetails;
		internal System.Windows.Forms.ListView AssemblyDetailsListView;
		internal System.Windows.Forms.ColumnHeader ColumnHeader1;
		internal System.Windows.Forms.ColumnHeader ColumnHeader2;
		internal System.Windows.Forms.ComboBox AssemblyNamesComboBox;
	}
}