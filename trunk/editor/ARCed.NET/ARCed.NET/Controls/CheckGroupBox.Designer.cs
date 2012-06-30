namespace ARCed.Controls
{
	partial class CheckGroupBox
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

		#region Component Designer generated code

		/// <summary>
		/// Required method for Designer support - do not modify
		/// the contents of this method with the code editor.
		/// </summary>
		private void InitializeComponent()
		{
			this.buttonAll = new System.Windows.Forms.Button();
			this.buttonNone = new System.Windows.Forms.Button();
			this.splitContainerButtons = new System.Windows.Forms.SplitContainer();
			this.checkedList = new System.Windows.Forms.CheckedListBox();
			((System.ComponentModel.ISupportInitialize)(this.splitContainerButtons)).BeginInit();
			this.splitContainerButtons.Panel1.SuspendLayout();
			this.splitContainerButtons.Panel2.SuspendLayout();
			this.splitContainerButtons.SuspendLayout();
			this.SuspendLayout();
			// 
			// buttonAll
			// 
			this.buttonAll.Dock = System.Windows.Forms.DockStyle.Fill;
			this.buttonAll.Location = new System.Drawing.Point(0, 0);
			this.buttonAll.Name = "buttonAll";
			this.buttonAll.Size = new System.Drawing.Size(58, 23);
			this.buttonAll.TabIndex = 1;
			this.buttonAll.Text = "All";
			this.buttonAll.UseVisualStyleBackColor = true;
			this.buttonAll.Click += new System.EventHandler(this.buttonAll_Click);
			// 
			// buttonNone
			// 
			this.buttonNone.Dock = System.Windows.Forms.DockStyle.Fill;
			this.buttonNone.Location = new System.Drawing.Point(0, 0);
			this.buttonNone.Name = "buttonNone";
			this.buttonNone.Size = new System.Drawing.Size(54, 23);
			this.buttonNone.TabIndex = 2;
			this.buttonNone.Text = "None";
			this.buttonNone.UseVisualStyleBackColor = true;
			this.buttonNone.Click += new System.EventHandler(this.buttonNone_Click);
			// 
			// splitContainerButtons
			// 
			this.splitContainerButtons.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.splitContainerButtons.Location = new System.Drawing.Point(6, 194);
			this.splitContainerButtons.Name = "splitContainerButtons";
			// 
			// splitContainerButtons.Panel1
			// 
			this.splitContainerButtons.Panel1.Controls.Add(this.buttonAll);
			// 
			// splitContainerButtons.Panel2
			// 
			this.splitContainerButtons.Panel2.Controls.Add(this.buttonNone);
			this.splitContainerButtons.Size = new System.Drawing.Size(116, 23);
			this.splitContainerButtons.SplitterDistance = 58;
			this.splitContainerButtons.TabIndex = 0;
			// 
			// checkedList
			// 
			this.checkedList.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.checkedList.CheckOnClick = true;
			this.checkedList.FormattingEnabled = true;
			this.checkedList.IntegralHeight = false;
			this.checkedList.Location = new System.Drawing.Point(6, 19);
			this.checkedList.Name = "checkedList";
			this.checkedList.Size = new System.Drawing.Size(116, 169);
			this.checkedList.TabIndex = 1;
			this.checkedList.ItemCheck += new System.Windows.Forms.ItemCheckEventHandler(this.checkedList_ItemCheck);
			// 
			// CheckGroupBox
			// 
			this.Controls.Add(this.checkedList);
			this.Controls.Add(this.splitContainerButtons);
			this.Location = new System.Drawing.Point(19, 82);
			this.Size = new System.Drawing.Size(128, 223);
			this.Text = "CheckGroupBox";
			this.splitContainerButtons.Panel1.ResumeLayout(false);
			this.splitContainerButtons.Panel2.ResumeLayout(false);
			((System.ComponentModel.ISupportInitialize)(this.splitContainerButtons)).EndInit();
			this.splitContainerButtons.ResumeLayout(false);
			this.ResumeLayout(false);

		}

		#endregion

		private System.Windows.Forms.Button buttonAll;
		private System.Windows.Forms.Button buttonNone;
		private System.Windows.Forms.SplitContainer splitContainerButtons;
		private System.Windows.Forms.CheckedListBox checkedList;
	}
}
