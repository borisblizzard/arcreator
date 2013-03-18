#region Using Directives

using System;
using System.Collections;
using System.Collections.Generic;

#endregion


namespace ARCed.Scintilla
{
    public class SnippetLinkCollection : IDictionary<string, SnippetLink>, IList<SnippetLink>
    {
        #region Fields

        private int _activeLinkIndex = -1;
        private SnippetLinkRange _activeRange;
        private SnippetLinkEnd _endPoint;
        private bool _isActive;
        private readonly List<SnippetLink> _snippetLinks = new List<SnippetLink>();

        #endregion Fields


        #region Methods

        public void Add(SnippetLink item)
        {
            this.Add(item.Key, item);
        }


        public void Add(string key, SnippetLink value)
        {
            if (!key.Equals(value.Key, StringComparison.CurrentCultureIgnoreCase))
                throw new ArgumentException("Key argument must == value.Key", "key");
            else if (this.ContainsKey(key))
                throw new ArgumentException("Key already exists", "key");

            this._snippetLinks.Add(value);
        }


        public void Add(KeyValuePair<string, SnippetLink> item)
        {
            this.Add(item.Key, item.Value);
        }


        public void Clear()
        {
            var rageList = new List<ManagedRange>();

            foreach (SnippetLink sl in this._snippetLinks)
            {
                foreach (Range r in sl.Ranges)
                {
                    var mr = r as ManagedRange;
                    rageList.Add(mr);
                }
            }

            this._snippetLinks.Clear();

            foreach (ManagedRange mr in rageList)
                mr.Dispose();
        }


        public bool Contains(SnippetLink item)
        {
            return this._snippetLinks.Contains(item);
        }


        public bool Contains(KeyValuePair<string, SnippetLink> item)
        {
            return this.ContainsKey(item.Key);
        }


        public bool ContainsKey(string key)
        {
            foreach (SnippetLink sl in this._snippetLinks)
                if (sl.Key.Equals(key, StringComparison.CurrentCultureIgnoreCase))
                    return true;

            return false;
        }


        public void CopyTo(SnippetLink[] array, int arrayIndex)
        {
            this._snippetLinks.CopyTo(array, arrayIndex);
        }


        public void CopyTo(KeyValuePair<string, SnippetLink>[] array, int arrayIndex)
        {
            throw new Exception("The method or operation is not implemented.");
        }


        public IEnumerator<KeyValuePair<string, SnippetLink>> GetEnumerator()
        {
            throw new Exception("The method or operation is not implemented.");
        }


        IEnumerator<SnippetLink> IEnumerable<SnippetLink>.GetEnumerator()
        {
            return this._snippetLinks.GetEnumerator();
        }


        public int IndexOf(SnippetLink item)
        {
            return this._snippetLinks.IndexOf(item);
        }


        public void Insert(int index, SnippetLink item)
        {
            this._snippetLinks.Insert(index, item);
        }


        public bool Remove(string key)
        {
            for (int i = 0; i < this._snippetLinks.Count; i++)
            {
                if (this._snippetLinks[i].Key.Equals(key, StringComparison.CurrentCultureIgnoreCase))
                {
                    this._snippetLinks.RemoveAt(i);
                    return true;
                }
            }

            return false;
        }


        public bool Remove(SnippetLink item)
        {
            return this._snippetLinks.Remove(item);
        }


        public bool Remove(KeyValuePair<string, SnippetLink> item)
        {
            return Remove(item.Key);
        }


        public void RemoveAt(int index)
        {
            this._snippetLinks.RemoveAt(index);
        }


        IEnumerator IEnumerable.GetEnumerator()
        {
            return this._snippetLinks.GetEnumerator();
        }


        public bool TryGetValue(string key, out SnippetLink value)
        {
            value = null;
            for (int i = 0; i < this._snippetLinks.Count; i++)
            {
                if (this._snippetLinks[i].Key.Equals(key, StringComparison.CurrentCultureIgnoreCase))
                {
                    value = this._snippetLinks[i];
                    return true;
                }
            }
            return false;
        }

        #endregion Methods


        #region Properties

        public SnippetLinkRange ActiveRange
        {
            get
            {
                return this._activeRange;
            }
            set
            {
                this._activeRange = value;
            }
        }


        public SnippetLink ActiveSnippetLink
        {
            get
            {
                if (this._activeLinkIndex < 0 || this._activeLinkIndex >= this._snippetLinks.Count)
                    return null;

                return this._snippetLinks[this._activeLinkIndex];
            }
            set
            {
                if (value == null)
                {
                    this._activeLinkIndex = -1;
                    return;
                }
                this._activeLinkIndex = this._snippetLinks.IndexOf(value);
            }
        }


        public int Count
        {
            get { return this._snippetLinks.Count; }
        }


        public SnippetLinkEnd EndPoint
        {
            get
            {
                return this._endPoint;
            }
            set
            {
                this._endPoint = value;
            }
        }


        public bool IsActive
        {
            get
            {
                return this._isActive;
            }
            set
            {
                this._isActive = value;
            }
        }


        public bool IsReadOnly
        {
            get { return false; }
        }


        public ICollection<string> Keys
        {
            get
            {
                var keys = new string[this._snippetLinks.Count];
                for (int i = 0; i < this._snippetLinks.Count; i++)
                {
                    keys[i] = this._snippetLinks[i].Key;
                }
                return keys;
            }
        }


        public SnippetLink NextActiveSnippetLink
        {
            get
            {
                int newIndex = this._activeLinkIndex;
                if (newIndex < 0)
                    return null;
                else if (++newIndex >= this._snippetLinks.Count)
                    newIndex = 0;

                return this._snippetLinks[newIndex];
            }
        }


        public SnippetLink PreviousActiveSnippetLink
        {
            get
            {
                int newIndex = this._activeLinkIndex;
                if (newIndex < 0)
                    return null;
                else if (--newIndex < 0)
                    newIndex = this._snippetLinks.Count - 1;

                return this._snippetLinks[newIndex];
            }
        }


        public ICollection<SnippetLink> Values
        {
            get
            {
                var values = new SnippetLink[this._snippetLinks.Count];
                for (int i = 0; i < this._snippetLinks.Count; i++)
                {
                    values[i] = this._snippetLinks[i];
                }
                return values;
            }
        }

        #endregion Properties


        #region Indexers

        public SnippetLink this[string key]
        {
            get
            {
                for (int i = 0; i < this._snippetLinks.Count; i++)
                {
                    if (this._snippetLinks[i].Key.Equals(key, StringComparison.CurrentCultureIgnoreCase))
                        return this._snippetLinks[i];
                }
                throw new KeyNotFoundException();
            }
            set
            {
                if (!key.Equals(value.Key, StringComparison.CurrentCultureIgnoreCase))
                    throw new ArgumentException("Key argument must == value.Key", "key");

                for (int i = 0; i < this._snippetLinks.Count; i++)
                {
                    if (this._snippetLinks[i].Key.Equals(key, StringComparison.CurrentCultureIgnoreCase))
                    {
                        this._snippetLinks[i] = value;
                        return;
                    }
                }

                this._snippetLinks.Add(value);
            }
        }


        public SnippetLink this[int index]
        {
            get
            {
                return this._snippetLinks[index];
            }
            set
            {
                this._snippetLinks[index] = value;
            }
        }

        #endregion Indexers
    }
}
