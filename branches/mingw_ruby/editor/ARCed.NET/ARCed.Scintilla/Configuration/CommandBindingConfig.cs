#region Using Directives



#endregion Using Directives


namespace ARCed.Scintilla.Configuration
{
    public struct CommandBindingConfig
    {
        #region Fields

        public KeyBinding KeyBinding;
        public bool? ReplaceCurrent;
        public BindableCommand BindableCommand;

        #endregion Fields


        #region Constructors

        /// <summary>
        ///     Initializes a new instance of the CommandBindingConfig structure.
        /// </summary>
        public CommandBindingConfig(KeyBinding keyBinding, bool? replaceCurrent, BindableCommand bindableCommand)
        {
            this.KeyBinding = keyBinding;
            this.ReplaceCurrent = replaceCurrent;
            this.BindableCommand = bindableCommand;
        }

        #endregion Constructors
    }
}
