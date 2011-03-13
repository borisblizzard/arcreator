#ifndef ZER0_RGSS_TILEMAP_H
#define ZER0_RGSS_TILEMAP_H

#include "RGSS/Table.h"

#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		class Viewport; // forward declaration of Viewport
		class Bitmap; // forward declaration of Bitmap
		class Table; // forward declaration of Table

		class zer0Export Tilemap
		{
		public:
			Bitmap* autotiles[7];
			/// @brief Table data to represent passable directions of tiles
			/// @todo Modify default methods to allow for more autotiles per map
			//Table flash_data;
			/// @brief Table containing data of each tile
			Table map_data;
			/// @brief The origin point of the x-coordinate
			int ox;
			/// @brief The origin point of the y-coordinate
			int oy;
			/// @brief Table to hold priority data
			Table priorities;
			/// @brief Bitmap used for the tilemap sprite
			Bitmap* tileset;
			/// @brief Visibility factor of tilemap
			bool visible;
			
			/// @brief Basic constructor
			Tilemap();
			/// @brief Constructor to specify viewport
			/// @param[in] value Viewport to set to tilemap
			Tilemap(Viewport* value);
			/// @brief Basic destructor
			~Tilemap();

			/// @brief Returns the viewport specified for the tilemap
			Viewport* getViewport() { return this->viewport; };

			// Instance methods
			/// @brief Frees the tilemap
			void dispose();
			/// @brief Flag for disposed tilemap
			bool disposed();
			/// @brief Updates the tilemap
			void update();
			
		private:
			/// @brief Viewport specified for tilemap sprite
			Viewport* viewport;
		};
	
	}
}
#endif