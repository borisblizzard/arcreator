#region Using Directives

using System;
using System.Collections.Generic;
using System.Windows.Forms;
using ARCed.Controls;
using ARCed.Dialogs;
using RPG;

#endregion

namespace ARCed.Database.Animations
{
	public partial class AnimationMainForm : DatabaseWindow
	{
		#region Private Fields

		Animation _animation;

		#endregion

		/// <summary>
		/// Gets the object list control of this database panel.
		/// </summary>
		protected override DatabaseObjectListBox DataObjectList { get { return this.dataObjectList; } }

		public override List<dynamic> Data { get { return Project.Data.Animations; } }

		#region Construction

		public AnimationMainForm()
		{
			// TEST ////////////////////////////////////////////
			
			////////////////////////////////////////////////////
			this.InitializeComponent();
		}

		private void AnimationMainForm_Load(object sender, EventArgs e)
		{
			// TEST ////////////////////////////////////////////

			Project.Data.Animations = new List<dynamic>
			{ null };
			for (int i = 1; i <= 20; i++)
				Project.Data.Animations.Add(new Animation
				{ id = i });

			// TEST ////////////////////////////////////////////
			RefreshObjectList();
			this.dataObjectList.SelectedIndex = 0;
			this.listBoxFrames.SelectedIndex = 0;
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

        /// <summary>
        /// Refreshes the form to display data for the currently selected <see cref="RPG.Animation"/>.
        /// </summary>
		public override void RefreshCurrentObject()
		{
			SuppressEvents = true;
			this.animeXnaPanel.Animation = this._animation;
			this.animeSrcXnaPanel.Animation = this._animation;
			this.textBoxName.Text = this._animation.name;
			this.textBoxGraphic.Text = String.IsNullOrWhiteSpace(this._animation.animation_name) ?
				"<None>" : this._animation.animation_name;
			this.numericUpDownFrames.Value = this._animation.frame_max;
			this.comboBoxPosition.SelectedIndex = this._animation.position;
			this.RefreshTimings();
			this.RefreshFrameList();
			SuppressEvents = false;
		}

		#endregion

		private void RefreshTimings()
		{
			this.listViewTiming.BeginUpdate();
			this.listViewTiming.Items.Clear();
			string[] items;
			string flash, condition;
			foreach (Animation.Timing timing in this._animation.timings)
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
				items = new[] {
					timing.frame.ToString(),
					String.IsNullOrWhiteSpace(timing.se.name) ? "<None>" : timing.se.ToString(),
					flash,
					new[] { "None", "Hit", "Miss"}[timing.condition]
				};
				this.listViewTiming.Items.Add(new ListViewItem(items));
			}
			this.listViewTiming.EndUpdate();
		}

		private void RefreshFrameList()
		{
			int index = this.listBoxFrames.SelectedIndex;
			this.listBoxFrames.BeginUpdate();
			this.listBoxFrames.Items.Clear();
			for (int i = 0; i < this._animation.frames.Count; i++)
				this.listBoxFrames.Items.Add(String.Format("#{0:d3}", i + 1));
			this.listBoxFrames.SelectedIndex = index.Clamp(0, this.listBoxFrames.Items.Count - 1);
			this.listBoxFrames.EndUpdate();
		}

		private void RefreshImages()
		{
			// TEST ////////////////////////////////////////////

			this._animation = new Animation
			{
				animation_hue = this._animation.animation_hue,
				animation_name = this._animation.animation_name
			};
			this.animeSrcXnaPanel.Animation = this._animation;
			////////////////////////////////////////////////////
		}

		private void numericUpDownFrames_ValueChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
			{
				var frames = (int)this.numericUpDownFrames.Value;
				if (this._animation.frames.Count > frames)
				{
					for (int i = this._animation.frames.Count; i > frames; i--)
						this._animation.frames.RemoveAt(i - 1);
				}
				else if (this._animation.frames.Count < frames)
				{
					for (int i = this._animation.frames.Count; i < frames; i++)
						this._animation.frames.Add(new Animation.Frame());
				}
				this._animation.frame_max = frames;
				this.RefreshFrameList();
			}
		}

		private void textBoxGraphic_OnButtonClick(object sender, EventArgs e)
		{
			using (var dialog =
				new ImageSelectionForm(@"Animations", this._animation.animation_name))
			{
				dialog.Hue = this._animation.animation_hue;
				dialog.OptionsEnabled = false;
				if (dialog.ShowDialog(this) == DialogResult.OK)
				{
					this._animation.animation_name = dialog.ImageName;
					this._animation.animation_hue = dialog.Hue;
					this.textBoxGraphic.Text = String.IsNullOrWhiteSpace(this._animation.animation_name) ?
						"<None>" : this._animation.animation_name;
					this.RefreshImages();
				}
			}
		}

		private void dataObjectList_OnListBoxIndexChanged(object sender, EventArgs e)
		{
			int index = this.dataObjectList.SelectedIndex;
			if (index >= 0)
			{
				this._animation = this.Data[index + 1];
				this.RefreshCurrentObject();
			}
		}

		private void textBoxName_TextChanged(object sender, EventArgs e)
		{
			if (!SuppressEvents)
			{
				this._animation.name = this.textBoxName.Text;
				int index = this.dataObjectList.SelectedIndex;
				this.dataObjectList.Items[index] = this._animation.ToString();
				this.dataObjectList.Invalidate(this.dataObjectList.GetItemRectangle(index));
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
				using (var dialog = new AnimationTimingDialog())
				{
					
					var indices = this.listViewTiming.SelectedIndices;
					int index = indices.Count > 0 ? indices[0] : -1;
					dialog.Timing = index >= 0 ? this._animation.timings[index] : new Animation.Timing();
					if (dialog.ShowDialog() == DialogResult.OK)
					{
						if (index >= 0)
							this._animation.timings[index] = dialog.Timing;
						else
							this._animation.timings.Add(dialog.Timing);
						this.RefreshTimings();
					}
				}
			}
		}
	}
}
