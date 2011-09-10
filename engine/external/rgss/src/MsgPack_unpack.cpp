#include <ruby.h>

#include <hltypes/exception.h>

#include "MsgPack.h"
#include "CodeSnippets.h"

#ifdef __BIG_ENDIAN__
#define READ_ENDIANESS_2(data) ((data[1] << 8) | data[0])
#define READ_ENDIANESS_4(data) ((data[3] << 24) | (data[2] << 16) | (data[1] << 8) | data[4])
#define READ_ENDIANESS_8(data) READ_ENDIANESS_4(data) // we use a 32-bit "long"
#else
#define READ_ENDIANESS_2(data) ((data[0] << 8) | data[1])
#define READ_ENDIANESS_4(data) ((data[0] << 24) | (data[1] << 16) | (data[2] << 8) | data[3])
#define READ_ENDIANESS_8(data) READ_ENDIANESS_4(data) // we use a 32-bit "long"
#endif

#define CHECK_BITS(data, value) (((data) & (value)) == (value))

namespace rgss
{
	/****************************************************************************************
	 * Utility
	 ****************************************************************************************/

	unsigned char MsgPack::__read_stream()
	{
		unsigned char result = stream[0];
		stream++;
		return result;
	}

	unsigned char* MsgPack::__read_stream(unsigned int bytes)
	{
		unsigned char* result = stream;
		stream += bytes;
		return result;
	}

	unsigned char MsgPack::__read_uint8()
	{
		return MsgPack::__read_stream();
	}

	unsigned short MsgPack::__read_uint16()
	{
		unsigned char* data = MsgPack::__read_stream(2);
		return READ_ENDIANESS_2(data);
	}

	unsigned int MsgPack::__read_uint32()
	{
		unsigned char* data = MsgPack::__read_stream(4);
		return READ_ENDIANESS_4(data);
	}

	unsigned long MsgPack::__read_uint64()
	{
		unsigned char* data = MsgPack::__read_stream(8);
		return READ_ENDIANESS_8(data);
	}

	/****************************************************************************************
	 * Main
	 ****************************************************************************************/

	VALUE MsgPack::_unpack(unsigned char* data)
	{
		stream = data;
		return MsgPack::_unpack_object();
	}

	VALUE MsgPack::_unpack_object()
	{
		unsigned char type = MsgPack::__read_stream();
		if (CHECK_BITS(type, 0x80))
		{
			return MsgPack::_unpack_pint8(type);
		}
		if (CHECK_BITS(type, 0xE0))
		{
			return MsgPack::_unpack_nint8(type);
		}
		if (type == 0xCC)
		{
			return MsgPack::_unpack_uint8();
		}
		if (type == 0xCD)
		{
			return MsgPack::_unpack_uint16();
		}
		if (type == 0xCE)
		{
			return MsgPack::_unpack_uint32();
		}
		if (type == 0xCF)
		{
			return MsgPack::_unpack_uint64();
		}
		if (type == 0xD0)
		{
			return MsgPack::_unpack_int8();
		}
		if (type == 0xD1)
		{
			return MsgPack::_unpack_int16();
		}
		if (type == 0xD2)
		{
			return MsgPack::_unpack_int32();
		}
		if (type == 0xD3)
		{
			return MsgPack::_unpack_int64();
		}
		if (type == 0xC0)
		{
			return MsgPack::_unpack_nil();
		}
		if (type == 0xC3)
		{
			return MsgPack::_unpack_true();
		}
		if (type == 0xC2)
		{
			return MsgPack::_unpack_false();
		}
		if (type == 0xCA)
		{
			return MsgPack::_unpack_float();
		}
		if (type == 0xCB)
		{
			return MsgPack::_unpack_double();
		}
		if (CHECK_BITS(type, 0xA0))
		{
			return MsgPack::_unpack_raw((type & 0x1F));
		}
		if (type == 0xDA)
		{
			return MsgPack::_unpack_raw(MsgPack::__read_uint16());
		}
		if (type == 0xDB)
		{
			return MsgPack::_unpack_raw(MsgPack::__read_uint32());
		}
		if (CHECK_BITS(type, 0x90))
		{
			return MsgPack::_unpack_array(type & 0x0F);
		}
		if (type == 0xDC)
		{
			return MsgPack::_unpack_array(MsgPack::__read_uint16());
		}
		if (type == 0xDD)
		{
			return MsgPack::_unpack_array(MsgPack::__read_uint32());
		}
		if (CHECK_BITS(type, 0x80))
		{
			return MsgPack::_unpack_map(type & 0x0F);
		}
		if (type == 0xDE)
		{
			return MsgPack::_unpack_map(MsgPack::__read_uint16());
		}
		if (type == 0xDF)
		{
			return MsgPack::_unpack_map(MsgPack::__read_uint32());
		}
		throw hl_exception("Unknown MsgPack identifier");
	}

	/****************************************************************************************
	 * Unpack types
	 ****************************************************************************************/

	VALUE MsgPack::_unpack_pint8(unsigned char data)
	{
		return INT2FIX(data & 0x7F);
	}

	VALUE MsgPack::_unpack_nint8(unsigned char data)
	{
		return INT2FIX((unsigned char)((data & 0x1F) | 0x80));
	}

	VALUE MsgPack::_unpack_uint8()
	{
		return INT2FIX(MsgPack::__read_stream());
	}

	VALUE MsgPack::_unpack_uint16()
	{
		return INT2FIX(MsgPack::__read_uint16());
	}

	VALUE MsgPack::_unpack_uint32()
	{
		return INT2FIX(MsgPack::__read_uint32());
	}

	VALUE MsgPack::_unpack_uint64()
	{
		return LONG2FIX(MsgPack::__read_uint64());
	}

	VALUE MsgPack::_unpack_int8()
	{
		return INT2FIX(MsgPack::__read_stream());
	}

	VALUE MsgPack::_unpack_int16()
	{
		return INT2FIX((short)MsgPack::__read_uint16());
	}

	VALUE MsgPack::_unpack_int32()
	{
		return INT2FIX((int)MsgPack::__read_uint32());
	}

	VALUE MsgPack::_unpack_int64()
	{
		return LONG2FIX((long)MsgPack::__read_uint64());
	}

	VALUE MsgPack::_unpack_nil()
	{
		return Qnil;
	}

	VALUE MsgPack::_unpack_true()
	{
		return Qtrue;
	}

	VALUE MsgPack::_unpack_false()
	{
		return Qfalse;
	}

	VALUE MsgPack::_unpack_float()
	{
		unsigned int i = MsgPack::__read_uint32();
		float f;
		memcpy(&f, &i, 4);
		return rb_float_new(f);
	}

	VALUE MsgPack::_unpack_double()
	{
		unsigned long l = MsgPack::__read_uint64();
		double d;
		memcpy(&d, &l, 8);
		return rb_float_new(d);
	}

	VALUE MsgPack::_unpack_raw(unsigned int size)
	{
		const char* data = (const char*)MsgPack::__read_stream(size);
		return rb_str_new(data, size);
	}

	VALUE MsgPack::_unpack_array(unsigned int size)
	{
		VALUE result = rb_ary_new();
		for (unsigned int i = 0; i < size; i++)
		{
			rb_ary_push(result, MsgPack::_unpack_object());
		}
		return result;
	}

	VALUE MsgPack::_unpack_map(unsigned int size)
	{
		VALUE result = rb_hash_new();
		for (unsigned int i = 0; i < size; i++)
		{
			rb_hash_aset(result, MsgPack::_unpack_object(), MsgPack::_unpack_object());
		}
		return result;
	}

}
