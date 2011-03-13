#include "RGSS/Tilemap.h"
#include "RGSS/Bitmap.h"
#include "RGSS/Table.h"
#include "RGSS/Viewport.h"

namespace zer0
{
	namespace RGSS
	{
		Tilemap::Tilemap() : map_data(20, 15, 3), priorities(20, 15, 3)
		{
			this->viewport = new Viewport();
		}

		Tilemap::Tilemap(Viewport* value) : map_data(20, 15, 3), priorities(20, 15, 3)
		{
			this->viewport = value;
		}
	
		/// @todo add RGSS Error calls
		Tilemap::~Tilemap()
		{
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
			return true;
		}
	
	}
}