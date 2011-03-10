#ifndef ZER0_RGSS_COLOR_H
#define ZER0_RGSS_COLOR_H

#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		/// @brief Emulates RGSS's Color class.
		class zer0Export Color
		{
		public:
			/// @brief Empty constructor.
			Color();
			/// @brief Basic constructor.
			/// @param[in] r Red component.
			/// @param[in] g Green component.
			/// @param[in] b Blue component.
			/// @param[in] a Alpha component.
			Color(float r, float g, float b, float a = 255.0f);
			/// @brief Destructor.
			~Color();

			/// @brief Gets the red component.
			/// @return Red component.
			float getRed() { return this->red; }
			/// @brief Gets the green component.
			/// @return Green component.
			float getGreen() { return this->red; }
			/// @brief Gets the blue component.
			/// @return Blue component.
			float getBlue() { return this->red; }
			/// @brief Gets the alpha component.
			/// @return Alpha component.
			float getAlpha() { return this->red; }
			/// @brief Sets the red component.
			/// @param[in] value Red component.
			/// @note The value will be clamped between -255 and 255.
			void setRed(float value);
			/// @brief Sets the green component.
			/// @param[in] value Green component.
			/// @note The value will be clamped between -255 and 255.
			void setGreen(float value);
			/// @brief Sets the blue component.
			/// @param[in] value Blue component.
			/// @note The value will be clamped between -255 and 255.
			void setBlue(float value);
			/// @brief Sets the alpha component.
			/// @param[in] value Alpha component.
			/// @note The value will be clamped between -255 and 255.
			void setAlpha(float value);

			/// @brief Sets the color to the specified value.
			/// @param[in] r Red component.
			/// @param[in] g Green component.
			/// @param[in] b Blue component.
			/// @param[in] a Alpha component.
			/// @note All values will be clamped between -255 and 255.
			void set(float r, float g, float b, float a = 255.0f);
		
		protected:
			/// @brief Red component.
			float red;
			/// @brief Green component.
			float green;
			/// @brief Blue component.
			float blue;
			/// @brief Alpha component.
			float alpha;

		};
	
	}
}
#endif
