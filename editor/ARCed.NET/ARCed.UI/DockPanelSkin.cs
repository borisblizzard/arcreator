#region Using Directives

using System;
using System.ComponentModel;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.Globalization;
using System.Xml.Serialization;
using ARCed.Core;

#endregion

namespace ARCed.UI
{
    #region DockPanelSkin classes
    /// <summary>
    /// The skin to use when displaying the DockPanel.
    /// The skin allows custom gradient color schemes to be used when drawing the
    /// DockStrips and Tabs.
    /// </summary>
    [TypeConverter(typeof(DockPanelSkinConverter))]
	[Serializable]
    public class DockPanelSkin
    {
        private AutoHideStripSkin _mAutoHideStripSkin;
        private DockPaneStripSkin _mDockPaneStripSkin;

        public DockPanelSkin()
        {
            this._mAutoHideStripSkin = new AutoHideStripSkin();
            this._mDockPaneStripSkin = new DockPaneStripSkin();
        }

        /// <summary>
        /// The skin used to display the auto hide strips and tabs.
        /// </summary>
        public AutoHideStripSkin AutoHideStripSkin
        {
            get { return this._mAutoHideStripSkin; }
            set { this._mAutoHideStripSkin = value; }
        }

        /// <summary>
        /// The skin used to display the Document and ToolWindow style DockStrips and Tabs.
        /// </summary>
        public DockPaneStripSkin DockPaneStripSkin
        {
            get { return this._mDockPaneStripSkin; }
            set { this._mDockPaneStripSkin = value; }
        }
    }

    /// <summary>
    /// The skin used to display the auto hide strip and tabs.
    /// </summary>
    [TypeConverter(typeof(AutoHideStripConverter))]
	[Serializable]
    public class AutoHideStripSkin
    {
        private DockPanelGradient _mDockStripGradient;
        private TabGradient _mTabGradient;
        private Font _mTextFont;

        public AutoHideStripSkin()
        {
            this._mDockStripGradient = new DockPanelGradient
            {
                StartColor = SystemColors.ControlLight,
                EndColor = SystemColors.ControlLight
            };

            this._mTabGradient = new TabGradient
            {
                TextColor = SystemColors.ControlDarkDark
            };

            this._mTextFont = SystemFonts.MenuFont;
        }

        /// <summary>
        /// The gradient color skin for the DockStrips.
        /// </summary>
        public DockPanelGradient DockStripGradient
        {
            get { return this._mDockStripGradient; }
            set { this._mDockStripGradient = value; }
        }

        /// <summary>
        /// The gradient color skin for the Tabs.
        /// </summary>
        public TabGradient TabGradient
        {
            get { return this._mTabGradient; }
            set { this._mTabGradient = value; }
        }

		/// <summary>
		/// The serializable version of the font used in AutoHideStrip elements
		/// </summary>
		[XmlElement("TextFont")]
		public SerializableFont SerializedTextFont
		{
			get { return this._mTextFont; }
			set { this._mTextFont = value; }
		}

        /// <summary>
        /// Font used in AutoHideStrip elements.
        /// </summary>
		[XmlIgnore]
        public Font TextFont
        {
            get { return this._mTextFont; }
            set { this._mTextFont = value; }
        }
    }

    /// <summary>
    /// The skin used to display the document and tool strips and tabs.
    /// </summary>
    [TypeConverter(typeof(DockPaneStripConverter))]
	[Serializable]
    public class DockPaneStripSkin
    {
        private DockPaneStripGradient _mDocumentGradient;
        private DockPaneStripToolWindowGradient _mToolWindowGradient;
        private Font _mTextFont;

        public DockPaneStripSkin()
        {
            this._mDocumentGradient = new DockPaneStripGradient
            {
                DockStripGradient =
                {
                    StartColor = SystemColors.Control,
                    EndColor = SystemColors.Control
                },
                ActiveTabGradient =
                {
                    StartColor = SystemColors.ControlLightLight,
                    EndColor = SystemColors.ControlLightLight
                },
                InactiveTabGradient =
                {
                    StartColor = SystemColors.ControlLight,
                    EndColor = SystemColors.ControlLight
                }
            };

            this._mToolWindowGradient = new DockPaneStripToolWindowGradient
            {
                DockStripGradient =
                {
                    StartColor = SystemColors.ControlLight,
                    EndColor = SystemColors.ControlLight
                },
                ActiveTabGradient =
                {
                    StartColor = SystemColors.Control,
                    EndColor = SystemColors.Control
                },
                InactiveTabGradient =
                {
                    StartColor = Color.Transparent,
                    EndColor = Color.Transparent,
                    TextColor = SystemColors.ControlDarkDark
                },
                ActiveCaptionGradient =
                {
                    StartColor = SystemColors.GradientActiveCaption,
                    EndColor = SystemColors.ActiveCaption,
                    LinearGradientMode = LinearGradientMode.Vertical,
                    TextColor = SystemColors.ActiveCaptionText
                },
                InactiveCaptionGradient =
                {
                    StartColor = SystemColors.GradientInactiveCaption,
                    EndColor = SystemColors.InactiveCaption,
                    LinearGradientMode = LinearGradientMode.Vertical,
                    TextColor = SystemColors.InactiveCaptionText
                }
            };

            this._mTextFont = SystemFonts.MenuFont;
        }

        /// <summary>
        /// The skin used to display the Document style DockPane strip and tab.
        /// </summary>
        public DockPaneStripGradient DocumentGradient
        {
            get { return this._mDocumentGradient; }
            set { this._mDocumentGradient = value; }
        }

        /// <summary>
        /// The skin used to display the ToolWindow style DockPane strip and tab.
        /// </summary>
        public DockPaneStripToolWindowGradient ToolWindowGradient
        {
            get { return this._mToolWindowGradient; }
            set { this._mToolWindowGradient = value; }
        }

		/// <summary>
		/// The serializable version of the font used in DockPaneStrip elements
		/// </summary>
		[XmlElement("TextFont")]
		public SerializableFont SerializedTextFont
		{
			get { return this._mTextFont; }
			set { this._mTextFont = value; }
		}

        /// <summary>
        /// Font used in DockPaneStrip elements.
        /// </summary>
		[XmlIgnore]
        public Font TextFont
        {
            get { return this._mTextFont; }
            set { this._mTextFont = value; }
        }
    }

    /// <summary>
    /// The skin used to display the DockPane ToolWindow strip and tab.
    /// </summary>
    [TypeConverter(typeof(DockPaneStripGradientConverter))]
	[Serializable]
    public class DockPaneStripToolWindowGradient : DockPaneStripGradient
    {
        private TabGradient _mActiveCaptionGradient;
        private TabGradient _mInactiveCaptionGradient;

        public DockPaneStripToolWindowGradient()
        {
            this._mActiveCaptionGradient = new TabGradient();
            this._mInactiveCaptionGradient = new TabGradient();
        }

        /// <summary>
        /// The skin used to display the active ToolWindow caption.
        /// </summary>
        public TabGradient ActiveCaptionGradient
        {
            get { return this._mActiveCaptionGradient; }
            set { this._mActiveCaptionGradient = value; }
        }

        /// <summary>
        /// The skin used to display the inactive ToolWindow caption.
        /// </summary>
        public TabGradient InactiveCaptionGradient
        {
            get { return this._mInactiveCaptionGradient; }
            set { this._mInactiveCaptionGradient = value; }
        }
    }

    /// <summary>
    /// The skin used to display the DockPane strip and tab.
    /// </summary>
    [TypeConverter(typeof(DockPaneStripGradientConverter))]
	[Serializable]
    public class DockPaneStripGradient
    {
        private DockPanelGradient _mDockStripGradient;
        private TabGradient _mActiveTabGradient;
        private TabGradient _mInactiveTabGradient;

        public DockPaneStripGradient()
        {
            this._mDockStripGradient = new DockPanelGradient();
            this._mActiveTabGradient = new TabGradient();
            this._mInactiveTabGradient = new TabGradient();
        }

        /// <summary>
        /// The gradient color skin for the DockStrip.
        /// </summary>
        public DockPanelGradient DockStripGradient
        {
            get { return this._mDockStripGradient; }
            set { this._mDockStripGradient = value; }
        }

        /// <summary>
        /// The skin used to display the active DockPane tabs.
        /// </summary>
        public TabGradient ActiveTabGradient
        {
            get { return this._mActiveTabGradient; }
            set { this._mActiveTabGradient = value; }
        }

        /// <summary>
        /// The skin used to display the inactive DockPane tabs.
        /// </summary>
        public TabGradient InactiveTabGradient
        {
            get { return this._mInactiveTabGradient; }
            set { this._mInactiveTabGradient = value; }
        }
    }

    /// <summary>
    /// The skin used to display the dock pane tab
    /// </summary>
    [TypeConverter(typeof(DockPaneTabGradientConverter))]
	[Serializable]
    public class TabGradient : DockPanelGradient
    {
        private Color _mTextColor;

        public TabGradient()
        {
            this._mTextColor = SystemColors.ControlText;
        }

		/// <summary>
		/// The serializable text color.
		/// </summary>
		[XmlElement("TextColor")]
		public string SerializedTextColor
		{
			get { return ColorTranslator.ToHtml(this._mTextColor); }
			set { this._mTextColor = ColorTranslator.FromHtml(value); }
		}

        /// <summary>
        /// The text color.
        /// </summary>
        [DefaultValue(typeof(SystemColors), "ControlText")]
		[XmlIgnore]
        public Color TextColor
        {
            get { return this._mTextColor; }
            set { this._mTextColor = value; }
        }
    }

    /// <summary>
    /// The gradient color skin.
    /// </summary>
    [TypeConverter(typeof(DockPanelGradientConverter))]
	[Serializable]
    public class DockPanelGradient
    {
        private Color _mStartColor;
        private Color _mEndColor;
        private LinearGradientMode _mLinearGradientMode;

        public DockPanelGradient()
        {
            this._mStartColor = SystemColors.Control;
            this._mEndColor = SystemColors.Control;
            this._mLinearGradientMode = LinearGradientMode.Horizontal;
        }

		/// <summary>
		/// The serializable beginning gradient color.
		/// </summary>
		[XmlElement("StartColor")]
		public string SerializedStartColor
		{
			get { return ColorTranslator.ToHtml(this._mStartColor); }
			set { this._mStartColor = ColorTranslator.FromHtml(value); }
		}

        /// <summary>
        /// The beginning gradient color.
        /// </summary>
        [DefaultValue(typeof(SystemColors), "Control")]
		[XmlIgnore]
        public Color StartColor
        {
            get { return this._mStartColor; }
            set { this._mStartColor = value; }
        }

		/// <summary>
		/// The serializable end gradient color.
		/// </summary>
		[XmlElement("EndColor")]
		public string SerializedEndColor
		{
			get { return ColorTranslator.ToHtml(this._mEndColor); }
			set { this._mEndColor = ColorTranslator.FromHtml(value); }
		}

        /// <summary>
        /// The ending gradient color.
        /// </summary>
        [DefaultValue(typeof(SystemColors), "Control")]
		[XmlIgnore]
        public Color EndColor
        {
            get { return this._mEndColor; }
            set { this._mEndColor = value; }
        }

		/// <summary>
		/// The serializable gradient mode to display the colors.
		/// </summary>
		[XmlElement("LinearGradientMode")]
		public int SerializedLinearGradientMode
		{
			get { return (int)this._mLinearGradientMode; }
			set { this._mLinearGradientMode = (LinearGradientMode)value; }
		}

        /// <summary>
        /// The gradient mode to display the colors.
        /// </summary>
        [DefaultValue(LinearGradientMode.Horizontal)]
		[XmlIgnore]
        public LinearGradientMode LinearGradientMode
        {
            get { return this._mLinearGradientMode; }
            set { this._mLinearGradientMode = value; }
        }
    }

    #endregion

    #region Converters
	[Serializable]
    public class DockPanelSkinConverter : ExpandableObjectConverter
    {
        public override bool CanConvertTo(ITypeDescriptorContext context, Type destinationType)
        {
            if (destinationType == typeof(DockPanelSkin))
                return true;

            return base.CanConvertTo(context, destinationType);
        }

        public override object ConvertTo(ITypeDescriptorContext context, CultureInfo culture, object value, Type destinationType)
        {
            if (destinationType == typeof(String) && value is DockPanelSkin)
            {
                return "DockPanelSkin";
            }
            return base.ConvertTo(context, culture, value, destinationType);
        }
    }

	[Serializable]
    public class DockPanelGradientConverter : ExpandableObjectConverter
    {
        public override bool CanConvertTo(ITypeDescriptorContext context, Type destinationType)
        {
            if (destinationType == typeof(DockPanelGradient))
                return true;

            return base.CanConvertTo(context, destinationType);
        }

        public override object ConvertTo(ITypeDescriptorContext context, CultureInfo culture, object value, Type destinationType)
        {
            if (destinationType == typeof(String) && value is DockPanelGradient)
            {
                return "DockPanelGradient";
            }
            return base.ConvertTo(context, culture, value, destinationType);
        }
    }

	[Serializable]
    public class AutoHideStripConverter : ExpandableObjectConverter
    {
        public override bool CanConvertTo(ITypeDescriptorContext context, Type destinationType)
        {
            if (destinationType == typeof(AutoHideStripSkin))
                return true;

            return base.CanConvertTo(context, destinationType);
        }

        public override object ConvertTo(ITypeDescriptorContext context, CultureInfo culture, object value, Type destinationType)
        {
            if (destinationType == typeof(String) && value is AutoHideStripSkin)
            {
                return "AutoHideStripSkin";
            }
            return base.ConvertTo(context, culture, value, destinationType);
        }
    }

	[Serializable]
    public class DockPaneStripConverter : ExpandableObjectConverter
    {
        public override bool CanConvertTo(ITypeDescriptorContext context, Type destinationType)
        {
            if (destinationType == typeof(DockPaneStripSkin))
                return true;

            return base.CanConvertTo(context, destinationType);
        }

        public override object ConvertTo(ITypeDescriptorContext context, CultureInfo culture, object value, Type destinationType)
        {
            if (destinationType == typeof(String) && value is DockPaneStripSkin)
            {
                return "DockPaneStripSkin";
            }
            return base.ConvertTo(context, culture, value, destinationType);
        }
    }

	[Serializable]
    public class DockPaneStripGradientConverter : ExpandableObjectConverter
    {
        public override bool CanConvertTo(ITypeDescriptorContext context, Type destinationType)
        {
            if (destinationType == typeof(DockPaneStripGradient))
                return true;

            return base.CanConvertTo(context, destinationType);
        }

        public override object ConvertTo(ITypeDescriptorContext context, CultureInfo culture, object value, Type destinationType)
        {
            if (destinationType == typeof(String) && value is DockPaneStripGradient)
            {
                return "DockPaneStripGradient";
            }
            return base.ConvertTo(context, culture, value, destinationType);
        }
    }

	[Serializable]
    public class DockPaneTabGradientConverter : ExpandableObjectConverter
    {
        public override bool CanConvertTo(ITypeDescriptorContext context, Type destinationType)
        {
            if (destinationType == typeof(TabGradient))
                return true;

            return base.CanConvertTo(context, destinationType);
        }

        public override object ConvertTo(ITypeDescriptorContext context, CultureInfo culture, object value, Type destinationType)
        {
            if (destinationType == typeof(String) && value is TabGradient)
            {
                return "DockPaneTabGradient";
            }
            return base.ConvertTo(context, culture, value, destinationType);
        }
    }
    #endregion
}