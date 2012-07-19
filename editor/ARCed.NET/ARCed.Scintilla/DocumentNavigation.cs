#region Using Directives

using System;
using System.ComponentModel;
using System.Windows.Forms;

#endregion


namespace ARCed.Scintilla
{
    /// <summary>
    ///     Manages Document Navigation, which is a snapshot history of movements within
    ///     a document.
    /// </summary>
    [TypeConverter(typeof(ExpandableObjectConverter))]
    public class DocumentNavigation : TopLevelHelper
    {
        #region Fields

        private bool _supressNext;
        private readonly Timer t;
        private int _navigationPointTimeout = 200;
        public FakeStack _forewardStack = new FakeStack();
        public FakeStack _backwardStack = new FakeStack();
        private int _maxHistorySize = 50;
        private bool _isEnabled = true;

        #endregion Fields


        #region Methods

        /// <summary>
        ///     Causes the current position to navigate to the last snapshotted document position.
        /// </summary>
        public void NavigateBackward()
        {
            if (this._backwardStack.Count == 0)
                return;

            int currentPos = Scintilla.Caret.Position;
            if (currentPos == this._backwardStack.Current.Start && this._backwardStack.Count == 1)
                return;

            int pos = this._backwardStack.Pop().Start;

            if (pos != currentPos)
            {
                this._forewardStack.Push(this.NewRange(currentPos));
                Scintilla.Caret.Goto(pos);
            }
            else
            {
                this._forewardStack.Push(this.NewRange(pos));
                Scintilla.Caret.Goto(this._backwardStack.Current.Start);
            }

            this._supressNext = true;
        }


        /// <summary>
        ///     After 1 or more backwards navigations this command navigates to the previous
        ///     backwards navigation point.
        /// </summary>
        public void NavigateForward()
        {
            if (!this.CanNavigateForward)
                return;

            int pos = this._forewardStack.Pop().Start;
            this._backwardStack.Push(this.NewRange(pos));
            Scintilla.Caret.Goto(pos);

            this._supressNext = true;
        }


        private NavigationPont NewRange(int pos)
        {
            var mr = new NavigationPont(pos, Scintilla);
            Scintilla.ManagedRanges.Add(mr);
            return mr;
        }


        public void Reset()
        {
            this._backwardStack.Clear();
            this._forewardStack.Clear();
            this.ResetIsEnabled();
            this.ResetMaxHistorySize();
        }


        private void ResetIsEnabled()
        {
            this._isEnabled = true;
        }


        private void ResetMaxHistorySize()
        {
            this._maxHistorySize = 50;
        }


        private void ResetNavigationPointTimeout()
        {
            this._navigationPointTimeout = 200;
        }


        private void scintilla_SelectionChanged(object sender, EventArgs e)
        {
            if (!this._isEnabled)
                return;

            if (!this._supressNext)
            {
                this.t.Enabled = false;
                this.t.Enabled = true;
            }
            else
            {
                this._supressNext = false;
            }
        }


        internal bool ShouldSerialize()
        {
            return this.ShouldSerializeIsEnabled() || this.ShouldSerializeMaxHistorySize();
        }


        private bool ShouldSerializeIsEnabled()
        {
            return !this._isEnabled;
        }


        private bool ShouldSerializeMaxHistorySize()
        {
            return this._maxHistorySize != 50;
        }


        private bool ShouldSerializeNavigationPointTimeout()
        {
            return this._navigationPointTimeout != 200;
        }


        private void t_Tick(object sender, EventArgs e)
        {
            this.t.Enabled = false;
            int pos = NativeScintilla.GetCurrentPos();
            if ((this._forewardStack.Count == 0 || this._forewardStack.Current.Start != pos) && (this._backwardStack.Count == 0 || this._backwardStack.Current.Start != pos))
                this._backwardStack.Push(this.NewRange(pos));
        }

        #endregion Methods


        #region Properties

        /// <summary>
        ///     List of entries that allow you to navigate backwards.
        /// </summary>
        /// <remarks>
        ///     The ForwardStack and BackwardStack can be shared between multiple
        ///     ARCed.Scintilla objects. This is useful in MDI applications when you wish
        ///     to have a shared document navigation that remembers positions in each
        ///     document.
        /// </remarks>
        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public FakeStack BackwardStack
        {
            get
            {
                return this._backwardStack;
            }
            set
            {
                this._backwardStack = value;
            }
        }


        /// <summary>
        ///     Returns true if ARCed.Scintilla can perform a successful backward navigation.
        /// </summary>
        [Browsable(false)]
        public bool CanNavigateBackward
        {
            get
            {
                if (this._backwardStack.Count == 0 || (NativeScintilla.GetCurrentPos() == this._backwardStack.Current.Start && this._backwardStack.Count == 1))
                    return false;

                return true;
            }
        }


        /// <summary>
        ///     Returns true if ARCed.Scintilla can perform a successful forward navigation.
        /// </summary>
        [Browsable(false)]
        public bool CanNavigateForward
        {
            get
            {
                return this._forewardStack.Count > 0;
            }
        }


        /// <summary>
        ///     List of entries that allow you to navigate forwards.
        /// </summary>
        /// <remarks>
        ///     The ForwardStack and BackwardStack can be shared between multiple
        ///     ARCed.Scintilla objects. This is useful in MDI applications when you wish
        ///     to have a shared document navigation that remembers positions in each
        ///     document.
        /// </remarks>
        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public FakeStack ForewardStack
        {
            get
            {
                return this._forewardStack;
            }
            set
            {
                this._forewardStack = value;
            }
        }


        /// <summary>
        ///     Gets/Sets whether Document Navigation is tracked. Defaults to true.
        /// </summary>
        public bool IsEnabled
        {
            get
            {
                return this._isEnabled;
            }
            set
            {
                this._isEnabled = value;
            }
        }


        /// <summary>
        ///     Maximum number of places the document navigation remembers. Defaults to 50.
        /// </summary>
        /// <remarks>
        ///     When the _maxBackups value is reached the oldest entries are removed.
        /// </remarks>
        public int MaxHistorySize
        {
            get
            {
                return this._maxHistorySize;
            }
            set
            {
                this._maxHistorySize = value;
                this._backwardStack.MaxCount = value;
                this._forewardStack.MaxCount = value;
            }
        }


        /// <summary>
        ///     Time in milliseconds to wait before a Navigation Point is set. Default is 200
        /// </summary>
        /// <remarks>
        ///     In text editing, the current caret position is constantly changing. Rather than capture every
        ///     change in position, ARCed.Scintilla captures the current position [NavigationPointTimeout]ms after a 
        ///     position changes, only then is it eligable for another snapshot
        /// </remarks>
        public int NavigationPointTimeout
        {
            get
            {
                return this._navigationPointTimeout;
            }
            set
            {
                this._navigationPointTimeout = value;
            }
        }

        #endregion Properties


        #region Constructors

        internal DocumentNavigation(Scintilla scintilla) : base(scintilla) 
        {
            this.t = new Timer
            {
                Interval = this._navigationPointTimeout
            };
            this.t.Tick += this.t_Tick;
            scintilla.SelectionChanged += this.scintilla_SelectionChanged;
        }

        #endregion Constructors
    }
}
