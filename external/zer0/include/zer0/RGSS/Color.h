#ifndef ZER0_RGSS_COLOR_H
#define ZER0_RGSS_COLOR_H

#include <ruby.h>

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
			//Color();
			/// @brief Basic constructor.
			/// @param[in] r Red component.
			/// @param[in] g Green component.
			/// @param[in] b Blue component.
			/// @param[in] a Alpha component.
			static VALUE initialize(int argc, VALUE *argv, VALUE self);
			//Color(float r, float g, float b, float a = 255.0f);
			/// @brief Destructor.
			//~Color();
			/*
			/// @brief Gets the red component.
			/// @return Red component.
			static VALUE getRed(VALUE self);
			/// @brief Gets the green component.
			/// @return Green component.
			static VALUE getGreen(VALUE self);
			/// @brief Gets the blue component.
			/// @return Blue component.
			static VALUE getBlue(VALUE self);
			/// @brief Gets the alpha component.
			/// @return Alpha component.
			static VALUE getAlpha(VALUE self);
			/// @brief Sets the red component.
			/// @param[in] value Red component.
			/// @note The value will be clamped between -255 and 255.
			static VALUE setRed(VALUE self, VALUE value);
			/// @brief Sets the green component.
			/// @param[in] value Green component.
			/// @note The value will be clamped between -255 and 255.
			static VALUE setGreen(VALUE self, VALUE value);
			/// @brief Sets the blue component.
			/// @param[in] value Blue component.
			/// @note The value will be clamped between -255 and 255.
			static VALUE setBlue(VALUE self, VALUE value);
			/// @brief Sets the alpha component.
			/// @param[in] value Alpha component.
			/// @note The value will be clamped between -255 and 255.
			static VALUE setAlpha(VALUE self, VALUE value);
			*/

			/// @brief Sets the color to the specified value.
			/// @param[in] r Red component.
			/// @param[in] g Green component.
			/// @param[in] b Blue component.
			/// @param[in] a Alpha component.
			/// @note All values will be clamped between -255 and 255.
			static VALUE set(int argc, VALUE *argv, VALUE self);
			/// @brief Exposes this class to Ruby.
			static void createRubyInterface();

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
