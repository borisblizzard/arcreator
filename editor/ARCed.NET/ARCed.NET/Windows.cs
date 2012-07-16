#region Using Directives

using System;
using System.Collections.Generic;
using System.Linq;
using System.Windows.Forms;
using ARCed.Database;
using ARCed.Database.Actors;
using ARCed.Forms;
using ARCed.Scintilla;
using ARCed.Scripting;

#endregion

namespace ARCed // INCOMPLETE
{
	/// <summary>
	/// Static class for getting editor windows. The windows are static properties that 
	/// will create the window if it does not exist and is referenced. 
	/// </summary>
	public static class Windows
	{
		#region Private Fields

		private static ARChiveForm _arcHiveForm;
		private static ScriptMenuForm _scriptMenu;
		private static ScriptStyleForm _scriptStyleForm;
		private static EditorOptionsForm _editorOptionsForm;
		private static List<ScriptEditorForm> _scriptEditors;
		private static List<DatabaseWindow> _databaseForms;
		private static SkinSettingsForm _skinSettingsForm;
		private static AutoCompleteForm _autoCompleteForm;
		private static ScriptSearchForm _scriptSearchForm;
		private static CalculatorForm _calculatorForm;
		private static FindReplaceDialog _scriptFindReplaceForm;
		private static ChartSettingsForm _chartSettingsForm;

		#endregion

		/// <summary>
		/// Disposes all loaded windows
		/// </summary>
		public static void DisposeAll()
		{
			Form[] contents = { _arcHiveForm, _scriptMenu, 
				_scriptStyleForm, _editorOptionsForm, _skinSettingsForm,
				_autoCompleteForm, _scriptSearchForm, _calculatorForm,
				_scriptFindReplaceForm, _chartSettingsForm
			};
			contents = (Form[])contents.Concat(_scriptEditors);
			foreach (Form content in contents)
			{
				if (content != null && !content.IsDisposed)
					content.Dispose();
			}
		}

		#region Windows

		/// <summary>
		/// Gets the instance of the chart form used for editing actor parameters.
		/// </summary>
		public static ChartSettingsForm ChartSettingsForm
		{
			get 
			{
				if (_chartSettingsForm == null || _chartSettingsForm.IsDisposed)
					_chartSettingsForm = new ChartSettingsForm();
				return _chartSettingsForm;
			}
		}

		/// <summary>
		/// Gets the instance of the Editor's ARChive Utility form.
		/// </summary>
		public static ARChiveForm ARChiveForm
		{
			get
			{
				if (_arcHiveForm == null || _arcHiveForm.IsDisposed)
					_arcHiveForm = new ARChiveForm();
				return _arcHiveForm;
			}
		}

		/// <summary>
		/// Gets the instance of the Editor's Script Menu form.
		/// </summary>
		public static ScriptMenuForm ScriptMenu
		{
			get
			{
				if (_scriptMenu == null || _scriptMenu.IsDisposed)
					_scriptMenu = new ScriptMenuForm();
				return _scriptMenu;
			}
			set { _scriptMenu = value; }
		}

		/// <summary>
		/// Gets the instance of the Editor's Script Style Menu form.
		/// </summary>
		public static ScriptStyleForm ScriptStyleMenu
		{
			get
			{
				if (_scriptStyleForm == null || _scriptStyleForm.IsDisposed)
					_scriptStyleForm = new ScriptStyleForm();
				return _scriptStyleForm;
			}
			set { _scriptStyleForm = value; }
		}

		/// <summary>
		/// Gets the instance of the Editor's Options Menu form.
		/// </summary>
		public static EditorOptionsForm EditorOptionsMenu
		{
			get
			{
				if (_editorOptionsForm == null || _editorOptionsForm.IsDisposed)
					_editorOptionsForm = new EditorOptionsForm();
				return _editorOptionsForm;
			}
			set { _editorOptionsForm = value; }
		}

		/// <summary>
		/// Gets a list of all script editor forms open in the editor
		/// </summary>
		public static List<ScriptEditorForm> ScriptEditors
		{
			get
			{
				if (_scriptEditors == null)
					_scriptEditors = new List<ScriptEditorForm>();
				return _scriptEditors;
			}
		}

		/// <summary>
		/// Gets all instances of database related forms
		/// </summary>
		public static List<DatabaseWindow> DatabaseForms
		{
			get
			{
				if (_databaseForms == null)
					_databaseForms = new List<DatabaseWindow>();
				return _databaseForms;
			}
			set { _databaseForms = value; }
		}

		/// <summary>
		/// Returns the static Find and Replace window used for scripts
		/// </summary>
		public static FindReplaceDialog ScintillaFindReplace
		{
			get
			{
                if (_scriptFindReplaceForm == null || _scriptFindReplaceForm.IsDisposed)
                {
                    // TODO: Search all windows for an instance of this window type
                    _scriptFindReplaceForm = new FindReplaceDialog();
                }	
				return _scriptFindReplaceForm;
			}
			set { _scriptFindReplaceForm = value; }
		}

		/// <summary>
		/// Returns the static Skin Setting window
		/// </summary>
		public static SkinSettingsForm SkinSettingForm
		{
			get
			{
				if (_skinSettingsForm == null || _skinSettingsForm.IsDisposed)
					_skinSettingsForm = new SkinSettingsForm();
				return _skinSettingsForm;
			}
			set { _skinSettingsForm = value; }
		}

		/// <summary>
		/// Returns the static Auto-Complete Window
		/// </summary>
		public static AutoCompleteForm AutoCompleteWindow
		{
			get
			{
				if (_autoCompleteForm == null || _autoCompleteForm.IsDisposed)
					_autoCompleteForm = new AutoCompleteForm();
				return _autoCompleteForm;
			}
		}

		/// <summary>
		/// Gets or sets the tab context menu for script windows
		/// </summary>
		public static ContextMenuStrip ScriptTabContextMenu { get; set; }

		/// <summary>
		/// Gets or sets the form used for searching all scripts
		/// </summary>
		public static ScriptSearchForm ScriptSearchForm
		{
			get
			{
				if (_scriptSearchForm == null || _scriptSearchForm.IsDisposed)
					_scriptSearchForm = new ScriptSearchForm();
				return _scriptSearchForm;
			}
			set { _scriptSearchForm = value; }
		}

		/// <summary>
		/// Gets or sets the instance of the Calculator
		/// </summary>
		public static CalculatorForm CalculatorWindow
		{
			get
			{
				if (_calculatorForm == null || _calculatorForm.IsDisposed)
					_calculatorForm = new CalculatorForm();
				return _calculatorForm;
			}
			set { _calculatorForm = value; }
		}

		#endregion

		/// <summary>
		/// Gets a database window of the given type. If one is already created, it returns it, 
		/// otherwise a new instance is created.
		/// </summary>
		/// <typeparam name="T">Type of database panel to get, must derive from DatabaseWindow</typeparam>
		/// <returns>A window instance of the given type.</returns>
		public static T DatabaseForm<T>() where T : DatabaseWindow
		{
			var form = (T)_databaseForms.Find(delegate(DatabaseWindow w) { return w is T; });
			if (form != null)
				return form;
			return Activator.CreateInstance<T>();
		}
	}
}
