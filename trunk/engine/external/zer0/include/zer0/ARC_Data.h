#ifndef ZER0_ARC_DATA_H
#define ZER0_ARC_DATA_H

#include <ruby.h>

#include <hltypes/harray.h>
#include <hltypes/hfile.h>
#include <hltypes/hmap.h>
#include <hltypes/hstring.h>

#include "zer0Export.h"

namespace zer0
{
	extern VALUE rb_mARC_Data;

	class zer0Export ARC_Data
	{
	public:
		/// @brief Serializer version.
		static hstr Version;
		/// @brief Type ID mapping.
		static hmap<VALUE, unsigned char> Types;

		/// @brief Initializes the module.
		static void init();
		/// @brief Destroys the module.
		static void destroy();
		/// @brief Exposes this class to Ruby.
		static void createRubyInterface();

		/// @brief Dumps an object into a stream.
		/// @param[in] stream IO stream.
		/// @param[in] object Ruby object to dump.
		static VALUE rb_dump(VALUE self, VALUE filename, VALUE object);
		/// @brief Loads an object from a stream.
		/// @param[in] stream IO stream.
		/// @return Ruby object loaded from stream.
		static VALUE rb_load(VALUE self, VALUE filename);

	private:
		/// @brief The file to use.
		static hfile file;
		/// @brief String mapping.
		static harray<VALUE> strings;
		/// @brief Array mapping.
		static harray<VALUE> arrays;
		/// @brief Hash mapping.
		static harray<VALUE> hashes;
		/// @brief Object mapping.
		static harray<VALUE> objects;

		/// @brief Resets all internal variables for data reading.
		static void _resetSerializer();

		/// @brief Gets the appropriate class from a class path.
		/// @param[in] Path of the class.
		/// @return Ruby class object from the path.
		static VALUE __get_class_object(hstr class_path);
		/// @brief Tries to map the object into the mapping.
		/// @param[in] data The VALUE array.
		/// @param[in] obj The object to map.
		/// @return True if object was mapped, false if object has been previously already mapped.
		static bool __try_map(harray<VALUE> data, VALUE obj);
		/// @brief Map the object into the mapping.
		/// @param[in] data The VALUE array.
		/// @param[in] obj The object to map.
		static void __map(harray<VALUE> data, VALUE obj);
		/// @brief Finds a mapped object by ID.
		/// @param[in] data The VALUE array.
		/// @param[in] id ID of the object to find.
		/// @return Qnil if there is no object with the ID, otherwise the object mapped under the ID.
		static VALUE __find_mapped(harray<VALUE> data, int id);
		/// @brief Dumps an int32.
		/// @param[in] obj int32 to dump.
		/// @todo Switch with a macro.
		static void __dump_int32(int obj);
		/// @brief Loads a dumped int32.
		/// @return Loaded int32.
		/// @todo Switch with a macro.
		static int __load_int32();
		
		/// @brief Dumps the object.
		/// @param[in] obj Object to dump.
		static void _dump(VALUE obj);
		/// @brief Loads the dumped object.
		/// @return Loaded object.
		static VALUE _load();

		/// @brief Dumps nil.
		/// @param[in] obj nil to dump.
		static void _dump_nil(VALUE obj);
		/// @brief Dumps false.
		/// @param[in] obj false to dump.
		static void _dump_false(VALUE obj);
		/// @brief Dumps true.
		/// @param[in] obj true to dump.
		static void _dump_true(VALUE obj);
		/// @brief Dumps a Fixnum.
		/// @param[in] obj Fixnum to dump.
		static void _dump_fixnum(VALUE obj);
		/// @brief Dumps a Bignum.
		/// @param[in] obj Bignum to dump.
		static void _dump_bignum(VALUE obj);
		/// @brief Dumps a Float.
		/// @param[in] obj Float to dump.
		static void _dump_float(VALUE obj);
		/// @brief Dumps a string.
		/// @param[in] obj String to dump.
		static void _dump_string(VALUE obj);
		/// @brief Dumps an array.
		/// @param[in] obj Array to dump.
		static void _dump_array(VALUE obj);
		/// @brief Dumps a hash.
		/// @param[in] obj Hash to dump.
		static void _dump_hash(VALUE obj);
		/// @brief Dumps the actual object.
		/// @param[in] obj Object to dump.
		static void _dump_object(VALUE obj);
		/// @brief Loads the dumped nil.
		/// @return Loaded nil.
		static VALUE _load_nil();
		/// @brief Loads the dumped false.
		/// @return Loaded false.
		static VALUE _load_false();
		/// @brief Loads the dumped true.
		/// @return Loaded true.
		static VALUE _load_true();
		/// @brief Loads the dumped Fixnum.
		/// @return Loaded Fixnum.
		static VALUE _load_fixnum();
		/// @brief Loads the dumped Bignum.
		/// @return Loaded Bignum.
		static VALUE _load_bignum();
		/// @brief Loads the dumped Float.
		/// @return Loaded Float.
		static VALUE _load_float();
		/// @brief Loads the dumped string.
		/// @return Loaded string.
		static VALUE _load_string();
		/// @brief Loads the dumped array.
		/// @return Loaded array.
		static VALUE _load_array();
		/// @brief Loads the dumped hash.
		/// @return Loaded hash.
		static VALUE _load_hash();
		/// @brief Loads the actual dumped object.
		/// @return Loaded object.
		static VALUE _load_object();

	};

}
#endif
