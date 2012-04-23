/// @file
/// @author  Kresimir Spes
/// @author  Boris Mikic
/// @author  Ivan Vucica
/// @version 1.56
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://www.opensource.org/licenses/bsd-license.php
/// 
/// @section DESCRIPTION
/// 
/// Provides high level utility methods and macros.

#ifndef HLTYPES_UTIL_H
#define HLTYPES_UTIL_H

#include <math.h>

#include "hltypesExport.h"
#include "hstring.h"

namespace hltypes
{
	template <class T> class Array;
}

/// @brief Used for optimized and quick calculation from RAD to DEG.
#define HL_RAD_TO_DEG_RATIO 57.295779513082320876798154814105
/// @brief Used for optimized and quick calculation from DEG to RAD.
#define HL_DEG_TO_RAD_RATIO 0.01745329251994329576923690768489

/// @brief Provides a simpler syntax for iteration.
/// @param[in] name Name of the iteration variable.
/// @param[in] min Start value.
/// @param[in] max Final value.
/// @note Iterates from min to max - 1.
#define for_iter(name, min, max) for (int name = min; name < max; name++)
/// @brief Provides a simpler syntax for iteration.
/// @param[in] name Name of the iteration variable.
/// @param[in] max Start value.
/// @param[in] min Final value.
/// @note Iterates from max - 1 to min.
#define for_iter_r(name, max, min) for (int name = max - 1; name >= min; name--)
/// @brief Provides a simpler syntax for iteration.
/// @param[in] name Name of the iteration variable.
/// @param[in] min Start value.
/// @param[in] max Final value.
/// @param[in] step Value to increase iterator.
/// @note Iterates from min to max - 1.
#define for_iter_step(name, min, max, step) for (int name = min; name < max; name += step)
/// @brief Provides a simpler syntax for iteration.
/// @param[in] name Name of the iteration variable.
/// @param[in] max Start value.
/// @param[in] min Final value.
/// @note Iterates from max - 1 to min.
#define for_iter_step_r(name, max, min, step) for (int name = max - 1; name >= min; name -= step)
/// @brief Provides a simpler syntax for iteration.
/// @param[in] type Type of the iteration variable.
/// @param[in] name Name of the iteration variable.
/// @param[in] min Start value.
/// @param[in] max Final value.
/// @param[in] step Value to increase iterator.
/// @note Iterates from min to max - 1.
#define for_itert(type, name, min, max) for (type name = min; name < max; name++)
/// @brief Provides a simpler syntax for iteration.
/// @param[in] type Type of the iteration variable.
/// @param[in] name Name of the iteration variable.
/// @param[in] max Start value.
/// @param[in] min Final value.
/// @note Iterates from max - 1 to min.
#define for_itert_r(type, name, max, min) for (type name = max - 1; name >= min; name--)
/// @brief Provides a simpler syntax for iteration.
/// @param[in] type Type of the iteration variable.
/// @param[in] name Name of the iteration variable.
/// @param[in] min Start value.
/// @param[in] max Final value.
/// @param[in] step Value to increase iterator.
/// @note Iterates from min to max - 1.
#define for_itert_step(type, name, min, max, step) for (type name = min; name < max; name += step)
/// @brief Provides a simpler syntax for iteration.
/// @param[in] type Type of the iteration variable.
/// @param[in] name Name of the iteration variable.
/// @param[in] max Start value.
/// @param[in] min Final value.
/// @param[in] step Value to increase iterator.
/// @note Iterates from max - 1 to min.
#define for_itert_step_r(type, name, max, min, step) for (type name = max - 1; name >= min; name -= step)
/// @brief Provides a simpler syntax for iteration.
/// @param[in] name Name of the iteration variable.
/// @param[in] min Start value.
/// @param[in] max Final value.
/// @param[in] step Value to increase iterator.
/// @note Iterates from min to max - 1.
/// @note The iteration variable has to be declared previously.
#define for_iterx(name, min, max) for (name = min; name < max; name++)
/// @brief Provides a simpler syntax for iteration.
/// @param[in] name Name of the iteration variable.
/// @param[in] max Start value.
/// @param[in] min Final value.
/// @note Iterates from max - 1 to min.
/// @note The iteration variable has to be declared previously.
#define for_iterx_r(name, max, min) for (name = max - 1; name >= min; name--)
/// @brief Provides a simpler syntax for iteration.
/// @param[in] name Name of the iteration variable.
/// @param[in] min Start value.
/// @param[in] max Final value.
/// @param[in] step Value to increase iterator.
/// @note Iterates from min to max - 1.
/// @note The iteration variable has to be declared previously.
#define for_iterx_step(name, min, max, step) for (name = min; name < max; name += step)
/// @brief Provides a simpler syntax for iteration.
/// @param[in] name Name of the iteration variable.
/// @param[in] max Start value.
/// @param[in] min Final value.
/// @param[in] step Value to increase iterator.
/// @note Iterates from max - 1 to min.
/// @note The iteration variable has to be declared previously.
#define for_iterx_step_r(name, max, min, step) for (name = max - 1; name >= min; name -= step)

/// @brief Utility macro for quick getter definition.
/// @param[in] type Variable type.
/// @param[in] name Variable name.
/// @param[in] capsName Variable name with capital beginning letter.
#define HL_DEFINE_GET(type, name, capsName) type get ## capsName() { return this->name; }
/// @brief Utility macro for quick getter (with "is") definition.
/// @param[in] type Variable type.
/// @param[in] name Variable name.
/// @param[in] capsName Variable name with capital beginning letter.
#define HL_DEFINE_IS(type, name, capsName) type is ## capsName() { return this->name; }
/// @brief Utility macro for quick setter definition.
/// @param[in] type Variable type.
/// @param[in] name Variable name.
/// @param[in] capsName Variable name with capital beginning letter.
#define HL_DEFINE_SET(type, name, capsName) void set ## capsName(type value) { this->name = value; }
/// @brief Utility macro for quick getter and setter definition.
/// @param[in] type Variable type.
/// @param[in] name Variable name.
/// @param[in] capsName Variable name with capital beginning letter.
#define HL_DEFINE_GETSET(type, name, capsName) HL_DEFINE_GET(type, name, capsName) HL_DEFINE_SET(type, name, capsName)
/// @brief Utility macro for quick getter (with "is") and setter definition.
/// @param[in] type Variable type.
/// @param[in] name Variable name.
/// @param[in] capsName Variable name with capital beginning letter.
#define HL_DEFINE_ISSET(type, name, capsName) HL_DEFINE_IS(type, name, capsName) HL_DEFINE_SET(type, name, capsName)

/// @brief Calculates sin from angle given in degrees.
/// @param[in] degrees Angle in degrees.
/// @return sin(degrees).
#define dsin(degrees) sin((degrees) * HL_DEG_TO_RAD_RATIO)
/// @brief Calculates cos from angle given in degrees.
/// @param[in] degrees Angle in degrees.
/// @return cos(degrees).
#define dcos(degrees) cos((degrees) * HL_DEG_TO_RAD_RATIO)
/// @brief Calculates asin in degrees.
/// @param[in] value sin value.
/// @return asin in degrees.
#define dasin(value) (asin(value) * HL_RAD_TO_DEG_RATIO)
/// @brief Calculates acos in degrees.
/// @param[in] value cos value.
/// @return acos in degrees.
#define dacos(value) (acos(value) * HL_RAD_TO_DEG_RATIO)
/// @brief hltypes e-tolerance.
#define HL_E_TOLERANCE 0.01

/// @brief Returns a random int number.
/// @param[in] min Inclusive lower boundary.
/// @param[in] max Exclusive upper boundary.
/// @return Random number between min inclusively and max exclusively.
/// @note Returns min if max is equal or less than min.
hltypesFnExport int hrand(int min, int max);
/// @brief Returns a random int number.
/// @param[in] max Exclusive upper boundary.
/// @return Random number between 0 inclusively and max exclusively.
/// @note Returns 0 if max is equal or less than 0.
hltypesFnExport int hrand(int max);
/// @brief Returns a random float number.
/// @param[in] min Inclusive lower boundary.
/// @param[in] max Exclusive upper boundary.
/// @return Random number between min inclusively and max exclusively.
/// @note Returns min if max is equal or less than min.
hltypesFnExport float hrandf(float min, float max);
/// @brief Returns a random float number.
/// @param[in] max Exclusive upper boundary.
/// @return Random number between 0.0 inclusively and max exclusively.
/// @note Returns 0.0 if max is equal or less than 0.0.
hltypesFnExport float hrandf(float max);
/// @brief Returns a random double number.
/// @param[in] min Inclusive lower boundary.
/// @param[in] max Exclusive upper boundary.
/// @return Random number between min inclusively and max exclusively.
/// @note Returns min if max is equal or less than min.
hltypesFnExport double hrandd(double min, double max);
/// @brief Returns a random double number.
/// @param[in] max Exclusive upper boundary.
/// @return Random number between 0.0 inclusively and max exclusively.
/// @note Returns 0.0 if max is equal or less than 0.0.
hltypesFnExport double hrandd(double max);
/// @brief Floors a float value.
/// @param[in] value The value to be floored.
/// @return Rounded value as integer.
hltypesFnExport int hfloor(float value);
/// @brief Floors a double value.
/// @param[in] value The value to be floored.
/// @return Rounded value as integer.
hltypesFnExport int hfloor(double value);
/// @brief Floors a float value.
/// @param[in] value The value to be floored.
/// @return Rounded value as float.
hltypesFnExport float hfloorf(float value);
/// @brief Floors a double value.
/// @param[in] value The value to be floored.
/// @return Rounded value as double.
hltypesFnExport double hfloord(double value);
/// @brief Ceils a float value.
/// @param[in] value The value to be ceiled.
/// @return Rounded value as integer.
hltypesFnExport int hceil(float value);
/// @brief Ceils a double value.
/// @param[in] value The value to be ceiled.
/// @return Rounded value as integer.
hltypesFnExport int hceil(double value);
/// @brief Ceils a float value.
/// @param[in] value The value to be ceiled.
/// @return Rounded value as float.
hltypesFnExport float hceilf(float value);
/// @brief Ceils a double value.
/// @param[in] value The value to be ceiled.
/// @return Rounded value as double.
hltypesFnExport double hceild(double value);
/// @brief Rounds a float value to the nearest integer value.
/// @param[in] value The value to be rounded.
/// @return Rounded value as integer.
hltypesFnExport int hround(float value);
/// @brief Rounds a double value to the nearest integer value.
/// @param[in] value The value to be rounded.
/// @return Rounded value as integer.
hltypesFnExport int hround(double value);
/// @brief Rounds a float value to the nearest integer value.
/// @param[in] value The value to be rounded.
/// @return Rounded value as float.
hltypesFnExport float hroundf(float value);
/// @brief Rounds a double value to the nearest integer value.
/// @param[in] value The value to be rounded.
/// @return Rounded value as double.
hltypesFnExport double hroundd(double value);
/// @brief Gets absolute value.
/// @param[in] value The value to be absoluted.
/// @return Absoluted value.
hltypesFnExport int habs(int value);
/// @brief Gets absolute value.
/// @param[in] value The value to be absoluted.
/// @return Absoluted value.
hltypesFnExport long habs(long value);
/// @brief Gets absolute value.
/// @param[in] value The value to be absoluted.
/// @return Absoluted value.
hltypesFnExport float habs(float value);
/// @brief Gets absolute value.
/// @param[in] value The value to be absoluted.
/// @return Absoluted value.
hltypesFnExport double habs(double value);
/// @brief Gets absolute value.
/// @param[in] value The value to be absoluted.
/// @return Absoluted value.
hltypesFnExport long double habs(long double value);
/// @brief Gets the always-positive value of i mod m.
/// @param[in] i Integer value.
/// @param[in] m Modulo value.
/// @return The always-positive value of i mod m.
hltypesFnExport int hmod(int i, int m);
/// @brief Gets the always-positive value of f mod m.
/// @param[in] f Float value.
/// @param[in] m Modulo value.
/// @return The always-positive value of f mod m.
hltypesFnExport float hmodf(float f, float m);
/// @brief Gets the always-positive value of d mod m.
/// @param[in] d Double value.
/// @param[in] m Modulo value.
/// @return The always-positive value of d mod m.
hltypesFnExport double hmodd(double d, double m);
/// @brief Compares 2 float values within using a tolerance factor.
/// @param[in] a First float value.
/// @param[in] b Second float value.
/// @return True if comparison matches within boundary limits.
hltypesFnExport bool heqf(float a, float b, float tolerance = HL_E_TOLERANCE);
/// @brief Compares 2 double values within using a tolerance factor.
/// @param[in] a First double value.
/// @param[in] b Second double value.
/// @return True if comparison matches within boundary limits.
hltypesFnExport bool heqd(double a, double b, double tolerance = HL_E_TOLERANCE);
/// @brief Uses a cmp-like comparison of 2 float values.
/// @param[in] a First float value.
/// @param[in] b Second float value.
/// @return 1 if a is greater than b, 0 if they are equal within the tolerance limits and -1 if a is less than b.
hltypesFnExport int hcmpf(float a, float b, float tolerance = HL_E_TOLERANCE);
/// @brief Uses a cmp-like comparison of 2 double values.
/// @param[in] a First double value.
/// @param[in] b Second double value.
/// @return 1 if a is greater than b, 0 if they are equal within the tolerance limits and -1 if a is less than b.
hltypesFnExport int hcmpd(double a, double b, double tolerance = HL_E_TOLERANCE);
/// @brief Normalizes a file path by converting all platform specific characters into / and proper removal of "." and ".." where necessary.
/// @param[in] path The path.
/// @return Normalized filepath.
hltypesFnExport hstr normalize_path(chstr path);
/// @brief Gets the base directory of a filename/directory.
/// @param[in] filename The path.
/// @return Base directory of the given filename/directory.
hltypesFnExport hstr get_basedir(chstr path);
/// @brief Gets the base filename/directory without the prepended directory path.
/// @param[in] filename The path.
/// @return Base directory of the filename/directory.
hltypesFnExport hstr get_basename(chstr path);
/// @brief Converts a unicode unsigned int to a UTF8 string.
/// @param[in] value The unsigned int value.
/// @return UTF8 string.
hltypesFnExport hstr unicode_to_utf8(unsigned int value);
/// @brief Converts a unicode unsigned int string to a UTF8 string.
/// @param[in] string The unsigned int string.
/// @return UTF8 string.
hltypesFnExport hstr unicode_to_utf8(const unsigned int* string);
/// @brief Converts a unicode unsigned int Array to a UTF8 string.
/// @param[in] string The unsigned int characters.
/// @return UTF8 string.
hltypesFnExport hstr unicode_to_utf8(hltypes::Array<unsigned int> chars);
/// @brief Converts a unicode wchar to a UTF8 string.
/// @param[in] value The wchar value.
/// @return UTF8 string.
hltypesFnExport hstr unicode_to_utf8(wchar_t value);
/// @brief Converts a unicode wchar string to a UTF8 string.
/// @param[in] string The wchar string.
/// @return UTF8 string.
hltypesFnExport hstr unicode_to_utf8(const wchar_t* string);
/// @brief Converts a unicode wchar Array to a UTF8 string.
/// @param[in] string The wchar characters.
/// @return UTF8 string.
hltypesFnExport hstr unicode_to_utf8(hltypes::Array<unsigned int> chars);
/// @brief Converts a UTF8 character into the corresponding character code.
/// @param[in] input The UTF8 character as C string.
/// @param[out] character_length Length of character in bytes.
/// @return Charcter code.
hltypesFnExport unsigned int utf8_to_uint(chstr input, int* character_length = NULL);
/// @brief Converts a UTF8 string into a unicode string.
/// @param[in] input The UTF8 string.
/// @param[out] lenght Length of the string.
/// @return The unsigned int string.
/// @note Make sure to use "delete []" on the result to prevent memory leaks.
hltypesFnExport unsigned int* utf8_to_unicode(chstr input, int* length = NULL);
/// @brief Converts a UTF8 string into a wchar string.
/// @param[in] input The UTF8 string.
/// @param[out] lenght Length of the string.
/// @return The wchar_t string.
/// @note Make sure to use "delete []" on the result to prevent memory leaks.
hltypesFnExport wchar_t* utf8_to_wchars(chstr input, int* length = NULL);
/// @brief Calculates CRC32 from a byte stream.
/// @param[in] data Data stream.
/// @param[in] size Size of the data stream.
/// @return CRC32 value of the stream.
hltypesFnExport unsigned int calc_crc32(unsigned char* data, int size);
/// @brief Calculates CRC32 from a byte stream.
/// @param[in] filename Filename of the file to calculate the CRC32 from.
/// @return CRC32 value of the file.
hltypesFnExport unsigned int calc_crc32(chstr filename);

/// @brief Returns the lesser of two elements.
/// @param[in] a First element.
/// @param[in] b Second element.
/// @return The lesser of two elements.
template <class T> T hmin(T a, T b)
{
	return (a < b ? a : b);
}
/// @brief Returns the greater of two elements.
/// @param[in] a First element.
/// @param[in] b Second element.
/// @return The greater of two elements.
template <class T> T hmax(T a, T b)
{
	return (a > b ? a : b);
}
/// @brief Clamps a value between two other values.
/// @param[in] value The element to clamp.
/// @param[in] min Minimum inclusive boundary.
/// @param[in] max Maximum inclusive boundary.
/// @return Clamped value.
template <class T> T hclamp(T value, T min, T max)
{
	return (value < min ? min : (value > max ? max : value));
}
/// @brief Swaps the values of two elements.
/// @param[in,out] a First element.
/// @param[in,out] b Second element.
template <class T> void hswap(T& a, T& b)
{
	T temp = a;
	a = b;
	b = temp;
}
/// @brief Returns Signum of the value.
/// @param[in] value The value.
/// @return Signum of the value.
template <class T> int hsgn(T value)
{
	return (value == 0 ? 0 : value >= 0 ? 1 : -1);
}
/// @brief Checks whether an element is within the range of two other elements, inclusively.
/// @param[in] value The element to check.
/// @param[in] min Minimum inclusive boundary.
/// @param[in] max Maximum inclusive boundary.
/// @return True if element is between minimum and maximum.
template <class T> bool is_between(T value, T min, T max)
{
	return (value >= min && value <= max);
}
/// @brief Checks whether an element is within the range of two other elements, exclusively.
/// @param[in] value The element to check.
/// @param[in] min Minimum exclusive boundary.
/// @param[in] max Maximum exclusive boundary.
/// @return True if element is between minimum and maximum.
template <class T> bool is_within(T value, T min, T max)
{
	return (value > min && value < max);
}
/// @brief Checks whether an element is within inclusive minimum and exclusive maximum of two other elements.
/// @param[in] value The element to check.
/// @param[in] min Minimum inclusive boundary.
/// @param[in] max Maximum exclusive boundary.
/// @return True if element is inside of minimum and maximum.
template <class T> bool is_in_range(T value, T min, T max)
{
	return (value >= min && value < max);
}
/// @brief Checks whether an element is within exclusive minimum and inclusive maximum of two other elements.
/// @param[in] value The element to check.
/// @param[in] min Minimum exclusive boundary.
/// @param[in] max Maximum inclusive boundary.
/// @return True if element is inside of minimum and maximum.
template <class T> bool is_inside(T value, T min, T max) // I'd like to be inside
{
	return (value > min && value <= max);
}

#endif
