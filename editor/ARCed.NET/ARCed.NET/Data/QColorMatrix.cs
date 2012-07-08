using System;
using System.Drawing;
using System.Drawing.Imaging;

namespace ARCed.Data
{
	/// <summary>
	/// QColorMatrix
	/// http://www.codeguru.com/Cpp/G-M/gdi/gdi/article.php/c3667
	/// 
	/// Extension of the GDI+ struct ColorMatrix.
	/// Adds some member functions so you can actually do something with it.
	/// Use QColorMatrix like ColorMatrix to update the ImmageAttributes class.
	/// Use at your own risk. Comments welcome.
	///
	/// See: http://www.sgi.com/grafica/matrix/
	/// http://www.sgi.com/software/opengl/advanced98/notes/node182.html
	///
	/// (chr) 2003, Sjaak Priester, Amsterdam.
	/// mailto:sjaak@sjaakpriester.nl
	/// 
	/// This C# port from original C++ code is done by:
	/// (C) 2010, Vasian Cepa
	/// http://madebits.com
	/// This port fixes a bug in TransformVector and offers some new convenience methods.
	/// This class is not thread-safe.
	/// </summary>
	public class QColorMatrix
	{
		#region privateData

		private const int MatrixLength = 5;
		private float[,] m = new float[MatrixLength, MatrixLength];
		private const float rad = (float)(Math.PI / 180.0);

		/*
		QColorMatrix rotates hues while preserving the luminance. In other words: only the color information is modified, not the black-and-white levels. If you would remove the color from an _srcTexture (by setting the saturation to zero), rotating the hue has no effect.
		Because the luminance of the brightest red on the computer screen (RGB 255, 0, 0) is way lower than the luminance of the brightest green (RGB 0, 255, 0), the brightest red does not translate into the brightest green, but into a darker green.
		It all has to do with the 'luminance weights' which are assigned to the R, G, and B elements of the color (see the const's in the top part of QColorMatrix.cpp). If all three luminance weights were equal (1.0), the brightest red would translate to the brightest green after rotation. However, rotating the hue would also mean modifying the luminance.
		See http://www.graficaobscura.com/matrix/ for some more information on hue rotation.
		For what it's worth, the Photoshop hue control works similar to QColormatrix in this respect.
		*/

		// The luminance weight factors for the RGB color space.
		// These values are actually preferable to the better known factors of
		// Y = 0.30R + 0.59G + 0.11B, the formula which is used in color television technique.
		public static float lumR = 0.3086f;
		public static float lumG = 0.6094f;
		public static float lumB = 0.0820f;

		private static QColorMatrix preHue = new QColorMatrix();
		private static QColorMatrix postHue = new QColorMatrix();
		private static bool initialized = false;

		#endregion privateData

		/// <summary>
		/// gdi+ type
		/// </summary>
		public enum MatrixOrder { MatrixOrderPrepend = 0, MatrixOrderAppend = 1 };

		#region ctors

		public QColorMatrix()
		{
			Reset();
		}

		public QColorMatrix(float[,] m)
		{
			if (m == null)
			{
				Reset();
				return;
			}
			Copy(m);
		}

		public QColorMatrix(float[][] m)
		{
			FromJaggedMatrix(m);
		}

		public QColorMatrix(QColorMatrix qm)
		{
			Copy(qm);
		}

		public QColorMatrix(ColorMatrix cm)
		{
			FromColorMatrix(cm);
		}

		#endregion ctors

		public float[,] Matrix { get { return m; } }

		#region conversions

		public void FromJaggedMatrix(float[][] m)
		{
			Reset();
			if (m == null)
			{
				return;
			}
			for (int i = 0; i < m.Length; i++)
			{
				if (m[i] == null)
				{
					throw new ArgumentException();
				}
				for (int j = 0; j < m[i].Length; j++)
				{
					this.m[i, j] = m[i][j];
				}
			}
		}

		public float[][] ToJaggedMatrix()
		{
			float[][] t = new float[MatrixLength][];
			for (int i = 0; i < t.Length; i++)
			{
				t[i] = new float[MatrixLength];
				for (int j = 0; j < t[i].Length; j++)
				{
					t[i][j] = this.m[i, j];
				}
			}
			return t;
		}

		public void FromColorMatrix(ColorMatrix cm)
		{
			if (cm == null)
			{
				Reset();
				return;
			}
			for (int i = 0; i < MatrixLength; i++)
			{
				for (int j = 0; j < MatrixLength; j++)
				{
					m[i, j] = cm[i, j];
				}
			}
		}

		public ColorMatrix ToColorMatrix()
		{
			ColorMatrix cm = new ColorMatrix();
			for (int i = 0; i < MatrixLength; i++)
			{
				for (int j = 0; j < MatrixLength; j++)
				{
					cm[i, j] = m[i, j];
				}
			}
			return cm;
		}

		#endregion conversions

		#region core

		/// <summary>
		/// set to identity matrix
		/// </summary>
		public void Reset()
		{
			for (int i = 0; i < MatrixLength; i++)
			{
				for (int j = 0; j < MatrixLength; j++)
				{
					m[i, j] = ((i == j) ? 1.0f : 0.0f);
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
			return TransformVector(v, false);
		}

		public static float[] Color2Vector(Color c)
		{
			if (c == null) return null;
			float[] p = new float[4];
			p[0] = (float)c.R;
			p[1] = (float)c.G;
			p[2] = (float)c.B;
			p[3] = (float)c.A;
			return p;
		}

		public static Color Vector2Color(float[] p)
		{
			if (p == null || (p.Length < 4))
			{
				throw new ArgumentException();
			}
			return Color.FromArgb((int)p[3], (int)p[0], (int)p[1], (int)p[2]);
		}

		public float[] TransformVector(float[] v, bool normalize)
		{
			if (v == null || (v.Length < 4))
			{
				throw new ArgumentException();
			}
			float[] temp = new float[4];
			for (int x = 0; x < 4; x++)
			{
				temp[x] = 255.0f * m[4, x];
				for (int y = 0; y < 4; y++)
				{
					temp[x] += v[y] * m[y, x];
				}
			}
			for (int x = 0; x < 4; x++)
			{
				v[x] = temp[x];
				if (normalize)
				{
					if (v[x] < 0) v[x] = 0.0f;
					else if (v[x] > 255.0f) v[x] = 255.0f;
				}
			}
			return v;
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
					TransformVector(
						Color2Vector(colors[i]), true));
			}
			return colors;
		}


		public void Multiply(QColorMatrix matrix)
		{
			Multiply(matrix, MatrixOrder.MatrixOrderPrepend);
		}

		/// <summary>
		/// Unlike the original C++ code we multiply all value here.
		/// </summary>
		public void Multiply(QColorMatrix matrix, MatrixOrder order)
		{
			if (matrix == null) throw new ArgumentException();
			float[,] a = null;
			float[,] b = null;

			if (order == MatrixOrder.MatrixOrderAppend)
			{
				a = matrix.m;
				b = m;
			}
			else
			{
				a = m;
				b = matrix.m;
			}

			float[,] temp = new float[MatrixLength, MatrixLength];
			for (int y = 0; y < MatrixLength; y++)
			{
				for (int x = 0; x < MatrixLength; x++)
				{
					float t = 0;
					for (int i = 0; i < MatrixLength; i++)
					{
						t += b[y, i] * a[i, x];
					}
					temp[y, x] = t;
				}
			}
			for (int y = 0; y < MatrixLength; y++)
			{
				for (int x = 0; x < MatrixLength; x++)
				{
					m[y, x] = temp[y, x];
				}
			}
		}

		#endregion core

		#region scale

		/// <summary>
		/// Update this matrix with the product of itself and a scaling vector.
		/// </summary>
		public void Scale(float scaleRed, float scaleGreen, float scaleBlue,
			float scaleOpacity)
		{
			Scale(scaleRed, scaleGreen, scaleBlue,
				scaleOpacity, MatrixOrder.MatrixOrderPrepend);
		}

		public void Scale(float scaleRed, float scaleGreen, float scaleBlue,
			float scaleOpacity, MatrixOrder order)
		{
			QColorMatrix qm = new QColorMatrix();
			qm.m[0, 0] = scaleRed;
			qm.m[1, 1] = scaleGreen;
			qm.m[2, 2] = scaleBlue;
			qm.m[3, 3] = scaleOpacity;
			Multiply(qm, order);
		}

		/// <summary>
		/// Scale just the three colors with the same amount, leave opacity unchanged
		/// </summary>
		public void ScaleColors(float scale)
		{
			ScaleColors(scale, MatrixOrder.MatrixOrderPrepend);
		}

		public void ScaleColors(float scale, MatrixOrder order)
		{
			Scale(scale, scale, scale, 1.0f, order);
		}

		public void ScaleOpacity(float scaleOpacity)
		{
			ScaleOpacity(scaleOpacity, MatrixOrder.MatrixOrderPrepend);
		}

		public void ScaleOpacity(float scaleOpacity, MatrixOrder order)
		{
			Scale(1.0f, 1.0f, 1.0f, scaleOpacity, order);
		}

		#endregion scale

		#region traslate

		/// <summary>
		/// Update this matrix with the product of itself and a translation vector.
		/// </summary>
		public void Translate(float offsetRed, float offsetGreen, float offsetBlue,
			float offsetOpacity)
		{
			Translate(offsetRed, offsetGreen, offsetBlue,
				offsetOpacity, MatrixOrder.MatrixOrderPrepend);
		}

		public void Translate(float offsetRed, float offsetGreen, float offsetBlue,
			float offsetOpacity, MatrixOrder order)
		{
			QColorMatrix qm = new QColorMatrix();
			qm.m[4, 0] = offsetRed;
			qm.m[4, 1] = offsetGreen;
			qm.m[4, 2] = offsetBlue;
			qm.m[4, 3] = offsetOpacity;
			Multiply(qm, order);
		}

		public void TranslateColors(float offset)
		{
			TranslateColors(offset, MatrixOrder.MatrixOrderPrepend);
		}

		public void TranslateColors(float offset, MatrixOrder order)
		{
			Translate(offset, offset, offset, 0.0f, order);
		}

		public void TranslateOpacity(float offsetOpacity)
		{
			TranslateOpacity(offsetOpacity, MatrixOrder.MatrixOrderPrepend);
		}

		public void TranslateOpacity(float offsetOpacity, MatrixOrder order)
		{
			Translate(0.0f, 0.0f, 0.0f, offsetOpacity, order);
		}

		#endregion traslate

		#region rotate

		// Rotate the matrix around one of the color axes. The color of the rotation
		// axis is unchanged, the other two colors are rotated in color space.
		// The angle phi is in degrees (-180.0f... 180.0f).

		public void RotateRed(float phi)
		{
			RotateRed(phi, MatrixOrder.MatrixOrderPrepend);
		}
		public void RotateGreen(float phi)
		{
			RotateGreen(phi, MatrixOrder.MatrixOrderPrepend);
		}
		public void RotateBlue(float phi)
		{
			RotateBlue(phi, MatrixOrder.MatrixOrderPrepend);
		}
		public void RotateRed(float phi, MatrixOrder order)
		{
			RotateColor(phi, 2, 1, order);
		}
		public void RotateGreen(float phi, MatrixOrder order)
		{
			RotateColor(phi, 0, 2, order);
		}
		public void RotateBlue(float phi, MatrixOrder order)
		{
			RotateColor(phi, 1, 0, order);
		}

		#endregion rotate

		#region shear

		// Shear the matrix in one of the color planes. The color of the color plane
		// is influenced by the two other colors.

		public void ShearRed(float green, float blue)
		{
			ShearRed(green, blue, MatrixOrder.MatrixOrderPrepend);
		}

		public void ShearGreen(float red, float blue)
		{
			ShearGreen(red, blue, MatrixOrder.MatrixOrderPrepend);
		}

		public void ShearBlue(float red, float green)
		{
			ShearBlue(red, green, MatrixOrder.MatrixOrderPrepend);
		}

		public void ShearRed(float green, float blue, MatrixOrder order)
		{
			ShearColor(0, 1, green, 2, blue, order);
		}

		public void ShearGreen(float red, float blue, MatrixOrder order)
		{
			ShearColor(1, 0, red, 2, blue, order);
		}

		public void ShearBlue(float red, float green, MatrixOrder order)
		{
			ShearColor(2, 0, red, 1, green, order);
		}

		#endregion shear

		#region HueSat

		public void SetSaturation(float saturation)
		{
			SetSaturation(saturation, MatrixOrder.MatrixOrderPrepend);
		}

		/// <summary>
		/// Set the saturation of the matrix. Saturation of 0.0f yields B&W, 1.0f is neutral.
		/// </summary>
		public void SetSaturation(float saturation, MatrixOrder order)
		{
			// For the theory behind this, see the web sites at the top of this file.
			// In short: if saturation is 1.0f, m becomes the identity matrix, and this matrix is
			// unchanged. If saturation is 0.0f, each color is scaled by it's luminance weight.
			float satCompl = 1.0f - saturation;
			float satComplR = lumR * satCompl;
			float satComplG = lumG * satCompl;
			float satComplB = lumB * satCompl;

			float[,] tm = new float[,]
            {
                {satComplR + saturation,	satComplR,	satComplR,	0.0f, 0.0f} ,
                {satComplG,	satComplG + saturation,	satComplG,	0.0f, 0.0f},
		        {satComplB,	satComplB,	satComplB + saturation,	0.0f, 0.0f},
		        {0.0f,	0.0f,	0.0f,	1.0f,	0.0f},
		        {0.0f,	0.0f,	0.0f,	0.0f,	1.0f}
            };

			QColorMatrix qm = new QColorMatrix(tm);
			Multiply(qm, order);
		}

		/// <summary>
		/// Rotate the hue around the grey axis, keeping luminance fixed. Greys are fixed,
		/// all other colors change.
		/// </summary>
		public void RotateHue(float phi)
		{
			InitHue();
			// Rotate the grey vector to the blue axis.
			Multiply(preHue, MatrixOrder.MatrixOrderAppend);
			// Rotate around the blue axis
			RotateBlue(phi, MatrixOrder.MatrixOrderAppend);
			Multiply(postHue, MatrixOrder.MatrixOrderAppend);
		}

		#endregion HueSat

		#region convenience

		public void SetContrast(float scale)
		{
			ScaleColors(scale);
		}

		public void SetBrightness(float offset)
		{
			TranslateColors(offset, MatrixOrder.MatrixOrderAppend);
		}

		public void SetSaturation2(float saturation)
		{
			SetSaturation(saturation, MatrixOrder.MatrixOrderAppend);
		}

		#endregion convenience

		#region private

		private static void InitHue()
		{
			const float greenRotation = 35.0f;
			//	const REAL greenRotation = 39.182655f;

			// NOTE: theoretically, greenRotation should have the value of 39.182655 degrees,
			// being the angle for which the sine is 1/(sqrt(3)), and the cosine is sqrt(2/3).
			// However, I found that using a slightly smaller angle works better.
			// In particular, the greys in the _srcTexture are not visibly affected with the smaller
			// angle, while they deviate a little bit with the theoretical value.
			// An explanation escapes me for now.
			// If you rather stick with the theory, change the comments in the previous lines.


			if (!initialized)
			{
				initialized = true;
				// Rotating the hue of an _srcTexture is a rather convoluted task, involving several matrix
				// multiplications. For efficiency, we prepare two static matrices.
				// This is by far the most complicated part of this class. For the background
				// theory, refer to the sgi-sites mentioned at the top of this file.

				// Prepare the preHue matrix.
				// Rotate the grey vector in the green plane.
				preHue.RotateRed(45.0f);

				// Next, rotate it again in the green plane, so it coincides with the blue axis.
				preHue.RotateGreen(-greenRotation, MatrixOrder.MatrixOrderAppend);

				// Hue rotations keep the color luminations constant, so that only the hues change
				// visible. To accomplish that, we shear the blue plane.
				float[] lum = new float[] { lumR, lumG, lumB, 1.0f };

				// Transform the luminance vector.
				preHue.TransformVector(lum);

				// Calculate the shear factors for red and green.
				float red = lum[0] / lum[2];
				float green = lum[1] / lum[2];

				// Shear the blue plane.
				preHue.ShearBlue(red, green, MatrixOrder.MatrixOrderAppend);

				// Prepare the postHue matrix. This holds the opposite transformations of the
				// preHue matrix. In fact, postHue is the inversion of preHue.
				postHue.ShearBlue(-red, -green);
				postHue.RotateGreen(greenRotation, MatrixOrder.MatrixOrderAppend);
				postHue.RotateRed(-45.0f, MatrixOrder.MatrixOrderAppend);
			}
		}

		/// <summary>
		/// x and y are the indices of the value to receive the sin(phi) value
		/// </summary>
		/// <param name="phi">phi is in degrees</param>
		private void RotateColor(float phi, int x, int y, MatrixOrder order)
		{
			phi *= rad;
			QColorMatrix qm = new QColorMatrix();

			qm.m[x, x] = qm.m[y, y] = (float)Math.Cos(phi);

			float s = (float)Math.Sin(phi);
			qm.m[y, x] = s;
			qm.m[x, y] = -s;

			Multiply(qm, order);
		}

		private void ShearColor(int x, int y1, float d1, int y2, float d2, MatrixOrder order)
		{
			QColorMatrix qm = new QColorMatrix();
			qm.m[y1, x] = d1;
			qm.m[y2, x] = d2;
			Multiply(qm, order);
		}

		private void Copy(QColorMatrix qm)
		{
			if (qm == null)
			{
				Reset();
				return;
			}
			Copy(qm.m);
		}

		private void Copy(float[,] m)
		{
			if ((m == null) || (m.Length != this.m.Length))
			{
				throw new ArgumentException();
			}
			Array.Copy(m, this.m, m.Length);
		}

		#endregion private

	}//EOC
}
