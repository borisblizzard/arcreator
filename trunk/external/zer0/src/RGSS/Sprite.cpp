#include <hltypes/util.h>

#include "RGSS/Sprite.h"
#include "RGSS/Color.h"
#include "RGSS/Rect.h"
#include "RGSS/Tone.h"
#include "RGSS/Viewport.h"
#include "RGSS/Bitmap.h"

namespace zer0
{
	namespace RGSS
	{
		Sprite::Sprite() 
		{
			this->viewport = new Viewport();
		}
		Sprite::Sprite(Viewport value)
		{
			this->viewport = value;
		}
		Sprite::~Sprite()
		{
			/// @todo Implement deconstructor;
		}

		void Sprite::setAngle(int value)
		{
			this->angle = hclamp(value, 0, 359);
		}
		void Sprite::setBitmap(Bitmap value)
		{
			this->bitmap = value;
			/// @todo Include Exception handling
			// Idea: Add constructors to simply initialize sprite's bitmap with init argument
		}
		void Sprite::setOpacity(float value)
		{
			this->opacity = hclamp(value, 0.0f, 255.0f);
		}
		void Sprite::setZoomX(float value)
		{
			this->zoom_x = hclamp(value, 0.0f, value);
		}
		void Sprite::setZoomY(float value)
		{
			this->zoom_y = hclamp(value, 0.0f, value);
		}

		void Sprite::dispose()
		{

		}
		bool Sprite::disposed()
		{

		}
		void Sprite::flash(Color color, int duration)
		{

		}
		void Sprite::update()
		{

		}
	}
}
