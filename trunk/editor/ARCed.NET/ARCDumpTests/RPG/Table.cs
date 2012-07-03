using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Collections;
using System.IO;
using ARCDumpTests;
using ARCed;

public class Table 
{
	private int[] _data;
	private int _xSize, _ySize, _zSize, _dimensions;

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

	public Table() : this(1, 1, 1) { }

	public Table(int xSize) : this(xSize, 1, 1) 
	{
		_dimensions = 1;
	}

	public Table(int xSize, int ySize) : this(xSize, ySize, 1) 
	{
		_dimensions = 2;
	}

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
		int[] newData = new int[xSize * ySize * zSize];

		if (copySize > 0)
		{
			for (int x = 0; x < copyXSize; x++)
			{
				for (int y = 0; y < copyYSize; y++)
				{
					for (int z = 0; z < copyZSize; z++)
					{
						newData[x + _xSize * (y + _ySize * z)] =
							_data[x + oldXSize * (y + oldXSize * z)];
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

	#region Serialization

	public byte[] _arc_dump()
	{
		List<byte> byteList = new List<byte>();
		byteList.AddRange(_dimensions.GetBytes());
		byteList.AddRange(_xSize.GetBytes());
		byteList.AddRange(_ySize.GetBytes());
		byteList.AddRange(_zSize.GetBytes());
		int size = _xSize * _ySize * _zSize;
		for (int i = 0; i < size; i++)
			byteList.AddRange(((short)_data[i]).GetBytes());
		return byteList.ToArray();
	}

	public static Table _arc_load(byte[] bytes)
	{
		int nx, ny, nz, dimensions, size;
		dimensions = BitConverter.ToInt32(bytes, 0);
		nx = BitConverter.ToInt32(bytes, 4);
		ny = BitConverter.ToInt32(bytes, 8);
		nz = BitConverter.ToInt32(bytes, 12);
		size = nx * ny * nz;
		Table table = new Table(nx, ny, nz);
		int[] data = new int[size];
		for (int i = 0; i < size; i++)
			data[i] = BitConverter.ToInt16(bytes, 16 + (i * 2));
		table._data = data;
		table._dimensions = dimensions;
		return table;
	}

	#endregion
}