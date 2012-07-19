#region Using Directives

using System.Drawing;
using System.Windows.Forms;
using ARCed.Core.Win32;

#endregion

namespace ARCed.UI
{
	internal class SplitterBase : Control
	{
		public SplitterBase()
		{
			SetStyle(ControlStyles.Selectable, false);
		}

		public override DockStyle Dock
		{
			get	{	return base.Dock;	}
			set
			{
				SuspendLayout();
				base.Dock = value;

				if (this.Dock == DockStyle.Left || this.Dock == DockStyle.Right)
					Width = this.SplitterSize;
				else if (this.Dock == DockStyle.Top || this.Dock == DockStyle.Bottom)
					Height = this.SplitterSize;
				else
					Bounds = Rectangle.Empty;

				if (this.Dock == DockStyle.Left || this.Dock == DockStyle.Right)
					Cursor = Cursors.VSplit;
				else if (this.Dock == DockStyle.Top || this.Dock == DockStyle.Bottom)
					Cursor = Cursors.HSplit;
				else
					Cursor = Cursors.Default;
					
				ResumeLayout();
			}
		}

		protected virtual int SplitterSize
		{
			get	{	return 0;	}
		}

		protected override void OnMouseDown(MouseEventArgs e)
		{
			base.OnMouseDown(e);

			if (e.Button != MouseButtons.Left)
				return;

			this.StartDrag();
		}

		protected virtual void StartDrag()
		{
		}

		protected override void WndProc(ref Message m)
		{
            // eat the WM_MOUSEACTIVATE message
			if (m.Msg == (int)Msgs.WM_MOUSEACTIVATE)
				return;

			base.WndProc(ref m);
		}
	}
}
