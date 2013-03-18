#region Using Directives

using System;
using System.Collections;
using System.Text.RegularExpressions;
using System.Windows.Forms;

#endregion

namespace ARCed.Controls
{
	/// <summary>
	/// This class is an implementation of the 'IComparer' interface.
	/// </summary>
	public class ListViewColumnSorter : IComparer
	{
		/// <summary>
		/// Specifies the column to be sorted
		/// </summary>
		private int ColumnToSort;
		/// <summary>
		/// Specifies the order in which to sort (i.e. 'Ascending').
		/// </summary>
		private SortOrder OrderOfSort;
		/// <summary>
		/// Case insensitive comparer object
		/// </summary>
		//private CaseInsensitiveComparer ObjectCompare;
		private readonly NumberCaseInsensitiveComparer ObjectCompare;
		private readonly ImageTextComparer FirstObjectCompare;

		/// <summary>
		/// Class constructor.  Initializes various elements
		/// </summary>
		public ListViewColumnSorter()
		{
			// Initialize the column to '0'
			this.ColumnToSort = 0;

			// Initialize the sort order to 'none'
			//OrderOfSort = SortOrder.None;
			this.OrderOfSort = SortOrder.Ascending;

			// Initialize the CaseInsensitiveComparer object
			this.ObjectCompare = new NumberCaseInsensitiveComparer();//CaseInsensitiveComparer();
			this.FirstObjectCompare = new ImageTextComparer();
		}

		/// <summary>
		/// This method is inherited from the IComparer interface.  It compares the two objects passed using a case insensitive comparison.
		/// </summary>
		/// <param name="x">First object to be compared</param>
		/// <param name="y">Second object to be compared</param>
		/// <returns>The result of the comparison. "0" if equal, negative if 'x' is less than 'y' and positive if 'x' is greater than 'y'</returns>
		public int Compare(object x, object y)
		{
			int compareResult;

		    // Cast the objects to be compared to ListViewItem objects
			var listviewX = (ListViewItem)x;
			var listviewY = (ListViewItem)y;

			if (this.ColumnToSort == 0)
			{
				compareResult = this.FirstObjectCompare.Compare(x,y);
			}
			else
			{
				// Compare the two items
				compareResult = this.ObjectCompare.Compare(listviewX.SubItems[this.ColumnToSort].Text, 
                    listviewY.SubItems[this.ColumnToSort].Text);
			}

			// Calculate correct return value based on object comparison
			switch (this.OrderOfSort)
			{
			    case SortOrder.Ascending:
			        return compareResult;
			    case SortOrder.Descending:
			        return (-compareResult);
			    default:
			        return 0;
			}
		}
    
		/// <summary>
		/// Gets or sets the number of the column to which to apply the sorting operation (Defaults to '0').
		/// </summary>
		public int SortColumn
		{
			set
			{
				this.ColumnToSort = value;
			}
			get
			{
				return this.ColumnToSort;
			}
		}

		/// <summary>
		/// Gets or sets the order of sorting to apply (for example, 'Ascending' or 'Descending').
		/// </summary>
		public SortOrder Order
		{
			set
			{
				this.OrderOfSort = value;
			}
			get
			{
				return this.OrderOfSort;
			}
		}
    
	}

	public class ImageTextComparer : IComparer
	{
		//private CaseInsensitiveComparer ObjectCompare;
		private readonly NumberCaseInsensitiveComparer ObjectCompare;
        
		public ImageTextComparer()
		{
			// Initialize the CaseInsensitiveComparer object
			this.ObjectCompare = new NumberCaseInsensitiveComparer();//CaseInsensitiveComparer();
		}

		public int Compare(object x, object y)
		{
			//int compareResult;

		    // Cast the objects to be compared to ListViewItem objects
			var listviewX = (ListViewItem)x;
			int image1 = listviewX.ImageIndex;
			var listviewY = (ListViewItem)y;
			int image2 = listviewY.ImageIndex;

			if (image1 < image2)
			{
				return -1;
			}
			else if (image1 == image2)
			{
				return this.ObjectCompare.Compare(listviewX.Text,listviewY.Text);
			}
			else
			{
				return 1;
			}
		}
	}

	public class NumberCaseInsensitiveComparer : CaseInsensitiveComparer
	{

		public new int Compare(object x, object y)
		{
			if ((x is String) && IsWholeNumber((string)x) && (y is String) && IsWholeNumber((string)y))
			{
				return base.Compare(Convert.ToInt32(x),Convert.ToInt32(y));
			}
			else
			{
				return base.Compare(x,y);
			}
		}

		private static bool IsWholeNumber(string strNumber)
		{
			var objNotWholePattern=new Regex("[^0-9]");
			return !objNotWholePattern.IsMatch(strNumber);
		}  
	}

}
