using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using ARCed.Dialogs;
using ARCed.Controls;

namespace ARCed.Database.Animations
{
	public partial class AnimationMainForm : DatabaseWindow
	{
		#region Private Fields

		RPG.Animation _animation = new RPG.Animation();

		#endregion

		/// <summary>
		/// Gets the object list control of this database panel.
		/// </summary>
		protected override DatabaseObjectListBox DataObjectList { get { return dataObjectList; } }

		#region Construction

		public AnimationMainForm()
		{
			// TEST ////////////////////////////////////////////
			
			////////////////////////////////////////////////////
			InitializeComponent();
		}

		private void AnimationMainForm_Load(object sender, EventArgs e)
		{
			//RefreshObjectList();
			//dataObjectList.SelectedIndex = 0;
		}

		#endregion

		#region Overrides

		/// <summary>
		/// Refreshes objects by type flag
		/// </summary>
		/// <param name="type">Flag for type of object to refresh</param>
		public override void NotifyRefresh(RefreshType type)
		{
			if (type.HasFlag(RefreshType.Classes))
			{

			}
			if (type.HasFlag(RefreshType.Parameters))
			{

			}
		}

		public override void RefreshCurrentObject()
		{
			suppressEvents = true;

			suppressEvents = false;
		}

		#endregion

		private void RefreshFrameList()
		{
			listBoxFrames.BeginUpdate();
			listBoxFrames.Items.Clear();
			for (int i = 0; i < _animation.frames.Count; i++)
				listBoxFrames.Items.Add(String.Format("#{0:d3}", i + 1));
			listBoxFrames.EndUpdate();
		}

		private void RefreshImages()
		{
			// TEST ////////////////////////////////////////////
			animeSrcXnaPanel.Animation = _animation;
			////////////////////////////////////////////////////
		}

		private void numericUpDownFrames_ValueChanged(object sender, EventArgs e)
		{
			if (!suppressEvents)
			{
				int frames = (int)numericUpDownFrames.Value;
				if (_animation.frames.Count > frames)
				{
					for (int i = _animation.frames.Count; i > frames; i--)
						_animation.frames.RemoveAt(i - 1);
				}
				else if (_animation.frames.Count < frames)
				{
					for (int i = _animation.frames.Count; i < frames; i++)
						_animation.frames.Add(new RPG.Animation.Frame());
				}
				_animation.frame_max = frames;
				RefreshFrameList();
			}
		}

		private void textBoxGraphic_OnButtonClick(object sender, EventArgs e)
		{
			using (ImageSelectionForm dialog =
				new ImageSelectionForm(@"Animations", _animation.animation_name))
			{
				dialog.Hue = _animation.animation_hue;
				dialog.OptionsEnabled = false;
				if (dialog.ShowDialog(this) == DialogResult.OK)
				{
					_animation.animation_name = dialog.ImageName;
					_animation.animation_hue = dialog.Hue;
					RefreshImages();
				}
			}
		}
	}
}
