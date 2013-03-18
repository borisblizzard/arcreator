#region Using Directives

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.IO;

#endregion


namespace ARCed.Scintilla
{
    [TypeConverter(typeof(ExpandableObjectConverter))]
    public class Lexing : TopLevelHelper
    {
        #region Constants

        private const string DEFAULT_WHITECHARS = " \t\r\n\0";
        private const string DEFAULT_WORDCHARS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_";

        #endregion Constants


        #region Fields

        private readonly KeywordCollection _keywords;
        private readonly Dictionary<string, string> _lexerLanguageMap = new Dictionary<string, string>(StringComparer.OrdinalIgnoreCase);
        private string _lexerName = "container";
        private string _lineCommentPrefix = string.Empty;
        private string _streamCommentPrefix = string.Empty;
        private string _streamCommentSufix = string.Empty;
        private readonly Dictionary<string, int> _styleNameMap = new Dictionary<string, int>(StringComparer.OrdinalIgnoreCase);
        private string _whitespaceChars;
        private string _wordChars;
        internal char[] WhitespaceCharsArr;
        internal char[] WordCharsArr = null;

        #endregion Fields


        #region Methods

        public void Colorize()
        {
            this.Colorize(0, -1);
        }


        public void Colorize(int startPos, int endPos)
        {
            NativeScintilla.Colourise(startPos, endPos);
        }


        private int FindFirstNonWhitespaceChar(string s)
        {
            for (int i = 0; i < s.Length; i++)
            {
                if (s[i].ToString().IndexOfAny(this.WhitespaceCharsArr) == -1)
                    return i;
            }

            return -1;
        }


        public string GetProperty(string name)
        {
            string s;
            NativeScintilla.GetProperty(name, out s);
            return s;
        }


        public string GetPropertyExpanded(string name)
        {
            string s;
            NativeScintilla.GetPropertyExpanded(name, out s);
            return s;
        }


        public int GetPropertyInt(string name)
        {
            return this.GetPropertyInt(name, 0);
        }


        public int GetPropertyInt(string name, int defaultValue)
        {
            return NativeScintilla.GetPropertyInt(name, defaultValue);
        }


        public void LineComment()
        {
            if (string.IsNullOrEmpty(this._lineCommentPrefix))
                return;

            // So the theory behind line commenting is that for every selected line
            // we look for the first non-whitespace character and insert the line
            // comment prefix. Lines without non-whitespace are skipped.
            NativeScintilla.BeginUndoAction();

            Range selRange = Scintilla.Selection.Range;
            int start = selRange.StartingLine.Number;
            int end = selRange.EndingLine.Number;

            // We're tracking the new _end of the selection range including
            // the amount it expands because we're inserting new text.
            int offset = this._lineCommentPrefix.Length;

            for (int i = start; i <= end; i++)
            {
                Line l = Scintilla.Lines[i];
                int firstWordChar = this.FindFirstNonWhitespaceChar(l.Text);
                if (firstWordChar >= 0)
                {
                    Scintilla.InsertText(l.StartPosition + firstWordChar, this._lineCommentPrefix);
                    selRange.End += offset;
                }
            }

            NativeScintilla.EndUndoAction();

            // An odd side-effect of InsertText is that we lose the current
            // selection. This is undesirable. This is why we were tracking
            // the _end position offset.
            selRange.Select();
        }


        public void LineUncomment()
        {
            if (string.IsNullOrEmpty(this._lineCommentPrefix))
                return;

            NativeScintilla.BeginUndoAction();

            // Uncommenting is a lot like line commenting. However in addition
            // to looking for a non-whitespace character, the string that follows
            // it MUST be our line Comment Prefix. If this is the case the prefex
            // is removed from the line at its position.
            Range selRange = Scintilla.Selection.Range;
            int start = selRange.StartingLine.Number;
            int end = selRange.EndingLine.Number;

            int offset = this._lineCommentPrefix.Length;

            for (int i = start; i <= end; i++)
            {
                Line l = Scintilla.Lines[i];
                int firstWordChar = this.FindFirstNonWhitespaceChar(l.Text);
                if (firstWordChar >= 0)
                {
                    int startPos = l.StartPosition + firstWordChar;
                    Range commentRange = Scintilla.GetRange(startPos, startPos + offset);
                    if (commentRange.Text == this._lineCommentPrefix)
                        commentRange.Text = string.Empty;
                }
            }

            NativeScintilla.EndUndoAction();
        }


        public void LoadLexerLibrary(string path)
        {
            NativeScintilla.LoadLexerLibrary(path);
        }


        private void loadStyleMap()
        {
            if (Scintilla.IsDesignMode)
                return;

            this._styleNameMap.Clear();

            // These are global constants that always apply
            this._styleNameMap.Add("BRACEBAD",Constants.STYLE_BRACEBAD);
            this._styleNameMap.Add("BRACELIGHT",Constants.STYLE_BRACELIGHT);
            this._styleNameMap.Add("CALLTIP",Constants.STYLE_CALLTIP);
            this._styleNameMap.Add("CONTROLCHAR",Constants.STYLE_CONTROLCHAR);
            this._styleNameMap.Add("DEFAULT",Constants.STYLE_DEFAULT);
            this._styleNameMap.Add("LINENUMBER",Constants.STYLE_LINENUMBER);

            string lexname = this.Lexer.ToString().ToLower();

            using (Stream s = GetType().Assembly.GetManifestResourceStream("ARCed.Scintilla.Configuration.Builtin.LexerStyleNames." + lexname + ".txt"))
            {
                if (s == null)
                    return;

                using (var sr = new StreamReader(s))
                {
                    while (!sr.EndOfStream)
                    {
                        string[] arr = sr.ReadLine().Split('=');
                        if (arr.Length != 2)
                            continue;

                        string key = arr[0].Trim();
                        int value = int.Parse(arr[1].Trim());
                        
                        this._styleNameMap.Remove(key);
                        this._styleNameMap.Add(key, value);
                    }
                }
            }

        }


        private void ResetLexer()
        {
            this.Lexer = Lexer.Container;
        }


        private void ResetLexerName()
        {
            this.LexerName = "container";
        }


        private void ResetWhitespaceChars()
        {
            this._whitespaceChars = DEFAULT_WHITECHARS;
        }


        private void ResetWordChars()
        {
            this.WordChars = DEFAULT_WORDCHARS;
        }


        public void SetKeywords(int keywordSet, string list)
        {
            NativeScintilla.SetKeywords(keywordSet, list);
        }


        public void SetProperty(string name, string value)
        {
            NativeScintilla.SetProperty(name, value);
        }


        internal bool ShouldSerialize()
        {
            return this.ShouldSerializeLexerName() ||
                this.ShouldSerializeLexer() ||
                this.ShouldSerializeWhitespaceChars() ||
                this.ShouldSerializeWordChars();
        }


        private bool ShouldSerializeLexer()
        {
            return this.Lexer != Lexer.Container;
        }


        private bool ShouldSerializeLexerName()
        {
            return this.LexerName != "container";
        }


        private bool ShouldSerializeWhitespaceChars()
        {
            return this._whitespaceChars != DEFAULT_WHITECHARS;
        }


        private bool ShouldSerializeWordChars()
        {
            return this._wordChars != DEFAULT_WORDCHARS;
        }


        public void StreamComment()
        {
            if (string.IsNullOrEmpty(this._streamCommentPrefix) || string.IsNullOrEmpty(this._streamCommentSufix))
                return;

            NativeScintilla.BeginUndoAction();
            
            Range selRange = Scintilla.Selection.Range;
            Scintilla.InsertText(selRange.Start, this._streamCommentPrefix);
            Scintilla.InsertText(selRange.End+ this._streamCommentPrefix.Length, this._streamCommentSufix);
            selRange.End += this._streamCommentPrefix.Length + this._streamCommentSufix.Length;
            selRange.Select();

            NativeScintilla.EndUndoAction();
        }


        public void ToggleLineComment()
        {
            if (string.IsNullOrEmpty(this._lineCommentPrefix))
                return;

            NativeScintilla.BeginUndoAction();

            Range selRange = Scintilla.Selection.Range;
            int start = selRange.StartingLine.Number;
            int end = selRange.EndingLine.Number;

            int offset = this._lineCommentPrefix.Length;

            for (int i = start; i <= end; i++)
            {
                Line l = Scintilla.Lines[i];
                int firstWordChar = this.FindFirstNonWhitespaceChar(l.Text);
                if (firstWordChar >= 0)
                {
                    int startPos = l.StartPosition + firstWordChar;
                    Range commentRange = Scintilla.GetRange(startPos, startPos + offset);
                    if (commentRange.Text == this._lineCommentPrefix)
                    {
                        commentRange.Text = string.Empty;
                        selRange.End -= offset;
                    }
                    else
                    {
                        Scintilla.InsertText(l.StartPosition + firstWordChar, this._lineCommentPrefix);
                        selRange.End += offset;
                    }
                }
            }

            NativeScintilla.EndUndoAction();
            selRange.Select();
        }

        #endregion Methods


        #region Properties

        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public KeywordCollection Keywords
        {
            get
            {
                return this._keywords;
            }
        }


        public Lexer Lexer
        {
            get
            {
                return (Lexer)NativeScintilla.GetLexer();
            }
            set
            {
                NativeScintilla.SetLexer((int)value);
                this._lexerName = value.ToString().ToLower();
                if (this._lexerName == "null")
                    this._lexerName = "";

                this.loadStyleMap();
            }
        }


        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public Dictionary<string, string> LexerLanguageMap
        {
            get
            {
                return this._lexerLanguageMap;
            }
        }


        public string LexerName
        {
            get
            {
                return this._lexerName;
            }
            set
            {
                if (string.IsNullOrEmpty(value))
                    value = "null";
                    
                NativeScintilla.SetLexerLanguage(value.ToLower());

                this._lexerName = value;

                this.loadStyleMap();
            }
        }


        public string LineCommentPrefix
        {
            get
            {
                return this._lineCommentPrefix;
            }
            set
            {
                if (value == null)
                    value = string.Empty;

                this._lineCommentPrefix = value;
            }
        }


        public string StreamCommentPrefix
        {
            get
            {
                return this._streamCommentPrefix;
            }
            set
            {
                if (value == null)
                    value = string.Empty;

                this._streamCommentPrefix = value;
            }
        }


        public string StreamCommentSufix
        {
            get
            {
                return this._streamCommentSufix;
            }
            set
            {
                if (value == null)
                    value = string.Empty;

                this._streamCommentSufix = value;
            }
        }


        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public Dictionary<string, int> StyleNameMap
        {
            get
            {
                return this._styleNameMap;
            }
        }


        [TypeConverter(typeof(WhitespaceStringConverter))]
        public string WhitespaceChars
        {
            get
            {
                return this._whitespaceChars;
            }
            set
            {
                this._whitespaceChars = value;
                this.WhitespaceCharsArr = this._whitespaceChars.ToCharArray();
                NativeScintilla.SetWhitespaceChars(value);
            }
        }


        public string WordChars
        {
            get
            {
                return this._wordChars;
            }
            set
            {
                this._wordChars = value;
                this.WordCharsArr = this._wordChars.ToCharArray();
                NativeScintilla.SetWordChars(value);
            }
        }

        #endregion Properties


        #region Constructors

        internal Lexing(Scintilla scintilla) : base(scintilla)
        {
            this.WhitespaceChars = DEFAULT_WHITECHARS;
            this.WordChars = DEFAULT_WORDCHARS;
            this._keywords = new KeywordCollection(scintilla);

            // Language names are a superset lexer names. For instance the chr and cs (chr#)
            // langauges both use the cpp lexer (by default). Languages are kind of a 
            // SCite concept, while Scintilla only cares about Lexers. However we don't
            // need to explicetly map a language to a lexer if they are the same name
            // like cpp.
            this._lexerLanguageMap.Add("cs", "cpp");
            this._lexerLanguageMap.Add("html", "hypertext");
            this._lexerLanguageMap.Add("xml", "hypertext");
        }

        #endregion Constructors
    }
}
