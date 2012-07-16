#region Using Directives

using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Drawing;
using System.Windows.Forms;
using ARCed.Controls;
using ARCed.Dialogs;
using ARCed.Helpers;
using ARCed.UI;

#endregion

namespace ARCed.Database
{
    /// <summary>
    /// Flags to specifiy what data structures need refreshed.
    /// </summary>
    [Flags]
	public enum RefreshType
	{
        /// <summary>
        /// Actor data needs refreshed flag.
        /// </summary>
		Actors,
        /// <summary>
        /// Class data needs refreshed flag.
        /// </summary>
		Classes,
        /// <summary>
        /// Skill data needs refreshed flag.
        /// </summary>
		Skills,
        /// <summary>
        /// Item data needs refreshed flag.
        /// </summary>
		Items,
        /// <summary>
        /// Weapon data needs refreshed flag.
        /// </summary>
		Weapons,
        /// <summary>
        /// Armor data needs refreshed flag.
        /// </summary>
		Armors,
        /// <summary>
        /// Enemy data needs refreshed flag.
        /// </summary>
		Enemies,
        /// <summary>
        /// Troop data needs refreshed flag.
        /// </summary>
		Troops,
        /// <summary>
        /// State data needs refreshed flag.
        /// </summary>
		States,
        /// <summary>
        /// Animation data needs refreshed flag.
        /// </summary>
		Animations,
        /// <summary>
        /// Tileset data needs refreshed flag.
        /// </summary>
		Tilesets,
        /// <summary>
        /// COmmon event data needs refreshed flag.
        /// </summary>
		CommonEvents,
        /// <summary>
        /// System data needs refreshed flag.
        /// </summary>
		System,
        /// <summary>
        /// Switch data needs refreshed flag.
        /// </summary>
		Switches,
        /// <summary>
        /// Variable data needs refreshed flag.
        /// </summary>
		Variables,
        /// <summary>
        /// Parameter data needs refreshed flag.
        /// </summary>
		Parameters,
        /// <summary>
        /// Equip kind data needs refreshed flag.
        /// </summary>
		EquipKinds,
        /// <summary>
        /// Element data needs refreshed flag.
        /// </summary>
		Elements,
        /// <summary>
        /// Scope data needs refreshed flag.
        /// </summary>
		Scopes,
        /// <summary>
        /// Occasion data needs refreshed flag.
        /// </summary>
		Occasions
	}

    /// <summary>
    /// Base class for database forms.
    /// </summary>
	public class DatabaseWindow : DockContent
    {
        #region Private Fields

        private Image _imageIcon;
		private Type _rpgType;

        #endregion

        /// <summary>
		/// Flag if control changing should cause events to be raised.
		/// </summary>
		protected bool SuppressEvents;
		/// <summary>
		/// Gets the instance of the windows DatabaseObjectListBox or null if there is not one.
		/// </summary>
		protected virtual DatabaseObjectListBox DataObjectList { get { return null; } }
		/// <summary>
		/// Gets the project game data associated with this window.
		/// </summary>
		[Browsable(false)]
		public virtual List<dynamic> Data { get { return null; } }
		/// <summary>
		/// Gets the game object type the window is associated with.
		/// </summary>
		[Browsable(false)]
		public Type RpgType
		{
			get
			{
			    if (String.IsNullOrEmpty(RpgTypeName))
					return null;
			    return this._rpgType ?? (this._rpgType = Util.ARCedAssembly.GetType(this.RpgTypeName));
			}
		}
		/// <summary>
		/// Gets or sets the name of the window's associated game object type. 
		/// </summary>
		/// <remarks>Once set, changing this value has no effect.</remarks>
		[Category("ARCed"), Description("Defines the name of the window's associated game object type.")]
		public string RpgTypeName { get; set; }

		/*
		/// <summary>
		/// Gets or sets the windows icon from a Bitmap.
		/// </summary>
		[Category("ARCed"), Description("Defines the windows icon from a Bitmap.")]
		public Image ImageIcon
		{
			get { return _imageIcon; }
			set { SetWindowIcon(value); }
		}
		 */

		/// <summary>
		/// Default constructor
		/// </summary>
		public DatabaseWindow()
		{
			Load += this.DatabaseWindowLoad;
			FormClosing += this.DatabaseWindowFormClosing;
			DefaultFloatSize = new Size(800, 600);
			ShowHint = DockState.Document;
		}

		/// <summary>
		/// Refreshes the header _srcTexture
		/// </summary>
		public void RefreshHeader()
		{
			DataObjectList.RefreshHeader();
		}

        /// <summary>
        /// Refreshes the current game object selected
        /// </summary>
        /// <exception cref="NotImplementedException">Thrown when method has not been overridden.</exception>
        /// <remarks>This method must be overridden in inherited classes</remarks>
        public virtual void RefreshCurrentObject() 
		{
            throw new NotImplementedException("Method needs to be overridden in inherited classes.");
		}

		/// <summary>
		/// Refreshes the list of game objects
		/// </summary>
		public virtual void RefreshObjectList()
		{
			if (Data != null && DataObjectList != null)
				DataObjectList.PopulateList(Data);
		}

		/// <summary>
		/// Sets the form's icon using the given Bitmap object.
		/// </summary>
		/// <param name="image">Bitmap to create Icon from.</param>
		public virtual void SetWindowIcon(Image image)
		{
			_imageIcon = image;
			Icon = Icon.FromHandle(((Bitmap)image).GetHicon());
		}

		/// <summary>
		/// Registers the window when it is loaded
		/// </summary>
		/// <param name="sender">Invoker of the event</param>
		/// <param name="e">Event arguments</param>
		private void DatabaseWindowLoad(object sender, EventArgs e)
		{
			if (!Windows.DatabaseForms.Contains(this))
				Windows.DatabaseForms.Add(this);
			if (DataObjectList != null)
			{
				DataObjectList.OnButtonMaxClick += (s, ev) => this.ChangeCapacity();
			}
		}

		/// <summary>
		/// Unregisters the window when it is closed
		/// </summary>
		/// <param name="sender">Invoker of the event</param>
		/// <param name="e">Event arguments</param>
		private void DatabaseWindowFormClosing(object sender, FormClosingEventArgs e)
		{
			if (Windows.DatabaseForms.Contains(this))
				Windows.DatabaseForms.Remove(this);
		}

		/// <summary>
		/// Changes the capcity of the given game object collection.
		/// </summary>
		protected void ChangeCapacity()
		{
			if (RpgType == null || DataObjectList == null)
				return;
			var current = Data.Count - 1;
			var max = current;
			using (var dialog = new ChangeMaxDialog(current, 1, 9999))
			{
				if (dialog.ShowDialog() == DialogResult.OK)
					max = dialog.MaxValue;
			}
			if (current == max)
				return;
			var listBoxGeneration = GC.GetGeneration(DataObjectList);
			var listGeneration = GC.GetGeneration(Data);
			var index = DataObjectList.SelectedIndex;
			if (current > max)
				Data.RemoveRange(max + 1, current - max);
			else if (current < max)
			{
				for (int i = current; i < max; i++)
				{
					dynamic obj = Activator.CreateInstance(RpgType);
					obj.id = i + 1;
					Data.Add(obj);
				}
			}
			DataObjectList.PopulateList(Data);
			DataObjectList.SelectedIndex = index.Clamp(0, DataObjectList.Items.Count - 1);
			GC.Collect(listGeneration, GCCollectionMode.Forced);
			GC.Collect(listBoxGeneration, GCCollectionMode.Forced);
		}

        /// <summary>
        /// Refreshes objects by type flag
        /// </summary>
        /// <param name="type">Flag for type of object to refresh</param>
        /// <exception cref="NotImplementedException">Thrown when method is not overridden.</exception>
        /// <remarks>This methods is to be overridden in inherited classes.</remarks>
        /// <exception cref="System.NotImplementedException">Thrown when method is not overridden in inherited class</exception>
        public virtual void NotifyRefresh(RefreshType type)
		{
			throw new NotImplementedException("Method needs to be overridden in inherited classes.");
		}
	}
}
