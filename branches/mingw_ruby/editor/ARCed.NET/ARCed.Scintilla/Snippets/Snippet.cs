#region Using Directives

using System;
using System.Collections.Generic;

#endregion


namespace ARCed.Scintilla
{
    public class Snippet : IComparable<Snippet>
    {
        #region Constants

        internal const char RealDelimeter = '\x1';

        #endregion Constants


        #region Fields

        private string _code;
        private char _delimeter;
        private bool _isSurroundsWith;
        private List<string> _languages = new List<string>();
        private string _realCode;
        private string _shortcut;
        public char DefaultDelimeter = '$';

        #endregion Fields


        #region Methods

        public int CompareTo(Snippet other)
        {
            return StringComparer.OrdinalIgnoreCase.Compare(this._shortcut, other._shortcut);
        }

        #endregion Methods


        #region Properties

        public string Code
        {
            get
            {
                return this._code;
            }
            set
            {
                this._code = value;
                this._realCode = this._code.Replace(this._delimeter, RealDelimeter);
            }
        }


        public char Delimeter
        {
            get
            {
                return this._delimeter;
            }
            set
            {
                this._delimeter = value;
            }
        }


        public bool IsSurroundsWith
        {
            get
            {
                return this._isSurroundsWith;
            }
            set
            {
                this._isSurroundsWith = value;
            }
        }


        public List<string> Languages
        {
            get
            {
                return this._languages;
            }
            set
            {
                this._languages = value;
            }
        }


        internal string RealCode
        {
            get
            {
                return this._realCode;
            }
            set
            {
                this._realCode = value;
            }
        }


        public string Shortcut
        {
            get
            {
                return this._shortcut;
            }
            set
            {
                this._shortcut = value;
            }
        }

        #endregion Properties


        #region Constructors

        public Snippet(string shortcut, string code) : this(shortcut, code, '$', false)
        {
        }


        public Snippet(string shortcut, string code, char delimeter, bool isSurroundsWith)
        {
            this._isSurroundsWith = isSurroundsWith;
            this._shortcut = shortcut;
            this._delimeter = delimeter;
            this.Code = code;
        }

        #endregion Constructors
    }
}
