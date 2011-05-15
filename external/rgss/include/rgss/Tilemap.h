#ifndef RGSS_TILEMAP_H
#define RGSS_TILEMAP_H

#include <ruby.h>

#include <hltypes/harray.h>

#include "Table.h"
#include "SourceRenderer.h"
#include "rgssExport.h"

namespace rgss
{
	extern VALUE rb_cTilemap;

	class Bitmap; 
	class Sprite;
	class Table;

	class rgssExport Tilemap : public SourceRenderer
	{
	public:
		/// @brief Disposes this instance.
		void dispose();

		/// @brief Initializes the module.
		static void init();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();
		/// @brief Marks referenced values of bitmap for garbage collection.
		/// @param[in] tilemap Pointer to the Tilemap to mark.
		static void gc_mark(Tilemap* tilemap);
		/// @brief Frees allocated memory.
		/// @param[in] sprite Pointer to the Tilemap to free.
		static void gc_free(Tilemap* tilemap);
		/// @brief Ruby allocation of an instance.
		static VALUE rb_new(VALUE classe);
		/// @brief Initializes this instance, setting the viewport if provided.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Argument is "[viewport]".
		static VALUE rb_initialize(int argc, VALUE* argv, VALUE self);

		/// @brief Sets the offset X coordinate.
		/// @param[in] value Offset X coordinate.
		static VALUE rb_setOX(VALUE self, VALUE value);
		/// @brief Sets the offset Y coordinate.
		/// @param[in] value Offset Y coordinate.
		static VALUE rb_setOY(VALUE self, VALUE value);
		/// @brief Sets the visible flag.
		/// @param[in] value The visible flag.
		static VALUE rb_setVisible(VALUE self, VALUE value);
		/// @brief Gets the tilemap's autotiles.
		/// @return value Array of pointers to autotile bitmaps.
		static VALUE rb_getAutotiles(VALUE self);
		/// @brief Gets the map data.
		/// @return value The map data.
		static VALUE rb_getMapData(VALUE self);
		/// @brief Sets the map data.
		/// @param[in] value The map data.
		static VALUE rb_setMapData(VALUE self, VALUE value);
		/// @brief Gets the priority data.
		/// @return value The priority data.
		static VALUE rb_getPriorities(VALUE self);
		/// @brief Sets the priority data.
		/// @param[in] value The priority data.
		static VALUE rb_setPriorities(VALUE self, VALUE value);
		/// @brief Gets the flash data.
		/// @return value The flash data.
		static VALUE rb_getFlashData(VALUE self);
		/// @brief Sets the flash data.
		/// @param[in] value The flash data.
		static VALUE rb_setFlashData(VALUE self, VALUE value);

		/// @brief Invokes the update method.
		static VALUE rb_update(VALUE self);

	protected:
		/// @brief Original autotile bitmaps.
		VALUE rb_autotiles;
		/// @brief Current autotile bitmaps.
		VALUE rb_currentAutotiles;
		/// @brief Generated bitmaps.
		VALUE rb_generatedAutotiles;
		/// @brief Map data.
		Table* mapData;
		/// @brief Ruby object of map data.
		VALUE rb_mapData;
		/// @brief Priority data.
		Table* priorities;
		/// @brief Ruby object of priority data.
		VALUE rb_priorities;
		/// @brief Flash data.
		Table* flashData;
		/// @brief Ruby object of flash data.
		VALUE rb_flashData;
		/// @brief Horizontal tile sprite count.
		int width;
		/// @brief Vertical tile sprite count.
		int height;
		/// @brief Depth tile sprite count.
		int depth;
		/// @brief Tile sprites.
		/// @note Ruby does not initialize the superclass when it creates an instance of a C++ class so this variable has to be created manually.
		harray<Sprite*>* tileSprites;
		/// @brief Ruby objects of tile sprites.
		/// @note Ruby does not initialize the superclass when it creates an instance of a C++ class so this variable has to be created manually.
		harray<VALUE>* rb_tileSprites;

		/// @brief Updates tile sprites.
		void _updateTileSprites();
		/// @brief Updates autotile bitmaps.
		void _updateAutotiles();

	};

}
#endif