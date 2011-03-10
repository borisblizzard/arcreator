#ifndef ZER0_RGSS_TONE_H
#define ZER0_RGSS_TONE_H

#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		/// @brief Emulates RGSS's Tone class.
		class zer0Export Tone
		{
		public:
			/// @brief Empty constructor.
			Tone();
			/// @brief Basic constructor.
			/// @param[in] r Red component.
			/// @param[in] g Green component.
			/// @param[in] b Blue component.
			/// @param[in] gr Gray component.
			Tone(float r, float g, float b, float gr = 255.0f);
			/// @brief Destructor.
			~Tone();

			/// @brief Gets the red component.
			/// @return Red component.
			float getRed() { return this->red; }
			/// @brief Gets the green component.
			/// @return Green component.
			float getGreen() { return this->red; }
			/// @brief Gets the blue component.
			/// @return Blue component.
			float getBlue() { return this->red; }
			/// @brief Gets the gray component.
			/// @return Gray component.
			float getGray() { return this->red; }
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
			/// @brief Sets the gray component.
			/// @param[in] value Gray component.
			/// @note The value will be clamped between -255 and 255.
			void setGray(float value);

			/// @brief Sets the color to the specified value.
			/// @param[in] r Red component.
			/// @param[in] g Green component.
			/// @param[in] b Blue component.
			/// @param[in] gr Gray component.
			/// @note All values will be clamped between -255 and 255.
			void set(float r, float g, float b, float gr = 255.0f);

		protected:
			/// @brief Red component.
			float red;
			/// @brief Green component.
			float green;
			/// @brief Blue component.
			float blue;
			/// @brief Gray component.
			float gray;

		};
	
	}
}
#endif
