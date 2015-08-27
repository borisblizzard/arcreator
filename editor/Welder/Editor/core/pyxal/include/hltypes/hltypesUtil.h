/// @file
/// @version 3.0
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://opensource.org/licenses/BSD-3-Clause
/// 
/// @section DESCRIPTION
/// 
/// Provides high level utility methods and macros.

#ifndef HLTYPES_UTIL_H
#define HLTYPES_UTIL_H

#include <math.h>
#include <stdint.h>

#include "hltypesExport.h"
#include "hstring.h"

namespace hltypes
{
	class Stream;
	class StreamBase;
	extern String logTag;
}

/// @brief Used for optimized and quick calculation from RAD to DEG.
#define HL_RAD_TO_DEG_RATIO 57.295779513082320876798154814105
/// @brief Used for optimized and quick calculation from DEG to RAD.
#define HL_DEG_TO_RAD_RATIO 0.01745329251994329576923690768489

/// @brief Calculates sin from angle given in degrees.
/// @param[in] degrees Angle in degrees.
/// @return sin(degrees).
#define dsin(degrees) sin((degrees) * HL_DEG_TO_RAD_RATIO)
/// @brief Calculates cos from angle given in degrees.
/// @param[in] degrees Angle in degrees.
/// @return cos(degrees).
#define dcos(degrees) cos((degrees) * HL_DEG_TO_RAD_RATIO)
/// @brief Calculates tan from angle given in degrees.
/// @param[in] degrees Angle in degrees.
/// @return tan(degrees).
#define dtan(degrees) tan((degrees) * HL_DEG_TO_RAD_RATIO)
/// @brief Calculates asin in degrees.
/// @param[in] value sin value.
/// @return asin in degrees.
#define dasin(value) (asin(value) * HL_RAD_TO_DEG_RATIO)
/// @brief Calculates acos in degrees.
/// @param[in] value cos value.
/// @return acos in degrees.
#define dacos(value) (acos(value) * HL_RAD_TO_DEG_RATIO)
/// @brief Calculates atan in degrees.
/// @param[in] value cos value.
/// @return atan in degrees.
/// @note This uses atan2.
#define datan(value) (atan2(value) * HL_RAD_TO_DEG_RATIO)
/// @brief hltypes e-tolerance.
#define HL_E_TOLERANCE 0.0001

/// @brief Utility macro for quick getter definition.
/// @param[in] type Variable type.
/// @param[in] name Variable name.
/// @param[in] capsName Variable name with capital beginning letter.
#define HL_DEFINE_GET(type, name, capsName) inline type get ## capsName() { return this->name; }
/// @brief Utility macro for quick getter definition.
/// @param[in] classe Template class.
/// @param[in] type1 First template type argument.
/// @param[in] type2 Second template type argument.
/// @param[in] name Variable name.
/// @param[in] capsName Variable name with capital beginning letter.
#define HL_DEFINE_GET2(classe, type1, type2, name, capsName) inline classe<type1, type2> get ## capsName() { return this->name; }
/// @brief Utility macro for quick getter (with "is") definition.
/// @param[in] name Variable name.
/// @param[in] capsName Variable name with capital beginning letter.
/// @note This is meant for use with bool only.
#define HL_DEFINE_IS(name, capsName) inline bool is ## capsName() { return this->name; }
/// @brief Utility macro for quick setter definition.
/// @param[in] type Variable type.
/// @param[in] name Variable name.
/// @param[in] capsName Variable name with capital beginning letter.
#define HL_DEFINE_SET(type, name, capsName) inline void set ## capsName(type value) { this->name = value; }
/// @brief Utility macro for quick setter definition.
/// @param[in] classe Template class.
/// @param[in] type1 First template type argument.
/// @param[in] type2 Second template type argument.
/// @param[in] name Variable name.
/// @param[in] capsName Variable name with capital beginning letter.
#define HL_DEFINE_SET2(classe, type1, type2, name, capsName) inline void set ## capsName(classe<type1, type2> value) { this->name = value; }
/// @brief Utility macro for quick getter and setter definition.
/// @param[in] classe Template class.
/// @param[in] type1 First template type argument.
/// @param[in] type2 Second template type argument.
/// @param[in] name Variable name.
/// @param[in] capsName Variable name with capital beginning letter.
#define HL_DEFINE_GETSET(type, name, capsName) HL_DEFINE_GET(type, name, capsName) HL_DEFINE_SET(type, name, capsName)
/// @brief Utility macro for quick getter and setter definition.
/// @param[in] classe Template class.
/// @param[in] type1 First template type argument.
/// @param[in] type2 Second template type argument.
/// @param[in] name Variable name.
/// @param[in] capsName Variable name with capital beginning letter.
#define HL_DEFINE_GETSET2(classe, type1, type2, name, capsName) HL_DEFINE_GET2(classe, type1, type2, name, capsName) HL_DEFINE_SET2(classe, type1, type2, name, capsName)
/// @brief Utility macro for quick getter (with "is") and setter definition.
/// @param[in] name Variable name.
/// @param[in] capsName Variable name with capital beginning letter.
/// @note This is meant for use with bool only.
#define HL_DEFINE_ISSET(name, capsName) HL_DEFINE_IS(name, capsName) HL_DEFINE_SET(bool, name, capsName)

/// @brief Provides a simpler syntax for iteration.
/// @param[in] name Name of the iteration variable.
/// @param[in] min Start value.
/// @param[in] max Final value.
/// @note Iterates from min to max - 1.
#define for_iter(name, min, max) for (int name = min; name < max; ++name)
/// @brief Provides a simpler syntax for iteration.
/// @param[in] name Name of the iteration variable.
/// @param[in] max Start value.
/// @param[in] min Final value.
/// @note Iterates from max - 1 to min.
#define for_iter_r(name, max, min) for (int name = max - 1; name >= min; --name)
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
#define for_itert(type, name, min, max) for (type name = min; name < max; ++name)
/// @brief Provides a simpler syntax for iteration.
/// @param[in] type Type of the iteration variable.
/// @param[in] name Name of the iteration variable.
/// @param[in] max Start value.
/// @param[in] min Final value.
/// @note Iterates from max - 1 to min.
#define for_itert_r(type, name, max, min) for (type name = max - 1; name >= min; --name)
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
#define for_iterx_r(name, max, min) for (name = max - 1; name >= min; --name)
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

/// @brief Gets the number of seconds passed since 1970/01/01 UTC.
/// @return Number of seconds passed since 1970/01/01 UTC.
/// @note Useful for rand operations, like setting the rand generator with srand().
hltypesFnExport uint64_t htime();
/// @brief Gets the number of miliseconds passed since the system boot.
/// @brief Number of miliseconds passed since the system boot.
/// @note Useful for rand operations, like setting the rand generator with srand().
/// @note Not all platforms actually support uint64 so be careful with this.
hltypesFnExport uint64_t htickCount();
/// @brief Gets an environment variable as String.
/// @param[in] env The environment variable.
/// @return Environment variable as String.
/// @note May not be available on all platforms (e.g. WinRT does not support it).
hltypesFnExport hltypes::String henv(const hltypes::String& name);
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
hltypesFnExport int64_t habs(int64_t value);
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
/// @brief Gets the always-positive value of i mod m.
/// @param[in] i Integer value.
/// @param[in] m Modulo value.
/// @return The always-positive value of i mod m.
hltypesFnExport int64_t hmod(int64_t i, int64_t m);
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
/// @brief Calculates the square root.
/// @param[in] value Value to square root.
/// @return Square root of a value.
hltypesFnExport float hsqrt(int value);
/// @brief Calculates the square root.
/// @param[in] value Value to square root.
/// @return Square root of a value.
hltypesFnExport float hsqrt(float value);
/// @brief Calculates the square root.
/// @param[in] value Value to square root.
/// @return Square root of a value.
hltypesFnExport double hsqrt(double value);
/// @brief Calculates the square root.
/// @param[in] value Value to square root.
/// @return Square root of a value.
hltypesFnExport long double hsqrt(long double value);
/// @brief Calculates the float length of the hypotenuse of a right-angles triangle.
/// @param[in] a First cathetus.
/// @param[in] b Second cathetus.
/// @return The float length of the hypotenuse of a right-angles triangle.
hltypesFnExport float hhypot(float a, float b);
/// @brief Calculates the double length of the hypotenuse of a right-angles triangle.
/// @param[in] a First cathetus.
/// @param[in] b Second cathetus.
/// @return The double length of the hypotenuse of a right-angles triangle.
hltypesFnExport double hhypot(double a, double b);
/// @brief Calculates the float length of the hypotenuse of a right-angles triangle.
/// @param[in] a First cathetus.
/// @param[in] b Second cathetus.
/// @return The float length of the hypotenuse of a right-angles triangle.
hltypesFnExport float hhypot(int a, int b);
/// @brief Calculates the double length of the hypotenuse of a right-angles triangle.
/// @param[in] a First cathetus.
/// @param[in] b Second cathetus.
/// @return The double length of the hypotenuse of a right-angles triangle.
hltypesFnExport double hhypotd(int a, int b);
/// @brief Calculates the float squared length of the hypotenuse of a right-angles triangle.
/// @param[in] a First cathetus.
/// @param[in] b Second cathetus.
/// @return The float squared length of the hypotenuse of a right-angles triangle.
hltypesFnExport float hhypotSquared(float a, float b);
/// @brief Calculates the double squared length of the hypotenuse of a right-angles triangle.
/// @param[in] a First cathetus.
/// @param[in] b Second cathetus.
/// @return The double squared length of the hypotenuse of a right-angles triangle.
hltypesFnExport double hhypotSquared(double a, double b);
/// @brief Calculates the int squared length of the hypotenuse of a right-angles triangle.
/// @param[in] a First cathetus.
/// @param[in] b Second cathetus.
/// @return The int squared length of the hypotenuse of a right-angles triangle.
hltypesFnExport int hhypotSquared(int a, int b);
/// @brief Calculates the float squared length of the hypotenuse of a right-angles triangle.
/// @param[in] a First cathetus.
/// @param[in] b Second cathetus.
/// @return The float squared length of the hypotenuse of a right-angles triangle.
hltypesFnExport float hhypotfSquared(int a, int b);
/// @brief Calculates the float squared length of the hypotenuse of a right-angles triangle.
/// @param[in] a First cathetus.
/// @param[in] b Second cathetus.
/// @return The double squared length of the hypotenuse of a right-angles triangle.
hltypesFnExport double hhypotdSquared(int a, int b);
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
/// @brief Returns the next power-of-two value of the given number.
/// @param[in] value the number to check.
/// @return The next power-of-two value of the given number.
hltypesFnExport int hpotceil(int value);
/// @brief Returns the next power-of-two value of the given number.
/// @param[in] value the number to check.
/// @return The next power-of-two value of the given number.
hltypesFnExport int64_t hpotceil(int64_t value);
/// @brief Returns the previous power-of-two value of the given number.
/// @param[in] value the number to check.
/// @return The previous power-of-two value of the given number.
hltypesFnExport int hpotfloor(int value);
/// @brief Returns the previous power-of-two value of the given number.
/// @param[in] value the number to check.
/// @return The previous power-of-two value of the given number.
hltypesFnExport int64_t hpotfloor(int64_t value);

/// @brief Calculates CRC32 from a byte stream.
/// @param[in] data Data stream.
/// @param[in] size Size of the data stream.
/// @return CRC32 value of the stream.
hltypesFnExport unsigned int hcrc32(const unsigned char* data, unsigned int size);
/// @brief Calculates CRC32 from a StreamBase.
/// @param[in] stream StreamBase from which to calculate the CRC32.
/// @param[in] size Number of bytes to read for CRC32.
/// @return CRC32 value of the StreamBase.
hltypesFnExport unsigned int hcrc32(hltypes::StreamBase* stream, unsigned int size);
/// @brief Calculates CRC32 from a StreamBase.
/// @param[in] stream StreamBase from which to calculate the CRC32.
/// @return CRC32 value of the StreamBase.
hltypesFnExport unsigned int hcrc32(hltypes::StreamBase* stream);
/// @brief Calculates CRC32 from a Stream.
/// @param[in] stream Stream from which to calculate the CRC32.
/// @param[in] size Number of bytes to read for CRC32.
/// @return CRC32 value of the Stream.
hltypesFnExport unsigned int hcrc32(hltypes::Stream* stream, unsigned int size);
/// @brief Calculates CRC32 from a Stream.
/// @param[in] stream Stream from which to calculate the CRC32.
/// @return CRC32 value of the Stream.
hltypesFnExport unsigned int hcrc32(hltypes::Stream* stream);

/// @brief Returns the lesser of two elements.
/// @param[in] a First element.
/// @param[in] b Second element.
/// @return The lesser of two elements.
template <class T>
inline T hmin(T a, T b)
{
	return (a < b ? a : b);
}
/// @brief Returns the greater of two elements.
/// @param[in] a First element.
/// @param[in] b Second element.
/// @return The greater of two elements.
template <class T>
inline T hmax(T a, T b)
{
	return (a > b ? a : b);
}
/// @brief Clamps a value between two other values.
/// @param[in] value The element to clamp.
/// @param[in] min Minimum inclusive boundary.
/// @param[in] max Maximum inclusive boundary.
/// @return Clamped value.
template <class T>
inline T hclamp(T value, T min, T max)
{
	return (value < min ? min : (value > max ? max : value));
}
/// @brief Swaps the values of two elements.
/// @param[in,out] a First element.
/// @param[in,out] b Second element.
template <class T>
inline void hswap(T& a, T& b)
{
	T temp = a;
	a = b;
	b = temp;
}
/// @brief Returns Signum of the value.
/// @param[in] value The value.
/// @return Signum of the value.
template <class T>
inline int hsgn(T value)
{
	return (value == 0 ? 0 : value >= 0 ? 1 : -1);
}
/// @brief Checks whether an element is within the range of two other elements, inclusively.
/// @param[in] value The element to check.
/// @param[in] min Minimum inclusive boundary.
/// @param[in] max Maximum inclusive boundary.
/// @return True if element is between minimum and maximum.
/// @note The "II" at the end indicates "inclusive minimum, inclusive maximum".
template <class T>
inline bool hbetweenII(T value, T min, T max)
{
	return (value >= min && value <= max);
}
/// @brief Checks whether an element is within the range of two other elements, exclusively.
/// @param[in] value The element to check.
/// @param[in] min Minimum exclusive boundary.
/// @param[in] max Maximum exclusive boundary.
/// @return True if element is between minimum and maximum.
/// @note The "EE" at the end indicates "exclusive minimum, exclusive maximum".
template <class T>
inline bool hbetweenEE(T value, T min, T max)
{
	return (value > min && value < max);
}
/// @brief Checks whether an element is within inclusive minimum and exclusive maximum of two other elements.
/// @param[in] value The element to check.
/// @param[in] min Minimum inclusive boundary.
/// @param[in] max Maximum exclusive boundary.
/// @return True if element is inside of minimum and maximum.
/// @note The "IE" at the end indicates "inclusive minimum, exclusive maximum".
template <class T>
inline bool hbetweenIE(T value, T min, T max)
{
	return (value >= min && value < max);
}
/// @brief Checks whether an element is within exclusive minimum and inclusive maximum of two other elements.
/// @param[in] value The element to check.
/// @param[in] min Minimum exclusive boundary.
/// @param[in] max Maximum inclusive boundary.
/// @return True if element is inside of minimum and maximum.
/// @note The "EI" at the end indicates "exclusive minimum, inclusive maximum".
template <class T>
inline bool hbetweenEI(T value, T min, T max)
{
	return (value > min && value <= max);
}

DEPRECATED_ATTRIBUTE hltypesFnExport uint64_t get_system_time();
DEPRECATED_ATTRIBUTE hltypesFnExport uint64_t get_system_tick_count();
DEPRECATED_ATTRIBUTE hltypesFnExport hltypes::String get_environment_variable(const hltypes::String& name);
DEPRECATED_ATTRIBUTE hltypesFnExport float hhypot_squared(float a, float b);
DEPRECATED_ATTRIBUTE hltypesFnExport double hhypot_squared(double a, double b);
DEPRECATED_ATTRIBUTE hltypesFnExport int hhypot_squared(int a, int b);
DEPRECATED_ATTRIBUTE hltypesFnExport float hhypotf_squared(int a, int b);
DEPRECATED_ATTRIBUTE hltypesFnExport double hhypotd_squared(int a, int b);
DEPRECATED_ATTRIBUTE hltypesFnExport unsigned int calc_crc32(unsigned char* data, unsigned int size);
DEPRECATED_ATTRIBUTE hltypesFnExport unsigned int calc_crc32(hltypes::StreamBase* stream, unsigned int size);
DEPRECATED_ATTRIBUTE hltypesFnExport unsigned int calc_crc32(hltypes::StreamBase* stream);
template <class T> DEPRECATED_ATTRIBUTE inline bool is_between_ii(T value, T min, T max) { return hbetweenII(value, min, max); }
template <class T> DEPRECATED_ATTRIBUTE inline bool is_between_ee(T value, T min, T max) { return hbetweenEE(value, min, max); }
template <class T> DEPRECATED_ATTRIBUTE inline bool is_between_ie(T value, T min, T max) { return hbetweenIE(value, min, max); }
template <class T> DEPRECATED_ATTRIBUTE inline bool is_between_ei(T value, T min, T max) { return hbetweenEI(value, min, max); }
template <class T> DEPRECATED_ATTRIBUTE inline bool is_between(T value, T min, T max) { return hbetweenII(value, min, max); }
template <class T> DEPRECATED_ATTRIBUTE inline bool is_within(T value, T min, T max) { return hbetweenEE(value, min, max); }
template <class T> DEPRECATED_ATTRIBUTE inline bool is_in_range(T value, T min, T max) { return hbetweenIE(value, min, max); }
template <class T> DEPRECATED_ATTRIBUTE inline bool is_inside(T value, T min, T max) { return hbetweenEI(value, min, max); }

#endif
