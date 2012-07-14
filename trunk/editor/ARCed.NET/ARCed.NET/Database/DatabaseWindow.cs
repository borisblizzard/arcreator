using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Windows.Forms;
using ARCed.Controls;
using ARCed.Dialogs;
using ARCed.Helpers;
using System.Drawing;
using ARCed.UI;

namespace ARCed.Database
{
	public enum RefreshType
	{
		Actors,
		Classes,
		Skills,
		Items,
		Weapons,
		Armors,
		Enemies,
		Troops,
		States,
		Animations,
		Tilesets,
		CommonEvents,
		System,
		Switches,
		Variables,
		Parameters,
		EquipKinds,
		Elements,
		Scopes,
		Occasions
	}

	public class DatabaseWindow : DockContent
	{
		private Image _imageIcon;
		private Type _rpgType;
		/// <summary>
		/// Flag if control changing should cause events to be raised.
		/// </summary>
		protected bool suppressEvents;

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
				if (_rpgType == null)
					_rpgType = Util.ARCedAssembly.GetType(RpgTypeName);
				return _rpgType;
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
		public DatabaseWindow() : base()
		{
			Load += new EventHandler(DatabaseWindow_Load);
			FormClosing += new System.Windows.Forms.FormClosingEventHandler(DatabaseWindow_FormClosing);
			this.DefaultFloatSize = new System.Drawing.Size(800, 600);
			this.ShowHint = UI.DockState.Document;
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
		/// <remarks>This method must be overridden in inherited classes</remarks>
		public virtual void RefreshCurrentObject() 
		{
			throw new NotImplementedException();
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
		public virtual void SetWindowIcon(System.Drawing.Image image)
		{
			_imageIcon = image;
			this.Icon = Icon.FromHandle((image as Bitmap).GetHicon());
		}

		/// <summary>
		/// Registers the window when it is loaded
		/// </summary>
		/// <param name="sender">Invoker of the event</param>
		/// <param name="e">Event arguments</param>
		private void DatabaseWindow_Load(object sender, EventArgs e)
		{
			if (!Windows.DatabaseForms.Contains(this))
				Windows.DatabaseForms.Add(this);
			if (DataObjectList != null)
			{
				DataObjectList.OnButtonMaxClick += (s, ev) => { ChangeCapacity(); };
			}
		}

		/// <summary>
		/// Unregisters the window when it is closed
		/// </summary>
		/// <param name="sender">Invoker of the event</param>
		/// <param name="e">Event arguments</param>
		private void DatabaseWindow_FormClosing(object sender, System.Windows.Forms.FormClosingEventArgs e)
		{
			if (Windows.DatabaseForms.Contains(this))
				Windows.DatabaseForms.Remove(this);
		}

		/// <summary>
		/// Changes the capcity of the given game object collection.
		/// </summary>
		/// <typeparam name="T">Type of items the collection contains</typeparam>
		/// <param name="list">Instance of the collection</param>
		protected void ChangeCapacity()
		{
			if (RpgType == null || DataObjectList == null)
				return;
			int current = Data.Count - 1;
			int max = current;
			using (ChangeMaxDialog dialog = new ChangeMaxDialog(current, 1, 9999))
			{
				if (dialog.ShowDialog() == DialogResult.OK)
					max = dialog.MaxValue;
			}
			if (current == max)
				return;
			int listBoxGeneration = GC.GetGeneration(DataObjectList);
			int listGeneration = GC.GetGeneration(Data);
			int index = DataObjectList.SelectedIndex;
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
		/// <remarks>This methods is to be overridden in inherited classes.</remarks>
		/// <exception cref="System.NotImplementedException">Thrown when method is not overridden in inherited class</exception>
		public virtual void NotifyRefresh(RefreshType type)
		{
			throw new NotImplementedException("Method needs to be overridden in inherited classes.");
		}
	}
}
