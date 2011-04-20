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

		/// @brief Initializes the module.
		static void init();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();
		/// @brief Frees allocated memory.
		/// @param[in] table Pointer to the Table to free.
		static void gc_free(Table* table);
		/// @brief Ruby allocation of an instance.
		static VALUE rb_new(VALUE classe);
		/// @brief Initializes the instance, setting the dimensions.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "xsize,[ysize [, zsize]]"
		static VALUE rb_initialize(int argc, VALUE* argv, VALUE self);

		/// @brief Creates a C++ version of this class.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "xsize[, ysize[, zsize]]"
		static VALUE create(int argc, VALUE* argv);

		/// @brief Gets the X dimension size.
		/// @return The X dimension size.
		static VALUE rb_getXSize(VALUE self);
		/// @brief Gets the Y dimension size.
		/// @return The Y dimension size.
		static VALUE rb_getYSize(VALUE self);
		/// @brief Gets the Z dimension size.
		/// @return The Z dimension size.
		static VALUE rb_getZSize(VALUE self);

		/// @brief Gets the value of an entry at a specific position in the table.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "x[, y[, z]]".
		/// @return value The value at position.
		static VALUE rb_getData(int argc, VALUE* argv, VALUE self);

		/// @brief Sets the value of an entry at a specific position in the table.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "x[, y[, z]], value".
		static VALUE rb_setData(int argc, VALUE* argv, VALUE self);
			
		/// @brief Resizes the Table to a new size.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "xsize[, ysize[, zsize]]".
		static VALUE rb_resize(int argc, VALUE* argv, VALUE self);

		/// @brief Returns a byte string containing data needed to reconstruct the Tone object.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Only one argument d, it defaults to 0 and is used for object depth.
		/// @return value A byte string.
		static VALUE rb_dump(int argc, VALUE* argv, VALUE self);

		/// @brief Returns an RGSS::Tone object constructed from a byte string.
		/// @param[in] value The byte string from which to load the object.
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
