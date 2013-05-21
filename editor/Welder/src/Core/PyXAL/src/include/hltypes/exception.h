/// @file
/// @author  Kresimir Spes
/// @author  Boris Mikic
/// @version 2.0
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://www.opensource.org/licenses/bsd-license.php
/// 
/// @section DESCRIPTION
/// 
/// Provides high level exceptions.

#ifndef HLTYPES_EXCEPTION_H
#define HLTYPES_EXCEPTION_H

#include "hstring.h"

#include "hltypesExport.h"

namespace hltypes
{
	/// @brief Provides functionality of a basic exception.
	class hltypesExport exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] message Exception message.
		/// @param[in] source_file Name of the source file.
		/// @param[in] line_number Number of the line.
		exception(chstr message, const char* source_file, int line_number);
		/// @brief Destructor.
		virtual ~exception();
		/// @brief Gets the exception message.
		/// @return The exception message.
		virtual hstr message() { return this->msg; }
		/// @brief Same as message.
		/// @see message
		hstr getErrorText() { return this->message(); }
		/// @brief Same as message.
		/// @see message
		hstr getMessage() { return this->message(); }
		/// @brief Same as message.
		/// @see message
		hstr getErrorMessage() { return this->message(); }
		
	protected:
		/// @brief Exception message.
		hstr msg;
		
	};
	/// @brief Alias for simpler code.
	#define hl_exception(msg) hltypes::exception(msg, __FILE__, __LINE__)
	
	/// @brief Defines a file-not-found exception.
	class hltypesExport _file_not_found : public exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] filename Name of the file.
		/// @param[in] source_file Name of the source file.
		/// @param[in] line_number Number of the line.
		_file_not_found(chstr filename, const char* source_file, int line_number);
		~_file_not_found();
		
	};
	/// @brief Alias for simpler code.
	#define file_not_found(filename) hltypes::_file_not_found(filename, __FILE__, __LINE__)
	
	/// @brief Defines a file-not-open exception.
	class hltypesExport _file_not_open : public exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] filename Name of the file.
		/// @param[in] source_file Name of the source file.
		/// @param[in] line_number Number of the line.
		_file_not_open(chstr filename, const char* source_file, int line_number);
		~_file_not_open();
		
	};
	/// @brief Alias for simpler code.
	#define file_not_open(filename) hltypes::_file_not_open(filename, __FILE__, __LINE__)
	
	/// @brief Defines a file-not-writeable exception.
	class hltypesExport _file_not_writeable : public exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] filename Name of the file.
		/// @param[in] source_file Name of the source file.
		/// @param[in] line_number Number of the line.
		_file_not_writeable(chstr filename, const char* source_file, int line_number);
		~_file_not_writeable();
		
	};
	/// @brief Alias for simpler code.
	#define file_not_writeable(filename) hltypes::_file_not_writeable(filename, __FILE__, __LINE__)
	
	/// @brief Defines a file-long-error exception.
	class hltypesExport _file_long_error : public exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] filename Name of the file.
		/// @param[in] source_file Name of the source file.
		/// @param[in] line_number Number of the line.
		_file_long_error(chstr filename, const char* source_file, int line_number);
		~_file_long_error();
		
	};
	/// @brief Alias for simpler code.
	#define file_long_error(filename) hltypes::_file_long_error(filename, __FILE__, __LINE__)
	
	/// @brief Defines a resource-not-exists exception.
	class hltypesExport _resource_not_exists : public exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] type Type of the resource.
		/// @param[in] name Name of the resource.
		/// @param[in] container Name of the container.
		/// @param[in] source_file Name of the source file.
		/// @param[in] line_number Number of the line.
		_resource_not_exists(chstr type, chstr name, chstr container, const char* source_file, int line_number);
		~_resource_not_exists();
		
	};
	/// @brief Alias for simpler code.
	#define resource_not_exists(type, name, container) hltypes::_resource_not_exists(type, name, container, __FILE__, __LINE__)
	
	/// @brief Defines a resource-already-exists exception.
	class hltypesExport _resource_already_exists : public exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] type Type of the resource.
		/// @param[in] name Name of the resource.
		/// @param[in] container Name of the container.
		/// @param[in] source_file Name of the source file.
		/// @param[in] line_number Number of the line.
		_resource_already_exists(chstr type, chstr name, chstr container, const char* source_file, int line_number);
		~_resource_already_exists();
		
	};
	/// @brief Alias for simpler code.
	#define resource_already_exists(type, name, container) hltypes::_resource_not_exists(type, name, container, __FILE__, __LINE__)
	
	/// @brief Defines an index-error exception.
	class hltypesExport _container_index_error : public exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] index Index of the entry.
		/// @param[in] source_file Name of the source file.
		/// @param[in] line_number Number of the line.
		_container_index_error(int index, const char* source_file, int line_number);
		~_container_index_error();
		
	};
	/// @brief Alias for simpler code.
	#define container_index_error(index) hltypes::_container_index_error(index, __FILE__, __LINE__)
	
	/// @brief Defines a random-error exception.
	class hltypesExport _container_empty_error : public exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] function_name Name of the function.
		/// @param[in] source_file Name of the source file.
		/// @param[in] line_number Number of the line.
		_container_empty_error(chstr function_name, const char* source_file, int line_number);
		~_container_empty_error();
		
	};
	/// @brief Alias for simpler code.
	#define container_empty_error(function_name) hltypes::_container_empty_error(function_name, __FILE__, __LINE__)
	
	/// @brief Defines an element-error exception.
	class hltypesExport _container_element_not_found : public exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] source_file Name of the source file.
		/// @param[in] line_number Number of the line.
		_container_element_not_found(const char* source_file, int line_number);
		~_container_element_not_found();
		
	};
	/// @brief Alias for simpler code.
	#define container_element_not_found() hltypes::_container_element_not_found(__FILE__, __LINE__)
	
	/// @brief Defines a range-error exception.
	class hltypesExport _container_range_error : public exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] start Start of the range.
		/// @param[in] count Number of elements in the range.
		/// @param[in] source_file Name of the source file.
		/// @param[in] line_number Number of the line.
		_container_range_error(int start, int count, const char* source_file, int line_number);
		~_container_range_error();
		
	};
	/// @brief Alias for simpler code.
	#define container_range_error(start, count) hltypes::_container_range_error(start, count, __FILE__, __LINE__)
	
	/// @brief Defines a key-error exception.
	class hltypesExport _container_key_error : public exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] key Name of the key.
		/// @param[in] container Name of the container.
		/// @param[in] source_file Name of the source file.
		/// @param[in] line_number Number of the line.
		_container_key_error(chstr key, chstr container, const char* source_file, int line_number);
		~_container_key_error();
		
	};
	/// @brief Alias for simpler code.
	#define container_key_error(key, container) hltypes::_container_key_error(key, container, __FILE__, __LINE__)
	
}

#endif
