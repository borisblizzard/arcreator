#include "RGSS/Tilemap.h"
#include "RGSS/Bitmap.h"
#include "RGSS/Table.h"
#include "RGSS/Viewport.h"

namespace zer0
{
	namespace RGSS
	{
	
		Tilemap::Tilemap()
		{
			this->viewport = new Viewport();
		}

		Tilemap::Tilemap(Viewport value)
		{
			this->viewport = value;
		}
	
		Tilemap::~Tilemap()
		{
			/// @todo Implement Deconstructor 
		}

		void Tilemap::update()
		{

		}

		void Tilemap::dispose()
		{
			/// @todo Implement dispose
		}

		bool Tilemap::disposed()
		{

		}
	
	}
}