#region Using Directives

using System;
using System.Collections.Generic;
using System.Drawing;
using System.Text.RegularExpressions;
using System.Windows.Forms;
using ARCed.UI;

#endregion


namespace ARCed.Scintilla
{
    public partial class FindReplaceDialog : DockContent
    {
        #region Fields

        private readonly BindingSource _bindingSourceFind = new BindingSource();
        private List<string> _mruFind;
        private readonly BindingSource _bindingSourceReplace = new BindingSource();
        private List<string> _mruReplace;
        private int _mruMaxCount = 10;
        private Scintilla _scintilla;
        private Range _searchRange;

        #endregion Fields


        #region Methods

        private void AddFindMru()
        {
            string find = this.cboFindF.Text;
            this._mruFind.Remove(find);

            this._mruFind.Insert(0, find);

            if (this._mruFind.Count > this._mruMaxCount)
                this._mruFind.RemoveAt(this._mruFind.Count - 1);

            this._bindingSourceFind.ResetBindings(false);
            this.cboFindR.SelectedIndex = 0;
            this.cboFindF.SelectedIndex = 0;
        }


        private void AddReplacMru()
        {
            string find = this.cboFindR.Text;
            this._mruFind.Remove(find);

            this._mruFind.Insert(0, find);

            if (this._mruFind.Count > this._mruMaxCount)
                this._mruFind.RemoveAt(this._mruFind.Count - 1);

            string replace = this.cboReplace.Text;
            if (replace != string.Empty)
            {
                this._mruReplace.Remove(replace);

                this._mruReplace.Insert(0, replace);

                if (this._mruReplace.Count > this._mruMaxCount)
                    this._mruReplace.RemoveAt(this._mruReplace.Count - 1);
            }

            this._bindingSourceFind.ResetBindings(false);
            this._bindingSourceReplace.ResetBindings(false);
            this.cboFindR.SelectedIndex = 0;
            this.cboFindF.SelectedIndex = 0;
            this.cboReplace.SelectedIndex = 0;
        }


        private void btnClear_Click(object sender, EventArgs e)
        {
            this.Scintilla.Markers.DeleteAll(this.Scintilla.FindReplace.Marker);
            this.Scintilla.FindReplace.ClearAllHighlights();
        }


        private void btnFindAll_Click(object sender, EventArgs e)
        {
            if (this.cboFindF.Text == string.Empty)
                return;

            this.AddFindMru();

            this.lblStatus.Text = string.Empty;

            List<Range> foundRanges = null;
            if (this.rdoRegexF.Checked)
            {
                Regex rr = null;
                try
                {
                    rr = new Regex(this.cboFindF.Text, this.GetRegexOptions());
                }
                catch (ArgumentException ex)
                {
                    this.lblStatus.Text = "Error in Regular Expression: " + ex.Message;
                    return;
                }

                if (this.chkSearchSelectionF.Checked)
                {
                    if (this._searchRange == null)
                    {
                        this._searchRange = this.Scintilla.Selection.Range;
                    }

                    foundRanges = this.Scintilla.FindReplace.FindAll(this._searchRange, rr);
                }
                else
                {
                    this._searchRange = null;
                    foundRanges = this.Scintilla.FindReplace.FindAll(rr);
                }
            }
            else
            {
                if (this.chkSearchSelectionF.Checked)
                {
                    if (this._searchRange == null)
                        this._searchRange = this.Scintilla.Selection.Range;

                    foundRanges = this.Scintilla.FindReplace.FindAll(this._searchRange, this.cboFindF.Text, this.GetSearchFlags());
                }
                else
                {
                    this._searchRange = null;
                    foundRanges = this.Scintilla.FindReplace.FindAll(this.cboFindF.Text, this.GetSearchFlags());
                }
            }

            this.lblStatus.Text = "Total found: " + foundRanges.Count.ToString();

            this.btnClear_Click(null, null);

            if (this.chkMarkLine.Checked)
                this.Scintilla.FindReplace.MarkAll(foundRanges);

            if (this.chkHighlightMatches.Checked)
                this.Scintilla.FindReplace.HighlightAll(foundRanges);
        }


        private void btnFindNext_Click(object sender, EventArgs e)
        {
            this.FindNext();
        }


        private void btnFindPrevious_Click(object sender, EventArgs e)
        {
            this.FindPrevious();
        }


        private void btnReplaceAll_Click(object sender, EventArgs e)
        {
            if (this.cboFindR.Text == string.Empty)
                return;

            this.lblStatus.Text = string.Empty;

            List<Range> foundRanges = null;

            if (this.rdoRegexR.Checked)
            {
                Regex rr = null;
                try
                {
                    rr = new Regex(this.cboFindR.Text, this.GetRegexOptions());
                }
                catch (ArgumentException ex)
                {
                    this.lblStatus.Text = "Error in Regular Expression: " + ex.Message;
                    return;
                }

                if (this.chkSearchSelectionR.Checked)
                {
                    if (this._searchRange == null)
                    {
                        this._searchRange = this.Scintilla.Selection.Range;
                    }

                    foundRanges = this.Scintilla.FindReplace.ReplaceAll(this._searchRange, rr, this.cboReplace.Text);
                }
                else
                {
                    this._searchRange = null;
                    foundRanges = this.Scintilla.FindReplace.ReplaceAll(rr, this.cboReplace.Text);
                }
            }
            else
            {
                if (this.chkSearchSelectionR.Checked)
                {
                    if (this._searchRange == null)
                        this._searchRange = this.Scintilla.Selection.Range;

                    foundRanges = this.Scintilla.FindReplace.ReplaceAll(this._searchRange, this.cboFindR.Text, this.cboReplace.Text, this.GetSearchFlags());
                }
                else
                {
                    this._searchRange = null;
                    foundRanges = this.Scintilla.FindReplace.ReplaceAll(this.cboFindR.Text, this.cboReplace.Text, this.GetSearchFlags());
                }
            }

            this.lblStatus.Text = "Total Replaced: " + foundRanges.Count.ToString();
        }


        private void btnReplaceNext_Click(object sender, EventArgs e)
        {
            this.ReplaceNext();
        }


        private void btnReplacePrevious_Click(object sender, EventArgs e)
        {
            if (this.cboFindR.Text == string.Empty)
                return;

            this.AddReplacMru();
            this.lblStatus.Text = string.Empty;

            Range nextRange = null;
            try
            {
                nextRange = this.ReplaceNext(true);
            }
            catch (ArgumentException ex)
            {
                this.lblStatus.Text = "Error in Regular Expression: " + ex.Message;
                return;
            }


            if (nextRange == null)
            {
                this.lblStatus.Text = "Match could not be found";
            }
            else
            {
                if (nextRange.Start > this.Scintilla.Caret.Anchor)
                {
                    if (this.chkSearchSelectionR.Checked)
                        this.lblStatus.Text = "Search match wrapped to the begining of the selection";
                    else
                        this.lblStatus.Text = "Search match wrapped to the begining of the document";
                }

                nextRange.Select();
                this.MoveFormAwayFromSelection();
            }
        }


        private void chkEcmaScript_CheckedChanged(object sender, EventArgs e)
        {
            if (((CheckBox)sender).Checked)
            {
                this.chkExplicitCaptureF.Checked = false;
                this.chkExplicitCaptureR.Checked = false;
                this.chkExplicitCaptureF.Enabled = false;
                this.chkExplicitCaptureR.Enabled = false;
                this.chkIgnorePatternWhitespaceF.Checked = false;
                this.chkIgnorePatternWhitespaceR.Checked = false;
                this.chkIgnorePatternWhitespaceF.Enabled = false;
                this.chkIgnorePatternWhitespaceR.Enabled = false;
                this.chkRightToLeftF.Checked = false;
                this.chkRightToLeftR.Checked = false;
                this.chkRightToLeftF.Enabled = false;
                this.chkRightToLeftR.Enabled = false;
                this.chkSinglelineF.Checked = false;
                this.chkSinglelineR.Checked = false;
                this.chkSinglelineF.Enabled = false;
                this.chkSinglelineR.Enabled = false;
            }
            else
            {
                this.chkExplicitCaptureF.Enabled = true;
                this.chkIgnorePatternWhitespaceF.Enabled = true;
                this.chkRightToLeftF.Enabled = true;
                this.chkSinglelineF.Enabled = true;
                this.chkExplicitCaptureR.Enabled = true;
                this.chkIgnorePatternWhitespaceR.Enabled = true;
                this.chkRightToLeftR.Enabled = true;
                this.chkSinglelineR.Enabled = true;
            }
        }


        public void FindNext()
        {
            if (this.cboFindF.Text == string.Empty)
                return;

            this.AddFindMru();
            this.lblStatus.Text = string.Empty;

            Range foundRange = null;

            try
            {
                foundRange = this.FindNextF(false);
            }
            catch (ArgumentException ex)
            {
                this.lblStatus.Text = "Error in Regular Expression: " + ex.Message;
                return;
            }

            if (foundRange == null)
            {
                this.lblStatus.Text = "Match could not be found";
            }
            else
            {
                if (foundRange.Start < this.Scintilla.Caret.Anchor)
                {
                    if (this.chkSearchSelectionF.Checked)
                        this.lblStatus.Text = "Search match wrapped to the begining of the selection";
                    else
                        this.lblStatus.Text = "Search match wrapped to the begining of the document";
                }

                foundRange.Select();
                this.MoveFormAwayFromSelection();
            }
        }


        private Range FindNextF(bool searchUp)
        {
            Range foundRange;

            if (this.rdoRegexF.Checked)
            {
                var rr = new Regex(this.cboFindF.Text, this.GetRegexOptions());

                if (this.chkSearchSelectionF.Checked)
                {
                    if (this._searchRange == null)
                        this._searchRange = this.Scintilla.Selection.Range;

                    if (searchUp)
                        foundRange = this.Scintilla.FindReplace.FindPrevious(rr, this.chkWrapF.Checked, this._searchRange);
                    else
                        foundRange = this.Scintilla.FindReplace.FindNext(rr, this.chkWrapF.Checked, this._searchRange);
                }
                else
                {
                    this._searchRange = null;
                    if (searchUp)
                        foundRange = this.Scintilla.FindReplace.FindPrevious(rr, this.chkWrapF.Checked);
                    else
                        foundRange = this.Scintilla.FindReplace.FindNext(rr, this.chkWrapF.Checked);
                }
            }
            else
            {
                if (this.chkSearchSelectionF.Checked)
                {
                    if (this._searchRange == null)
                        this._searchRange = this.Scintilla.Selection.Range;

                    if (searchUp)
                        foundRange = this.Scintilla.FindReplace.FindPrevious(this.cboFindF.Text, this.chkWrapF.Checked, this.GetSearchFlags(), this._searchRange);
                    else
                        foundRange = this.Scintilla.FindReplace.FindNext(this.cboFindF.Text, this.chkWrapF.Checked, this.GetSearchFlags(), this._searchRange);
                }
                else
                {
                    this._searchRange = null;
                    if (searchUp)
                        foundRange = this.Scintilla.FindReplace.FindPrevious(this.cboFindF.Text, this.chkWrapF.Checked, this.GetSearchFlags());
                    else
                        foundRange = this.Scintilla.FindReplace.FindNext(this.cboFindF.Text, this.chkWrapF.Checked, this.GetSearchFlags());
                }
            }
            return foundRange;
        }


        private Range FindNextR(bool searchUp, ref Regex rr)
        {
            Range foundRange;


            if (this.rdoRegexR.Checked)
            {
                if (rr == null)
                    rr = new Regex(this.cboFindR.Text, this.GetRegexOptions());

                if (this.chkSearchSelectionR.Checked)
                {
                    if (this._searchRange == null)
                        this._searchRange = this.Scintilla.Selection.Range;

                    if (searchUp)
                        foundRange = this.Scintilla.FindReplace.FindPrevious(rr, this.chkWrapR.Checked, this._searchRange);
                    else
                        foundRange = this.Scintilla.FindReplace.FindNext(rr, this.chkWrapR.Checked, this._searchRange);
                }
                else
                {
                    this._searchRange = null;
                    if (searchUp)
                        foundRange = this.Scintilla.FindReplace.FindPrevious(rr, this.chkWrapR.Checked);
                    else
                        foundRange = this.Scintilla.FindReplace.FindNext(rr, this.chkWrapR.Checked);
                }
            }
            else
            {
                if (this.chkSearchSelectionF.Checked)
                {
                    if (this._searchRange == null)
                        this._searchRange = this.Scintilla.Selection.Range;

                    if (searchUp)
                        foundRange = this.Scintilla.FindReplace.FindPrevious(this.cboFindR.Text, this.chkWrapR.Checked, this.GetSearchFlags(), this._searchRange);
                    else
                        foundRange = this.Scintilla.FindReplace.FindNext(this.cboFindR.Text, this.chkWrapR.Checked, this.GetSearchFlags(), this._searchRange);
                }
                else
                {
                    this._searchRange = null;
                    if (searchUp)
                        foundRange = this.Scintilla.FindReplace.FindPrevious(this.cboFindR.Text, this.chkWrapF.Checked, this.GetSearchFlags());
                    else
                        foundRange = this.Scintilla.FindReplace.FindNext(this.cboFindR.Text, this.chkWrapF.Checked, this.GetSearchFlags());
                }
            }
            return foundRange;
        }


        public void FindPrevious()
        {
            if (this.cboFindF.Text == string.Empty)
                return;

            this.AddFindMru();
            this.lblStatus.Text = string.Empty;
            Range foundRange = null;
            try
            {
                foundRange = this.FindNextF(true);
            }
            catch (ArgumentException ex)
            {
                this.lblStatus.Text = "Error in Regular Expression: " + ex.Message;
                return;
            }

            if (foundRange == null)
            {
                this.lblStatus.Text = "Match could not be found";
            }
            else
            {
                if (foundRange.Start > this.Scintilla.Caret.Position)
                {
                    if (this.chkSearchSelectionF.Checked)
                        this.lblStatus.Text = "Search match wrapped to the _end of the selection";
                    else
                        this.lblStatus.Text = "Search match wrapped to the _end of the document";
                }

                foundRange.Select();
                this.MoveFormAwayFromSelection();
            }
        }


        private void FindReplaceDialog_FormClosing(object sender, FormClosingEventArgs e)
        {
            if (e.CloseReason == CloseReason.UserClosing)
            {
                e.Cancel = true;
                Hide();
            }
        }


        public RegexOptions GetRegexOptions()
        {
            var ro = RegexOptions.None;

            if (this.tabAll.SelectedTab == this.tpgFind)
            {
                if (this.chkCompiledF.Checked)
                    ro |= RegexOptions.Compiled;

                if (this.chkCultureInvariantF.Checked)
                    ro |= RegexOptions.Compiled;

                if (this.chkEcmaScriptF.Checked)
                    ro |= RegexOptions.ECMAScript;

                if (this.chkExplicitCaptureF.Checked)
                    ro |= RegexOptions.ExplicitCapture;

                if (this.chkIgnoreCaseF.Checked)
                    ro |= RegexOptions.IgnoreCase;

                if (this.chkIgnorePatternWhitespaceF.Checked)
                    ro |= RegexOptions.IgnorePatternWhitespace;

                if (this.chkMultilineF.Checked)
                    ro |= RegexOptions.Multiline;

                if (this.chkRightToLeftF.Checked)
                    ro |= RegexOptions.RightToLeft;

                if (this.chkSinglelineF.Checked)
                    ro |= RegexOptions.Singleline;
            }
            else
            {
                if (this.chkCompiledR.Checked)
                    ro |= RegexOptions.Compiled;

                if (this.chkCultureInvariantR.Checked)
                    ro |= RegexOptions.Compiled;

                if (this.chkEcmaScriptR.Checked)
                    ro |= RegexOptions.ECMAScript;

                if (this.chkExplicitCaptureR.Checked)
                    ro |= RegexOptions.ExplicitCapture;

                if (this.chkIgnoreCaseR.Checked)
                    ro |= RegexOptions.IgnoreCase;

                if (this.chkIgnorePatternWhitespaceR.Checked)
                    ro |= RegexOptions.IgnorePatternWhitespace;

                if (this.chkMultilineR.Checked)
                    ro |= RegexOptions.Multiline;

                if (this.chkRightToLeftR.Checked)
                    ro |= RegexOptions.RightToLeft;

                if (this.chkSinglelineR.Checked)
                    ro |= RegexOptions.Singleline;
            }

            return ro;
        }


        public SearchFlags GetSearchFlags()
        {
            var sf = SearchFlags.Empty;

            if (this.tabAll.SelectedTab == this.tpgFind)
            {
                if (this.chkMatchCaseF.Checked)
                    sf |= SearchFlags.MatchCase;

                if (this.chkWholeWordF.Checked)
                    sf |= SearchFlags.WholeWord;

                if (this.chkWordStartF.Checked)
                    sf |= SearchFlags.WordStart;
            }
            else
            {
                if (this.chkMatchCaseR.Checked)
                    sf |= SearchFlags.MatchCase;

                if (this.chkWholeWordR.Checked)
                    sf |= SearchFlags.WholeWord;

                if (this.chkWordStartR.Checked)
                    sf |= SearchFlags.WordStart;
            }

            return sf;
        }


        public void MoveFormAwayFromSelection()
        {
            if (!Visible)
                return;

            int pos = this.Scintilla.Caret.Position;
            int x = this.Scintilla.PointXFromPosition(pos);
            int y = this.Scintilla.PointYFromPosition(pos);

            Point cursorPoint = this.Scintilla.PointToScreen(new Point(x, y));

            var r = new Rectangle(Location, Size);
            if (r.Contains(cursorPoint))
            {
                Point newLocation;
                if (cursorPoint.Y < (Screen.PrimaryScreen.Bounds.Height / 2))
                {
                    // Top half of the screen
                    newLocation = this.Scintilla.PointToClient(
                        new Point(Location.X, cursorPoint.Y + this.Scintilla.Lines.Current.Height * 2)
                        );
                }
                else
                {
                    // FixedY half of the screen
                    newLocation = this.Scintilla.PointToClient(
                        new Point(Location.X, cursorPoint.Y - Height - (this.Scintilla.Lines.Current.Height * 2))
                        );
                }
                newLocation = this.Scintilla.PointToScreen(newLocation);
                Location = newLocation;
            }
        }


        protected override void OnActivated(EventArgs e)
        {
            if (this.Scintilla.Selection.Length > 0)
            {
                this.chkSearchSelectionF.Enabled = true;
                this.chkSearchSelectionR.Enabled = true;
            }
            else
            {
                this.chkSearchSelectionF.Enabled = false;
                this.chkSearchSelectionR.Enabled = false;
                this.chkSearchSelectionF.Checked = false;
                this.chkSearchSelectionR.Checked = false;
            }

            //	if they leave the dialog and come back any "Search Selection"
            //	range they might have had is invalidated
            this._searchRange = null;

            this.lblStatus.Text = string.Empty;

            this.MoveFormAwayFromSelection();

            base.OnActivated(e);
        }


        protected override void OnKeyDown(KeyEventArgs e)
        {
            //	So what we're doing here is testing for any of the find/replace
            //	command shortcut bindings. If the key combination matches we send
            //	the KeyEventArgs back to Scintilla so it can be processed. That
            //	way things like Find Next, Show Replace are all available from
            //	the dialog using Scintilla's configured Shortcuts

            List<KeyBinding> findNextBinding = this.Scintilla.Commands.GetKeyBindings(BindableCommand.FindNext);
            List<KeyBinding> findPrevBinding = this.Scintilla.Commands.GetKeyBindings(BindableCommand.FindPrevious);
            List<KeyBinding> showFindBinding = this.Scintilla.Commands.GetKeyBindings(BindableCommand.ShowFind);
            List<KeyBinding> showReplaceBinding = this.Scintilla.Commands.GetKeyBindings(BindableCommand.ShowReplace);

            var kb = new KeyBinding(e.KeyCode, e.Modifiers);

            if (findNextBinding.Contains(kb) || findPrevBinding.Contains(kb) || showFindBinding.Contains(kb) || showReplaceBinding.Contains(kb))
            {
                this.Scintilla.FireKeyDown(e);
            }


            if (e.KeyCode == Keys.Escape)
                Hide();

            base.OnKeyDown(e);
        }


        private void rdoStandardF_CheckedChanged(object sender, EventArgs e)
        {
			if (this.rdoStandardF.Checked)
			{
				this.pnlStandardOptionsF.BringToFront();
				this.pnlRegexpOptionsF.SendToBack();
			}
			else
			{
				this.pnlRegexpOptionsF.BringToFront();
				this.pnlStandardOptionsF.SendToBack();
			}
        }


        private void rdoStandardR_CheckedChanged(object sender, EventArgs e)
        {	
			if (this.rdoStandardR.Checked)
			{
				this.pnlStandardOptionsR.BringToFront();
				this.pnlRegexpOptionsR.SendToBack();
			}
			else
			{
				this.pnlRegexpOptionsR.BringToFront();
				this.pnlStandardOptionsR.SendToBack();
			}
        }


        public void ReplaceNext()
        {
            if (this.cboFindR.Text == string.Empty)
                return;

            this.AddReplacMru();
            this.lblStatus.Text = string.Empty;

            Range nextRange = null;
            try
            {
                nextRange = this.ReplaceNext(false);
            }
            catch (ArgumentException ex)
            {
                this.lblStatus.Text = "Error in Regular Expression: " + ex.Message;
                return;
            }

            if (nextRange == null)
            {
                this.lblStatus.Text = "Match could not be found";
            }
            else
            {
                if (nextRange.Start < this.Scintilla.Caret.Anchor)
                {
                    if (this.chkSearchSelectionR.Checked)
                        this.lblStatus.Text = "Search match wrapped to the begining of the selection";
                    else
                        this.lblStatus.Text = "Search match wrapped to the begining of the document";
                }

                nextRange.Select();
                this.MoveFormAwayFromSelection();
            }
        }


        private Range ReplaceNext(bool searchUp)
        {
            Regex rr = null;
            Range selRange = this.Scintilla.Selection.Range;

            //	We only do the actual replacement if the current selection exactly
            //	matches the find.
            if (selRange.Length > 0)
            {
                if (this.rdoRegexR.Checked)
                {
                    rr = new Regex(this.cboFindR.Text, this.GetRegexOptions());
                    string selRangeText = selRange.Text;

                    if (selRange.Equals(this.Scintilla.FindReplace.Find(selRange, rr, false)))
                    {
                        //	If searching up we do the replacement using the range object.
                        //	Otherwise we use the selection object. The reason being if
                        //	we use the range the caret is positioned before the replaced
                        //	text. Conversely if we use the selection object the caret will
                        //	be positioned after the replaced text. This is very important
                        //	becuase we don't want the new text to be potentially matched
                        //	in the next search.
                        if (searchUp)
                            selRange.Text = rr.Replace(selRangeText, this.cboReplace.Text);
                        else
                            this.Scintilla.Selection.Text = rr.Replace(selRangeText, this.cboReplace.Text);
                    }
                }
                else
                {
                    if (selRange.Equals(this.Scintilla.FindReplace.Find(selRange, this.cboFindR.Text, false)))
                    {
                        if (searchUp)
                            selRange.Text = this.cboReplace.Text;
                        else
                            this.Scintilla.Selection.Text = this.cboReplace.Text;
                    }
                }
            }
            return this.FindNextR(searchUp, ref rr);
        }


        private void tabAll_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (this.tabAll.SelectedTab == this.tpgFind)
            {
                this.cboFindF.Text = this.cboFindR.Text;

                this.rdoStandardF.Checked = this.rdoStandardR.Checked;
                this.rdoRegexF.Checked = this.rdoRegexR.Checked;

                this.chkWrapF.Checked = this.chkWrapR.Checked;
                this.chkSearchSelectionF.Checked = this.chkSearchSelectionR.Checked;

                this.chkMatchCaseF.Checked = this.chkMatchCaseR.Checked;
                this.chkWholeWordF.Checked = this.chkWholeWordR.Checked;
                this.chkWordStartF.Checked = this.chkWordStartR.Checked;

                this.chkCompiledF.Checked = this.chkCompiledR.Checked;
                this.chkCultureInvariantF.Checked = this.chkCultureInvariantR.Checked;
                this.chkEcmaScriptF.Checked = this.chkEcmaScriptR.Checked;
                this.chkExplicitCaptureF.Checked = this.chkExplicitCaptureR.Checked;
                this.chkIgnoreCaseF.Checked = this.chkIgnoreCaseR.Checked;
                this.chkIgnorePatternWhitespaceF.Checked = this.chkIgnorePatternWhitespaceR.Checked;
                this.chkMultilineF.Checked = this.chkMultilineR.Checked;
                this.chkRightToLeftF.Checked = this.chkRightToLeftR.Checked;
                this.chkSinglelineF.Checked = this.chkSinglelineR.Checked;

                AcceptButton = this.btnFindNext;
            }
            else
            {
                this.cboFindR.Text = this.cboFindF.Text;

                this.rdoStandardR.Checked = this.rdoStandardF.Checked;
                this.rdoRegexR.Checked = this.rdoRegexF.Checked;

                this.chkWrapR.Checked = this.chkWrapF.Checked;
                this.chkSearchSelectionR.Checked = this.chkSearchSelectionF.Checked;

                this.chkMatchCaseR.Checked = this.chkMatchCaseF.Checked;
                this.chkWholeWordR.Checked = this.chkWholeWordF.Checked;
                this.chkWordStartR.Checked = this.chkWordStartF.Checked;

                this.chkCompiledR.Checked = this.chkCompiledF.Checked;
                this.chkCultureInvariantR.Checked = this.chkCultureInvariantF.Checked;
                this.chkEcmaScriptR.Checked = this.chkEcmaScriptF.Checked;
                this.chkExplicitCaptureR.Checked = this.chkExplicitCaptureF.Checked;
                this.chkIgnoreCaseR.Checked = this.chkIgnoreCaseF.Checked;
                this.chkIgnorePatternWhitespaceR.Checked = this.chkIgnorePatternWhitespaceF.Checked;
                this.chkMultilineR.Checked = this.chkMultilineF.Checked;
                this.chkRightToLeftR.Checked = this.chkRightToLeftF.Checked;
                this.chkSinglelineR.Checked = this.chkSinglelineF.Checked;

                AcceptButton = this.btnReplaceNext;
            }
        }

        #endregion Methods


        #region Properties

        public List<string> MruFind
        {
            get
            {
                return this._mruFind;
            }
            set
            {
                this._mruFind = value;
                this._bindingSourceFind.DataSource = this._mruFind;
            }
        }


        public int MruMaxCount
        {
            get { return this._mruMaxCount; }
            set { this._mruMaxCount = value; }
        }


        public List<string> MruReplace
        {
            get
            {
                return this._mruReplace;
            }
            set
            {
                this._mruReplace = value;
                this._bindingSourceReplace.DataSource = this._mruReplace;
            }
        }


        public Scintilla Scintilla
        {
            get
            {
                return this._scintilla;
            }
            set
            {
                this._scintilla = value;
            }
        }

        #endregion Properties


        #region Constructors

        public FindReplaceDialog()
        {
            this.InitializeComponent();
            this._mruFind = new List<string>();
            this._mruReplace = new List<string>();
            this._bindingSourceFind.DataSource = this._mruFind;
            this._bindingSourceReplace.DataSource = this._mruReplace;
            this.cboFindF.DataSource = this._bindingSourceFind;
            this.cboFindR.DataSource = this._bindingSourceFind;
            this.cboReplace.DataSource = this._bindingSourceReplace;
        }

        #endregion Constructors

		private void grpOptionsF_CollapseBoxClickedEvent(object sender)
		{
			int y = this.grpOptionsF.Location.Y + 6;
			y += this.grpOptionsF.IsCollapsed ? this.grpOptionsF.CollapsedHeight : this.grpOptionsF.FullHeight;
			this.grpFindAll.Location = new Point(this.grpFindAll.Location.X, y);
			this.grpFindAll_CollapseBoxClickedEvent(sender);
		}

		private void grpFindAll_CollapseBoxClickedEvent(object sender)
		{
			int y = this.grpFindAll.Location.Y + 6;
			y += this.grpFindAll.IsCollapsed ? this.grpFindAll.CollapsedHeight : this.grpFindAll.FullHeight;
			this.btnFindNext.Location = new Point(this.btnFindNext.Location.X, y);
			this.btnFindPrevious.Location = new Point(this.btnFindPrevious.Location.X, y);
		}

		private void grdOptionsR_CollapseBoxClickedEvent(object sender)
		{
			int y = this.grdOptionsR.Location.Y + 6;
			y += this.grdOptionsR.IsCollapsed ? this.grdOptionsR.CollapsedHeight : this.grdOptionsR.FullHeight;
			this.btnReplaceAll.Location = new Point(this.btnReplaceAll.Location.X, y);
			this.btnReplacePrevious.Location = new Point(this.btnReplacePrevious.Location.X, y);
			y += this.btnReplaceNext.Location.Y - this.btnReplacePrevious.Location.Y;
			this.btnReplaceNext.Location = new Point(this.btnReplaceNext.Location.X, y);
		}
    }
}
