#region Using Directives

using System;
using System.IO;
using System.Windows.Forms;
using ARCed.Helpers;

#endregion

namespace ARCed.Dialogs
{
    /// <summary>
    /// Dialog for creating a new ARCed project.
    /// </summary>
	public partial class NewProjectForm : Form
	{
		#region Private Fields

		private string _location, _folder;

		#endregion

		#region Public Properties
		/// <summary>
		/// Gets the path to the defined project directory from the text control
		/// </summary>
		public string ProjectDirectory { get { return this.textBoxLocation.Text; } }
		/// <summary>
		/// Gets the title of the game from the text control
		/// </summary>
		public string ProjectTitle { get { return this.textBoxTitle.Text; } }
		/// <summary>
		/// Gets the name of the selected template from the combo control
		/// </summary>
		public string ProjectTemplate { get { return this.comboTemplates.Text; } }
		#endregion

		#region Construction

		/// <summary>
		/// Object initialization
		/// </summary>
		public NewProjectForm()
		{
			this.InitializeComponent();
		}

		/// <summary>
		/// Fills the default name in with first new directory in sequence
		/// </summary>
		/// <param name="sender">The invoker of the event</param>
		/// <param name="e">Event arguments</param>
		private void NewProjectFormLoad(object sender, EventArgs e)
		{
			string dir = PathHelper.DefaultSaveDirectory;
			string path, name;
			int count = 0;
			while (true)
			{
				count++;
				name = "Project" + count;
				path = Path.Combine(dir, name);
				if (!Directory.Exists(path))
					break;
			}
			this._location = Path.GetDirectoryName(path);
			this._folder = this.textBoxFolderName.Text = name;
			this.RefreshTemplates();
			this.comboTemplates.SelectedIndex = 0;
		}

		#endregion

		#region Private Methods

		/// <summary>
		/// Iterates over installed .zip templates and adds their names to the combo control
		/// </summary>
		private void RefreshTemplates()
		{
			this.comboTemplates.Items.Clear();
			this.comboTemplates.Items.Add("Default");
			var templateDir = PathHelper.ProjectTemplateDirectory;
		    if (!Directory.Exists(templateDir)) return;
		    string name;
            foreach (string filename in Directory.GetFiles(templateDir, "*.7z"))
            {
                name = Path.GetFileNameWithoutExtension(filename);
                if (name != null) this.comboTemplates.Items.Add(name);
            }
		}

		/// <summary>
		/// Opens the folder browser dialog to select a project location
		/// </summary>
		/// <param name="sender">The invoker of the event</param>
		/// <param name="e">Event arguments</param>
		private void ButtonBrowseClick(object sender, EventArgs e)
		{
			using (var dialog = new FolderBrowserDialog())
			{
				dialog.Description = "Choose a location for the project.";
				dialog.ShowNewFolderButton = true;
				dialog.RootFolder = Environment.SpecialFolder.MyComputer;
				dialog.SelectedPath = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments);
				if (dialog.ShowDialog() == DialogResult.OK)
				{
					this.textBoxLocation.Text = Path.Combine(dialog.SelectedPath, this._folder);
					this._location = dialog.SelectedPath;
				}
			}
		}

		/// <summary>
		/// Sets the dialog result and closes the dialog
		/// </summary>
		/// <param name="sender">The invoker of the event</param>
		/// <param name="e">Event arguments</param>
		private void ButtonOkClick(object sender, EventArgs e)
		{
			DialogResult = DialogResult.OK;
			Close();
		}

		/// <summary>
		/// Updates the title and location when the text changes
		/// </summary>
		/// <param name="sender">The invoker of the event</param>
		/// <param name="e">Event arguments</param>
		private void TextBoxFolderNameTextChanged(object sender, EventArgs e)
		{
			this._folder = this.textBoxFolderName.Text;
			this.textBoxTitle.Text = this._folder;
			this.textBoxLocation.Text = Path.Combine(this._location, this._folder);
		}

		/// <summary>
		/// Updates the location when the text changes
		/// </summary>
		/// <param name="sender">The invoker of the event</param>
		/// <param name="e">Event arguments</param>
		private void TextBoxLocationTextChanged(object sender, EventArgs e)
		{
			if (ActiveControl != null && !this.textBoxFolderName.Focused)
				this._location = this.textBoxLocation.Text;
		}

		#endregion
	}
}
