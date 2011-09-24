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
		/// @brief Gets the Z size.
		/// @return The Z size.
		int getZSize() { return this->zSize; }

		/// @brief Gets the table entry at a specific position.
		/// @param[in] x X coordinate.
		/// @param[in] y Y coordinate.
		/// @param[in] z Z coordinate.
		/// @return The table entry at a specific position.
		short getData(int x, int y = 0, int z = 0);
		/// @brief Gets the table entry at a specific position with circular x, y rotation.
		/// @param[in] x X coordinate.
		/// @param[in] y Y coordinate.
		/// @param[in] z Z coordinate.
		/// @return The table entry at a specific position.
		short getCircularData(int x, int y = 0, int z = 0);

		/// @brief Initializes.
		static void init();
		/// @brief Destroys.
		static void destroy();
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
		/// @brief Used for clone and dup.
		/// @param[in] original The original.
		static VALUE rb_initialize_copy(VALUE self, VALUE original);

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

		/// @brief Returns a byte stream containing serialization data for Marshal.
		/// @param[in] argc Number of arguments.
		/// @param[in] argv Pointer to first argument.
		/// @note Arguments are "[depth = -1]".
		/// @return Data byte stream.
		static VALUE rb_dump(int argc, VALUE* argv, VALUE self);
		/// @brief Returns an RGSS::Table object constructed from a serialized Marshal byte stream.
		/// @param[in] stream The byte stream from which to load the object.
		static VALUE rb_load(VALUE self, VALUE stream);

		/// @brief Returns a byte stream containing serialization data.
		/// @return Data byte stream.
		static VALUE rb_arcDump(VALUE self);
		/// @brief Returns an RGSS::Table object constructed from a serialized byte stream.
		/// @param[in] stream The byte stream from which to load the object.
		static VALUE rb_arcLoad(VALUE self, VALUE stream);

	protected:
		/// @brief Number of dimensions
		int dimensions;
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
		/// @note Entries at intersecting positions will remain in the table.
		void _resize(int xSize);
		/// @brief Resizes the Table to a new size.
		/// @param xSize New X dimension size.
		/// @param ySize New Y dimension size.
		/// @note Entries at intersecting positions will remain in the table.
		void _resize(int xSize, int ySize);
		/// @brief Resizes the Table to a new size.
		/// @param xSize New X dimension size.
		/// @param ySize New Y dimension size.
		/// @param zSize New Z dimension size.
		/// @note Entries at intersecting positions will remain in the table.
		void _resize(int xSize, int ySize, int zSize);
			
	};

}
#endif
