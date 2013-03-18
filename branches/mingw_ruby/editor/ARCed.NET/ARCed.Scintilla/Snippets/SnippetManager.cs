#region Using Directives

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Text.RegularExpressions;
using System.Windows.Forms;

#endregion


namespace ARCed.Scintilla
{
    [TypeConverter(typeof(ExpandableObjectConverter))]
    public class SnippetManager : TopLevelHelper
    {
        #region Fields

        private Color _activeSnippetColor = Color.Lime;
        private int _activeSnippetIndicator = 15;
        private IndicatorStyle _activeSnippetIndicatorStyle = IndicatorStyle.RoundBox;
        private char _defaultDelimeter = '$';
        private Color _inactiveSnippetColor = Color.Lime;
        private int _inactiveSnippetIndicator = 16;
        private IndicatorStyle _inactiveSnippetIndicatorStyle = IndicatorStyle.Box;
        private bool _isEnabled = true;
        
        //	Yeah I know this is a bit unwieldly but I can't come up with a better name
        private bool _isOneKeySelectionEmbedEnabled;
        private SnippetList _list;
        private bool _pendingUndo;
        private SnippetChooser _snipperChooser;
        private readonly SnippetLinkCollection _snippetLinks = new SnippetLinkCollection();
        private readonly Timer _snippetLinkTimer = new Timer();
        private readonly Regex snippetRegex1 = new Regex(string.Format(@"(?<dm>{0}DropMarker(?<dmi>\[[0-9]*\])?{0})|(?<c>{0}caret{0})|(?<a>{0}anchor{0})|(?<e>{0}_end{0})|(?<s>{0}selected{0})|(?<l>{0}.+?(?<li>\[[0-9]*\])?{0})", Snippet.RealDelimeter), RegexOptions.IgnoreCase | RegexOptions.ExplicitCapture | RegexOptions.Compiled);

        #endregion Fields


        #region Methods

        public bool AcceptActiveSnippets()
        {
            if (this._snippetLinks.IsActive && !Scintilla.AutoComplete.IsActive)
            {
                int pos = Scintilla.Caret.Position;
                bool end = false;
                foreach (SnippetLink sl in this._snippetLinks.Values)
                {
                    foreach (SnippetLinkRange sr in sl.Ranges)
                    {
                        if (sr.PositionInRange(pos))
                        {
                            end = true;
                            break;
                        }
                    }
                    if (end)
                        break;
                }

                if (end)
                {
                    this.cascadeSnippetLinkRangeChange(this._snippetLinks.ActiveSnippetLink, this._snippetLinks.ActiveRange);

                    if (this._snippetLinks.EndPoint != null)
                        Scintilla.Caret.Goto(this._snippetLinks.EndPoint.Start);

                    this.IsActive = false;
                    Scintilla.Commands.StopProcessingCommands = true;
                    return true;
                }
            }

            return false;
        }


        private SnippetLinkRange addSnippetLink(SnippetLinkRange range)
        {
            string key = range.Key;
            SnippetLink sl = null;
            for (int i = 0; i < this._snippetLinks.Count; i++)
            {
                if (this._snippetLinks[i].Key.Equals(key, StringComparison.CurrentCultureIgnoreCase))
                {
                    sl = this._snippetLinks[i];
                    break;
                }
            }
            if (sl == null)
            {
                sl = new SnippetLink(key);
                this._snippetLinks.Add(sl);
            }

            sl.Ranges.Add(range);
            range.Parent = sl.Ranges;

            return range;
        }


        public bool CancelActiveSnippets()
        {
            if (this._snippetLinks.IsActive && !Scintilla.AutoComplete.IsActive)
            {
                this.IsActive = false;
                Scintilla.Commands.StopProcessingCommands = true;
                return true;
            }

            return false;
        }


        private void cascadeSnippetLinkRangeChange(SnippetLink oldActiveSnippetLink, SnippetLinkRange oldActiveRange)
        {
            Scintilla.ManagedRanges.Sort();

            int offset = 0;

            string newText = oldActiveRange.Text;


            Scintilla.NativeInterface.SetModEventMask(0);
            foreach (ManagedRange mr in Scintilla.ManagedRanges)
            {
                if (offset != 0)
                    mr.Change(mr.Start + offset, mr.End + offset);

                var slr = mr as SnippetLinkRange;
                if (slr == null || !oldActiveSnippetLink.Ranges.Contains(slr) || slr.Text == newText)
                    continue;

                int oldLength = slr.Length;
                slr.Text = newText;
                slr.End += newText.Length - oldLength;
                offset += newText.Length - oldLength;
            }

            Scintilla.NativeInterface.SetModEventMask(Constants.SC_MODEVENTMASKALL);
        }


        public bool DoSnippetCheck()
        {
            if (!this._isEnabled || this._snippetLinks.IsActive || Scintilla.AutoComplete.IsActive || Scintilla.Selection.Length > 0)
                return false;

            int pos = Scintilla.NativeInterface.GetCurrentPos();

            //	In order to even _start searching for a snippet keyword the
            //	current position needs to meet these conditions:
            //	Can't be at the very beginning of the document. Why? becuase
            //	then obviously there can't be a preceding keyword then can it?
            //	The preceding character can't be whitespace (same reason) 
            //
            //	I decided I like expanding a template in the middle of a word
            if (pos <= 0 || Scintilla.NativeInterface.GetCharAt(pos - 1).ToString().IndexOfAny(Scintilla.Lexing.WhitespaceCharsArr) >= 0)
                return false;

            //	We also don't want a template expand if we're in a Comment or 
            //	String. Be sure and mask out any indicator style that may be applied
            int currentStyle = Scintilla.NativeInterface.GetStyleAt(pos - 1) & 0x1f;
            if (currentStyle == 1 || currentStyle == 2 || currentStyle == 4)
                return false;

            //	Let Scintilla figure out where the beginning of
            //	the word to the left is.
            int newPos = Scintilla.NativeInterface.WordStartPosition(pos, true);

            Range snipRange = Scintilla.GetRange(newPos, pos);
            string keyworkCandidate = snipRange.Text;

            Snippet snip;
            if (!this._list.TryGetValue(keyworkCandidate, out snip))
            {
                //	Not a match. Buh-bye
                return false;
            }

            this.InsertSnippet(snip, newPos);
            Scintilla.Commands.StopProcessingCommands = true;
            return true;
        }


        public void InsertSnippet(string shortcut)
        {
            Snippet snip;
            if (!this._list.TryGetValue(shortcut, out snip))
            {
                //	Not a match. Buh-bye
                return;
            }

            this.InsertSnippet(snip, Math.Min(NativeScintilla.GetCurrentPos(), NativeScintilla.GetAnchor()));
        }


        public void InsertSnippet(Snippet snip)
        {
            this.InsertSnippet(snip, Math.Min(NativeScintilla.GetCurrentPos(), NativeScintilla.GetAnchor()));
        }


        internal void InsertSnippet(Snippet snip, int startPos)
        {
            NativeScintilla.BeginUndoAction();
            this.IsActive = false;

            string snippet = snip.RealCode;

            //	First properly indent the template. We do this by
            //	getting the indent string of the current line and
            //	adding it to all newlines
            int indentPoint = 0;
            string line = Scintilla.Lines.Current.Text;
            if(line != string.Empty)
            {				
                while (indentPoint < line.Length)
                {
                    char c = line[indentPoint];
                    if (c != ' ' && c != '\t')
                        break;

                    indentPoint++;
                }
            }

            //	Grab the current selected text in case we have a surrounds with scenario.
            string selText = Scintilla.Selection.Text;
            //	Now we clear the selection
            if (selText != string.Empty)
                Scintilla.Selection.Clear();

            if (indentPoint > 0)
            {
                string indent = line.Substring(0, indentPoint);

                //	This is a bit of a tough decision, but I think the best way to handle it
                //	is to assume that the Snippet's Eol Marker matches the Platform DOCUMENT_DEFAULT
                //	but the target Eol Marker should match the Document's.
                snippet = snippet.Replace(Environment.NewLine, Scintilla.EndOfLine.EolString + indent);

                //	Same deal with the selected text if any				
                selText = selText.Replace(Environment.NewLine, Scintilla.EndOfLine.EolString + indent);
            }

            int anchorPos = -1;
            int caretPos = -1;
            int endPos = -1;
            int selPos = -1;
            var dropMarkers = new SortedList<int, int>();
            var indexedRangesToActivate = new SortedList<int, SnippetLinkRange>();
            var unindexedRangesToActivate = new List<SnippetLinkRange>();
            Match m = this.snippetRegex1.Match(snippet);

            while (m.Success)
            {
                //	Did it match a $DropMarker$ token?
                if (m.Groups["dm"].Success)
                {
                    //	Yep, was it an indexed or unindexed DropMarker
                    if (m.Groups["dmi"].Success)
                    {
                        //	Indexed, set the indexed drop marker's character offset
                        //	if it is specified more than once the last one wins.
                        dropMarkers[int.Parse(m.Groups["dmi"].Value)] = m.Groups["dm"].Index;
                    }
                    else
                    {
                        //	Unindexed, just tack it on at the _end
                        dropMarkers[dropMarkers.Count] = m.Groups["dm"].Index;
                    }

                    //	Take the token out of the string
                    snippet = snippet.Remove(m.Groups["dm"].Index, m.Groups["dm"].Length);
                }
                else if (m.Groups["c"].Success)
                {
                    //	We matched the $Caret$ Token. Since there can be 
                    //	only 1 we set the caretPos. If this is specified
                    //	more than once the last one wins
                    caretPos = m.Groups["c"].Index;

                    //	Take the token out of the string
                    snippet = snippet.Remove(m.Groups["c"].Index, m.Groups["c"].Length);
                }
                else if (m.Groups["a"].Success)
                {
                    //	We matched the $Anchor$ Token. Since there can be 
                    //	only 1 we set the anchorPos. If this is specified
                    //	more than once the last one wins
                    anchorPos = m.Groups["a"].Index;

                    //	Take the token out of the string
                    snippet = snippet.Remove(m.Groups["a"].Index, m.Groups["a"].Length);
                }
                else if (m.Groups["e"].Success)
                {
                    //	We matched the $End$ Token. Since there can be 
                    //	only 1 we set the endPos. If this is specified
                    //	more than once the last one wins
                    endPos = m.Groups["e"].Index;

                    //	Take the token out of the string
                    snippet = snippet.Remove(m.Groups["e"].Index, m.Groups["e"].Length);
                }
                else if (m.Groups["s"].Success)
                {
                    //	We matched the $Selection$ Token. Simply insert the
                    //	selected text at this position
                    selPos = m.Groups["s"].Index;

                    //	Take the token out of the string
                    snippet = snippet.Remove(m.Groups["s"].Index, m.Groups["s"].Length);
                    snippet = snippet.Insert(m.Groups["s"].Index, selText);
                }
                else if (m.Groups["l"].Success)
                {
                    //	Finally match for Snippet Link Ranges. This is at the bottom of the if/else
                    //	because we want the more specific findRegex groups to match first so that this
                    //	generic expression group doesn't create a SnippetLinkRange for say the 
                    //	$Caret$ Token.
                    Group g = m.Groups["l"];

                    int rangeIndex;
                    string groupKey;

                    if (m.Groups["li"].Success)
                    {
                        //	We have a subindexed SnippetLinkRange along the lines of $sometoken[1]$
                        Group sg = m.Groups["li"];

                        //	At this point g.Value = $sometoken[1]$
                        //	and sg.Value = [1].
                        //	We want the range's Key, which would be sometoken
                        groupKey = g.Value.Substring(1, g.Value.Length - sg.Length - 2);

                        //	Now we need the range's Index which would be 1 in our fictitional case
                        rangeIndex = int.Parse(sg.Value.Substring(1, sg.Value.Length - 2));

                        //	Now we need to determine the actual _start and _end positions of the range.
                        //	Keep in mind we'll be stripping out the 2 $ and the subindex string (eg [1])
                        int start = startPos + g.Index;
                        int end = start + g.Length - sg.Length - 2;

                        //	And now we add (or replace) the snippet link range at the index
                        //	keep in mind duplicates will stomp all over each other, the last
                        //	one wins. Replaced tokens won't get a range
                        indexedRangesToActivate[rangeIndex] = new SnippetLinkRange(start, end, Scintilla, groupKey);

                        //	And remove all the token info including the subindex from the snippet text 
                        //	leaving only the key
                        snippet = snippet.Remove(g.Index, 1).Remove(g.Index - 2 + g.Length - sg.Length, sg.Length + 1);
                    }
                    else
                    {
                        //	We have a regular old SnippetLinkRange along the lines of $sometoken$

                        //	We want the range's Key, which would be sometoken
                        groupKey = g.Value.Substring(1, g.Value.Length - 2);

                        //	Now we need to determine the actual _start and _end positions of the range.
                        //	Keep in mind we'll be stripping out the 2 $
                        int start = startPos + g.Index;
                        int end = start + g.Length - 2;

                        //	Now create the range object
                        unindexedRangesToActivate.Add(new SnippetLinkRange(start, end, Scintilla, groupKey));

                        //	And remove all the token info from the snippet text 
                        //	leaving only the key
                        snippet = snippet.Remove(g.Index, 1).Remove(g.Index + g.Length - 2, 1);
                    }
                }
                //	Any more matches? Note that I'm rerunning the regexp query
                //	on the snippet string becuase it's contents have been modified
                //	and we need to get the updated index values.
                m = this.snippetRegex1.Match(snippet);
            }

            //	Replace the snippet Keyword with the snippet text. Or if this
            //	isn't triggered by a shortcut, it will insert at the current
            //	Caret Position
            Scintilla.GetRange(startPos, NativeScintilla.GetCurrentPos()).Text = snippet;

            //	Now that we have the text set we can activate our link ranges
            //	we couldn't do it before becuase they were managed ranges and
            //	would get offset by the text change

            //	Since we are done adding new SnippetLinkRanges we can tack
            //	on the unindexed ranges to the _end of the indexed ranges
            var allLinks = new SnippetLinkRange[indexedRangesToActivate.Count + unindexedRangesToActivate.Count];
            for (int i = 0; i < indexedRangesToActivate.Values.Count; i++)
                allLinks[i] = indexedRangesToActivate[i];

            for (int i = 0; i < unindexedRangesToActivate.Count; i++)
                allLinks[i + indexedRangesToActivate.Count] = unindexedRangesToActivate[i];

            foreach (SnippetLinkRange slr in allLinks)
                this.addSnippetLink(slr);

            foreach (SnippetLinkRange slr in allLinks)
                slr.Init();

            //	Now we need to activate the Snippet links. However we have a bit
            //	of a styling confilct. If we set the indicator styles before the
            //	SQL Lexer styles the newly added text it won't get styled. So to
            //	make sure we set the Indicator Styles after we put the call on
            //	a timer.
            if (this._snippetLinks.Count > 0)
            {
                var t = new Timer
                {
                    Interval = 10
                };

                //	Oh how I love anonymous delegates, this is starting to remind
                //	me of JavaScript and SetTimeout...
                t.Tick += delegate
                {
                    t.Dispose();
                    this.IsActive = true;
                };
                t.Start();
            }

            //	Add all the Drop markers in the indexed order. The
            //	order is reversed of course because drop markers work
            //	in a FILO manner
            for (int i = dropMarkers.Count - 1; i >= 0; i--)
                Scintilla.DropMarkers.Drop(startPos + dropMarkers.Values[i]);

            //	Place the caret at either the position of the token or
            //	at the _end of the snippet text.
            if (caretPos >= 0)
                Scintilla.Caret.Goto(startPos + caretPos);
            else
                Scintilla.Caret.Goto(startPos + snippet.Length);

            //	Ahoy, way anchor!
            if (anchorPos >= 0)
                Scintilla.Caret.Anchor = startPos + anchorPos;

            //	Do we have an _end cursor?
            if (endPos >= 0)
            {
                //	If they have snippet link ranges activated in this snippet
                //	go ahead and set up an EndPoint marker
                if (allLinks.Length > 0)
                {
                    var eci = new SnippetLinkEnd(endPos + startPos, Scintilla);
                    Scintilla.ManagedRanges.Add(eci);
                    this._snippetLinks.EndPoint = eci;
                }
                else
                {
                    //	Otherwise we treat it like an Anchor command because
                    //	the SnippetLink mode isn't activated
                    Scintilla.Caret.Goto(endPos + startPos);
                }
            }

            NativeScintilla.EndUndoAction();
        }


        public bool NextSnippetRange()
        {
            //	This would be a whole lot easier if I had the Command Contexts set
            //	up. The way it's working now is that this command will always execute
            //	irregardlessly of if the SnippetLinks are active. Since we may not have
            //	a valid context to execute we don't necessarily want to eat the
            //	keystroke in all circumstances, hence the bool return
            if (!this._snippetLinks.IsActive || Scintilla.AutoComplete.IsActive)
                return false;

            //	OK So we want to find the next SnippetLink in
            //	whatever order they are in and then select it
            //	so that they can fill it out.
            SnippetLink sl = this._snippetLinks.NextActiveSnippetLink;
            if (sl != null)
            {
                //	However it is possible that all of this Snippet Links'
                //	ranges have been deleted by the user. If this is the case
                //	we need to remove this snippet link from the list and go
                //	to the next link.

                while (sl.Ranges.Count == 0)
                {
                    this._snippetLinks.Remove(sl);
                    sl = this._snippetLinks.NextActiveSnippetLink;

                    //	No more snippet links? Nothing to do but quit
                    if (sl == null)
                    {
                        Scintilla.Commands.StopProcessingCommands = true;
                        return true;
                    }
                }

                //	Yay we have it. Select the first Range in the Snippet Link's Series
                sl.Ranges[0].Select();
                Scintilla.Commands.StopProcessingCommands = true;
                return true;
            }

            return false;
        }


        public bool PreviousSnippetRange()
        {
            //	Same as NextSnippetRange but going in the opposite direction
            if (!this._snippetLinks.IsActive || Scintilla.AutoComplete.IsActive)
                return false;

            SnippetLink sl = this._snippetLinks.PreviousActiveSnippetLink;
            if (sl != null)
            {
                while (sl.Ranges.Count == 0)
                {
                    this._snippetLinks.Remove(sl);
                    sl = this._snippetLinks.PreviousActiveSnippetLink;
                    if (sl == null)
                    {
                        Scintilla.Commands.StopProcessingCommands = true;
                        return true;
                    }
                }

                sl.Ranges[0].Select();
                Scintilla.Commands.StopProcessingCommands = true;
                return true;
            }

            return false;
        }


        private void ResetActiveSnippetColor()
        {
            this._activeSnippetColor = Color.Lime;
        }


        private void ResetActiveSnippetIndicator()
        {
            this._activeSnippetIndicator = 15;
        }


        private void ResetActiveSnippetIndicatorStyle()
        {
            this._activeSnippetIndicatorStyle = IndicatorStyle.RoundBox;
        }


        private void ResetDefaultDelimeter()
        {
            this._defaultDelimeter = '$';
        }


        private void ResetInactiveSnippetColor()
        {
            this._inactiveSnippetColor = Color.Lime;
        }


        private void ResetInactiveSnippetIndicator()
        {
            this._inactiveSnippetIndicator = 16;
        }


        private void ResetInactiveSnippetIndicatorStyle()
        {
            this._inactiveSnippetIndicatorStyle = IndicatorStyle.Box;
        }


        private void ResetIsEnabled()
        {
            this._isEnabled = true;
        }


        private void ResetIsOneKeySelectionEmbedEnabled()
        {
            this._isOneKeySelectionEmbedEnabled = false;
        }


        private void Scintilla_BeforeTextDelete(object sender, TextModifiedEventArgs e)
        {
            if (!this._isEnabled)
                return;

            if (this._snippetLinks.IsActive && !this._pendingUndo && !(e.UndoRedoFlags.IsUndo || e.UndoRedoFlags.IsRedo))
            {
                this._pendingUndo = true;
                Scintilla.UndoRedo.BeginUndoAction();
                this._snippetLinkTimer.Enabled = true;
            }

            ManagedRange undoneSnippetLinkRange = null;
            if (e.UndoRedoFlags.IsUndo && this._snippetLinks.IsActive)
            {
                foreach (ManagedRange mr in Scintilla.ManagedRanges)
                {
                    if (mr.Start == e.Position && mr.Length == e.Length && mr.Length > 1)
                    {
                        undoneSnippetLinkRange = mr;

                        //	Expanding the range So that it won't get marked for deletion
                        mr.End++;
                    }
                }
            }

            //	It's possible that the _end point may have been deleted. The endpoint
            //	is an ultra persistent marker that cannot be deleted until the Snippet
            //	Link mode is deactivated. Place a new EndPoint at the begining of the
            //	deleted range.
            if (this._snippetLinks.IsActive && this._snippetLinks.EndPoint != null && this._snippetLinks.EndPoint.Scintilla == null)
            {
                var eci = new SnippetLinkEnd(e.Position, Scintilla);
                Scintilla.ManagedRanges.Add(eci);
                this._snippetLinks.EndPoint = eci;
            }

            //	Now collapse the Undone range in preparation for the
            //	newly inserted text that will be put in here
            if (undoneSnippetLinkRange != null)
                undoneSnippetLinkRange.End = undoneSnippetLinkRange.Start;

            //	Check to see if all SnippetLink ranges have been deleted.
            //	If this is the case we need to turn Deactivate SnippetLink
            //	mode.

            bool deactivate = true;
            foreach (SnippetLink sl in this._snippetLinks.Values)
            {
                if (sl.Ranges.Count > 0)
                {
                    foreach (SnippetLinkRange slr in sl.Ranges)
                    {
                        if (slr.Scintilla != null)
                        {
                            deactivate = false;
                            break;
                        }
                    }
                }
                if (!deactivate)
                    break;
            }

            if (deactivate && this.IsActive)
                this.IsActive = false;
        }


        private void Scintilla_BeforeTextInsert(object sender, TextModifiedEventArgs e)
        {
            if (this._snippetLinks.IsActive && !this._pendingUndo && !(e.UndoRedoFlags.IsUndo || e.UndoRedoFlags.IsRedo))
            {
                this._pendingUndo = true;
                Scintilla.UndoRedo.BeginUndoAction();
                this._snippetLinkTimer.Enabled = true;
            }
        }


        private void Scintilla_SelectionChanged(object sender, EventArgs e)
        {
            Range sr = Scintilla.Selection.Range;

            if (this._snippetLinks.IsActive)
            {
                SnippetLink oldActiveSnippetLink = this._snippetLinks.ActiveSnippetLink;
                SnippetLinkRange oldActiveRange = this._snippetLinks.ActiveRange;

                this._snippetLinks.ActiveSnippetLink = null;
                this._snippetLinks.ActiveRange = null;

                for (int i = 0; i < this._snippetLinks.Count; i++)
                {

                    SnippetLink sl = this._snippetLinks[i];

                    foreach (SnippetLinkRange r in sl.Ranges)
                    {
                        if (r.IntersectsWith(sr))
                        {
                            this._snippetLinks.ActiveSnippetLink = sl;
                            this._snippetLinks.ActiveRange = r;
                            break;
                        }
                    }
                    if (this._snippetLinks.ActiveRange != null)
                        break;
                }

                foreach (SnippetLink sl in this._snippetLinks.Values)
                    foreach (Range r in sl.Ranges)
                    {
                        if (sl == this._snippetLinks.ActiveSnippetLink)
                        {
                            r.ClearIndicator(Scintilla.Snippets.InactiveSnippetIndicator);
                            r.SetIndicator(Scintilla.Snippets.ActiveSnippetIndicator);
                        }
                        else
                        {
                            r.SetIndicator(Scintilla.Snippets.InactiveSnippetIndicator);
                            r.ClearIndicator(Scintilla.Snippets.ActiveSnippetIndicator);
                        }
                    }
            }
        }


        private void Scintilla_TextInserted(object sender, TextModifiedEventArgs e)
        {
            //	I'm going to have to look into making this a little less "sledge hammer to
            //	the entire documnet"ish
            if (this._snippetLinks.IsActive && (e.UndoRedoFlags.IsUndo || e.UndoRedoFlags.IsRedo))
                Scintilla.NativeInterface.Colourise(0, -1);
        }


        internal void SetIndicators()
        {
            Scintilla.Indicators[this._activeSnippetIndicator].Style = this._activeSnippetIndicatorStyle;
            Scintilla.Indicators[this._activeSnippetIndicator].Color = this._activeSnippetColor;

            Scintilla.Indicators[this._inactiveSnippetIndicator].Style = this._inactiveSnippetIndicatorStyle;
            Scintilla.Indicators[this._inactiveSnippetIndicator].Color = this._inactiveSnippetColor;
        }


        internal bool ShouldSerialize()
        {
            return this.ShouldSerializeActiveSnippetColor() ||
                this.ShouldSerializeActiveSnippetIndicator() ||
                this.ShouldSerializeActiveSnippetIndicatorStyle() ||
                this.ShouldSerializeInactiveSnippetColor() ||
                this.ShouldSerializeInactiveSnippetIndicator() ||
                this.ShouldSerializeInactiveSnippetIndicatorStyle()||
                this.ShouldSerializeIsOneKeySelectionEmbedEnabled() ||
                this.ShouldSerializeIsEnabled() ||
                this.ShouldSerializeDefaultDelimeter();
        }


        private bool ShouldSerializeActiveSnippetColor()
        {
            return this._activeSnippetColor != Color.Lime;
        }


        private bool ShouldSerializeActiveSnippetIndicator()
        {
            return this._activeSnippetIndicator != 15;
        }


        private bool ShouldSerializeActiveSnippetIndicatorStyle()
        {
            return this._activeSnippetIndicatorStyle != IndicatorStyle.RoundBox;
        }


        private bool ShouldSerializeDefaultDelimeter()
        {
            return this._defaultDelimeter != '$';
        }


        private bool ShouldSerializeInactiveSnippetColor()
        {
            return this._inactiveSnippetColor != Color.Lime;
        }


        private bool ShouldSerializeInactiveSnippetIndicator()
        {
            return this._inactiveSnippetIndicator != 16;
        }


        private bool ShouldSerializeInactiveSnippetIndicatorStyle()
        {
            return this._inactiveSnippetIndicatorStyle != IndicatorStyle.Box;
        }


        private bool ShouldSerializeIsEnabled()
        {
            return !this._isEnabled;
        }


        private bool ShouldSerializeIsOneKeySelectionEmbedEnabled()
        {
            return this._isOneKeySelectionEmbedEnabled;
        }


         public void ShowSnippetList()
        {
            if (this._list.Count == 0)
                return;

            if (this._snipperChooser == null)
            {
                this._snipperChooser = new SnippetChooser
                {
                    Scintilla = Scintilla,
                    SnippetList = this._list.ToString()
                };
                this._snipperChooser.Scintilla.Controls.Add(this._snipperChooser);
            }
            this._snipperChooser.SnippetList = this._list.ToString();
            this._snipperChooser.Show();
        }


        public void ShowSurroundWithList()
        {
            var sl = new SnippetList(null);
            foreach (Snippet s in this._list)
            {
                if (s.IsSurroundsWith)
                    sl.Add(s);
            }

            if (sl.Count == 0)
                return;

            if (this._snipperChooser == null)
            {
                this._snipperChooser = new SnippetChooser
                {
                    Scintilla = Scintilla,
                    SnippetList = this._list.ToString()
                };
                this._snipperChooser.Scintilla.Controls.Add(this._snipperChooser);
            }
            this._snipperChooser.SnippetList = sl.ToString();
            this._snipperChooser.Show();
        }


        private void snippetLinkTimer_Tick(object sender, EventArgs e)
        {
            this._snippetLinkTimer.Enabled = false;
            Range sr = Scintilla.Selection.Range;

            if (this._snippetLinks.IsActive)
            {
                SnippetLink oldActiveSnippetLink = this._snippetLinks.ActiveSnippetLink;
                SnippetLinkRange oldActiveRange = this._snippetLinks.ActiveRange;

                if (oldActiveRange != null && (oldActiveRange.IntersectsWith(sr) || oldActiveRange.Equals(sr)))
                {
                    Scintilla.BeginInvoke(new MethodInvoker(delegate
                    {
                        this.cascadeSnippetLinkRangeChange(oldActiveSnippetLink, oldActiveRange);

                        foreach (SnippetLink sl in this._snippetLinks.Values)
                            foreach (Range r in sl.Ranges)
                            {
                                if (sl == this._snippetLinks.ActiveSnippetLink)
                                {
                                    r.ClearIndicator(Scintilla.Snippets.InactiveSnippetIndicator);
                                    r.SetIndicator(Scintilla.Snippets.ActiveSnippetIndicator);
                                }
                                else
                                {
                                    r.SetIndicator(Scintilla.Snippets.InactiveSnippetIndicator);
                                    r.ClearIndicator(Scintilla.Snippets.ActiveSnippetIndicator);
                                }

                            }

                        if (this._pendingUndo)
                        {
                            this._pendingUndo = false;
                            Scintilla.UndoRedo.EndUndoAction();
                        }

                        Scintilla.NativeInterface.Colourise(0, -1);
                    }));
                }
            }
        }

        #endregion Methods


        #region Properties

        public Color ActiveSnippetColor
        {
            get
            {
                return this._activeSnippetColor;
            }
            set
            {
                this._activeSnippetColor = value;
            }
        }


        public int ActiveSnippetIndicator
        {
            get
            {
                return this._activeSnippetIndicator;
            }
            set
            {
                this._activeSnippetIndicator = value;
            }
        }


        public IndicatorStyle ActiveSnippetIndicatorStyle
        {
            get
            {
                return this._activeSnippetIndicatorStyle;
            }
            set
            {
                this._activeSnippetIndicatorStyle = value;
            }
        }


        public char DefaultDelimeter
        {
            get
            {
                return this._defaultDelimeter;
            }
            set
            {
                this._defaultDelimeter = value;
            }
        }


        public Color InactiveSnippetColor
        {
            get
            {
                return this._inactiveSnippetColor;
            }
            set
            {
                this._inactiveSnippetColor = value;
            }
        }


        public int InactiveSnippetIndicator
        {
            get
            {
                return this._inactiveSnippetIndicator;
            }
            set
            {
                this._inactiveSnippetIndicator = value;
            }
        }


        public IndicatorStyle InactiveSnippetIndicatorStyle
        {
            get
            {
                return this._inactiveSnippetIndicatorStyle;
            }
            set
            {
                this._inactiveSnippetIndicatorStyle = value;
            }
        }


        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public bool IsActive
        {
            get
            {
                return this._snippetLinks.IsActive;
            }
            internal set
            {
                this._snippetLinks.IsActive = value;

                if (value)
                {
                    this.SetIndicators();
                    this._snippetLinks[0].Ranges[0].Select();
                }
                else
                {
                    //	Deactivating Snippet Link mode. First make sure all
                    //	the snippet link ranges have their indicators cleared
                    foreach (SnippetLink sl in this._snippetLinks.Values)
                        foreach (Range r in sl.Ranges)
                        {
                            r.ClearIndicator(Scintilla.Snippets.InactiveSnippetIndicator);
                            r.ClearIndicator(Scintilla.Snippets.ActiveSnippetIndicator);
                        }

                    //	Then clear out the _snippetLinks list cuz we're done with them
                    this._snippetLinks.Clear();

                    if (this._snippetLinks.EndPoint != null)
                    {
                        this._snippetLinks.EndPoint.Dispose();
                        this._snippetLinks.EndPoint = null;
                    }
                }
            }
        }


        [DesignerSerializationVisibility(DesignerSerializationVisibility.Visible)]
        public bool IsEnabled
        {
            get
            {
                return this._isEnabled;
            }
            set
            {
                this._isEnabled = value;

                if (value)
                {
                    Scintilla.TextInserted += this.Scintilla_TextInserted;
                    Scintilla.BeforeTextInsert += this.Scintilla_BeforeTextInsert;
                    Scintilla.BeforeTextDelete += this.Scintilla_BeforeTextDelete;
                    Scintilla.SelectionChanged += this.Scintilla_SelectionChanged;
                }
                else
                {
                    Scintilla.TextInserted -= this.Scintilla_TextInserted;
                    Scintilla.BeforeTextInsert -= this.Scintilla_BeforeTextInsert;
                    Scintilla.BeforeTextDelete -= this.Scintilla_BeforeTextDelete;
                    Scintilla.SelectionChanged -= this.Scintilla_SelectionChanged;
                }
            }
        }


        public bool IsOneKeySelectionEmbedEnabled
        {
            get
            {
                return this._isOneKeySelectionEmbedEnabled;
            }
            set
            {
                this._isOneKeySelectionEmbedEnabled = value;
            }
        }


        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public SnippetList List
        {
            get
            {
                return this._list;
            }
            set
            {
                this._list = value;
            }
        }

        #endregion Properties


        #region Constructors

        public SnippetManager(Scintilla scintilla) : base(scintilla)
        {
            this._list = new SnippetList(this);

            this._snippetLinkTimer.Interval = 1;
            this._snippetLinkTimer.Tick += this.snippetLinkTimer_Tick;

            this.IsEnabled = this._isEnabled;
        }

        #endregion Constructors
    }
}