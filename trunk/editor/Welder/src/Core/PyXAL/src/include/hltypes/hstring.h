/// @file
/// @version 2.3
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
	/// @todo capitalize?
	/// @todo swapcase?
	/// @todo utf8_len?
	/// @todo sscanf?
	class hltypesSpecialExport String : public std::basic_string<char>
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
		/// @param[in] s A C-type string.
		hltypesMemberExport String(const char* s);
		/// @brief Copy constructor.
		/// @param[in] s String to copy.
		hltypesMemberExport String(const String& s);
		/// @brief Copy constructor.
		/// @param[in] s std::string to copy.
		hltypesMemberExport String(const std::string& s);
		/// @brief Copy constructor.
		/// @param[in] s A C-type string.
		/// @param[in] length How many characters to copy.
		hltypesMemberExport String(const char* s, const int length);
		/// @brief Copy constructor.
		/// @param[in] s String to copy.
		/// @param[in] length How many characters to copy.
		hltypesMemberExport String(const String& s, const int length);
		/// @brief Type constructor.
		/// @param[in] i Integer to create String of.
		hltypesMemberExport String(const int i);
		/// @brief Type constructor.
		/// @param[in] i Unsigned integer to create String of.
		hltypesMemberExport String(const unsigned int i);
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

		/// @brief Splits the String with the delimiter once.
		/// @param[in] delimiter The character acting as splitting delimiter.
		/// @param[out] out_left First portion of the split String.
		/// @param[out] out_right Second portion of the split String.
		/// @return True if String was split.
		/// @brief Basic destructor.
		hltypesMemberExport bool split(const char delimiter, String& out_left, String& out_right) const;
		/// @brief Splits the String with the delimiter once.
		/// @param[in] delimiter The C-type string acting as splitting delimiter.
		/// @param[out] out_left First portion of the split String.
		/// @param[out] out_right Second portion of the split String.
		/// @return True if String was split.
		hltypesMemberExport bool split(const char* delimiter, String& out_left, String& out_right) const;
		/// @brief Splits the String with the delimiter once.
		/// @param[in] delimiter The String acting as splitting delimiter.
		/// @param[out] out_left First portion of the split String.
		/// @param[out] out_right Second portion of the split String.
		/// @return True if String was split.
		hltypesMemberExport bool split(const String& delimiter, String& out_left, String& out_right) const;
		/// @brief Reverse splits the String with the delimiter once.
		/// @param[in] delimiter The character acting as splitting delimiter.
		/// @param[out] out_left First portion of the split String.
		/// @param[out] out_right Second portion of the split String.
		/// @return True if String was split.
		hltypesMemberExport bool rsplit(const char delimiter, String& out_left, String& out_right) const;
		/// @brief Reverse splits the String with the delimiter once.
		/// @param[in] delimiter The C-type string acting as splitting delimiter.
		/// @param[out] out_left First portion of the split String.
		/// @param[out] out_right Second portion of the split String.
		/// @return True if String was split.
		hltypesMemberExport bool rsplit(const char* delimiter, String& out_left, String& out_right) const;
		/// @brief Reverse splits the String with the delimiter once.
		/// @param[in] delimiter The String acting as splitting delimiter.
		/// @param[out] out_left First portion of the split String.
		/// @param[out] out_right Second portion of the split String.
		/// @return True if String was split.
		hltypesMemberExport bool rsplit(const String& delimiter, String& out_left, String& out_right) const;
		/// @brief Counts the occurrences of a substring.
		/// @param[in] substr The character to look for.
		/// @return Number of occurrences of the substring.
		hltypesMemberExport int count(const char substr) const;
		/// @brief Counts the occurrences of a substring.
		/// @param[in] substr The C-type string to look for.
		/// @return Number of occurrences of the substring.
		hltypesMemberExport int count(const char* substr) const;
		/// @brief Counts the occurrences of a substring.
		/// @param[in] substr The String to look for.
		/// @return Number of occurrences of the substring.
		hltypesMemberExport int count(const String& substr) const;
		/// @brief Splits all characters in the String.
		/// @return Array of chars.
		hltypesMemberExport Array<char> split() const;
		/// @brief Splits the String with the delimiter.
		/// @param[in] delimiter The character acting as splitting delimiter.
		/// @param[in] n How many times the string should be split maximally.
		/// @param[in] remove_empty Whether to remove empty strings from result.
		/// @return Array of Strings.
		hltypesMemberExport Array<String> split(const char delimiter, unsigned int n = -1, bool remove_empty = false) const;
		/// @brief Splits the String with the delimiter.
		/// @param[in] delimiter The C-type string acting as splitting delimiter.
		/// @param[in] n How many times the string should be split maximally.
		/// @param[in] remove_empty Whether to remove empty strings from result.
		/// @return Array of Strings.
		hltypesMemberExport Array<String> split(const char* delimiter, unsigned int n = -1, bool remove_empty = false) const;
		/// @brief Splits the String with the delimiter.
		/// @param[in] delimiter The String acting as splitting delimiter.
		/// @param[in] n How many times the string should be split maximally.
		/// @param[in] remove_empty Whether to remove empty strings from result.
		/// @return Array of Strings.
		hltypesMemberExport Array<String> split(const String& delimiter, unsigned int n = -1, bool remove_empty = false) const;
		/// @brief Reverse splits the String with the delimiter.
		/// @param[in] delimiter The character acting as splitting delimiter.
		/// @param[in] n How many times the string should be split maximally.
		/// @param[in] remove_empty Whether to remove empty strings from result.
		/// @return Array of Strings.
		hltypesMemberExport Array<String> rsplit(const char delimiter, unsigned int n = -1, bool remove_empty = false) const;
		/// @brief Reverse splits the String with the delimiter.
		/// @param[in] delimiter The C-type string acting as splitting delimiter.
		/// @param[in] n How many times the string should be split maximally.
		/// @param[in] remove_empty Whether to remove empty strings from result.
		/// @return Array of Strings.
		hltypesMemberExport Array<String> rsplit(const char* delimiter, unsigned int n = -1, bool remove_empty = false) const;
		/// @brief Reverse splits the String with the delimiter.
		/// @param[in] delimiter The String acting as splitting delimiter.
		/// @param[in] n How many times the string should be split maximally.
		/// @param[in] remove_empty Whether to remove empty strings from result.
		/// @return Array of Strings.
		hltypesMemberExport Array<String> rsplit(const String& delimiter, unsigned int n = -1, bool remove_empty = false) const;
		/// @brief Checks if the string starts with a specific string.
		/// @param[in] s The C-type string to check.
		/// @return True if String starts with s.
		hltypesMemberExport bool starts_with(const char* s) const;
		/// @brief Checks if the string starts with a specific string.
		/// @param[in] s The String to check.
		/// @return True if String starts with s.
		hltypesMemberExport bool starts_with(const String& s) const;
		/// @brief Checks if the string ends with a specific string.
		/// @param[in] s The C-type string to check.
		/// @return True if String ends with s.
		hltypesMemberExport bool ends_with(const char* s) const;
		/// @brief Checks if the string ends with a specific string.
		/// @param[in] s The String to check.
		/// @return True if String ends with s.
		hltypesMemberExport bool ends_with(const String& s) const;
		/// @brief Transforms String into lower case.
		/// @return String in lower case.
		hltypesMemberExport String lower() const;
		/// @brief Transforms String into upper case.
		/// @return String in upper case.
		hltypesMemberExport String upper() const;
		/// @brief Reverses String.
		/// @return Reversed String.
		hltypesMemberExport String reverse() const;
		/// @brief Checks if all elements of the string contain only one digit '0'-'9'.
		/// @return True if string is a digit.
		hltypesMemberExport bool is_digit() const;
		/// @brief Checks if the string is an integer.
		/// @return True if string is a number.
		hltypesMemberExport bool is_int() const;
		/// @brief Checks if the string is a float.
		/// @param[in] require_dot If this parameter is false, then a decimal point is not required to designate a float value.
		/// @return True if string is a number.
		hltypesMemberExport bool is_float(bool require_dot = true) const;
		/// @brief Checks if the string is a number, positive or negative integer or float.
		/// @return True if string is a number.
		hltypesMemberExport bool is_number() const;
		/// @brief Checks if the string is a hexadecimal number, case ignored.
		/// @return True if string is a hex number.
		/// @note This method is case insensitive.
		/// @note Hex numbers cannot be negative in this context.
		hltypesMemberExport bool is_hex() const;
		/// @brief Left-trims and right-trims String from a specific character.
		/// @param[in] c Character to trim.
		/// @return Trimmed String.
		hltypesMemberExport String trim(char c = ' ') const;
		/// @brief Left-trims String from a specific character.
		/// @param[in] c Character to trim.
		/// @return Left-trimmed String.
		hltypesMemberExport String ltrim(char c = ' ') const;
		/// @brief Right-trims String from a specific character.
		/// @param[in] c Character to trim.
		/// @return Right-trimmed String.
		hltypesMemberExport String rtrim(char c = ' ') const;
		/// @brief Replaces occurrences of a substring with another substring.
		/// @param[in] what C-type substring.
		/// @param[in] with_what C-type substitution.
		/// @return New String.
		hltypesMemberExport String replace(const char* what, const char* with_what) const;
		/// @brief Replaces occurrences of a substring with another substring.
		/// @param[in] what String substring.
		/// @param[in] with_what C-type substitution.
		/// @return New String.
		hltypesMemberExport String replace(const String& what, const char* with_what) const;
		/// @brief Replaces occurrences of a substring with another substring.
		/// @param[in] what C-type substring.
		/// @param[in] with_what String substitution.
		/// @return New String.
		hltypesMemberExport String replace(const char* what, const String& with_what) const;
		/// @brief Replaces occurrences of a substring with another substring.
		/// @param[in] what String substring.
		/// @param[in] with_what String substitution.
		/// @return New String.
		hltypesMemberExport String replace(const String& what, const String& with_what) const;
		/// @brief Replaces a sequence of characters with a substring.
		/// @param[in] pos1 Start index of character sequence.
		/// @param[in] n1 How many characters to replace.
		/// @param[in] str String substitution.
		/// @return New String.
		hltypesMemberExport String replace(int pos1, int n1, const String& str);
		/// @brief Replaces a sequence of characters with a substring.
		/// @param[in] pos1 Start index of character sequence.
		/// @param[in] n1 How many characters to replace.
		/// @param[in] str String substitution.
		/// @param[in] pos2 Start index in substring.
		/// @param[in] n2 How many characters from substring.
		/// @return New String.
		hltypesMemberExport String replace(int pos1, int n1, const String& str, int pos2, int n2);
		/// @brief Replaces a sequence of characters with a substring.
		/// @param[in] pos1 Start index of character sequence.
		/// @param[in] n1 How many characters to replace.
		/// @param[in] s C-type string substitution.
		/// @return New String.
		hltypesMemberExport String replace(int pos1, int n1, const char* s);
		/// @brief Replaces a sequence of characters with a substring.
		/// @param[in] pos1 Start index of character sequence.
		/// @param[in] n1 How many characters to replace.
		/// @param[in] s C-type string substitution.
		/// @param[in] n2 Length of C-type string.
		/// @return New String.
		hltypesMemberExport String replace(int pos1, int n1, const char* s, int n2);
		/// @brief Replaces a sequence of characters with a substring.
		/// @param[in] pos1 Start index of character sequence.
		/// @param[in] n1 How many characters to replace.
		/// @param[in] c Character substitution.
		/// @param[in] n2 Number of times character should be inserted.
		/// @return New String.
		hltypesMemberExport String replace(int pos1, int n1, char c, int n2);
		/// @brief Checks if String contains character.
		/// @param[in] c Character to search for.
		/// @return True if String contains character.
		hltypesMemberExport bool contains(const char c) const;
		/// @brief Checks if String contains C-type string.
		/// @param[in] s C-type string to search for.
		/// @return True if String contains C-type string.
		hltypesMemberExport bool contains(const char* s) const;
		/// @brief Checks if String contains another String.
		/// @param[in] s String to search for.
		/// @return True if this String contains other String.
		hltypesMemberExport bool contains(const String& s) const;
		/// @brief Checks if String contains any character from a C-type string.
		/// @param[in] s C-type string to search for.
		/// @return True if String contains any character from a C-type string.
		hltypesMemberExport bool contains_any(const char* s) const;
		/// @brief Checks if String contains any character from another String.
		/// @param[in] s String to search for.
		/// @return True if this String contains any character from another String.
		hltypesMemberExport bool contains_any(const String& s) const;
		/// @brief Checks if String contains all characters from a C-type string.
		/// @param[in] s C-type string to search for.
		/// @return True if String contains all characters from a C-type string.
		hltypesMemberExport bool contains_all(const char* s) const;
		/// @brief Checks if String contains all characters from another String.
		/// @param[in] s String to search for.
		/// @return True if this String contains all characters from another String.
		hltypesMemberExport bool contains_all(const String& s) const;
		/// @brief Creates a substring from UTF8-indexed characters.
		/// @param[in] start Start index of the substring.
		/// @param[in] count Character length of the substring (UT8, not ASCII).
		/// @return The substring.
		hltypesMemberExport String substr(int start, int count) const;
		/// @brief Creates a substring from UTF8-indexed characters.
		/// @param[in] start Start index of the substring.
		/// @param[in] count Character length of the substring (UT8, not ASCII).
		/// @return The substring.
		hltypesMemberExport String utf8_substr(int start, int count) const;
		/// @brief Gets the byte length of the String.
		/// @return Byte length of String.
		hltypesMemberExport int size() const;
		/// @brief Same as size.
		/// @see size
		hltypesMemberExport int length() const;
		/// @brief Gets the character length of the String.
		/// @return Character length of String.
		hltypesMemberExport int utf8_size() const;
		/// @brief Same as utf8_size.
		/// @see utf8_size
		hltypesMemberExport int utf8_length() const;
		/// @brief Checks if string contains ASCII only characters.
		/// @return True if String contains only ASCII-7 characters.
		hltypesMemberExport bool is_ascii() const;
		/// @brief Creates a string with characters converted using the %02X format.
		/// @return String of hex values of the characters.
		hltypesMemberExport String to_hex() const;
		/// @brief Creates an unsigned int from hex value string.
		/// @return An unsigned int.
		/// @note Will return 0 if string is not a hex number. Use String::is_hex() to check first.
		/// @note Hex strings above 0xFFFFFFFF cause undefined behavior.
		hltypesMemberExport unsigned int unhex() const;

		/// @brief Casts String into float.
		hltypesMemberExport operator float() const;
		/// @brief Casts String into double.
		hltypesMemberExport operator double() const;
		/// @brief Casts String into int.
		hltypesMemberExport operator int() const;
		/// @brief Casts String into unsigned int.
		hltypesMemberExport operator unsigned int() const;
		/// @brief Casts String into bool.
		/// @note "false", "0" and "" are regarded as false, everything else is regarded as true.
		hltypesMemberExport operator bool() const;
		/// @brief Converts float into String.
		/// @param[in] f Float value.
		hltypesMemberExport void operator=(const float f);
		/// @brief Converts double into String.
		/// @param[in] d Double value.
		hltypesMemberExport void operator=(const double d);
		/// @brief Converts int into String.
		/// @param[in] i Int value.
		hltypesMemberExport void operator=(const int i);
		/// @brief Converts unsigned int into String.
		/// @param[in] i Unsigned int value.
		hltypesMemberExport void operator=(const unsigned int i);
		/// @brief Converts bool into String.
		/// @param[in] b Bool value.
		hltypesMemberExport void operator=(const bool b);
		/// @brief Converts std::string into String.
		/// @param[in] s std::string value.
		hltypesMemberExport void operator=(const std::string& s);
		/// @brief Converts C-type string into String.
		/// @param[in] s C-type string value.
		hltypesMemberExport void operator=(const char* s);
		/// @brief Converts float into a String and concatenates the new String at the end of this one.
		/// @param[in] f Float value.
		hltypesMemberExport void operator+=(const float f);
		/// @brief Converts int into a String and concatenates the new String at the end of this one.
		/// @param[in] i Int value.
		hltypesMemberExport void operator+=(const int i);
		/// @brief Converts unsigned int into a String and concatenates the new String at the end of this one.
		/// @param[in] i Unsigned int value.
		hltypesMemberExport void operator+=(const unsigned int i);
		/// @brief Converts bool into a String and concatenates the new String at the end of this one.
		/// @param[in] b Bool value.
		hltypesMemberExport void operator+=(const bool b);
		/// @brief Converts char into a String and concatenates the new String at the end of this one.
		/// @param[in] c Character value.
		hltypesMemberExport void operator+=(const char c);
		/// @brief Converts std::string into a String and concatenates the new String at the end of this one.
		/// @param[in] s std::string value.
		hltypesMemberExport void operator+=(const std::string& s);
		/// @brief Converts C-type string into a String and concatenates the new String at the end of this one.
		/// @param[in] s C-type string value.
		hltypesMemberExport void operator+=(const char* s);
		/// @brief Merges String with a C-type string converted into String first.
		/// @param[in] s C-type string value.
		/// @return New String.
		hltypesMemberExport String operator+(const char* s) const;
		/// @brief Merges String with a character converted into String first.
		/// @param[in] c Character value.
		/// @return New String.
		hltypesMemberExport String operator+(const char c) const;
		/// @brief Merges String with a C-type string converted into String first.
		/// @param[in] s C-type string value.
		/// @return New String.
		hltypesMemberExport String operator+(char* s) const;
		/// @brief Merges String with another String.
		/// @param[in] s String value.
		/// @return New String.
		hltypesMemberExport String operator+(const String& s) const;
		/// @brief Merges String with an std::string converted into String first.
		/// @param[in] s std::string value.
		/// @return New String.
		hltypesMemberExport String operator+(const std::string& s) const;
		/// @brief Compares String for equivalency.
		/// @param[in] f Float value.
		/// @return True if value converted into String is equal to this one.
		hltypesMemberExport bool operator==(const float f) const;
		/// @brief Compares String for equivalency.
		/// @param[in] i Int value.
		/// @return True if value converted into String is equal to this one.
		hltypesMemberExport bool operator==(const int i) const;
		/// @brief Compares String for equivalency.
		/// @param[in] i Unsigned int value.
		/// @return True if value converted into String is equal to this one.
		hltypesMemberExport bool operator==(const unsigned int i) const;
		/// @brief Compares String for equivalency.
		/// @param[in] b bool value.
		/// @return True if value converted into String is equal to this one.
		hltypesMemberExport bool operator==(const bool b) const;
		/// @brief Compares String for equivalency.
		/// @param[in] s C-type string value.
		/// @return True if value converted into String is equal to this one.
		hltypesMemberExport bool operator==(const char* s) const;
		/// @brief Compares String for equivalency.
		/// @param[in] s std::string value.
		/// @return True if value converted into String is equal to this one.
		hltypesMemberExport bool operator==(const std::string& s) const;
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

		/// @brief Creates an unicode (unsigned int) string.
		/// @return A unicode (unsigned int) string.
		hltypesMemberExport std::basic_string<unsigned int> u_str() const;
		/// @brief Creates a wchar string.
		/// @return A wchar string.
		hltypesMemberExport std::basic_string<wchar_t> w_str() const;
		/// @brief Converts first UTF8 character into the corresponding character code.
		/// @param[in] index The byte position of the first character in the string.
		/// @param[out] character_length Length of UTF8 character in bytes.
		/// @return Character code.
		/// @note The out value of character_length parameter can be used to move a character iterator forward.
		hltypesMemberExport unsigned int first_unicode_char(int index = 0, int* character_length = NULL) const;
		/// @brief Converts a unicode unsigned int to a UTF8 string.
		/// @param[in] value The unsigned int value.
		/// @return UTF8 string.
		hltypesMemberExport static String from_unicode(unsigned int value);
		/// @brief Converts a unicode wchar to a UTF8 string.
		/// @param[in] value The wchar value.
		/// @return UTF8 string.
		hltypesMemberExport static String from_unicode(wchar_t value);
		/// @brief Converts a char to a UTF8 string.
		/// @param[in] string The char.
		/// @return UTF8 string.
		hltypesMemberExport static String from_unicode(char value);
		/// @brief Converts an unsigned char to a UTF8 string.
		/// @param[in] string The unsigned char.
		/// @return UTF8 string.
		hltypesMemberExport static String from_unicode(unsigned char value);
		/// @brief Converts a unicode unsigned int string to a UTF8 string.
		/// @param[in] string The unsigned int string.
		/// @return UTF8 string.
		hltypesMemberExport static String from_unicode(const unsigned int* string);
		/// @brief Converts a unicode wchar string to a UTF8 string.
		/// @param[in] string The wchar string.
		/// @return UTF8 string.
		hltypesMemberExport static String from_unicode(const wchar_t* string);
		/// @brief Converts a char string to a UTF8 string.
		/// @param[in] string The char string.
		/// @return UTF8 string.
		hltypesMemberExport static String from_unicode(const char* string);
		/// @brief Converts an unsigned char string to a UTF8 string.
		/// @param[in] string The unsigned char string.
		/// @return UTF8 string.
		hltypesMemberExport static String from_unicode(const unsigned char* string);
		/// @brief Converts a unicode unsigned int Array to a UTF8 string.
		/// @param[in] string The unsigned int characters.
		/// @return UTF8 string.
		hltypesMemberExport static String from_unicode(Array<unsigned int> chars);
		/// @brief Converts a unicode wchar Array to a UTF8 string.
		/// @param[in] string The wchar characters.
		/// @return UTF8 string.
		hltypesMemberExport static String from_unicode(Array<wchar_t> chars);
		/// @brief Converts a char Array to a UTF8 string.
		/// @param[in] string The char characters.
		/// @return UTF8 string.
		hltypesMemberExport static String from_unicode(Array<char> chars);
		/// @brief Converts an unsigned char Array to a UTF8 string.
		/// @param[in] string The unsigned char characters.
		/// @return UTF8 string.
		hltypesMemberExport static String from_unicode(Array<unsigned char> chars);

	};
}

/// @brief Alias for simpler code.
typedef hltypes::String hstr;
/// @brief Alias for simpler code.
typedef const hltypes::String& chstr;

/// @brief Merges a C-type string and a String into a new String.
/// @param[in] s1 C-type string to merge.
/// @param[in] s2 String to merge.
/// @return Merged String.
hstr hltypesFnExport operator+(const char* s1, chstr s2);
/// @brief Merges a C-type string and a String into a new String.
/// @param[in] s1 C-type string to merge.
/// @param[in] s2 String to merge.
/// @return Merged String.
hstr hltypesFnExport operator+(char* s1, chstr s2);
/// @brief Applies formatting to a string.
/// @param[in] format C-type string containing format.
/// @param[in] args Variable argument list.
/// @return Formatted String.
hstr hltypesFnExport hvsprintf(const char* format, va_list args);
/// @brief Applies formatting to a string.
/// @param[in] format C-type string containing format.
/// @param[in] ... Formatting arguments.
/// @return Formatted String.
hstr hltypesFnExport hsprintf(const char* format, ...);

#endif

