#ifndef ZER0_RGSS_TABLE_H
#define ZER0_RGSS_TABLE_H

#include "zer0Export.h"

namespace zer0
{
	namespace RGSS
	{
		/// @brief Emulates RGSS's Table class.
		/// @note Depending on the instance's dimensions, specific method calls will not work. Use the proper method calls.
		class zer0Export Table
		{
		public:
			/// @brief Basic constructor.
			/// @param xSize X dimension size.
			/// @param ySize Y dimension size.
			/// @param zSize Z dimension size.
			Table(int xSize, int ySize = 1, int zSize = 1);
			// @brief Destructor
			~Table();

			/// @brief Gets the X dimension size.
			/// @return X dimension size.
			int getXSize() const { return this->xSize; }
			/// @brief Gets the Y dimension size.
			/// @return Y dimension size.
			int getYSize() const { return this->xSize; }
			/// @brief Gets the Z dimension size.
			/// @return Z dimension size.
			int getZSize() const { return this->xSize; }

			/// @brief Gets the value of an entry at a specific position in the table.
			/// @param[in] x X position.
			/// @return Value at position.
			/// @todo Add out-of-range exception
			short getData(int x) const;
			/// @brief Gets the value of an entry at a specific position in the table.
			/// @param[in] x X position.
			/// @param[in] y Y position.
			/// @return Value at position.
			/// @todo Add out-of-range exception
			short getData(int x, int y) const;
			/// @brief Gets the value of an entry at a specific position in the table.
			/// @param[in] x X position.
			/// @param[in] y Y position.
			/// @param[in] z Z position.
			/// @return Value at position.
			/// @todo Add out-of-range exception
			short getData(int x, int y, int z) const;
			/// @brief Sets the value of an entry at a specific position in the table.
			/// @param[in] x X position.
			/// @param[in] value The new value.
			/// @todo Add out-of-range exception
			void setData(int x, short value);
			/// @brief Sets the value of an entry at a specific position in the table.
			/// @param[in] x X position.
			/// @param[in] y Y position.
			/// @param[in] value The new value.
			/// @todo Add out-of-range exception
			void setData(int x, int y, short value);
			/// @brief Sets the value of an entry at a specific position in the table.
			/// @param[in] x X position.
			/// @param[in] y Y position.
			/// @param[in] z Z position.
			/// @param[in] value The new value.
			/// @todo Add out-of-range exception
			void setData(int x, int y, int z, short value);

			/// @brief Resizes the Table to a new size.
			/// @param xSize New X dimension size.
			/// @param ySize New Y dimension size.
			/// @param zSize New Z dimension size.
			/// @note Entries at intersecting positions will remain in the table.
			void resize(int xSize, int ySize = 1, int zSize = 1);

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
			
		};

	}
}
#endif
