#region Using Directives

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.IO;
using System.Reflection;
using System.Windows.Forms;

#endregion


namespace ARCed.Scintilla.Configuration
{
	[TypeConverter(typeof(ExpandableObjectConverter))]
	public class ConfigurationManager : TopLevelHelper
	{
		#region Fields

		private string _appDataFolder;
		private bool _clearIndicators;
		private bool _clearKeyBindings;
		private bool _clearMargins;
		private bool _clearMarkers;
		private bool _clearSnippets;
		private bool _clearStyles;
		private string _customLocation;
		private bool _isBuiltInEnabled = true;
		private bool _isUserEnabled = true;
		private string _language;
		private ConfigurationLoadOrder _loadOrder = ConfigurationLoadOrder.BuiltInCustomUser;
		private string _userFolder;
		private bool _useXmlReader = true;

		#endregion Fields

		#region Methods

		public void Configure()
		{
			if (Scintilla.IsDesignMode || Scintilla.IsInitializing)
				return;

			Configuration builtInDefault = null,
				builtInLang = null,
				customDefault = null,
				customLang = null,
				userDefault = null,
				userLang = null;

			if (this._isBuiltInEnabled)
			{
				using (Stream s = GetType().Assembly.GetManifestResourceStream("ARCed.Scintilla.Configuration.Builtin.default.xml"))
					builtInDefault = new Configuration(s, "default", this._useXmlReader);
				if (!string.IsNullOrEmpty(this._language))
					using (Stream s = GetType().Assembly.GetManifestResourceStream("ARCed.Scintilla.Configuration.Builtin." + this._language + ".xml"))
						if (s != null)
							builtInLang = new Configuration(s, this._language, this._useXmlReader);
			}

			if (this._isUserEnabled)
			{
				string defPath = Path.Combine(this.UserFolder, "default.xml");
				if (File.Exists(defPath))
					userDefault = new Configuration(defPath, "default", this._useXmlReader);

				if (!string.IsNullOrEmpty(this._language))
				{
					string langPath = Path.Combine(this.UserFolder, this._language + ".xml");
					if (File.Exists(langPath))
						userLang = new Configuration(langPath, this._language, this._useXmlReader);
				}
			}

			if (!string.IsNullOrEmpty(this._customLocation))
			{
				string customDefaultPath = this.GetCustomConfigPath("default");
				string customLanguagePath = this.GetCustomConfigPath(this._language);

				if (!string.IsNullOrEmpty(customDefaultPath))
					customDefault = new Configuration(customDefaultPath, "default", this._useXmlReader);

				if (!string.IsNullOrEmpty(customLanguagePath))
					customLang = new Configuration(customLanguagePath, this._language, this._useXmlReader);
				else
					throw new FileNotFoundException("Could not find the custom configuration file.", this._customLocation);
			}

			var configList = new List<Configuration>();
			if (this._loadOrder == ConfigurationLoadOrder.BuiltInCustomUser)
			{
				if (builtInDefault != null && builtInDefault.HasData)
					configList.Add(builtInDefault);

				if (builtInLang != null && builtInLang.HasData)
					configList.Add(builtInLang);

				if (customDefault != null && customDefault.HasData)
					configList.Add(customDefault);

				if (customLang != null && customLang.HasData)
					configList.Add(customLang);

				if (userDefault != null && userDefault.HasData)
					configList.Add(userDefault);

				if (userLang != null && userLang.HasData)
					configList.Add(userLang);
			}
			else if (this._loadOrder == ConfigurationLoadOrder.BuiltInUserCustom)
			{
				if (builtInDefault != null && builtInDefault.HasData)
					configList.Add(builtInDefault);

				if (builtInLang != null && builtInLang.HasData)
					configList.Add(builtInLang);

				if (userDefault != null && userDefault.HasData)
					configList.Add(userDefault);

				if (userLang != null && userLang.HasData)
					configList.Add(userLang);

				if (customDefault != null && customDefault.HasData)
					configList.Add(customDefault);

				if (customLang != null && customLang.HasData)
					configList.Add(customLang);
			}
			else if (this._loadOrder == ConfigurationLoadOrder.CustomBuiltInUser)
			{
				if (customDefault != null && customDefault.HasData)
					configList.Add(customDefault);

				if (customLang != null && customLang.HasData)
					configList.Add(customLang);

				if (builtInDefault != null && builtInDefault.HasData)
					configList.Add(builtInDefault);

				if (builtInLang != null && builtInLang.HasData)
					configList.Add(builtInLang);

				if (userDefault != null && userDefault.HasData)
					configList.Add(userDefault);

				if (userLang != null && userLang.HasData)
					configList.Add(userLang);
			}
			else if (this._loadOrder == ConfigurationLoadOrder.CustomUserBuiltIn)
			{
				if (customDefault != null && customDefault.HasData)
					configList.Add(customDefault);

				if (customLang != null && customLang.HasData)
					configList.Add(customLang);

				if (userDefault != null && userDefault.HasData)
					configList.Add(userDefault);

				if (userLang != null && userLang.HasData)
					configList.Add(userLang);

				if (builtInDefault != null && builtInDefault.HasData)
					configList.Add(builtInDefault);

				if (builtInLang != null && builtInLang.HasData)
					configList.Add(builtInLang);
			}
			else if (this._loadOrder == ConfigurationLoadOrder.UserBuiltInCustom)
			{
				if (userDefault != null && userDefault.HasData)
					configList.Add(userDefault);

				if (userLang != null && userLang.HasData)
					configList.Add(userLang);

				if (builtInDefault != null && builtInDefault.HasData)
					configList.Add(builtInDefault);

				if (builtInLang != null && builtInLang.HasData)
					configList.Add(builtInLang);

				if (customDefault != null && customDefault.HasData)
					configList.Add(customDefault);

				if (customLang != null && customLang.HasData)
					configList.Add(customLang);

			}
			else if (this._loadOrder == ConfigurationLoadOrder.UserCustomBuiltIn)
			{
				if (userDefault != null && userDefault.HasData)
					configList.Add(userDefault);

				if (userLang != null && userLang.HasData)
					configList.Add(userLang);

				if (customDefault != null && customDefault.HasData)
					configList.Add(customDefault);

				if (customLang != null && customLang.HasData)
					configList.Add(customLang);

				if (builtInDefault != null && builtInDefault.HasData)
					configList.Add(builtInDefault);

				if (builtInLang != null && builtInLang.HasData)
					configList.Add(builtInLang);
			}

			Configure(configList);
		}


		public void Configure(Configuration config)
		{
			this.Configure(new List<Configuration>(new[] { config }));
		}


		internal void Configure(List<Configuration> configList)
		{
			//	So here is the general pattern: We go through each of
			//	the configurations in the list (which has been ordered
			//	by terrain). If the configuration has a value we're
			//	looking for it overwrites whatever was before it.
			//	In the _end if the value isn't null, we set the
			//	corresponding Scintilla Value to this.
			bool? b = null;
			int? i = null;
			Color co = Color.Empty;
			char? ch = null;
			string s = null;

			foreach (Configuration c in configList)
			{
				if (c.AutoComplete_AutoHide.HasValue)
					b = c.AutoComplete_AutoHide;
			}
			if (b.HasValue)
				Scintilla.AutoComplete.AutoHide = b.Value;

			b = null;
			foreach (Configuration c in configList)
			{
				if (c.AutoComplete_AutomaticLengthEntered.HasValue)
					b = c.AutoComplete_AutomaticLengthEntered;
			}
			if (b.HasValue)
				Scintilla.AutoComplete.AutomaticLengthEntered = b.Value;

			b = null;
			foreach (Configuration c in configList)
			{
				if (c.AutoComplete_CancelAtStart.HasValue)
					b = c.AutoComplete_CancelAtStart;
			}
			if (b.HasValue)
				Scintilla.AutoComplete.CancelAtStart = b.Value;

			b = null;
			foreach (Configuration c in configList)
			{
				if (c.AutoComplete_DropRestOfWord.HasValue)
					b = c.AutoComplete_DropRestOfWord;
			}
			if (b.HasValue)
				Scintilla.AutoComplete.DropRestOfWord = b.Value;

			s = null;
			foreach (Configuration c in configList)
			{
				if (c.AutoComplete_FillUpCharacters != null)
					s = c.AutoComplete_FillUpCharacters;
			}
			if (s != null)
				Scintilla.AutoComplete.FillUpCharacters = s;

			ch = null;
			foreach (Configuration c in configList)
			{
				if (c.AutoComplete_ImageSeperator != null)
					ch = c.AutoComplete_ImageSeperator;
			}
			if (ch != null)
				Scintilla.AutoComplete.ImageSeparator = ch.Value;

			b = null;
			foreach (Configuration c in configList)
			{
				if (c.AutoComplete_IsCaseSensitive.HasValue)
					b = c.AutoComplete_IsCaseSensitive;

			}
			if (b.HasValue)
				Scintilla.AutoComplete.IsCaseSensitive = b.Value;

			ch = null;
			foreach (Configuration c in configList)
			{
				if (c.AutoComplete_ListSeperator.HasValue)
					ch = c.AutoComplete_ListSeperator;

			}
			if (ch.HasValue)
				Scintilla.AutoComplete.ListSeparator = ch.Value;

			string seperator = Scintilla.AutoComplete.ListSeparator.ToString();
			s = null;
			foreach (Configuration c in configList)
			{
				//	Lists tend to have an extra config property of "inherits".
				//	It this flag set to false, the list is cleared before setting
				//	the current config's list. Otherwise the current config adds
				//	to the previous configs'.
				if (c.AutoComplete_List != null)
				{
					if (!(c.AutoComplete_ListInherits.HasValue && !c.AutoComplete_ListInherits.Value) || string.IsNullOrEmpty(s))
						s = c.AutoComplete_List;
					else
						s += seperator + c.AutoComplete_List;
				}
			}
			if (s != null)
				Scintilla.AutoComplete.ListString = s;

			i = null;
			foreach (Configuration c in configList)
			{
				if (c.AutoComplete_MaxHeight.HasValue)
					i = c.AutoComplete_MaxHeight;

			}
			if (i.HasValue)
				Scintilla.AutoComplete.MaxHeight = i.Value;

			i = null;
			foreach (Configuration c in configList)
			{
				if (c.AutoComplete_MaxWidth.HasValue)
					i = c.AutoComplete_MaxWidth;
			}
			if (i.HasValue)
				Scintilla.AutoComplete.MaxWidth = i.Value;


			b = null;
			foreach (Configuration c in configList)
			{
				if (c.AutoComplete_SingleLineAccept.HasValue)
					b = c.AutoComplete_SingleLineAccept;

			}
			if (b.HasValue)
				Scintilla.AutoComplete.SingleLineAccept = b.Value;

			s = null;
			foreach (Configuration c in configList)
			{
				if (c.AutoComplete_StopCharacters != null)
					s = c.AutoComplete_StopCharacters;
			}
			if (s != null)
				Scintilla.AutoComplete.StopCharacters = s;


			co = Color.Empty;
			foreach (Configuration c in configList)
			{
				if (c.CallTip_BackColor != Color.Empty)
					co = c.CallTip_BackColor;

			}
			if (co != Color.Empty)
				Scintilla.CallTip.BackColor = co;

			co = Color.Empty;
			foreach (Configuration c in configList)
			{
				if (c.CallTip_ForeColor != Color.Empty)
					co = c.CallTip_ForeColor;

			}
			if (co != Color.Empty)
				Scintilla.CallTip.ForeColor = co;

			co = Color.Empty;
			foreach (Configuration c in configList)
			{
				if (c.CallTip_HighlightTextColor != Color.Empty)
					co = c.CallTip_HighlightTextColor;

			}
			if (co != Color.Empty)
				Scintilla.CallTip.HighlightTextColor = co;

			i = null;
			foreach (Configuration c in configList)
			{
				if (c.Caret_BlinkRate.HasValue)
					i = c.Caret_BlinkRate;
			}
			if (i.HasValue)
				Scintilla.Caret.BlinkRate = i.Value;

			co = Color.Empty;
			foreach (Configuration c in configList)
			{
				if (c.Caret_Color != Color.Empty)
					co = c.Caret_Color;

			}
			if (co != Color.Empty)
				Scintilla.Caret.Color = co;

			i = null;
			foreach (Configuration c in configList)
			{
				if (c.Caret_CurrentLineBackgroundAlpha.HasValue)
					i = c.Caret_CurrentLineBackgroundAlpha;
			}
			if (i.HasValue)
				Scintilla.Caret.CurrentLineBackgroundAlpha = i.Value;

			co = Color.Empty;
			foreach (Configuration c in configList)
			{
				if (c.Caret_CurrentLineBackgroundColor != Color.Empty)
					co = c.Caret_CurrentLineBackgroundColor;

			}
			if (co != Color.Empty)
				Scintilla.Caret.CurrentLineBackgroundColor = co;

			b = null;
			foreach (Configuration c in configList)
			{
				if (c.Caret_HighlightCurrentLine.HasValue)
					b = c.Caret_HighlightCurrentLine;

			}
			if (b.HasValue)
				Scintilla.Caret.HighlightCurrentLine = b.Value;

			b = null;
			foreach (Configuration c in configList)
			{
				if (c.Caret_IsSticky.HasValue)
					b = c.Caret_IsSticky;

			}
			if (b.HasValue)
				Scintilla.Caret.IsSticky = b.Value;


			CaretStyle? caretStyle = null;
			foreach (Configuration c in configList)
			{
				if (c.Caret_Style.HasValue)
					caretStyle = c.Caret_Style;
			}
			if (caretStyle.HasValue)
				Scintilla.Caret.Style = caretStyle.Value;

			i = null;
			foreach (Configuration c in configList)
			{
				if (c.Caret_Width.HasValue)
					i = c.Caret_Width;
			}
			if (i.HasValue)
				Scintilla.Caret.Width = i.Value;

			b = null;
			foreach (Configuration c in configList)
			{
				if (c.Clipboard_ConvertLineBreaksOnPaste.HasValue)
					b = c.Clipboard_ConvertLineBreaksOnPaste;
			}
			if (b.HasValue)
				Scintilla.Clipboard.ConvertLineBreaksOnPaste = b.Value;

			b = null;
			foreach (Configuration c in configList)
			{
				if (c.Commands_KeyBindingList.AllowDuplicateBindings.HasValue)
					b = c.Commands_KeyBindingList.AllowDuplicateBindings;
			}
			if (b.HasValue)
				Scintilla.Commands.AllowDuplicateBindings = b.Value;

			if (this._clearKeyBindings)
				Scintilla.Commands.RemoveAllBindings();

			var cbcl = new CommandBindingConfigList();
			foreach (Configuration c in configList)
			{
				if (c.Commands_KeyBindingList.Inherit.HasValue && !c.Commands_KeyBindingList.Inherit.Value)
					cbcl.Clear();

				foreach (CommandBindingConfig cbc in c.Commands_KeyBindingList)
					cbcl.Add(cbc);
			}

			foreach (CommandBindingConfig cbc in cbcl)
			{
				//	This indicates that we should clear out any
				//	existing commands bound to this key combination
				if (cbc.ReplaceCurrent.HasValue && cbc.ReplaceCurrent.Value)
					Scintilla.Commands.RemoveBinding(cbc.KeyBinding.KeyCode, cbc.KeyBinding.Modifiers);

				Scintilla.Commands.AddBinding(cbc.KeyBinding.KeyCode, cbc.KeyBinding.Modifiers, cbc.BindableCommand);
			}

			s = null;
			foreach (Configuration c in configList)
			{
				if (c.DropMarkers_SharedStackName != null)
					s = c.DropMarkers_SharedStackName;
			}
			if (s != null)
				Scintilla.DropMarkers.SharedStackName = s;

			b = null;
			foreach (Configuration c in configList)
			{
				if (c.EndOfLine_IsVisisble.HasValue)
					b = c.EndOfLine_IsVisisble;
			}
			if (b.HasValue)
				Scintilla.EndOfLine.IsVisible = b.Value;

			EndOfLineMode? endOfLineMode = null;
			foreach (Configuration c in configList)
			{
				if (c.EndOfLine_Mode.HasValue)
					endOfLineMode = c.EndOfLine_Mode;
			}
			if (endOfLineMode.HasValue)
				Scintilla.EndOfLine.Mode = endOfLineMode.Value;

			FoldFlag? ff = null;
			foreach (Configuration c in configList)
			{
				if (c.Folding_Flags.HasValue)
					ff = c.Folding_Flags;
			}
			if (ff.HasValue)
				Scintilla.Folding.Flags = ff.Value;

			// FoldMarkerScheme moved to Markers section
			// becuase Markers need to come first as the
			// FoldMarkerScheme really just manipulates
			// Markers.

			b = null;
			foreach (Configuration c in configList)
			{
				if (c.Folding_IsEnabled.HasValue)
					b = c.Folding_IsEnabled;
			}
			if (b.HasValue)
				Scintilla.Folding.IsEnabled = b.Value;

			b = null;
			foreach (Configuration c in configList)
			{
				if (c.Folding_UseCompactFolding.HasValue)
					b = c.Folding_UseCompactFolding;
			}
			if (b.HasValue)
				Scintilla.Folding.UseCompactFolding = b.Value;

			co = Color.Empty;
			foreach (Configuration c in configList)
			{
				if (c.Hotspot_ActiveBackColor != Color.Empty)
					co = c.Hotspot_ActiveBackColor;

			}
			if (co != Color.Empty)
				Scintilla.HotspotStyle.ActiveBackColor = co;

			co = Color.Empty;
			foreach (Configuration c in configList)
			{
				if (c.Hotspot_ActiveForeColor != Color.Empty)
					co = c.Hotspot_ActiveForeColor;

			}
			if (co != Color.Empty)
				Scintilla.HotspotStyle.ActiveForeColor = co;

			b = null;
			foreach (Configuration c in configList)
			{
				if (c.Hotspot_ActiveUnderline.HasValue)
					b = c.Hotspot_ActiveUnderline;
			}
			if (b.HasValue)
				Scintilla.HotspotStyle.ActiveUnderline = b.Value;

			b = null;
			foreach (Configuration c in configList)
			{
				if (c.Hotspot_SingleLine.HasValue)
					b = c.Hotspot_SingleLine;
			}
			if (b.HasValue)
				Scintilla.HotspotStyle.SingleLine = b.Value;


			b = null;
			foreach (Configuration c in configList)
			{
				if (c.Hotspot_UseActiveBackColor.HasValue)
					b = c.Hotspot_UseActiveBackColor;
			}
			if (b.HasValue)
				Scintilla.HotspotStyle.UseActiveBackColor = b.Value;

			b = null;
			foreach (Configuration c in configList)
			{
				if (c.Hotspot_UseActiveForeColor.HasValue)
					b = c.Hotspot_UseActiveForeColor;
			}
			if (b.HasValue)
				Scintilla.HotspotStyle.UseActiveForeColor = b.Value;

			b = null;
			foreach (Configuration c in configList)
			{
				if (c.Indentation_BackspaceUnindents.HasValue)
					b = c.Indentation_BackspaceUnindents;
			}
			if (b.HasValue)
				Scintilla.Indentation.BackspaceUnindents = b.Value;


			i = null;
			foreach (Configuration c in configList)
			{
				if (c.Indentation_IndentWidth.HasValue)
					i = c.Indentation_IndentWidth;
			}
			if (i.HasValue)
				Scintilla.Indentation.IndentWidth = i.Value;


			b = null;
			foreach (Configuration c in configList)
			{
				if (c.Indentation_ShowGuides.HasValue)
					b = c.Indentation_ShowGuides;
			}
			if (b.HasValue)
				Scintilla.Indentation.ShowGuides = b.Value;

			b = null;
			foreach (Configuration c in configList)
			{
				if (c.Indentation_TabIndents.HasValue)
					b = c.Indentation_TabIndents;
			}
			if (b.HasValue)
				Scintilla.Indentation.TabIndents = b.Value;


			i = null;
			foreach (Configuration c in configList)
			{
				if (c.Indentation_TabWidth.HasValue)
					i = c.Indentation_TabWidth;
			}
			if (i.HasValue)
				Scintilla.Indentation.TabWidth = i.Value;

			b = null;
			foreach (Configuration c in configList)
			{
				if (c.Indentation_UseTabs.HasValue)
					b = c.Indentation_UseTabs;
			}
			if (b.HasValue)
				Scintilla.Indentation.UseTabs = b.Value;

			SmartIndent? si = null;
			foreach (Configuration c in configList)
			{
				if (c.Indentation_SmartIndentType.HasValue)
					si = c.Indentation_SmartIndentType;
			}
			if (si.HasValue)
				Scintilla.Indentation.SmartIndentType = si.Value;

			if (this._clearIndicators)
				Scintilla.Indicators.Reset();

			var resolvedIndicators = new IndicatorConfigList();
			foreach (Configuration c in configList)
			{
				if (c.Indicator_List.Inherit.HasValue && !c.Indicator_List.Inherit.Value)
					resolvedIndicators.Clear();

				foreach (IndicatorConfig ic in c.Indicator_List)
				{
					if (!resolvedIndicators.Contains(ic.Number) || !(ic.Inherit.HasValue && ic.Inherit.Value))
					{
						resolvedIndicators.Remove(ic.Number);
						resolvedIndicators.Add(ic);
					}
					else
					{
						IndicatorConfig rc = resolvedIndicators[ic.Number];
						if (ic.Color != Color.Empty)
							rc.Color = ic.Color;

						if (ic.Style.HasValue)
							rc.Style = ic.Style;

						if (ic.IsDrawnUnder.HasValue)
							rc.IsDrawnUnder = ic.IsDrawnUnder;
					}
				}
			}

			foreach (IndicatorConfig ic in resolvedIndicators)
			{
				Indicator ind = Scintilla.Indicators[ic.Number];
				if (ic.Color != Color.Empty)
					ind.Color = ic.Color;

				if (ic.IsDrawnUnder.HasValue)
					ind.IsDrawnUnder = ic.IsDrawnUnder.Value;

				if (ic.Style.HasValue)
					ind.Style = ic.Style.Value;
			}

			//	Hrm... unfortunately there's no way to clear
			//	Scintilla's Lexing Properties. Guess we'll just
			//	have to live with adding to the existing list 
			//	and/or just overriding with new values. This
			//	means that the "Inherit" attribute is really
			//	meaningless. Nevertheless I'm leaving it in
			//	just in case it ever becomes useful.
			foreach (Configuration c in configList)
			{
				foreach (KeyValuePair<string, string> item in c.Lexing_Properties)
				{
					Scintilla.Lexing.SetProperty(item.Key, item.Value);
				}
			}

			s = null;
			foreach (Configuration c in configList)
			{
				if (c.Lexing_WhitespaceChars != null)
					s = c.Lexing_WhitespaceChars;
			}
			if (s != null)
				Scintilla.Lexing.WhitespaceChars = s;


			s = null;
			foreach (Configuration c in configList)
			{
				if (c.Lexing_WordChars != null)
					s = c.Lexing_WordChars;
			}
			if (s != null)
				Scintilla.Lexing.WordChars = s;

			s = null;
			foreach (Configuration c in configList)
			{
				if (c.Lexing_LineCommentPrefix != null)
					s = c.Lexing_LineCommentPrefix;
			}
			if (s != null)
				Scintilla.Lexing.LineCommentPrefix = s;

			s = null;
			foreach (Configuration c in configList)
			{
				if (c.Lexing_StreamCommentPrefix != null)
					s = c.Lexing_StreamCommentPrefix;
			}
			if (s != null)
				Scintilla.Lexing.StreamCommentPrefix = s;

			s = null;
			foreach (Configuration c in configList)
			{
				if (c.Lexing_StreamCommentSuffix != null)
					s = c.Lexing_StreamCommentSuffix;
			}
			if (s != null)
				Scintilla.Lexing.StreamCommentSufix = s;

			s = null;
			foreach (Configuration c in configList)
			{
				if (c.Lexing_Language != null)
					s = c.Lexing_Language;
			}

			if (s == null)
			{
				//	None of the configs specified a lexer. First let's see if
				//	we have a Language-Lexer map defined:
				if (Scintilla.Lexing.LexerLanguageMap.ContainsKey(this._language))
				{
					s = Scintilla.Lexing.LexerLanguageMap[this._language];
				}
				else
				{
					try
					{
						Enum.Parse(typeof(Lexer), this._language, true);

						//	If we made it here, the language matches one of
						//	the lexer names, just use that.
						s = this._language;
					}
					catch (ArgumentException)
					{
						//	No match, oh well. Don't set the lexer.
					}
				}
			}
			Scintilla.Lexing.LexerName = s;

			// Issue 32402: After some experimentation I found that keywords
			// must be set AFTER the lexer is set.
			foreach (Configuration c in configList)
			{
				foreach (KeyWordConfig kwc in c.Lexing_Keywords)
				{
					if (kwc.Inherit.HasValue && kwc.Inherit.Value)
						Scintilla.Lexing.Keywords[kwc.List] += kwc.Value;
					else
						Scintilla.Lexing.Keywords[kwc.List] = kwc.Value;
				}
			}

			i = null;
			foreach (Configuration c in configList)
			{
				if (c.LineWrapping_IndentSize.HasValue)
					i = c.LineWrapping_IndentSize;
			}
			if (i.HasValue)
				Scintilla.LineWrapping.IndentSize = i.Value;

			LineWrappingIndentMode? lwim = null;
			foreach (Configuration c in configList)
			{
				if (c.LineWrapping_IndentMode.HasValue)
					lwim = c.LineWrapping_IndentMode;
			}
			if (lwim.HasValue)
				Scintilla.LineWrapping.IndentMode = lwim.Value;

			LineWrappingMode? lwm = null;
			foreach (Configuration c in configList)
			{
				if (c.LineWrapping_Mode.HasValue)
					lwm = c.LineWrapping_Mode;
			}
			if (lwm.HasValue)
				Scintilla.LineWrapping.Mode = lwm.Value;

			LineWrappingVisualFlags? lwvf = null;
			foreach (Configuration c in configList)
			{
				if (c.LineWrapping_VisualFlags.HasValue)
					lwvf = c.LineWrapping_VisualFlags;
			}
			if (lwvf.HasValue)
				Scintilla.LineWrapping.VisualFlags = lwvf.Value;

			LineWrappingVisualFlagsLocations? lwvfl = null;
			foreach (Configuration c in configList)
			{
				if (c.LineWrapping_VisualFlagsLocations.HasValue)
					lwvfl = c.LineWrapping_VisualFlagsLocations;
			}
			if (lwvfl.HasValue)
				Scintilla.LineWrapping.VisualFlagsLocations = lwvfl.Value;

			co = Color.Empty;
			foreach (Configuration c in configList)
			{
				if (c.LongLines_EdgeColor != Color.Empty)
					co = c.LongLines_EdgeColor;

			}
			if (co != Color.Empty)
				Scintilla.LongLines.EdgeColor = co;


			i = null;
			foreach (Configuration c in configList)
			{
				if (c.LongLines_EdgeColumn.HasValue)
					i = c.LongLines_EdgeColumn;
			}
			if (i.HasValue)
				Scintilla.LongLines.EdgeColumn = i.Value;


			EdgeMode? em = null;
			foreach (Configuration c in configList)
			{
				if (c.LongLines_EdgeMode.HasValue)
					em = c.LongLines_EdgeMode;

			}
			if (em.HasValue)
				Scintilla.LongLines.EdgeMode = em.Value;


			if (this._clearMargins)
				Scintilla.Margins.Reset();

			var margins = new Dictionary<int, MarginConfig>();
			foreach (Configuration c in configList)
			{
				if (c.Margin_List.Inherit.HasValue && !c.Margin_List.Inherit.Value)
					margins.Clear();

				foreach (MarginConfig mc in c.Margin_List)
				{

					if (!margins.ContainsKey(mc.Number) || (mc.Inherit.HasValue && !mc.Inherit.Value))
					{
						margins.Remove(mc.Number);
						margins.Add(mc.Number, mc);
					}
					else
					{
						MarginConfig m = margins[mc.Number];

						if (mc.AutoToggleMarkerNumber.HasValue)
							m.AutoToggleMarkerNumber = mc.AutoToggleMarkerNumber.Value;

						if (mc.IsClickable.HasValue)
							m.IsClickable = mc.IsClickable.Value;

						if (mc.IsFoldMargin.HasValue)
							m.IsFoldMargin = mc.IsFoldMargin.Value;

						if (mc.IsMarkerMargin.HasValue)
							m.IsMarkerMargin = mc.IsMarkerMargin.Value;

						if (mc.Type.HasValue)
							m.Type = mc.Type.Value;

						if (mc.Width.HasValue)
							m.Width = mc.Width.Value;
					}
				}
			}

			foreach (MarginConfig mc in margins.Values)
			{
				Margin m = Scintilla.Margins[mc.Number];

				if (mc.AutoToggleMarkerNumber.HasValue)
					m.AutoToggleMarkerNumber = mc.AutoToggleMarkerNumber.Value;

				if (mc.IsClickable.HasValue)
					m.IsClickable = mc.IsClickable.Value;

				if (mc.IsFoldMargin.HasValue)
					m.IsFoldMargin = mc.IsFoldMargin.Value;

				if (mc.IsMarkerMargin.HasValue)
					m.IsMarkerMargin = mc.IsMarkerMargin.Value;

				if (mc.Type.HasValue)
					m.Type = mc.Type.Value;

				if (mc.Width.HasValue)
					m.Width = mc.Width.Value;
			}

			if (this._clearMarkers)
				Scintilla.Markers.Reset();

			var resolvedMarkers = new MarkersConfigList();
			foreach (Configuration c in configList)
			{
				if (c.Markers_List.Inherit.HasValue && !c.Markers_List.Inherit.Value)
					resolvedMarkers.Clear();

				foreach (MarkersConfig mc in c.Markers_List)
				{
					if (!resolvedMarkers.Contains(mc.Number.Value) || (mc.Inherit.HasValue && !mc.Inherit.Value))
					{
						resolvedMarkers.Remove(mc.Number.Value);
						resolvedMarkers.Add(mc);
					}
					else
					{
						if (!mc.Number.HasValue)
							mc.Number = (int)(MarkerOutline)Enum.Parse(typeof(MarkerOutline), mc.Name, true);

						MarkersConfig m = resolvedMarkers[mc.Number.Value];
						if (mc.Alpha.HasValue)
							m.Alpha = mc.Alpha;

						if (mc.BackColor != Color.Empty)
							m.BackColor = mc.BackColor;

						if (mc.ForeColor != Color.Empty)
							m.ForeColor = mc.ForeColor;

						if (mc.Symbol.HasValue)
							m.Symbol = mc.Symbol;
					}
				}
			}

			foreach (MarkersConfig mc in resolvedMarkers)
			{
				Marker m = Scintilla.Markers[mc.Number.Value];

				if (mc.Alpha.HasValue)
					m.Alpha = mc.Alpha.Value;

				if (mc.BackColor != Color.Empty)
					m.BackColor = mc.BackColor;

				if (mc.ForeColor != Color.Empty)
					m.ForeColor = mc.ForeColor;

				if (mc.Symbol.HasValue)
					m.Symbol = mc.Symbol.Value;
			}



			FoldMarkerScheme? fms = null;
			foreach (Configuration c in configList)
			{
				if (c.Folding_MarkerScheme.HasValue)
					fms = c.Folding_MarkerScheme;
			}
			if (fms.HasValue)
				Scintilla.Folding.MarkerScheme = fms.Value;



			b = null;
			foreach (Configuration c in configList)
			{
				if (c.Scrolling_EndAtLastLine.HasValue)
					b = c.Scrolling_EndAtLastLine;
			}
			if (b.HasValue)
				Scintilla.Scrolling.EndAtLastLine = b.Value;

			i = null;
			foreach (Configuration c in configList)
			{
				if (c.Scrolling_HorizontalWidth.HasValue)
					i = c.Scrolling_HorizontalWidth;
			}
			if (i.HasValue)
				Scintilla.Scrolling.HorizontalWidth = i.Value;

			ScrollBars? sb = null;
			foreach (Configuration c in configList)
			{
				if (c.Scrolling_ScrollBars.HasValue)
					sb = c.Scrolling_ScrollBars;
			}
			if (sb.HasValue)
				Scintilla.Scrolling.ScrollBars = sb.Value;


			i = null;
			foreach (Configuration c in configList)
			{
				if (c.Scrolling_XOffset.HasValue)
					i = c.Scrolling_XOffset;
			}
			if (i.HasValue)
				Scintilla.Scrolling.XOffset = i.Value;


			co = Color.Empty;
			foreach (Configuration c in configList)
			{
				if (c.Selection_BackColor != Color.Empty)
					co = c.Selection_BackColor;

			}
			if (co != Color.Empty)
				Scintilla.Selection.BackColor = co;


			co = Color.Empty;
			foreach (Configuration c in configList)
			{
				if (c.Selection_BackColorUnfocused != Color.Empty)
					co = c.Selection_BackColorUnfocused;

			}
			if (co != Color.Empty)
				Scintilla.Selection.BackColorUnfocused = co;

			co = Color.Empty;
			foreach (Configuration c in configList)
			{
				if (c.Selection_ForeColor != Color.Empty)
					co = c.Selection_ForeColor;

			}
			if (co != Color.Empty)
				Scintilla.Selection.ForeColor = co;

			co = Color.Empty;
			foreach (Configuration c in configList)
			{
				if (c.Selection_ForeColorUnfocused != Color.Empty)
					co = c.Selection_ForeColorUnfocused;

			}
			if (co != Color.Empty)
				Scintilla.Selection.ForeColorUnfocused = co;


			b = null;
			foreach (Configuration c in configList)
			{
				if (c.Selection_Hidden.HasValue)
					b = c.Selection_Hidden;
			}
			if (b.HasValue)
				Scintilla.Selection.Hidden = b.Value;


			b = null;
			foreach (Configuration c in configList)
			{
				if (c.Selection_HideSelection.HasValue)
					b = c.Selection_HideSelection;
			}
			if (b.HasValue)
				Scintilla.Selection.HideSelection = b.Value;

			SelectionMode? selectionMode = null;
			foreach (Configuration c in configList)
			{
				if (c.Selection_Mode.HasValue)
					selectionMode = c.Selection_Mode;
			}
			if (selectionMode.HasValue)
				Scintilla.Selection.Mode = selectionMode.Value;


			if (this._clearSnippets)
				Scintilla.Snippets.List.Clear();

			b = null;
			foreach (Configuration c in configList)
			{
				if (c.SnippetsConfigList.IsEnabled.HasValue)
					b = c.SnippetsConfigList.IsEnabled;
			}
			if (b.HasValue)
				Scintilla.Snippets.IsEnabled = b.Value;

			b = null;
			foreach (Configuration c in configList)
			{
				if (c.SnippetsConfigList.IsOneKeySelectionEmbedEnabled.HasValue)
					b = c.SnippetsConfigList.IsOneKeySelectionEmbedEnabled;
			}
			if (b.HasValue)
				Scintilla.Snippets.IsOneKeySelectionEmbedEnabled = b.Value;

			char? defaultDelimeter = null;
			foreach (Configuration c in configList)
			{
				if (c.SnippetsConfigList.DefaultDelimeter.HasValue)
					defaultDelimeter = c.SnippetsConfigList.DefaultDelimeter;

			}
			if (!ch.HasValue)
				Scintilla.Snippets.DefaultDelimeter = '$';

			var snips = new SnippetList(null);
			foreach (Configuration c in configList)
			{
				if (c.SnippetsConfigList.Inherit.HasValue && !c.SnippetsConfigList.Inherit.Value)
					snips.Clear();

				foreach (SnippetsConfig sc in c.SnippetsConfigList)
				{
					if (snips.Contains(sc.Shortcut))
						snips.Remove(sc.Shortcut);

					Snippet snip;
					if (sc.Delimeter.HasValue)
						snip = snips.Add(sc.Shortcut, sc.Code, sc.Delimeter.Value);
					else
						snip = snips.Add(sc.Shortcut, sc.Code, Scintilla.Snippets.DefaultDelimeter);

					if (sc.IsSurroundsWith.HasValue)
						snip.IsSurroundsWith = sc.IsSurroundsWith.Value;
				}
			}

			SnippetList sl = Scintilla.Snippets.List;
			foreach (Snippet sc in snips)
			{
				if (sl.Contains(sc.Shortcut))
					sl.Remove(sc.Shortcut);

				sl.Add(sc.Shortcut, sc.Code, Scintilla.Snippets.DefaultDelimeter, sc.IsSurroundsWith);
			}

			sl.Sort();

			co = Color.Empty;
			foreach (Configuration c in configList)
			{
				if (c.SnippetsConfigList.ActiveSnippetColor != Color.Empty)
					co = c.SnippetsConfigList.ActiveSnippetColor;
			}
			if (co != Color.Empty)
				Scintilla.Snippets.ActiveSnippetColor = co;


			IndicatorStyle? indicatorStyle = null;
			foreach (Configuration c in configList)
			{
				if (c.SnippetsConfigList.ActiveSnippetIndicatorStyle.HasValue)
					indicatorStyle = c.SnippetsConfigList.ActiveSnippetIndicatorStyle;
			}
			if (indicatorStyle.HasValue)
				Scintilla.Snippets.ActiveSnippetIndicatorStyle = indicatorStyle.Value;


			i = null;
			foreach (Configuration c in configList)
			{
				if (c.SnippetsConfigList.ActiveSnippetIndicator.HasValue)
					i = c.SnippetsConfigList.ActiveSnippetIndicator;
			}
			if (i.HasValue)
				Scintilla.Snippets.ActiveSnippetIndicator = i.Value;


			co = Color.Empty;
			foreach (Configuration c in configList)
			{
				if (c.SnippetsConfigList.InactiveSnippetColor != Color.Empty)
					co = c.SnippetsConfigList.InactiveSnippetColor;

			}
			if (co != Color.Empty)
				Scintilla.Snippets.InactiveSnippetColor = co;


			i = null;
			foreach (Configuration c in configList)
			{
				if (c.SnippetsConfigList.InactiveSnippetIndicator.HasValue)
					i = c.SnippetsConfigList.InactiveSnippetIndicator;
			}
			if (i.HasValue)
				Scintilla.Snippets.InactiveSnippetIndicator = i.Value;


			IndicatorStyle? ics = null;
			foreach (Configuration c in configList)
			{
				if (c.SnippetsConfigList.ActiveSnippetIndicatorStyle.HasValue)
					ics = c.SnippetsConfigList.ActiveSnippetIndicatorStyle;
			}
			if (ics.HasValue)
				Scintilla.Snippets.ActiveSnippetIndicatorStyle = ics.Value;

			indicatorStyle = null;
			foreach (Configuration c in configList)
			{
				if (c.SnippetsConfigList.InactiveSnippetIndicatorStyle.HasValue)
					indicatorStyle = c.SnippetsConfigList.InactiveSnippetIndicatorStyle;
			}
			if (indicatorStyle.HasValue)
				Scintilla.Snippets.InactiveSnippetIndicatorStyle = indicatorStyle.Value;

			b = null;
			foreach (Configuration c in configList)
			{
				if (c.UndoRedoIsUndoEnabled.HasValue)
					b = c.UndoRedoIsUndoEnabled;
			}
			if (b.HasValue)
				Scintilla.UndoRedo.IsUndoEnabled = b.Value;

			co = Color.Empty;
			foreach (Configuration c in configList)
			{
				if (c.Whitespace_BackColor != Color.Empty)
					co = c.Whitespace_BackColor;

			}
			if (co != Color.Empty)
				Scintilla.Whitespace.BackColor = co;


			co = Color.Empty;
			foreach (Configuration c in configList)
			{
				if (c.Whitespace_ForeColor != Color.Empty)
					co = c.Whitespace_ForeColor;
			}
			if (co != Color.Empty)
				Scintilla.Whitespace.ForeColor = co;

			WhitespaceMode? wsm = null;
			foreach (Configuration c in configList)
			{
				if (c.Whitespace_Mode.HasValue)
					wsm = c.Whitespace_Mode;
			}
			if (wsm.HasValue)
				Scintilla.Whitespace.Mode = wsm.Value;


			//	OK so we saved the best for last instead of going in
			//	strict lexical order. Styles! This is really the section
			//	that people care about most in the config, and is also
			//	the most complex.
			if (this._clearStyles)
				Scintilla.Styles.Reset();

			i = null;
			foreach (Configuration c in configList)
			{
				if (c.Styles.Bits.HasValue)
					i = c.Styles.Bits;
			}

#pragma warning disable 618
			if (i.HasValue)
				Scintilla.Styles.Bits = i.Value;
#pragma warning restore 618

			Dictionary<string, int> styleNameMap = Scintilla.Lexing.StyleNameMap;
			var resolvedStyles = new ResolvedStyleList();

			int _unmappedStyleNumber = -1;
			var _unmappedStyleMap = new Dictionary<string, int>();
			foreach (Configuration c in configList)
			{
				if (c.Styles.Inherit.HasValue && !c.Styles.Inherit.Value)
					resolvedStyles.Clear();

				foreach (StyleConfig sc in c.Styles)
				{
					i = sc.Number;

					if (!i.HasValue)
					{
						if (!styleNameMap.ContainsKey(sc.Name))
						{
							if (_unmappedStyleMap.ContainsKey(sc.Name))
							{
								i = _unmappedStyleMap[sc.Name];
								sc.Number = i;
							}
							else
							{
								i = _unmappedStyleNumber--;
								sc.Number = i;

								_unmappedStyleMap[sc.Name] = sc.Number.Value;
							}
						}
						else
						{
							i = styleNameMap[sc.Name];
							sc.Number = i;
						}
					}

					StyleConfig baseStyleConfig = null;
					if (!string.IsNullOrEmpty(sc.Name) && sc.Name.Contains("."))
					{
						baseStyleConfig = resolvedStyles.FindByName(sc.Name.Substring(sc.Name.IndexOf(".") + 1));
					}

					if (!resolvedStyles.ContainsKey(i.Value) || (sc.Inherit.HasValue && !sc.Inherit.Value))
					{
						resolvedStyles.Remove(i.Value);
						resolvedStyles.Add(i.Value, sc);
					}

					StyleConfig rs = resolvedStyles[i.Value];

					if (sc.BackColor != Color.Empty)
						rs.BackColor = sc.BackColor;
					else if (baseStyleConfig != null && baseStyleConfig.BackColor != Color.Empty)
						rs.BackColor = baseStyleConfig.BackColor;

					if (sc.Bold.HasValue)
						rs.Bold = sc.Bold.Value;
					else if (baseStyleConfig != null && baseStyleConfig.Bold.HasValue)
						rs.Bold = baseStyleConfig.Bold.Value;

					if (sc.Case.HasValue)
						rs.Case = sc.Case.Value;
					else if (baseStyleConfig != null && baseStyleConfig.Case.HasValue)
						rs.Case = baseStyleConfig.Case.Value;

					if (sc.CharacterSet.HasValue)
						rs.CharacterSet = sc.CharacterSet.Value;
					else if (baseStyleConfig != null && baseStyleConfig.CharacterSet.HasValue)
						rs.CharacterSet = baseStyleConfig.CharacterSet.Value;

					if (sc.FontName != null)
						rs.FontName = sc.FontName;
					else if (baseStyleConfig != null && baseStyleConfig.FontName != null)
						rs.FontName = baseStyleConfig.FontName;

					if (sc.ForeColor != Color.Empty)
						rs.ForeColor = sc.ForeColor;
					else if (baseStyleConfig != null && baseStyleConfig.ForeColor != Color.Empty)
						rs.ForeColor = baseStyleConfig.ForeColor;

					if (sc.IsChangeable.HasValue)
						rs.IsChangeable = sc.IsChangeable.Value;
					else if (baseStyleConfig != null && baseStyleConfig.IsChangeable.HasValue)
						rs.IsChangeable = baseStyleConfig.IsChangeable.Value;

					if (sc.IsHotspot.HasValue)
						rs.IsHotspot = sc.IsHotspot.Value;
					else if (baseStyleConfig != null && baseStyleConfig.IsHotspot.HasValue)
						rs.IsHotspot = baseStyleConfig.IsHotspot.Value;

					if (sc.IsSelectionEolFilled.HasValue)
						rs.IsSelectionEolFilled = sc.IsSelectionEolFilled.Value;
					else if (baseStyleConfig != null && baseStyleConfig.IsSelectionEolFilled.HasValue)
						rs.IsSelectionEolFilled = baseStyleConfig.IsSelectionEolFilled.Value;

					if (sc.IsVisible.HasValue)
						rs.IsVisible = sc.IsVisible.Value;
					else if (baseStyleConfig != null && baseStyleConfig.IsVisible.HasValue)
						rs.IsVisible = baseStyleConfig.IsVisible.Value;

					if (sc.Italic.HasValue)
						rs.Italic = sc.Italic.Value;
					else if (baseStyleConfig != null && baseStyleConfig.Italic.HasValue)
						rs.Italic = baseStyleConfig.Italic.Value;

					if (sc.Size.HasValue)
						rs.Size = sc.Size.Value;
					else if (baseStyleConfig != null && baseStyleConfig.Size.HasValue)
						rs.Size = baseStyleConfig.Size.Value;

					if (sc.Underline.HasValue)
						rs.Underline = sc.Underline.Value;
					else if (baseStyleConfig != null && baseStyleConfig.Underline.HasValue)
						rs.Underline = baseStyleConfig.Underline.Value;
				}


			}
			//	If a Default styles exist we want them at the top of the list because
			//	it needs to be applied first, then StyleClearAll() called so that all
			//	other styles will "inherit" this style. Then the other styles will 
			//	override the default with any defined properties.
			var arr = new StyleConfig[resolvedStyles.Count];
			resolvedStyles.Values.CopyTo(arr, 0);
			Array.Sort(arr, delegate(StyleConfig sc1, StyleConfig sc2)
			{
				int v1 = sc1.Number.Value == Constants.STYLE_DEFAULT ? -1 : sc1.Number.Value;
				int v2 = sc2.Number.Value == Constants.STYLE_DEFAULT ? -1 : sc2.Number.Value;

				if (v1 < v2)
					return -1;
				else if (v2 < v1)
					return 1;

				return 0;
			});


			foreach (StyleConfig sc in arr)
			{
				if (sc.Number < 0)
					continue;

				Style style = Scintilla.Styles[sc.Number.Value];

				if (sc.BackColor != Color.Empty)
					style.BackColor = sc.BackColor;

				if (sc.Bold.HasValue)
					style.Bold = sc.Bold.Value;

				if (sc.Case.HasValue)
					style.Case = sc.Case.Value;

				if (sc.CharacterSet.HasValue)
					style.CharacterSet = sc.CharacterSet.Value;

				if (sc.FontName != null)
					style.FontName = sc.FontName;

				if (sc.ForeColor != Color.Empty)
					style.ForeColor = sc.ForeColor;

				if (sc.IsChangeable.HasValue)
					style.IsChangeable = sc.IsChangeable.Value;

				if (sc.IsHotspot.HasValue)
					style.IsHotspot = sc.IsHotspot.Value;

				if (sc.IsSelectionEolFilled.HasValue)
					style.IsSelectionEolFilled = sc.IsSelectionEolFilled.Value;

				if (sc.IsVisible.HasValue)
					style.IsVisible = sc.IsVisible.Value;

				if (sc.Italic.HasValue)
					style.Italic = sc.Italic.Value;

				if (sc.Size.HasValue)
					style.Size = sc.Size.Value;

				if (sc.Underline.HasValue)
					style.Underline = sc.Underline.Value;

				if (sc.Number == Constants.STYLE_DEFAULT)
					Scintilla.Styles.ClearAll();
			}
		}


		private string GetCustomConfigPath(string language)
		{
			string langPath = language;

			if (!string.IsNullOrEmpty(language))
			{
				//	First try the exact string given as a path
				if (!File.Exists(langPath))
				{
					//	Nope, well maybe its an absolute path to a folder.
					//	Add [language name].xml to the path and try that
					langPath = Path.Combine(this._customLocation, language + ".xml");

					if (!File.Exists(langPath))
					{
						//	Not that either. Now assume its a relative path with the
						//	path specified in the string
						string basePath = new FileInfo(Assembly.GetExecutingAssembly().Location).DirectoryName;
						langPath = Path.Combine(basePath, this._customLocation);

						if (!File.Exists(langPath))
						{
							//	OK This is the last try. Tack on the [language name].xml
							langPath = Path.Combine(langPath, language + ".xml");
							if (!File.Exists(langPath))
								return null;
						}
					}
				}
			}
			return langPath;
		}


		protected internal override void Initialize()
		{
			if (this._language != null)
				this.Configure();
		}


		private void ResetClearIndicators()
		{
			this._clearIndicators = false;
		}


		private void ResetClearKeyBindings()
		{
			this._clearKeyBindings = false;
		}


		private void ResetClearMargins()
		{
			this._clearMargins = true;
		}


		private void ResetClearMarkers()
		{
			this._clearMarkers = false;
		}


		private void ResetClearSnippets()
		{
			this._clearSnippets = false;
		}


		private void ResetClearStyles()
		{
			this._clearStyles = false;
		}


		private void ResetCustomLocation()
		{
			this._customLocation = string.Empty;
		}


		private void ResetIsBuiltInEnabled()
		{
			this._isBuiltInEnabled = true;
		}


		private void ResetIsUserEnabled()
		{
			this._isUserEnabled = true;
		}


		private void ResetLanguage()
		{
			this._language = null;
		}


		private void ResetLoadOrder()
		{
			this._loadOrder = ConfigurationLoadOrder.BuiltInCustomUser;
		}


		internal bool ShouldSerialize()
		{
			return this.ShouldSerializeClearKeyBindings() ||
				this.ShouldSerializeClearMargins() ||
				this.ShouldSerializeClearSnippets() ||
				this.ShouldSerializeClearStyles() ||
				this.ShouldSerializeCustomLocation() ||
				this.ShouldSerializeIsBuiltInEnabled() ||
				this.ShouldSerializeIsUserEnabled() ||
				this.ShouldSerializeLanguage() ||
				this.ShouldSerializeLoadOrder();
		}


		private bool ShouldSerializeClearIndicators()
		{
			return this._clearIndicators;
		}


		private bool ShouldSerializeClearKeyBindings()
		{
			return this._clearKeyBindings;
		}


		private bool ShouldSerializeClearMargins()
		{
			return this._clearMargins;
		}


		private bool ShouldSerializeClearMarkers()
		{
			return this._clearMarkers;
		}


		private bool ShouldSerializeClearSnippets()
		{
			return this._clearSnippets;
		}


		private bool ShouldSerializeClearStyles()
		{
			return this._clearStyles;
		}


		private bool ShouldSerializeCustomLocation()
		{
			return !string.IsNullOrEmpty(this._customLocation);
		}


		private bool ShouldSerializeIsBuiltInEnabled()
		{
			return !this._isBuiltInEnabled;
		}


		private bool ShouldSerializeIsUserEnabled()
		{
			return !this._isUserEnabled;
		}


		private bool ShouldSerializeLanguage()
		{
			return !string.IsNullOrEmpty(this._language);
		}


		private bool ShouldSerializeLoadOrder()
		{
			return this._loadOrder != ConfigurationLoadOrder.BuiltInCustomUser;
		}

		#endregion Methods


		#region Properties

		public bool ClearIndicators
		{
			get
			{
				return this._clearIndicators;
			}
			set
			{
				this._clearIndicators = value;
			}
		}


		public bool ClearKeyBindings
		{
			get
			{
				return this._clearKeyBindings;
			}
			set
			{
				this._clearKeyBindings = value;
			}
		}


		public bool ClearMargins
		{
			get
			{
				return this._clearMargins;
			}
			set
			{
				this._clearMargins = value;
			}
		}


		public bool ClearMarkers
		{
			get
			{
				return this._clearMarkers;
			}
			set
			{
				this._clearMarkers = value;
			}
		}


		public bool ClearSnippets
		{
			get
			{
				return this._clearSnippets;
			}
			set
			{
				this._clearSnippets = value;
			}
		}


		public bool ClearStyles
		{
			get
			{
				return this._clearStyles;
			}
			set
			{
				this._clearStyles = value;
			}
		}


		public string CustomLocation
		{
			get
			{
				return this._customLocation;
			}
			set
			{
				this._customLocation = value;
			}
		}


		public bool IsBuiltInEnabled
		{
			get
			{
				return this._isBuiltInEnabled;
			}
			set
			{
				this._isBuiltInEnabled = value;
			}
		}


		public bool IsUserEnabled
		{
			get
			{
				return this._isUserEnabled;
			}
			set
			{
				this._isUserEnabled = value;
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

				if (!Scintilla.IsDesignMode)
					this.Configure();
			}
		}


		public ConfigurationLoadOrder LoadOrder
		{
			get
			{
				return this._loadOrder;
			}
			set
			{
				this._loadOrder = value;
			}
		}


		private string UserFolder
		{
			get
			{
				if (this._appDataFolder == null)
					this._appDataFolder = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData);

				if (this._userFolder == null)
				{
					Version v = GetType().Assembly.GetName().Version;

					this._userFolder = Path.Combine(Path.Combine(this._appDataFolder, "ARCed.Scintilla"), v.Major.ToString() + "." + v.Minor.ToString());
				}

				return this._userFolder;
			}
		}


		[DefaultValue(true)]
		public bool UseXmlReader
		{
			get { return this._useXmlReader; }
			set
			{
				this._useXmlReader = value;
			}
		}

		#endregion Properties


		#region Constructors

		internal ConfigurationManager(Scintilla scintilla)
			: base(scintilla)
		{
		}

		#endregion Constructors
	}
}

