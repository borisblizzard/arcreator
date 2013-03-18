namespace ARCed.Dialogs
{
	partial class NewProjectForm
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
            this.components = new System.ComponentModel.Container();
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(NewProjectForm));
            this.labelFolderName = new System.Windows.Forms.Label();
            this.labelTitle = new System.Windows.Forms.Label();
            this.textBoxFolderName = new System.Windows.Forms.TextBox();
            this.textBoxTitle = new System.Windows.Forms.TextBox();
            this.labelLocation = new System.Windows.Forms.Label();
            this.textBoxLocation = new System.Windows.Forms.TextBox();
            this.buttonBrowse = new System.Windows.Forms.Button();
            this.buttonCancel = new System.Windows.Forms.Button();
            this.buttonOK = new System.Windows.Forms.Button();
            this.labelTemplates = new System.Windows.Forms.Label();
            this.comboTemplates = new System.Windows.Forms.ComboBox();
            this.toolTip = new System.Windows.Forms.ToolTip(this.components);
            this.SuspendLayout();
            // 
            // labelFolderName
            // 
            resources.ApplyResources(this.labelFolderName, "labelFolderName");
            this.labelFolderName.Name = "labelFolderName";
            // 
            // labelTitle
            // 
            resources.ApplyResources(this.labelTitle, "labelTitle");
            this.labelTitle.Name = "labelTitle";
            // 
            // textBoxFolderName
            // 
            resources.ApplyResources(this.textBoxFolderName, "textBoxFolderName");
            this.textBoxFolderName.Name = "textBoxFolderName";
            this.toolTip.SetToolTip(this.textBoxFolderName, resources.GetString("textBoxFolderName.ToolTip"));
            this.textBoxFolderName.TextChanged += new System.EventHandler(this.TextBoxFolderNameTextChanged);
            // 
            // textBoxTitle
            // 
            resources.ApplyResources(this.textBoxTitle, "textBoxTitle");
            this.textBoxTitle.Name = "textBoxTitle";
            this.toolTip.SetToolTip(this.textBoxTitle, resources.GetString("textBoxTitle.ToolTip"));
            // 
            // labelLocation
            // 
            resources.ApplyResources(this.labelLocation, "labelLocation");
            this.labelLocation.Name = "labelLocation";
            // 
            // textBoxLocation
            // 
            resources.ApplyResources(this.textBoxLocation, "textBoxLocation");
            this.textBoxLocation.Name = "textBoxLocation";
            this.toolTip.SetToolTip(this.textBoxLocation, resources.GetString("textBoxLocation.ToolTip"));
            this.textBoxLocation.TextChanged += new System.EventHandler(this.TextBoxLocationTextChanged);
            // 
            // buttonBrowse
            // 
            this.buttonBrowse.BackgroundImage = global::ARCed.Properties.Resources.FileOpen;
            resources.ApplyResources(this.buttonBrowse, "buttonBrowse");
            this.buttonBrowse.Name = "buttonBrowse";
            this.toolTip.SetToolTip(this.buttonBrowse, resources.GetString("buttonBrowse.ToolTip"));
            this.buttonBrowse.UseVisualStyleBackColor = true;
            this.buttonBrowse.Click += new System.EventHandler(this.ButtonBrowseClick);
            // 
            // buttonCancel
            // 
            this.buttonCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
            resources.ApplyResources(this.buttonCancel, "buttonCancel");
            this.buttonCancel.Name = "buttonCancel";
            this.toolTip.SetToolTip(this.buttonCancel, resources.GetString("buttonCancel.ToolTip"));
            this.buttonCancel.UseVisualStyleBackColor = true;
            // 
            // buttonOK
            // 
            resources.ApplyResources(this.buttonOK, "buttonOK");
            this.buttonOK.Name = "buttonOK";
            this.toolTip.SetToolTip(this.buttonOK, resources.GetString("buttonOK.ToolTip"));
            this.buttonOK.UseVisualStyleBackColor = true;
            this.buttonOK.Click += new System.EventHandler(this.ButtonOkClick);
            // 
            // labelTemplates
            // 
            resources.ApplyResources(this.labelTemplates, "labelTemplates");
            this.labelTemplates.Name = "labelTemplates";
            // 
            // comboTemplates
            // 
            this.comboTemplates.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.comboTemplates.FormattingEnabled = true;
            resources.ApplyResources(this.comboTemplates, "comboTemplates");
            this.comboTemplates.Name = "comboTemplates";
            this.toolTip.SetToolTip(this.comboTemplates, resources.GetString("comboTemplates.ToolTip"));
            // 
            // NewProjectForm
            // 
            this.AcceptButton = this.buttonOK;
            this.AccessibleRole = System.Windows.Forms.AccessibleRole.Dialog;
            resources.ApplyResources(this, "$this");
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.CancelButton = this.buttonCancel;
            this.Controls.Add(this.comboTemplates);
            this.Controls.Add(this.labelTemplates);
            this.Controls.Add(this.buttonOK);
            this.Controls.Add(this.buttonCancel);
            this.Controls.Add(this.buttonBrowse);
            this.Controls.Add(this.textBoxLocation);
            this.Controls.Add(this.labelLocation);
            this.Controls.Add(this.textBoxTitle);
            this.Controls.Add(this.textBoxFolderName);
            this.Controls.Add(this.labelTitle);
            this.Controls.Add(this.labelFolderName);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedDialog;
            this.MaximizeBox = false;
            this.MinimizeBox = false;
            this.Name = "NewProjectForm";
            this.Load += new System.EventHandler(this.NewProjectFormLoad);
            this.ResumeLayout(false);
            this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.Label labelFolderName;
		private System.Windows.Forms.Label labelTitle;
		private System.Windows.Forms.TextBox textBoxFolderName;
		private System.Windows.Forms.TextBox textBoxTitle;
		private System.Windows.Forms.Label labelLocation;
		private System.Windows.Forms.TextBox textBoxLocation;
		private System.Windows.Forms.Button buttonBrowse;
		private System.Windows.Forms.Button buttonCancel;
		private System.Windows.Forms.Button buttonOK;
		private System.Windows.Forms.Label labelTemplates;
		private System.Windows.Forms.ComboBox comboTemplates;
		private System.Windows.Forms.ToolTip toolTip;
	}
}