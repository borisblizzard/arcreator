﻿namespace ARCed.Controls
{
	partial class SearchControl
	{
		/// <summary> 
		/// Variable nécessaire au concepteur.
		/// </summary>
		private System.ComponentModel.IContainer components = null;

		/// <summary> 
		/// Nettoyage des ressources utilisées.
		/// </summary>
		/// <param name="disposing">true si les ressources managées doivent être supprimées ; sinon, false.</param>
		protected override void Dispose(bool disposing)
		{
			if (disposing && (components != null))
			{
				components.Dispose();
			}
			base.Dispose(disposing);
		}

		#region Code généré par le Concepteur de composants

		/// <summary> 
		/// Méthode requise pour la prise en charge du concepteur - ne modifiez pas 
		/// le contenu de cette méthode avec l'éditeur de code.
		/// </summary>
		private void InitializeComponent()
		{
			this.listViewResults = new System.Windows.Forms.ListView();
			this.columnHeaderTitle = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
			this.columnHeaderLineNumber = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
			this.columnHeaderLineText = ((System.Windows.Forms.ColumnHeader)(new System.Windows.Forms.ColumnHeader()));
			this.label_Statistics = new System.Windows.Forms.Label();
			this.toolStripLabel1 = new System.Windows.Forms.ToolStripLabel();
			this.textBoxSearch = new System.Windows.Forms.ToolStripTextBox();
			this.toolStripLabel3 = new System.Windows.Forms.ToolStripLabel();
			this.toolStripComboBox_Scope = new System.Windows.Forms.ToolStripComboBox();
			this.toolStripDropDownButton_Options = new System.Windows.Forms.ToolStripDropDownButton();
			this.toolStripMenuItem_RegExp = new System.Windows.Forms.ToolStripMenuItem();
			this.toolStripMenuItem_MatchCase = new System.Windows.Forms.ToolStripMenuItem();
			this.toolStripMenuItem_WholeWord = new System.Windows.Forms.ToolStripMenuItem();
			this.toolStripMenuItem_WordStart = new System.Windows.Forms.ToolStripMenuItem();
			this.buttonSearch = new System.Windows.Forms.ToolStripButton();
			this.toolStrip1 = new System.Windows.Forms.ToolStrip();
			this.toolStrip1.SuspendLayout();
			this.SuspendLayout();
			// 
			// listViewResults
			// 
			this.listViewResults.Anchor = ((System.Windows.Forms.AnchorStyles)((((System.Windows.Forms.AnchorStyles.Top | System.Windows.Forms.AnchorStyles.Bottom)
						| System.Windows.Forms.AnchorStyles.Left)
						| System.Windows.Forms.AnchorStyles.Right)));
			this.listViewResults.Columns.AddRange(new System.Windows.Forms.ColumnHeader[] {
            this.columnHeaderTitle,
            this.columnHeaderLineNumber,
            this.columnHeaderLineText});
			this.listViewResults.FullRowSelect = true;
			this.listViewResults.GridLines = true;
			this.listViewResults.HeaderStyle = System.Windows.Forms.ColumnHeaderStyle.Nonclickable;
			this.listViewResults.Location = new System.Drawing.Point(3, 28);
			this.listViewResults.MultiSelect = false;
			this.listViewResults.Name = "listViewResults";
			this.listViewResults.Size = new System.Drawing.Size(530, 147);
			this.listViewResults.TabIndex = 5;
			this.listViewResults.UseCompatibleStateImageBehavior = false;
			this.listViewResults.View = System.Windows.Forms.View.Details;
			// 
			// columnHeaderTitle
			// 
			this.columnHeaderTitle.Text = "Script";
			this.columnHeaderTitle.Width = 147;
			// 
			// columnHeaderLineNumber
			// 
			this.columnHeaderLineNumber.Text = "Line #";
			this.columnHeaderLineNumber.Width = 73;
			// 
			// columnHeaderLineText
			// 
			this.columnHeaderLineText.Text = "Text";
			this.columnHeaderLineText.Width = 278;
			// 
			// label_Statistics
			// 
			this.label_Statistics.Anchor = ((System.Windows.Forms.AnchorStyles)((System.Windows.Forms.AnchorStyles.Bottom | System.Windows.Forms.AnchorStyles.Left)));
			this.label_Statistics.AutoSize = true;
			this.label_Statistics.Location = new System.Drawing.Point(3, 178);
			this.label_Statistics.Name = "label_Statistics";
			this.label_Statistics.Size = new System.Drawing.Size(0, 13);
			this.label_Statistics.TabIndex = 10;
			// 
			// toolStripLabel1
			// 
			this.toolStripLabel1.Name = "toolStripLabel1";
			this.toolStripLabel1.Size = new System.Drawing.Size(33, 22);
			this.toolStripLabel1.Text = "Find:";
			// 
			// textBoxSearch
			// 
			this.textBoxSearch.Name = "textBoxSearch";
			this.textBoxSearch.Size = new System.Drawing.Size(100, 25);
			this.textBoxSearch.KeyDown += new System.Windows.Forms.KeyEventHandler(this.toolStripTextBox_SearchString_KeyDown);
			// 
			// toolStripLabel3
			// 
			this.toolStripLabel3.Margin = new System.Windows.Forms.Padding(16, 1, 0, 2);
			this.toolStripLabel3.Name = "toolStripLabel3";
			this.toolStripLabel3.Size = new System.Drawing.Size(20, 22);
			this.toolStripLabel3.Text = "In:";
			// 
			// toolStripComboBox_Scope
			// 
			this.toolStripComboBox_Scope.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
			this.toolStripComboBox_Scope.Items.AddRange(new object[] {
            "Open Scripts",
            "All Scripts"});
			this.toolStripComboBox_Scope.Name = "toolStripComboBox_Scope";
			this.toolStripComboBox_Scope.Size = new System.Drawing.Size(100, 25);
			// 
			// toolStripDropDownButton_Options
			// 
			this.toolStripDropDownButton_Options.DropDownItems.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolStripMenuItem_RegExp,
            this.toolStripMenuItem_MatchCase,
            this.toolStripMenuItem_WholeWord,
            this.toolStripMenuItem_WordStart});
			this.toolStripDropDownButton_Options.ImageTransparentColor = System.Drawing.Color.Magenta;
			this.toolStripDropDownButton_Options.Margin = new System.Windows.Forms.Padding(16, 1, 0, 2);
			this.toolStripDropDownButton_Options.Name = "toolStripDropDownButton_Options";
			this.toolStripDropDownButton_Options.Size = new System.Drawing.Size(62, 22);
			this.toolStripDropDownButton_Options.Text = "Options";
			// 
			// toolStripMenuItem_RegExp
			// 
			this.toolStripMenuItem_RegExp.CheckOnClick = true;
			this.toolStripMenuItem_RegExp.Name = "toolStripMenuItem_RegExp";
			this.toolStripMenuItem_RegExp.Size = new System.Drawing.Size(152, 22);
			this.toolStripMenuItem_RegExp.Text = "RegExp";
			this.toolStripMenuItem_RegExp.Click += new System.EventHandler(this.toolStripMenuItem_OptionsItem_Click);
			// 
			// toolStripMenuItem_MatchCase
			// 
			this.toolStripMenuItem_MatchCase.CheckOnClick = true;
			this.toolStripMenuItem_MatchCase.Name = "toolStripMenuItem_MatchCase";
			this.toolStripMenuItem_MatchCase.Size = new System.Drawing.Size(152, 22);
			this.toolStripMenuItem_MatchCase.Text = "Match Case";
			this.toolStripMenuItem_MatchCase.Click += new System.EventHandler(this.toolStripMenuItem_OptionsItem_Click);
			// 
			// toolStripMenuItem_WholeWord
			// 
			this.toolStripMenuItem_WholeWord.CheckOnClick = true;
			this.toolStripMenuItem_WholeWord.Name = "toolStripMenuItem_WholeWord";
			this.toolStripMenuItem_WholeWord.Size = new System.Drawing.Size(152, 22);
			this.toolStripMenuItem_WholeWord.Text = "Whole Word";
			this.toolStripMenuItem_WholeWord.Click += new System.EventHandler(this.toolStripMenuItem_OptionsItem_Click);
			// 
			// toolStripMenuItem_WordStart
			// 
			this.toolStripMenuItem_WordStart.CheckOnClick = true;
			this.toolStripMenuItem_WordStart.Name = "toolStripMenuItem_WordStart";
			this.toolStripMenuItem_WordStart.Size = new System.Drawing.Size(152, 22);
			this.toolStripMenuItem_WordStart.Text = "Word Start";
			this.toolStripMenuItem_WordStart.Click += new System.EventHandler(this.toolStripMenuItem_OptionsItem_Click);
			// 
			// buttonSearch
			// 
			this.buttonSearch.Image = global::ARCed.Properties.Resources.Find3;
			this.buttonSearch.ImageTransparentColor = System.Drawing.Color.Magenta;
			this.buttonSearch.Margin = new System.Windows.Forms.Padding(16, 1, 0, 2);
			this.buttonSearch.Name = "buttonSearch";
			this.buttonSearch.Overflow = System.Windows.Forms.ToolStripItemOverflow.Never;
			this.buttonSearch.Size = new System.Drawing.Size(65, 22);
			this.buttonSearch.Text = "Search!";
			// 
			// toolStrip1
			// 
			this.toolStrip1.GripStyle = System.Windows.Forms.ToolStripGripStyle.Hidden;
			this.toolStrip1.Items.AddRange(new System.Windows.Forms.ToolStripItem[] {
            this.toolStripLabel1,
            this.textBoxSearch,
            this.toolStripLabel3,
            this.toolStripComboBox_Scope,
            this.toolStripDropDownButton_Options,
            this.buttonSearch});
			this.toolStrip1.Location = new System.Drawing.Point(0, 0);
			this.toolStrip1.Name = "toolStrip1";
			this.toolStrip1.RenderMode = System.Windows.Forms.ToolStripRenderMode.System;
			this.toolStrip1.Size = new System.Drawing.Size(536, 25);
			this.toolStrip1.TabIndex = 9;
			this.toolStrip1.Text = "toolStrip1";
			// 
			// SearchControl
			// 
			this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
			this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
			this.Controls.Add(this.label_Statistics);
			this.Controls.Add(this.toolStrip1);
			this.Controls.Add(this.listViewResults);
			this.Name = "SearchControl";
			this.Size = new System.Drawing.Size(536, 191);
			this.toolStrip1.ResumeLayout(false);
			this.toolStrip1.PerformLayout();
			this.ResumeLayout(false);
			this.PerformLayout();

		}

		#endregion

		private System.Windows.Forms.ColumnHeader columnHeaderTitle;
		private System.Windows.Forms.ColumnHeader columnHeaderLineNumber;
		private System.Windows.Forms.ColumnHeader columnHeaderLineText;
		private System.Windows.Forms.ToolStripLabel toolStripLabel1;
		private System.Windows.Forms.ToolStripLabel toolStripLabel3;
		private System.Windows.Forms.ToolStripDropDownButton toolStripDropDownButton_Options;
		private System.Windows.Forms.ToolStrip toolStrip1;
		public System.Windows.Forms.ToolStripButton buttonSearch;
		public System.Windows.Forms.ToolStripMenuItem toolStripMenuItem_RegExp;
		public System.Windows.Forms.ToolStripMenuItem toolStripMenuItem_MatchCase;
		public System.Windows.Forms.ToolStripMenuItem toolStripMenuItem_WholeWord;
		public System.Windows.Forms.ToolStripMenuItem toolStripMenuItem_WordStart;
		public System.Windows.Forms.ToolStripComboBox toolStripComboBox_Scope;
		public System.Windows.Forms.ToolStripTextBox textBoxSearch;
		public System.Windows.Forms.Label label_Statistics;
		public System.Windows.Forms.ListView listViewResults;
	}
}
