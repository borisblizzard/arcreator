#region Using Directives

using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

#endregion


namespace ARCed.Scintilla
{
    /// <summary>
    ///     Used to invoke AutoComplete and UserList windows. Also manages AutoComplete
    ///     settings.
    /// </summary>
    /// <remarks>
    ///     Autocomplete is typically used in IDEs to automatically complete some kind
    ///     of identifier or keyword based on a partial name. 
    /// </remarks>
    [TypeConverter(typeof(ExpandableObjectConverter))]
    public class AutoComplete : TopLevelHelper
    {
        #region Fields

        private List<string> _list = new List<string>();
        private string _stopCharacters = string.Empty;
        private bool _automaticLengthEntered = true;
        private string _fillUpCharacters = string.Empty;

        #endregion Fields


        #region Methods

        /// <summary>
        ///     Accepts the current AutoComplete window entry
        /// </summary>
        /// <remarks>
        ///     If the AutoComplete window is open Accept() will close it. This also causes the
        ///     <see cref="Scintilla.AutoCompleteAccepted" /> event to fire
        /// </remarks>
        public void Accept()
        {
            NativeScintilla.AutoCComplete();
        }


        /// <summary>
        ///     Cancels the autocomplete window
        /// </summary>
        /// <remarks>
        ///     If the AutoComplete window is displayed calling Cancel() will close the window. 
        /// </remarks>
        public void Cancel()
        {
            NativeScintilla.AutoCCancel();
        }


        /// <summary>
        ///     Deletes all registered images.
        /// </summary>
        public void ClearRegisteredImages()
        {
            NativeScintilla.ClearRegisteredImages();
        }


        private int GetLengthEntered()
        {
            if (!this._automaticLengthEntered)
                return 0;

            int pos = NativeScintilla.GetCurrentPos();
            return pos - NativeScintilla.WordStartPosition(pos, true);
        }


        private string GetListString(IEnumerable<string> list)
        {
            var listString = new StringBuilder();
            foreach (string s in list)
            {
                listString.Append(s).Append(this.ListSeparator);
            }
            if (listString.Length > 1)
                listString.Remove(listString.Length - 1, 1);

            return listString.ToString().Trim();
        }


        /// <summary>
        ///     Registers an _srcTexture with index to be displayed in the AutoComplete window.
        /// </summary>
        /// <param name="type">Index of the _srcTexture to register to</param>
        /// <param name="image">Image to display in Bitmap format</param>
        private void RegisterImage(int type, Bitmap image)
        {
            NativeScintilla.RegisterImage(type, XpmConverter.ConvertToXPM(image));
        }


        /// <summary>
        ///     Registers an _srcTexture with index to be displayed in the AutoComplete window.
        /// </summary>
        /// <param name="type">Index of the _srcTexture to register to</param>
        /// <param name="image">Image to display in the XPM _srcTexture format</param>
        /// <param name="transparentColor">Color to mask the _srcTexture as transparent</param>
        private void RegisterImage(int type, Bitmap image, Color transparentColor)
        {
            NativeScintilla.RegisterImage(type, XpmConverter.ConvertToXPM(image, Utilities.ColorToHtml(transparentColor)));
        }


        /// <summary>
        ///     Registers an _srcTexture with index to be displayed in the AutoComplete window.
        /// </summary>
        /// <param name="type">Index of the _srcTexture to register to</param>
        /// <param name="xpmImage">Image in the XPM _srcTexture format</param>
        public void RegisterImage(int type, string xpmImage)
        {
            NativeScintilla.RegisterImage(type, xpmImage);
        }


        /// <summary>
        ///     Registers a list of images to be displayed in the AutoComplete window.
        /// </summary>
        /// <param name="images">List of images in the Bitmap _srcTexture format</param>
        /// <remarks>Indecis are assigned sequentially starting at 0</remarks>
        public void RegisterImages(IList<Bitmap> images)
        {
            for (int i = 0; i < images.Count; i++)
                RegisterImage(i, images[i]);
        }


        /// <summary>
        ///     Registers a list of images to be displayed in the AutoComplete window.
        /// </summary>
        /// <param name="images">List of images in the Bitmap _srcTexture format</param>
        /// <param name="transparentColor">Color to mask the _srcTexture as transparent</param>
        /// <remarks>Indecis are assigned sequentially starting at 0</remarks>
        public void RegisterImages(IList<Bitmap> images, Color transparentColor)
        {
            for (int i = 0; i < images.Count; i++)
                this.RegisterImage(i, images[i], transparentColor);
        }


        /// <summary>
        ///     Registers a list of images to be displayed in the AutoComplete window.
        /// </summary>
        /// <param name="xpmImages">List of images in the XPM _srcTexture format</param>
        /// <remarks>Indecis are assigned sequentially starting at 0</remarks>
        public void RegisterImages(IList<string> xpmImages)
        {
            for (int i = 0; i < xpmImages.Count; i++)
                NativeScintilla.RegisterImage(i, xpmImages[i]);
        }


        /// <summary>
        ///     Registers a list of images to be displayed in the AutoComplete window.
        /// </summary>
        /// <param name="images">List of images contained in an ImageList</param>
        /// <remarks>Indecis are assigned sequentially starting at 0</remarks>
        public void RegisterImages(ImageList images)
        {
            RegisterImages(XpmConverter.ConvertToXPM(images));
        }


        /// <summary>
        ///     Registers a list of images to be displayed in the AutoComplete window.
        /// </summary>
        /// <param name="images">List of images contained in an ImageList</param>
        /// <param name="transparentColor">Color to mask the _srcTexture as transparent</param>
        /// <remarks>Indecis are assigned sequentially starting at 0</remarks>
        public void RegisterImages(ImageList images, Color transparentColor)
        {
            RegisterImages(XpmConverter.ConvertToXPM(images, Utilities.ColorToHtml(transparentColor)));
        }


        private void ResetAutoHide()
        {
            this.AutoHide = true;
        }


        private void ResetAutomaticLengthEntered()
        {
            this.AutomaticLengthEntered = true;
        }


        private void ResetCancelAtStart()
        {
            this.CancelAtStart = true;
        }


        private void ResetDropRestOfWord()
        {
            this.DropRestOfWord = false;
        }


        private void ResetFillUpCharacters()
        {
            this._fillUpCharacters = string.Empty;
        }


        private void ResetImageSeparator()
        {
            this.ImageSeparator = '?';
        }


        private void ResetIsCaseSensitive()
        {
            this.IsCaseSensitive = true;
        }


        private void ResetListSeparator()
        {
            this.ListSeparator = ' ';
        }


        private void ResetMaxHeight()
        {
            this.MaxHeight = 5;
        }


        private void ResetMaxWidth()
        {
            this.MaxWidth = 0;
        }


        private void ResetSingleLineAccept()
        {
            this.SingleLineAccept = false;
        }


        private void ResetStopCharacters()
        {
            this._stopCharacters = string.Empty;
        }


        internal bool ShouldSerialize()
        {
            return this.ShouldSerializeAutoHide() ||
                this.ShouldSerializeCancelAtStart() ||
                this.ShouldSerializeDropRestOfWord() ||
                this.ShouldSerializeFillUpCharacters() ||
                this.ShouldSerializeImageSeparator() ||
                this.ShouldSerializeIsCaseSensitive() ||
                this.ShouldSerializeListSeparator() ||
                this.ShouldSerializeMaxHeight() ||
                this.ShouldSerializeMaxWidth() ||
                this.ShouldSerializeSingleLineAccept() ||
                this.ShouldSerializeStopCharacters();
        }


        private bool ShouldSerializeAutoHide()
        {
            return !this.AutoHide;
        }


        private bool ShouldSerializeAutomaticLengthEntered()
        {
            return !this.AutomaticLengthEntered;
        }


        private bool ShouldSerializeCancelAtStart()
        {
            return !this.CancelAtStart;
        }


        private bool ShouldSerializeDropRestOfWord()
        {
            return this.DropRestOfWord;
        }


        private bool ShouldSerializeFillUpCharacters()
        {
            return this._fillUpCharacters != string.Empty;
        }


        private bool ShouldSerializeImageSeparator()
        {
            return this.ImageSeparator != '?';
        }


        private bool ShouldSerializeIsCaseSensitive()
        {
            return !this.IsCaseSensitive;
        }


        private bool ShouldSerializeListSeparator()
        {
            return this.ListSeparator != ' ';
        }


        private bool ShouldSerializeMaxHeight()
        {
            return this.MaxHeight != 5;
        }


        private bool ShouldSerializeMaxWidth()
        {
            return this.MaxWidth != 0;
        }


        private bool ShouldSerializeSingleLineAccept()
        {
            return this.SingleLineAccept;
        }


        private bool ShouldSerializeStopCharacters()
        {
            return this._stopCharacters != string.Empty;
        }


        /// <summary>
        ///     Shows the autocomplete window.
        /// </summary>
        /// <remarks>
        ///     This overload assumes that the <see cref="List"/> property has been
        ///     set. The lengthEntered is automatically detected by the editor.
        /// </remarks>
        public void Show()
        {
            this.Show(-1, this.GetListString(this._list), false);
        }


        /// <summary>
        ///     Shows the autocomplete window
        /// </summary>
        /// <param name="list">
        ///     Sets the <see cref="List"/> property. 
        ///     In this overload the lengthEntered is automatically detected by the editor.
        /// </param>
        public void Show(IEnumerable<string> list)
        {
            this._list = new List<string>(list);
            this.Show(-1);
        }


        /// <summary>
        ///     Shows the autocomplete window
        /// </summary>
        /// <param name="lengthEntered">Number of characters of the current word already entered in the editor </param>
        /// <remarks>
        ///     This overload assumes that the <see cref="List"/> property has been set.
        /// </remarks>
        public void Show(int lengthEntered)
        {
            this.Show(lengthEntered, this.GetListString(this._list), false);
        }


        /// <summary>
        ///     Shows the autocomplete window
        /// </summary>
        /// <param name="lengthEntered">Number of characters of the current word already entered in the editor </param>
        /// <param name="list">Sets the <see cref="List"/> property. </param>
        public void Show(int lengthEntered, IEnumerable<string> list)
        {
            this._list = new List<string>(list);
            this.Show(-1);
        }


        /// <summary>
        ///     Shows the autocomplete window.
        /// </summary>
        /// <param name="lengthEntered">Number of characters of the current word already entered in the editor </param>
        /// <param name="list">Sets the <see cref="ListString"/> property. </param>
        public void Show(int lengthEntered, string list)
        {
            this._list = list == string.Empty ? new List<string>() : 
                new List<string>(list.Split(this.ListSeparator));
            this.Show(lengthEntered, list, true);
        }

        internal void Show(int lengthEntered, string list, bool dontSplit)
        {
            //	We may have the auto-detect of lengthEntered. In which case
            //	look for the last word character as the _start
            int le = lengthEntered;
            if (le < 0)
                le = this.GetLengthEntered();

            NativeScintilla.AutoCShow(le, list);

            //	Now it may have been that the auto-detect lengthEntered
            //	caused to AutoCShow call to fail becuase no words matched
            //	the letters we autodetected. In this case just show the
            //	list with a 0 lengthEntered to make sure it will show
            if (!this.IsActive && lengthEntered < 0)
                NativeScintilla.AutoCShow(0, list);
        }


        /// <summary>
        ///     Shows the autocomplete window.
        /// </summary>
        /// <param name="list">Sets the <see cref="ListString"/> property. </param>
        /// <remarks>
        ///     In this overload the lengthEntered is automatically detected by the editor.
        /// </remarks>
        public void Show(string list)
        {
            Show(-1, list);
        }


        /// <summary>
        ///     Shows a UserList window
        /// </summary>
        /// <param name="listType">Index of the userlist to show. Can be any integer</param>
        /// <param name="list">List of words to show.</param>
        /// <remarks>
        ///     UserLists are not as powerful as autocomplete but can be assigned to a user defined index.
        /// </remarks>
        public void ShowUserList(int listType, IEnumerable<string> list)
        {
            this.Show(listType, this.GetListString(list), true);
        }


        /// <summary>
        ///     Shows a UserList window
        /// </summary>
        /// <param name="listType">Index of the userlist to show. Can be any integer</param>
        /// <param name="list">List of words to show separated by " "</param>
        /// <remarks>
        ///     UserLists are not as powerful as autocomplete but can be assigned to a user defined index.
        /// </remarks>
        public void ShowUserList(int listType, string list)
        {
            NativeScintilla.UserListShow(listType, list);
        }

        #endregion Methods


        #region Properties

        /// <summary>
        ///     By default, the list is cancelled if there are no viable matches (the user has typed characters that no longer match a list entry). 
        ///     If you want to keep displaying the original list, set AutoHide to false. 
        /// </summary>
        public bool AutoHide
        {
            get
            {
                return NativeScintilla.AutoCGetAutoHide();
            }
            set
            {
                NativeScintilla.AutoCSetAutoHide(value);
            }
        }


        /// <summary>
        /// Gets or Sets the last automatically calculated LengthEntered used 
        /// with <see cref="System.Windows.Forms.Control.Show" />.
        /// </summary>
        public bool AutomaticLengthEntered
        {
            get
            {
                return this._automaticLengthEntered;
            }
            set
            {
                this._automaticLengthEntered = value;
            }
        }


        /// <summary>
        ///     The default behavior is for the list to be cancelled if the caret moves before the location it was at when the list was displayed. 
        ///     By setting this property to false, the list is not cancelled until the caret moves before the first character of the word being completed.
        /// </summary>
        public bool CancelAtStart
        {
            get
            {
                return NativeScintilla.AutoCGetCancelAtStart();
            }
            set
            {
                NativeScintilla.AutoCSetCancelAtStart(value);
            }
        }


        /// <summary>
        ///     When an item is selected, any word characters following the caret are first erased if dropRestOfWord is set to true.
        /// </summary>
        /// <remarks>Defaults to false</remarks>
        public bool DropRestOfWord
        {
            get
            {
                return NativeScintilla.AutoCGetDropRestOfWord();
            }
            set
            {
                NativeScintilla.AutoCSetDropRestOfWord(value);
            }
        }


        /// <summary>
        ///     List of characters (no separated) that causes the AutoComplete window to accept the current
        ///     selection.
        /// </summary>
        public string FillUpCharacters
        {
            get
            {
                return this._fillUpCharacters;
            }
            set
            {
                this._fillUpCharacters = value;
                NativeScintilla.AutoCSetFillUps(value);
            }
        }


        /// <summary>
        ///     Autocompletion list items may display an _srcTexture as well as text. Each _srcTexture is first registered with an integer type. 
        ///     Then this integer is included in the text of the list separated by a '?' from the text. For example, "fclose?2 fopen" 
        ///     displays _srcTexture 2 before the string "fclose" and no _srcTexture before "fopen". 
        /// </summary>
        public char ImageSeparator
        {
            get
            {
                return NativeScintilla.AutoCGetTypeSeparator();
            }
            set
            {
                NativeScintilla.AutoCSetTypeSeparator(value);
            }
        }


        /// <summary>
        ///     Returns wether or not the AutoComplete window is currently displayed
        /// </summary>
        [Browsable(false)]
        public bool IsActive
        {
            get
            {
                return NativeScintilla.AutoCActive();
            }
        }


        /// <summary>
        ///     Gets or Sets if the comparison of words to the AutoComplete <see cref="List"/> are case sensitive.
        /// </summary>
        /// <remarks>Defaults to true</remarks>
        public bool IsCaseSensitive
        {
            get
            {
                return !NativeScintilla.AutoCGetIgnoreCase();
            }
            set
            {
                NativeScintilla.AutoCSetIgnoreCase(!value);
            }
        }


        /// <summary>
        ///     Gets the document posision when the AutoComplete window was last invoked
        /// </summary>
        [Browsable(false)]
        public int LastStartPosition
        {
            get
            {
                return NativeScintilla.AutoCPosStart();
            }
        }


        /// <summary>
        ///     List if words to display in the AutoComplete window when invoked.
        /// </summary>
        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public List<string> List
        {
            get
            {
                return this._list;
            }
            set
            {
                if (value == null)
                    value = new List<string>();

                this._list = value;
            }
        }


        /// <summary>
        ///     CharacterStance used to split <see cref="ListString"/> to convert to a List.
        /// </summary>
        [TypeConverter(typeof(WhitespaceStringConverter))]
        public char ListSeparator
        {
            get
            {
                return NativeScintilla.AutoCGetSeparator();
            }
            set
            {
                NativeScintilla.AutoCSetSeparator(value);
            }
        }


        /// <summary>
        ///     List of words to display in the AutoComplete window.
        /// </summary>
        /// <remarks>
        ///     The list of words separated by <see cref="ListSeparator"/> which
        ///     is " " by default.
        /// </remarks>
        public string ListString
        {
            get
            {
                return this.GetListString(this._list);
            }
            set
            {
                this._list = new List<string>(value.Split(this.ListSeparator));
            }
        }


        /// <summary>
        ///     Get or set the maximum number of rows that will be visible in an autocompletion list. If there are more rows in the list, then a vertical scrollbar is shown
        /// </summary>
        /// <remarks>Defaults to 5</remarks>
        public int MaxHeight
        {
            get
            {
                return NativeScintilla.AutoCGetMaxHeight();
            }
            set
            {
                NativeScintilla.AutoCSetMaxHeight(value);
            }
        }


        /// <summary>
        ///     Get or set the maximum width of an autocompletion list expressed as the number of characters in the longest item that will be totally visible. 
        /// </summary>
        /// <remarks>
        ///     If zero (the default) then the list's width is calculated to fit the item with the most characters. Any items that cannot be fully displayed 
        ///     within the available width are indicated by the presence of ellipsis.
        /// </remarks>
        public int MaxWidth
        {
            get
            {
                return NativeScintilla.AutoCGetMaxWidth();
            }
            set
            {
                NativeScintilla.AutoCSetMaxWidth(value);
            }
        }


        /// <summary>
        ///     Gets or Sets the index of the currently selected item in the AutoComplete <see cref="List"/>
        /// </summary>
        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public int SelectedIndex
        {
            get
            {
                return NativeScintilla.AutoCGetCurrent();
            }
            set
            {
                this.SelectedText = this._list[value];
            }
        }


        /// <summary>
        ///     Gets or Sets the Text of the currently selected AutoComplete item.
        /// </summary>
        /// <remarks>
        ///     When setting this property it does not change the text of the currently
        ///     selected item. Instead it searches the list for the given value and selects
        ///     that item if it matches.
        /// </remarks>
        [Browsable(false), DesignerSerializationVisibility(DesignerSerializationVisibility.Hidden)]
        public string SelectedText
        {
            get
            {
                return this._list[NativeScintilla.AutoCGetCurrent()];
            }
            set
            {
                NativeScintilla.AutoCSelect(value);
            }
        }


        /// <summary>
        ///     If you set this value to true and a list has only one item, it is automatically added and no list is displayed.
        ///     The default is to display the list even if there is only a single item.
        /// </summary>
        public bool SingleLineAccept
        {
            get
            {
                return NativeScintilla.AutoCGetChooseSingle();
            }
            set
            {
                NativeScintilla.AutoCSetChooseSingle(value);
            }
        }


        /// <summary>
        ///     List of characters (no separator) that causes the AutoComplete window to cancel.
        /// </summary>
        public string StopCharacters
        {
            get
            {
                return this._stopCharacters;
            }
            set
            {
                this._stopCharacters = value;
                NativeScintilla.AutoCStops(value);
            }
        }

        #endregion Properties


        #region Constructors

        internal AutoComplete(Scintilla scintilla) : base(scintilla)
        {
        }

        #endregion Constructors
    }
}
