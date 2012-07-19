#region Using Directives

using System;
using System.Collections;
using System.Collections.Generic;
using System.Collections.Specialized;
using System.ComponentModel;
using System.Drawing;
using System.Drawing.Design;
using System.Drawing.Drawing2D;
using System.IO;
using System.Runtime.InteropServices;
using System.Security.Permissions;
using System.Text;
using System.Windows.Forms;
using ARCed.Scintilla.Configuration;
using ARCed.Scintilla.Design;

#endregion


namespace ARCed.Scintilla
{
    #pragma warning disable 612, 618
    /// <summary>
    ///     Represents a Scintilla text editor control.
    /// </summary>
    [Designer(typeof(ScintillaDesigner))]
    [Docking(DockingBehavior.Ask)]
    [DefaultBindingProperty("Text")]
    [DefaultProperty("Text")]
    [DefaultEvent("DocumentChanged")]
    public partial class Scintilla : Control, INativeScintilla, ISupportInitialize
    {
        #region Fields

        private static IntPtr _moduleHandle;
		private static string _moduleName = (IntPtr.Size == 4 ? Resources.ModuleName : Resources.ModuleName64);
        private static NativeMethods.Scintilla_DirectFunction _directFunction;
        private IntPtr _directPointer;

        private static readonly object _annotationChangedEventKey = new object();
        private static readonly object _autoCompleteAcceptedEventKey = new object();
        private static readonly object _beforeTextDeleteEventKey = new object();
        private static readonly object _beforeTextInsertEventKey = new object();
        private static readonly object _borderStyleChangedEventKey = new object();
        private static readonly object _callTipClickEventKey = new object();
        private static readonly object _charAddedEventKey = new object();
        private static readonly object _documentChangeEventKey = new object();
        private static readonly object _dropMarkerCollectEventKey = new object();
        private static readonly object _dwellEndEventKey = new object();
        private static readonly object _dwellStartEventKey = new object();
        private static readonly object _fileDropEventKey = new object();
        private static readonly object _foldChangedEventKey = new object();
        private static readonly object _hotspotClickedEventKey = new object();
        private static readonly object _hotspotDoubleClickedEventKey = new object();
        private static readonly object _hotspotReleaseClickEventKey = new object();
        private static readonly object _indicatorClickEventKey = new object();
        private static readonly object _linesNeedShownEventKey = new object();
        private static readonly object _loadEventKey = new object();
        private static readonly object _macroRecordEventKey = new object();
        private static readonly object _marginClickEventKey = new object();
        private static readonly object _markerChangedEventKey = new object();
        private static readonly object _modifiedChangedEventKey = new object();
        private static readonly object _readOnlyModifyAttemptEventKey = new object();
        private static readonly object _scrollEventKey = new object();
        private static readonly object _selectionChangedEventKey = new object();
        private static readonly object _styleNeededEventKey = new object();
        private static readonly object _textDeletedEventKey = new object();
        private static readonly object _textInsertedEventKey = new object();
        private static readonly object _uriDroppedEventKey = new object();
        private static readonly object _userListEventKey = new object();
        private static readonly object _zoomChangedEventKey = new object();

        private static readonly int _modifiedState = BitVector32.CreateMask();
        private static readonly int _acceptsReturnState = BitVector32.CreateMask(_modifiedState);
        private static readonly int _acceptsTabState = BitVector32.CreateMask(_acceptsReturnState);
        private BitVector32 _state;

        private AnnotationCollection _annotations;
        private LineWrapping _lineWrapping;

        private List<TopLevelHelper> _helpers = new List<TopLevelHelper>();
        private readonly AutoComplete _autoComplete;
        private CallTip _callTip;
        private readonly CaretInfo _caret;
        private readonly Clipboard _clipboard;
        private Commands _commands;
        private ConfigurationManager _configurationManager;
        private DocumentHandler _documentHandler;
        private DocumentNavigation _documentNavigation;
        private readonly DropMarkers _dropMarkers;
        private Encoding _encoding;
        private EndOfLine _endOfLine;
        private FindReplace _findReplace;
        private Folding _folding;
        private GoTo _goto;
        private HotspotStyle _hotspotStyle;
        private Indentation _indentation;
        private readonly IndicatorCollection _indicators;
        private Lexing _lexing;
        private readonly LineCollection _lines;
        private LongLines _longLines;
        private readonly MarginCollection _margins;
        private MarkerCollection _markers;
        private Printing _printing;
        private Scrolling _scrolling;
        private readonly Selection _selection;
        private readonly SnippetManager _snippets;
        private StyleCollection _styles;
        private readonly UndoRedo _undoRedo;
        private readonly Whitespace _whitespace;

        private bool _allowDrop;
        private string _caption;
        private readonly Dictionary<string, Color> _colorBag = new Dictionary<string, Color>();

        /// <summary>
        ///     Enables the brace matching from current position.
        /// </summary>
        private bool _isBraceMatching;
        private bool _isCustomPaintingEnabled = true;
        private bool _isInitializing;
        private readonly List<ManagedRange> _managedRanges = new List<ManagedRange>();
        private bool _matchBraces = true;

        private readonly INativeScintilla _ns;
        private readonly Hashtable _propertyBag = new Hashtable();
        private SearchFlags _searchFlags = SearchFlags.Empty;
        private bool _supressControlCharacters = true;

        // List of Scintilla Supported encodings
        internal static readonly IList<Encoding> ValidCodePages = new[]
        {
            Encoding.ASCII,
            Encoding.UTF8,
            Encoding.Unicode,           // UTF-16
            Encoding.GetEncoding(932),  // shift_jis - Japanese (Shift-JIS)
            Encoding.GetEncoding(936),  // gb2312 - Chinese Simplified (GB2312)
            Encoding.GetEncoding(949),  // ks_c_5601-1987  - Korean
            Encoding.GetEncoding(950),  // big5 - Chinese Traditional (Big5)
            Encoding.GetEncoding(1361)  // Johab - Korean (Johab)
        };

        // This has to be set *early* because CreateParams is called before our constructor
        private BorderStyle _borderStyle = BorderStyle.Fixed3D;

        #endregion Fields


        #region Methods

        /// <summary>
        ///     Adds a line _end marker to the _end of the document
        /// </summary>
        public void AddLastLineEnd()
        {
            EndOfLineMode eolMode = this._endOfLine.Mode;
            string eolMarker = "\r\n";

            if (eolMode == EndOfLineMode.CR)
                eolMarker = "\r";
            else if (eolMode == EndOfLineMode.LF)
                eolMarker = "\n";

            int tl = this.TextLength;
            int start = tl - eolMarker.Length;

            if (start < 0 || this.GetRange(start, start + eolMarker.Length).Text != eolMarker)
                this.AppendText(eolMarker);
        }


        /// <summary>
        ///     Appends a copy of the specified string to the _end of this instance.
        /// </summary>
        /// <param name="text">The <see cref="String"/> to append.</param>
        /// <returns>A <see cref="Range"/> representing the appended text.</returns>
        public Range AppendText(string text)
        {
            int oldLength = this.TextLength;
            this.NativeInterface.AppendText(this.Encoding.GetByteCount(text), text);
            return this.GetRange(oldLength, this.TextLength);
        }


        public void BeginInit()
        {
            this._isInitializing = true;
        }


        public char CharAt(int position)
        {
            return this._ns.GetCharAt(position);
        }


        /// <summary>
        ///     Creates and returns a new <see cref="AnnotationCollection" /> object.
        /// </summary>
        /// <returns>A new <see cref="AnnotationCollection" /> object.</returns>
        [EditorBrowsable(EditorBrowsableState.Advanced)]
        protected virtual AnnotationCollection CreateAnnotationsInstance()
        {
            return new AnnotationCollection(this);
        }


        /// <summary>
        ///     Creates and returns a new <see cref="LineWrapping" /> object.
        /// </summary>
        /// <returns>A new <see cref="LineWrapping" /> object.</returns>
        [EditorBrowsable(EditorBrowsableState.Advanced)]
        protected virtual LineWrapping CreateLineWrappingInstance()
        {
            return new LineWrapping(this);
        }


        /// <summary>
        ///     Sends the specified message directly to the native Scintilla window,
        ///     bypassing any managed APIs.
        /// </summary>
        /// <param name="msg">The message ID.</param>
        /// <param name="wParam">The message <chr>wparam</chr> field.</param>
        /// <param name="lParam">The message <chr>lparam</chr> field.</param>
        /// <returns>An <see cref="IntPtr"/> representing the result of the message request.</returns>
        /// <remarks>
        ///     Warning: The Surgeon General Has Determined that Calling the Underlying Scintilla
        ///     Window Directly May Result in Unexpected Behavior!
        /// </remarks>
        /// <exception cref="InvalidOperationException">
        ///     The method was called from a thread other than the thread it was created on.
        /// </exception>
        [EditorBrowsable(EditorBrowsableState.Advanced)]
        public IntPtr DirectMessage(int msg, IntPtr wParam, IntPtr lParam)
        {
            // Enforce illegal cross-thread calls
            if (CheckForIllegalCrossThreadCalls && InvokeRequired)
            {
                string message = string.Format(Resources.Culture, Resources.Exception_IllegalCrossThreadCall, Name);
                throw new InvalidOperationException(message);
            }

            // Call the direct function delegate
            return _directFunction(this._directPointer, msg, wParam, lParam);
        }


        /// <summary>
        ///     Overridden. Releases the unmanaged resources used by the <see cref="Control" /> and
        ///     its child controls and optionally releases the managed resources.
        /// </summary>
        /// <param name="disposing"><chr>true</chr> to release both managed and unmanaged resources; <chr>false</chr> to release only unmanaged resources.</param>
        protected override void Dispose(bool disposing)
        {
            foreach (ScintillaHelperBase heler in this._helpers)
            {
                heler.Dispose();
            }

            if (disposing && IsHandleCreated)
            {
                // wi11811 2008-07-28 Chris Rickard
                // Since we eat the destroy message in WndProc
                // we have to manually let Scintilla know to
                // clean up its resources.
                var destroyMessage = new Message
                {
                    Msg = NativeMethods.WM_DESTROY,
                    HWnd = Handle
                };
                base.DefWndProc(ref destroyMessage);
            }

            base.Dispose(disposing);
        }


        public void EndInit()
        {
            this._isInitializing = false;
            foreach (ScintillaHelperBase helper in this._helpers)
            {
                helper.Initialize();
            }
        }


        /// <summary>
        ///     Exports a HTML representation of the current document.
        /// </summary>
        /// <returns>A <see cref="String"/> containing the contents of the document formatted as HTML.</returns>
        /// <remarks>Only ASCII documents are supported. Other encoding types have undefined behavior.</remarks>
        public string ExportHtml()
        {
            var sb = new StringBuilder();
            using (var sw = new StringWriter(sb))
                this.ExportHtml(sw, "Untitled", false);

            return sb.ToString();
        }


        /// <summary>
        ///     Exports a HTML representation of the current document.
        /// </summary>
        /// <param name="writer">The <see cref="TextWriter"/>with which to write. </param>
        /// <param name="title">The title of the HTML document.</param>
        /// <param name="allStyles">
        ///     <chr>true</chr> to output all styles including those not
        ///     used in the document; otherwise, <chr>false</chr>.
        /// </param>
        /// <remarks>Only ASCII documents are supported. Other encoding types have undefined behavior.</remarks>
        public void ExportHtml(TextWriter writer, string title, bool allStyles)
        {
            // Make sure the document is current
            // Lexing.Colorize();

            // Get the styles used
            int length = this.NativeInterface.GetLength();
            var stylesUsed = new bool[(int)StylesCommon.Max + 1];
            if (allStyles)
            {
                for (int i = 0; i < stylesUsed.Length; i++)
                    stylesUsed[i] = true;
            }
            else
            {
                // Record all the styles used
                for (int i = 0; i < length; i++)
                    stylesUsed[this.Styles.GetStyleAt(i) & (int)StylesCommon.Max] = true;
            }

            // The tab width
            int tabWidth = this.Indentation.TabWidth;

            // Start writing
            writer.WriteLine(@"<!DOCTYPE HTML PUBLIC ""-//W3C//DTD HTML 4.01 Transitional//EN"" ""http://www.w3.org/TR/html4/loose.dtd"">");
            writer.WriteLine("<html>");
            writer.WriteLine("<head>");
            writer.WriteLine("<title>{0}</title>", title);
            writer.WriteLine(@"<style type=""text/css"">");
            writer.WriteLine();

            // Write the body style
            writer.WriteLine("body {");
            writer.WriteLine("background-color: {0};", Utilities.ColorToHtml(this.Styles.Default.BackColor));
            if (this.LineWrapping.Mode == LineWrappingMode.None)
                writer.WriteLine("white-space: nowrap;");
            writer.WriteLine("}");
            writer.WriteLine();

            // Write the styles
            for (int i = 0; i < stylesUsed.Length; i++)
            {
                if (!stylesUsed[i])
                    continue;

                Style s = this.Styles[i];
                writer.WriteLine("span.s{0} {{", i);
                writer.WriteLine("font-family: \"" + s.FontName + "\";");
                writer.WriteLine("font-size: {0}pt;", s.Size);
                if (s.Italic)
                    writer.WriteLine("font-style: italic;");
                if (s.Bold)
                    writer.WriteLine("font-weight: bold;");
                if (!s.ForeColor.IsEmpty && s.ForeColor != Color.Transparent)
                    writer.WriteLine("color: {0};", Utilities.ColorToHtml(s.ForeColor));
                if (!s.BackColor.IsEmpty && s.BackColor != Color.Transparent)
                    writer.WriteLine("background-color: {0};", Utilities.ColorToHtml(s.BackColor));

                writer.WriteLine("}");
                writer.WriteLine();
            }

            writer.WriteLine("</style>");
            writer.WriteLine("</head>");
            writer.WriteLine("<body>");

            // Write the document
            // TODO There's more to be done here to support codepages/UTF-8
            char lc;
            char c = '\0';
            int lastStyle = -1;
            for (int i = 0; i < length; i++)
            {
                lc = c;
                c = this.NativeInterface.GetCharAt(i);
                int style = this.Styles.GetStyleAt(i);
                if(style != lastStyle)
                {
                    if(lastStyle != -1)
                        writer.Write("</span>");

                    writer.Write(@"<span class=""s{0}"">", style);
                    lastStyle = style;
                }

                switch (c)
                {
                    case '\0':
                        continue;

                    case ' ':
                        if (lc == ' ')
                            writer.Write("&nbsp;");
                        else
                            writer.Write(c);
                        continue;

                    case '\t':
                        for (int t = 0; t < tabWidth; t++)
                            writer.Write("&nbsp; ");
                        continue;

                    case '\r':
                    case '\n':
                        if (c == '\r' && i < length - 1 && this.NativeInterface.GetCharAt(i + 1) == '\n')
                            i++;

                        if (lastStyle != -1)
                            writer.Write("</span>");

                        writer.WriteLine("<br />");
                        lastStyle = -1;
                        continue;

                    case '<':
                        writer.Write("&lt;");
                        continue;

                    case '>':
                        writer.Write("&gt;");
                        continue;

                    case '&':
                        writer.Write("&amp;");
                        continue;

                    default:
                        writer.Write(c);
                        continue;
                }
            }

            if (lastStyle != -1)
                writer.Write("</span>");

            writer.WriteLine();
            writer.WriteLine("</body>");
            writer.WriteLine("</html>");
        }


        public int FindColumn(int line, int column)
        {
            return this._ns.FindColumn(line, column);
        }


        internal void FireCallTipClick(int arrow)
        {
            var a = (CallTipArrow)arrow;
            OverloadList ol = this.CallTip.OverloadList;
            CallTipClickEventArgs e;

            if (ol == null)
            {
                e = new CallTipClickEventArgs(a, -1, -1, null, this.CallTip.HighlightStart, this.CallTip.HighlightEnd);
            }
            else
            {
                int newIndex = ol.CurrentIndex;

                if (a == CallTipArrow.Down)
                {
                    if (ol.CurrentIndex == ol.Count - 1)
                        newIndex = 0;
                    else
                        newIndex++;
                }
                else if (a == CallTipArrow.Up)
                {
                    if (ol.CurrentIndex == 0)
                        newIndex = ol.Count - 1;
                    else
                        newIndex--;
                }

                e = new CallTipClickEventArgs(a, ol.CurrentIndex, newIndex, ol, this.CallTip.HighlightStart, this.CallTip.HighlightEnd);
            }

            this.OnCallTipClick(e);

            if (e.Cancel)
            {
                this.CallTip.Cancel();
            }
            else
            {
                if (ol != null)
                {
                    // We allow them to alse replace the list entirely or just
                    // manipulate the New Index
                    this.CallTip.OverloadList = e.OverloadList;
                    this.CallTip.OverloadList.CurrentIndex = e.NewIndex;
                    this.CallTip.ShowOverloadInternal();
                }
            }
        }


        internal void FireKeyDown(KeyEventArgs e)
        {
            this.OnKeyDown(e);
        }


        internal void FireMarginClick(SCNotification n)
        {
            Margin m = this.Margins[n.margin];
            var k = Keys.None;

            if ((n.modifiers & (int)KeyMod.Alt) == (int)KeyMod.Alt)
                k |= Keys.Alt;

            if ((n.modifiers & (int)KeyMod.Ctrl) == (int)KeyMod.Ctrl)
                k |= Keys.Control;

            if ((n.modifiers & (int)KeyMod.Shift) == (int)KeyMod.Shift)
                k |= Keys.Shift;

            this.OnMarginClick(new MarginClickEventArgs(k, n.position, this.Lines.FromPosition(n.position), m, m.AutoToggleMarkerNumber, m.IsFoldMargin));
        }


        public int GetColumn(int position)
        {
            return this._ns.GetColumn(position);
        }


        /// <summary>
        ///     Gets the text of the line containing the caret.
        /// </summary>
        /// <returns>A <see cref="String" /> representing the text of the line containing the caret.</returns>
        public string GetCurrentLine()
        {
            int tmp;
            return this.GetCurrentLine(out tmp);
        }


        /// <summary>
        ///     Gets the text of the line containing the caret and the current caret position within that line.
        /// </summary>
        /// <param name="caretPosition">When this method returns, contains the byte offset of the current caret position with the line.</param>
        /// <returns>A <see cref="String" /> representing the text of the line containing the caret.</returns>
        public unsafe string GetCurrentLine(out int caretPosition)
        {
            int length = this.DirectMessage(NativeMethods.SCI_GETCURLINE, IntPtr.Zero, IntPtr.Zero).ToInt32();
            var buffer = new byte[length];
            fixed (byte* bp = buffer)
                caretPosition = this.DirectMessage(NativeMethods.SCI_GETCURLINE, new IntPtr(buffer.Length), new IntPtr(bp)).ToInt32();

            return this.Encoding.GetString(buffer, 0, length - 1);
        }


        public Range GetRange()
        {
            return new Range(0, this._ns.GetTextLength(), this);
        }


        public Range GetRange(int position)
        {
            return new Range(position, position + 1, this);
        }


        public Range GetRange(int startPosition, int endPosition)
        {
            return new Range(startPosition, endPosition, this);
        }


        /// <summary>
        ///     Gets a word from the specified position
        /// </summary>
        public string GetWordFromPosition(int position)
        {
            // Chris Rickard 2008-07-28
            // Fixing implementation to actually return the word at the position...
            // Credit goes to Stumpii for the code.
            // As a side note: I think the previous code was implemented based off
            // some funky code I made for the snippet keyword detection, but since
            // it doesn't reference this method there's no reason to keep the buggy
            // behavior. I also removed the try..catch because in theory this
            // shouldn't throw and we REALLY shouldn't be eating exceptions at the
            // System.Exception level. If some _start popping up I can add some
            // conditionals or catch more specific Exceptions.
            int startPosition = this.NativeInterface.WordStartPosition(position, true);
            int endPosition = this.NativeInterface.WordEndPosition(position, true);
            return this.GetRange(startPosition, endPosition).Text;
        }


        private void HandleFileDrop(IntPtr hDrop)
        {
            StringBuilder buffer = null;
            uint nfiles = NativeMethods.DragQueryFile(hDrop, 0xffffffff, buffer, 0);
            var files = new List<string>();
            for (uint i = 0; i < nfiles; i++)
            {
                buffer = new StringBuilder(512);

                NativeMethods.DragQueryFile(hDrop, i, buffer, 512);
                files.Add(buffer.ToString());
            }
            NativeMethods.DragFinish(hDrop);

            this.OnFileDrop(new FileDropEventArgs(files.ToArray()));
        }


        /// <summary>
        ///     Inserts text at the current cursor position
        /// </summary>
        /// <param name="text">Text to insert</param>
        /// <returns>The range inserted</returns>
        public Range InsertText(string text)
        {
            this.NativeInterface.AddText(this.Encoding.GetByteCount(text), text);
            return this.GetRange(this._caret.Position, this.Encoding.GetByteCount(text));
        }


        /// <summary>
        ///     Inserts text at the given position
        /// </summary>
        /// <param name="position">The position to insert text in</param>
        /// <param name="text">Text to insert</param>
        /// <returns>The text range inserted</returns>
        public Range InsertText(int position, string text)
        {
            this.NativeInterface.InsertText(position, text);
            return this.GetRange(position, this.Encoding.GetByteCount(text));
        }


        /// <summary>
        ///     Overridden. See <see cref="Control.IsInputKey"/>.
        /// </summary>
        protected override bool IsInputKey(Keys keyData)
        {
            if ((keyData & Keys.Shift) != Keys.None)
                keyData ^= Keys.Shift;

            switch (keyData)
            {
                case Keys.Tab:
                    return this._state[_acceptsTabState];
                case Keys.Enter:
                    return this._state[_acceptsReturnState];
                case Keys.Up:
                case Keys.Down:
                case Keys.Left:
                case Keys.Right:
                case Keys.F:

                    return true;
            }

            return base.IsInputKey(keyData);
        }


        private static void LoadModule()
        {
            if (_moduleHandle == IntPtr.Zero)
            {
                // Load the Scintilla module into memory
                if ((_moduleHandle = NativeMethods.LoadLibrary(_moduleName)) == IntPtr.Zero)
                {
                    string message = string.Format(Resources.Culture, Resources.Exception_CannotLoadModule, _moduleName);
                    throw new Win32Exception(message, new Win32Exception(Marshal.GetLastWin32Error()));
                }

                // Get the direct function. We use GetProcAddress instead of DllImport
                // because we don't know the name of the module ahead of time.
                _directFunction = Marshal.GetDelegateForFunctionPointer(
                    NativeMethods.GetProcAddress(_moduleHandle, "Scintilla_DirectFunction"),
                    typeof(NativeMethods.Scintilla_DirectFunction)) as NativeMethods.Scintilla_DirectFunction;

                if (_directFunction == null)
                {
                    string message = string.Format(Resources.Culture, Resources.Exception_InvalidModule, _moduleName);
                    throw new Win32Exception(message, new Win32Exception(Marshal.GetLastWin32Error()));
                }
            }
        }


        private List<ManagedRange> ManagedRangesInRange(int firstPos, int lastPos)
        {
            // TODO: look into optimizing this so that it isn't a linear
            // search. This is fine for a few markers per document but
            // can be greatly improved if there are a large # of markers
            var ret = new List<ManagedRange>();
            foreach (ManagedRange mr in this._managedRanges)
                if (mr.Start >= firstPos && mr.Start <= lastPos)
                    ret.Add(mr);

            return ret;
        }


        /// <summary>
        ///     Raises the <see cref="AnnotationChanged" /> event.
        /// </summary>
        /// <param name="e">An <see cref="AnnotationChangedEventArgs" /> that contains the event data.</param>
        protected virtual void OnAnnotationChanged(AnnotationChangedEventArgs e)
        {
            var handler = Events[_annotationChangedEventKey] as EventHandler<AnnotationChangedEventArgs>;
            if (handler != null)
                handler(this, e);
        }


        /// <summary>
        ///     Raises the <see cref="AutoCompleteAccepted"/> event.
        /// </summary>
        /// <param name="e">An <see cref="AutoCompleteAcceptedEventArgs"/> that contains the event data.</param>
        protected virtual void OnAutoCompleteAccepted(AutoCompleteAcceptedEventArgs e)
        {
            var handler = Events[_autoCompleteAcceptedEventKey] as EventHandler<AutoCompleteAcceptedEventArgs>;
            if (handler != null)
                handler(this, e);

            if (e.Cancel)
                this.AutoComplete.Cancel();
        }


        /// <summary>
        ///     Raises the <see cref="E:System.Windows.Forms.Control.BackColorChanged"/> event.
        /// </summary>
        /// <param name="e">An <see cref="EventArgs"/> that contains the event data. </param>
        protected override void OnBackColorChanged(EventArgs e)
        {
            this.ResetStyles();
            base.OnBackColorChanged(e);
        }


        /// <summary>
        ///     Raises the <see cref="BeforeTextDelete"/> event.
        /// </summary>
        /// <param name="e">An <see cref="TextModifiedEventArgs"/> that contains the event data.</param>
        protected virtual void OnBeforeTextDelete(TextModifiedEventArgs e)
        {
            int firstPos = e.Position;
            int lastPos = firstPos + e.Length;

            var deletedRanges = new List<ManagedRange>();
            foreach (ManagedRange mr in this._managedRanges)
            {

                //	These ranges lie within the deleted range so
                //	the ranges themselves need to be deleted
                if (mr.Start >= firstPos && mr.End <= lastPos)
                {

                    //	If the entire range is being delete and NOT a superset of the range,
                    //	don't delete it, only collapse it.
                    if (!mr.IsPoint && e.Position == mr.Start && (e.Position + e.Length == mr.End))
                    {
                        mr.Change(mr.Start, mr.Start);
                    }
                    else
                    {
                        //	Notify the virtual Range that it needs to cleanup
                        mr.Change(-1, -1);

                        //	Mark for deletion after this foreach:
                        deletedRanges.Add(mr);

                    }
                }
                else if (mr.Start >= lastPos)
                {
                    //	These ranges are merely offset by the deleted range
                    mr.Change(mr.Start - e.Length, mr.End - e.Length);
                }
                else if (mr.Start >= firstPos && mr.Start <= lastPos)
                {
                    //	The left side of the managed range is getting
                    //	cut off
                    mr.Change(firstPos, mr.End - e.Length);
                }
                else if (mr.Start < firstPos && mr.End >= firstPos && mr.End >= lastPos)
                {
                    mr.Change(mr.Start, mr.End - e.Length);
                }
                else if (mr.Start < firstPos && mr.End >= firstPos && mr.End < lastPos)
                {
                    mr.Change(mr.Start, firstPos);
                }

            }

            foreach (ManagedRange mr in deletedRanges)
                mr.Dispose();

            var handler = Events[_beforeTextDeleteEventKey] as EventHandler<TextModifiedEventArgs>;
            if (handler != null)
                handler(this, e);
        }


        /// <summary>
        ///     Raises the <see cref="BeforeTextInsert"/> event.
        /// </summary>
        /// <param name="e">An <see cref="TextModifiedEventArgs"/> that contains the event data.</param>
        protected virtual void OnBeforeTextInsert(TextModifiedEventArgs e)
        {
            var offsetRanges = new List<ManagedRange>();
            foreach (ManagedRange mr in this._managedRanges)
            {
                if (mr.Start == e.Position && mr.PendingDeletion)
                {
                    mr.PendingDeletion = false;
                    ManagedRange lmr = mr;
                    BeginInvoke(new MethodInvoker(() => lmr.Change(e.Position, e.Position + e.Length)));
                }

                //	If the Range is a single point we treat it slightly
                //	differently than a spanned range
                if (mr.IsPoint)
                {
                    //	Unlike a spanned range, if the insertion point of
                    //	the new text == the _start of the range (and thus
                    //	the _end as well) we offset the entire point.
                    if (mr.Start >= e.Position)
                        mr.Change(mr.Start + e.Length, mr.End + e.Length);
                    else if (mr.End >= e.Position)
                        mr.Change(mr.Start, mr.End + e.Length);
                }
                else
                {
                    //	We offset a spanned range entirely only if the
                    //	_start occurs after the insertion point of the new
                    //	text.
                    if (mr.Start > e.Position)
                        mr.Change(mr.Start + e.Length, mr.End + e.Length);
                    else if (mr.End >= e.Position)
                    {
                        //	However it the _start of the range == the insertion
                        //	point of the new text instead of offestting the
                        //	range we expand it.
                        mr.Change(mr.Start, mr.End + e.Length);
                    }
                }

            }

            var handler = Events[_beforeTextInsertEventKey] as EventHandler<TextModifiedEventArgs>;
            if (handler != null)
                handler(this, e);
        }


        /// <summary>
        ///     Raises the <see cref="BorderStyleChanged" /> event.
        /// </summary>
        /// <param name="e">An <see cref="EventArgs"/> that contains the event data.</param>
        protected virtual void OnBorderStyleChanged(EventArgs e)
        {
            var handler = Events[_borderStyleChangedEventKey] as EventHandler;
            if (handler != null)
                handler(this, e);
        }


        /// <summary>
        ///     Raises the <see cref="CallTipClick"/> event.
        /// </summary>
        /// <param name="e">An <see cref="CallTipClickEventArgs"/> that contains the event data.</param>
        protected virtual void OnCallTipClick(CallTipClickEventArgs e)
        {
            var handler = Events[_callTipClickEventKey] as EventHandler<CallTipClickEventArgs>;
            if (handler != null)
                handler(this, e);
        }


        /// <summary>
        ///     Raises the <see cref="CharAdded"/> event.
        /// </summary>
        /// <param name="e">An <see cref="CharAddedEventArgs"/> that contains the event data.</param>
        protected virtual void OnCharAdded(CharAddedEventArgs e)
        {
            var handler = Events[_charAddedEventKey] as EventHandler<CharAddedEventArgs>;
            if (handler != null)
                handler(this, e);

            if (this._indentation.SmartIndentType != SmartIndent.None)
                this._indentation.CheckSmartIndent(e.Ch);
        }


        /// <summary>
        ///     Overridden. See <see cref="Control.OnCreateControl"/>.
        /// </summary>
        protected override void OnCreateControl()
        {
            base.OnCreateControl();
            this.OnLoad(EventArgs.Empty);
        }


        /// <summary>
        ///     Raises the <see cref="DocumentChange"/> event.
        /// </summary>
        /// <param name="e">An <see cref="NativeScintillaEventArgs"/> that contains the event data.</param>
        protected virtual void OnDocumentChange(NativeScintillaEventArgs e)
        {
            var handler = Events[_documentChangeEventKey] as EventHandler<NativeScintillaEventArgs>;
            if (handler != null)
                handler(this, e);
        }


        /// <summary>
        ///     Provides the support for code block selection
        /// </summary>
        protected override void OnDoubleClick(EventArgs e)
        {
            base.OnDoubleClick(e);

            if (this._isBraceMatching)
            {
                int position = this.CurrentPos - 1,
                       bracePosStart = -1,
                       bracePosEnd = -1;

                char character = this.CharAt(position);

                switch (character)
                {
                    case '{':
                    case '(':
                    case '[':
                        if (!this.PositionIsOnComment(position))
                        {
                            bracePosStart = position;
                            bracePosEnd = this._ns.BraceMatch(position, 0) + 1;
                            this._selection.Start = bracePosStart;
                            this._selection.End = bracePosEnd;
                        }
                        break;
                }
            }
        }


        /// <summary>
        ///     Raises the <see cref="DropMarkerCollect"/> event.
        /// </summary>
        /// <param name="e">An <see cref="DropMarkerCollectEventArgs"/> that contains the event data.</param>
        protected internal virtual void OnDropMarkerCollect(DropMarkerCollectEventArgs e)
        {
            var handler = Events[_dropMarkerCollectEventKey] as EventHandler<DropMarkerCollectEventArgs>;
            if (handler != null)
                handler(this, e);
        }


        /// <summary>
        ///     Raises the <see cref="DwellEnd"/> event.
        /// </summary>
        /// <param name="e">An <see cref="ScintillaMouseEventArgs"/> that contains the event data.</param>
        protected virtual void OnDwellEnd(ScintillaMouseEventArgs e)
        {
            var handler = Events[_dwellEndEventKey] as EventHandler<ScintillaMouseEventArgs>;
            if (handler != null)
                handler(this, e);
        }


        /// <summary>
        ///     Raises the <see cref="DwellStart"/> event.
        /// </summary>
        /// <param name="e">An <see cref="ScintillaMouseEventArgs"/> that contains the event data.</param>
        protected virtual void OnDwellStart(ScintillaMouseEventArgs e)
        {
            var handler = Events[_dwellStartEventKey] as EventHandler<ScintillaMouseEventArgs>;
            if (handler != null)
                handler(this, e);
        }


        /// <summary>
        ///     Raises the <see cref="FileDrop"/> event.
        /// </summary>
        /// <param name="e">An <see cref="FileDropEventArgs"/> that contains the event data.</param>
        protected virtual void OnFileDrop(FileDropEventArgs e)
        {
            var handler = Events[_fileDropEventKey] as EventHandler<FileDropEventArgs>;
            if (handler != null)
                handler(this, e);
        }


        /// <summary>
        ///     Raises the <see cref="FoldChanged"/> event.
        /// </summary>
        /// <param name="e">An <see cref="FoldChangedEventArgs"/> that contains the event data.</param>
        protected virtual void OnFoldChanged(FoldChangedEventArgs e)
        {
            var handler = Events[_foldChangedEventKey] as EventHandler<FoldChangedEventArgs>;
            if (handler != null)
                handler(this, e);
        }


        /// <summary>
        ///     Raises the <see cref="E:System.Windows.Forms.Control.FontChanged"/> event.
        /// </summary>
        /// <param name="e">An <see cref="EventArgs"/> that contains the event data.</param>
        protected override void OnFontChanged(EventArgs e)
        {
            this.ResetStyles();
            base.OnFontChanged(e);
        }


        /// <summary>
        ///     Raises the <see cref="E:System.Windows.Forms.Control.ForeColorChanged"/> event.
        /// </summary>
        /// <param name="e">An <see cref="EventArgs"/> that contains the event data. </param>
        protected override void OnForeColorChanged(EventArgs e)
        {
            this.ResetStyles();
            base.OnForeColorChanged(e);
        }


        /// <summary>
        ///     Overridden. See <see cref="Control.OnGotFocus"/>.
        /// </summary>
        protected override void OnGotFocus(EventArgs e)
        {
            if (!this.Selection.Hidden)
                this._ns.HideSelection(false);

            this._ns.SetSelBack(this.Selection.BackColor != Color.Transparent, Utilities.ColorToRgb(this.Selection.BackColor));
            this._ns.SetSelFore(this.Selection.ForeColor != Color.Transparent, Utilities.ColorToRgb(this.Selection.ForeColor));

            base.OnGotFocus(e);
        }


        /// <summary>
        ///     Overridden. Raises the <see cref="Control.HandleCreated"/> event.
        /// </summary>
        /// <param name="e">An <see cref="EventArgs"/> that contains the event data.</param>
        protected override void OnHandleCreated(EventArgs e)
        {
            // TODO Recreating handle?

            // Get the Scintilla direct pointer
            this._directPointer = NativeMethods.SendMessage(Handle, NativeMethods.SCI_GETDIRECTPOINTER, IntPtr.Zero, IntPtr.Zero);
            if (this._directPointer == IntPtr.Zero)
                throw new Win32Exception(Resources.Exception_CannotCreateDirectFunction);

            base.OnHandleCreated(e);
        }


        /// <summary>
        ///     Raises the <see cref="HotspotClick"/> event.
        /// </summary>
        /// <param name="e">A <see cref="HotspotClickEventArgs"/> that contains the event data.</param>
        protected virtual void OnHotspotClick(HotspotClickEventArgs e)
        {
            var handler = Events[_hotspotClickEventKey] as EventHandler<HotspotClickEventArgs>;
            if (handler != null)
                handler(this, e);
        }


        /// <summary>
        ///     Raises the <see cref="HotspotDoubleClick"/> event.
        /// </summary>
        /// <param name="e">A <see cref="HotspotClickEventArgs"/> that contains the event data.</param>
        protected virtual void OnHotspotDoubleClick(HotspotClickEventArgs e)
        {
            var handler = Events[_hotspotDoubleClickEventKey] as EventHandler<HotspotClickEventArgs>;
            if (handler != null)
                handler(this, e);
        }


        /// <summary>
        ///     Raises the <see cref="HotspotReleaseClick"/> event.
        /// </summary>
        /// <param name="e">A <see cref="HotspotClickEventArgs"/> that contains the event data.</param>
        protected virtual void OnHotspotReleaseClick(HotspotClickEventArgs e)
        {
            var handler = Events[_hotspotReleaseClickEventKey] as EventHandler<HotspotClickEventArgs>;
            if (handler != null)
                handler(this, e);
        }


        /// <summary>
        ///     Raises the <see cref="IndicatorClick"/> event.
        /// </summary>
        /// <param name="e">An <see cref="ScintillaMouseEventArgs"/> that contains the event data.</param>
        protected virtual void OnIndicatorClick(ScintillaMouseEventArgs e)
        {
            var handler = Events[_indicatorClickEventKey] as EventHandler<ScintillaMouseEventArgs>;
            if (handler != null)
                handler(this, e);
        }


        /// <summary>
        ///     Overridden. See <see cref="Control.OnKeyDown"/>.
        /// </summary>
        protected override void OnKeyDown(KeyEventArgs e)
        {
            base.OnKeyDown(e);
            if (!e.Handled)
                e.SuppressKeyPress = this._commands.ProcessKey(e);
        }


        /// <summary>
        ///     Overridden. See <see cref="Control.OnKeyPress"/>.
        /// </summary>
        protected override void OnKeyPress(KeyPressEventArgs e)
        {
            if (this._supressControlCharacters && e.KeyChar < 32)
                e.Handled = true;

            if (this._snippets.IsEnabled && this._snippets.IsOneKeySelectionEmbedEnabled && this._selection.Length > 0)
            {
                Snippet s;
                if (this._snippets.List.TryGetValue(e.KeyChar.ToString(), out s))
                {
                    if (s.IsSurroundsWith)
                    {
                        this._snippets.InsertSnippet(s);
                        e.Handled = true;
                    }
                }
            }

            base.OnKeyPress(e);
        }


        /// <summary>
        ///     Raises the <see cref="LinesNeedShown"/> event.
        /// </summary>
        /// <param name="e">An <see cref="LinesNeedShownEventArgs"/> that contains the event data.</param>
        protected virtual void OnLinesNeedShown(LinesNeedShownEventArgs e)
        {
            var handler = Events[_linesNeedShownEventKey] as EventHandler<LinesNeedShownEventArgs>;
            if (handler != null)
                handler(this, e);
        }


        /// <summary>
        ///     Raises the <see cref="Load"/> event.
        /// </summary>
        /// <param name="e">An <see cref="EventArgs"/> that contains the event data.</param>
        protected virtual void OnLoad(EventArgs e)
        {
            var handler = Events[_loadEventKey] as EventHandler;
            if (handler != null)
                handler(this, e);
        }


        /// <summary>
        ///     Overridden. See <see cref="Control.OnLostFocus"/>.
        /// </summary>
        protected override void OnLostFocus(EventArgs e)
        {
            if (this.Selection.HideSelection)
                this._ns.HideSelection(true);

            this._ns.SetSelBack(this.Selection.BackColorUnfocused != Color.Transparent, Utilities.ColorToRgb(this.Selection.BackColorUnfocused));
            this._ns.SetSelFore(this.Selection.ForeColorUnfocused != Color.Transparent, Utilities.ColorToRgb(this.Selection.ForeColorUnfocused));

            base.OnLostFocus(e);
        }


        /// <summary>
        ///     Raises the <see cref="MacroRecord"/> event.
        /// </summary>
        /// <param name="e">An <see cref="MacroRecordEventArgs"/> that contains the event data.</param>
        protected virtual void OnMacroRecord(MacroRecordEventArgs e)
        {
            var handler = Events[_macroRecordEventKey] as EventHandler<MacroRecordEventArgs>;
            if (handler != null)
                handler(this, e);
        }


        /// <summary>
        ///     Raises the <see cref="MarginClick"/> event.
        /// </summary>
        /// <param name="e">An <see cref="MarginClickEventArgs"/> that contains the event data.</param>
        protected virtual void OnMarginClick(MarginClickEventArgs e)
        {
            var handler = Events[_marginClickEventKey] as EventHandler<MarginClickEventArgs>;
            if (handler != null)
                handler(this, e);

            if (e.ToggleMarkerNumber >= 0)
            {
                var mask = (int)Math.Pow(2, e.ToggleMarkerNumber);
                if ((e.Line.GetMarkerMask() & mask) == mask)
                    e.Line.DeleteMarker(e.ToggleMarkerNumber);
                else
                    e.Line.AddMarker(e.ToggleMarkerNumber);
            }

            if (e.ToggleFold)
                e.Line.ToggleFoldExpanded();
        }


        /// <summary>
        ///     Raises the <see cref="MarkerChanged"/> event.
        /// </summary>
        /// <param name="e">An <see cref="MarkerChangedEventArgs"/> that contains the event data.</param>
        protected virtual void OnMarkerChanged(MarkerChangedEventArgs e)
        {
            var handler = Events[_markerChangedEventKey] as EventHandler<MarkerChangedEventArgs>;
            if (handler != null)
                handler(this, e);
        }


        /// <summary>
        ///     Raises the <see cref="ModifiedChanged"/> event.
        /// </summary>
        /// <param name="e">An <see cref="EventArgs"/> that contains the event data.</param>
        protected virtual void OnModifiedChanged(EventArgs e)
        {
            var handler = Events[_modifiedChangedEventKey] as EventHandler;
            if (handler != null)
                handler(this, e);
        }


        /// <summary>
        ///     Overridden. See <see cref="Control.OnPaint"/>.
        /// </summary>
        protected override void OnPaint(PaintEventArgs e)
        {
            base.OnPaint(e);

            this.paintRanges(e.Graphics);
        }


        /// <summary>
        ///     Raises the <see cref="ReadOnlyModifyAttempt"/> event.
        /// </summary>
        /// <param name="e">An <see cref="EventArgs"/> that contains the event data.</param>
        protected virtual void OnReadOnlyModifyAttempt(EventArgs e)
        {
            var handler = Events[_readOnlyModifyAttemptEventKey] as EventHandler;
            if (handler != null)
                handler(this, e);
        }


        /// <summary>
        ///     Raises the <see cref="Scroll"/> event.
        /// </summary>
        /// <param name="e">An <see cref="ScrollEventArgs"/> that contains the event data.</param>
        protected virtual void OnScroll(ScrollEventArgs e)
        {
            var handler = Events[_scrollEventKey] as EventHandler<ScrollEventArgs>;
            if (handler != null)
                handler(this, e);
        }


        /// <summary>
        ///     Raises the <see cref="SelectionChanged"/> event.
        /// </summary>
        /// <param name="e">An <see cref="EventArgs"/> that contains the event data.</param>
        protected virtual void OnSelectionChanged(EventArgs e)
        {
            //this is being fired in tandem with the cursor blink...
            var handler = Events[_selectionChangedEventKey] as EventHandler;
            if (handler != null)
                handler(this, e);

            if (this._isBraceMatching && (this._selection.Length == 0))
            {
                int position = this.CurrentPos - 1,
                    bracePosStart = -1,
                    bracePosEnd = -1;

                char character = this.CharAt(position);

                switch (character)
                {
                    case '{':
                    case '}':
                    case '(':
                    case ')':
                    case '[':
                    case ']':
                        if (!this.PositionIsOnComment(position))
                        {
                            bracePosStart = position;
                            bracePosEnd = this._ns.BraceMatch(position,0);

                            if(bracePosEnd >= 0)
                            {
                                this._ns.BraceHighlight(bracePosStart, bracePosEnd);
                            }
                            else
                            {
                                this._ns.BraceBadLight(bracePosStart);
                            }
                        }
                        break;
                    default:
                        position = this.CurrentPos;
                        character = this.CharAt(position); //this is not being used anywhere... --Cory
                        this._ns.BraceHighlight(bracePosStart, bracePosEnd);
                        break;
                }
            }
        }


        /// <summary>
        ///     Raises the <see cref="StyleNeeded"/> event.
        /// </summary>
        /// <param name="e">An <see cref="StyleNeededEventArgs"/> that contains the event data.</param>
        protected virtual void OnStyleNeeded(StyleNeededEventArgs e)
        {
            var handler = Events[_styleNeededEventKey] as EventHandler<StyleNeededEventArgs>;
            if (handler != null)
                handler(this, e);
        }


        /// <summary>
        ///     Raises the <see cref="TextDeleted"/> event.
        /// </summary>
        /// <param name="e">An <see cref="TextModifiedEventArgs"/> that contains the event data.</param>
        protected virtual void OnTextDeleted(TextModifiedEventArgs e)
        {
            var handler = Events[_textDeletedEventKey] as EventHandler<TextModifiedEventArgs>;
            if (handler != null)
                handler(this, e);
        }


        /// <summary>
        ///     Raises the <see cref="TextInserted"/> event.
        /// </summary>
        /// <param name="e">An <see cref="TextModifiedEventArgs"/> that contains the event data.</param>
        protected virtual void OnTextInserted(TextModifiedEventArgs e)
        {
            var handler = Events[_textInsertedEventKey] as EventHandler<TextModifiedEventArgs>;
            if (handler != null)
                handler(this, e);
        }


        /// <summary>
        ///     Raises the <see cref="ZoomChanged"/> event.
        /// </summary>
        /// <param name="e">An <see cref="EventArgs"/> that contains the event data.</param>
        protected virtual void OnZoomChanged(EventArgs e)
        {
            var handler = Events[_zoomChangedEventKey] as EventHandler;
            if (handler != null)
                handler(this, e);
        }


        private void paintRanges(Graphics g)
        {
            //	First we want to get the range (in positions) of what
            //	will be painted so that we know which markers to paint
            int firstLine = this._ns.GetFirstVisibleLine();
            int lastLine = firstLine + this._ns.LinesOnScreen();
            int firstPos = this._ns.PositionFromLine(firstLine);
            int lastPos = this._ns.PositionFromLine(lastLine + 1) - 1;

            //	If the lastLine was outside the defined document range it will
            //	contain -1, defualt it to the last doc position
            if (lastPos < 0)
                lastPos = this._ns.GetLength();

            List<ManagedRange> mrs = this.ManagedRangesInRange(firstPos, lastPos);


            g.SmoothingMode = SmoothingMode.AntiAlias;
            foreach (ManagedRange mr in mrs)
            {
                mr.Paint(g);
            }
        }


        public int PointXFromPosition(int position)
        {
            return this._ns.PointXFromPosition(position);
        }


        public int PointYFromPosition(int position)
        {
            return this._ns.PointYFromPosition(position);
        }


        public int PositionFromPoint(int x, int y)
        {
            return this._ns.PositionFromPoint(x, y);
        }


        public int PositionFromPointClose(int x, int y)
        {
            return this._ns.PositionFromPointClose(x, y);
        }


        /// <summary>
        ///     Checks that if the specified position is on comment.
        /// </summary>
        public bool PositionIsOnComment(int position)
        {
            //this.Colorize(0, -1);
            return this.PositionIsOnComment(position, this._lexing.Lexer);
        }


        /// <summary>
        ///     Checks that if the specified position is on comment.
        /// </summary>
        public bool PositionIsOnComment(int position, Lexer lexer)
        {
            int style = this._styles.GetStyleAt(position);
            if ((lexer == Lexer.Python || lexer == Lexer.Lisp)
                && (style == 1
                || style == 12))
            {
                return true; // python or lisp
            }
            else if ((lexer == Lexer.Cpp || lexer == Lexer.Pascal || lexer == Lexer.Tcl || lexer == Lexer.Bullant)
                && (style == 1
                || style == 2
                || style == 3
                || style == 15
                || style == 17
                || style == 18))
            {
                return true; // cpp, tcl, bullant or pascal
            }
            else if ((lexer == Lexer.Hypertext || lexer == Lexer.Xml)
                && (style == 9
                || style == 20
                || style == 29
                || style == 30
                || style == 42
                || style == 43
                || style == 44
                || style == 57
                || style == 58
                || style == 59
                || style == 72
                || style == 82
                || style == 92
                || style == 107
                || style == 124
                || style == 125))
            {
                return true; // html or xml
            }
            else if ((lexer == Lexer.Perl || lexer == Lexer.Ruby || lexer == Lexer.Clw || lexer == Lexer.Bash)
                && style == 2)
            {
                return true; // perl, bash, clarion/clw or ruby
            }
            else if ((lexer == Lexer.Sql)
                && (style == 1
                || style == 2
                || style == 3
                || style == 13
                || style == 15
                || style == 17
                || style == 18))
            {
                return true; // sql
            }
            else if ((lexer == Lexer.VB || lexer == Lexer.Properties || lexer == Lexer.MakeFile || lexer == Lexer.Batch || lexer == Lexer.Diff || lexer == Lexer.Conf || lexer == Lexer.Ave || lexer == Lexer.Eiffel || lexer == Lexer.EiffelKw || lexer == Lexer.Tcl || lexer == Lexer.VBScript || lexer == Lexer.MatLab || lexer == Lexer.Fortran || lexer == Lexer.F77 || lexer == Lexer.Lout || lexer == Lexer.Mmixal || lexer == Lexer.Yaml || lexer == Lexer.PowerBasic || lexer == Lexer.ErLang || lexer == Lexer.Octave || lexer == Lexer.Kix || lexer == Lexer.Asn1)
                && style == 1)
            {
                return true; // asn1, vb, diff, _batch, makefile, avenue, eiffel, eiffelkw, vbscript, matlab, crontab, fortran, f77, lout, mmixal, yaml, powerbasic, erlang, octave, kix or properties
            }
            else if ((lexer == Lexer.Latex)
                && style == 4)
            {
                return true; // latex
            }
            else if ((lexer == Lexer.Lua || lexer == Lexer.EScript || lexer == Lexer.Verilog)
                && (style == 1
                || style == 2
                || style == 3))
            {
                return true; // lua, verilog or escript
            }
            else if ((lexer == Lexer.Ada)
                && style == 10)
            {
                return true; // ada
            }
            else if ((lexer == Lexer.Baan || lexer == Lexer.Pov || lexer == Lexer.Ps || lexer == Lexer.Forth || lexer == Lexer.MsSql || lexer == Lexer.Gui4Cli || lexer == Lexer.Au3 || lexer == Lexer.Apdl || lexer == Lexer.Vhdl || lexer == Lexer.Rebol)
                && (style == 1
                || style == 2))
            {
                return true; // au3, apdl, baan, ps, mssql, rebol, forth, gui4cli, vhdl or pov
            }
            else if ((lexer == Lexer.Asm)
                && (style == 1
                || style == 11))
            {
                return true; // asm
            }
            else if ((lexer == Lexer.Nsis)
                && (style == 1
                || style == 18))
            {
                return true; // nsis
            }
            else if ((lexer == Lexer.Specman)
                && (style == 2
                || style == 3))
            {
                return true; // specman
            }
            else if ((lexer == Lexer.Tads3)
                && (style == 3
                || style == 4))
            {
                return true; // tads3
            }
            else if ((lexer == Lexer.CSound)
                && (style == 1
                || style == 9))
            {
                return true; // csound
            }
            else if ((lexer == Lexer.Caml)
                && (style == 12
                || style == 13
                || style == 14
                || style == 15))
            {
                return true; // caml
            }
            else if ((lexer == Lexer.Haskell)
                && (style == 13
                || style == 14
                || style == 15
                || style == 16))
            {
                return true; // haskell
            }
            else if ((lexer == Lexer.Flagship)
                && (style == 1
                || style == 2
                || style == 3
                || style == 4
                || style == 5
                || style == 6))
            {
                return true; // flagship
            }
            else if ((lexer == Lexer.Smalltalk)
                && style == 3)
            {
                return true; // smalltalk
            }
            else if ((lexer == Lexer.Css)
                && style == 9)
            {
                return true; // css
            }
            return false;
        }


        /// <summary>
        ///     Overridden. See <see cref="Control.ProcessKeyMessage"/>.
        /// </summary>
        protected override bool ProcessKeyMessage(ref Message m)
        {
            //	For some reason IsInputKey isn't working for
            //	Key.Enter. This seems to make it work as expected
            if ((int)m.WParam == (int)Keys.Enter && !this.AcceptsReturn)
            {
                return true;
            }
            else
            {
                return base.ProcessKeyMessage(ref m);
            }
        }


        private void ResetCaption()
        {
            this.Caption = GetType().FullName;
        }


        private void ResetMargins()
        {
            this._margins.Reset();
        }


        private void ResetStyles()
        {
            // One of the core appearance properties has changed. When this happens
            // we restyle the document (overriding any existing styling) in the core
            // appearance properties. This behavior is consistent with the RichTextBox.
            this.NativeInterface.StartStyling(0, 0x7F);
            this.NativeInterface.SetStyling(this.NativeInterface.GetLength(), 0);
            this.Styles[0].Reset();
            this.Styles[0].Font = Font;
            this.Styles[0].ForeColor = this.ForeColor;
            this.Styles[0].BackColor = this.BackColor;
            this.Styles.Default.BackColor = this.BackColor;
        }


        /// <summary>
        ///     Custom way to find the matching brace when BraceMatch() does not work
        /// </summary>
        internal int SafeBraceMatch(int position)
        {
            int match = this.CharAt(position);
            int toMatch = 0;
            int length = this.TextLength;
            int ch;
            int sub = 0;
            Lexer lexer = this._lexing.Lexer;
            this._lexing.Colorize(0, -1);
            bool comment = this.PositionIsOnComment(position, lexer);
            switch (match)
            {
                case '{':
                    toMatch = '}';
                    goto down;
                case '(':
                    toMatch = ')';
                    goto down;
                case '[':
                    toMatch = ']';
                    goto down;
                case '}':
                    toMatch = '{';
                    goto up;
                case ')':
                    toMatch = '(';
                    goto up;
                case ']':
                    toMatch = '[';
                    goto up;
            }
            return -1;
        // search up
        up:
            while (position >= 0)
            {
                position--;
                ch = this.CharAt(position);
                if (ch == match)
                {
                    if (comment == this.PositionIsOnComment(position, lexer)) sub++;
                }
                else if (ch == toMatch && comment == this.PositionIsOnComment(position, lexer))
                {
                    sub--;
                    if (sub < 0) return position;
                }
            }
            return -1;
        // search down
        down:
            while (position < length)
            {
                position++;
                ch = this.CharAt(position);
                if (ch == match)
                {
                    if (comment == this.PositionIsOnComment(position, lexer)) sub++;
                }
                else if (ch == toMatch && comment == this.PositionIsOnComment(position, lexer))
                {
                    sub--;
                    if (sub < 0) return position;
                }
            }
            return -1;
        }


        private void ScnModified(ref NativeMethods.SCNotification scn)
        {
            if ((scn.modificationType & NativeMethods.SC_MOD_CHANGEANNOTATION) == NativeMethods.SC_MOD_CHANGEANNOTATION)
            {
                var acea = new AnnotationChangedEventArgs(scn.line, scn.annotationLinesAdded);
                this.OnAnnotationChanged(acea);
            }
        }


        /// <summary>
        ///     Sets the application-wide default module name of the native Scintilla library.
        /// </summary>
        /// <param name="moduleName">The native Scintilla module name.</param>
        /// <remarks>This method must be called prior to the first <see cref="Scintilla"/> control being created.</remarks>
        /// <exception cref="ArgumentNullException">The <paramref name="moduleName"/> is <chr>null</chr>.</exception>
        /// <exception cref="ArgumentException">The <paramref name="moduleName"/> is an empty string.</exception>
        /// <exception cref="InvalidOperationException">This method was called after the first <see cref="Scintilla"/> control was created.</exception>
        public static void SetModuleName(string moduleName)
        {
            const string paramName = "moduleName";

            if (moduleName == null)
                throw new ArgumentNullException(paramName);

            if (moduleName.Length == 0)
                throw new ArgumentException(string.Format(Resources.Culture, Resources.Exception_EmptyStringArgument, paramName), paramName);

            if (_moduleHandle != IntPtr.Zero)
                throw new InvalidOperationException(Resources.Exception_ModuleAlreadyLoaded);

            _moduleName = moduleName;
        }


        private bool ShouldSerializeAnnotations()
        {
            return this._annotations != null && this._annotations.ShouldSerialize();
        }


        private bool ShouldSerializeAutoComplete()
        {
            return this._autoComplete.ShouldSerialize();
        }


        private bool ShouldSerializeCallTip()
        {
            return this._callTip.ShouldSerialize();
        }


        private bool ShouldSerializeCaption()
        {
            return this.Caption != GetType().FullName;
        }


        private bool ShouldSerializeCaret()
        {
            return this._caret.ShouldSerialize();
        }


        private bool ShouldSerializeClipboard()
        {
            return this._clipboard.ShouldSerialize();
        }


        private bool ShouldSerializeCommands()
        {
            return this._commands.ShouldSerialize();
        }


        private bool ShouldSerializeConfigurationManager()
        {
            return this._configurationManager.ShouldSerialize();
        }


        private bool ShouldSerializeDocumentNavigation()
        {
            return this._documentNavigation.ShouldSerialize();
        }


        private bool ShouldSerializeDropMarkers()
        {
            return this._dropMarkers.ShouldSerialize();
        }


        private bool ShouldSerializeEndOfLine()
        {
            return this._endOfLine.ShouldSerialize();
        }


        private bool ShouldSerializeFindReplace()
        {
            return this._findReplace.ShouldSerialize();
        }


        private bool ShouldSerializeFolding()
        {
            return this._folding.ShouldSerialize();
        }


        private bool ShouldSerializeHotspotStyle()
        {
            return this._hotspotStyle.ShouldSerialize();
        }


        private bool ShouldSerializeIndentation()
        {
            return this._indentation.ShouldSerialize();
        }


        private bool ShouldSerializeLexing()
        {
            return this._lexing.ShouldSerialize();
        }


        private bool ShouldSerializeLineWrapping()
        {
            return this.LineWrapping.ShouldSerialize();
        }


        private bool ShouldSerializeLongLines()
        {
            return this._longLines.ShouldSerialize();
        }


        private bool ShouldSerializeMargins()
        {
            return this._margins.ShouldSerialize();
        }


        private bool ShouldSerializeMarkers()
        {
            return this._markers.ShouldSerialize();
        }


        private bool ShouldSerializePrinting()
        {
            return this._printing.ShouldSerialize();
        }


        private bool ShouldSerializeScrolling()
        {
            return this._scrolling.ShouldSerialize();
        }


        private bool ShouldSerializeSelection()
        {
            return this._selection.ShouldSerialize();
        }


        private bool ShouldSerializeSnippets()
        {
            return this._snippets.ShouldSerialize();
        }


        private bool ShouldSerializeStyles()
        {
            return this._styles.ShouldSerialize();
        }


        public bool ShouldSerializeUndoRedo()
        {
            return this._undoRedo.ShouldSerialize();
        }


        private void WmReflectCommand(ref Message m)
        {
            switch(Utilities.SignedHiWord(m.WParam))
            {
                case NativeMethods.SCEN_CHANGE:
                    // TODO It looks like NoteTextChanged is firing twice for every change.
                    // This appears to be a Scintilla behavior, not us, but we might be able to work around it.
                    OnTextChanged(EventArgs.Empty);
                    break;

                default:
                    base.WndProc(ref m);
                    break;
            }
        }


        private void WmReflectNotify(ref Message m)
        {
            // New *internal* structure...
            var scn = (NativeMethods.SCNotification)Marshal.PtrToStructure(m.LParam, typeof(NativeMethods.SCNotification));

            // Old *public* *outdated* structure and event args...
            var scnOld = (SCNotification)Marshal.PtrToStructure(m.LParam, typeof(SCNotification));
            var nsea = new NativeScintillaEventArgs(m, scnOld);

            switch (scnOld.nmhdr.code)
            {
                case Constants.SCN_AUTOCSELECTION:
                    this.FireAutoCSelection(nsea);
                    break;

                case Constants.SCN_CALLTIPCLICK:
                    FireCallTipClick(nsea);
                    break;

                case Constants.SCN_CHARADDED:
                    this.FireCharAdded(nsea);
                    break;

                case Constants.SCN_DOUBLECLICK:
                    this.FireDoubleClick(nsea);
                    break;

                case Constants.SCN_DWELLEND:
                    this.FireDwellEnd(nsea);
                    break;

                case Constants.SCN_DWELLSTART:
                    this.FireDwellStart(nsea);
                    break;

                case NativeMethods.SCN_HOTSPOTCLICK:
                    this.OnHotspotClick(new HotspotClickEventArgs(scn.position));
                    break;

                case NativeMethods.SCN_HOTSPOTDOUBLECLICK:
                    this.OnHotspotDoubleClick(new HotspotClickEventArgs(scn.position));
                    break;

                case NativeMethods.SCN_HOTSPOTRELEASECLICK:
                    this.OnHotspotReleaseClick(new HotspotClickEventArgs(scn.position));
                    break;

                case Constants.SCN_INDICATORCLICK:
                    this.FireIndicatorClick(nsea);
                    break;

                case Constants.SCN_INDICATORRELEASE:
                    this.FireIndicatorRelease(nsea);
                    break;

                case Constants.SCN_KEY:
                    this.FireKey(nsea);
                    break;

                case Constants.SCN_MACRORECORD:
                    this.FireMacroRecord(nsea);
                    break;

                case Constants.SCN_MARGINCLICK:
                    FireMarginClick(nsea);
                    break;

                case Constants.SCN_MODIFIED:
                    this.ScnModified(ref scn);
                    this.FireModified(nsea);
                    break;

                case Constants.SCN_MODIFYATTEMPTRO:
                    this.FireModifyAttemptRO(nsea);
                    break;

                case Constants.SCN_NEEDSHOWN:
                    this.FireNeedShown(nsea);
                    break;

                case Constants.SCN_PAINTED:
                    this.FirePainted(nsea);
                    break;

                case Constants.SCN_SAVEPOINTLEFT:
                    this.FireSavePointLeft(nsea);
                    break;

                case Constants.SCN_SAVEPOINTREACHED:
                    this.FireSavePointReached(nsea);
                    break;

                case Constants.SCN_STYLENEEDED:
                    this.FireStyleNeeded(nsea);
                    break;

                case Constants.SCN_UPDATEUI:
                    this.FireUpdateUI(nsea);
                    break;

                case Constants.SCN_URIDROPPED:
                    this.FireUriDropped(nsea);
                    break;

                case Constants.SCN_USERLISTSELECTION:
                    this.FireUserListSelection(nsea);
                    break;

                case Constants.SCN_ZOOM:
                    this.FireZoom(nsea);
                    break;
            }
        }


        private void WmScroll(ref Message m)
        {
            var so = ScrollOrientation.VerticalScroll;
            int oldScroll = 0, newScroll = 0;
            var set = (ScrollEventType)(Utilities.SignedLoWord(m.WParam));
            if (m.Msg == NativeMethods.WM_HSCROLL)
            {
                so = ScrollOrientation.HorizontalScroll;
                oldScroll = this._ns.GetXOffset();

                //	Let Scintilla Handle the scroll Message to actually perform scrolling
                base.WndProc(ref m);
                newScroll = this._ns.GetXOffset();
            }
            else
            {
                so = ScrollOrientation.VerticalScroll;
                oldScroll = this._ns.GetFirstVisibleLine();
                base.WndProc(ref m);
                newScroll = this._ns.GetFirstVisibleLine();
            }

            this.OnScroll(new ScrollEventArgs(set, oldScroll, newScroll, so));
        }


        /// <summary>
        ///     Overridden. Processes Windows messages.
        /// </summary>
        /// <param name="m">The Windows <see cref="Message" /> to process.</param>
        protected override void WndProc(ref Message m)
        {
            switch (m.Msg)
            {
                case NativeMethods.WM_DESTROY:
                    // wi11811 2008-07-28 Chris Rickard
                    // If we get a destroy message we make this window a message-only window so that it doesn't actually
                    // get destroyed, causing Scintilla to wipe out all its settings associated with this window handle.
                    // We do send a WM_DESTROY message to Scintilla in the Dispose() method so that it does clean up its
                    // resources when this control is actually done with. Credit (blame :) goes to tom103 for figuring
                    // this one out.

                    if (IsHandleCreated)
                    {
                        NativeMethods.SetParent(Handle, NativeMethods.HWND_MESSAGE);
                        return;
                    }

                    base.WndProc(ref m);
                    break;

                case NativeMethods.WM_PAINT:
                    // I tried toggling the ControlStyles.UserPaint flag and sending the message
                    // to both base.WndProc and DefWndProc in order to get the best of both worlds,
                    // Scintilla Paints as normal and .NET fires the Paint Event with the proper
                    // clipping regions and such. This didn't work too well, I kept getting weird
                    // phantom paints, or sometimes the .NET paint events would seem to get painted
                    // over by Scintilla. This technique I use below seems to work perfectly.

                    base.WndProc(ref m);
                    if (this._isCustomPaintingEnabled)
                    {
                        RECT r;
                        if (!NativeMethods.GetUpdateRect(Handle, out r, false))
                            r = ClientRectangle;

                        Graphics g = CreateGraphics();
                        g.SetClip(r);

                        this.OnPaint(new PaintEventArgs(CreateGraphics(), r));
                    }
                    break;

                case NativeMethods.WM_DROPFILES:
                    this.HandleFileDrop(m.WParam);
                    break;

                case NativeMethods.WM_SETCURSOR:
                    base.DefWndProc(ref m);
                    break;

                case NativeMethods.WM_GETTEXT:
                    m.WParam = (IntPtr)(this.Caption.Length + 1);
                    Marshal.Copy(this.Caption.ToCharArray(), 0, m.LParam, this.Caption.Length);
                    m.Result = (IntPtr)this.Caption.Length;
                    break;

                case NativeMethods.WM_GETTEXTLENGTH:
                    m.Result = (IntPtr)this.Caption.Length;
                    break;

                case NativeMethods.WM_REFLECT + NativeMethods.WM_NOTIFY:
                    this.WmReflectNotify(ref m);
                    break;

                case NativeMethods.WM_REFLECT + NativeMethods.WM_COMMAND:
                    this.WmReflectCommand(ref m);
                    break;

                case NativeMethods.WM_HSCROLL:
                case NativeMethods.WM_VSCROLL:
                    this.WmScroll(ref m);
                    break;

                default:
                    if (m.Msg >= 10000) // TODO Remove "magic number"
                    {
                        this._commands.Execute((BindableCommand)m.Msg);
                        return;
                    }

                    base.WndProc(ref m);
                    break;
            }
        }


        public void ZoomIn()
        {
            this._ns.ZoomIn();
        }


        private void ZoomOut()
        {
            this._ns.ZoomOut();
        }

        #endregion Methods


        #region Properties

        /// <summary>
        ///     Gets or sets a value indicating whether pressing ENTER creates a new line of text in the
        ///     control or activates the default button for the form.
        /// </summary>
        /// <returns>
        ///     <chr>true</chr> if the ENTER key creates a new line of text; <chr>false</chr> if the ENTER key activates
        ///     the default button for the form. The default is <chr>false</chr>.
        /// </returns>
        [DefaultValue(true), Category("Behavior")]
        [Description("Indicates if return characters are accepted as text input.")]
        public bool AcceptsReturn
        {
            get { return this._state[_acceptsReturnState]; }
            set { this._state[_acceptsReturnState] = value; }
        }


        /// <summary>
        ///     Gets or sets a value indicating whether pressing the TAB key types a TAB character in the control
        ///     instead of moving the focus to the next control in the tab order.
        /// </summary>
        /// <returns>
        ///     <chr>true</chr> if users can enter tabs using the TAB key; <chr>false</chr> if pressing the TAB key
        ///     moves the focus. The default is <chr>false</chr>.
        /// </returns>
        [DefaultValue(true), Category("Behavior")]
        [Description("Indicates if tab characters are accepted as text input.")]
        public bool AcceptsTab
        {
            get { return this._state[_acceptsTabState]; }
            set { this._state[_acceptsTabState] = value; }
        }


        /// <summary>
        ///     Gets or sets if .NET Drag and Drop operations are supported.
        /// </summary>
        public override bool AllowDrop
        {
            get
            {
                return this._allowDrop;
            }
            set
            {
                NativeMethods.DragAcceptFiles(Handle, value);
                this._allowDrop = value;
            }
        }


        /// <summary>
        ///     Gets a collection containing all annotations in the control.
        /// </summary>
        /// <returns>
        ///     A <see cref="AnnotationCollection" /> that contains all the annotations in the <see cref="Scintilla" /> control.
        /// </returns>
        [Category("Appearance")]
        [Description("The annotations and options.")]
        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content)]
        public AnnotationCollection Annotations
        {
            get
            {
                if (this._annotations == null)
                    this._annotations = this.CreateAnnotationsInstance();

                return this._annotations;
            }
        }


        /// <summary>
        ///     Controls autocompletion behavior.
        /// </summary>
        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content), Category("Behavior")]
        public AutoComplete AutoComplete
        {
            get
            {
                return this._autoComplete;
            }
        }


        /// <summary>
        ///     Gets or sets the background color for the control.
        /// </summary>
        /// <value>
        ///     A <see cref="Color"/> that represents the background color of the control.
        ///     The default is <see cref="SystemColors.Window"/>.
        /// </value>
        /// <remarks>Settings this property resets any current document styling.</remarks>
        [DefaultValue(typeof(Color), "Window")]
        public override Color BackColor
        {
            get { return base.BackColor; }
            set { base.BackColor = value; }
        }


        /// <summary>
        ///     This property is not relevant for this class.
        /// </summary>
        [Browsable(false), EditorBrowsable(EditorBrowsableState.Never)]
        public override Image BackgroundImage
        {
            get { return base.BackgroundImage; }
            set { base.BackgroundImage = value; }
        }


        /// <summary>
        ///     This property is not relevant for this class.
        /// </summary>
        [Browsable(false), EditorBrowsable(EditorBrowsableState.Never)]
        public override ImageLayout BackgroundImageLayout
        {
            get { return base.BackgroundImageLayout; }
            set { base.BackgroundImageLayout = value; }
        }


        /// <summary>
        ///     Gets or sets the border style of the control.
        /// </summary>
        /// <value>
        ///     A <see cref="System.Windows.Forms.BorderStyle" /> that represents the border type of the control.
        ///     The default is <see cref="System.Windows.Forms.BorderStyle.Fixed3D" />.
        /// </value>
        /// <exception cref="InvalidEnumArgumentException">
        ///     The value assigned is not one of the <see cref="System.Windows.Forms.BorderStyle" /> values.
        /// </exception>
        [DefaultValue(BorderStyle.Fixed3D), Category("Appearance")]
        [Description("Indicates whether the control should have a border.")] // TODO Move to a resource
        public BorderStyle BorderStyle
        {
            get
            {
                return this._borderStyle;
            }
            set
            {
                if (!Enum.IsDefined(typeof(BorderStyle), value))
                    throw new InvalidEnumArgumentException("value", (int)value, typeof(BorderStyle));

                if (value != this._borderStyle)
                {
                    this._borderStyle = value;

                    // This will cause the CreateParams to be reapplied
                    UpdateStyles();

                    this.OnBorderStyleChanged(EventArgs.Empty);
                }
            }
        }


        /// <summary>
        ///     Manages CallTip (Visual Studio-like code Tooltip) behaviors
        /// </summary>
        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content), Category("Behavior")]
        public CallTip CallTip
        {
            get
            {
                return this._callTip;
            }
            set
            {
                this._callTip = value;
            }
        }


        /// <summary>
        ///     Gets/Sets the Win32 Window Caption. Defaults to Type's FullName
        /// </summary>
        [Category("Behavior")]
        [Description("Win32 Window Caption")]
        public string Caption
        {
            get { return this._caption; }
            set
            {
                if (this._caption != value)
                {
                    this._caption = value;

                    //	Triggers a new WM_GETTEXT query
                    base.Text = value;
                }

            }
        }


        /// <summary>
        ///     Controls Caret Behavior
        /// </summary>
        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content), Category("Appearance")]
        public CaretInfo Caret
        {
            get
            {
                return this._caret;
            }
        }


        /// <summary>
        ///     Gets Clipboard access for the control.
        /// </summary>
        /// <returns>A <see cref="Clipboard" /> object the provides Clipboard access for the control.</returns>
        [Category("Behavior")] // TODO Place in resource file
        [Description("Clipboard (cut, copy, paste) options.")] // TODO Place in resource file
        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content)]
        public Clipboard Clipboard
        {
            get
            {
                return this._clipboard;
            }
        }


        internal Dictionary<string, Color> ColorBag { get { return this._colorBag; } }


        /// <summary>
        ///     Controls behavior of keyboard bound commands.
        /// </summary>
        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content), Category("Behavior")]
        public Commands Commands
        {
            get
            {
                return this._commands;
            }
            set
            {
                this._commands = value;
            }
        }


        /// <summary>
        ///     Controls behavior of loading/managing ARCed.Scintilla configurations.
        /// </summary>
        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content), Category("Behavior")]
        public ConfigurationManager ConfigurationManager
        {
            get
            {
                return this._configurationManager;
            }
            set
            {
                this._configurationManager = value;
            }
        }


        /// <summary>
        ///     Overridden. See <see cref="Control.CreateParams"/>.
        /// </summary>
        protected override CreateParams CreateParams
        {
            [SecurityPermission(SecurityAction.LinkDemand, Flags = SecurityPermissionFlag.UnmanagedCode)]
            get
            {
                // Otherwise Scintilla won't paint. When UserPaint is set to
                // true the base Class (Control) eats the WM_PAINT message.
                // Of course when this set to false we can't use the Paint
                // events. This is why I'm relying on the Paint notification
                // sent from scintilla to paint the Marker Arrows.
                SetStyle(ControlStyles.UserPaint, false);

                // I hope the old man got that tractor beam out if commission,
                // or this is going to be a real short trip. Okay, hit it!
                LoadModule();

                // Tell Windows Forms to create a Scintilla
                // derived Window Class for this control
                CreateParams cp = base.CreateParams;
                cp.ClassName = "Scintilla";

                // Set the window style or extended style
                // to the appropriate border type.
                switch (this._borderStyle)
                {
                    case BorderStyle.Fixed3D:
                        cp.ExStyle |= NativeMethods.WS_EX_CLIENTEDGE;
                        cp.Style &= ~NativeMethods.WS_BORDER;
                        break;

                    case BorderStyle.FixedSingle:
                        cp.ExStyle &= ~NativeMethods.WS_EX_CLIENTEDGE;
                        cp.Style |= NativeMethods.WS_BORDER;
                        break;

                    default:
                        cp.ExStyle &= ~NativeMethods.WS_EX_CLIENTEDGE;
                        cp.Style &= ~NativeMethods.WS_BORDER;
                        break;
                }

                return cp;
            }
        }


        /// <summary>
        ///     Gets or sets the character index of the current caret position.
        /// </summary>
        /// <returns>The character index of the current caret position.</returns>
        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public int CurrentPos
        {
            get
            {
                return this.NativeInterface.GetCurrentPos();
            }
            set
            {
                this.NativeInterface.GotoPos(value);
            }
        }


        /// <summary>Gets or sets the default cursor for the control.</summary>
        /// <returns>An object of type <see cref="T:System.Windows.Forms.Cursor"></see> representing the current default cursor.</returns>
        protected override Cursor DefaultCursor
        {
            get
            {
                return Cursors.IBeam;
            }
        }


        /// <summary>
        ///     Overridden. See <see cref="Control.DefaultSize"/>.
        /// </summary>
        protected override Size DefaultSize
        {
            get
            {
                return new Size(200, 100);
            }
        }


        /// <summary>
        ///     Controls behavior of Documents
        /// </summary>
        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public DocumentHandler DocumentHandler
        {
            get
            {
                return this._documentHandler;
            }
            set
            {
                this._documentHandler = value;
            }
        }


        /// <summary>
        ///     Controls behavior of automatic document navigation
        /// </summary>
        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content), Category("Behavior")]
        public DocumentNavigation DocumentNavigation
        {
            get
            {
                return this._documentNavigation;
            }
            set
            {
                this._documentNavigation = value;
            }
        }


        /// <summary>
        ///     Controls behavior of Drop Markers
        /// </summary>
        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content), Category("Behavior")]
        public DropMarkers DropMarkers
        {
            get
            {
                return this._dropMarkers;
            }
        }


        /// <summary>
        ///     Controls Encoding behavior
        /// </summary>
        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public Encoding Encoding
        {
            get
            {
                return this._encoding;
            }
            set
            {
                //	EncoderFallbackException isn't really the correct exception but
                //	I'm being lazy and you get the point
                if (!ValidCodePages.Contains(value))
                    throw new EncoderFallbackException("Scintilla only supports the following Encodings: " + ValidCodePages);

                this._encoding = value;
                this._ns.SetCodePage(this._encoding.CodePage);
            }
        }


        /// <summary>
        ///     Controls End Of Line Behavior
        /// </summary>
        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content), Category("Behavior")]
        public EndOfLine EndOfLine
        {
            get
            {
                return this._endOfLine;
            }
            set
            {
                this._endOfLine = value;
            }
        }


        [Category("Behavior")]
        public FindReplace FindReplace
        {
            get
            {
                return this._findReplace;
            }
            set
            {
                this._findReplace = value;
            }
        }


        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content), Category("Behavior")]
        public Folding Folding
        {
            get
            {
                return this._folding;
            }
            set
            {
                this._folding = value;
            }
        }

        /*
        /// <summary>
        ///     Gets or sets the font of the text displayed by the control.
        /// </summary>
        /// <value>
        ///     The <see cref="Font"/> to apply to the text displayed by the control.
        ///     The default is the value of the <see cref="DefaultFont"/> property.
        /// </value>
        /// <remarks>Settings this property resets any current document styling.</remarks>
        public override Font Font
        {
            get { return base.Font; }
            set { base.Font = value; }
        }
        */

        /// <summary>
        ///     Gets or sets the foreground color of the control.
        /// </summary>
        /// <value>
        ///     The foreground <see cref="Color"/> of the control.
        ///     The default is <see cref="SystemColors.WindowText"/>.
        /// </value>
        /// <remarks>Settings this property resets any current document styling.</remarks>
        [DefaultValue(typeof(Color), "WindowText")]
        public override Color ForeColor
        {
            get { return base.ForeColor; }
            set { base.ForeColor = value; }
        }


        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public GoTo GoTo
        {
            get
            {
                return this._goto;
            }
            set
            {
                this._goto = value;
            }
        }


        protected internal List<TopLevelHelper> Helpers
        {
            get
            {
                return this._helpers;
            }
            set
            {
                this._helpers = value;
            }
        }


        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content), Category("Appearance")]
        public HotspotStyle HotspotStyle
        {
            get
            {
                return this._hotspotStyle;
            }
            set
            {
                this._hotspotStyle = value;
            }
        }


        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content), Category("Behavior")]
        public Indentation Indentation
        {
            get
            {
                return this._indentation;
            }
            set
            {
                this._indentation = value;
            }
        }


        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public IndicatorCollection Indicators
        {
            get { return this._indicators; }
        }


        [DefaultValue(false), Category("Behavior")]
        public bool IsBraceMatching
        {
            get { return this._isBraceMatching; }
            set { this._isBraceMatching = value; }
        }


        [DefaultValue(true), Category("Behavior")]
        public bool IsCustomPaintingEnabled
        {
            get
            {
                return this._isCustomPaintingEnabled;
            }
            set
            {
                this._isCustomPaintingEnabled = value;
            }
        }


        internal bool IsDesignMode
        {
            get
            {
                return DesignMode;
            }
        }


        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        internal bool IsInitializing
        {
            get
            {
                return this._isInitializing;
            }
            set
            {
                this._isInitializing = value;
            }
        }


        [DefaultValue(false), Category("Behavior")]
        public bool IsReadOnly
        {
            get
            {
                return this._ns.GetReadOnly();

            }
            set
            {
                this._ns.SetReadOnly(value);
            }
        }


        /// <summary>
        ///     Gets or sets the line layout caching strategy in a <see cref="Scintilla" /> control.
        /// </summary>
        /// <returns>
        ///     One of the <see cref="ARCed.Scintilla.LayoutCacheMode"/> enumeration values.
        ///     The default is <see cref="ARCed.Scintilla.LayoutCacheMode.Caret" />.
        /// </returns>
        /// <exception cref="InvalidEnumArgumentException">
        ///     The value assigned is not one of the <see cref="ARCed.Scintilla.LayoutCacheMode" /> values.
        /// </exception>
        /// <remarks>Larger cache sizes increase performance at the expense of memory.</remarks>
        [Browsable(false)]
        [EditorBrowsable(EditorBrowsableState.Advanced)]
        [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public LayoutCacheMode LayoutCacheMode
        {
            get
            {
                return (LayoutCacheMode)this.DirectMessage(NativeMethods.SCI_GETLAYOUTCACHE, IntPtr.Zero, IntPtr.Zero);
            }
            set
            {
                if (!Enum.IsDefined(typeof(LayoutCacheMode), value))
                    throw new InvalidEnumArgumentException("value", (int)value, typeof(LayoutCacheMode));

                this.DirectMessage(NativeMethods.SCI_SETLAYOUTCACHE, new IntPtr((int)value), IntPtr.Zero);
            }
        }


        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content), Category("Behavior")]
        public Lexing Lexing
        {
            get
            {
                return this._lexing;
            }
            set
            {
                this._lexing = value;
            }
        }


        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public LineCollection Lines
        {
            get
            {

                return this._lines;
            }
        }


        /// <summary>
        ///     Gets an object that controls line wrapping options in the <see cref="Scintilla"/> control.
        /// </summary>
        /// <returns>A <see cref="LineWrapping"/> object that manages line wrapping options in a <see cref="Scintilla"/> control.</returns>
        [Category("Behavior")] // TODO Move to resource file
        [Description("The control's line wrapping options.")] // TODO Move to resource file
        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content)]
        public LineWrapping LineWrapping
        {
            get
            {
                if (this._lineWrapping == null)
                    this._lineWrapping = this.CreateLineWrappingInstance();

                return this._lineWrapping;
            }
        }


        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content), Category("Behavior")]
        public LongLines LongLines
        {
            get
            {
                return this._longLines;
            }
            set
            {
                this._longLines = value;
            }
        }


        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public List<ManagedRange> ManagedRanges
        {
            get { return this._managedRanges; }
        }


        [Browsable(true), DesignerSerializationVisibility(DesignerSerializationVisibility.Content), Category("Appearance")]
        public MarginCollection Margins
        {
            get
            {
                return this._margins;
            }
        }


        /// <summary>
        ///     Gets a collection representing the marker objects and options within the control.
        /// </summary>
        /// <returns>A <see cref="MarkerCollection" /> representing the marker objects and options within the control.</returns>
        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content), Category("Behavior")]
        public MarkerCollection Markers
        {
            get
            {
                return this._markers;
            }
            set
            {
                this._markers = value;
            }
        }


        [DefaultValue(true), Category("Behavior")]
        public bool MatchBraces
        {
            get
            {
                return this._matchBraces;
            }
            set
            {
                this._matchBraces = value;

                //	Clear any active Brace matching that may exist
                if (!value)
                    this._ns.BraceHighlight(-1, -1);
            }
        }


        /// <summary>
        ///     Gets or sets a value that indicates that the control has been modified by the user since
        ///     the control was created or its contents were last set.
        /// </summary>
        /// <returns>
        ///     <chr>true</chr> if the control's contents have been modified; otherwise, <chr>false</chr>.
        ///     The default is <chr>false</chr>.
        /// </returns>
        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public bool Modified
        {
            get { return this._state[_modifiedState]; }
            set
            {
                if (this._state[_modifiedState] != value)
                {
                    // Update the local (and native) state
                    this._state[_modifiedState] = value;
                    if (!value)
                        this._ns.SetSavePoint();

                    this.OnModifiedChanged(EventArgs.Empty);
                }
            }
        }


        [DefaultValue(true), Category("Behavior")]
        public bool MouseDownCaptures
        {
            get
            {
                return this.NativeInterface.GetMouseDownCaptures();
            }
            set
            {
                this.NativeInterface.SetMouseDownCaptures(value);
            }
        }


        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public INativeScintilla NativeInterface
        {
            get
            {
                return this;
            }
        }


        [DefaultValue(false), Category("Behavior")]
        public bool OverType
        {
            get
            {
                return this._ns.GetOvertype();
            }
            set
            {
                this._ns.SetOvertype(value);
            }
        }


        /// <summary>
        ///     Gets or sets the position cache size used to layout short runs of text in a <see cref="Scintilla" /> control.
        /// </summary>
        /// <returns>The size of the position cache in bytes. The default is 1024.</returns>
        /// <remarks>Larger cache sizes increase performance at the expense of memory.</remarks>
        [Browsable(false)]
        [EditorBrowsable(EditorBrowsableState.Advanced)]
        [DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public virtual int PositionCacheSize
        {
            get
            {
                return this.DirectMessage(NativeMethods.SCI_GETPOSITIONCACHE, IntPtr.Zero, IntPtr.Zero).ToInt32();
            }
            set
            {
                // TODO Some range checking? Scintilla provides no guidance
                this.DirectMessage(NativeMethods.SCI_SETPOSITIONCACHE, new IntPtr(value), IntPtr.Zero);
            }
        }


        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content), Category("Layout")]
        public Printing Printing
        {
            get
            {
                return this._printing;
            }
            set
            {
                this._printing = value;
            }
        }


        internal Hashtable PropertyBag { get { return this._propertyBag; } }


        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        unsafe public byte[] RawText
        {
            get
            {
                int length = this.NativeInterface.GetTextLength() + 1;

                //	May as well avoid all the crap below if we know what the outcome
                //	is going to be :)
                if (length == 1)
                    return new byte[] { 0 };

                //  Allocate a buffer the size of the string + 1 for
                //  the NULL terminator. Scintilla always sets this
                //  regardless of the encoding
                var buffer = new byte[length];

                //  Get a direct pointer to the the head of the buffer
                //  to pass to the message along with the wParam.
                //  Scintilla will fill the buffer with string data.
                fixed (byte* bp = buffer)
                {
                    this._ns.SendMessageDirect(Constants.SCI_GETTEXT, (IntPtr)length, (IntPtr)bp);
                    return buffer;
                }
            }
            set
            {
                if (value == null || value.Length == 0)
                {
                    this._ns.ClearAll();
                }
                else
                {
                    //	This byte[] HAS to be NULL terminated or who knows how big
                    //	of an overrun we'll have on our hands
                    if (value[value.Length - 1] != 0)
                    {
                        //	I hate to have to do this becuase it can be very inefficient.
                        //	It can probably be done much better by the client app
                        Array.Resize(ref value, value.Length + 1);
                        value[value.Length - 1] = 0;
                    }
                    fixed (byte* bp = value)
                        this._ns.SendMessageDirect(Constants.SCI_SETTEXT, IntPtr.Zero, (IntPtr)bp);
                }
            }
        }


        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content), Category("Layout")]
        public Scrolling Scrolling
        {
            get
            {
                return this._scrolling;
            }
            set
            {
                this._scrolling = value;
            }
        }


        [DefaultValue(SearchFlags.Empty), Category("Behavior")]
        [Editor(typeof(FlagEnumUIEditor), typeof(UITypeEditor))]
        public SearchFlags SearchFlags
        {
            get
            {
                return this._searchFlags;
            }
            set
            {
                this._searchFlags = value;
            }
        }


        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content), Category("Appearance")]
        public Selection Selection
        {
            get
            {
                return this._selection;
            }
        }


        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content), Category("Behavior")]
        public SnippetManager Snippets
        {
            get
            {
                return this._snippets;
            }
        }


        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content), Category("Appearance")]
        public StyleCollection Styles
        {
            get
            {
                return this._styles;
            }
            set
            {
                this._styles = value;
            }
        }


        /// <summary>
        ///     Gets or sets a value indicating whether characters not considered alphanumeric (ASCII values 0 through 31)
        ///     are prevented as text input.
        /// </summary>
        /// <returns>
        ///     <chr>true</chr> to prevent control characters as input; otherwise, <chr>false</chr>.
        ///     The default is <chr>true</chr>.
        /// </returns>
        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public bool SupressControlCharacters
        {
            get
            {
                return this._supressControlCharacters;
            }
            set
            {
                this._supressControlCharacters = value;
            }
        }


        /// <summary>
        ///     Gets or sets the current text in the <see cref="Scintilla" /> control.
        /// </summary>
        /// <returns>The text displayed in the control.</returns>
        [Editor("System.ComponentModel.Design.MultilineStringEditor, System.Design", typeof(UITypeEditor))]
        public override string Text
        {
            get
            {
                string s;
                this._ns.GetText(this._ns.GetLength() + 1, out s);
                return s;
            }

            set
            {
                if (string.IsNullOrEmpty(value))
                    this._ns.ClearAll();
                else
                    this._ns.SetText(value);
            }
        }


        /// <summary>
        ///     Gets the _length of text in the control.
        /// </summary>
        /// <returns>The number of characters contained in the text of the control.</returns>
        [Browsable(false)]
        public int TextLength
        {
            get
            {
                return this.NativeInterface.GetTextLength();
            }
        }


        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content), Category("Behavior")]
        public UndoRedo UndoRedo
        {
            get
            {
                return this._undoRedo;
            }
        }


        public new bool UseWaitCursor
        {
            get
            {
                return base.UseWaitCursor;
            }
            set
            {
                base.UseWaitCursor = value;

                if (value)
                    this.NativeInterface.SetCursor(Constants.SC_CURSORWAIT);
                else
                    this.NativeInterface.SetCursor(Constants.SC_CURSORNORMAL);
            }
        }


        /// <summary>
        ///     Gets the <see cref="Whitespace"/> display mode and style behavior associated with the <see cref="Scintilla"/> control.
        /// </summary>
        /// <returns>A <see cref="Whitespace"/> object that represents whitespace display mode and style behavior in a <see cref="Scintilla"/> control.</returns>
        [Category("Appearance"), Description("The display mode and style of whitespace characters.")]
        [DesignerSerializationVisibility(DesignerSerializationVisibility.Content)]
        public Whitespace Whitespace
        {
            get { return this._whitespace; }
        }


        /// <summary>
        /// Gets or sets the current zoom level of the <see cref="Scintilla" /> control.
        /// </summary>
        /// <returns>The factor by which the contents of the control is zoomed.</returns>
        [DefaultValue(0), Category("Appearance")]
        [Description("Defines the current scaling factor of the text display; 0 is normal viewing.")]
        public int Zoom
        {
            get
            {
                return this._ns.GetZoom();
            }
            set
            {
                this._ns.SetZoom(value);
            }
        }

        #endregion Properties


        #region Events

        /// <summary>
        ///     Occurs when an annotation has changed.
        /// </summary>
        [Category("Scintilla")] // TODO Move to resource
        [Description("Occurs when an annotation has changed.")] // TODO Move to resource
        public event EventHandler<AnnotationChangedEventArgs> AnnotationChanged
        {
            add
            {
                Events.AddHandler(_annotationChangedEventKey, value);
            }
            remove
            {
                Events.RemoveHandler(_annotationChangedEventKey, value);
            }
        }


        /// <summary>
        ///     Occurs when the user makes a selection from the auto-complete list.
        /// </summary>
        [Category("Scintilla"), Description("Occurs when the user makes a selection from the auto-complete list.")]
        public event EventHandler<AutoCompleteAcceptedEventArgs> AutoCompleteAccepted
        {
            add { Events.AddHandler(_autoCompleteAcceptedEventKey, value); }
            remove { Events.RemoveHandler(_autoCompleteAcceptedEventKey, value); }
        }


        /// <summary>
        ///     Occurs when text is about to be removed from the document.
        /// </summary>
        [Category("Scintilla"), Description("Occurs when text is about to be removed from the document.")]
        public event EventHandler<TextModifiedEventArgs> BeforeTextDelete
        {
            add { Events.AddHandler(_beforeTextDeleteEventKey, value); }
            remove { Events.RemoveHandler(_beforeTextDeleteEventKey, value); }
        }


        /// <summary>
        ///     Occurs when text is about to be inserted into the document.
        /// </summary>
        [Category("Scintilla"), Description("Occurs when text is about to be inserted into the document.")]
        public event EventHandler<TextModifiedEventArgs> BeforeTextInsert
        {
            add { Events.AddHandler(_beforeTextInsertEventKey, value); }
            remove { Events.RemoveHandler(_beforeTextInsertEventKey, value); }
        }


        /// <summary>
        ///     Occurs when the value of the <see cref="BorderStyle" /> property has changed.
        /// </summary>
        [Category("Property Changed")]
        [Description("Occurs when the value of the BorderStyle property changes.")] // TODO Move to resource
        public event EventHandler BorderStyleChanged
        {
            add
            {
                Events.AddHandler(_borderStyleChangedEventKey, value);
            }
            remove
            {
                Events.RemoveHandler(_borderStyleChangedEventKey, value);
            }
        }


        /// <summary>
        ///     Occurs when a user clicks on a call tip.
        /// </summary>
        [Category("Scintilla"), Description("Occurs when a user clicks on a call tip.")]
        public event EventHandler<CallTipClickEventArgs> CallTipClick
        {
            add { Events.AddHandler(_callTipClickEventKey, value); }
            remove { Events.RemoveHandler(_callTipClickEventKey, value); }
        }


        /// <summary>
        ///     Occurs when the user types an ordinary text character (as opposed to a command character) into the text.
        /// </summary>
        [Category("Scintilla"), Description("Occurs when the user types a text character.")]
        public event EventHandler<CharAddedEventArgs> CharAdded
        {
            add { Events.AddHandler(_charAddedEventKey, value); }
            remove { Events.RemoveHandler(_charAddedEventKey, value); }
        }


        /// <summary>
        ///     Occurs when the text or styling of the document changes or is about to change.
        /// </summary>
        [Category("Scintilla"), Description("Occurs when the text or styling of the document changes or is about to change.")]
        public event EventHandler<NativeScintillaEventArgs> DocumentChange
        {
            add { Events.AddHandler(_documentChangeEventKey, value); }
            remove { Events.RemoveHandler(_documentChangeEventKey, value); }
        }


        /// <summary>
        ///     Occurs when a <see cref="DropMarker"/> is about to be collected.
        /// </summary>
        [Category("Scintilla"), Description("Occurs when a DropMarker is about to be collected.")]
        public event EventHandler<DropMarkerCollectEventArgs> DropMarkerCollect
        {
            add { Events.AddHandler(_dropMarkerCollectEventKey, value); }
            remove { Events.RemoveHandler(_dropMarkerCollectEventKey, value); }
        }


        /// <summary>
        ///     Occurs when a user actions such as a mouse move or key press ends a dwell (hover) activity.
        /// </summary>
        [Category("Scintilla"), Description("Occurs when a dwell (hover) activity has ended.")]
        public event EventHandler<ScintillaMouseEventArgs> DwellEnd
        {
            add { Events.AddHandler(_dwellEndEventKey, value); }
            remove { Events.RemoveHandler(_dwellEndEventKey, value); }
        }


        /// <summary>
        ///     Occurs when the user hovers the mouse (dwells) in one position for the dwell period.
        /// </summary>
        [Category("Scintilla"), Description("Occurs when the user hovers the mouse (dwells) in one position for the dwell period.")]
        public event EventHandler<ScintillaMouseEventArgs> DwellStart
        {
            add { Events.AddHandler(_dwellStartEventKey, value); }
            remove { Events.RemoveHandler(_dwellStartEventKey, value); }
        }


        /// <summary>
        ///     Occurs when a user drops a file on the <see cref="Scintilla"/> control.
        /// </summary>
        [Category("Scintilla"), Description("Occurs when a user drops a file on the control.")]
        public event EventHandler<FileDropEventArgs> FileDrop
        {
            add { Events.AddHandler(_fileDropEventKey, value); }
            remove { Events.RemoveHandler(_fileDropEventKey, value); }
        }


        /// <summary>
        ///     Occurs when a folding change has occurred.
        /// </summary>
        [Category("Scintilla"), Description("Occurs when a folding change has occurred.")]
        public event EventHandler<FoldChangedEventArgs> FoldChanged
        {
            add { Events.AddHandler(_foldChangedEventKey, value); }
            remove { Events.RemoveHandler(_foldChangedEventKey, value); }
        }


        /// <summary>
        ///     Occurs when a user clicks on text that is in a style with the hotspot attribute set.
        /// </summary>
        [Category("Scintilla")]
        [Description("Occurs when a user clicks on text with the hotspot style.")] // TODO Move to resource
        public event EventHandler<HotspotClickEventArgs> HotspotClick
        {
            add
            {
                Events.AddHandler(_hotspotClickEventKey, value);
            }
            remove
            {
                Events.RemoveHandler(_hotspotClickEventKey, value);
            }
        }


        /// <summary>
        ///     Occurs when a user double-clicks on text that is in a style with the hotspot attribute set.
        /// </summary>
        [Category("Scintilla")]
        [Description("Occurs when a user double-clicks on text with the hotspot style.")] // TODO Move to resource
        public event EventHandler<HotspotClickEventArgs> HotspotDoubleClick
        {
            add
            {
                Events.AddHandler(_hotspotDoubleClickEventKey, value);
            }
            remove
            {
                Events.RemoveHandler(_hotspotDoubleClickEventKey, value);
            }
        }


        /// <summary>
        ///     Occurs when a user releases a click on text that is in a style with the hotspot attribute set.
        /// </summary>
        [Category("Scintilla")]
        [Description("Occurs when a user releases a click on text with the hotspot style.")] // TODO Move to resource
        public event EventHandler<HotspotClickEventArgs> HotspotReleaseClick
        {
            add
            {
                Events.AddHandler(_hotspotReleaseClickEventKey, value);
            }
            remove
            {
                Events.RemoveHandler(_hotspotReleaseClickEventKey, value);
            }
        }


        /// <summary>
        ///     Occurs when the a clicks or releases the mouse on text that has an indicator.
        /// </summary>
        [Category("Scintilla"), Description("Occurs when the a clicks or releases the mouse on text that has an indicator.")]
        public event EventHandler<ScintillaMouseEventArgs> IndicatorClick
        {
            add { Events.AddHandler(_indicatorClickEventKey, value); }
            remove { Events.RemoveHandler(_indicatorClickEventKey, value); }
        }


        /// <summary>
        ///     Occurs when a range of lines that is currently invisible should be made visible.
        /// </summary>
        [Category("Scintilla"), Description("Occurs when a range of lines that is currently invisible should be made visible.")]
        public event EventHandler<LinesNeedShownEventArgs> LinesNeedShown
        {
            add { Events.AddHandler(_linesNeedShownEventKey, value); }
            remove { Events.RemoveHandler(_linesNeedShownEventKey, value); }
        }


        /// <summary>
        ///     Occurs when the control is first loaded.
        /// </summary>
        [Category("Behavior"), Description("Occurs when the control is first loaded.")]
        public event EventHandler Load
        {
            add { Events.AddHandler(_loadEventKey, value); }
            remove { Events.RemoveHandler(_loadEventKey, value); }
        }


        /// <summary>
        ///     Occurs each time a recordable change occurs.
        /// </summary>
        [Category("Scintilla"), Description("Occurs each time a recordable change occurs.")]
        public event EventHandler<MacroRecordEventArgs> MacroRecord
        {
            add { Events.AddHandler(_macroRecordEventKey, value); }
            remove { Events.RemoveHandler(_macroRecordEventKey, value); }
        }


        /// <summary>
        ///     Occurs when the mouse was clicked inside a margin that was marked as sensitive.
        /// </summary>
        [Category("Scintilla"), Description("Occurs when the mouse was clicked inside a margin that was marked as sensitive.")]
        public event EventHandler<MarginClickEventArgs> MarginClick
        {
            add { Events.AddHandler(_marginClickEventKey, value); }
            remove { Events.RemoveHandler(_marginClickEventKey, value); }
        }


        /// <summary>
        ///     Occurs when one or more markers has changed in a line of text.
        /// </summary>
        [Category("Scintilla"), Description("Occurs when one or more markers has changed in a line of text.")]
        public event EventHandler<MarkerChangedEventArgs> MarkerChanged
        {
            add { Events.AddHandler(_markerChangedEventKey, value); }
            remove { Events.RemoveHandler(_markerChangedEventKey, value); }
        }


        /// <summary>
        ///     Occurs when the value of the <see cref="Modified"/> property has changed.
        /// </summary>
        [Category("Property Changed"), Description("Occurs when the value of the Modified property changes.")]
        public event EventHandler ModifiedChanged
        {
            add { Events.AddHandler(_modifiedChangedEventKey, value); }
            remove { Events.RemoveHandler(_modifiedChangedEventKey, value); }
        }


        /// <summary>
        ///     Occurs when a user tries to modify text when in read-only mode.
        /// </summary>
        [Category("Scintilla"), Description("Occurs when a user tries to modifiy text when in read-only mode.")]
        public event EventHandler ReadOnlyModifyAttempt
        {
            add { Events.AddHandler(_readOnlyModifyAttemptEventKey, value); }
            remove { Events.RemoveHandler(_readOnlyModifyAttemptEventKey, value); }
        }


        /// <summary>
        ///     Occurs when the control is scrolled.
        /// </summary>
        [Category("Action"), Description("Occurs when the control is scrolled.")]
        public event EventHandler<ScrollEventArgs> Scroll
        {
            add { Events.AddHandler(_scrollEventKey, value); }
            remove { Events.RemoveHandler(_scrollEventKey, value); }
        }


        /// <summary>
        ///     Occurs when the selection has changed.
        /// </summary>
        [Category("Scintilla"), Description("Occurs when the selection has changed.")]
        public event EventHandler SelectionChanged
        {
            add { Events.AddHandler(_selectionChangedEventKey, value); }
            remove { Events.RemoveHandler(_selectionChangedEventKey, value); }
        }


        /// <summary>
        ///     Occurs when the control is about to display or print text that requires styling.
        /// </summary>
        [Category("Scintilla"), Description("Occurs when the control is about to display or print text that requires styling.")]
        public event EventHandler<StyleNeededEventArgs> StyleNeeded
        {
            add { Events.AddHandler(_styleNeededEventKey, value); }
            remove { Events.RemoveHandler(_styleNeededEventKey, value); }
        }


        /// <summary>
        ///     Occurs when text has been removed from the document.
        /// </summary>
        [Category("Scintilla"), Description("Occurs when text has been removed from the document.")]
        public event EventHandler<TextModifiedEventArgs> TextDeleted
        {
            add { Events.AddHandler(_textDeletedEventKey, value); }
            remove { Events.RemoveHandler(_textDeletedEventKey, value); }
        }


        /// <summary>
        ///     Occurs when text has been inserted into the document.
        /// </summary>
        [Category("Scintilla"), Description("Occurs when text has been inserted into the document.")]
        public event EventHandler<TextModifiedEventArgs> TextInserted
        {
            add { Events.AddHandler(_textInsertedEventKey, value); }
            remove { Events.RemoveHandler(_textInsertedEventKey, value); }
        }


        /// <summary>
        ///     Occurs when the user zooms the display using the keyboard or the <see cref="Zoom"/> property is set.
        /// </summary>
        [Category("Scintilla"), Description("Occurs when the user zooms the display using the keyboard or the Zoom property is set.")]
        public event EventHandler ZoomChanged
        {
            add { Events.AddHandler(_zoomChangedEventKey, value); }
            remove { Events.RemoveHandler(_zoomChangedEventKey, value); }
        }

        #endregion Events


        #region Constructors

        public Scintilla()
        {
            this._state = new BitVector32(0);
            this._state[_acceptsReturnState] = true;
            this._state[_acceptsTabState] = true;

            this._ns = this;

            this._caption = GetType().FullName;

            // Set up default encoding to UTF-8 which is the Scintilla's best supported.
            // .NET strings are UTF-16 but should be able to convert without any problems
            this.Encoding = Encoding.UTF8;

            // Ensure all style values have at least defaults
            this._ns.StyleClearAll();

            this._caret = new CaretInfo(this);
            this._lines = new LineCollection(this);
            this._selection = new Selection(this);
            this._indicators = new IndicatorCollection(this);
            this._snippets = new SnippetManager(this);
            this._margins = new MarginCollection(this);
            this._scrolling = new Scrolling(this);
            this._whitespace = new Whitespace(this);
            this._endOfLine = new EndOfLine(this);
            this._clipboard = new Clipboard(this);
            this._undoRedo = new UndoRedo(this);
            this._dropMarkers = new DropMarkers(this);
            this._hotspotStyle = new HotspotStyle(this);
            this._callTip = new CallTip(this);
            this._styles = new StyleCollection(this);
            this._indentation = new Indentation(this);
            this._markers = new MarkerCollection(this);
            this._autoComplete = new AutoComplete(this);
            this._documentHandler = new DocumentHandler(this);
            this._lexing = new Lexing(this);
            this._longLines = new LongLines(this);
            this._commands = new Commands(this);
            this._folding = new Folding(this);
            this._configurationManager = new ConfigurationManager(this);
            this._printing = new Printing(this);
            this._findReplace = new FindReplace(this);
            this._documentNavigation = new DocumentNavigation(this);
            this._goto = new GoTo(this);


            this._helpers.AddRange(new TopLevelHelper[]
            {
                this._caret,
                this._lines,
                this._selection,
                this._indicators,
                this._snippets,
                this._margins,
                this._scrolling,
                this._whitespace,
                this._endOfLine,
                this._clipboard,
                this._undoRedo,
                this._dropMarkers,
                this._hotspotStyle,
                this._styles,
                this._indentation,
                this._markers,
                this._autoComplete,
                this._documentHandler,
                this._lexing,
                this._longLines,
                this._commands,
                this._folding,
                this._configurationManager,
                this._printing,
                this._findReplace,
                this._documentNavigation,
                this._goto
            });


            // Change from Scintilla's default black on white to
            // platform defaults for edit controls.
            base.BackColor = SystemColors.Window;
            base.ForeColor = SystemColors.WindowText;

            this.Styles[0].Font = Font;
            this.Styles[0].ForeColor = this.ForeColor;
            this.Styles[0].BackColor = this.BackColor;
            this.Styles.Default.BackColor = this.BackColor;
        }

        #endregion Constructors
    }
    #pragma warning restore 612, 618
}
