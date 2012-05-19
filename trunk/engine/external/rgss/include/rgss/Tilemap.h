#ifndef RGSS_TILEMAP_H
#define RGSS_TILEMAP_H

#include <ruby.h>

#include <hltypes/harray.h>

#include "Table.h"
#include "SourceRenderer.h"
#include "rgssExport.h"

#define MAX_AUTOTILES 7

namespace rgss
{
	extern VALUE rb_cTilemap;

	class Bitmap;
	class SystemSprite;
	class Table;

	class rgssExport Tilemap : public SourceRenderer
	{
	public:
		/// @brief Constructor.
		Tilemap();
		/// @brief Destructor.
		~Tilemap();
		/// @brief Initializes the basic object.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		void initialize(VALUE rb_viewport);
		/// @brief Disposes this object.
		void dispose();
		/// @brief Ruby garbage collector marking.
		void mark();

		/// @brief Gets the collection flag.
		/// @return True if this object is not to be actually rendered.
		bool isCollection() { return true; }

		/// @brief Makes sure all sprites are up to date.
		void update();

		/// @brief Initializes.
		static void init();
		/// @brief Destroys.
		static void destroy();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();
		/// @brief Ruby allocation of an instance.
		static VALUE rb_new(VALUE classe);
		/// @brief Initializes this instance, setting the viewport if provided.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Argument is "[viewport]".
		static VALUE rb_initialize(int argc, VALUE* argv, VALUE self);
		/// @brief Used to prevent for cloning.
		/// @param[in] original The original.
		static VALUE rb_initialize_clone(VALUE self, VALUE original);
		/// @brief Used to prevent for duping.
		/// @param[in] original The original.
		static VALUE rb_initialize_dup(VALUE self, VALUE original);

		/// @brief Gets the tilemap's autotiles.
		/// @return Array of pointers to autotile bitmaps.
		static VALUE rb_getAutotiles(VALUE self);
		/// @brief Gets the map data.
		/// @return The map data.
		static VALUE rb_getMapData(VALUE self);
		/// @brief Sets the map data.
		/// @param[in] value The map data.
		static VALUE rb_setMapData(VALUE self, VALUE value);
		/// @brief Gets the priority data.
		/// @return The priority data.
		static VALUE rb_getPriorities(VALUE self);
		/// @brief Sets the priority data.
		/// @param[in] value The priority data.
		static VALUE rb_setPriorities(VALUE self, VALUE value);

		/// @brief Invokes the update method.
		static VALUE rb_update(VALUE self);

	protected:
		/// @brief Original autotile bitmaps.
		VALUE rb_autotiles;
		/// @brief Current autotile bitmaps.
		VALUE rb_currentAutotiles;
		/// @brief Map data.
		Table* mapData;
		/// @brief Ruby object of map data.
		VALUE rb_mapData;
		/// @brief Priority data.
		Table* priorities;
		/// @brief Ruby object of priority data.
		VALUE rb_priorities;
		/// @brief Horizontal tile sprite count.
		int width;
		/// @brief Vertical tile sprite count.
		int height;
		/// @brief Depth tile sprite count.
		int depth;
		/// @brief Autotile update counter.
		int autotileUpdateCount;
		/// @brief Generated bitmaps.
		Bitmap* generatedAutotiles[MAX_AUTOTILES];
		/// @brief Tile sprites.
		harray<SystemSprite*> tileSprites;
		/// @brief Main tileset bitmap.

		/// @brief Updates autotile bitmaps.
		void _updateAutotiles();
		/// @brief Updates tile sprites.
		void _updateTileSprites();

	};

}
#endif