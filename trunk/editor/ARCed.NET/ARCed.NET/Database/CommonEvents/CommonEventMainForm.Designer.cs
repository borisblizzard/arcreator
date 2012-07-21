namespace ARCed.Database.CommonEvents
{
	sealed partial class CommonEventMainForm
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
			this.splitContainerMain = new System.Windows.Forms.SplitContainer();
			this.dataObjectList = new ARCed.Controls.DatabaseObjectListBox();
			this.splitContainerTop = new System.Windows.Forms.SplitContainer();
			this.labelName = new System.Windows.Forms.Label();
			this.textBoxName = new System.Windows.Forms.TextBox();
			this.splitContainerTopRight = new System.Windows.Forms.SplitContainer();
			this.labelTrigger = new System.Windows.Forms.Label();
			this.comboBoxTrigger = new System.Windows.Forms.ComboBox();
			this.comboBoxCondition = new System.Windows.Forms.ComboBox();
			this.labelCondition = new System.Windows.Forms.Label();
			this.groupBoxEvents = new System.Windows.Forms.GroupBox();
			this.eventTextBox = new ARCed.Controls.EventTextBox();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerMain)).BeginInit();
			this.splitContainerMain.Panel1.SuspendLayout();
			this.splitContainerMain.Panel2.SuspendLayout();
			this.splitContainerMain.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerTop)).BeginInit();
			this.splitContainerTop.Panel1.SuspendLayout();
			this.splitContainerTop.Panel2.SuspendLayout();
			this.splitContainerTop.SuspendLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerTopRight)).BeginInit();
			this.splitContainerTopRight.Panel1.SuspendLayout();
			this.splitContainerTopRight.Panel2.SuspendLayout();
			this.splitContainerTopRight.SuspendLayout();
			this.groupBoxEvents.SuspendLayout();
			this.SuspendLayout();
			// 
			// splitContainerMain
			// 
			this.splitContainerMain.Dock = System.Windows.Forms.DockStyle.Fill;
			this.splitContainerMain.Location = new System.Drawing.Point(0, 0);
			this.splitContainerMain.Name = "splitContainerMain";
			// 
			// splitContainerMain.Panel1
			// 
			this.splitContainerMain.Panel1.Controls.Add(this.dataObjectList);
			// 
			// splitContainerMain.Panel2
			// 
			this.splitContainerMain.Panel2.Controls.Add(this.splitContainerTop);
			this.splitContainerMain.Panel2.Controls.Add(this.groupBoxEvents);
			this.splitContainerMain.Size = new System.Drawing.Size(784, 562);
			this.splitContainerMain.SplitterDistance = 204;
			this.splitContainerMain.TabIndex = 0;
			// 
			// dataObjectList
			// 
			this.dataObjectList.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.dataObjectList.HeaderText = "Common Events";
			this.dataObjectList.Location = new System.Drawing.Point(3, 3);
			this.dataObjectList.Name = "dataObjectList";
			this.dataObjectList.SelectedIndex = -1;
			this.dataObjectList.Size = new System.Drawing.Size(198, 556);
			this.dataObjectList.TabIndex = 0;
			this.dataObjectList.TabStop = false;
			this.dataObjectList.OnListBoxIndexChanged += new ARCed.Controls.DatabaseObjectListBox.ObjectListIndexChangedEventHandler(this.DataObjectListIndexChanged);
			// 
			// splitContainerTop
			// 
			this.splitContainerTop.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.splitContainerTop.Location = new System.Drawing.Point(6, 3);
			this.splitContainerTop.Name = "splitContainerTop";
			// 
			// splitContainerTop.Panel1
			// 
			this.splitContainerTop.Panel1.Controls.Add(this.labelName);
			this.splitContainerTop.Panel1.Controls.Add(this.textBoxName);
			// 
			// splitContainerTop.Panel2
			// 
			this.splitContainerTop.Panel2.Controls.Add(this.splitContainerTopRight);
			this.splitContainerTop.Size = new System.Drawing.Size(567, 50);
			this.splitContainerTop.SplitterDistance = 214;
			this.splitContainerTop.TabIndex = 6;
			// 
			// labelName
			// 
			this.labelName.AutoSize = true;
			this.labelName.Location = new System.Drawing.Point(3, 6);
			this.labelName.Name = "labelName";
			this.labelName.Size = new System.Drawing.Size(38, 13);
			this.labelName.TabIndex = 0;
			this.labelName.Text = "Name:";
			// 
			// textBoxName
			// 
			this.textBoxName.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.textBoxName.Location = new System.Drawing.Point(6, 22);
			this.textBoxName.Name = "textBoxName";
			this.textBoxName.Size = new System.Drawing.Size(205, 20);
			this.textBoxName.TabIndex = 3;
			// 
			// splitContainerTopRight
			// 
			this.splitContainerTopRight.Dock = System.Windows.Forms.DockStyle.Fill;
			this.splitContainerTopRight.Location = new System.Drawing.Point(0, 0);
			this.splitContainerTopRight.Name = "splitContainerTopRight";
			// 
			// splitContainerTopRight.Panel1
			// 
			this.splitContainerTopRight.Panel1.Controls.Add(this.labelTrigger);
			this.splitContainerTopRight.Panel1.Controls.Add(this.comboBoxTrigger);
			// 
			// splitContainerTopRight.Panel2
			// 
			this.splitContainerTopRight.Panel2.Controls.Add(this.comboBoxCondition);
			this.splitContainerTopRight.Panel2.Controls.Add(this.labelCondition);
			this.splitContainerTopRight.Size = new System.Drawing.Size(349, 50);
			this.splitContainerTopRight.SplitterDistance = 141;
			this.splitContainerTopRight.TabIndex = 0;
			// 
			// labelTrigger
			// 
			this.labelTrigger.AutoSize = true;
			this.labelTrigger.Location = new System.Drawing.Point(3, 6);
			this.labelTrigger.Name = "labelTrigger";
			this.labelTrigger.Size = new System.Drawing.Size(43, 13);
			this.labelTrigger.TabIndex = 1;
			this.labelTrigger.Text = "Trigger:";
			// 
			// comboBoxTrigger
			// 
			this.comboBoxTrigger.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.comboBoxTrigger.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxTrigger.FormattingEnabled = true;
			this.comboBoxTrigger.Items.AddRange(new object[] {
            "<None>",
            "Autorun",
            "Parallel"});
			this.comboBoxTrigger.Location = new System.Drawing.Point(6, 22);
			this.comboBoxTrigger.Name = "comboBoxTrigger";
			this.comboBoxTrigger.Size = new System.Drawing.Size(132, 21);
			this.comboBoxTrigger.TabIndex = 4;
			this.comboBoxTrigger.SelectedIndexChanged += new System.EventHandler(this.ComboBoxTriggerSelectedIndexChanged);
			// 
			// comboBoxCondition
			// 
			this.comboBoxCondition.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.comboBoxCondition.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxCondition.FormattingEnabled = true;
			this.comboBoxCondition.Location = new System.Drawing.Point(6, 22);
			this.comboBoxCondition.Name = "comboBoxCondition";
			this.comboBoxCondition.Size = new System.Drawing.Size(195, 21);
			this.comboBoxCondition.TabIndex = 6;
			this.comboBoxCondition.SelectedIndexChanged += new System.EventHandler(this.ComboBoxConditionSelectedIndexChanged);
			// 
			// labelCondition
			// 
			this.labelCondition.AutoSize = true;
			this.labelCondition.Location = new System.Drawing.Point(3, 6);
			this.labelCondition.Name = "labelCondition";
			this.labelCondition.Size = new System.Drawing.Size(89, 13);
			this.labelCondition.TabIndex = 2;
			this.labelCondition.Text = "Condition Switch:";
			// 
			// groupBoxEvents
			// 
			this.groupBoxEvents.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.groupBoxEvents.Controls.Add(this.eventTextBox);
			this.groupBoxEvents.Location = new System.Drawing.Point(6, 51);
			this.groupBoxEvents.Name = "groupBoxEvents";
			this.groupBoxEvents.Size = new System.Drawing.Size(567, 508);
			this.groupBoxEvents.TabIndex = 5;
			this.groupBoxEvents.TabStop = false;
			this.groupBoxEvents.Text = "Event Commands";
			// 
			// eventTextBox
			// 
			this.eventTextBox.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.eventTextBox.BackColor = System.Drawing.SystemColors.Window;
			this.eventTextBox.Font = new System.Drawing.Font("Consolas", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.eventTextBox.Location = new System.Drawing.Point(6, 19);
			this.eventTextBox.Name = "eventTextBox";
			this.eventTextBox.ReadOnly = true;
			this.eventTextBox.Size = new System.Drawing.Size(552, 480);
			this.eventTextBox.TabIndex = 0;
			this.eventTextBox.Text = "";
			// 
			// CommonEventMainForm
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.ClientSize = new System.Drawing.Size(784, 562);
			this.Controls.Add(this.splitContainerMain);
			this.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
			this.Name = "CommonEventMainForm";
			this.RpgTypeName = "RPG.CommonEvent";
			this.Text = "Common Events";
			this.splitContainerMain.Panel1.ResumeLayout(false);
			this.splitContainerMain.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerMain)).EndInit();
			this.splitContainerMain.ResumeLayout(false);
			this.splitContainerTop.Panel1.ResumeLayout(false);
			this.splitContainerTop.Panel1.PerformLayout();
			this.splitContainerTop.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerTop)).EndInit();
			this.splitContainerTop.ResumeLayout(false);
			this.splitContainerTopRight.Panel1.ResumeLayout(false);
			this.splitContainerTopRight.Panel1.PerformLayout();
			this.splitContainerTopRight.Panel2.ResumeLayout(false);
			this.splitContainerTopRight.Panel2.PerformLayout();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerTopRight)).EndInit();
			this.splitContainerTopRight.ResumeLayout(false);
			this.groupBoxEvents.ResumeLayout(false);
			this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.SplitContainer splitContainerMain;
		private Controls.DatabaseObjectListBox dataObjectList;
		private System.Windows.Forms.SplitContainer splitContainerTop;
		private System.Windows.Forms.Label labelName;
		private System.Windows.Forms.TextBox textBoxName;
		private System.Windows.Forms.SplitContainer splitContainerTopRight;
		private System.Windows.Forms.Label labelTrigger;
		private System.Windows.Forms.ComboBox comboBoxTrigger;
		private System.Windows.Forms.ComboBox comboBoxCondition;
		private System.Windows.Forms.Label labelCondition;
		private System.Windows.Forms.GroupBox groupBoxEvents;
		private Controls.EventTextBox eventTextBox;
	}
}