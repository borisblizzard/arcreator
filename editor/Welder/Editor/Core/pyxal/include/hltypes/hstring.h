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
/// Provides high level utility methods.

#ifndef HLTYPES_STRING_H
#define HLTYPES_STRING_H

#include <stdarg.h>
#include <stdint.h>
#include <string>

#include "hltypesExport.h"

#if defined(_MSC_VER) && _MSC_VER >= 1600 && defined(_WIN32)
/// @brief Circumvents a compilation problem in VS 2010 and higher
const std::string::size_type std::string::npos = size_t(-1);
#endif

namespace hltypes
{
	template <class T> class Array;
	
	/// @brief Encapsulates std::string and adds high level methods.
	class hltypesSpecialExport String : std::basic_string<char>
	{
	public:
		/// @brief Empty constructor.
		hltypesMemberExport String();
		/// @brief Basic constructor.
		/// @param[in] c A character.
		hltypesMemberExport String(const char c);
		/// @brief Basic constructor.
		/// @param[in] c A character.
		/// @param[in] times How many times c should be added.
		hltypesMemberExport String(const char c, const int times);
		/// @brief Copy constructor.
		/// @param[in] string A C-type string.
		hltypesMemberExport String(const char* string);
		/// @brief Copy constructor.
		/// @param[in] string String to copy.
		hltypesMemberExport String(const String& string);
		/// @brief Copy constructor.
		/// @param[in] string A C-type string.
		/// @param[in] length How many characters to copy.
		hltypesMemberExport String(const char* string, const int length);
		/// @brief Copy constructor.
		/// @param[in] string String to copy.
		/// @param[in] length How many characters to copy.
		hltypesMemberExport String(const String& string, const int length);
		/// @brief Type constructor.
		/// @param[in] s Short integer to create String of.
		hltypesMemberExport String(const short s);
		/// @brief Type constructor.
		/// @param[in] s Unsigned short integer to create String of.
		hltypesMemberExport String(const unsigned short s);
		/// @brief Type constructor.
		/// @param[in] i Integer to create String of.
		hltypesMemberExport String(const int i);
		/// @brief Type constructor.
		/// @param[in] i Unsigned integer to create String of.
		hltypesMemberExport String(const unsigned int i);
		/// @brief Type constructor.
		/// @param[in] i 64-bit integer to create String of.
		hltypesMemberExport String(const int64_t i);
		/// @brief Type constructor.
		/// @param[in] i Unsigned 64-bit integer to create String of.
		hltypesMemberExport String(const uint64_t i);
		/// @brief Type constructor.
		/// @param[in] f Float to create String of.
		hltypesMemberExport String(const float f);
		/// @brief Type constructor.
		/// @param[in] f Float to create String of.
		/// @param[in] precision The floating point precision to use.
		hltypesMemberExport String(const float f, int precision);
		/// @brief Type constructor.
		/// @param[in] d Double to create String of.
		hltypesMemberExport String(const double f);
		/// @brief Type constructor.
		/// @param[in] d Double to create String of.
		/// @param[in] precision The floating point precision to use.
		hltypesMemberExport String(const double d, int precision);
		/// @brief Destructor.
		hltypesMemberExport ~String();

		/// @brief Transforms String into lower case.
		/// @return String in lower case.
		hltypesMemberExport String lowered() const;
		/// @brief Transforms String into upper case.
		/// @return String in upper case.
		hltypesMemberExport String uppered() const;
		/// @brief Reverses String.
		/// @return Reversed String.
		hltypesMemberExport String reversed() const;
		/// @brief Left-trims and right-trims String from a specific character.
		/// @param[in] c Character to trim.
		/// @return Trimmed String.
		hltypesMemberExport String trimmed(char c = ' ') const;
		/// @brief Left-trims String from a specific character.
		/// @param[in] c Character to trim.
		/// @return Left-trimmed String.
		hltypesMemberExport String trimmedLeft(char c = ' ') const;
		/// @brief Right-trims String from a specific character.
		/// @param[in] c Character to trim.
		/// @return Right-trimmed String.
		hltypesMemberExport String trimmedRight(char c = ' ') const;
		/// @brief Basic destructor.
		/// @brief Replaces occurrences of a substring with another substring.
		/// @param[in] what C-type substring.
		/// @param[in] withWhat C-type substitution.
		/// @return New String.
		hltypesMemberExport String replaced(const char* what, const char* withWhat) const;
		/// @brief Replaces occurrences of a substring with another substring.
		/// @param[in] what String substring.
		/// @param[in] withWhat C-type substitution.
		/// @return New String.
		hltypesMemberExport String replaced(const String& what, const char* withWhat) const;
		/// @brief Replaces occurrences of a substring with another substring.
		/// @param[in] what C-type substring.
		/// @param[in] withWhat String substitution.
		/// @return New String.
		hltypesMemberExport String replaced(const char* what, const String& withWhat) const;
		/// @brief Replaces occurrences of a substring with another substring.
		/// @param[in] what String substring.
		/// @param[in] withWhat String substitution.
		/// @return New String.
		hltypesMemberExport String replaced(const String& what, const String& withWhat) const;
		/// @brief Replaces a sequence of characters with a substring.
		/// @param[in] pos1 Start index of character sequence.
		/// @param[in] n1 How many characters to replace.
		/// @param[in] string String substitution.
		/// @return New String.
		hltypesMemberExport String replace(int pos1, int n1, const String& string);
		/// @brief Replaces a sequence of characters with a substring.
		/// @param[in] pos1 Start index of character sequence.
		/// @param[in] n1 How many characters to replace.
		/// @param[in] string String substitution.
		/// @param[in] pos2 Start index in substring.
		/// @param[in] n2 How many characters from substring.
		/// @return New String.
		hltypesMemberExport String replace(int pos1, int n1, const String& string, int pos2, int n2);
		/// @brief Replaces a sequence of characters with a substring.
		/// @param[in] pos1 Start index of character sequence.
		/// @param[in] n1 How many characters to replace.
		/// @param[in] string C-type string substitution.
		/// @return New String.
		hltypesMemberExport String replace(int pos1, int n1, const char* string);
		/// @brief Replaces a sequence of characters with a substring.
		/// @param[in] pos1 Start index of character sequence.
		/// @param[in] n1 How many characters to replace.
		/// @param[in] string C-type string substitution.
		/// @param[in] n2 Length of C-type string.
		/// @return New String.
		hltypesMemberExport String replace(int pos1, int n1, const char* string, int n2);
		/// @brief Replaces a sequence of characters with a substring.
		/// @param[in] pos1 Start index of character sequence.
		/// @param[in] n1 How many characters to replace.
		/// @param[in] c Character substitution.
		/// @param[in] n2 Number of times character should be inserted.
		/// @return New String.
		hltypesMemberExport String replace(int pos1, int n1, char c, int n2);
		/// @brief Splits the String with the delimiter once.
		/// @param[in] delimiter The character acting as splitting delimiter.
		/// @param[out] outLeft First portion of the split String.
		/// @param[out] outRight Second portion of the split String.
		/// @return True if String was split.
		hltypesMemberExport bool split(const char delimiter, String& outLeft, String& outRight) const;
		/// @brief Splits the String with the delimiter once.
		/// @param[in] delimiter The C-type string acting as splitting delimiter.
		/// @param[out] outLeft First portion of the split String.
		/// @param[out] outRight Second portion of the split String.
		/// @return True if String was split.
		hltypesMemberExport bool split(const char* delimiter, String& outLeft, String& outRight) const;
		/// @brief Splits the String with the delimiter once.
		/// @param[in] delimiter The String acting as splitting delimiter.
		/// @param[out] outLeft First portion of the split String.
		/// @param[out] outRight Second portion of the split String.
		/// @return True if String was split.
		hltypesMemberExport bool split(const String& delimiter, String& outLeft, String& outRight) const;
		/// @brief Splits all characters in the String.
		/// @return Array of chars.
		hltypesMemberExport Array<char> split() const;
		/// @brief Splits the String with the delimiter.
		/// @param[in] delimiter The character acting as splitting delimiter.
		/// @param[in] n How many times the string should be split maximally.
		/// @param[in] removeEmpty Whether to remove empty strings from result.
		/// @return Array of Strings.
		hltypesMemberExport Array<String> split(const char delimiter, unsigned int n = -1, bool removeEmpty = false) const;
		/// @brief Splits the String with the delimiter.
		/// @param[in] delimiter The C-type string acting as splitting delimiter.
		/// @param[in] n How many times the string should be split maximally.
		/// @param[in] removeEmpty Whether to remove empty strings from result.
		/// @return Array of Strings.
		hltypesMemberExport Array<String> split(const char* delimiter, unsigned int n = -1, bool removeEmpty = false) const;
		/// @brief Splits the String with the delimiter.
		/// @param[in] delimiter The String acting as splitting delimiter.
		/// @param[in] n How many times the string should be split maximally.
		/// @param[in] removeEmpty Whether to remove empty strings from result.
		/// @return Array of Strings.
		hltypesMemberExport Array<String> split(const String& delimiter, unsigned int n = -1, bool removeEmpty = false) const;
		/// @brief Reverse splits the String with the delimiter once.
		/// @param[in] delimiter The character acting as splitting delimiter.
		/// @param[out] outLeft First portion of the split String.
		/// @param[out] outRight Second portion of the split String.
		/// @return True if String was split.
		hltypesMemberExport bool rsplit(const char delimiter, String& outLeft, String& outRight) const;
		/// @brief Reverse splits the String with the delimiter once.
		/// @param[in] delimiter The C-type string acting as splitting delimiter.
		/// @param[out] outLeft First portion of the split String.
		/// @param[out] outRight Second portion of the split String.
		/// @return True if String was split.
		hltypesMemberExport bool rsplit(const char* delimiter, String& outLeft, String& outRight) const;
		/// @brief Reverse splits the String with the delimiter once.
		/// @param[in] delimiter The String acting as splitting delimiter.
		/// @param[out] outLeft First portion of the split String.
		/// @param[out] outRight Second portion of the split String.
		/// @return True if String was split.
		hltypesMemberExport bool rsplit(const String& delimiter, String& outLeft, String& outRight) const;
		/// @brief Reverse splits the String with the delimiter.
		/// @param[in] delimiter The character acting as splitting delimiter.
		/// @param[in] n How many times the string should be split maximally.
		/// @param[in] removeEmpty Whether to remove empty strings from result.
		/// @return Array of Strings.
		hltypesMemberExport Array<String> rsplit(const char delimiter, unsigned int n = -1, bool removeEmpty = false) const;
		/// @brief Reverse splits the String with the delimiter.
		/// @param[in] delimiter The C-type string acting as splitting delimiter.
		/// @param[in] n How many times the string should be split maximally.
		/// @param[in] removeEmpty Whether to remove empty strings from result.
		/// @return Array of Strings.
		hltypesMemberExport Array<String> rsplit(const char* delimiter, unsigned int n = -1, bool removeEmpty = false) const;
		/// @brief Reverse splits the String with the delimiter.
		/// @param[in] delimiter The String acting as splitting delimiter.
		/// @param[in] n How many times the string should be split maximally.
		/// @param[in] removeEmpty Whether to remove empty strings from result.
		/// @return Array of Strings.
		hltypesMemberExport Array<String> rsplit(const String& delimiter, unsigned int n = -1, bool removeEmpty = false) const;
		/// @brief Finds the first index of a character.
		/// @param[in] c Character to search for.
		/// @param[in] start Starting index.
		/// @return The index of the first occurrence of the character.
		hltypesMemberExport int indexOf(const char c, int start = 0) const;
		/// @brief Finds the first index of a character.
		/// @param[in] string C-string to search for.
		/// @param[in] start Starting index.
		/// @return The index of the first occurrence of the character.
		hltypesMemberExport int indexOf(const char* string, int start = 0) const;
		/// @brief Finds the first index of a character.
		/// @param[in] string String to search for.
		/// @param[in] start Starting index.
		/// @return The index of the first occurrence of the character.
		hltypesMemberExport int indexOf(const String& string, int start = 0) const;
		/// @brief Finds the first index of a character searching from the back.
		/// @param[in] c Character to search for.
		/// @param[in] start Starting index.
		/// @return The index of the first occurrence of the character searching from the back.
		hltypesMemberExport int rindexOf(const char c, int start = -1) const;
		/// @brief Finds the first index of a character searching from the back.
		/// @param[in] string C-string to search for.
		/// @param[in] start Starting index.
		/// @return The index of the first occurrence of the character searching from the back.
		hltypesMemberExport int rindexOf(const char* string, int start = -1) const;
		/// @brief Finds the first index of a character searching from the back.
		/// @param[in] string String to search for.
		/// @param[in] start Starting index.
		/// @return The index of the first occurrence of the character searching from the back.
		hltypesMemberExport int rindexOf(const String& string, int start = -1) const;
		/// @brief Finds the first index of any character.
		/// @param[in] string Characters as C-string to search for.
		/// @param[in] start Starting index.
		/// @return The index of the first occurrence of any of the characters.
		hltypesMemberExport int indexOfAny(const char* string, int start = 0) const;
		/// @brief Finds the first index of any character.
		/// @param[in] string Characters as String to search for.
		/// @param[in] start Starting index.
		/// @return The index of the first occurrence of any of the characters.
		hltypesMemberExport int indexOfAny(const String& string, int start = 0) const;
		/// @brief Finds the first index of any character searching from the back.
		/// @param[in] string Characters as C-string to search for.
		/// @param[in] start Starting index.
		/// @return The index of the first occurrence of any of the characters searching from the back.
		hltypesMemberExport int rindexOfAny(const char* string, int start = -1) const;
		/// @brief Finds the first index of any character searching from the back.
		/// @param[in] string Characters as String to search for.
		/// @param[in] start Starting index.
		/// @return The index of the first occurrence of any of the characters searching from the back.
		hltypesMemberExport int rindexOfAny(const String& string, int start = -1) const;
		/// @brief Counts the occurrences of a substring.
		/// @param[in] c The character to look for.
		/// @return Number of occurrences of the substring.
		hltypesMemberExport int count(const char c) const;
		/// @brief Counts the occurrences of a substring.
		/// @param[in] string The C-type string to look for.
		/// @return Number of occurrences of the substring.
		hltypesMemberExport int count(const char* string) const;
		/// @brief Counts the occurrences of a substring.
		/// @param[in] string The String to look for.
		/// @return Number of occurrences of the substring.
		hltypesMemberExport int count(const String& string) const;
		/// @brief Checks if the string starts with a specific string.
		/// @param[in] string The C-type string to check.
		/// @return True if String starts with s.
		hltypesMemberExport bool startsWith(const char* string) const;
		/// @brief Checks if the string starts with a specific string.
		/// @param[in] string The String to check.
		/// @return True if String starts with s.
		hltypesMemberExport bool startsWith(const String& string) const;
		/// @brief Checks if the string ends with a specific string.
		/// @param[in] string The C-type string to check.
		/// @return True if String ends with s.
		hltypesMemberExport bool endsWith(const char* string) const;
		/// @brief Checks if the string ends with a specific string.
		/// @param[in] string The String to check.
		/// @return True if String ends with s.
		hltypesMemberExport bool endsWith(const String& string) const;
		/// @brief Checks if String contains character.
		/// @param[in] c Character to search for.
		/// @return True if String contains character.
		hltypesMemberExport bool contains(const char c) const;
		/// @brief Checks if String contains C-type string.
		/// @param[in] string C-type string to search for.
		/// @return True if String contains C-type string.
		hltypesMemberExport bool contains(const char* string) const;
		/// @brief Checks if String contains another String.
		/// @param[in] string String to search for.
		/// @return True if this String contains other String.
		hltypesMemberExport bool contains(const String& string) const;
		/// @brief Checks if String contains any character from a C-type string.
		/// @param[in] string C-type string to search for.
		/// @return True if String contains any character from a C-type string.
		hltypesMemberExport bool containsAny(const char* string) const;
		/// @brief Checks if String contains any character from another String.
		/// @param[in] string String to search for.
		/// @return True if this String contains any character from another String.
		hltypesMemberExport bool containsAny(const String& string) const;
		/// @brief Checks if String contains all characters from a C-type string.
		/// @param[in] string C-type string to search for.
		/// @return True if String contains all characters from a C-type string.
		hltypesMemberExport bool containsAll(const char* string) const;
		/// @brief Checks if String contains all characters from another String.
		/// @param[in] string String to search for.
		/// @return True if this String contains all characters from another String.
		hltypesMemberExport bool containsAll(const String& string) const;
		/// @brief Checks if all elements of the string contain only one digit '0'-'9'.
		/// @return True if string is a digit.
		hltypesMemberExport bool isDigit() const;
		/// @brief Checks if the string is an integer.
		/// @return True if string is a number.
		hltypesMemberExport bool isInt() const;
		/// @brief Checks if the string is a float.
		/// @param[in] requireDot If this parameter is false, then a decimal point is not required to designate a float value.
		/// @return True if string is a number.
		hltypesMemberExport bool isFloat(bool requireDot = true) const;
		/// @brief Checks if the string is a number, positive or negative integer or float.
		/// @return True if string is a number.
		hltypesMemberExport bool isNumber() const;
		/// @brief Checks if the string is a hexadecimal number, case ignored.
		/// @return True if string is a hex number.
		/// @note This method is case insensitive.
		/// @note Hex numbers cannot be negative in this context.
		hltypesMemberExport bool isHex() const;
		/// @brief Checks if string contains ASCII only characters.
		/// @return True if String contains only ASCII-7 characters.
		hltypesMemberExport bool isAscii() const;
		/// @brief Creates a substring from UTF8-indexed characters.
		/// @param[in] start Start index of the substring.
		/// @param[in] count Character length of the substring (byte-length, not UT8 character count).
		/// @return The substring.
		hltypesMemberExport String subString(int start, int count) const;
		/// @brief Creates a substring from UTF8-indexed characters.
		/// @param[in] start Start index of the substring.
		/// @param[in] count Character length of the substring (UT8 character count, not byte-length).
		/// @return The substring.
		hltypesMemberExport String utf8SubString(int start, int count) const;
		/// @brief Gets the byte length of the String.
		/// @return Byte length of String.
		hltypesMemberExport int size() const;
		/// @brief Gets the character length of the String.
		/// @return Character length of String.
		hltypesMemberExport int utf8Size() const;
		/// @brief Same as size.
		/// @see size
		hltypesMemberExport int length() const;
		/// @brief Same as utf8Size.
		/// @see utf8_size
		hltypesMemberExport int utf8Length() const;
		/// @brief Creates a string with characters converted using the %02X format.
		/// @return String of hex values of the characters.
		hltypesMemberExport String toHex() const;
		/// @brief Creates an unsigned int from hex value string.
		/// @return An unsigned int.
		/// @note Will return 0 if string is not a hex number. Use String::is_hex() to check first.
		/// @note Hex strings above 0xFFFFFFFF cause undefined behavior.
		hltypesMemberExport unsigned int unhex() const;

		/// @brief Creates a substring.
		/// @param[in] start Start index of the substring.
		/// @param[in] count Length of the substring.
		/// @return The substring.
		hltypesMemberExport String operator()(int start, int count) const;
		/// @brief Creates a substring.
		/// @param[in] start Start index of the substring.
		/// @param[in] count Length of the substring.
		/// @param[in] step Every nth character only.
		/// @return The substring.
		/// @note count defines the length of the substring, step only defines which characters are used for the new String.
		hltypesMemberExport String operator()(int start, int count, int step) const;
		/// @brief Returns character at position in form of String.
		/// @param[in] index Index of the character.
		/// @return A String.
		hltypesMemberExport String operator()(int index) const;
		/// @brief Returns character at position.
		/// @param[in] index Index of the character.
		/// @return A character.
		hltypesMemberExport char& operator[](int index);
		/// @brief Returns character at position.
		/// @param[in] index Index of the character.
		/// @return A character.
		hltypesMemberExport const char& operator[](int index) const;
		/// @brief Casts String into short.
		hltypesMemberExport operator short() const;
		/// @brief Casts String into unsigned short.
		hltypesMemberExport operator unsigned short() const;
		/// @brief Casts String into int.
		hltypesMemberExport operator int() const;
		/// @brief Casts String into unsigned int.
		hltypesMemberExport operator unsigned int() const;
		/// @brief Casts String into 64-bit int.
		hltypesMemberExport operator int64_t() const;
		/// @brief Casts String into unsigned 64-bit int.
		hltypesMemberExport operator uint64_t() const;
		/// @brief Casts String into float.
		hltypesMemberExport operator float() const;
		/// @brief Casts String into double.
		hltypesMemberExport operator double() const;
		/// @brief Casts String into bool.
		/// @note "false", "0" and "" are regarded as false, everything else is regarded as true.
		hltypesMemberExport operator bool() const;
		/// @brief Converts short into String.
		/// @param[in] s Short value.
		/// @return This modified String.
		hltypesMemberExport String operator=(const short s);
		/// @brief Converts unsigned short into String.
		/// @param[in] s Unsigned short value.
		/// @return This modified String.
		hltypesMemberExport String operator=(const unsigned short s);
		/// @brief Converts int into String.
		/// @param[in] i Int value.
		/// @return This modified String.
		hltypesMemberExport String operator=(const int i);
		/// @brief Converts unsigned int into String.
		/// @param[in] i Unsigned int value.
		/// @return This modified String.
		hltypesMemberExport String operator=(const unsigned int i);
		/// @brief Converts 64-bit int into String.
		/// @param[in] i 64-bit int value.
		/// @return This modified String.
		hltypesMemberExport String operator=(const int64_t i);
		/// @brief Converts unsigned 64-bit int into String.
		/// @param[in] i Unsigned 64-bit int value.
		/// @return This modified String.
		hltypesMemberExport String operator=(const uint64_t i);
		/// @brief Converts float into String.
		/// @param[in] f Float value.
		/// @return This modified String.
		hltypesMemberExport String operator=(const float f);
		/// @brief Converts double into String.
		/// @param[in] d Double value.
		/// @return This modified String.
		hltypesMemberExport String operator=(const double d);
		/// @brief Converts bool into String.
		/// @param[in] b Bool value.
		/// @return This modified String.
		hltypesMemberExport String operator=(const bool b);
		/// @brief Converts C-type string into String.
		/// @param[in] string C-type string value.
		/// @return This modified String.
		hltypesMemberExport String operator=(char* string);
		/// @brief Converts C-type string into String.
		/// @param[in] string C-type string value.
		/// @return This modified String.
		hltypesMemberExport String operator=(const char* string);
		/// @brief Assigns String to this one.
		/// @param[in] string String value.
		/// @return This modified String.
		hltypesMemberExport String operator=(const String& string);
		/// @brief Converts short into a String and concatenates the new String at the end of this one.
		/// @param[in] s Short value.
		hltypesMemberExport void operator+=(const short s);
		/// @brief Converts unsigned short into a String and concatenates the new String at the end of this one.
		/// @param[in] s Unsigned short value.
		hltypesMemberExport void operator+=(const unsigned short s);
		/// @brief Converts int into a String and concatenates the new String at the end of this one.
		/// @param[in] i Int value.
		hltypesMemberExport void operator+=(const int i);
		/// @brief Converts unsigned int into a String and concatenates the new String at the end of this one.
		/// @param[in] i Unsigned int value.
		hltypesMemberExport void operator+=(const unsigned int i);
		/// @brief Converts 64-bit int into a String and concatenates the new String at the end of this one.
		/// @param[in] i 64-bit int value.
		hltypesMemberExport void operator+=(const int64_t i);
		/// @brief Converts unsigned 64-bit int into a String and concatenates the new String at the end of this one.
		/// @param[in] i Unsigned 64-bit int value.
		hltypesMemberExport void operator+=(const uint64_t i);
		/// @brief Converts float into a String and concatenates the new String at the end of this one.
		/// @param[in] f Float value.
		hltypesMemberExport void operator+=(const float f);
		/// @brief Converts double into a String and concatenates the new String at the end of this one.
		/// @param[in] d Double value.
		hltypesMemberExport void operator+=(const double d);
		/// @brief Converts bool into a String and concatenates the new String at the end of this one.
		/// @param[in] b Bool value.
		hltypesMemberExport void operator+=(const bool b);
		/// @brief Converts char into a String and concatenates the new String at the end of this one.
		/// @param[in] c Character value.
		hltypesMemberExport void operator+=(const char c);
		/// @brief Converts C-type string into a String and concatenates the new String at the end of this one.
		/// @param[in] string C-type string value.
		hltypesMemberExport void operator+=(char* string);
		/// @brief Converts C-type string into a String and concatenates the new String at the end of this one.
		/// @param[in] string C-type string value.
		hltypesMemberExport void operator+=(const char* string);
		/// @brief Concatenates a String at the end of this one.
		/// @param[in] string String value.
		hltypesMemberExport void operator+=(const String& string);
		/// @brief Merges String with a character converted into String first.
		/// @param[in] c Character value.
		/// @return New String.
		hltypesMemberExport String operator+(const char c) const;
		/// @brief Merges String with a C-type string converted into String first.
		/// @param[in] string C-type string value.
		/// @return New String.
		hltypesMemberExport String operator+(char* string) const;
		/// @brief Merges String with a C-type string converted into String first.
		/// @param[in] string C-type string value.
		/// @return New String.
		hltypesMemberExport String operator+(const char* string) const;
		/// @brief Merges String with another String.
		/// @param[in] string String value.
		/// @return New String.
		hltypesMemberExport String operator+(const String& string) const;
		/// @brief Compares String for equivalency.
		/// @param[in] s Short value.
		/// @return True if value converted into String is equal to this one.
		hltypesMemberExport bool operator==(const short s) const;
		/// @brief Compares String for equivalency.
		/// @param[in] s Unsigned short value.
		/// @return True if value converted into String is equal to this one.
		hltypesMemberExport bool operator==(const unsigned short s) const;
		/// @brief Compares String for equivalency.
		/// @param[in] i Int value.
		/// @return True if value converted into String is equal to this one.
		hltypesMemberExport bool operator==(const int i) const;
		/// @brief Compares String for equivalency.
		/// @param[in] i Unsigned int value.
		/// @return True if value converted into String is equal to this one.
		hltypesMemberExport bool operator==(const unsigned int i) const;
		/// @brief Compares String for equivalency.
		/// @param[in] i 64-bit int value.
		/// @return True if value converted into String is equal to this one.
		hltypesMemberExport bool operator==(const int64_t i) const;
		/// @brief Compares String for equivalency.
		/// @param[in] i Unsigned 64-bit int value.
		/// @return True if value converted into String is equal to this one.
		hltypesMemberExport bool operator==(const uint64_t i) const;
		/// @brief Compares String for equivalency.
		/// @param[in] f Float value.
		/// @return True if value converted into String is equal to this one.
		hltypesMemberExport bool operator==(const float f) const;
		/// @brief Compares String for equivalency.
		/// @param[in] d Double value.
		/// @return True if value converted into String is equal to this one.
		hltypesMemberExport bool operator==(const double d) const;
		/// @brief Compares String for equivalency.
		/// @param[in] b bool value.
		/// @return True if value converted into String is equal to this one.
		hltypesMemberExport bool operator==(const bool b) const;
		/// @brief Compares String for equivalency.
		/// @param[in] s C-type string value.
		/// @return True if other String is equal to this one.
		hltypesMemberExport bool operator==(const char* s) const;
		/// @brief Compares String for equivalency.
		/// @param[in] string String value.
		/// @return True if other String is equal to this one.
		hltypesMemberExport bool operator==(const String& string) const;
		/// @brief Compares String for non-equivalency.
		/// @param[in] s Short value.
		/// @return True if value converted into String is not equal to this one.
		hltypesMemberExport bool operator!=(const short s) const;
		/// @brief Compares String for non-equivalency.
		/// @param[in] s Unsigned short value.
		/// @return True if value converted into String is not equal to this one.
		hltypesMemberExport bool operator!=(const unsigned short s) const;
		/// @brief Compares String for non-equivalency.
		/// @param[in] i Int value.
		/// @return True if value converted into String is not equal to this one.
		hltypesMemberExport bool operator!=(const int i) const;
		/// @brief Compares String for non-equivalency.
		/// @param[in] i Unsigned int value.
		/// @return True if value converted into String is not equal to this one.
		hltypesMemberExport bool operator!=(const unsigned int i) const;
		/// @brief Compares String for non-equivalency.
		/// @param[in] i 64-bit int value.
		/// @return True if value converted into String is not equal to this one.
		hltypesMemberExport bool operator!=(const int64_t i) const;
		/// @brief Compares String for non-equivalency.
		/// @param[in] i Unsigned 64-bit int value.
		/// @return True if value converted into String is not equal to this one.
		hltypesMemberExport bool operator!=(const uint64_t i) const;
		/// @brief Compares String for non-equivalency.
		/// @param[in] f Float value.
		/// @return True if value converted into String is not equal to this one.
		hltypesMemberExport bool operator!=(const float f) const;
		/// @brief Compares String for non-equivalency.
		/// @param[in] d Double value.
		/// @return True if value converted into String is not equal to this one.
		hltypesMemberExport bool operator!=(const double d) const;
		/// @brief Compares String for non-equivalency.
		/// @param[in] b bool value.
		/// @return True if value converted into String is not equal to this one.
		hltypesMemberExport bool operator!=(const bool b) const;
		/// @brief Compares String for non-equivalency.
		/// @param[in] s C-type string value.
		/// @return True if other String is not equal to this one.
		hltypesMemberExport bool operator!=(const char* s) const;
		/// @brief Compares String for non-equivalency.
		/// @param[in] string String value.
		/// @return True if other String is not equal to this one.
		hltypesMemberExport bool operator!=(const String& string) const;
		/// @brief Compares String for being less than another String.
		/// @param[in] string String value.
		/// @return True if this String is less than other String.
		hltypesMemberExport bool operator<(const String& string) const;
		/// @brief Compares String for being greater than another String.
		/// @param[in] string String value.
		/// @return True if this String is greater than other String.
		hltypesMemberExport bool operator>(const String& string) const;
		/// @brief Compares String for being less than or equal to another String.
		/// @param[in] string String value.
		/// @return True if this String is less than or equal to other String.
		hltypesMemberExport bool operator<=(const String& string) const;
		/// @brief Compares String for being greater than or equal to another String.
		/// @param[in] string String value.
		/// @return True if this String is greater than or equal to other String.
		hltypesMemberExport bool operator>=(const String& string) const;

		/// @brief Gets the C-string.
		/// @return This String's C-string.
		hltypesMemberExport const char* cStr() const;
		/// @brief Creates an unicode (unsigned int) string.
		/// @return A unicode (unsigned int) string.
		hltypesMemberExport std::basic_string<unsigned int> uStr() const;
		/// @brief Creates a wchar string.
		/// @return A wchar string.
		hltypesMemberExport std::basic_string<wchar_t> wStr() const;
		/// @brief Converts first UTF8 character into the corresponding character code.
		/// @param[in] index The byte position of the first character in the string.
		/// @param[out] byteCount Length of UTF8 character in bytes.
		/// @return Character code.
		/// @note The out value of byteCount parameter can be used to move a character iterator forward.
		hltypesMemberExport unsigned int firstUnicodeChar(int index = 0, int* byteCount = NULL) const;

		/// @brief Converts a unicode unsigned int to a UTF8 string.
		/// @param[in] value The unsigned int value.
		/// @return UTF8 string.
		hltypesMemberExport static String fromUnicode(unsigned int value);
		/// @brief Converts a unicode wchar to a UTF8 string.
		/// @param[in] value The wchar value.
		/// @return UTF8 string.
		hltypesMemberExport static String fromUnicode(wchar_t value);
		/// @brief Converts a char to a UTF8 string.
		/// @param[in] string The char.
		/// @return UTF8 string.
		hltypesMemberExport static String fromUnicode(char value);
		/// @brief Converts an unsigned char to a UTF8 string.
		/// @param[in] string The unsigned char.
		/// @return UTF8 string.
		hltypesMemberExport static String fromUnicode(unsigned char value);
		/// @brief Converts a unicode unsigned int string to a UTF8 string.
		/// @param[in] string The unsigned int string.
		/// @return UTF8 string.
		hltypesMemberExport static String fromUnicode(const unsigned int* string);
		/// @brief Converts a unicode wchar string to a UTF8 string.
		/// @param[in] string The wchar string.
		/// @return UTF8 string.
		hltypesMemberExport static String fromUnicode(const wchar_t* string);
		/// @brief Converts a char string to a UTF8 string.
		/// @param[in] string The char string.
		/// @return UTF8 string.
		hltypesMemberExport static String fromUnicode(const char* string);
		/// @brief Converts an unsigned char string to a UTF8 string.
		/// @param[in] string The unsigned char string.
		/// @return UTF8 string.
		hltypesMemberExport static String fromUnicode(const unsigned char* string);
		/// @brief Converts a unicode unsigned int Array to a UTF8 string.
		/// @param[in] string The unsigned int characters.
		/// @return UTF8 string.
		hltypesMemberExport static String fromUnicode(Array<unsigned int> chars);
		/// @brief Converts a unicode wchar Array to a UTF8 string.
		/// @param[in] string The wchar characters.
		/// @return UTF8 string.
		hltypesMemberExport static String fromUnicode(Array<wchar_t> chars);
		/// @brief Converts a char Array to a UTF8 string.
		/// @param[in] string The char characters.
		/// @return UTF8 string.
		hltypesMemberExport static String fromUnicode(Array<char> chars);
		/// @brief Converts an unsigned char Array to a UTF8 string.
		/// @param[in] string The unsigned char characters.
		/// @return UTF8 string.
		hltypesMemberExport static String fromUnicode(Array<unsigned char> chars);

		// Potentially temp functionality, avoid
		hltypesMemberExport void assign(const char* string, unsigned int length) { std::string::assign(string, length); }

		DEPRECATED_ATTRIBUTE hltypesMemberExport int find_first_of(const char c) const										{ return this->indexOfAny(c); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport int rfind_first_of(const char c) const										{ return this->rindexOfAny(c); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport int find(const char c) const												{ return this->indexOf(c); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport int find(const char* string) const											{ return this->indexOf(string); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport int find(const std::string& string)										{ return this->indexOf(string.c_str()); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport int find(const String& string)												{ return this->indexOf(string); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport int rfind(const char c) const												{ return this->rindexOf(c); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport int rfind(const char* string) const										{ return this->rindexOf(string); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport int rfind(const std::string& string)										{ return this->rindexOf(string.c_str()); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport int rfind(const String& string)											{ return this->rindexOf(string); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport bool starts_with(const char* s) const										{ return this->startsWith(s); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport bool starts_with(const String& s) const									{ return this->startsWith(s); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport bool ends_with(const char* s) const										{ return this->endsWith(s); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport bool ends_with(const String& s) const										{ return this->endsWith(s); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport String lower() const														{ return this->lowered(); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport String upper() const														{ return this->uppered(); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport String reverse() const														{ return this->reversed(); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport bool is_digit() const														{ return this->isDigit(); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport bool is_int() const														{ return this->isInt(); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport bool is_float(bool requireDot = true) const								{ return this->isFloat(requireDot); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport bool is_number() const														{ return this->isNumber(); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport bool is_hex() const														{ return this->isHex(); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport String trim(char c = ' ') const											{ return this->trimmed(c); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport String ltrim(char c = ' ') const											{ return this->trimmedLeft(c); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport String rtrim(char c = ' ') const											{ return this->trimmedRight(c); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport String replace(const char* what, const char* withWhat) const				{ return this->replaced(what, withWhat); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport String replace(const String& what, const char* withWhat) const				{ return this->replaced(what, withWhat); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport String replace(const char* what, const String& withWhat) const				{ return this->replaced(what, withWhat); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport String replace(const String& what, const String& withWhat) const			{ return this->replaced(what, withWhat); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport bool contains_any(const char* s) const										{ return this->containsAny(s); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport bool contains_any(const String& s) const									{ return this->containsAny(s); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport bool contains_all(const char* s) const										{ return this->containsAll(s); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport bool contains_all(const String& s) const									{ return this->containsAll(s); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport String substr(int start, int count) const									{ return this->subString(start, count); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport String utf8_substr(int start, int count) const								{ return this->utf8SubString(start, count); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport int utf8_size() const														{ return this->utf8Size(); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport int utf8_length() const													{ return this->utf8Length(); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport bool is_ascii() const														{ return this->isAscii(); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport String to_hex() const														{ return this->isHex(); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport const char* c_str() const													{ return this->cStr(); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport std::basic_string<unsigned int> u_str() const								{ return this->uStr(); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport std::basic_string<wchar_t> w_str() const									{ return this->wStr(); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport unsigned int first_unicode_char(int index = 0, int* length = NULL) const	{ return this->firstUnicodeChar(index, length); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport static String from_unicode(unsigned int value)								{ return String::fromUnicode(value); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport static String from_unicode(wchar_t value)									{ return String::fromUnicode(value); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport static String from_unicode(char value)										{ return String::fromUnicode(value); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport static String from_unicode(unsigned char value)							{ return String::fromUnicode(value); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport static String from_unicode(const unsigned int* string)						{ return String::fromUnicode(string); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport static String from_unicode(const wchar_t* string)							{ return String::fromUnicode(string); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport static String from_unicode(const char* string)								{ return String::fromUnicode(string); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport static String from_unicode(const unsigned char* string)					{ return String::fromUnicode(string); }
		DEPRECATED_ATTRIBUTE hltypesMemberExport static String from_unicode(Array<unsigned int> chars);
		DEPRECATED_ATTRIBUTE hltypesMemberExport static String from_unicode(Array<wchar_t> chars);
		DEPRECATED_ATTRIBUTE hltypesMemberExport static String from_unicode(Array<char> chars);
		DEPRECATED_ATTRIBUTE hltypesMemberExport static String from_unicode(Array<unsigned char> chars);

	};
}

/// @brief Alias for simpler code.
typedef hltypes::String hstr;
/// @brief Alias for simpler code.
typedef const hltypes::String& chstr;

/// @brief Merges a C-type string and a String into a new String.
/// @param[in] string1 C-type string to merge.
/// @param[in] string2 String to merge.
/// @return Merged String.
hltypes::String hltypesFnExport operator+(const char* string1, const hltypes::String& string2);
/// @brief Merges a C-type string and a String into a new String.
/// @param[in] string1 C-type string to merge.
/// @param[in] string2 String to merge.
/// @return Merged String.
hltypes::String hltypesFnExport operator+(char* string1, const hltypes::String& string2);
/// @brief Applies formatting to a string.
/// @param[in] format C-type string containing format.
/// @param[in] args Variable argument list.
/// @return Formatted String.
hltypes::String hltypesFnExport hvsprintf(const char* format, va_list args);
/// @brief Applies formatting to a string.
/// @param[in] format C-type string containing format.
/// @param[in] ... Formatting arguments.
/// @return Formatted String.
hltypes::String hltypesFnExport hsprintf(const char* format, ...);

#endif

