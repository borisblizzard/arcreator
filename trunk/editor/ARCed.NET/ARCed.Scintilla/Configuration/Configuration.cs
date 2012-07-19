#region Using Directives

using System;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text.RegularExpressions;
using System.Windows.Forms;
using System.Xml;

#endregion


namespace ARCed.Scintilla.Configuration
{
    public class Configuration
    {
        #region Fields

        private bool? _autoComplete_AutoHide;
        private bool? _autoComplete_AutomaticLengthEntered;
        private bool? _autoComplete_cancelAtStart;
        private bool? _autoComplete_DropRestOfWord;
        private string _autoComplete_fillUpCharacters;
        private char? _autoComplete_ImageSeperator;
        private bool? _autoComplete_IsCaseSensitive;
        private string _autoComplete_List;
        private bool? _autoComplete_ListInherit;
        private char? _autoComplete_ListSeperator;
        private int? _autoComplete_MaxHeight;
        private int? _autoComplete_MaxWidth;
        private bool? _autoComplete_singleLineAccept;
        private string _autoComplete_StopCharacters;
        private Color _callTip_BackColor;
        private Color _callTip_ForeColor;
        private Color _callTip_HighlightTextColor;
        private int? _caret_BlinkRate;
        private Color _caret_Color;
        private int? _caret_CurrentLineBackgroundAlpha;
        private Color _caret_CurrentLineBackgroundColor;
        private bool? _caret_HighlightCurrentLine;
        private bool? _caret_IsSticky;
        private CaretStyle? _caret_Style;
        private int? _caret_Width;
        private bool? _clipboard_ConvertLineBreaksOnPaste;
        private CommandBindingConfigList _commands_KeyBindingList = new CommandBindingConfigList();
        private string _dropMarkers_SharedStackName;
        private bool? _endOfLine_IsVisisble;
        private EndOfLineMode? _endOfLine_Mode;
        private FoldFlag? _folding_Flags;
        private bool? _folding_IsEnabled;
        private FoldMarkerScheme? _folding_MarkerScheme;
        private bool? _folding_UseCompactFolding;
        private bool _hasData;
        private Color _hotspot_ActiveBackColor;
        private Color _hotspot_ActiveForeColor;
        private bool? _hotspot_ActiveUnderline;
        private bool? _hotspot_SingleLine;
        private bool? _hotspot_UseActiveBackColor;
        private bool? _hotspot_UseActiveForeColor;
        private bool? _indentation_BackspaceUnindents;
        private int? _indentation_IndentWidth;
        private bool? _indentation_ShowGuides;
        private SmartIndent? _indentation_SmartIndentType;
        private bool? _indentation_TabIndents;
        private int? _indentation_TabWidth;
        private bool? _indentation_UseTabs;
        private IndicatorConfigList _indicator_List = new IndicatorConfigList();
        private string _language;
        private KeyWordConfigList _lexing_Keywords = new KeyWordConfigList();
        private string _lexing_Language;
        private string _lexing_LineCommentPrefix;
        private LexerPropertiesConfig _lexing_Properties = new LexerPropertiesConfig();
        private string _lexing_StreamCommentPrefix;
        private string _lexing_StreamCommentSuffix;
        private string _lexing_WhitespaceChars;
        private string _lexing_WordChars;
        private LineWrappingMode? _lineWrapping_Mode;
        private LineWrappingIndentMode? _lineWrapping_IndentMode;
        private int? _lineWrapping_IndentSize;
        private LineWrappingVisualFlags? _lineWrapping_VisualFlags;
        private LineWrappingVisualFlagsLocations? _lineWrapping_VisualFlagsLocations;
        private Color _longLines_EdgeColor;
        private int? _longLines_EdgeColumn;
        private EdgeMode? _longLines_EdgeMode;
        private MarginConfigList _margin_List = new MarginConfigList();
        private MarkersConfigList _markers_List;
        private bool? _scrolling_EndAtLastLine;
        private int? _scrolling_HorizontalWidth;
        private ScrollBars? _scrolling_ScrollBars;
        private int? _scrolling_XOffset;
        private Color _selection_BackColor;
        private Color _selection_BackColorUnfocused;
        private Color _selection_ForeColor;
        private Color _selection_ForeColorUnfocused;
        private bool? _selection_Hidden;
        private bool? _selection_HideSelection;
        private SelectionMode? _selection_Mode;
        private SnippetsConfigList _snippetsConfigList = new SnippetsConfigList();
        private StyleConfigList _styles = new StyleConfigList();
        private bool? _undoRedoIsUndoEnabled;
        private Color _whitespace_BackColor;
        private Color _whitespace_ForeColor;
        private WhitespaceMode? _whitespace_Mode;

        #endregion Fields


        #region Methods

        private bool? getBool(string s)
        {
            s = s.ToLower();

            switch (s)
            {
                case "true":
                case "t":
                case "1":
                case "y":
                case "yes":
                    return true;
                case "false":
                case "f":
                case "0":
                case "n":
                case "no":
                    return false;
            }

            return null;
        }


        private char? getChar(string s)
        {
            if (string.IsNullOrEmpty(s))
                return null;

            return s[0];
        }


        private Color getColor(string s)
        {
            return (Color)new ColorConverter().ConvertFromString(s);
        }


        private int? getInt(string s)
        {
            int i;
            if (int.TryParse(s, out i))
                return i;

            return null;
        }


        private string getString(XmlAttribute a)
        {
            return a == null ? null : a.Value;
        }

        private StyleConfig getStyleConfigFromElement(XmlReader reader)
        {
            var sc = new StyleConfig();
            if (reader.HasAttributes)
            {
                while (reader.MoveToNextAttribute())
                {
                    string attrName = reader.Name.ToLower();
                    switch (attrName)
                    {
                        case "name":
                            sc.Name = reader.Value;
                            break;
                        case "number":
                            sc.Number = this.getInt(reader.Value);
                            break;
                        case "backcolor":
                            sc.BackColor = this.getColor(reader.Value);
                            break;
                        case "bold":
                            sc.Bold = this.getBool(reader.Value);
                            break;
                        case "case":
                            sc.Case = (StyleCase)Enum.Parse(typeof(StyleCase), reader.Value, true);
                            break;
                        case "characterset":
                            sc.CharacterSet = (CharacterSet)Enum.Parse(typeof(CharacterSet), reader.Value, true);
                            break;
                        case "fontname":
                            sc.FontName = reader.Value;
                            break;
                        case "forecolor":
                            sc.ForeColor = this.getColor(reader.Value);
                            break;
                        case "ischangeable":
                            sc.IsChangeable = this.getBool(reader.Value);
                            break;
                        case "ishotspot":
                            sc.IsHotspot = this.getBool(reader.Value);
                            break;
                        case "isselectioneolfilled":
                            sc.IsSelectionEolFilled = this.getBool(reader.Value);
                            break;
                        case "isvisible":
                            sc.IsVisible = this.getBool(reader.Value);
                            break;
                        case "italic":
                            sc.Italic = this.getBool(reader.Value);
                            break;
                        case "size":
                            sc.Size = this.getInt(reader.Value);
                            break;
                        case "underline":
                            sc.Underline = this.getBool(reader.Value);
                            break;
                        case "inherit":
                            sc.Inherit = this.getBool(reader.Value);
                            break;
                    }
                }
                reader.MoveToElement();
            }

            return sc;
        }


        public void Load(TextReader txtReader)
        {
            var configDocument = new XmlDocument
            {
                PreserveWhitespace = true
            };
            configDocument.Load(txtReader);
            Load(configDocument);
        }


        public void Load(XmlReader reader)
        {
            reader.ReadStartElement();
            

            while (!reader.EOF)
            {
                if (reader.Name.Equals("language", StringComparison.OrdinalIgnoreCase) && reader.HasAttributes)
                {
                    while (reader.MoveToNextAttribute())
                    {
                        if (reader.Name.Equals("name", StringComparison.OrdinalIgnoreCase) && reader.Value.Equals(this._language, StringComparison.OrdinalIgnoreCase))
                        {
                            this.ReadLanguage(reader);
                            this._hasData = true;
                        }
                    }

                    if (this._hasData)
                        reader.Skip();
                }
                else
                {
                    reader.Skip();
                    continue;
                }

                
                reader.Read();
            }

            reader.Close();
        }


        public void Load(XmlDocument configDocument)
        {
            var langNode = configDocument.DocumentElement.SelectSingleNode("./Language[@Name='" + this._language + "']") as XmlElement;
            if (langNode == null)
                return;

            var autoCNode = langNode.SelectSingleNode("AutoComplete") as XmlElement;
            if (autoCNode != null)
            {
                this._autoComplete_AutoHide = this.getBool(autoCNode.GetAttribute("AutoHide"));
                this._autoComplete_AutomaticLengthEntered = this.getBool(autoCNode.GetAttribute("AutomaticLengthEntered"));
                this._autoComplete_cancelAtStart = this.getBool(autoCNode.GetAttribute("CancelAtStart"));
                this._autoComplete_DropRestOfWord = this.getBool(autoCNode.GetAttribute("DropRestOfWord"));
                this._autoComplete_fillUpCharacters = this.getString(autoCNode.GetAttributeNode("FillUpCharacters"));
                this._autoComplete_ImageSeperator = this.getChar(autoCNode.GetAttribute("AutomaticLengthEntered"));
                this._autoComplete_IsCaseSensitive = this.getBool(autoCNode.GetAttribute("IsCaseSensitive"));
                this._autoComplete_ListSeperator = this.getChar(autoCNode.GetAttribute("ListSeperator"));
                this._autoComplete_MaxHeight = this.getInt(autoCNode.GetAttribute("MaxHeight"));
                this._autoComplete_MaxWidth = this.getInt(autoCNode.GetAttribute("MaxWidth"));
                this._autoComplete_singleLineAccept = this.getBool(autoCNode.GetAttribute("SingleLineAccept"));
                this._autoComplete_StopCharacters = this.getString(autoCNode.GetAttributeNode("StopCharacters"));

                var listNode = autoCNode.SelectSingleNode("./List") as XmlElement;
                if (listNode != null)
                {
                    this._autoComplete_ListInherit = this.getBool(listNode.GetAttribute("Inherit"));
                    this._autoComplete_List = new Regex("\\s+").Replace(listNode.InnerText, " ").Trim();

                }
            }
            autoCNode = null;

            var callTipNode = langNode.SelectSingleNode("CallTip") as XmlElement;
            if (callTipNode != null)
            {
                this._callTip_BackColor = this.getColor(callTipNode.GetAttribute("BackColor"));
                this._callTip_ForeColor = this.getColor(callTipNode.GetAttribute("ForeColor"));
                this._callTip_HighlightTextColor = this.getColor(callTipNode.GetAttribute("HighlightTextColor"));
            }
            callTipNode = null;

            var caretNode = langNode.SelectSingleNode("Caret") as XmlElement;
            if (caretNode != null)
            {
                //	This guy is a bit of an oddball becuase null means "I don't Care"
                //	and we need some way of using the OS value.
                string blinkRate = caretNode.GetAttribute("BlinkRate");
                if (blinkRate.ToLower() == "system")
                    this._caret_BlinkRate = SystemInformation.CaretBlinkTime;
                else
                    this._caret_BlinkRate = this.getInt(blinkRate);

                this._caret_Color = this.getColor(caretNode.GetAttribute("Color"));
                this._caret_CurrentLineBackgroundAlpha = this.getInt(caretNode.GetAttribute("CurrentLineBackgroundAlpha"));
                this._caret_CurrentLineBackgroundColor = this.getColor(caretNode.GetAttribute("CurrentLineBackgroundColor"));
                this._caret_HighlightCurrentLine = this.getBool(caretNode.GetAttribute("HighlightCurrentLine"));
                this._caret_IsSticky = this.getBool(caretNode.GetAttribute("IsSticky"));
                try
                {
                    this._caret_Style = (CaretStyle)Enum.Parse(typeof(CaretStyle), caretNode.GetAttribute("Style"), true);
                }
                catch (ArgumentException) { }
                this._caret_Width = this.getInt(caretNode.GetAttribute("Width"));
            }
            caretNode = null;

            var clipboardNode = langNode.SelectSingleNode("Clipboard") as XmlElement;
            if (clipboardNode != null)
            {
                this._clipboard_ConvertLineBreaksOnPaste = this.getBool(clipboardNode.GetAttribute("ConvertLineBreaksOnPaste"));
            }
            clipboardNode = null;

            this._commands_KeyBindingList = new CommandBindingConfigList();
            var commandsNode = langNode.SelectSingleNode("Commands") as XmlElement;
            if (commandsNode != null)
            {
                this._commands_KeyBindingList.Inherit = this.getBool(commandsNode.GetAttribute("Inherit"));
                this._commands_KeyBindingList.AllowDuplicateBindings = this.getBool(commandsNode.GetAttribute("AllowDuplicateBindings"));
                foreach (XmlElement el in commandsNode.SelectNodes("./Binding"))
                {
                    var kb = new KeyBinding
                    {
                        KeyCode = Utilities.GetKeys(el.GetAttribute("Key"))
                    };

                    string modifiers = el.GetAttribute("Modifier");
                    if (modifiers != string.Empty)
                    {
                        foreach (string modifier in modifiers.Split(' '))
                            kb.Modifiers |= (Keys)Enum.Parse(typeof(Keys), modifier.Trim(), true);
                    }

                    var cmd = (BindableCommand)Enum.Parse(typeof(BindableCommand), el.GetAttribute("Command"), true);
                    var cfg = new CommandBindingConfig(kb, this.getBool(el.GetAttribute("ReplaceCurrent")), cmd);
                    this._commands_KeyBindingList.Add(cfg);
                }
            }
            commandsNode = null;

            var endOfLineNode = langNode.SelectSingleNode("EndOfLine") as XmlElement;
            if (endOfLineNode != null)
            {
                this._endOfLine_IsVisisble = this.getBool(endOfLineNode.GetAttribute("IsVisible"));

                try
                {
                    this._endOfLine_Mode = (EndOfLineMode)Enum.Parse(typeof(EndOfLineMode), endOfLineNode.GetAttribute("Mode"), true);
                }
                catch (ArgumentException) { }
            }
            endOfLineNode = null;

            var foldingNode = langNode.SelectSingleNode("Folding") as XmlElement;
            if (foldingNode != null)
            {
                string flags = foldingNode.GetAttribute("Flags").Trim();
                if (flags != string.Empty)
                {
                    FoldFlag? ff = flags.Split(' ').Aggregate<string, FoldFlag?>(null, 
                        (current, flag) => current | (FoldFlag)Enum.Parse(typeof (FoldFlag), flag.Trim(), true));

                    if (ff.HasValue)
                        this._folding_Flags = ff;
                }

                this._folding_IsEnabled = this.getBool(foldingNode.GetAttribute("IsEnabled"));
                try
                {
                    this._folding_MarkerScheme = (FoldMarkerScheme)Enum.Parse(typeof(FoldMarkerScheme), foldingNode.GetAttribute("MarkerScheme"), true);
                }
                catch (ArgumentException) { }

                this._folding_UseCompactFolding = this.getBool(foldingNode.GetAttribute("UseCompactFolding"));
            }
            foldingNode = null;

            var hotSpotNode = langNode.SelectSingleNode("Hotspot") as XmlElement;
            if (hotSpotNode != null)
            {
                this._hotspot_ActiveBackColor = this.getColor(hotSpotNode.GetAttribute("ActiveBackColor"));
                this._hotspot_ActiveForeColor = this.getColor(hotSpotNode.GetAttribute("ActiveForeColor"));
                this._hotspot_ActiveUnderline = this.getBool(hotSpotNode.GetAttribute("ActiveUnderline"));
                this._hotspot_SingleLine = this.getBool(hotSpotNode.GetAttribute("SingleLine"));
                this._hotspot_UseActiveBackColor = this.getBool(hotSpotNode.GetAttribute("UseActiveBackColor"));
                this._hotspot_UseActiveForeColor = this.getBool(hotSpotNode.GetAttribute("UseActiveForeColor"));
            }
            hotSpotNode = null;

            var indentationNode = langNode.SelectSingleNode("Indentation") as XmlElement;
            if (indentationNode != null)
            {
                this._indentation_BackspaceUnindents = this.getBool(indentationNode.GetAttribute("BackspaceUnindents"));
                this._indentation_IndentWidth = this.getInt(indentationNode.GetAttribute("IndentWidth"));
                this._indentation_ShowGuides = this.getBool(indentationNode.GetAttribute("ShowGuides"));
                this._indentation_TabIndents = this.getBool(indentationNode.GetAttribute("TabIndents"));
                this._indentation_TabWidth = this.getInt(indentationNode.GetAttribute("TabWidth"));
                this._indentation_UseTabs = this.getBool(indentationNode.GetAttribute("UseTabs"));

                try
                {
                    this._indentation_SmartIndentType = (SmartIndent)Enum.Parse(typeof(SmartIndent), indentationNode.GetAttribute("SmartIndentType"), true);
                }
                catch (ArgumentException) { }

            }
            indentationNode = null;

            var indicatorNode = langNode.SelectSingleNode("Indicators") as XmlElement;
            if (indicatorNode != null)
            {
                this._indicator_List.Inherit = this.getBool(indicatorNode.GetAttribute("Inherit"));
                foreach (XmlElement el in indicatorNode.SelectNodes("Indicator"))
                {
                    var ic = new IndicatorConfig
                    {
                        Number = int.Parse(el.GetAttribute("Number")),
                        Color = this.getColor(el.GetAttribute("Color")),
                        Inherit = this.getBool(el.GetAttribute("Inherit")),
                        IsDrawnUnder = this.getBool(el.GetAttribute("IsDrawnUnder"))
                    };
                    try
                    {
                        ic.Style = (IndicatorStyle)Enum.Parse(typeof(IndicatorStyle), el.GetAttribute("Style"), true);
                    }
                    catch (ArgumentException) { }

                    this._indicator_List.Add(ic);
                }
            }

            this._lexing_Properties = new LexerPropertiesConfig();
            this._lexing_Keywords = new KeyWordConfigList();
            var lexerNode = langNode.SelectSingleNode("Lexer") as XmlElement;
            if (lexerNode != null)
            {
                this._lexing_WhitespaceChars = this.getString(lexerNode.GetAttributeNode("WhitespaceChars"));
                this._lexing_WordChars = this.getString(lexerNode.GetAttributeNode("WordChars"));
                this._lexing_Language = this.getString(lexerNode.GetAttributeNode("LexerName"));
                this._lexing_LineCommentPrefix = this.getString(lexerNode.GetAttributeNode("LineCommentPrefix"));
                this._lexing_StreamCommentPrefix = this.getString(lexerNode.GetAttributeNode("StreamCommentPrefix"));
                this._lexing_StreamCommentSuffix = this.getString(lexerNode.GetAttributeNode("StreamCommentSuffix"));

                var propNode = lexerNode.SelectSingleNode("Properties") as XmlElement;
                if (propNode != null)
                {
                    this._lexing_Properties.Inherit = this.getBool(propNode.GetAttribute("Inherit"));

                    foreach (XmlElement el in propNode.SelectNodes("Property"))
                        this._lexing_Properties.Add(el.GetAttribute("Name"), el.GetAttribute("Value"));
                }

                foreach (XmlElement el in lexerNode.SelectNodes("Keywords"))
                    this._lexing_Keywords.Add(new KeyWordConfig(this.getInt(el.GetAttribute("List")).Value, el.InnerText.Trim(), this.getBool(el.GetAttribute("Inherit"))));

            }
            lexerNode = null;

            var lineWrapNode = langNode.SelectSingleNode("LineWrapping") as XmlElement;
            if (lineWrapNode != null)
            {
                try
                {
                    this._lineWrapping_Mode = (LineWrappingMode)Enum.Parse(typeof(LineWrappingMode), lineWrapNode.GetAttribute("Mode"), true);
                }
                catch (ArgumentException) { }

                this._lineWrapping_IndentSize = this.getInt(lineWrapNode.GetAttribute("IndentSize"));

                try
                {
                    this._lineWrapping_IndentMode = (LineWrappingIndentMode)Enum.Parse(typeof(LineWrappingIndentMode), lineWrapNode.GetAttribute("IndentMode"), true);
                }
                catch (ArgumentException) { }

                string flags = lineWrapNode.GetAttribute("VisualFlags").Trim();
                if (flags != string.Empty)
                {
                    LineWrappingVisualFlags? wvf = null;
                    foreach (string flag in flags.Split(' '))
                        wvf |= (LineWrappingVisualFlags)Enum.Parse(typeof(LineWrappingVisualFlags), flag.Trim(), true);

                    if (wvf.HasValue)
                        this._lineWrapping_VisualFlags = wvf;
                }

                try
                {
                    this._lineWrapping_VisualFlagsLocations = (LineWrappingVisualFlagsLocations)Enum.Parse(typeof(LineWrappingVisualFlagsLocations), lineWrapNode.GetAttribute("VisualFlagsLocations"), true);
                }
                catch (ArgumentException) { }
            }
            lineWrapNode = null;

            var longLinesNode = langNode.SelectSingleNode("LongLines") as XmlElement;
            if (longLinesNode != null)
            {
                this._longLines_EdgeColor = this.getColor(longLinesNode.GetAttribute("EdgeColor"));
                this._longLines_EdgeColumn = this.getInt(longLinesNode.GetAttribute("EdgeColumn"));
                try
                {
                    this._longLines_EdgeMode = (EdgeMode)Enum.Parse(typeof(EdgeMode), longLinesNode.GetAttribute("EdgeMode"), true);
                }
                catch (ArgumentException) { }
            }
            longLinesNode = null;

            this._margin_List = new MarginConfigList();
            var marginNode = langNode.SelectSingleNode("Margins") as XmlElement;
            if (marginNode != null)
            {
                this._margin_List.FoldMarginColor = this.getColor(marginNode.GetAttribute("FoldMarginColor"));
                this._margin_List.FoldMarginHighlightColor = this.getColor(marginNode.GetAttribute("FoldMarginHighlightColor"));
                this._margin_List.Left = this.getInt(marginNode.GetAttribute("Left"));
                this._margin_List.Right = this.getInt(marginNode.GetAttribute("Right"));
                this._margin_List.Inherit = this.getBool(marginNode.GetAttribute("Inherit"));

                foreach (XmlElement el in marginNode.SelectNodes("./Margin"))
                {
                    var mc = new MarginConfig
                    {
                        Number = int.Parse(el.GetAttribute("Number")),
                        Inherit = this.getBool(el.GetAttribute("Inherit")),
                        AutoToggleMarkerNumber = this.getInt(el.GetAttribute("AutoToggleMarkerNumber")),
                        IsClickable = this.getBool(el.GetAttribute("IsClickable")),
                        IsFoldMargin = this.getBool(el.GetAttribute("IsFoldMargin")),
                        IsMarkerMargin = this.getBool(el.GetAttribute("IsMarkerMargin"))
                    };
                    try
                    {
                        mc.Type = (MarginType)Enum.Parse(typeof(MarginType), el.GetAttribute("Type"), true);
                    }
                    catch (ArgumentException) { }

                    mc.Width = this.getInt(el.GetAttribute("Width"));

                    this._margin_List.Add(mc);
                }
            }
            marginNode = null;

            var markersNode = langNode.SelectSingleNode("Markers") as XmlElement;
            this._markers_List = new MarkersConfigList();
            if (markersNode != null)
            {
                this._markers_List.Inherit = this.getBool(markersNode.GetAttribute("Inherit"));

                foreach (XmlElement el in markersNode.SelectNodes("Marker"))
                {
                    var mc = new MarkersConfig
                    {
                        Alpha = this.getInt(el.GetAttribute("Alpha")),
                        BackColor = this.getColor(el.GetAttribute("BackColor")),
                        ForeColor = this.getColor(el.GetAttribute("ForeColor")),
                        Name = this.getString(el.GetAttributeNode("Name")),
                        Number = this.getInt(el.GetAttribute("Number")),
                        Inherit = this.getBool(el.GetAttribute("Inherit"))
                    };
                    try
                    {
                        mc.Symbol = (MarkerSymbol)Enum.Parse(typeof(MarkerSymbol), el.GetAttribute("Symbol"), true);
                    }
                    catch (ArgumentException) { }
                    this._markers_List.Add(mc);
                }
            }

            var scrollingNode = langNode.SelectSingleNode("Scrolling") as XmlElement;
            if (scrollingNode != null)
            {
                this._scrolling_EndAtLastLine = this.getBool(scrollingNode.GetAttribute("EndAtLastLine"));
                this._scrolling_HorizontalWidth = this.getInt(scrollingNode.GetAttribute("HorizontalWidth"));

                string flags = scrollingNode.GetAttribute("ScrollBars").Trim();
                if (flags != string.Empty)
                {
                    ScrollBars? sb = null;
                    foreach (string flag in flags.Split(' '))
                        sb |= (ScrollBars)Enum.Parse(typeof(ScrollBars), flag.Trim(), true);

                    if (sb.HasValue)
                        this._scrolling_ScrollBars = sb;
                }

                this._scrolling_XOffset = this.getInt(scrollingNode.GetAttribute("XOffset"));
            }
            scrollingNode = null;


            var selectionNode = langNode.SelectSingleNode("Selection") as XmlElement;
            if (selectionNode != null)
            {
                this._selection_BackColor = this.getColor(selectionNode.GetAttribute("BackColor"));
                this._selection_BackColorUnfocused = this.getColor(selectionNode.GetAttribute("BackColorUnfocused"));
                this._selection_ForeColor = this.getColor(selectionNode.GetAttribute("ForeColor"));
                this._selection_ForeColorUnfocused = this.getColor(selectionNode.GetAttribute("ForeColorUnfocused"));
                this._selection_Hidden = this.getBool(selectionNode.GetAttribute("Hidden"));
                this._selection_HideSelection = this.getBool(selectionNode.GetAttribute("HideSelection"));
                try
                {
                    this._selection_Mode = (SelectionMode)Enum.Parse(typeof(SelectionMode), selectionNode.GetAttribute("Mode"), true);
                }
                catch (ArgumentException) { }
            }
            selectionNode = null;

            this._snippetsConfigList = new SnippetsConfigList();
            var snippetsNode = langNode.SelectSingleNode("Snippets") as XmlElement;
            if (snippetsNode != null)
            {
                this._snippetsConfigList.ActiveSnippetColor = this.getColor(snippetsNode.GetAttribute("ActiveSnippetColor"));
                this._snippetsConfigList.ActiveSnippetIndicator = this.getInt(snippetsNode.GetAttribute("ActiveSnippetIndicator"));
                this._snippetsConfigList.InactiveSnippetColor = this.getColor(snippetsNode.GetAttribute("InactiveSnippetColor"));
                this._snippetsConfigList.InactiveSnippetIndicator = this.getInt(snippetsNode.GetAttribute("InactiveSnippetIndicator"));

                try
                {
                    this._snippetsConfigList.ActiveSnippetIndicatorStyle = (IndicatorStyle)Enum.Parse(typeof(IndicatorStyle), snippetsNode.GetAttribute("ActiveSnippetIndicatorStyle"), true);
                }
                catch (ArgumentException) { }

                try
                {
                    this._snippetsConfigList.InactiveSnippetIndicatorStyle = (IndicatorStyle)Enum.Parse(typeof(IndicatorStyle), snippetsNode.GetAttribute("InactiveSnippetIndicatorStyle"), true);
                }
                catch (ArgumentException) { }

                this._snippetsConfigList.DefaultDelimeter = this.getChar(snippetsNode.GetAttribute("DefaultDelimeter"));
                this._snippetsConfigList.IsEnabled = this.getBool(snippetsNode.GetAttribute("IsEnabled"));
                this._snippetsConfigList.IsOneKeySelectionEmbedEnabled = this.getBool(snippetsNode.GetAttribute("IsOneKeySelectionEmbedEnabled"));

                foreach (XmlElement el in snippetsNode.SelectNodes("Snippet"))
                {
                    var sc = new SnippetsConfig
                    {
                        Shortcut = el.GetAttribute("Shortcut"),
                        Code = el.InnerText,
                        Delimeter = this.getChar(el.GetAttribute("Delimeter")),
                        IsSurroundsWith = this.getBool(el.GetAttribute("IsSurroundsWith"))
                    };
                    this._snippetsConfigList.Add(sc);
                }
            }
            snippetsNode = null;

            this._styles = new StyleConfigList();
            var stylesNode = langNode.SelectSingleNode("Styles") as XmlElement;
            if (stylesNode != null)
            {
                this._styles.Bits = this.getInt(stylesNode.GetAttribute("Bits"));
                foreach (XmlElement el in stylesNode.SelectNodes("Style"))
                {
                    var sc = new StyleConfig
                    {
                        Name = el.GetAttribute("Name"),
                        Number = this.getInt(el.GetAttribute("Number")),
                        BackColor = this.getColor(el.GetAttribute("BackColor")),
                        Bold = this.getBool(el.GetAttribute("Bold"))
                    };
                    try
                    {
                        sc.Case = (StyleCase)Enum.Parse(typeof(StyleCase), el.GetAttribute("Case"), true);
                    }
                    catch (ArgumentException) { }

                    try
                    {
                        sc.CharacterSet = (CharacterSet)Enum.Parse(typeof(CharacterSet), el.GetAttribute("CharacterSet"), true);
                    }
                    catch (ArgumentException) { }

                    sc.FontName = this.getString(el.GetAttributeNode("FontName"));
                    sc.ForeColor = this.getColor(el.GetAttribute("ForeColor"));
                    sc.IsChangeable = this.getBool(el.GetAttribute("IsChangeable"));
                    sc.IsHotspot = this.getBool(el.GetAttribute("IsHotspot"));
                    sc.IsSelectionEolFilled = this.getBool(el.GetAttribute("IsSelectionEolFilled"));
                    sc.IsVisible = this.getBool(el.GetAttribute("IsVisible"));
                    sc.Italic = this.getBool(el.GetAttribute("Italic"));
                    sc.Size = this.getInt(el.GetAttribute("Size"));
                    sc.Underline = this.getBool(el.GetAttribute("Underline"));
                    sc.Inherit = this.getBool(el.GetAttribute("Inherit"));
                    
                    this._styles.Add(sc);
                }

                //	This is a nifty added on hack made specifically for HTML.
                //	Normally the style config elements are quite managable as there
                //	are typically less than 10 when you don't count common styles.
                //	
                //	However HTML uses 9 different Sub languages that combined make 
                //	use of all 128 styles (well there are some small gaps). In order
                //	to make this more managable I did added a SubLanguage element that
                //	basically just prepends the Language's name and "." to the Style 
                //	Name definition.
                //
                //	So for example if you had the following
                //	<Styles>
                //		<SubLanguage Name="ASP JavaScript">
                //			<Style Name="Keyword" Bold="True" />
                //		</SubLanguage>
                //	</Styles>
                //	That style's name will get interpreted as "ASP JavaScript.Keyword".
                //	which if you look at the html.txt in LexerStyleNames you'll see it
                //	maps to Style # 62

                //	Yeah I copied and pasted from above. I know. Feel free to refactor
                //	this and check it in since you're so high and mighty.
                foreach (XmlElement subLanguage in stylesNode.SelectNodes("SubLanguage"))
                {
                    string subLanguageName = subLanguage.GetAttribute("Name");
                    foreach (XmlElement el in subLanguage.SelectNodes("Style"))
                    {
                        var sc = new StyleConfig
                        {
                            Name = subLanguageName + "." + el.GetAttribute("Name"),
                            Number = this.getInt(el.GetAttribute("Number")),
                            BackColor = this.getColor(el.GetAttribute("BackColor")),
                            Bold = this.getBool(el.GetAttribute("Bold"))
                        };
                        try
                        {
                            sc.Case = (StyleCase)Enum.Parse(typeof(StyleCase), el.GetAttribute("Case"), true);
                        }
                        catch (ArgumentException) { }

                        try
                        {
                            sc.CharacterSet = (CharacterSet)Enum.Parse(typeof(CharacterSet), el.GetAttribute("CharacterSet"), true);
                        }
                        catch (ArgumentException) { }

                        sc.FontName = this.getString(el.GetAttributeNode("FontName"));
                        sc.ForeColor = this.getColor(el.GetAttribute("ForeColor"));
                        sc.IsChangeable = this.getBool(el.GetAttribute("IsChangeable"));
                        sc.IsHotspot = this.getBool(el.GetAttribute("IsHotspot"));
                        sc.IsSelectionEolFilled = this.getBool(el.GetAttribute("IsSelectionEolFilled"));
                        sc.IsVisible = this.getBool(el.GetAttribute("IsVisible"));
                        sc.Italic = this.getBool(el.GetAttribute("Italic"));
                        sc.Size = this.getInt(el.GetAttribute("Size"));
                        sc.Underline = this.getBool(el.GetAttribute("Underline"));
                        sc.Inherit = this.getBool(el.GetAttribute("Inherit"));

                        this._styles.Add(sc);
                    }
                }
            }
            stylesNode = null;

            var undoRedoNode = langNode.SelectSingleNode("UndoRedo") as XmlElement;
            if (undoRedoNode != null)
            {
                this._undoRedoIsUndoEnabled = this.getBool(undoRedoNode.GetAttribute("IsUndoEnabled"));
            }
            undoRedoNode = null;


            var whitespaceNode = langNode.SelectSingleNode("Whitespace") as XmlElement;
            if (whitespaceNode != null)
            {
                this._whitespace_BackColor = this.getColor(whitespaceNode.GetAttribute("BackColor"));
                this._whitespace_ForeColor = this.getColor(whitespaceNode.GetAttribute("ForeColor"));
                this._whitespace_Mode = (WhitespaceMode)Enum.Parse(typeof(WhitespaceMode), whitespaceNode.GetAttribute("Mode"), true);
            }
            whitespaceNode = null;

            configDocument = null;
        }


        public void Load(string fileName, bool useXmlReader)
        {
            if (useXmlReader)
            {
                var s = new XmlReaderSettings
                {
                    IgnoreComments = true,
                    IgnoreWhitespace = true
                };

                Load(XmlReader.Create(fileName, s));
            }
            else
            {
                var doc = new XmlDocument
                {
                    PreserveWhitespace = true
                };
                doc.Load(fileName);
                Load(doc);
            }
        }


        public void Load(Stream inStream, bool useXmlReader)
        {
            if (useXmlReader)
            {
                var s = new XmlReaderSettings
                {
                    IgnoreComments = true,
                    IgnoreWhitespace = true
                };
                Load(XmlReader.Create(inStream, s));
            }
            else
            {
                var doc = new XmlDocument
                {
                    PreserveWhitespace = true
                };
                doc.Load(inStream);
                Load(doc);
            }
        }


        private void ReadAutoComplete(XmlReader reader)
        {
            if (reader.HasAttributes)
            {
                while (reader.MoveToNextAttribute())
                {
                    string attrName = reader.Name.ToLower();

                    switch (attrName)
                    {
                        case "autohide":
                            this._autoComplete_AutoHide = this.getBool(reader.Value);
                            break;
                        case "automaticlengthentered":
                            this._autoComplete_AutomaticLengthEntered = this.getBool(reader.Value);
                            break;
                        case "cancelatstart":
                            this._autoComplete_cancelAtStart = this.getBool(reader.Value);
                            break;
                        case "droprestofword":
                            this._autoComplete_DropRestOfWord = this.getBool(reader.Value);
                            break;
                        case "fillupcharacters":
                            this._autoComplete_fillUpCharacters = reader.Value;
                            break;
                        case "imageseperator":
                            this._autoComplete_ImageSeperator = this.getChar(reader.Value);
                            break;
                        case "iscasesensitive":
                            this._autoComplete_IsCaseSensitive= this.getBool(reader.Value);
                            break;
                        case "listseperator":
                            this._autoComplete_ListSeperator = this.getChar(reader.Value);
                            break;
                        case "maxheight":
                            this._autoComplete_MaxHeight = this.getInt(reader.Value);
                            break;
                        case "maxwidth":
                            this._autoComplete_MaxWidth = this.getInt(reader.Value);
                            break;
                        case "singlelineaccept":
                            this._autoComplete_singleLineAccept = this.getBool(reader.Value);
                            break;
                        case "stopcharacters":
                            this._autoComplete_StopCharacters = reader.Value;
                            break;
                    }
                }

                reader.MoveToElement();
            }

            if (!reader.IsEmptyElement)
            {
                while (!(reader.NodeType == XmlNodeType.EndElement && reader.Name.Equals("autocomplete", StringComparison.OrdinalIgnoreCase)))
                {
                    reader.Read();
                    if (reader.NodeType == XmlNodeType.Element && reader.Name.Equals("list", StringComparison.OrdinalIgnoreCase))
                    {
                        if (reader.HasAttributes)
                        {
                            while (reader.MoveToNextAttribute())
                                if (reader.Name.Equals("inherit", StringComparison.OrdinalIgnoreCase))
                                    this._autoComplete_ListInherit = this.getBool(reader.Value);
                            
                            reader.MoveToElement();
                        }
                        this._autoComplete_List = new Regex("\\s+").Replace(reader.ReadString(), " ").Trim();
                    }
                }
            }
            reader.Read();
        }


        private void ReadCallTip(XmlReader reader)
        {
            if (reader.HasAttributes)
            {
                while (reader.MoveToNextAttribute())
                {
                    string attrName = reader.Name.ToLower();
                    switch (attrName)
                    {
                        case "backcolor":
                            this._callTip_BackColor = this.getColor(reader.Value);
                            break;
                        case "forecolor":
                            this._callTip_ForeColor = this.getColor(reader.Value);
                            break;
                        case "highlighttextcolor":
                            this._callTip_HighlightTextColor = this.getColor(reader.Value);
                            break;
                    }
                }

                reader.MoveToElement();
            }

            reader.Skip();
        }


        private void ReadCaret(XmlReader reader)
        {
            if (reader.HasAttributes)
            {
                while (reader.MoveToNextAttribute())
                {
                    string attrName = reader.Name.ToLower();
                    switch (attrName)
                    {
                        case "blinkrate":
                            //	This guy is a bit of an oddball becuase null means "I don't Care"
                            //	and we need some way of using the OS value.
                            string blinkRate = reader.Value;
                            this._caret_BlinkRate = blinkRate.ToLower() == "system" ? 
                                SystemInformation.CaretBlinkTime : this.getInt(blinkRate);
                            break;
                        case "color":
                            this._caret_Color = this.getColor(reader.Value);
                            break;
                        case "currentlinebackgroundalpha":
                            this._caret_CurrentLineBackgroundAlpha = this.getInt(reader.Value);
                            break;
                        case "currentlinebackgroundcolor":
                            this._caret_CurrentLineBackgroundColor = this.getColor(reader.Value);
                            break;
                        case "highlightcurrentline":
                            this._caret_HighlightCurrentLine = this.getBool(reader.Value);
                            break;
                        case "issticky":
                            this._caret_IsSticky = this.getBool(reader.Value);
                            break;
                        case "style":
                            this._caret_Style = (CaretStyle)Enum.Parse(typeof(CaretStyle), reader.Value, true);
                            break;
                        case "width":
                            this._caret_Width = this.getInt(reader.Value);
                            break;
                    }
                }
                reader.MoveToElement();
            }
            reader.Skip();
        }


        private void ReadClipboard(XmlReader reader)
        {
            if (reader.HasAttributes)
            {
                while (reader.MoveToNextAttribute())
                {
                    string attrName = reader.Name.ToLower();
                    switch (attrName)
                    {
                        case "convertlinebreaksonpaste":
                            this._clipboard_ConvertLineBreaksOnPaste = this.getBool(reader.Value);
                            break;
                    }
                }
                reader.MoveToElement();
            }
            reader.Skip();
        }


        private void ReadCommands(XmlReader reader)
        {
            if (reader.HasAttributes)
            {
                while (reader.MoveToNextAttribute())
                {
                    string attrName = reader.Name.ToLower();
                    switch (attrName)
                    {
                        case "Inherit":
                            this._commands_KeyBindingList.Inherit = this.getBool(reader.Value);
                            break;
                        case "AllowDuplicateBindings":
                            this._commands_KeyBindingList.AllowDuplicateBindings = this.getBool(reader.Value);
                            break;
                    }
                }

                reader.MoveToElement();
            }

            if (!reader.IsEmptyElement)
            {
                while (!(reader.NodeType == XmlNodeType.EndElement && reader.Name.Equals("commands", StringComparison.OrdinalIgnoreCase)))
                {
                    reader.Read();
                    if (reader.NodeType == XmlNodeType.Element && reader.Name.Equals("binding", StringComparison.OrdinalIgnoreCase))
                    {
                        if (reader.HasAttributes)
                        {
                            var kb = new KeyBinding();
                            var cmd = new BindableCommand();
                            bool? replaceCurrent = null;

                            while (reader.MoveToNextAttribute())
                            {
                                string attrName = reader.Name.ToLower();
                                switch (attrName)
                                {
                                    case "key":
                                        kb.KeyCode = Utilities.GetKeys(reader.Value);
                                        break;
                                    case "modifier":
                                        if (reader.Value != string.Empty)
                                        {
                                            foreach (string modifier in reader.Value.Split(' '))
                                                kb.Modifiers |= (Keys)Enum.Parse(typeof(Keys), modifier.Trim(), true);
                                        }
                                        break;
                                    case "command":
                                        cmd = (BindableCommand)Enum.Parse(typeof(BindableCommand), reader.Value, true);
                                        break;
                                    case "replacecurrent":
                                        replaceCurrent = this.getBool(reader.Value);
                                        break;
                                }
                            }

                            this._commands_KeyBindingList.Add(new CommandBindingConfig(kb, replaceCurrent, cmd));
                        }

                        reader.MoveToElement();
                    }
                }
            }
            reader.Read();
        }


        private void ReadEndOfLine(XmlReader reader)
        {
            if (reader.HasAttributes)
            {
                while (reader.MoveToNextAttribute())
                {
                    string attrName = reader.Name.ToLower();
                    switch (attrName)
                    {
                        case "isvisible":
                            this._endOfLine_IsVisisble = this.getBool(reader.Value);
                            break;
                        case "mode":
                            this._endOfLine_Mode = (EndOfLineMode)Enum.Parse(typeof(EndOfLineMode), reader.Value, true);
                            break;
                    }
                }

                reader.MoveToElement();
            }

            reader.Skip();
        }


        private void ReadFolding(XmlReader reader)
        {
            if (reader.HasAttributes)
            {
                while (reader.MoveToNextAttribute())
                {
                    string attrName = reader.Name.ToLower();
                    switch (attrName)
                    {
                        case "flags":
                            string flags = reader.Value.Trim();
                            if (flags != string.Empty)
                            {
                                FoldFlag? ff = null;
                                foreach (string flag in flags.Split(' '))
                                    ff |= (FoldFlag)Enum.Parse(typeof(FoldFlag), flag.Trim(), true);

                                if (ff.HasValue)
                                    this._folding_Flags = ff;
                            }
                            break;
                        case "IsEnabled":
                            this._folding_MarkerScheme = (FoldMarkerScheme)Enum.Parse(typeof(FoldMarkerScheme), reader.Value, true);
                            break;
                        case "usecompactfolding":
                            this._folding_UseCompactFolding = this.getBool(reader.Value);
                            break;
                    }
                }

                reader.MoveToElement();
            }

            reader.Skip();
        }


        private void ReadHotspot(XmlReader reader)
        {
            if (reader.HasAttributes)
            {
                while (reader.MoveToNextAttribute())
                {
                    string attrName = reader.Name.ToLower();
                    switch (attrName)
                    {
                        case "activebackcolor":
                            this._hotspot_ActiveBackColor = this.getColor(reader.Value);
                            break;
                        case "activeforecolor":
                            this._hotspot_ActiveForeColor = this.getColor(reader.Value);
                            break;
                        case "activeunderline":
                            this._hotspot_ActiveUnderline = this.getBool(reader.Value);
                            break;
                        case "singleline":
                            this._hotspot_SingleLine = this.getBool(reader.Value);
                            break;
                        case "useactivebackcolor":
                            this._hotspot_UseActiveBackColor = this.getBool(reader.Value);
                            break;
                        case "useactiveforecolor":
                            this._hotspot_UseActiveForeColor = this.getBool(reader.Value);
                            break;
                    }
                }

                reader.MoveToElement();
            }

            reader.Skip();
        }


        private void ReadIndentation(XmlReader reader)
        {
            if (reader.HasAttributes)
            {
                while (reader.MoveToNextAttribute())
                {
                    string attrName = reader.Name.ToLower();
                    switch (attrName)
                    {
                        case "backspaceunindents":
                            this._indentation_BackspaceUnindents = this.getBool(reader.Value);
                            break;
                        case "indentwidth":
                            this._indentation_IndentWidth = this.getInt(reader.Value);
                            break;
                        case "showguides":
                            this._indentation_ShowGuides = this.getBool(reader.Value);
                            break;
                        case "tabindents":
                            this._indentation_TabIndents = this.getBool(reader.Value);
                            break;
                        case "tabwidth":
                            this._indentation_TabWidth = this.getInt(reader.Value);
                            break;
                        case "usetabs":
                            this._indentation_UseTabs = this.getBool(reader.Value);
                            break;
                        case "smartindenttype":
                            this._indentation_SmartIndentType = (SmartIndent)Enum.Parse(typeof(SmartIndent), reader.Value, true);
                            break;
                    }
                }

                reader.MoveToElement();
            }

            reader.Skip();
        }


        private void ReadIndicators(XmlReader reader)
        {
            if (reader.HasAttributes)
            {
                while (reader.MoveToNextAttribute())
                {
                    string attrName = reader.Name.ToLower();
                    switch (attrName)
                    {
                        case "inherit":
                            this._indicator_List.Inherit = this.getBool(reader.Value);
                            break;
                    }
                }
                reader.MoveToElement();
            }

            if (!reader.IsEmptyElement)
            {
                while (!(reader.NodeType == XmlNodeType.EndElement && reader.Name.Equals("indicators", StringComparison.OrdinalIgnoreCase)))
                {
                    reader.Read();
                    if (reader.NodeType == XmlNodeType.Element && reader.Name.Equals("indicator", StringComparison.OrdinalIgnoreCase))
                    {
                        if (reader.HasAttributes)
                        {
                            var ic = new IndicatorConfig();
                            while (reader.MoveToNextAttribute())
                            {
                                string attrName = reader.Name.ToLower();
                                switch (attrName)
                                {
                                    case "number":
                                        ic.Number = int.Parse(reader.Value);
                                        break;
                                    case "color":
                                        ic.Color = this.getColor(reader.Value);
                                        break;
                                    case "inherit":
                                        ic.Inherit = this.getBool(reader.Value);
                                        break;
                                    case "isdrawnunder":
                                        ic.IsDrawnUnder = this.getBool(reader.Value);
                                        break;
                                    case "style":
                                        ic.Style = (IndicatorStyle)Enum.Parse(typeof(IndicatorStyle), reader.Value, true);
                                        break;
                                }
                            }
                            this._indicator_List.Add(ic);
                            reader.MoveToElement();
                        }
                    }
                }
            }
            reader.Read();
        }


        private void ReadLanguage(XmlReader reader)
        {
            this._commands_KeyBindingList = new CommandBindingConfigList();
            this._lexing_Properties = new LexerPropertiesConfig();
            this._lexing_Keywords = new KeyWordConfigList();
            this._margin_List = new MarginConfigList();
            this._markers_List = new MarkersConfigList();
            this._snippetsConfigList = new SnippetsConfigList();
            this._styles = new StyleConfigList();

            reader.Read();
            while (reader.NodeType == XmlNodeType.Element)
            {
                string elName = reader.Name.ToLower();
                switch (elName)
                {
                    case "autocomplete":
                        this.ReadAutoComplete(reader);
                        break;
                    case "calltip":
                        this.ReadCallTip(reader);
                        break;
                    case "caret":
                        this.ReadCaret(reader);
                        break;
                    case "clipboard":
                        this.ReadClipboard(reader);
                        break;
                    case "commands":
                        this.ReadCommands(reader);
                        break;
                    case "endofline":
                        this.ReadEndOfLine(reader);
                        break;
                    case "folding":
                        this.ReadFolding(reader);
                        break;
                    case "hotspot":
                        this.ReadHotspot(reader);
                        break;
                    case "indentation":
                        this.ReadIndentation(reader);
                        break;
                    case "indicators":
                        this.ReadIndicators(reader);
                        break;
                    case "lexer":
                        this.ReadLexer(reader);
                        break;
                    case "linewrapping":
                        this.ReadLineWrapping(reader);
                        break;
                    case "longlines":
                        this.ReadLongLines(reader);
                        break;
                    case "margins":
                        this.ReadMargins(reader);
                        break;
                    case "markers":
                        this.ReadMarkers(reader);
                        break;
                    case "scrolling":
                        this.ReadScrolling(reader);
                        break;
                    case "selection":
                        this.ReadSelection(reader);
                        break;
                    case "snippets":
                        this.ReadSnippets(reader);
                        break;
                    case "styles":
                        this.ReadStyles(reader);
                        break;
                    case "undoredo":
                        this.ReadUndoRedo(reader);
                        break;
                    case "whitespace":
                        this.ReadWhitespace(reader);
                        break;
                    default:
                        reader.Skip();
                        break;
                }
                
            }
        }


        private void ReadLexer(XmlReader reader)
        {
            if (reader.HasAttributes)
            {
                while (reader.MoveToNextAttribute())
                {
                    string attrName = reader.Name.ToLower();
                    switch (attrName)
                    {
                        case "whitespacechars":
                            this._lexing_WhitespaceChars = reader.Value;
                            break;
                        case "wordchars":
                            this._lexing_WordChars = reader.Value;
                            break;
                        case "lexername":
                            this._lexing_Language = reader.Value;
                            break;
                        case "linecommentprefix":
                            this._lexing_LineCommentPrefix = reader.Value;
                            break;
                        case "streamcommentprefix":
                            this._lexing_StreamCommentPrefix = reader.Value;
                            break;
                        case "streamcommentsuffix":
                            this._lexing_StreamCommentSuffix = reader.Value;
                            break;
                    }
                }
                reader.MoveToElement();
            }

            if (!reader.IsEmptyElement)
            {
                reader.Read();
                while (!(reader.NodeType == XmlNodeType.EndElement && reader.Name.Equals("lexer", StringComparison.OrdinalIgnoreCase)))
                {
                    if (reader.NodeType == XmlNodeType.Element)
                    {
                        if (reader.Name.Equals("properties", StringComparison.OrdinalIgnoreCase))
                            this.ReadLexerProperties(reader);
                        else if (reader.Name.Equals("keywords", StringComparison.OrdinalIgnoreCase))
                            this.ReadLexerKeywords(reader);
                    }
                }
            }
            reader.Read();
        }


        private void ReadLexerKeywords(XmlReader reader)
        {
            bool? inherit = null;
            int? list = null;
            string keywords = null;

            if (reader.HasAttributes)
            {
                while (reader.MoveToNextAttribute())
                {
                    string attrName = reader.Name.ToLower();
                    switch (attrName)
                    {
                        case "inherit":
                            inherit = this.getBool(reader.Value);
                            break;
                        case "list":
                            list = this.getInt(reader.Value);
                            break;
                    }
                }

                reader.MoveToElement();
            }
            
            if (!reader.IsEmptyElement)
                keywords = reader.ReadString().Trim();

            this._lexing_Keywords.Add(new KeyWordConfig(list.Value, keywords, inherit));

            reader.Read();
        }


        private void ReadLexerProperties(XmlReader reader)
        {
            if (reader.HasAttributes)
            {
                while (reader.MoveToNextAttribute())
                    if (reader.Name.ToLower() == "inherit")
                        this._lexing_Properties.Inherit = this.getBool(reader.Value);

                reader.MoveToElement();
            }

            if (!reader.IsEmptyElement)
            {
                while (!(reader.NodeType == XmlNodeType.EndElement && reader.Name.Equals("properties", StringComparison.OrdinalIgnoreCase)))
                {
                    reader.Read();
                    if (reader.NodeType == XmlNodeType.Element && reader.Name.Equals("property", StringComparison.OrdinalIgnoreCase))
                    {
                        if (reader.HasAttributes)
                        {
                            string name = string.Empty;
                            string value = string.Empty;
                            while (reader.MoveToNextAttribute())
                            {
                                string attrName = reader.Name.ToLower();
                                switch (attrName)
                                {
                                    case "name":
                                        name = reader.Value;
                                        break;
                                    case "value":
                                        value = reader.Value;
                                        break;
                                }
                            }
                            this._lexing_Properties.Add(name, value);
                            reader.MoveToElement();
                        }
                    }
                }
            }

            reader.Read();
        }


        private void ReadLineWrapping(XmlReader reader)
        {
            if (reader.HasAttributes)
            {
                while (reader.MoveToNextAttribute())
                {
                    string attrName = reader.Name.ToLower();
                    switch (attrName)
                    {
                        case "mode":
                            this._lineWrapping_Mode = (LineWrappingMode)Enum.Parse(typeof(LineWrappingMode), reader.Value, true);
                            break;
                        case "indentsize":
                            this._lineWrapping_IndentSize = this.getInt(reader.Value);
                            break;
                        case "indentmode":
                            this._lineWrapping_IndentMode = (LineWrappingIndentMode)Enum.Parse(typeof(LineWrappingIndentMode), reader.Value, true);
                            break;
                        case "visualflags":
                            string flags = reader.Value.Trim();
                            if (flags != string.Empty)
                            {
                                LineWrappingVisualFlags? wvf = null;
                                foreach (string flag in flags.Split(' '))
                                    wvf |= (LineWrappingVisualFlags)Enum.Parse(typeof(LineWrappingVisualFlags), flag.Trim(), true);

                                if (wvf.HasValue)
                                    this._lineWrapping_VisualFlags = wvf;
                            }
                            break;
                        case "visualflagslocations":
                            this._lineWrapping_VisualFlagsLocations = (LineWrappingVisualFlagsLocations)Enum.Parse(typeof(LineWrappingVisualFlagsLocations), reader.Value, true);
                            break;
                    }
                }
                reader.MoveToElement();
            }

            reader.Skip();
        }


        private void ReadLongLines(XmlReader reader)
        {
            if (reader.HasAttributes)
            {
                while (reader.MoveToNextAttribute())
                {
                    string attrName = reader.Name.ToLower();
                    switch (attrName)
                    {
                        case "edgecolor":
                            this._longLines_EdgeColor = this.getColor(reader.Value);
                            break;
                        case "edgecolumn":
                            this._longLines_EdgeColumn = this.getInt(reader.Value);
                            break;
                        case "edgemode":
                            this._longLines_EdgeMode = (EdgeMode)Enum.Parse(typeof(EdgeMode), reader.Value, true);
                            break;
                    }
                }
                reader.MoveToElement();
            }
            reader.Skip();
        }


        private void ReadMargins(XmlReader reader)
        {
            if (reader.HasAttributes)
            {
                while (reader.MoveToNextAttribute())
                {
                    string attrName = reader.Name.ToLower();
                    switch (attrName)
                    {
                        case "foldmargincolor":
                            this._margin_List.FoldMarginColor = this.getColor(reader.Value);
                            break;
                        case "foldmarginhighlightcolor":
                            this._margin_List.FoldMarginHighlightColor = this.getColor(reader.Value);
                            break;
                        case "left":
                            this._margin_List.Left = this.getInt(reader.Value);
                            break;
                        case "right":
                            this._margin_List.Right = this.getInt(reader.Value);
                            break;
                        case "inherit":
                            this._margin_List.Inherit = this.getBool(reader.Value);
                            break;
                    }
                }
                reader.MoveToElement();
            }
            
            
            if (!reader.IsEmptyElement)
            {
                while (!(reader.NodeType == XmlNodeType.EndElement && reader.Name.Equals("margins", StringComparison.OrdinalIgnoreCase)))
                {
                    reader.Read();
                    if (reader.NodeType == XmlNodeType.Element && reader.Name.Equals("margin", StringComparison.OrdinalIgnoreCase))
                    {
                        if (reader.HasAttributes)
                        {
                            var mc = new MarginConfig();
                            while (reader.MoveToNextAttribute())
                            {
                                string attrName = reader.Name.ToLower();
                                switch (attrName)
                                {
                                    case "number":
                                        mc.Number = int.Parse(reader.Value);
                                        break;
                                    case "inherit":
                                        mc.Inherit = this.getBool(reader.Value);
                                        break;
                                    case "autotogglemarkernumber":
                                        mc.AutoToggleMarkerNumber = this.getInt(reader.Value);
                                        break;
                                    case "isclickable":
                                        mc.IsClickable = this.getBool(reader.Value);
                                        break;
                                    case "isfoldmargin":
                                        mc.IsFoldMargin = this.getBool(reader.Value);
                                        break;
                                    case "ismarkermargin":
                                        mc.IsMarkerMargin = this.getBool(reader.Value);
                                        break;
                                    case "type":
                                        mc.Type = (MarginType)Enum.Parse(typeof(MarginType), reader.Value, true);
                                        break;
                                    case "width":
                                        mc.Width = this.getInt(reader.Value);
                                        break;
                                }
                            }
                            this._margin_List.Add(mc);
                            reader.MoveToElement();
                        }
                    }
                }
            }

            reader.Read();
        }


        private void ReadMarkers(XmlReader reader)
        {
            if (reader.HasAttributes)
            {
                while (reader.MoveToNextAttribute())
                    if(reader.Name.ToLower() == "inherit")
                        this._markers_List.Inherit = this.getBool(reader.Value);

                reader.MoveToElement();
            }

            if (!reader.IsEmptyElement)
            {
                while (!(reader.NodeType == XmlNodeType.EndElement && reader.Name.Equals("markers", StringComparison.OrdinalIgnoreCase)))
                {
                    reader.Read();
                    if (reader.NodeType == XmlNodeType.Element && reader.Name.Equals("marker", StringComparison.OrdinalIgnoreCase))
                    {
                        if (reader.HasAttributes)
                        {
                            var mc = new MarkersConfig();
                            while (reader.MoveToNextAttribute())
                            {
                                string attrName = reader.Name.ToLower();
                                switch (attrName)
                                {
                                    case "alpha":
                                        mc.Alpha = this.getInt(reader.Value);
                                        break;
                                    case "backcolor":
                                        mc.BackColor = this.getColor(reader.Value);
                                        break;
                                    case "forecolor":
                                        mc.ForeColor = this.getColor(reader.Value);
                                        break;
                                    case "name":
                                        mc.Name = reader.Value;
                                        break;
                                    case "number":
                                        mc.Number = this.getInt(reader.Value);
                                        break;
                                    case "inherit":
                                        mc.Inherit = this.getBool(reader.Value);
                                        break;
                                    case "symbol":
                                        mc.Symbol = (MarkerSymbol)Enum.Parse(typeof(MarkerSymbol), reader.Value, true);
                                        break;
                                }
                            }
                            
                            reader.MoveToElement();
                            this._markers_List.Add(mc);
                        }
                    }
                }
            }
            reader.Read();
        }


        private void ReadScrolling(XmlReader reader)
        {
            if (reader.HasAttributes)
            {
                while (reader.MoveToNextAttribute())
                {
                    string attrName = reader.Name.ToLower();
                    switch (attrName)
                    {
                        case "endatlastline":
                            this._scrolling_EndAtLastLine = this.getBool(reader.Value);
                            break;
                        case "horizontalwidth":
                            this._scrolling_HorizontalWidth = this.getInt(reader.Value);
                            break;
                        case "scrollbars":
                            string flags = reader.Value.Trim();
                            if (flags != string.Empty)
                            {
                                ScrollBars? sb = null;
                                foreach (string flag in flags.Split(' '))
                                    sb |= (ScrollBars)Enum.Parse(typeof(ScrollBars), flag.Trim(), true);

                                if (sb.HasValue)
                                    this._scrolling_ScrollBars = sb;
                            }
                            break;
                        case "xoffset":
                            this._scrolling_XOffset = this.getInt(reader.Value);
                            break;
                    }
                }
                reader.MoveToElement();
            }

            reader.Skip();
        }


        private void ReadSelection(XmlReader reader)
        {
            if (reader.HasAttributes)
            {
                while (reader.MoveToNextAttribute())
                {
                    string attrName = reader.Name.ToLower();
                    switch (attrName)
                    {
                        case "backcolor":
                            this._selection_BackColor = this.getColor(reader.Value);
                            break;
                        case "backcolorunfocused":
                            this._selection_BackColorUnfocused = this.getColor(reader.Value);
                            break;
                        case "forecolor":
                            this._selection_ForeColor = this.getColor(reader.Value);
                            break;
                        case "forecolorunfocused":
                            this._selection_ForeColorUnfocused = this.getColor(reader.Value);
                            break;
                        case "hidden":
                            this._selection_Hidden = this.getBool(reader.Value);
                            break;
                        case "hideselection":
                            this._selection_HideSelection = this.getBool(reader.Value);
                            break;
                        case "mode":
                            this._selection_Mode = (SelectionMode)Enum.Parse(typeof(SelectionMode), reader.Value, true);
                            break;
                    }
                }
                reader.MoveToElement();
            }

            reader.Skip();
        }


        private void ReadSnippets(XmlReader reader)
        {
            if (reader.HasAttributes)
            {
                while (reader.MoveToNextAttribute())
                {
                    string attrName = reader.Name.ToLower();
                    switch (attrName)
                    {
                        case "activesnippetcolor":
                            this._snippetsConfigList.ActiveSnippetColor = this.getColor(reader.Value);
                            break;
                        case "activesnippetindicator":
                            this._snippetsConfigList.ActiveSnippetIndicator = this.getInt(reader.Value);
                            break;
                        case "inactivesnippetcolor":
                            this._snippetsConfigList.InactiveSnippetColor = this.getColor(reader.Value);
                            break;
                        case "inactivesnippetindicator":
                            this._snippetsConfigList.InactiveSnippetIndicator = this.getInt(reader.Value);
                            break;
                        case "activesnippetindicatorstyle":
                            this._snippetsConfigList.ActiveSnippetIndicatorStyle = (IndicatorStyle)Enum.Parse(typeof(IndicatorStyle), reader.Value, true);
                            break;
                        case "inactivesnippetindicatorstyle":
                            this._snippetsConfigList.InactiveSnippetIndicatorStyle = (IndicatorStyle)Enum.Parse(typeof(IndicatorStyle), reader.Value, true);
                            break;
                        case "defaultdelimeter":
                            this._snippetsConfigList.DefaultDelimeter = this.getChar(reader.Value);
                            break;
                        case "isenabled":
                            this._snippetsConfigList.IsEnabled = this.getBool(reader.Value);
                            break;
                        case "isonekeyselectionembedenabled":
                            this._snippetsConfigList.IsOneKeySelectionEmbedEnabled = this.getBool(reader.Value);
                            break;
                    }
                }

                reader.MoveToElement();
            }

            if (!reader.IsEmptyElement)
            {
                while (!(reader.NodeType == XmlNodeType.EndElement && reader.Name.Equals("snippets", StringComparison.OrdinalIgnoreCase)))
                {
                    reader.Read();
                    if (reader.NodeType == XmlNodeType.Element && reader.Name.Equals("snippet", StringComparison.OrdinalIgnoreCase))
                    {
                        if (reader.HasAttributes)
                        {
                            var sc = new SnippetsConfig();
                            if (reader.HasAttributes)
                            {
                                while (reader.MoveToNextAttribute())
                                {
                                    string attrName = reader.Name.ToLower();
                                    switch (attrName)
                                    {

                                        case "shortcut":
                                            sc.Shortcut = reader.Value;
                                            break;
                                        case "delimeter":
                                            sc.Delimeter = this.getChar(reader.Value);
                                            break;
                                        case "issurroundswith":
                                            sc.IsSurroundsWith = this.getBool(reader.Value);
                                            break;
                                    }
                                }
                            }
                            reader.MoveToElement();
                            sc.Code = reader.ReadString();
                            this._snippetsConfigList.Add(sc);
                        }
                    }
                }
            }

            reader.Read();
        }


        private void ReadStyles(XmlReader reader)
        {
            if (reader.HasAttributes)
            {
                while (reader.MoveToNextAttribute())
                    if (reader.Name.ToLower() == "bits")
                        this._undoRedoIsUndoEnabled = this.getBool(reader.Value);

                reader.MoveToElement();
            }

            if (!reader.IsEmptyElement)
            {
                while (!(reader.NodeType == XmlNodeType.EndElement && reader.Name.Equals("styles", StringComparison.OrdinalIgnoreCase)))
                {
                    reader.Read();
                    if (reader.NodeType == XmlNodeType.Element && reader.Name.Equals("style", StringComparison.OrdinalIgnoreCase))
                    {
                        this._styles.Add(this.getStyleConfigFromElement(reader));
                    }
                    else if (reader.NodeType == XmlNodeType.Element && reader.Name.Equals("sublanguage", StringComparison.OrdinalIgnoreCase))
                    {
                        this.ReadSubLanguage(reader);
                    }
                }
            }

            reader.Read();
        }


        private void ReadSubLanguage(XmlReader reader)
        {
            //	This is a nifty added on hack made specifically for HTML.
            //	Normally the style config elements are quite managable as there
            //	are typically less than 10 when you don't count common styles.
            //	
            //	However HTML uses 9 different Sub languages that combined make 
            //	use of all 128 styles (well there are some small gaps). In order
            //	to make this more managable I did added a SubLanguage element that
            //	basically just prepends the Language's name and "." to the Style 
            //	Name definition.
            //
            //	So for example if you had the following
            //	<Styles>
            //		<SubLanguage Name="ASP JavaScript">
            //			<Style Name="Keyword" Bold="True" />
            //		</SubLanguage>
            //	</Styles>
            //	That style's name will get interpreted as "ASP JavaScript.Keyword".
            //	which if you look at the html.txt in LexerStyleNames you'll see it
            //	maps to Style # 62
            string subLanguageName = string.Empty;
            if (reader.HasAttributes)
            {
                while (reader.MoveToNextAttribute())
                    if (reader.Name.ToLower() == "name")
                        subLanguageName = reader.Value;

                reader.MoveToElement();
            }

            if (!reader.IsEmptyElement)
            {
                while (!(reader.NodeType == XmlNodeType.EndElement && reader.Name.Equals("sublanguage", StringComparison.OrdinalIgnoreCase)))
                {
                    reader.Read();
                    if (reader.NodeType == XmlNodeType.Element && reader.Name.Equals("style", StringComparison.OrdinalIgnoreCase))
                    {
                        StyleConfig sc = this.getStyleConfigFromElement(reader);
                        sc.Name = subLanguageName + "." + sc.Name;
                        this._styles.Add(sc);
                    }
                }
            }

            reader.Read();
        }


        private void ReadUndoRedo(XmlReader reader)
        {
            if (reader.HasAttributes)
            {
                while (reader.MoveToNextAttribute())
                    if (reader.Name.ToLower() == "isundoenabled")
                        this._undoRedoIsUndoEnabled = this.getBool(reader.Value);

                reader.MoveToElement();
            }
            reader.Skip();
        }


        private void ReadWhitespace(XmlReader reader)
        {
            if (reader.HasAttributes)
            {
                while (reader.MoveToNextAttribute())
                {
                    string attrName = reader.Name.ToLower();
                    switch (attrName)
                    {
                        case "backcolor":
                            this._whitespace_BackColor = this.getColor(reader.Value);
                            break;
                        case "forecolor":
                            this._whitespace_ForeColor = this.getColor(reader.Value);
                            break;
                        case "mode":
                            this._whitespace_Mode = (WhitespaceMode)Enum.Parse(typeof(WhitespaceMode), reader.Value, true);
                            break;
                    }
                }
            }
            reader.Skip();
        }

        #endregion Methods


        #region Properties

        public bool? AutoComplete_AutoHide
        {
            get
            {
                return this._autoComplete_AutoHide;
            }
            set
            {
                this._autoComplete_AutoHide = value;
            }
        }


        public bool? AutoComplete_AutomaticLengthEntered
        {
            get
            {
                return this._autoComplete_AutomaticLengthEntered;
            }
            set
            {
                this._autoComplete_AutomaticLengthEntered = value;
            }
        }


        public bool? AutoComplete_CancelAtStart
        {
            get
            {
                return this._autoComplete_cancelAtStart;
            }
            set
            {
                this._autoComplete_cancelAtStart = value;
            }
        }


        public bool? AutoComplete_DropRestOfWord
        {
            get
            {
                return this._autoComplete_DropRestOfWord;
            }
            set
            {
                this._autoComplete_DropRestOfWord = value;
            }
        }


        public string AutoComplete_FillUpCharacters
        {
            get
            {
                return this._autoComplete_fillUpCharacters;
            }
            set
            {
                this._autoComplete_fillUpCharacters = value;
            }
        }


        public char? AutoComplete_ImageSeperator
        {
            get
            {
                return this._autoComplete_ImageSeperator;
            }
            set
            {
                this._autoComplete_ImageSeperator = value;
            }
        }


        public bool? AutoComplete_IsCaseSensitive
        {
            get
            {
                return this._autoComplete_IsCaseSensitive;
            }
            set
            {
                this._autoComplete_IsCaseSensitive = value;
            }
        }


        public string AutoComplete_List
        {
            get
            {
                return this._autoComplete_List;
            }
            set
            {
                this._autoComplete_List = value;
            }
        }


        public bool? AutoComplete_ListInherits
        {
            get
            {
                return this._autoComplete_ListInherit;
            }
            set
            {
                this._autoComplete_ListInherit = value;
            }
        }


        public char? AutoComplete_ListSeperator
        {
            get
            {
                return this._autoComplete_ListSeperator;
            }
            set
            {
                this._autoComplete_ListSeperator = value;
            }
        }


        public int? AutoComplete_MaxHeight
        {
            get
            {
                return this._autoComplete_MaxHeight;
            }
            set
            {
                this._autoComplete_MaxHeight = value;
            }
        }


        public int? AutoComplete_MaxWidth
        {
            get
            {
                return this._autoComplete_MaxWidth;
            }
            set
            {
                this._autoComplete_MaxWidth = value;
            }
        }


        public bool? AutoComplete_SingleLineAccept
        {
            get
            {
                return this._autoComplete_singleLineAccept;
            }
            set
            {
                this._autoComplete_singleLineAccept = value;
            }
        }


        public string AutoComplete_StopCharacters
        {
            get
            {
                return this._autoComplete_StopCharacters;
            }
            set
            {
                this._autoComplete_StopCharacters = value;
            }
        }


        public Color CallTip_BackColor
        {
            get
            {
                return this._callTip_BackColor;
            }
            set
            {
                this._callTip_BackColor = value;
            }
        }


        public Color CallTip_ForeColor
        {
            get
            {
                return this._callTip_ForeColor;
            }
            set
            {
                this._callTip_ForeColor = value;
            }
        }


        public Color CallTip_HighlightTextColor
        {
            get
            {
                return this._callTip_HighlightTextColor;
            }
            set
            {
                this._callTip_HighlightTextColor = value;
            }
        }


        public int? Caret_BlinkRate
        {
            get
            {
                return this._caret_BlinkRate;
            }
            set
            {
                this._caret_BlinkRate = value;
            }
        }


        public Color Caret_Color
        {
            get
            {
                return this._caret_Color;
            }
            set
            {
                this._caret_Color = value;
            }
        }


        public int? Caret_CurrentLineBackgroundAlpha
        {
            get
            {
                return this._caret_CurrentLineBackgroundAlpha;
            }
            set
            {
                this._caret_CurrentLineBackgroundAlpha = value;
            }
        }


        public Color Caret_CurrentLineBackgroundColor
        {
            get
            {
                return this._caret_CurrentLineBackgroundColor;
            }
            set
            {
                this._caret_CurrentLineBackgroundColor = value;
            }
        }


        public bool? Caret_HighlightCurrentLine
        {
            get
            {
                return this._caret_HighlightCurrentLine;
            }
            set
            {
                this._caret_HighlightCurrentLine = value;
            }
        }


        public bool? Caret_IsSticky
        {
            get
            {
                return this._caret_IsSticky;
            }
            set
            {
                this._caret_IsSticky = value;
            }
        }


        public CaretStyle? Caret_Style
        {
            get
            {
                return this._caret_Style;
            }
            set
            {
                this._caret_Style = value;
            }
        }


        public int? Caret_Width
        {
            get
            {
                return this._caret_Width;
            }
            set
            {
                this._caret_Width = value;
            }
        }


        public bool? Clipboard_ConvertLineBreaksOnPaste
        {
            get
            {
                return this._clipboard_ConvertLineBreaksOnPaste;
            }
            set
            {
                this._clipboard_ConvertLineBreaksOnPaste = value;
            }
        }


        public CommandBindingConfigList Commands_KeyBindingList
        {
            get
            {
                return this._commands_KeyBindingList;
            }
            set
            {
                this._commands_KeyBindingList = value;
            }
        }


        public string DropMarkers_SharedStackName
        {
            get
            {
                return this._dropMarkers_SharedStackName;
            }
            set
            {
                this._dropMarkers_SharedStackName = value;
            }
        }


        public bool? EndOfLine_IsVisisble
        {
            get
            {
                return this._endOfLine_IsVisisble;
            }
            set
            {
                this._endOfLine_IsVisisble = value;
            }
        }


        public EndOfLineMode? EndOfLine_Mode
        {
            get
            {
                return this._endOfLine_Mode;
            }
            set
            {
                this._endOfLine_Mode = value;
            }
        }


        public FoldFlag? Folding_Flags
        {
            get
            {
                return this._folding_Flags;
            }
            set
            {
                this._folding_Flags = value;
            }
        }


        public bool? Folding_IsEnabled
        {
            get
            {
                return this._folding_IsEnabled;
            }
            set
            {
                this._folding_IsEnabled = value;
            }
        }


        public FoldMarkerScheme? Folding_MarkerScheme
        {
            get
            {
                return this._folding_MarkerScheme;
            }
            set
            {
                this._folding_MarkerScheme = value;
            }
        }


        public bool? Folding_UseCompactFolding
        {
            get
            {
                return this._folding_UseCompactFolding;
            }
            set
            {
                this._folding_UseCompactFolding = value;
            }
        }


        public bool HasData
        {
            get { return this._hasData; }
            set
            {
                this._hasData = value;
            }
        }


        public Color Hotspot_ActiveBackColor
        {
            get
            {
                return this._hotspot_ActiveBackColor;
            }
            set
            {
                this._hotspot_ActiveBackColor = value;
            }
        }


        public Color Hotspot_ActiveForeColor
        {
            get
            {
                return this._hotspot_ActiveForeColor;
            }
            set
            {
                this._hotspot_ActiveForeColor = value;
            }
        }


        public bool? Hotspot_ActiveUnderline
        {
            get
            {
                return this._hotspot_ActiveUnderline;
            }
            set
            {
                this._hotspot_ActiveUnderline = value;
            }
        }


        public bool? Hotspot_SingleLine
        {
            get
            {
                return this._hotspot_SingleLine;
            }
            set
            {
                this._hotspot_SingleLine = value;
            }
        }


        public bool? Hotspot_UseActiveBackColor
        {
            get
            {
                return this._hotspot_UseActiveBackColor;
            }
            set
            {
                this._hotspot_UseActiveBackColor = value;
            }
        }


        public bool? Hotspot_UseActiveForeColor
        {
            get
            {
                return this._hotspot_UseActiveForeColor;
            }
            set
            {
                this._hotspot_UseActiveForeColor = value;
            }
        }


        public bool? Indentation_BackspaceUnindents
        {
            get
            {
                return this._indentation_BackspaceUnindents;
            }
            set
            {
                this._indentation_BackspaceUnindents = value;
            }
        }


        public int? Indentation_IndentWidth
        {
            get
            {
                return this._indentation_IndentWidth;
            }
            set
            {
                this._indentation_IndentWidth = value;
            }
        }


        public bool? Indentation_ShowGuides
        {
            get
            {
                return this._indentation_ShowGuides;
            }
            set
            {
                this._indentation_ShowGuides = value;
            }
        }


        public SmartIndent? Indentation_SmartIndentType
        {
            get
            {
                return this._indentation_SmartIndentType;
            }
            set
            {
                this._indentation_SmartIndentType = value;
            }
        }


        public bool? Indentation_TabIndents
        {
            get
            {
                return this._indentation_TabIndents;
            }
            set
            {
                this._indentation_TabIndents = value;
            }
        }


        public int? Indentation_TabWidth
        {
            get
            {
                return this._indentation_TabWidth;
            }
            set
            {
                this._indentation_TabWidth = value;
            }
        }


        public bool? Indentation_UseTabs
        {
            get
            {
                return this._indentation_UseTabs;
            }
            set
            {
                this._indentation_UseTabs = value;
            }
        }


        public IndicatorConfigList Indicator_List
        {
            get
            {
                return this._indicator_List;
            }
            set
            {
                this._indicator_List = value;
            }
        }


        public string Language
        {
            get
            {
                return this._language;
            }
            set
            {
                this._language = value;
            }
        }


        public KeyWordConfigList Lexing_Keywords
        {
            get
            {
                return this._lexing_Keywords;
            }
            set
            {
                this._lexing_Keywords = value;
            }
        }


        public string Lexing_Language
        {
            get
            {
                return this._lexing_Language;
            }
            set
            {
                this._lexing_Language = value;
            }
        }


        public string Lexing_LineCommentPrefix
        {
            get
            {
                return this._lexing_LineCommentPrefix;
            }
            set
            {
                this._lexing_LineCommentPrefix = value;
            }
        }


        public LexerPropertiesConfig Lexing_Properties
        {
            get
            {
                return this._lexing_Properties;
            }
            set
            {
                this._lexing_Properties = value;
            }
        }


        public string Lexing_StreamCommentPrefix
        {
            get
            {
                return this._lexing_StreamCommentPrefix;
            }
            set
            {
                this._lexing_StreamCommentPrefix = value;
            }
        }


        public string Lexing_StreamCommentSuffix
        {
            get
            {
                return this._lexing_StreamCommentSuffix;
            }
            set
            {
                this._lexing_StreamCommentSuffix = value;
            }
        }


        public string Lexing_WhitespaceChars
        {
            get
            {
                return this._lexing_WhitespaceChars;
            }
            set
            {
                this._lexing_WhitespaceChars = value;
            }
        }


        public string Lexing_WordChars
        {
            get
            {
                return this._lexing_WordChars;
            }
            set
            {
                this._lexing_WordChars = value;
            }
        }

        public LineWrappingIndentMode? LineWrapping_IndentMode
        {
            get
            {
                return this._lineWrapping_IndentMode;
            }
            set
            {
                this._lineWrapping_IndentMode = value;
            }
        }


        public int? LineWrapping_IndentSize
        {
            get
            {
                return this._lineWrapping_IndentSize;
            }
            set
            {
                this._lineWrapping_IndentSize = value;
            }
        }


        public LineWrappingMode? LineWrapping_Mode
        {
            get
            {
                return this._lineWrapping_Mode;
            }
            set
            {
                this._lineWrapping_Mode = value;
            }
        }


        public LineWrappingVisualFlags? LineWrapping_VisualFlags
        {
            get
            {
                return this._lineWrapping_VisualFlags;
            }
            set
            {
                this._lineWrapping_VisualFlags = value;
            }
        }


        public LineWrappingVisualFlagsLocations? LineWrapping_VisualFlagsLocations
        {
            get
            {
                return this._lineWrapping_VisualFlagsLocations;
            }
            set
            {
                this._lineWrapping_VisualFlagsLocations = value;
            }
        }


        public Color LongLines_EdgeColor
        {
            get
            {
                return this._longLines_EdgeColor;
            }
            set
            {
                this._longLines_EdgeColor = value;
            }
        }


        public int? LongLines_EdgeColumn
        {
            get
            {
                return this._longLines_EdgeColumn;
            }
            set
            {
                this._longLines_EdgeColumn = value;
            }
        }


        public EdgeMode? LongLines_EdgeMode
        {
            get
            {
                return this._longLines_EdgeMode;
            }
            set
            {
                this._longLines_EdgeMode = value;
            }
        }


        public MarginConfigList Margin_List
        {
            get
            {
                return this._margin_List;
            }
            set
            {
                this._margin_List = value;
            }
        }


        public MarkersConfigList Markers_List
        {
            get
            {
                return this._markers_List;
            }
            set
            {
                this._markers_List = value;
            }
        }


        public bool? Scrolling_EndAtLastLine
        {
            get
            {
                return this._scrolling_EndAtLastLine;
            }
            set
            {
                this._scrolling_EndAtLastLine = value;
            }
        }


        public int? Scrolling_HorizontalWidth
        {
            get
            {
                return this._scrolling_HorizontalWidth;
            }
            set
            {
                this._scrolling_HorizontalWidth = value;
            }
        }


        public ScrollBars? Scrolling_ScrollBars
        {
            get
            {
                return this._scrolling_ScrollBars;
            }
            set
            {
                this._scrolling_ScrollBars = value;
            }
        }


        public int? Scrolling_XOffset
        {
            get
            {
                return this._scrolling_XOffset;
            }
            set
            {
                this._scrolling_XOffset = value;
            }
        }


        public Color Selection_BackColor
        {
            get
            {
                return this._selection_BackColor;
            }
            set
            {
                this._selection_BackColor = value;
            }
        }


        public Color Selection_BackColorUnfocused
        {
            get
            {
                return this._selection_BackColorUnfocused;
            }
            set
            {
                this._selection_BackColorUnfocused = value;
            }
        }


        public Color Selection_ForeColor
        {
            get
            {
                return this._selection_ForeColor;
            }
            set
            {
                this._selection_ForeColor = value;
            }
        }


        public Color Selection_ForeColorUnfocused
        {
            get
            {
                return this._selection_ForeColorUnfocused;
            }
            set
            {
                this._selection_ForeColorUnfocused = value;
            }
        }


        public bool? Selection_Hidden
        {
            get
            {
                return this._selection_Hidden;
            }
            set
            {
                this._selection_Hidden = value;
            }
        }


        public bool? Selection_HideSelection
        {
            get
            {
                return this._selection_HideSelection;
            }
            set
            {
                this._selection_HideSelection = value;
            }
        }


        public SelectionMode? Selection_Mode
        {
            get
            {
                return this._selection_Mode;
            }
            set
            {
                this._selection_Mode = value;
            }
        }


        public SnippetsConfigList SnippetsConfigList
        {
            get
            {
                return this._snippetsConfigList;
            }
            set
            {
                this._snippetsConfigList = value;
            }
        }


        public StyleConfigList Styles
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


        public bool? UndoRedoIsUndoEnabled
        {
            get
            {
                return this._undoRedoIsUndoEnabled;
            }
            set
            {
                this._undoRedoIsUndoEnabled = value;
            }
        }


        public Color Whitespace_BackColor
        {
            get
            {
                return this._whitespace_BackColor;
            }
            set
            {
                this._whitespace_BackColor = value;
            }
        }


        public Color Whitespace_ForeColor
        {
            get
            {
                return this._whitespace_ForeColor;
            }
            set
            {
                this._whitespace_ForeColor = value;
            }
        }


        public WhitespaceMode? Whitespace_Mode
        {
            get
            {
                return this._whitespace_Mode;
            }
            set
            {
                this._whitespace_Mode = value;
            }
        }

        #endregion Properties


        #region Constructors

        public Configuration(string language)
        {
            this._language = language;
        }


        public Configuration(XmlDocument configDocument, string language)
        {
            this._language = language;
            Load(configDocument);
        }


        public Configuration(TextReader txtReader, string language)
        {
            this._language = language;
            Load(txtReader);
        }


        public Configuration(XmlReader reader, string language)
        {
            this._language = language;
            Load(reader);
        }


        public Configuration(string fileName, string language, bool useXmlReader)
        {
            this._language = language;
            Load(fileName, useXmlReader);
        }


        public Configuration(Stream inStream, string language, bool useXmlReader)
        {
            this._language = language;
            Load(inStream, useXmlReader);
        }

        #endregion Constructors
    }
}

