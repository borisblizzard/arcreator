#region Using Directives

using System;
using System.Collections.Generic;
using ARCed;

#endregion

/// <summary>
/// The multidimensional array class. 
/// Each element takes up 2 signed bytes (<see langword="short"/>), ranging from -32,768 to 32,767.
/// </summary>
public class Table
{
    #region Private Fields

    private int[] _data;
	private int _xSize, _ySize, _zSize, _dimensions;

    #endregion

    #region Public Properties

    /// <summary>
	/// Accesses the array's elements. Pulls the same number of arguments as 
	/// there are dimensions in the created array. Returns nil if the specified 
	/// element does not exist.
	/// </summary>
	/// <param name="x">Index on the x-axis</param>
	/// <returns>Value at the specified position</returns>
	public int this[int x]
	{
		get { return GetData(x, 0, 0); }
		set { SetData(x, 0, 0, value); }
	}

	/// <summary>
	/// Accesses the array's elements. Pulls the same number of arguments as 
	/// there are dimensions in the created array. Returns nil if the specified 
	/// element does not exist.
	/// </summary>
	/// <param name="x">Index on the x-axis</param>
	/// <param name="y">Index on the y-axis</param>
	/// <returns>Value at the specified position</returns>
	public int this[int x, int y]
	{
		get { return GetData(x, y, 0); }
		set { SetData(x, y, 0, value); }
	}

	/// <summary>
	/// Accesses the array's elements. Pulls the same number of arguments as 
	/// there are dimensions in the created array. Returns nil if the specified 
	/// element does not exist.
	/// </summary>
	/// <param name="x">Index on the x-axis</param>
	/// <param name="y">Index on the y-axis</param>
	/// <param name="z">Index on the z-axis</param>
	/// <returns>Value at the specified position</returns>
	public int this[int x, int y, int z]
	{
		get { return GetData(x, y, z); }
		set { SetData(x, y, z, value); }
	}
	
	/// <summary>
	/// Gets the size of the Table on the x-axis
	/// </summary>
	public int xsize { get { return _xSize; } }

	/// <summary>
	/// Gets the size of the Table on the y-axis
	/// </summary>
	public int ysize { get { return _ySize; } }

	/// <summary>
	/// Gets the size of the Table on the z-axis
	/// </summary>
	public int zsize { get { return _zSize; } }

	#endregion

	#region Constructors

    /// <summary>
    /// Creates a Table object. Specifies the size of each dimension in the multidimensional array. 
    /// 1-, 2-, and 3-dimensional arrays are possible. Arrays with no parameters are also permitted.
    /// </summary>
	public Table() : this(1, 1, 1) { }

    /// <summary>
    /// Creates a Table object. Specifies the size of each dimension in the multidimensional array. 
    /// 1-, 2-, and 3-dimensional arrays are possible. Arrays with no parameters are also permitted.
    /// </summary>
    /// <param name="xSize">The size of the Table on the X-axis.</param>
	public Table(int xSize) : this(xSize, 1, 1) 
	{
		_dimensions = 1;
	}

    /// <summary>
    /// Creates a Table object. Specifies the size of each dimension in the multidimensional array. 
    /// 1-, 2-, and 3-dimensional arrays are possible. Arrays with no parameters are also permitted.
    /// </summary>
    /// <param name="xSize">The size of the Table on the X-axis.</param>
    /// <param name="ySize">The size of the Table on the Y-axis.</param>
	public Table(int xSize, int ySize) : this(xSize, ySize, 1) 
	{
		_dimensions = 2;
	}

    /// <summary>
    /// Creates a Table object. Specifies the size of each dimension in the multidimensional array. 
    /// 1-, 2-, and 3-dimensional arrays are possible. Arrays with no parameters are also permitted.
    /// </summary>
    /// <param name="xSize">The size of the Table on the X-axis.</param>
    /// <param name="ySize">The size of the Table on the Y-axis.</param>
    /// <param name="zSize">The size of the Table on the Z-axis.</param>
	public Table(int xSize, int ySize, int zSize) 
	{
		_data = new int[0];
		xSize = xSize.Clamp(0, xSize);
		ySize = ySize.Clamp(0, ySize);
		zSize = zSize.Clamp(0, zSize);
		resize(xSize, ySize, zSize);
	}

	#endregion

	#region Resizing

	/// <summary>
	/// Resizes the table to the specified dimensions
	/// </summary>
	/// <param name="xSize">Size of the Table on the x-axis</param>
	public void resize(int xSize) 
	{ 
		resize(xSize, 1, 1);
		_dimensions = 1;
	}

	/// <summary>
	/// Resizes the table to the specified dimensions
	/// </summary>
	/// <param name="xSize">Size of the Table on the x-axis</param>
	/// <param name="ySize">Size of the Table on the y-axis</param>
	public void resize(int xSize, int ySize) 
	{ 
		resize(xSize, ySize, 1);
		_dimensions = 2;
	}

	/// <summary>
	/// Resizes the table to the specified dimensions
	/// </summary>
	/// <param name="xSize">Size of the Table on the x-axis</param>
	/// <param name="ySize">Size of the Table on the y-axis</param>
	/// <param name="zSize">Size of the Table on the z-axis</param>
	public void resize(int xSize, int ySize, int zSize)
	{
		int oldXSize = _xSize;
		int oldYSize = _ySize;
		int copyXSize = Math.Min(_xSize, xSize);
		int copyYSize = Math.Min(_ySize, ySize);
		int copyZSize = Math.Min(_zSize, zSize);
		int copySize = copyXSize * copyYSize * copyZSize;
		_xSize = Math.Max(xSize, 0);
		_ySize = Math.Max(ySize, 0);
		_zSize = Math.Max(zSize, 0);
		var newData = new int[xSize * ySize * zSize];

		if (copySize > 0)
		{
			for (int x = 0; x < copyXSize; x++)
			{
				for (int y = 0; y < copyYSize; y++)
				{
					for (int z = 0; z < copyZSize; z++)
					{
						newData[x + _xSize * (y + _ySize * z)] =
							_data[x + oldXSize * (y + oldYSize * z)];
					}
				}
			}
		}
		_data = newData;
		_dimensions = 3;
	}

	#endregion

	#region Get/Set Data

	private int GetData(int x, int y, int z)
	{
		if (_xSize == 0 || _ySize == 0 || _zSize == 0)
			return 0;
		x = x.Clamp(0, _xSize - 1);
		y = y.Clamp(0, _ySize - 1);
		z = z.Clamp(0, _zSize - 1);
		return _data[x + _xSize * (y + _ySize * z)];
	}

	private int GetCircularData(int x, int y, int z)
	{
		if (_xSize == 0 || _ySize == 0 || _zSize == 0)
			return 0;
		x %= _xSize;
		y %= _ySize;
		z = z.Clamp(0, _zSize - 1);
		return _data[x + _xSize * (y + _ySize * z)];
	}

	private void SetData(int x, int y, int z, int value)
	{
		if (!x.IsBetween(0, _xSize - 1) || !y.IsBetween(0, _ySize - 1) || !z.IsBetween(0, _zSize - 1))
			return;
		_data[x + _xSize * (y + _ySize * z)] = value.Clamp(-32768, 32767);
	}

	#endregion

	#region Dump/Load

    /// <summary>
    /// Serializes and dumps the <see cref="Table"/> object in ARC format.
    /// </summary>
    /// <returns>An <see langword="byte"/> array containing the serialized data.</returns>
	public byte[] _arc_dump()
	{
		var byteList = new List<byte>();
		byteList.AddRange(_dimensions.GetBytes());
		byteList.AddRange(_xSize.GetBytes());
		byteList.AddRange(_ySize.GetBytes());
		byteList.AddRange(_zSize.GetBytes());
		int size = _xSize * _ySize * _zSize;
		for (int i = 0; i < size; i++)
			byteList.AddRange(((short)_data[i]).GetBytes());
		return byteList.ToArray();
	}

    /// <summary>
    /// Deserializes and loads a <see cref="Table"/> object saved in ARC format.
    /// </summary>
    /// <param name="bytes">A <see langword="byte"/> array containing the serialized data.</param>
    /// <returns>The deserialized <see cref="Table"/> object.</returns>
	public static Table _arc_load(byte[] bytes)
	{
	    int dimensions = BitConverter.ToInt32(bytes, 0);
		int nx = BitConverter.ToInt32(bytes, 4);
		int ny = BitConverter.ToInt32(bytes, 8);
		int nz = BitConverter.ToInt32(bytes, 12);
		int size = nx * ny * nz;
		var table = new Table(nx, ny, nz);
		var data = new int[size];
		for (int i = 0; i < size; i++)
			data[i] = BitConverter.ToInt16(bytes, 16 + (i * 2));
		table._data = data;
		table._dimensions = dimensions;
		return table;
	}

	#endregion
}