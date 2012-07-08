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

		RPG.Animation _animation;

		#endregion

		/// <summary>
		/// Gets the object list control of this database panel.
		/// </summary>
		protected override DatabaseObjectListBox DataObjectList { get { return dataObjectList; } }

		public override List<dynamic> Data { get { return Project.Data.Animations; } }

		#region Construction

		public AnimationMainForm()
		{
			// TEST ////////////////////////////////////////////
			
			////////////////////////////////////////////////////
			InitializeComponent();
		}

		private void AnimationMainForm_Load(object sender, EventArgs e)
		{
			// TEST ////////////////////////////////////////////

			Project.Data.Animations = new List<dynamic>() { null };
			for (int i = 1; i <= 20; i++)
				Project.Data.Animations.Add(new RPG.Animation() { id = i });

			// TEST ////////////////////////////////////////////
			RefreshObjectList();
			dataObjectList.SelectedIndex = 0;
			listBoxFrames.SelectedIndex = 0;
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
			animeXnaPanel.Animation = _animation;
			animeSrcXnaPanel.Animation = _animation;
			textBoxName.Text = _animation.name;
			textBoxGraphic.Text = String.IsNullOrWhiteSpace(_animation.animation_name) ?
				"<None>" : _animation.animation_name;
			numericUpDownFrames.Value = _animation.frame_max;
			comboBoxPosition.SelectedIndex = _animation.position;
			RefreshTimings();
			RefreshFrameList();
			suppressEvents = false;
		}

		#endregion

		private void RefreshTimings()
		{
			listViewTiming.BeginUpdate();
			listViewTiming.Items.Clear();
			string[] items;
			string flash, condition;
			foreach (RPG.Animation.Timing timing in _animation.timings)
			{
				switch (timing.flash_scope)
				{
					case 1: 
						flash = String.Format("Target{0}, @{1}", timing.flash_color, timing.flash_duration);
						break;
					case 2:
						flash = String.Format("Screen{0}, @{1}", timing.flash_color, timing.flash_duration);
						break;
					case 3:
						flash = String.Format("Hide Target, @{0}", timing.flash_duration);
						break;
					default: flash = "<None>"; break;
				}
				condition = String.Format("");
				items = new string[] {
					timing.frame.ToString(),
					String.IsNullOrWhiteSpace(timing.se.name) ? "<None>" : timing.se.ToString(),
					flash,
					new[] { "None", "Hit", "Miss"}[timing.condition]
				};
				listViewTiming.Items.Add(new ListViewItem(items));
			}
			listViewTiming.EndUpdate();
		}

		private void RefreshFrameList()
		{
			int index = listBoxFrames.SelectedIndex;
			listBoxFrames.BeginUpdate();
			listBoxFrames.Items.Clear();
			for (int i = 0; i < _animation.frames.Count; i++)
				listBoxFrames.Items.Add(String.Format("#{0:d3}", i + 1));
			listBoxFrames.SelectedIndex = index.Clamp(0, listBoxFrames.Items.Count - 1);
			listBoxFrames.EndUpdate();
		}

		private void RefreshImages()
		{
			// TEST ////////////////////////////////////////////

			_animation = new RPG.Animation()
			{
				animation_hue = _animation.animation_hue,
				animation_name = _animation.animation_name
			};
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
					textBoxGraphic.Text = String.IsNullOrWhiteSpace(_animation.animation_name) ?
						"<None>" : _animation.animation_name;
					RefreshImages();
				}
			}
		}

		private void dataObjectList_OnListBoxIndexChanged(object sender, EventArgs e)
		{
			int index = dataObjectList.SelectedIndex;
			if (index >= 0)
			{
				_animation = Data[index + 1];
				RefreshCurrentObject();
			}
		}

		private void textBoxName_TextChanged(object sender, EventArgs e)
		{
			if (!suppressEvents)
			{
				_animation.name = textBoxName.Text;
				int index = dataObjectList.SelectedIndex;
				dataObjectList.Items[index] = _animation.ToString();
				dataObjectList.Invalidate(dataObjectList.GetItemRectangle(index));
			}
		}

		private void listViewTiming_DoubleClick(object sender, EventArgs e)
		{

		}

		private void listViewTiming_ColumnClick(object sender, ColumnClickEventArgs e)
		{

		}

		private void listViewTiming_MouseDown(object sender, MouseEventArgs e)
		{
			if (e.Clicks == 2)
			{
				using (AnimationTimingDialog dialog = new AnimationTimingDialog())
				{
					
					var indices = listViewTiming.SelectedIndices;
					int index = indices.Count > 0 ? indices[0] : -1;
					if (index >= 0)
						dialog.Timing = _animation.timings[index];
					else
						dialog.Timing = new RPG.Animation.Timing();
					if (dialog.ShowDialog() == DialogResult.OK)
					{
						if (index >= 0)
							_animation.timings[index] = dialog.Timing;
						else
							_animation.timings.Add(dialog.Timing);
						RefreshTimings();
					}
				}
			}
		}
	}
}
