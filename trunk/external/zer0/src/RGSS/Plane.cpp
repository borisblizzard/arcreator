#include <hltypes/util.h>

#include "RGSS/Plane.h"
#include "RGSS/Bitmap.h"
#include "RGSS/Color.h"
#include "RGSS/Tone.h"
#include "RGSS/Viewport.h"

namespace zer0
{
	namespace RGSS
	{
	
		Plane::Plane()
		{
			this->viewport = new Viewport();
		}
		Plane::Plane(Viewport* value)
		{
			this->viewport = value;
		}
		Plane::~Plane()
		{
			/// @todo Implement deconstructor
		}

		void Plane::setBitmap(Bitmap* value)
		{
			this->bitmap = value;
			/// @todo Include Exception handling
		}
		void Plane::setOpacity(float value)
		{
			this->opacity = hclamp(value, 0.0f, 255.0f);
		}
		void Plane::setZoomX(float value)
		{
			this->zoomX = hclamp(value, 0.0f, value);
		}
		void Plane::setZoomY(float value)
		{
			this->zoomY = hclamp(value, 0.0f, value);
		}

		void Plane::dispose()
		{

		}
		bool Plane::disposed()
		{
			return true;
		}
	}
}
