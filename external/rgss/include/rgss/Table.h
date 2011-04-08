#ifndef RGSS_TABLE_H
#define RGSS_TABLE_H

#include <ruby.h>

#include "rgssExport.h"

namespace rgss
{
	extern VALUE rb_cTable;

	/// @brief Emulates RGSS's Table class.
	/// @note Depending on the instance's dimensions, specific method calls will not work. Use the proper method calls.
	class rgssExport Table
	{
	public:
		/// @todo Dummy for now, needs to be removed later.
		Table() { }
		// @todo Dummy for now, needs to be removed later.
		~Table() { }

		/// @brief Intializes the module.
		static void init();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();
		/// @brief Frees allocated memory.
		/// @param[in] table Table to free.
		static void gc_free(Table* table);
		/// @brief Ruby allocation of an instance.
		static VALUE rb_new(VALUE classe);
		/// @brief Sets the rect to the specified value.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		static VALUE rb_initialize(int argc, VALUE* argv, VALUE self);
		/// @brief Gets the X dimension size.
		/// @return X dimension size.

		/// @brief Creates a C++ version of this class.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "xsize[, ysize[, zsize]]"
		static VALUE create(int argc, VALUE* argv);

		static VALUE rb_getXSize(VALUE self);
		/// @brief Gets the Y dimension size.
		/// @return Y dimension size.
		static VALUE rb_getYSize(VALUE self);
		/// @brief Gets the Z dimension size.
		/// @return Z dimension size.
		static VALUE rb_getZSize(VALUE self);

		/// @brief Gets the value of an entry at a specific position in the table.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "x[, y[, z]]".
		/// @return Value at position.
		static VALUE rb_getData(int argc, VALUE* argv, VALUE self);

		/// @brief Sets the value of an entry at a specific position in the table.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "x, value[, y[, z]]" where value is shifted right for each optional argument (it's allways the last argument).
		static VALUE rb_setData(int argc, VALUE* argv, VALUE self);
			
			
		/// @brief Resizes the Table to a new size.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "xSize[, ySize[, zSize]]".
		static VALUE rb_resize(int argc, VALUE* argv, VALUE self);

		/// @brief returns a bytestring containging data needed to ronconstruct the Tone object
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note only one argument d, it defualts to 0 and is used for object depth
		/// @return byte string.
		static VALUE rb_dump(int argc, VALUE* argv, VALUE self);

		/// @brief returns a Tone object constructed form a byte string
		/// @param[in] value the byte string forom which to load the object
		static VALUE rb_load(VALUE self, VALUE value);

	protected:
		/// @brief X dimension size.
		int xSize;
		/// @brief Y dimension size.
		int ySize;
		/// @brief Z dimension size.
		int zSize;
		/// @brief Table entry data.
		short* data;

		/// @brief Allocates memory for a new table.
		/// @param xSize X dimension size.
		/// @param ySize Y dimension size.
		/// @param zSize Z dimension size.
		/// @return Pointer to the newly allocated memory.
		short* _createData(int xSize, int ySize, int zSize) const;

		/// @brief Resizes the Table to a new size.
		/// @param xSize New X dimension size.
		/// @param ySize New Y dimension size.
		/// @param zSize New Z dimension size.
		/// @note Entries at intersecting positions will remain in the table.
		void _resize(int xSize, int ySize = 1, int zSize = 1);
			
	};

}
#endif
