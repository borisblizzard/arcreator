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
			this.labelFolderName.AutoSize = true;
			this.labelFolderName.Location = new System.Drawing.Point(12, 9);
			this.labelFolderName.Name = "labelFolderName";
			this.labelFolderName.Size = new System.Drawing.Size(70, 13);
			this.labelFolderName.TabIndex = 0;
			this.labelFolderName.Text = "Folder Name:";
			// 
			// labelTitle
			// 
			this.labelTitle.AutoSize = true;
			this.labelTitle.Location = new System.Drawing.Point(169, 9);
			this.labelTitle.Name = "labelTitle";
			this.labelTitle.Size = new System.Drawing.Size(61, 13);
			this.labelTitle.TabIndex = 1;
			this.labelTitle.Text = "Game Title:";
			// 
			// textBoxFolderName
			// 
			this.textBoxFolderName.Location = new System.Drawing.Point(15, 25);
			this.textBoxFolderName.Name = "textBoxFolderName";
			this.textBoxFolderName.Size = new System.Drawing.Size(151, 20);
			this.textBoxFolderName.TabIndex = 0;
			this.toolTip.SetToolTip(this.textBoxFolderName, "The directory name of the project");
			this.textBoxFolderName.TextChanged += new System.EventHandler(this.textBoxFolderName_TextChanged);
			// 
			// textBoxTitle
			// 
			this.textBoxTitle.Location = new System.Drawing.Point(172, 25);
			this.textBoxTitle.Name = "textBoxTitle";
			this.textBoxTitle.Size = new System.Drawing.Size(190, 20);
			this.textBoxTitle.TabIndex = 1;
			this.toolTip.SetToolTip(this.textBoxTitle, "The title of the game");
			// 
			// labelLocation
			// 
			this.labelLocation.AutoSize = true;
			this.labelLocation.Location = new System.Drawing.Point(12, 59);
			this.labelLocation.Name = "labelLocation";
			this.labelLocation.Size = new System.Drawing.Size(51, 13);
			this.labelLocation.TabIndex = 4;
			this.labelLocation.Text = "Location:";
			// 
			// textBoxLocation
			// 
			this.textBoxLocation.Location = new System.Drawing.Point(15, 75);
			this.textBoxLocation.Name = "textBoxLocation";
			this.textBoxLocation.Size = new System.Drawing.Size(318, 20);
			this.textBoxLocation.TabIndex = 2;
			this.toolTip.SetToolTip(this.textBoxLocation, "The location of the project directory");
			this.textBoxLocation.TextChanged += new System.EventHandler(this.textBoxLocation_TextChanged);
			// 
			// buttonBrowse
			// 
			this.buttonBrowse.BackgroundImage = global::ARCed.Properties.Resources.FileOpen;
			this.buttonBrowse.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Zoom;
			this.buttonBrowse.Location = new System.Drawing.Point(339, 73);
			this.buttonBrowse.Name = "buttonBrowse";
			this.buttonBrowse.Size = new System.Drawing.Size(23, 23);
			this.buttonBrowse.TabIndex = 3;
			this.toolTip.SetToolTip(this.buttonBrowse, "Browse for a folder");
			this.buttonBrowse.UseVisualStyleBackColor = true;
			this.buttonBrowse.Click += new System.EventHandler(this.buttonBrowse_Click);
			// 
			// buttonCancel
			// 
			this.buttonCancel.DialogResult = System.Windows.Forms.DialogResult.Cancel;
			this.buttonCancel.Location = new System.Drawing.Point(287, 128);
			this.buttonCancel.Name = "buttonCancel";
			this.buttonCancel.Size = new System.Drawing.Size(75, 23);
			this.buttonCancel.TabIndex = 6;
			this.buttonCancel.Text = "Cancel";
			this.toolTip.SetToolTip(this.buttonCancel, "Cancel and return");
			this.buttonCancel.UseVisualStyleBackColor = true;
			// 
			// buttonOK
			// 
			this.buttonOK.Location = new System.Drawing.Point(206, 128);
			this.buttonOK.Name = "buttonOK";
			this.buttonOK.Size = new System.Drawing.Size(75, 23);
			this.buttonOK.TabIndex = 5;
			this.buttonOK.Text = "OK";
			this.toolTip.SetToolTip(this.buttonOK, "Confirm and create");
			this.buttonOK.UseVisualStyleBackColor = true;
			this.buttonOK.Click += new System.EventHandler(this.buttonOK_Click);
			// 
			// labelTemplates
			// 
			this.labelTemplates.AutoSize = true;
			this.labelTemplates.Location = new System.Drawing.Point(12, 109);
			this.labelTemplates.Name = "labelTemplates";
			this.labelTemplates.Size = new System.Drawing.Size(54, 13);
			this.labelTemplates.TabIndex = 9;
			this.labelTemplates.Text = "Template:";
			// 
			// comboTemplates
			// 
			this.comboTemplates.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboTemplates.FormattingEnabled = true;
			this.comboTemplates.Location = new System.Drawing.Point(15, 125);
			this.comboTemplates.Name = "comboTemplates";
			this.comboTemplates.Size = new System.Drawing.Size(151, 21);
			this.comboTemplates.TabIndex = 4;
			this.toolTip.SetToolTip(this.comboTemplates, "Choose the template for the new project");
			// 
			// NewProjectForm
			// 
			this.AcceptButton = this.buttonOK;
			this.AccessibleRole = System.Windows.Forms.AccessibleRole.Dialog;
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.CancelButton = this.buttonCancel;
			this.ClientSize = new System.Drawing.Size(374, 163);
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
			this.StartPosition = System.Windows.Forms.FormStartPosition.CenterParent;
			this.Text = "New Project";
			this.Load += new System.EventHandler(this.NewProjectForm_Load);
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