#region Using Directives

using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;

#endregion

namespace ARCed.UI
{
    public class DockContentCollection : ReadOnlyCollection<IDockContent>
    {
        private static readonly List<IDockContent> _emptyList = new List<IDockContent>(0);

        public DockContentCollection()
            : base(new List<IDockContent>())
        {
        }

        public DockContentCollection(DockPane pane)
            : base(_emptyList)
        {
            this._mDockPane = pane;
        }

        private readonly DockPane _mDockPane;
        private DockPane DockPane
        {
            get { return this._mDockPane; }
        }

        public new IDockContent this[int index]
        {
            get
            {
                if (this.DockPane == null)
                    return Items[index];
                else
                    return this.GetVisibleContent(index);
            }
        }

        public int Add(IDockContent content)
        {
#if DEBUG
			if (this.DockPane != null)
				throw new InvalidOperationException();
#endif

            if (this.Contains(content))
                return this.IndexOf(content);

            Items.Add(content);
            return this.Count - 1;
        }

        internal void AddAt(IDockContent content, int index)
        {
#if DEBUG
			if (this.DockPane != null)
				throw new InvalidOperationException();
#endif

            if (index < 0 || index > Items.Count - 1)
                return;

            if (this.Contains(content))
                return;

            Items.Insert(index, content);
        }

        public new bool Contains(IDockContent content)
        {
            if (this.DockPane == null)
                return Items.Contains(content);
            else
                return (this.GetIndexOfVisibleContents(content) != -1);
        }

        public new int Count
        {
            get
            {
                if (this.DockPane == null)
                    return base.Count;
                else
                    return this.CountOfVisibleContents;
            }
        }

        public new int IndexOf(IDockContent content)
        {
            if (this.DockPane == null)
            {
                if (!this.Contains(content))
                    return -1;
                else
                    return Items.IndexOf(content);
            }
            else
                return this.GetIndexOfVisibleContents(content);
        }

        public void Remove(IDockContent content)
        {
            if (this.DockPane != null)
                throw new InvalidOperationException();

            if (!this.Contains(content))
                return;

            Items.Remove(content);
        }

        private int CountOfVisibleContents
        {
            get
            {
#if DEBUG
				if (this.DockPane == null)
					throw new InvalidOperationException();
#endif

                int count = 0;
                foreach (IDockContent content in this.DockPane.Contents)
                {
                    if (content.DockHandler.DockState == this.DockPane.DockState)
                        count++;
                }
                return count;
            }
        }

        private IDockContent GetVisibleContent(int index)
        {
#if DEBUG
			if (this.DockPane == null)
				throw new InvalidOperationException();
#endif

            int currentIndex = -1;
            foreach (IDockContent content in this.DockPane.Contents)
            {
                if (content.DockHandler.DockState == this.DockPane.DockState)
                    currentIndex++;

                if (currentIndex == index)
                    return content;
            }
            throw (new ArgumentOutOfRangeException());
        }

        private int GetIndexOfVisibleContents(IDockContent content)
        {
#if DEBUG
			if (this.DockPane == null)
				throw new InvalidOperationException();
#endif

            if (content == null)
                return -1;

            int index = -1;
            foreach (IDockContent c in this.DockPane.Contents)
            {
                if (c.DockHandler.DockState == this.DockPane.DockState)
                {
                    index++;

                    if (c == content)
                        return index;
                }
            }
            return -1;
        }
    }
}
