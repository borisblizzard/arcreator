#region Using Directives

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Linq;
using System.Windows.Forms;

#endregion


namespace ARCed.Scintilla
{
    /// <summary>
    ///     Manages commands, which are actions in ARCed.Scintilla that can be bound to key combinations.
    /// </summary>
    [TypeConverter(typeof(ExpandableObjectConverter))]
    public class Commands : TopLevelHelper
    {
        #region Fields

        private readonly Dictionary<KeyBinding, List<BindableCommand>> _boundCommands = new Dictionary<KeyBinding, List<BindableCommand>>();
        private readonly CommandComparer _commandComparer = new CommandComparer();

        // Hmmm.. This is getting more and more hackyish
        internal bool StopProcessingCommands = false;

        private bool _allowDuplicateBindings = true;

        #endregion Fields


        #region Methods

        /// <summary>
        ///     Adds a key combination to a Command
        /// </summary>
        /// <param name="shortcut">CharacterStance corresponding to a (keyboard) key to trigger command</param>
        /// <param name="command">Command to execute</param>
        public void AddBinding(char shortcut, BindableCommand command)
        {
            AddBinding(Utilities.GetKeys(shortcut), Keys.None, command);
        }


        /// <summary>
        ///     Adds a key combination to a Command
        /// </summary>
        /// <param name="shortcut">CharacterStance corresponding to a (keyboard) key to trigger command</param>
        /// <param name="modifiers">Shift, alt, ctrl</param>
        /// <param name="command">Command to execute</param>
        public void AddBinding(char shortcut, Keys modifiers, BindableCommand command)
        {
            AddBinding(Utilities.GetKeys(shortcut), modifiers, command);
        }


        /// <summary>
        ///     Adds a key combination to a Command
        /// </summary>
        /// <param name="shortcut">Key to trigger command</param>
        /// <param name="command">Command to execute</param>
        public void AddBinding(Keys shortcut, BindableCommand command)
        {
            AddBinding(shortcut, Keys.None, command);
        }


        /// <summary>
        ///     Adds a key combination to a Command
        /// </summary>
        /// <param name="shortcut">Key to trigger command</param>
        /// <param name="modifiers">Shift, alt, ctrl</param>
        /// <param name="command">Command to execute</param>
        public void AddBinding(Keys shortcut, Keys modifiers, BindableCommand command)
        {
            var kb = new KeyBinding(shortcut, modifiers);
            if (!this._boundCommands.ContainsKey(kb))
                this._boundCommands.Add(kb, new List<BindableCommand>());

            List<BindableCommand> l = this._boundCommands[kb];
            if (this._allowDuplicateBindings || !l.Contains(command))
                l.Add(command);
        }


        /// <summary>
        ///     Executes a Command
        /// </summary>
        /// <param name="command">Any <see cref="BindableCommand"/></param>
        /// <returns>Value to indicate whether other bound commands should continue to execute</returns>
        public bool Execute(BindableCommand command)
        {
            if ((int)command < 10000)
            {
                NativeScintilla.SendMessageDirect((uint)command, IntPtr.Zero, IntPtr.Zero);
                return true;
            }

            switch (command)
            {
                case BindableCommand.AutoCShow:
                    Scintilla.AutoComplete.Show();
                    return true;

                case BindableCommand.AcceptActiveSnippets:
                    return Scintilla.Snippets.AcceptActiveSnippets();

                case BindableCommand.CancelActiveSnippets:
                    return Scintilla.Snippets.CancelActiveSnippets();

                case BindableCommand.DoSnippetCheck:
                    return Scintilla.Snippets.DoSnippetCheck();

                case BindableCommand.NextSnippetRange:
                    return Scintilla.Snippets.NextSnippetRange();

                case BindableCommand.PreviousSnippetRange:
                    return Scintilla.Snippets.PreviousSnippetRange();

                case BindableCommand.DropMarkerCollect:
                    Scintilla.DropMarkers.Collect();
                    return false;

                case BindableCommand.DropMarkerDrop:
                    Scintilla.DropMarkers.Drop();
                    return true;

                case BindableCommand.Print:
                    Scintilla.Printing.Print();
                    return true;

                case BindableCommand.PrintPreview:
                    Scintilla.Printing.PrintPreview();
                    return true;

                case BindableCommand.ShowFind:
                    Scintilla.FindReplace.ShowFind();
                    return true;

                case BindableCommand.ShowReplace:
                    Scintilla.FindReplace.ShowReplace();
                    return true;

                case BindableCommand.FindNext:
                    Scintilla.FindReplace.Window.FindNext();
                    return true;

                case BindableCommand.FindPrevious:
                    Scintilla.FindReplace.Window.FindPrevious();
                    return true;

                case BindableCommand.IncrementalSearch:
                    Scintilla.FindReplace.IncrementalSearch();
                    return true;

                case BindableCommand.LineComment:
                    Scintilla.Lexing.LineComment();
                    return true;

                case BindableCommand.LineUncomment:
                    Scintilla.Lexing.LineUncomment();
                    return true;

                case BindableCommand.DocumentNavigateForward:
                    Scintilla.DocumentNavigation.NavigateForward();
                    return true;

                case BindableCommand.DocumentNavigateBackward:
                    Scintilla.DocumentNavigation.NavigateBackward();
                    return true;

                case BindableCommand.ToggleLineComment:
                    Scintilla.Lexing.ToggleLineComment();
                    return true;

                case BindableCommand.StreamComment:
                    Scintilla.Lexing.StreamComment();
                    return true;

                case BindableCommand.ShowSnippetList:
                    Scintilla.Snippets.ShowSnippetList();
                    return true;

                case BindableCommand.ShowSurroundWithList:
                    Scintilla.Snippets.ShowSurroundWithList();
                    return true;

                case BindableCommand.ShowGoTo:
                    Scintilla.GoTo.ShowGoToDialog();
                    break;
            }

            return false;
        }


        /// <summary>
        ///     Returns a list of Commands bound to a keyboard shortcut
        /// </summary>
        /// <param name="shortcut">CharacterStance corresponding to a (keyboard) key to trigger command</param>
        /// <returns>List of Commands bound to a keyboard shortcut</returns>
        private List<BindableCommand> GetCommands(char shortcut)
        {
            return GetCommands(Utilities.GetKeys(shortcut), Keys.None);
        }


        /// <summary>
        ///     Returns a list of Commands bound to a keyboard shortcut
        /// </summary>
        /// <param name="shortcut">CharacterStance corresponding to a (keyboard) key to trigger command</param>
        /// <param name="modifiers">Shift, alt, ctrl</param>
        /// <returns>List of Commands bound to a keyboard shortcut</returns>
        private List<BindableCommand> GetCommands(char shortcut, Keys modifiers)
        {
            return GetCommands(Utilities.GetKeys(shortcut), modifiers);
        }


        /// <summary>
        ///     Returns a list of Commands bound to a keyboard shortcut
        /// </summary>
        /// <param name="shortcut">Key to trigger command</param>
        /// <returns>List of Commands bound to a keyboard shortcut</returns>
        private List<BindableCommand> GetCommands(Keys shortcut)
        {
            return GetCommands(shortcut, Keys.None);
        }


        /// <summary>
        ///     Returns a list of Commands bound to a keyboard shortcut
        /// </summary>
        /// <param name="shortcut">Key to trigger command</param>
        /// <param name="modifiers">Shift, alt, ctrl</param>
        /// <returns>List of Commands bound to a keyboard shortcut</returns>
        private List<BindableCommand> GetCommands(Keys shortcut, Keys modifiers)
        {
            var kb = new KeyBinding(shortcut, modifiers);
            return !this._boundCommands.ContainsKey(kb) ? new List<BindableCommand>() : 
                this._boundCommands[kb];
        }


        /// <summary>
        ///     Returns a list of KeyBindings bound to a given command
        /// </summary>
        /// <param name="command">Command to execute</param>
        /// <returns>List of KeyBindings bound to the given command</returns>
        public List<KeyBinding> GetKeyBindings(BindableCommand command)
        {
            return (from item in this._boundCommands
                where item.Value.Contains(command)
                select item.Key).ToList();
        }

        internal bool ProcessKey(KeyEventArgs e)
        {
            this.StopProcessingCommands = false;

            var kb = new KeyBinding(e.KeyCode, e.Modifiers);
            if (!this._boundCommands.ContainsKey(kb))
                return false;

            List<BindableCommand> cmds = this._boundCommands[kb];
            if (cmds.Count == 0)
                return false;

            cmds.Sort(this._commandComparer);

            bool ret = false;
            foreach (BindableCommand cmd in cmds)
            {
                ret |= this.Execute(cmd);

                if (this.StopProcessingCommands)
                    return ret;
            }

            return ret;
        }


        /// <summary>
        ///     Removes all key command bindings
        /// </summary>
        /// <remarks>
        ///     Performing this action will make ARCed.Scintilla virtually unusable until you assign new command bindings.
        ///     This removes even basic functionality like arrow keys, common clipboard commands, home/_end, etc.
        /// </remarks>
        public void RemoveAllBindings()
        {
            this._boundCommands.Clear();
        }


        /// <summary>
        ///     Removes all commands bound to a  keyboard shortcut
        /// </summary>
        /// <param name="shortcut">CharacterStance corresponding to a (keyboard) key to trigger command</param>
        public void RemoveBinding(char shortcut)
        {
            RemoveBinding(Utilities.GetKeys(shortcut), Keys.None);
        }


        /// <summary>
        ///     Removes a keyboard shortcut / command combination
        /// </summary>
        /// <param name="shortcut">CharacterStance corresponding to a (keyboard) key to trigger command</param>
        /// <param name="command">Command to execute</param>
        public void RemoveBinding(char shortcut, BindableCommand command)
        {
            RemoveBinding(Utilities.GetKeys(shortcut), Keys.None, command);
        }


        /// <summary>
        ///     Removes all commands bound to a  keyboard shortcut
        /// </summary>
        /// <param name="shortcut">CharacterStance corresponding to a (keyboard) key to trigger command</param>
        /// <param name="modifiers">Shift, alt, ctrl</param>
        public void RemoveBinding(char shortcut, Keys modifiers)
        {
            RemoveBinding(Utilities.GetKeys(shortcut), modifiers);
        }


        /// <summary>
        ///     Removes a keyboard shortcut / command combination
        /// </summary>
        /// <param name="shortcut">CharacterStance corresponding to a (keyboard) key to trigger command</param>
        /// <param name="modifiers">Shift, alt, ctrl</param>
        /// <param name="command">Command to execute</param>
        public void RemoveBinding(char shortcut, Keys modifiers, BindableCommand command)
        {
            RemoveBinding(Utilities.GetKeys(shortcut), modifiers, command);
        }


        /// <summary>
        ///     Removes all commands bound to a  keyboard shortcut
        /// </summary>
        /// <param name="shortcut">Key to trigger command</param>
        public void RemoveBinding(Keys shortcut)
        {
            RemoveBinding(shortcut, Keys.None);
        }


        /// <summary>
        ///     Removes a keyboard shortcut / command combination
        /// </summary>
        /// <param name="shortcut">Key to trigger command</param>
        /// <param name="command">Command to execute</param>
        public void RemoveBinding(Keys shortcut, BindableCommand command)
        {
            RemoveBinding(shortcut, Keys.None, command);
        }


        /// <summary>
        ///     Removes all commands bound to a  keyboard shortcut
        /// </summary>
        /// <param name="shortcut">Key to trigger command</param>
        /// <param name="modifiers">Shift, alt, ctrl</param>
        public void RemoveBinding(Keys shortcut, Keys modifiers)
        {
            this._boundCommands.Remove(new KeyBinding(shortcut, modifiers));
        }


        /// <summary>
        ///     Removes a keyboard shortcut / command combination
        /// </summary>
        /// <param name="shortcut">Key to trigger command</param>
        /// <param name="modifiers">Shift, alt, ctrl</param>
        /// <param name="command">Command to execute</param>
        public void RemoveBinding(Keys shortcut, Keys modifiers, BindableCommand command)
        {
            var kb = new KeyBinding(shortcut, modifiers);
            if (!this._boundCommands.ContainsKey(kb))
                return;

            this._boundCommands[kb].Remove(command);
        }


        private void ResetAllowDuplicateBindings()
        {
            this._allowDuplicateBindings = true;
        }


        internal bool ShouldSerialize()
        {
            return this.ShouldSerializeAllowDuplicateBindings();
        }


        private bool ShouldSerializeAllowDuplicateBindings()
        {
            return !this._allowDuplicateBindings;
        }

        #endregion Methods


        #region Properties

        /// <summary>
        ///     Gets/Sets if a key combination can be bound to more than one command. (default is true)
        /// </summary>
        /// <remarks>
        ///     When set to false only the first command bound to a key combination is kept.
        ///     Subsequent requests are ignored. 
        /// </remarks>
        public bool AllowDuplicateBindings
        {
            get
            {
                return this._allowDuplicateBindings;
            }
            set
            {
                this._allowDuplicateBindings = value;
            }
        }

        #endregion Properties


        #region Constructors

        internal Commands(Scintilla scintilla) : base(scintilla)
        {

            //	Ha Ha Ha Ha all your commands are belong to us!
            NativeScintilla.ClearAllCmdKeys();

            //	The reason we're doing this is because ARCed.Scintilla is going to own
            //	all the command bindings. There are two reasons for this: #1 it makes
            //	it easier to handle ARCed.Scintilla specific commands, we don't have to
            //	do special logic if its a native command vs. ARCed.Scintilla extension.

            //	#2 Scintilla's built in support for commands binding only allows 1
            //	command per key combination. Our key handling allows for any number
            //	of commands to be bound to a keyboard combination. 

            //	Other future enhancements that I want to do in the future are:
            //	Visual Studioesque Key/Chord commands like Ctrl+D, w

            //	Binding contexts. This is another CodeRush inspired idea where
            //	commands can only execute if a given context is satisfied (or not).
            //	Some examples are "At beginning of line", "In comment", 
            //	"Autocomplete window active", "In Snippet Range".

            //	OK in order for these commands to play nice with each other some of them 
            //	have to have knowledge of each other AND they have to execute in a certain
            //	order. 

            //	Since all the native Scintilla Commands already know how to work together
            //	properly they all have the same order. But our commands have to execute first

            this._commandComparer.CommandOrder.Add(BindableCommand.AutoCShow, 100);
            this._commandComparer.CommandOrder.Add(BindableCommand.AutoCComplete, 100);
            this._commandComparer.CommandOrder.Add(BindableCommand.AutoCCancel, 100);
            this._commandComparer.CommandOrder.Add(BindableCommand.DoSnippetCheck, 200);
            this._commandComparer.CommandOrder.Add(BindableCommand.AcceptActiveSnippets, 200);
            this._commandComparer.CommandOrder.Add(BindableCommand.CancelActiveSnippets, 200);
            this._commandComparer.CommandOrder.Add(BindableCommand.NextSnippetRange, 200);
            this._commandComparer.CommandOrder.Add(BindableCommand.PreviousSnippetRange, 200);

            this.AddBinding(Keys.Down , Keys.None, BindableCommand.LineDown);
            this.AddBinding(Keys.Down , Keys.Shift, BindableCommand.LineDownExtend);
            this.AddBinding(Keys.Down , Keys.Control, BindableCommand.LineScrollDown);
            this.AddBinding(Keys.Down , Keys.Alt | Keys.Shift, BindableCommand.LineDownRectExtend);
            this.AddBinding(Keys.Up , Keys.None, BindableCommand.LineUp);
            this.AddBinding(Keys.Up , Keys.Shift, BindableCommand.LineUpExtend);
            this.AddBinding(Keys.Up , Keys.Control, BindableCommand.LineScrollUp);
            this.AddBinding(Keys.Up , Keys.Alt | Keys.Shift, BindableCommand.LineUpRectExtend);
            this.AddBinding('[',  Keys.Control, BindableCommand.ParaUp);
            this.AddBinding('[' , Keys.Control | Keys.Shift, BindableCommand.ParaUpExtend);
            this.AddBinding(']' , Keys.Control, BindableCommand.ParaDown);
            this.AddBinding(']' , Keys.Control | Keys.Shift, BindableCommand.ParaDownExtend);
            this.AddBinding(Keys.Left , Keys.None, BindableCommand.CharLeft);
            this.AddBinding(Keys.Left , Keys.Shift, BindableCommand.CharLeftExtend);
            this.AddBinding(Keys.Left , Keys.Control, BindableCommand.WordLeft);
            this.AddBinding(Keys.Left , Keys.Control | Keys.Shift, BindableCommand.WordLeftExtend);
            this.AddBinding(Keys.Left , Keys.Alt | Keys.Shift, BindableCommand.CharLeftRectExtend);
            this.AddBinding(Keys.Right , Keys.None, BindableCommand.CharRight);
            this.AddBinding(Keys.Right , Keys.Shift, BindableCommand.CharRightExtend);
            this.AddBinding(Keys.Right , Keys.Control, BindableCommand.WordRight);
            this.AddBinding(Keys.Right , Keys.Control | Keys.Shift, BindableCommand.WordRightExtend);
            this.AddBinding(Keys.Right , Keys.Alt | Keys.Shift, BindableCommand.CharRightRectExtend);
            this.AddBinding('/' , Keys.Control, BindableCommand.WordPartLeft);
            this.AddBinding('/' , Keys.Control | Keys.Shift, BindableCommand.WordPartLeftExtend);
            this.AddBinding('\\' , Keys.Control, BindableCommand.WordPartRight);
            this.AddBinding('\\' , Keys.Control | Keys.Shift, BindableCommand.WordPartRightExtend);
            this.AddBinding(Keys.Home , Keys.None, BindableCommand.VCHome);
            this.AddBinding(Keys.Home , Keys.Shift, BindableCommand.VCHomeExtend);
            this.AddBinding(Keys.Home , Keys.Control, BindableCommand.DocumentStart);
            this.AddBinding(Keys.Home , Keys.Control | Keys.Shift, BindableCommand.DocumentStartExtend);
            this.AddBinding(Keys.Home , Keys.Alt, BindableCommand.HomeDisplay);
            this.AddBinding(Keys.Home , Keys.Alt | Keys.Shift, BindableCommand.VCHomeRectExtend);
            this.AddBinding(Keys.End , Keys.None, BindableCommand.LineEnd);
            this.AddBinding(Keys.End , Keys.Shift, BindableCommand.LineEndExtend);
            this.AddBinding(Keys.End , Keys.Control, BindableCommand.DocumentEnd);
            this.AddBinding(Keys.End , Keys.Control | Keys.Shift, BindableCommand.DocumentEndExtend);
            this.AddBinding(Keys.End , Keys.Alt, BindableCommand.LineEndDisplay);
            this.AddBinding(Keys.End , Keys.Alt | Keys.Shift, BindableCommand.LineEndRectExtend);
            this.AddBinding(Keys.PageUp , Keys.None, BindableCommand.PageUp);
            this.AddBinding(Keys.PageUp , Keys.Shift, BindableCommand.PageUpExtend);
            this.AddBinding(Keys.PageUp , Keys.Alt | Keys.Shift, BindableCommand.PageUpRectExtend);
            this.AddBinding(Keys.PageDown , Keys.None, BindableCommand.PageDown);
            this.AddBinding(Keys.PageDown , Keys.Shift, BindableCommand.PageDownExtend);
            this.AddBinding(Keys.PageDown , Keys.Alt | Keys.Shift, BindableCommand.PageDownRectExtend);
            this.AddBinding(Keys.Delete , Keys.None, BindableCommand.Clear);
            this.AddBinding(Keys.Delete , Keys.Shift, BindableCommand.Cut);
            this.AddBinding(Keys.Delete , Keys.Control, BindableCommand.DelWordRight);
            this.AddBinding(Keys.Delete , Keys.Control | Keys.Shift, BindableCommand.DelLineRight);
            this.AddBinding(Keys.Insert , Keys.None, BindableCommand.EditToggleOvertype);
            this.AddBinding(Keys.Insert , Keys.Shift, BindableCommand.Paste);
            this.AddBinding(Keys.Insert , Keys.Control, BindableCommand.Copy);
            this.AddBinding(Keys.Escape , Keys.None, BindableCommand.Cancel);
            this.AddBinding(Keys.Back , Keys.None, BindableCommand.DeleteBack);
            this.AddBinding(Keys.Back , Keys.Shift, BindableCommand.DeleteBack);
            this.AddBinding(Keys.Back , Keys.Control, BindableCommand.DelWordLeft);
            this.AddBinding(Keys.Back , Keys.Alt, BindableCommand.Undo);
            this.AddBinding(Keys.Back , Keys.Control | Keys.Shift, BindableCommand.DelLineLeft);
            this.AddBinding(Keys.Z, Keys.Control, BindableCommand.Undo);
            this.AddBinding(Keys.Y, Keys.Control, BindableCommand.Redo);
            this.AddBinding(Keys.X, Keys.Control, BindableCommand.Cut);
            this.AddBinding(Keys.C, Keys.Control, BindableCommand.Copy);
            this.AddBinding(Keys.V, Keys.Control, BindableCommand.Paste);
            this.AddBinding(Keys.A, Keys.Control, BindableCommand.SelectAll);
            this.AddBinding(Keys.Tab , Keys.None, BindableCommand.Tab);
            this.AddBinding(Keys.Tab , Keys.Shift, BindableCommand.BackTab);
            this.AddBinding(Keys.Enter , Keys.None, BindableCommand.NewLine);
            this.AddBinding(Keys.Enter , Keys.Shift, BindableCommand.NewLine);
            this.AddBinding(Keys.Add , Keys.Control, BindableCommand.ZoomIn);
            this.AddBinding(Keys.Subtract , Keys.Control, BindableCommand.ZoomOut);
            this.AddBinding(Keys.Divide, Keys.Control, BindableCommand.SetZoom);
            this.AddBinding(Keys.L, Keys.Control, BindableCommand.LineCut);
            this.AddBinding(Keys.L, Keys.Control | Keys.Shift, BindableCommand.LineDelete);
            this.AddBinding(Keys.T , Keys.Control | Keys.Shift, BindableCommand.LineCopy);
            this.AddBinding(Keys.T, Keys.Control, BindableCommand.LineTranspose);
            this.AddBinding(Keys.D, Keys.Control, BindableCommand.SelectionDuplicate);
            this.AddBinding(Keys.U, Keys.Control, BindableCommand.LowerCase);
            this.AddBinding(Keys.U, Keys.Control | Keys.Shift, BindableCommand.UpperCase);

            this.AddBinding(Keys.Space, Keys.Control, BindableCommand.AutoCShow);
            this.AddBinding(Keys.Tab, BindableCommand.DoSnippetCheck);
            this.AddBinding(Keys.Tab, BindableCommand.NextSnippetRange);
            this.AddBinding(Keys.Tab, Keys.Shift, BindableCommand.PreviousSnippetRange);
            this.AddBinding(Keys.Escape, BindableCommand.CancelActiveSnippets);
            this.AddBinding(Keys.Enter, BindableCommand.AcceptActiveSnippets);

            this.AddBinding(Keys.P, Keys.Control, BindableCommand.Print);
            this.AddBinding(Keys.P, Keys.Control | Keys.Shift, BindableCommand.PrintPreview);

            this.AddBinding(Keys.F, Keys.Control, BindableCommand.ShowFind);
            this.AddBinding(Keys.H, Keys.Control, BindableCommand.ShowReplace);
            this.AddBinding(Keys.F3, BindableCommand.FindNext);
            this.AddBinding(Keys.F3, Keys.Shift, BindableCommand.FindPrevious);
            this.AddBinding(Keys.I, Keys.Control, BindableCommand.IncrementalSearch);

            this.AddBinding(Keys.Q, Keys.Control, BindableCommand.LineComment);
            this.AddBinding(Keys.Q, Keys.Control | Keys.Shift, BindableCommand.LineUncomment);

            this.AddBinding('-', Keys.Control, BindableCommand.DocumentNavigateBackward);
            this.AddBinding('-', Keys.Control | Keys.Shift, BindableCommand.DocumentNavigateForward);

            this.AddBinding(Keys.J, Keys.Control, BindableCommand.ShowSnippetList);

            this.AddBinding(Keys.M, Keys.Control, BindableCommand.DropMarkerDrop);
            this.AddBinding(Keys.Escape, BindableCommand.DropMarkerCollect);

            this.AddBinding(Keys.G, Keys.Control, BindableCommand.ShowGoTo);
        }

        #endregion Constructors


        #region Types

        private class CommandComparer : IComparer<BindableCommand>
        {
            #region Fields

            private Dictionary<BindableCommand, int> _commandOrder = new Dictionary<BindableCommand, int>();

            #endregion Fields


            #region Methods

            public int Compare(BindableCommand x, BindableCommand y)
            {
                return this.GetCommandOrder(y).CompareTo(this.GetCommandOrder(x));
            }


            private int GetCommandOrder(BindableCommand cmd)
            {
                return !this._commandOrder.ContainsKey(cmd) ? 0 : this._commandOrder[cmd];
            }

            #endregion Methods


            #region Properties

            public Dictionary<BindableCommand, int> CommandOrder
            {
                get
                {
                    return this._commandOrder;
                }
                set
                {
                    this._commandOrder = value;
                }
            }

            #endregion Properties
        }

        #endregion Types
    }
}
