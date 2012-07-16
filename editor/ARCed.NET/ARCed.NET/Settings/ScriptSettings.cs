#region Using Directives

using System;
using System.Collections.Generic;
using System.Drawing;
using System.Xml.Serialization;
using ARCed.Helpers;
using ARCed.Scripting;

#endregion

namespace ARCed.Settings
{
	[Serializable]
	public class ScriptSettings
	{
		/// <summary>
		/// Gets or sets the flag if autocomplete is used
		/// </summary>
		public bool AutoComplete { get; set; }
		/// <summary>
		/// Gets or sets the number of characters needed to begin autocomplete
		/// </summary>
		public int AutoCompleteLength { get; set; }
		/// <summary>
		/// Gets or sets the auto-complete flag.
		/// </summary>
		public int AutoCompleteFlag { get; set; }
		/// <summary>
		/// Gets or sets the list of autocomplete words
		/// </summary>
		public List<string> AutoCompleteWords { get; set; }
		/// <summary>
		/// Gets or sets the flag to use auto-indentation
		/// </summary>
		public bool AutoIndent { get; set; }
		/// <summary>
		/// Gets or sets the flag to use column guidelines
		/// </summary>
		public bool GuideLines { get; set; }
		/// <summary>
		/// Gets or sets the flag to use the caret marker
		/// </summary>
		public bool Caret { get; set; }
		/// <summary>
		/// Gets or sets the color used for the caret
		/// </summary>
		[XmlIgnore]
		public Color CaretColor { get; set; }
		/// <summary>
		/// Gets or sets the caret color using an Html formatted color string
		/// </summary>
		[XmlElement("CaretColor")]
		public string CaretColorHtml
		{
			get 
			{
				string color = ColorTranslator.ToHtml(CaretColor);
				return color.Insert(1, CaretColor.A.ToString("X"));
			}
			set { CaretColor = ColorTranslator.FromHtml(value); }
		}
		/// <summary>
		/// Gets or sets the flag to use code folding
		/// </summary>
		public bool CodeFolding { get; set; }
		/// <summary>
		/// Gets or sets the array of script styles
		/// </summary>
		public ScriptStyle[] ScriptStyles { get; set; }
		/// <summary>
		/// Gets or sets the string of characters that accept autocomplete when pressed
		/// </summary>
		public string FillUpCharacters { get; set; }

		/// <summary>
		/// Default constructor
		/// </summary>
		public ScriptSettings()
		{
			AutoComplete = true;
			AutoCompleteLength = 2;
			AutoCompleteFlag = 0;
			AutoCompleteWords = new List<string>();
			AutoIndent = true;
			GuideLines = true;
			Caret = false;
			CaretColor = Color.FromArgb(32, 0, 0, 0);
			ScriptStyles = DefaultStyles;
			FillUpCharacters = " )]}.";
		}

		/// <summary>
		/// Gets the array of script styles created internally as the default
		/// </summary>
		public static ScriptStyle[] DefaultStyles
		{
			get
			{
			    Font font;
				if (FontHelper.IsInstalled("Consolas"))
					font = new Font("Consolas", 10.25f, FontStyle.Regular);
				else
					font = FontHelper.MonoFont;
				var styles = new[] {
				    new ScriptStyle("White Space"        , Color.Black          , Color.White   , font),
				    new ScriptStyle("Brace Match"        , Color.Purple         , Color.Yellow  , font),
				    new ScriptStyle("Comment Line"       , Color.Green          , Color.White   , font),
				    new ScriptStyle("Comment Block"      , Color.Green          , Color.White   , font),
				    new ScriptStyle("Number"             , Color.DarkRed        , Color.White   , font),
				    new ScriptStyle("Keyword"            , Color.Blue           , Color.White   , font),
				    new ScriptStyle("Double Quote String", Color.Purple         , Color.White   , font),
				    new ScriptStyle("Single Quote String", Color.MediumVioletRed, Color.White   , font),
				    new ScriptStyle("Class Name"         , Color.DarkViolet     , Color.White   , font),
				    new ScriptStyle("Method Name"        , Color.Black          , Color.White   , font),
				    new ScriptStyle("Operator"           , Color.DarkCyan       , Color.White   , font),
				    new ScriptStyle("Call"               , Color.Black          , Color.White   , font),
				    new ScriptStyle("Regular Expression" , Color.MediumPurple   , Color.White   , font),
				    new ScriptStyle("Global Variable"    , Color.Black          , Color.White   , font),
				    new ScriptStyle("Symbol"             , Color.Black          , Color.White   , font),
				    new ScriptStyle("Module Name"        , Color.DarkViolet     , Color.White   , font),
				    new ScriptStyle("Instance Variable"  , Color.Black          , Color.White   , font),
				    new ScriptStyle("Class Variable"     , Color.Black          , Color.White   , font),
				    new ScriptStyle("System String"      , Color.Red            , Color.White   , font),
				    new ScriptStyle("Line Number"        , Color.Black          , Color.Lavender, font)
				};
				styles[8].Font = styles[15].Font = new Font(font, FontStyle.Bold);
				styles[19].Font = new Font(font.FontFamily, 8.25f, FontStyle.Regular);
				font.Dispose();
				return styles;
			}
		}
	}
}


