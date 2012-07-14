namespace ARCed.Controls
{
	partial class BattleTestActorPanel
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
			System.Windows.Forms.ListViewItem listViewItem1 = new System.Windows.Forms.ListViewItem(new string[] {
            "MaxHP",
            ""}, -1);
			System.Windows.Forms.ListViewItem listViewItem2 = new System.Windows.Forms.ListViewItem(new string[] {
            "MaxSP",
            ""}, -1);
			System.Windows.Forms.ListViewItem listViewItem3 = new System.Windows.Forms.ListViewItem(new string[] {
            "STR",
            ""}, -1);
			System.Windows.Forms.ListViewItem listViewItem4 = new System.Windows.Forms.ListViewItem(new string[] {
            "DEX",
            ""}, -1);
			System.Windows.Forms.ListViewItem listViewItem5 = new System.Windows.Forms.ListViewItem(new string[] {
            "AGI",
            ""}, -1);
			System.Windows.Forms.ListViewItem listViewItem6 = new System.Windows.Forms.ListViewItem(new string[] {
            "INT",
            ""}, -1);
			System.Windows.Forms.ListViewItem listViewItem7 = new System.Windows.Forms.ListViewItem(new string[] {
            "ATK",
            ""}, -1);
			System.Windows.Forms.ListViewItem listViewItem8 = new System.Windows.Forms.ListViewItem(new string[] {
            "PDEF",
            ""}, -1);
			System.Windows.Forms.ListViewItem listViewItem9 = new System.Windows.Forms.ListViewItem(new string[] {
            "MDEF",
            ""}, -1);
			this.labelActor = new System.Windows.Forms.Label();
			this.comboBoxActor = new System.Windows.Forms.ComboBox();
			this.labelLevel = new System.Windows.Forms.Label();
			this.numericUpDownLevel = new System.Windows.Forms.NumericUpDown();
			this.groupBoxEquipment = new System.Windows.Forms.GroupBox();
			this.groupBoxStatus = new System.Windows.Forms.GroupBox();
			this.listViewStatus = new System.Windows.Forms.ListView();
			this.columnHeaderLabel = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
			this.columnHeaderValue = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
			this.buttonInitialize = new System.Windows.Forms.Button();
			((System.ComponentModel.ISupportInitialize)(this.numericUpDownLevel)).BeginInit();
			this.groupBoxStatus.SuspendLayout();
			this.SuspendLayout();
			// 
			// labelActor
			// 
			this.labelActor.AutoSize = true;
			this.labelActor.Location = new System.Drawing.Point(3, 9);
			this.labelActor.Name = "labelActor";
			this.labelActor.Size = new System.Drawing.Size(35, 13);
			this.labelActor.TabIndex = 0;
			this.labelActor.Text = "Actor:";
			// 
			// comboBoxActor
			// 
			this.comboBoxActor.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.comboBoxActor.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.comboBoxActor.FormattingEnabled = true;
			this.comboBoxActor.Location = new System.Drawing.Point(6, 25);
			this.comboBoxActor.Name = "comboBoxActor";
			this.comboBoxActor.Size = new System.Drawing.Size(183, 21);
			this.comboBoxActor.TabIndex = 1;
			// 
			// labelLevel
			// 
			this.labelLevel.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.labelLevel.AutoSize = true;
			this.labelLevel.Location = new System.Drawing.Point(192, 9);
			this.labelLevel.Name = "labelLevel";
			this.labelLevel.Size = new System.Drawing.Size(36, 13);
			this.labelLevel.TabIndex = 2;
			this.labelLevel.Text = "Level:";
			// 
			// numericUpDownLevel
			// 
			this.numericUpDownLevel.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Right)));
			this.numericUpDownLevel.Location = new System.Drawing.Point(195, 25);
			this.numericUpDownLevel.Maximum = new decimal(new int[] {
            999,
            0,
            0,
            0});
			this.numericUpDownLevel.Minimum = new decimal(new int[] {
            1,
            0,
            0,
            0});
			this.numericUpDownLevel.Name = "numericUpDownLevel";
			this.numericUpDownLevel.Size = new System.Drawing.Size(60, 20);
			this.numericUpDownLevel.TabIndex = 3;
			this.numericUpDownLevel.Value = new decimal(new int[] {
            1,
            0,
            0,
            0});
			// 
			// groupBoxEquipment
			// 
			this.groupBoxEquipment.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.groupBoxEquipment.Location = new System.Drawing.Point(6, 52);
			this.groupBoxEquipment.Name = "groupBoxEquipment";
			this.groupBoxEquipment.Size = new System.Drawing.Size(249, 196);
			this.groupBoxEquipment.TabIndex = 4;
			this.groupBoxEquipment.TabStop = false;
			this.groupBoxEquipment.Text = "Equipment";
			// 
			// groupBoxStatus
			// 
			this.groupBoxStatus.Anchor = ((System.Windows.Forms.AnchorStyles)(((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.groupBoxStatus.Controls.Add(this.listViewStatus);
			this.groupBoxStatus.Location = new System.Drawing.Point(261, 9);
			this.groupBoxStatus.Name = "groupBoxStatus";
			this.groupBoxStatus.Size = new System.Drawing.Size(111, 210);
			this.groupBoxStatus.TabIndex = 5;
			this.groupBoxStatus.TabStop = false;
			this.groupBoxStatus.Text = "Status";
			// 
			// listViewStatus
			// 
			this.listViewStatus.BorderStyle = System.Windows.Forms.BorderStyle.None;
			this.listViewStatus.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.columnHeaderLabel,
            this.columnHeaderValue});
			this.listViewStatus.Dock = System.Windows.Forms.DockStyle.Fill;
			this.listViewStatus.FullRowSelect = true;
			this.listViewStatus.HeaderStyle = System.Windows.Forms.ColumnHeaderStyle.None;
			this.listViewStatus.Items.AddRange(new System.Windows.Forms.ListViewItem[] {
            listViewItem1,
            listViewItem2,
            listViewItem3,
            listViewItem4,
            listViewItem5,
            listViewItem6,
            listViewItem7,
            listViewItem8,
            listViewItem9});
			this.listViewStatus.LabelWrap = false;
			this.listViewStatus.Location = new System.Drawing.Point(3, 16);
			this.listViewStatus.MultiSelect = false;
			this.listViewStatus.Name = "listViewStatus";
			this.listViewStatus.Scrollable = false;
			this.listViewStatus.Size = new System.Drawing.Size(105, 191);
			this.listViewStatus.TabIndex = 0;
			this.listViewStatus.UseCompatibleStateImageBehavior = false;
			this.listViewStatus.View = System.Windows.Forms.View.Details;
			// 
			// columnHeaderLabel
			// 
			this.columnHeaderLabel.Text = "";
			this.columnHeaderLabel.Width = 47;
			// 
			// columnHeaderValue
			// 
			this.columnHeaderValue.Text = "";
			this.columnHeaderValue.TextAlign = System.Windows.Forms.HorizontalAlignment.Right;
			this.columnHeaderValue.Width = 46;
			// 
			// buttonInitialize
			// 
			this.buttonInitialize.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Right)));
			this.buttonInitialize.Location = new System.Drawing.Point(261, 225);
			this.buttonInitialize.Name = "buttonInitialize";
			this.buttonInitialize.Size = new System.Drawing.Size(111, 23);
			this.buttonInitialize.TabIndex = 6;
			this.buttonInitialize.Text = "Initialize";
			this.buttonInitialize.UseVisualStyleBackColor = true;
			// 
			// BattleTestActorPanel
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.BackColor = System.Drawing.SystemColors.Window;
			this.Controls.Add(this.buttonInitialize);
			this.Controls.Add(this.groupBoxStatus);
			this.Controls.Add(this.groupBoxEquipment);
			this.Controls.Add(this.numericUpDownLevel);
			this.Controls.Add(this.labelLevel);
			this.Controls.Add(this.comboBoxActor);
			this.Controls.Add(this.labelActor);
			this.Name = "BattleTestActorPanel";
			this.Size = new System.Drawing.Size(375, 256);
			((System.ComponentModel.ISupportInitialize)(this.numericUpDownLevel)).EndInit();
			this.groupBoxStatus.ResumeLayout(false);
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.Label labelActor;
		private System.Windows.Forms.ComboBox comboBoxActor;
		private System.Windows.Forms.Label labelLevel;
		private System.Windows.Forms.NumericUpDown numericUpDownLevel;
		private System.Windows.Forms.GroupBox groupBoxEquipment;
		private System.Windows.Forms.GroupBox groupBoxStatus;
		private System.Windows.Forms.Button buttonInitialize;
		private System.Windows.Forms.ListView listViewStatus;
		private System.Windows.Forms.ColumnHeader columnHeaderLabel;
		private System.Windows.Forms.ColumnHeader columnHeaderValue;
	}
}
