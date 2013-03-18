/// @file
/// @author  Kresimir Spes
/// @author  Boris Mikic
/// @author  Ivan Vucica
/// @author  Domagoj Cerjan
/// @version 2.0
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://www.opensource.org/licenses/bsd-license.php
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
/// @brief Circumvents a compilation problem in VS 2010
const std::string::size_type std::string::npos = size_t(-1);
#endif

namespace hltypes
{
	template <class T> class Array;
	
	/// @brief Encapsulates std::string and adds high level methods.
	/// @author Kresimir Spes
	/// @author Boris Mikic
	/// @author Ivan Vucica
	/// @author Domagoj Cerjan
	/// @todo capitalize?
	/// @todo swapcase?
	/// @todo utf8_len?
	/// @todo sscanf?
	class hltypesExport String : public std::basic_string<char>
	{
	public:
		/// @brief Empty constructor.
		String();
		/// @brief Basic constructor.
		/// @param[in] c A character.
		String(const char c);
		/// @brief Basic constructor.
		/// @param[in] c A character.
		/// @param[in] times How many times c should be added.
		String(const char c, const int times);
		/// @brief Copy constructor.
		/// @param[in] s A C-type string.
		String(const char* s);
		/// @brief Copy constructor.
		/// @param[in] s String to copy.
		String(const String& s);
		/// @brief Copy constructor.
		/// @param[in] s std::string to copy.
		String(const std::string& s);
		/// @brief Copy constructor.
		/// @param[in] s A C-type string.
		/// @param[in] length How many characters to copy.
		String(const char* s, const int length);
		/// @brief Copy constructor.
		/// @param[in] s String to copy.
		/// @param[in] length How many characters to copy.
		String(const String& s, const int length);
		/// @brief Type constructor.
		/// @param[in] i Integer to create String of.
		String(const int i);
		/// @brief Type constructor.
		/// @param[in] i Unsigned integer to create String of.
		String(const unsigned int i);
		/// @brief Type constructor.
		/// @param[in] f Float to create String of.
		String(const float f);
		/// @brief Type constructor.
		/// @param[in] f Float to create String of.
		/// @param[in] precision The floating point precision to use.
		String(const float f, int precision);
		/// @brief Destructor.
		~String();

		/// @brief Splits the String with the delimiter once.
		/// @param[in] delimiter The character acting as splitting delimiter.
		/// @param[out] out_left First portion of the split String.
		/// @param[out] out_right Second portion of the split String.
		/// @return True if String was split.
		/// @brief Basic destructor.
		bool split(const char delimiter, String& out_left, String& out_right) const;
		/// @brief Splits the String with the delimiter once.
		/// @param[in] delimiter The C-type string acting as splitting delimiter.
		/// @param[out] out_left First portion of the split String.
		/// @param[out] out_right Second portion of the split String.
		/// @return True if String was split.
		bool split(const char* delimiter, String& out_left, String& out_right) const;
		/// @brief Splits the String with the delimiter once.
		/// @param[in] delimiter The String acting as splitting delimiter.
		/// @param[out] out_left First portion of the split String.
		/// @param[out] out_right Second portion of the split String.
		/// @return True if String was split.
		bool split(const String& delimiter, String& out_left, String& out_right) const;
		/// @brief Reverse splits the String with the delimiter once.
		/// @param[in] delimiter The character acting as splitting delimiter.
		/// @param[out] out_left First portion of the split String.
		/// @param[out] out_right Second portion of the split String.
		/// @return True if String was split.
		bool rsplit(const char delimiter, String& out_left, String& out_right) const;
		/// @brief Reverse splits the String with the delimiter once.
		/// @param[in] delimiter The C-type string acting as splitting delimiter.
		/// @param[out] out_left First portion of the split String.
		/// @param[out] out_right Second portion of the split String.
		/// @return True if String was split.
		bool rsplit(const char* delimiter, String& out_left, String& out_right) const;
		/// @brief Reverse splits the String with the delimiter once.
		/// @param[in] delimiter The String acting as splitting delimiter.
		/// @param[out] out_left First portion of the split String.
		/// @param[out] out_right Second portion of the split String.
		/// @return True if String was split.
		bool rsplit(const String& delimiter, String& out_left, String& out_right) const;
		/// @brief Counts the occurrences of a substring.
		/// @param[in] substr The character to look for.
		/// @return Number of occurrences of the substring.
		int count(const char substr) const;
		/// @brief Counts the occurrences of a substring.
		/// @param[in] substr The C-type string to look for.
		/// @return Number of occurrences of the substring.
		int count(const char* substr) const;
		/// @brief Counts the occurrences of a substring.
		/// @param[in] substr The String to look for.
		/// @return Number of occurrences of the substring.
		int count(const String& substr) const;
		/// @brief Splits the String with the delimiter.
		/// @param[in] delimiter The character acting as splitting delimiter.
		/// @param[in] n How many times the string should be split maximally.
		/// @param[in] remove_empty Whether to remove empty strings from result.
		/// @return Array of Strings.
		Array<String> split(const char delimiter, unsigned int n = -1, bool remove_empty = false) const;
		/// @brief Splits the String with the delimiter.
		/// @param[in] delimiter The C-type string acting as splitting delimiter.
		/// @param[in] n How many times the string should be split maximally.
		/// @param[in] remove_empty Whether to remove empty strings from result.
		/// @return Array of Strings.
		Array<String> split(const char* delimiter, unsigned int n = -1, bool remove_empty = false) const;
		/// @brief Splits the String with the delimiter.
		/// @param[in] delimiter The String acting as splitting delimiter.
		/// @param[in] n How many times the string should be split maximally.
		/// @param[in] remove_empty Whether to remove empty strings from result.
		/// @return Array of Strings.
		Array<String> split(const String& delimiter, unsigned int n = -1, bool remove_empty = false) const;
		/// @brief Reverse splits the String with the delimiter.
		/// @param[in] delimiter The character acting as splitting delimiter.
		/// @param[in] n How many times the string should be split maximally.
		/// @param[in] remove_empty Whether to remove empty strings from result.
		/// @return Array of Strings.
		Array<String> rsplit(const char delimiter, unsigned int n = -1, bool remove_empty = false) const;
		/// @brief Reverse splits the String with the delimiter.
		/// @param[in] delimiter The C-type string acting as splitting delimiter.
		/// @param[in] n How many times the string should be split maximally.
		/// @param[in] remove_empty Whether to remove empty strings from result.
		/// @return Array of Strings.
		Array<String> rsplit(const char* delimiter, unsigned int n = -1, bool remove_empty = false) const;
		/// @brief Reverse splits the String with the delimiter.
		/// @param[in] delimiter The String acting as splitting delimiter.
		/// @param[in] n How many times the string should be split maximally.
		/// @param[in] remove_empty Whether to remove empty strings from result.
		/// @return Array of Strings.
		Array<String> rsplit(const String& delimiter, unsigned int n = -1, bool remove_empty = false) const;
		/// @brief Checks if the string starts with a specific string.
		/// @param[in] s The C-type string to check.
		/// @return True if String starts with s.
		bool starts_with(const char* s) const;
		/// @brief Checks if the string starts with a specific string.
		/// @param[in] s The String to check.
		/// @return True if String starts with s.
		bool starts_with(const String& s) const;
		/// @brief Checks if the string ends with a specific string.
		/// @param[in] s The C-type string to check.
		/// @return True if String ends with s.
		bool ends_with(const char* s) const;
		/// @brief Checks if the string ends with a specific string.
		/// @param[in] s The String to check.
		/// @return True if String ends with s.
		bool ends_with(const String& s) const;
		/// @brief Transforms String into lower case.
		/// @return String in lower case.
		String lower() const;
		/// @brief Transforms String into upper case.
		/// @return String in upper case.
		String upper() const;
		/// @brief Reverses String.
		/// @return Reversed String.
		String reverse() const;
		/// @brief Checks if all elements of the string contain only one digit '0'-'9'.
		/// @return True if string is a digit.
		bool is_digit() const;
		/// @brief Checks if the string is an integer.
		/// @return True if string is a number.
		bool is_int() const;
		/// @brief Checks if the string is a float.
		/// @param[in] require_dot If this parameter is false, then a decimal point is not required to designate a float value.
		/// @return True if string is a number.
		bool is_float(bool require_dot = true) const;
		/// @brief Checks if the string is a number, positive or negative integer or float.
		/// @return True if string is a number.
		bool is_number() const;
		/// @brief Checks if the string is a hexadecimal number, case ignore.
		/// @return True if string is a hex number.
		/// @note This method is case insensitive.
		/// @note Hex numbers cannot be negative in this context.
		bool is_hex() const;
		/// @brief Left-trims and right-trims String from a specific character.
		/// @param[in] c Character to trim.
		/// @return Trimmed String.
		String trim(char c = ' ') const;
		/// @brief Left-trims String from a specific character.
		/// @param[in] c Character to trim.
		/// @return Left-trimmed String.
		String ltrim(char c = ' ') const;
		/// @brief Right-trims String from a specific character.
		/// @param[in] c Character to trim.
		/// @return Right-trimmed String.
		String rtrim(char c = ' ') const;
		/// @brief Replaces occurrences of a substring with another substring.
		/// @param[in] what C-type substring.
		/// @param[in] with_what C-type substitution.
		/// @return New String.
		String replace(const char* what, const char* with_what) const;
		/// @brief Replaces occurrences of a substring with another substring.
		/// @param[in] what String substring.
		/// @param[in] with_what C-type substitution.
		/// @return New String.
		String replace(const String& what, const char* with_what) const;
		/// @brief Replaces occurrences of a substring with another substring.
		/// @param[in] what C-type substring.
		/// @param[in] with_what String substitution.
		/// @return New String.
		String replace(const char* what, const String& with_what) const;
		/// @brief Replaces occurrences of a substring with another substring.
		/// @param[in] what String substring.
		/// @param[in] with_what String substitution.
		/// @return New String.
		String replace(const String& what, const String& with_what) const;
		/// @brief Replaces a sequence of characters with a substring.
		/// @param[in] pos1 Start index of character sequence.
		/// @param[in] n1 How many characters to replace.
		/// @param[in] str String substitution.
		/// @return New String.
		String replace(int pos1, int n1, const String& str);
		/// @brief Replaces a sequence of characters with a substring.
		/// @param[in] pos1 Start index of character sequence.
		/// @param[in] n1 How many characters to replace.
		/// @param[in] str String substitution.
		/// @param[in] pos2 Start index in substring.
		/// @param[in] n2 How many characters from substring.
		/// @return New String.
		String replace(int pos1, int n1, const String& str, int pos2, int n2);
		/// @brief Replaces a sequence of characters with a substring.
		/// @param[in] pos1 Start index of character sequence.
		/// @param[in] n1 How many characters to replace.
		/// @param[in] s C-type string substitution.
		/// @return New String.
		String replace(int pos1, int n1, const char* s);
		/// @brief Replaces a sequence of characters with a substring.
		/// @param[in] pos1 Start index of character sequence.
		/// @param[in] n1 How many characters to replace.
		/// @param[in] s C-type string substitution.
		/// @param[in] n2 Length of C-type string.
		/// @return New String.
		String replace(int pos1, int n1, const char* s, int n2);
		/// @brief Replaces a sequence of characters with a substring.
		/// @param[in] pos1 Start index of character sequence.
		/// @param[in] n1 How many characters to replace.
		/// @param[in] c Character substitution.
		/// @param[in] n2 Number of times character should be inserted.
		/// @return New String.
		String replace(int pos1, int n1, char c, int n2);
		/// @brief Checks if String contains character.
		/// @param[in] c Character to search for.
		/// @return True if String contains character.
		bool contains(const char c) const;
		/// @brief Checks if String contains C-type string.
		/// @param[in] s C-type string to search for.
		/// @return True if String contains C-type string.
		bool contains(const char* s) const;
		/// @brief Checks if String contains another String.
		/// @param[in] s String to search for.
		/// @return True if this String contains other String.
		bool contains(const String& s) const;
		/// @brief Gets the length of the String.
		/// @return Length of String.
		int size() const;
		/// @brief Same as size.
		/// @see size
		int length() const;
		/// @brief Creates a string with characters converted using the %02X format.
		/// @return String of hex values of the charcaters.
		String to_hex() const;
		/// @brief Creates an unicode (unsigned int) string.
		/// @return A unicode (unsigned int) string.
		std::basic_string<unsigned int> u_str() const;
#ifndef _ANDROID
		/// @brief Creates a wchar string.
		/// @return A wchar string.
		std::basic_string<wchar_t> w_str() const;
#endif

		/// @brief Casts String into float.
		operator float() const;
		/// @brief Casts String into int.
		operator int() const;
		/// @brief Casts String into unsigned int.
		operator unsigned int() const;
		/// @brief Casts String into bool.
		/// @note "false", "0" and "" are regarded as false, everything else is regarded as true.
		operator bool() const;
		/// @brief Converts float into String.
		/// @param[in] f Float value.
		void operator=(const float f);
		/// @brief Converts int into String.
		/// @param[in] i Int value.
		void operator=(const int i);
		/// @brief Converts unsigned int into String.
		/// @param[in] i Unsigned int value.
		void operator=(const unsigned int i);
		/// @brief Converts bool into String.
		/// @param[in] b Bool value.
		void operator=(const bool b);
		/// @brief Converts std::string into String.
		/// @param[in] s std::string value.
		void operator=(const std::string& s);
		/// @brief Converts C-type string into String.
		/// @param[in] s C-type string value.
		void operator=(const char* s);
		/// @brief Converts float into a String and concatenates the new String at the end of this one.
		/// @param[in] f Float value.
		void operator+=(const float f);
		/// @brief Converts int into a String and concatenates the new String at the end of this one.
		/// @param[in] i Int value.
		void operator+=(const int i);
		/// @brief Converts unsigned int into a String and concatenates the new String at the end of this one.
		/// @param[in] i Unsigned int value.
		void operator+=(const unsigned int i);
		/// @brief Converts bool into a String and concatenates the new String at the end of this one.
		/// @param[in] b Bool value.
		void operator+=(const bool b);
		/// @brief Converts char into a String and concatenates the new String at the end of this one.
		/// @param[in] c Character value.
		void operator+=(const char c);
		/// @brief Converts std::string into a String and concatenates the new String at the end of this one.
		/// @param[in] s std::string value.
		void operator+=(const std::string& s);
		/// @brief Converts C-type string into a String and concatenates the new String at the end of this one.
		/// @param[in] s C-type string value.
		void operator+=(const char* s);
		/// @brief Merges String with a C-type string converted into String first.
		/// @param[in] s C-type string value.
		/// @return New String.
		String operator+(const char* s) const;
		/// @brief Merges String with a character converted into String first.
		/// @param[in] c Character value.
		/// @return New String.
		String operator+(const char c) const;
		/// @brief Merges String with a C-type string converted into String first.
		/// @param[in] s C-type string value.
		/// @return New String.
		String operator+(char* s) const;
		/// @brief Merges String with another String.
		/// @param[in] s String value.
		/// @return New String.
		String operator+(const String& s) const;
		/// @brief Merges String with an std::string converted into String first.
		/// @param[in] s std::string value.
		/// @return New String.
		String operator+(const std::string& s) const;
		/// @brief Compares String for equivalency.
		/// @param[in] f Float value.
		/// @return True if value converted into String is equal to this one.
		bool operator==(const float f) const;
		/// @brief Compares String for equivalency.
		/// @param[in] i Int value.
		/// @return True if value converted into String is equal to this one.
		bool operator==(const int i) const;
		/// @brief Compares String for equivalency.
		/// @param[in] i Unsigned int value.
		/// @return True if value converted into String is equal to this one.
		bool operator==(const unsigned int i) const;
		/// @brief Compares String for equivalency.
		/// @param[in] b bool value.
		/// @return True if value converted into String is equal to this one.
		bool operator==(const bool b) const;
		/// @brief Compares String for equivalency.
		/// @param[in] s C-type string value.
		/// @return True if value converted into String is equal to this one.
		bool operator==(const char* s) const;
		/// @brief Compares String for equivalency.
		/// @param[in] s std::string value.
		/// @return True if value converted into String is equal to this one.
		bool operator==(const std::string& s) const;
		/// @brief Creates a substring.
		/// @param[in] start Start index of the substring.
		/// @param[in] count Length of the substring.
		/// @return The substring.
		String operator()(int start, int count) const;
		/// @brief Creates a substring.
		/// @param[in] start Start index of the substring.
		/// @param[in] count Length of the substring.
		/// @param[in] step Every nth character only.
		/// @return The substring.
		/// @note count defines the length of the substring, step only defines which characters are used for the new String.
		String operator()(int start, int count, int step) const;
		/// @brief Returns character at position in form of String.
		/// @param[in] index Index of the character.
		/// @return A String.
		String operator()(int index) const;
		/// @brief Returns character at position.
		/// @param[in] index Index of the character.
		/// @return A character.
		char& operator[](int index);
		/// @brief Returns character at position.
		/// @param[in] index Index of the character.
		/// @return A character.
		const char& operator[](int index) const;

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

