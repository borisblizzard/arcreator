#ifndef ZER0_RGSS_TILEMAP_H
#define ZER0_RGSS_TILEMAP_H

#include <ruby.h>

#include "RGSS/Table.h"
#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		static VALUE rb_cTilemap;

		class Viewport; 
		class Bitmap; 
		class Table; 

		class zer0Export Tilemap
		{
		public:
			/// @todo Dummy for now, needs to be removed later.
			Tilemap() { }
			/// @todo Dummy for now, needs to be removed later.
			~Tilemap() { }

			/// @brief Exposes this class to Ruby.
			static void createRubyInterface();
			/// @brief Wraps this instance into a Ruby cobject.
			/// @return Ruby object.
			VALUE wrap();
			/// @brief Marks referenced values of bitmap for garbage collection.
			/// @param[in] bitmap Bitmap to mark.
			static void gc_mark(Tilemap* tilemap);
			/// @brief Ruby allocation of an instance.
			static VALUE rb_new(VALUE classe);
			/// @brief Sets the bitmap dimensions
			/// @param[in] argc Number of arguments.
			/// @param[in] argv Pointer to first argument.
			/// @note Argument is "[viewport]".
			static VALUE rb_initialize(int argc, VALUE* argv, VALUE self);
			/// @brief Gets a string representation of the instance.
			/// @return String representation of the instance.
			static VALUE rb_inspect(VALUE self);
			/// @brief Disposes this object.
			static VALUE rb_dispose(VALUE self);

			/// @brief Gets the tilemap's autotiles.
			/// @return Array of pointers to autotile bitmaps.
			static VALUE rb_getAutotiles(VALUE self);
			/// @brief Sets the tilemap's autotiles.
			/// @param[in] Array of pointers for each autotile bitmap.
			static VALUE rb_setAutotiles(VALUE self, VALUE* value);
			/// @brief Gets the tilemap's map data.
			/// @return Table that contains tile info.
			static VALUE rb_getMapData(VALUE self);
			/// @brief Sets the tilemap's map data.
			/// @param[in] Table to set as the tilemap's map data.
			static VALUE rb_setMapData(VALUE self, VALUE* value);
			/// @brief Gets the tilemap's origin point on the x-axis.
			/// @return Integer value of the starting point.
			static VALUE rb_getOx(VALUE self);
			/// @brief Sets the tilemap's origin point on the x-axis.
			/// @param[in] Integer value to set for the origin point.
			static VALUE rb_setOx(VALUE self, VALUE value);
			/// @brief Gets the tilemap's origin point on the y-axis.
			/// @return Integer value of the starting point.
			static VALUE rb_getOy(VALUE self);
			/// @brief Sets the tilemap's origin point on the y-axis.
			/// @param[in] Integer value to set for the origin point.
			static VALUE rb_setOy(VALUE self, VALUE value);
			/// @brief Gets the tilemap's priority data.
			/// @return Table that contains priority data.
			static VALUE rb_getPriorities(VALUE self);
			/// @brief Sets the tilemap's priority data.
			/// @param[in] Table to use for the map's priorities.
			static VALUE rb_setPriorities(VALUE self, VALUE* value);
			/// @brief Gets the tilemap's flash data.
			/// @return Table used to represent possible movement.
			static VALUE rb_getFlashData(VALUE self);
			/// @brief Sets the tilemap's flash data.
			/// @param[in] Table to represent possible movement.
			static VALUE rb_setFlashData(VALUE self, VALUE* value);
			/// @brief Gets the tilemap's tileset data.
			/// @return Bitmap used for the tilemap.
			static VALUE rb_getTileset(VALUE self);
			/// @brief Sets the tilemap's tileset bitmap.
			/// @param[in] Bitmap to use for the tilemap's tileset.
			static VALUE rb_setTileset(VALUE self, VALUE* value);
			/// @brief Gets the tilemap's visibility value.
			/// @return Bool whether or not tilemap is visible.
			static VALUE Tilemap::rb_getVisible(VALUE self);
			/// @brief Sets the tilemap's visibility value.
			/// @param[in] Bool value to set for tilemap's visibility.
			static VALUE Tilemap::rb_setVisible(VALUE self, VALUE value);
			/// @brief Gets the tilemap's viewport.
			/// @return Viewport used for the tilemap.
			static VALUE rb_getViewport(VALUE self);

			/// @brief Invokes the update method.
			static VALUE rb_update(VALUE self);
			/// @brief Gets the truth value if the tilemap has been disposed.
			/// @return Bool value of instance disposal.
			static VALUE rb_isDisposed(VALUE self);

		protected:
			/// @brief Pointers to each autotile bitmap.
			/// @todo Modify default methods to allow for more autotiles per map
			Bitmap* autotiles[7];
			/// @brief Table data to represent passable directions of tiles
			Table* flash_data;
			/// @brief Table containing data of each tile
			Table* map_data;
			/// @brief The origin point of the x-coordinate
			int ox;
			/// @brief The origin point of the y-coordinate
			int oy;
			/// @brief Table to hold priority data
			Table* priorities;
			/// @brief Bitmap used for the tilemap sprite
			Bitmap* tileset;
			/// @brief Visibility factor of tilemap
			bool visible;
			/// @brief Viewport specified for tilemap sprite
			Viewport* viewport;
		};
	
	}
}
#endif