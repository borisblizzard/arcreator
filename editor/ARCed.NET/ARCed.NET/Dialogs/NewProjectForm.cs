#region Using Directives

using System;
using System.IO;
using System.Windows.Forms;
using ARCed.Helpers;

#endregion

namespace ARCed.Dialogs
{
	public partial class NewProjectForm : Form
	{
		#region Private Fields

		private string _location, _folder;

		#endregion

		#region Public Properties
		/// <summary>
		/// Gets the path to the defined project directory from the text control
		/// </summary>
		public string ProjectDirectory { get { return textBoxLocation.Text; } }
		/// <summary>
		/// Gets the title of the game from the text control
		/// </summary>
		public string ProjectTitle { get { return textBoxTitle.Text; } }
		/// <summary>
		/// Gets the name of the selected template from the combo control
		/// </summary>
		public string ProjectTemplate { get { return comboTemplates.Text; } }
		#endregion

		#region Construction

		/// <summary>
		/// Object initialization
		/// </summary>
		public NewProjectForm()
		{
			InitializeComponent();
		}

		/// <summary>
		/// Fills the default name in with first new directory in sequence
		/// </summary>
		/// <param name="sender">The invoker of the event</param>
		/// <param name="e">Event arguments</param>
		private void NewProjectForm_Load(object sender, EventArgs e)
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
			_location = Path.GetDirectoryName(path);
			_folder = textBoxFolderName.Text = name;
			RefreshTemplates();
			comboTemplates.SelectedIndex = 0;
		}

		#endregion

		#region Private Methods

		/// <summary>
		/// Iterates over installed .zip templates and adds their names to the combo control
		/// </summary>
		private void RefreshTemplates()
		{
			comboTemplates.Items.Clear();
			comboTemplates.Items.Add("Default");
			string templateDir = PathHelper.ProjectTemplateDirectory;
			if (Directory.Exists(templateDir))
			{
				foreach (string filename in Directory.GetFiles(templateDir, "*.7z"))
					comboTemplates.Items.Add(Path.GetFileNameWithoutExtension(filename));
			}
		}

		/// <summary>
		/// Opens the folder browser dialog to select a project location
		/// </summary>
		/// <param name="sender">The invoker of the event</param>
		/// <param name="e">Event arguments</param>
		private void buttonBrowse_Click(object sender, EventArgs e)
		{
			using (var dialog = new FolderBrowserDialog())
			{
				dialog.Description = "Choose a location for the project.";
				dialog.ShowNewFolderButton = true;
				dialog.RootFolder = Environment.SpecialFolder.MyComputer;
				dialog.SelectedPath = Environment.GetFolderPath(Environment.SpecialFolder.MyDocuments);
				if (dialog.ShowDialog() == DialogResult.OK)
				{
					textBoxLocation.Text = Path.Combine(dialog.SelectedPath, _folder);
					_location = dialog.SelectedPath;
				}
			}
		}

		/// <summary>
		/// Sets the dialog result and closes the dialog
		/// </summary>
		/// <param name="sender">The invoker of the event</param>
		/// <param name="e">Event arguments</param>
		private void buttonOK_Click(object sender, EventArgs e)
		{
			this.DialogResult = DialogResult.OK;
			this.Close();
		}

		/// <summary>
		/// Updates the title and location when the text changes
		/// </summary>
		/// <param name="sender">The invoker of the event</param>
		/// <param name="e">Event arguments</param>
		private void textBoxFolderName_TextChanged(object sender, EventArgs e)
		{
			_folder = textBoxFolderName.Text;
			textBoxTitle.Text = _folder;
			textBoxLocation.Text = Path.Combine(_location, _folder);
		}

		/// <summary>
		/// Updates the location when the text changes
		/// </summary>
		/// <param name="sender">The invoker of the event</param>
		/// <param name="e">Event arguments</param>
		private void textBoxLocation_TextChanged(object sender, EventArgs e)
		{
			if (this.ActiveControl != null && !textBoxFolderName.Focused)
				_location = textBoxLocation.Text;
		}

		#endregion
	}
}
