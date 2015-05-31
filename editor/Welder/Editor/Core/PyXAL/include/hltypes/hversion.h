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
/// Provides versioning functionality.

#ifndef HLTYPES_VERSION_H
#define HLTYPES_VERSION_H

#include "harray.h"
#include "hltypesExport.h"
#include "hstring.h"

namespace hltypes
{
	/// @brief Provides versioning functionality.
	class hltypesExport Version
	{
	public:
		/// @brief Major version.
		unsigned int major;
		/// @brief Minor version.
		unsigned int minor;
		/// @brief Revision number.
		unsigned int revision;
		/// @brief Build number.
		unsigned int build;
		
		/// @brief Basic constructor.
		Version();
		/// @brief Constructor.
		/// @param[in] major Major version.
		/// @param[in] minor Minor version.
		/// @param[in] revision Revision number.
		/// @param[in] build Build number.
		Version(unsigned int major, unsigned int minor = 0, unsigned int revision = 0, unsigned int build = 0);
		/// @brief Destructor.
		~Version();
		
		/// @brief Checks validity of version.
		/// @return True if version is valid.
		/// @note An invalid version is considered only "0.0.0.0".
		bool isValid() const;
		
		/// @brief Sets the version values.
		/// @param[in] major Major version.
		/// @param[in] minor Minor version.
		/// @param[in] revision Revision number.
		/// @param[in] build Build number.
		void set(unsigned int major, unsigned int minor = 0, unsigned int revision = 0, unsigned int build = 0);
		/// @brief Sets the version values.
		/// @param[in] versions Array of versions.
		/// @note Only the first 4 values are used in versions.
		void set(Array<unsigned int> versions);
		/// @brief Sets the version values.
		/// @param[in] versions Version numbers separated by period characters.
		/// @note Only the first 4 values are used in versions.
		void set(const String& versions);
		/// @brief Creates a String representation of the Version.
		/// @param[in] count How many version values should be used (between 1 and 4).
		/// @return A String representation of the Version.
		String toString(int count = 3) const;
		
		/// @brief Checks if this Version is greater than another Version.
		/// @param[in] other Other Version.
		/// @return True if this Version is greater than another Version.
		bool operator>(const Version& other) const;
		/// @brief Checks if this Version is less than another Version.
		/// @param[in] other Other Version.
		/// @return True if this Version is less than another Version.
		bool operator<(const Version& other) const;
		/// @brief Checks if this Version is greater than or equal to another Version.
		/// @param[in] other Other Version.
		/// @return True if this Version is greater than or equal to another Version.
		bool operator>=(const Version& other) const;
		/// @brief Checks if this Version is less than or equal to another Version.
		/// @param[in] other Other Version.
		/// @return True if this Version is less than or equal to another Version.
		bool operator<=(const Version& other) const;
		/// @brief Checks if this Version equals another Version.
		/// @param[in] other Other Version.
		/// @return True if this Version equals another Version.
		bool operator==(const Version& other) const;
		/// @brief Checks if this Version non-equals another Version.
		/// @param[in] other Other Version.
		/// @return True if this Version non-equals another Version.
		bool operator!=(const Version& other) const;
		
	};

}

/// @brief Alias for simpler code.
typedef hltypes::Version hversion;

#endif
