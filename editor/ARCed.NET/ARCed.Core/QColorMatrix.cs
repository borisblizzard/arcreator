#region Using Directives

using System;
using System.Drawing;
using System.Drawing.Imaging;

#endregion

namespace ARCed.Core
{
	/// <summary>
	/// Extension of the GDI+ struct ColorMatrix.
	/// </summary>
	public class QColorMatrix
    {
        #region Nested Enum

        /// <summary>
        /// GDI+ type for MatrixOrder
        /// </summary>
        public enum MatrixOrder
        {
            /// <summary>
            /// Prepend matrix order
            /// </summary>
            MatrixOrderPrepend = 0x00,
            /// <summary>
            /// Append matrix order
            /// </summary>
            MatrixOrderAppend = 0x01
        }

        #endregion

        #region Private Constants

        private const float LUM_R = 0.3086f;
        private const float LUM_G = 0.6094f;
        private const float LUM_B = 0.0820f;
		private const int MATRIX_LENGTH = 5;
        private const float RAD = (float)(Math.PI / 180.0);
		
        #endregion

        #region Private Fields

        private readonly float[,] _matrix = new float[MATRIX_LENGTH, MATRIX_LENGTH];
	    private static readonly QColorMatrix _preHue = new QColorMatrix();
		private static readonly QColorMatrix _postHue = new QColorMatrix();
	    private static bool _initialized;

		#endregion 

        #region Public Properties

        /// <summary>
        /// Gets the matrix
        /// </summary>
        public float[,] Matrix { get { return this._matrix; } }

        #endregion

		#region Constructor

        /// <summary>
        /// Default constructor
        /// </summary>
		public QColorMatrix()
		{
			this.Reset();
		}

        /// <summary>
        /// Constructor specifying matrix data
        /// </summary>
        /// <param name="matrixData">Matrix data to initialize with</param>
		public QColorMatrix(float[,] matrixData)
		{
			if (matrixData == null)
			{
				this.Reset();
				return;
			}
			Copy(matrixData);
		}

        /// <summary>
        /// Constructor specifying matrix data
        /// </summary>
        /// <param name="matrixData">Matrix data to initialize with</param>
		public QColorMatrix(float[][] matrixData)
		{
			this.FromJaggedMatrix(matrixData);
		}

        /// <summary>
        /// Constructor specifying matrix data
        /// </summary>
        /// <param name="matrixData">Matrix data to initialize with</param>
		public QColorMatrix(QColorMatrix matrixData)
		{
			Copy(matrixData);
		}

        /// <summary>
        /// Constructor specifying matrix data
        /// </summary>
        /// <param name="colorMatrix">Matrix data to initialize with</param>
		public QColorMatrix(ColorMatrix colorMatrix)
		{
			this.FromColorMatrix(colorMatrix);
		}

		#endregion 

		#region Conversions

        /// <summary>
        /// Returns the given matrix data as a jagged matrix
        /// </summary>
        /// <param name="matrixData">Matrix data</param>
		public void FromJaggedMatrix(float[][] matrixData)
		{
			this.Reset();
			if (matrixData == null)
			{
				return;
			}
			for (int i = 0; i < matrixData.Length; i++)
			{
				if (matrixData[i] == null)
				{
					throw new ArgumentException();
				}
				for (int j = 0; j < matrixData[i].Length; j++)
				{
					this._matrix[i, j] = matrixData[i][j];
				}
			}
		}

        /// <summary>
        /// Converts the matrix to a jagged array of data
        /// </summary>
        /// <returns>Jagged array</returns>
		public float[][] ToJaggedMatrix()
		{
			var t = new float[MATRIX_LENGTH][];
			for (int i = 0; i < t.Length; i++)
			{
				t[i] = new float[MATRIX_LENGTH];
				for (int j = 0; j < t[i].Length; j++)
				{
					t[i][j] = this._matrix[i, j];
				}
			}
			return t;
		}

        /// <summary>
        /// Translates the matrix from a <seealso cref="ColorMatrix"/>.
        /// </summary>
        /// <param name="colorMatrix">ColorMatrix to translate from</param>
		public void FromColorMatrix(ColorMatrix colorMatrix)
		{
			if (colorMatrix == null)
			{
				this.Reset();
				return;
			}
			for (int i = 0; i < MATRIX_LENGTH; i++)
			{
				for (int j = 0; j < MATRIX_LENGTH; j++)
				{
					this._matrix[i, j] = colorMatrix[i, j];
				}
			}
		}

        /// <summary>
        /// Converts the matrix to a <seealso cref="ColorMatrix"/> and returns it.
        /// </summary>
        /// <returns>ColorMatrix representation</returns>
		public ColorMatrix ToColorMatrix()
		{
			var cm = new ColorMatrix();
			for (int i = 0; i < MATRIX_LENGTH; i++)
			{
				for (int j = 0; j < MATRIX_LENGTH; j++)
				{
					cm[i, j] = this._matrix[i, j];
				}
			}
			return cm;
		}

		#endregion

		#region Core

		/// <summary>
		/// Set to identity matrix
		/// </summary>
		public void Reset()
		{
			for (int i = 0; i < MATRIX_LENGTH; i++)
			{
				for (int j = 0; j < MATRIX_LENGTH; j++)
				{
					this._matrix[i, j] = ((i == j) ? 1.0f : 0.0f);
				}
			}
		}

		/// <summary>
		/// Multiply the vector v by the matrix in place. 
		/// v points to an array of at least four values,
		/// representing R, G, B and A.
		/// </summary>
		public float[] TransformVector(float[] v)
		{
			return this.TransformVector(v, false);
		}

        /// <summary>
        /// Converts a <seealso cref="Color"/> object to a vector and returns it.
        /// </summary>
        /// <param name="color">Color to convert</param>
        /// <returns>Vector representation of the color</returns>
		public static float[] Color2Vector(Color color)
		{
			var p = new float[4];
			p[0] = color.R;
			p[1] = color.G;
			p[2] = color.B;
			p[3] = color.A;
			return p;
		}

        /// <summary>
        /// Converts a vector array to a <seealso cref="Color"/> object.
        /// </summary>
        /// <param name="vector">Floar array vector</param>
        /// <returns>Color representation of the vector</returns>
		public static Color Vector2Color(float[] vector)
		{
			if (vector == null || (vector.Length < 4))
			{
				throw new ArgumentException();
			}
			return Color.FromArgb((int)vector[3], (int)vector[0], (int)vector[1], (int)vector[2]);
		}

        /// <summary>
        /// Transforms a vector
        /// </summary>
        /// <param name="vector">Vector to transform</param>
        /// <param name="normalize">Flag to normalize data before returning</param>
        /// <returns>Transformed vector.</returns>
		public float[] TransformVector(float[] vector, bool normalize)
		{
			if (vector == null || (vector.Length < 4))
			{
				throw new ArgumentException();
			}
			var temp = new float[4];
			for (int x = 0; x < 4; x++)
			{
				temp[x] = 255.0f * this._matrix[4, x];
				for (int y = 0; y < 4; y++)
				{
					temp[x] += vector[y] * this._matrix[y, x];
				}
			}
			for (int x = 0; x < 4; x++)
			{
				vector[x] = temp[x];
				if (normalize)
				{
					if (vector[x] < 0) vector[x] = 0.0f;
					else if (vector[x] > 255.0f) vector[x] = 255.0f;
				}
			}
			return vector;
		}

		/// <summary>
		/// Multiply each color by the matrix.
		/// </summary>
		public Color[] TransformColors(Color[] colors)
		{
			if (colors == null) return null;
			for (int i = 0; i < colors.Length; i++)
			{
				colors[i] = Vector2Color(
					this.TransformVector(
						Color2Vector(colors[i]), true));
			}
			return colors;
		}
        
        /// <summary>
        /// Multiplies the given matrix
        /// </summary>
        /// <param name="matrix">Matrix to multiply</param>
		public void Multiply(QColorMatrix matrix)
		{
			this.Multiply(matrix, MatrixOrder.MatrixOrderPrepend);
		}

        /// <summary>
        /// Multiply the given matrix using the specified matrix order.
        /// </summary>
        /// <param name="matrix">Matrix to multiply</param>
        /// <param name="order">Order to multiply with</param>
		public void Multiply(QColorMatrix matrix, MatrixOrder order)
		{
			if (matrix == null) throw new ArgumentException();
            float[,] a, b;
			if (order == MatrixOrder.MatrixOrderAppend)
			{
				a = matrix._matrix;
				b = this._matrix;
			}
			else
			{
				a = this._matrix;
				b = matrix._matrix;
			}

			var temp = new float[MATRIX_LENGTH, MATRIX_LENGTH];
			for (int y = 0; y < MATRIX_LENGTH; y++)
			{
				for (int x = 0; x < MATRIX_LENGTH; x++)
				{
					float t = 0;
					for (int i = 0; i < MATRIX_LENGTH; i++)
					{
						t += b[y, i] * a[i, x];
					}
					temp[y, x] = t;
				}
			}
			for (int y = 0; y < MATRIX_LENGTH; y++)
			{
				for (int x = 0; x < MATRIX_LENGTH; x++)
				{
					this._matrix[y, x] = temp[y, x];
				}
			}
		}

		#endregion 

		#region Scale

        /// <summary>
        /// Update this matrix with the product of itself and a scaling vector.
        /// </summary>
        /// <param name="scaleRed">Red scaling value</param>
        /// <param name="scaleGreen">Green scaling value</param>
        /// <param name="scaleBlue">Blue scaling value</param>
        /// <param name="scaleOpacity">Alpha scaling value</param>
		public void Scale(float scaleRed, float scaleGreen, float scaleBlue,
			float scaleOpacity)
		{
			this.Scale(scaleRed, scaleGreen, scaleBlue,
				scaleOpacity, MatrixOrder.MatrixOrderPrepend);
		}

        /// <summary>
        /// Update this matrix with the product of itself and a scaling vector.
        /// </summary>
        /// <param name="scaleRed">Red scaling value</param>
        /// <param name="scaleGreen">Green scaling value</param>
        /// <param name="scaleBlue">Blue scaling value</param>
        /// <param name="scaleOpacity">Alpha scaling value</param>
        /// <param name="order">Matrix order</param>
		public void Scale(float scaleRed, float scaleGreen, float scaleBlue,
			float scaleOpacity, MatrixOrder order)
		{
			var qm = new QColorMatrix();
			qm._matrix[0, 0] = scaleRed;
			qm._matrix[1, 1] = scaleGreen;
			qm._matrix[2, 2] = scaleBlue;
			qm._matrix[3, 3] = scaleOpacity;
			this.Multiply(qm, order);
		}
        
        /// <summary>
        /// Scale just the three colors with the same amount, leave opacity unchanged
        /// </summary>
        /// <param name="scale">Scale value</param>
		public void ScaleColors(float scale)
		{
			this.ScaleColors(scale, MatrixOrder.MatrixOrderPrepend);
		}

        /// <summary>
        /// Scale just the three colors with the same amount, leave opacity unchanged
        /// </summary>
        /// <param name="scale">Scale value</param>
        /// <param name="order">Matrix order</param>
		public void ScaleColors(float scale, MatrixOrder order)
		{
			this.Scale(scale, scale, scale, 1.0f, order);
		}

        /// <summary>
        /// Scales the matrix opacity
        /// </summary>
        /// <param name="scaleOpacity">Alpha scaling value</param>
		public void ScaleOpacity(float scaleOpacity)
		{
			this.ScaleOpacity(scaleOpacity, MatrixOrder.MatrixOrderPrepend);
		}

        /// <summary>
        /// Scales the matrix opacity
        /// </summary>
        /// <param name="scaleOpacity">Alpha scaling value</param>
        /// <param name="order">Matrix order</param>
		public void ScaleOpacity(float scaleOpacity, MatrixOrder order)
		{
			this.Scale(1.0f, 1.0f, 1.0f, scaleOpacity, order);
		}

		#endregion

		#region Translate

        /// <summary>
        /// Update this matrix with the product of itself and a translation vector.
        /// </summary>
        /// <param name="offsetRed">Red offset value</param>
        /// <param name="offsetGreen">Green offset value</param>
        /// <param name="offsetBlue">Blue offset value</param>
        /// <param name="offsetOpacity">Alpha offset value</param>
		public void Translate(float offsetRed, float offsetGreen, float offsetBlue,
			float offsetOpacity)
		{
			this.Translate(offsetRed, offsetGreen, offsetBlue,
				offsetOpacity, MatrixOrder.MatrixOrderPrepend);
		}

        /// <summary>
        /// Update this matrix with the product of itself and a translation vector.
        /// </summary>
        /// <param name="offsetRed">Red offset value</param>
        /// <param name="offsetGreen">Green offset value</param>
        /// <param name="offsetBlue">Blue offset value</param>
        /// <param name="offsetOpacity">Alpha offset value</param>
        /// <param name="order">Matrix order</param>
		public void Translate(float offsetRed, float offsetGreen, float offsetBlue,
			float offsetOpacity, MatrixOrder order)
		{
			var qm = new QColorMatrix();
			qm._matrix[4, 0] = offsetRed;
			qm._matrix[4, 1] = offsetGreen;
			qm._matrix[4, 2] = offsetBlue;
			qm._matrix[4, 3] = offsetOpacity;
			this.Multiply(qm, order);
		}

        /// <summary>
        /// Translate matrix colors
        /// </summary>
        /// <param name="offset">Offset value</param>
		public void TranslateColors(float offset)
		{
			this.TranslateColors(offset, MatrixOrder.MatrixOrderPrepend);
		}

        /// <summary>
        /// Translate matrix colors
        /// </summary>
        /// <param name="offset">Offset value</param>
        /// <param name="order">Matrix order</param>
		public void TranslateColors(float offset, MatrixOrder order)
		{
			this.Translate(offset, offset, offset, 0.0f, order);
		}

        /// <summary>
        /// Translate matrix opacity
        /// </summary>
        /// <param name="offsetOpacity">Alpha offset value</param>
		public void TranslateOpacity(float offsetOpacity)
		{
			this.TranslateOpacity(offsetOpacity, MatrixOrder.MatrixOrderPrepend);
		}

        /// <summary>
        /// Translate matrix opacity
        /// </summary>
        /// <param name="offsetOpacity">Alpha offset value</param>
        /// <param name="order">Matrix order</param>
		public void TranslateOpacity(float offsetOpacity, MatrixOrder order)
		{
			this.Translate(0.0f, 0.0f, 0.0f, offsetOpacity, order);
		}

		#endregion 

		#region Rotate

        /// <summary>
        /// Rotate the matrix around the red color axes. The color of the rotation 
        /// axis is unchanged, the other two colors are rotated in color space.
        /// </summary>
        /// <param name="phi">Angle in degrees to rotate (-180.0f... 180.0f).</param>
		public void RotateRed(float phi)
		{
			this.RotateRed(phi, MatrixOrder.MatrixOrderPrepend);
		}

        /// <summary>
        /// Rotate the matrix around the green color axes. The color of the rotation 
        /// axis is unchanged, the other two colors are rotated in color space.
        /// </summary>
        /// <param name="phi">Angle in degrees to rotate (-180.0f... 180.0f).</param>
		public void RotateGreen(float phi)
		{
			this.RotateGreen(phi, MatrixOrder.MatrixOrderPrepend);
		}

        /// <summary>
        /// Rotate the matrix around the blue color axes. The color of the rotation 
        /// axis is unchanged, the other two colors are rotated in color space.
        /// </summary>
        /// <param name="phi">Angle in degrees to rotate (-180.0f... 180.0f).</param>
		public void RotateBlue(float phi)
		{
			this.RotateBlue(phi, MatrixOrder.MatrixOrderPrepend);
		}

        /// <summary>
        /// Rotate the matrix around the red color axes. The color of the rotation 
        /// axis is unchanged, the other two colors are rotated in color space.
        /// </summary>
        /// <param name="phi">Angle in degrees to rotate (-180.0f... 180.0f).</param>
        /// <param name="order">Matrix order</param>
		public void RotateRed(float phi, MatrixOrder order)
		{
			this.RotateColor(phi, 2, 1, order);
		}

        /// <summary>
        /// Rotate the matrix around the green color axes. The color of the rotation 
        /// axis is unchanged, the other two colors are rotated in color space.
        /// </summary>
        /// <param name="phi">Angle in degrees to rotate (-180.0f... 180.0f).</param>
        /// <param name="order">Matrix order</param>
		public void RotateGreen(float phi, MatrixOrder order)
		{
			this.RotateColor(phi, 0, 2, order);
		}

        /// <summary>
        /// Rotate the matrix around the blue color axes. The color of the rotation 
        /// axis is unchanged, the other two colors are rotated in color space.
        /// </summary>
        /// <param name="phi">Angle in degrees to rotate (-180.0f... 180.0f).</param>
        /// <param name="order">Matrix order</param>
		public void RotateBlue(float phi, MatrixOrder order)
		{
			this.RotateColor(phi, 1, 0, order);
		}

		#endregion 

		#region Shear

		// Shear the matrix in one of the color planes. The color of the color plane
		// is influenced by the two other colors.

        /// <summary>
        /// Shear the matrix in the red color plane. The color is influenced by the other two planes.
        /// </summary>
        /// <param name="green">Green color plane</param>
        /// <param name="blue">Blue color plane</param>
		public void ShearRed(float green, float blue)
		{
			this.ShearRed(green, blue, MatrixOrder.MatrixOrderPrepend);
		}

        /// <summary>
        /// Shear the matrix in the green color plane. The color is influenced by the other two planes.
        /// </summary>
        /// <param name="red">Red color plane</param>
        /// <param name="blue">Blue color plane</param>
		public void ShearGreen(float red, float blue)
		{
			this.ShearGreen(red, blue, MatrixOrder.MatrixOrderPrepend);
		}

        /// <summary>
        /// Shear the matrix in the blue color plane. The color is influenced by the other two planes.
        /// </summary>
        /// <param name="red">Red color plane</param>
        /// <param name="green">Green color plane</param>
		public void ShearBlue(float red, float green)
		{
			this.ShearBlue(red, green, MatrixOrder.MatrixOrderPrepend);
		}

        /// <summary>
        /// Shear the matrix in the red color plane. The color is influenced by the other two planes.
        /// </summary>
        /// <param name="green">Green color plane</param>
        /// <param name="blue">Blue color plane</param>
        /// <param name="order">Matrix order</param>
		public void ShearRed(float green, float blue, MatrixOrder order)
		{
			this.ShearColor(0, 1, green, 2, blue, order);
		}

        /// <summary>
        /// Shear the matrix in the green color plane. The color is influenced by the other two planes.
        /// </summary>
        /// <param name="red">Red color plane</param>
        /// <param name="blue">Blue color plane</param>
        /// <param name="order">Matrix order</param>
		public void ShearGreen(float red, float blue, MatrixOrder order)
		{
			this.ShearColor(1, 0, red, 2, blue, order);
		}

        /// <summary>
        /// Shear the matrix in the blue color plane. The color is influenced by the other two planes.
        /// </summary>
        /// <param name="red">Red color plane</param>
        /// <param name="green">Green color plane</param>
        /// <param name="order">Matrix order</param>
		public void ShearBlue(float red, float green, MatrixOrder order)
		{
			this.ShearColor(2, 0, red, 1, green, order);
		}

		#endregion 

		#region Hue/Saturation

        /// <summary>
        /// Sets the matrix saturation
        /// </summary>
        /// <param name="saturation">Saturation value</param>
		public void SetSaturation(float saturation)
		{
			this.SetSaturation(saturation, MatrixOrder.MatrixOrderPrepend);
		}

        /// <summary>
        /// Set the saturation of the matrix. Saturation of 0.0f yields black and white, 1.0f is neutral.
        /// </summary>
        /// <param name="saturation">Saturation value</param>
        /// <param name="order">Matrix order</param>
		public void SetSaturation(float saturation, MatrixOrder order)
		{
			float satCompl = 1.0f - saturation;
			float satComplR = LUM_R * satCompl;
			float satComplG = LUM_G * satCompl;
			float satComplB = LUM_B * satCompl;
			var tm = new[,]
            {
                {satComplR + saturation,	satComplR,	satComplR,	0.0f, 0.0f} ,
                {satComplG,	satComplG + saturation,	satComplG,	0.0f, 0.0f},
		        {satComplB,	satComplB,	satComplB + saturation,	0.0f, 0.0f},
		        {0.0f,	0.0f,	0.0f,	1.0f,	0.0f},
		        {0.0f,	0.0f,	0.0f,	0.0f,	1.0f}
            };
			var qm = new QColorMatrix(tm);
			this.Multiply(qm, order);
		}


        /// <summary>
        /// Rotate the hue around the gray axis, keeping luminance fixed. Grays are fixed,
        /// all other colors change.
        /// </summary>
        /// <param name="phi">Degrees to rotate</param>
		public void RotateHue(float phi)
		{
			InitHue();
			this.Multiply(_preHue, MatrixOrder.MatrixOrderAppend);
			this.RotateBlue(phi, MatrixOrder.MatrixOrderAppend);
			this.Multiply(_postHue, MatrixOrder.MatrixOrderAppend);
		}

		#endregion 

		#region Convenience

        /// <summary>
        /// Sets the matrix contrast
        /// </summary>
        /// <param name="scale">Constrast scale value</param>
		public void SetContrast(float scale)
		{
			this.ScaleColors(scale);
		}

        /// <summary>
        /// Sets the matrix brightness
        /// </summary>
        /// <param name="offset">Brightness offset value</param>
		public void SetBrightness(float offset)
		{
			this.TranslateColors(offset, MatrixOrder.MatrixOrderAppend);
		}

        /// <summary>
        /// Sets the matrix saturation using <seealso cref="MatrixOrder.MatrixOrderAppend"/> order.
        /// </summary>
        /// <param name="saturation">Saturation value.</param>
		public void SetSaturation2(float saturation)
		{
			this.SetSaturation(saturation, MatrixOrder.MatrixOrderAppend);
		}

		#endregion 

		#region Private Methods

		private static void InitHue()
		{
			const float greenRotation = 35.0f;
			if (!_initialized)
			{
				_initialized = true;
				_preHue.RotateRed(45.0f);
				_preHue.RotateGreen(-greenRotation, MatrixOrder.MatrixOrderAppend);
				var lum = new[] { LUM_R, LUM_G, LUM_B, 1.0f };
				_preHue.TransformVector(lum);
				float red = lum[0] / lum[2];
				float green = lum[1] / lum[2];
				_preHue.ShearBlue(red, green, MatrixOrder.MatrixOrderAppend);
				_postHue.ShearBlue(-red, -green);
				_postHue.RotateGreen(greenRotation, MatrixOrder.MatrixOrderAppend);
				_postHue.RotateRed(-45.0f, MatrixOrder.MatrixOrderAppend);
			}
		}

        /// <summary>
        /// X and Y are the indices of the value to receive the sin(phi) value
        /// </summary>
        /// <param name="phi">phi is in degrees</param>
        /// <param name="x">x value</param>
        /// <param name="y">y value</param>
        /// <param name="order">Matrix order</param>
		private void RotateColor(float phi, int x, int y, MatrixOrder order)
		{
			phi *= RAD;
			var qm = new QColorMatrix();
			qm._matrix[x, x] = qm._matrix[y, y] = (float)Math.Cos(phi);
			var s = (float)Math.Sin(phi);
			qm._matrix[y, x] = s;
			qm._matrix[x, y] = -s;
			this.Multiply(qm, order);
		}

		private void ShearColor(int x, int y1, float d1, int y2, float d2, MatrixOrder order)
		{
			var qm = new QColorMatrix();
			qm._matrix[y1, x] = d1;
			qm._matrix[y2, x] = d2;
			this.Multiply(qm, order);
		}

		private void Copy(QColorMatrix qm)
		{
			if (qm == null)
			{
				this.Reset();
				return;
			}
			Copy(qm._matrix);
		}

		private void Copy(float[,] m)
		{
			if ((m == null) || (m.Length != this._matrix.Length))
			{
				throw new ArgumentException();
			}
			Array.Copy(m, this._matrix, m.Length);
		}

		#endregion 

	}
}
