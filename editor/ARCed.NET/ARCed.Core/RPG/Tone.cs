#region Using Directives

using System;
using System.Collections.Generic;
using ARCed;

#endregion

namespace RPG
{
	/// <summary>
	/// The color tone class. Each component is handled with a <see langword="float"/> value.
	/// </summary>
	public class Tone
	{
		#region Private Fields

		private float _red, _green, _blue, _gray;

		#endregion

		#region Public Properties

		/// <summary>
		/// The red value (-255-255). Values out of range are automatically corrected.
		/// </summary>
		public float red
		{
			get { return this._red; }
			set { this._red = value.Clamp(-255, 255); }
		}

		/// <summary>
		/// The green value (-255-255). Values out of range are automatically corrected.
		/// </summary>
		public float green
		{
			get { return this._green; }
			set { this._green = value.Clamp(-255, 255); }
		}
		/// <summary>
		/// The blue value (-255-255). Values out of range are automatically corrected.
		/// </summary>
		public float blue
		{
			get { return this._blue; }
			set { this._blue = value.Clamp(-255, 255); }
		}

		/// <summary>
		/// The gray value (0-255). Values out of range are automatically corrected.
		/// </summary>
		public float gray
		{
			get { return this._gray; }
			set { this._gray = value.Clamp(0, 255); }
		}

		#endregion

		#region Constructors

		/// <summary>
		/// Creates a Tone object with all values initialized as 0.0.
		/// </summary>
		public Tone() : this(0.0f, 0.0f, 0.0f) { }

		/// <summary>
		/// Creates a Tone object. If gray is omitted, it is assumed at 0.
		/// </summary>
		/// <param name="red">The red value (-255-255)</param>
		/// <param name="green">The green value (-255-255)</param>
		/// <param name="blue">The blue value (-255-255)</param>
		/// <param name="gray">The gray value (0-255)</param>
		public Tone(float red, float green, float blue, float gray = 0.0f)
		{
			this.red = red;
			this.green = green;
			this.blue = blue;
			this.gray = gray;
		}

		#endregion

		#region Public Methods

		/// <summary>
		/// Sets all components at once. Gray remains the same.
		/// </summary>
		/// <param name="red">The red value (-255-255)</param>
		/// <param name="green">The green value (-255-255)</param>
		/// <param name="blue">The blue value (-255-255)</param>
		public void set(float red, float green, float blue)
		{
			this.set(red, green, blue, this.gray);
		}

		/// <summary>
		/// Sets all components at once. 
		/// </summary>
		/// <param name="red">The red value (-255-255)</param>
		/// <param name="green">The green value (-255-255)</param>
		/// <param name="blue">The blue value (-255-255)</param>
		/// <param name="gray">The gray value (0-255)</param>
		public void set(float red, float green, float blue, float gray)
		{
			this.red = red;
			this.green = green;
			this.blue = blue;
			this.gray = gray;
		}

		/// <summary>
		/// Returns a <see langword="string"/> that represents the current object.
		/// </summary>
		/// <returns>String representation of object.</returns>
		public override string ToString()
		{
			return string.Format("{0}, {1}, {2}, {3}", this.red, this.green, this.blue, this.gray);
		}

		#endregion

		#region Dump/Load

		/// <summary>
		/// Serializes and dumps the <see cref="Color"/> object in ARC format.
		/// </summary>
		/// <returns>An <see langword="byte"/> array containing the serialized data.</returns>
		public byte[] _arc_dump()
		{
			var byteList = new List<byte>();
			byteList.AddRange(BitConverter.GetBytes(this._red));
			byteList.AddRange(BitConverter.GetBytes(this._green));
			byteList.AddRange(BitConverter.GetBytes(this._blue));
			byteList.AddRange(BitConverter.GetBytes(this._gray));
			return byteList.ToArray();
		}

		/// <summary>
		/// Deserializes and loads a <see cref="Color"/> object saved in ARC format.
		/// </summary>
		/// <param name="bytes">A <see langword="byte"/> array containing the serialized data.</param>
		/// <returns>The deserialized <see cref="Color"/> object.</returns>
		public static Tone _arc_load(byte[] bytes)
		{
			Tone c = new Tone();
			c._red = (float)BitConverter.ToSingle(bytes, 0);
			c._green = (float)BitConverter.ToSingle(bytes, 4);
			c._blue = (float)BitConverter.ToSingle(bytes, 8);
			c._gray = (float)BitConverter.ToSingle(bytes, 12);
			return c;
		}

		#endregion

	}
}
