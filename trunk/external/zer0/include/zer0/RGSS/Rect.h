#ifndef ZER0_RGSS_RECT_H
#define ZER0_RGSS_RECT_H

#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		/// @brief Emulates RGSS's Rect class.
		class zer0Export Rect
		{
		public:
			/// @brief X coordinate.
			int x;
			/// @brief Y coordinate.
			int y;
			/// @brief Rectangle Width.
			int width;
			/// @brief Rectangle Height.
			int height;

			/// @brief Empty constructor.
			Rect();
			/// @brief Basic constructor.
			/// @param[in] x X coordinate.
			/// @param[in] y Y coordinate.
			/// @param[in] width Rectangle width.
			/// @param[in] height Rectangle height.
			Rect(int x, int y, int width, int height);
			/// @brief Destructor.
			~Rect();

			/// @brief Sets the values of the Rectangle.
			/// @param[in] x X coordinate.
			/// @param[in] y Y coordinate.
			/// @param[in] width Rectangle width.
			/// @param[in] height Rectangle height.
			void set(int x, int y, int width, int height);
			/// @brief Sets all values of the Rectangle to 0.
			void empty();

		};
	}
}
#endif
