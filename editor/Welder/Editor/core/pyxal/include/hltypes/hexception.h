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
/// Provides high level exceptions.

#ifndef HLTYPES_EXCEPTION_H
#define HLTYPES_EXCEPTION_H

#include "hltypesExport.h"
#include "hstring.h"

namespace hltypes
{
	/// @brief Provides functionality of a basic exception.
	class hltypesExport _Exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] message Exception message.
		/// @param[in] sourceFile Name of the source file.
		/// @param[in] lineNumber Number of the line.
		_Exception(const String& message, const char* sourceFile, int lineNumber);
		/// @brief Destructor.
		virtual ~_Exception();
		/// @brief Gets the exception message.
		/// @return The exception message.
		inline virtual String getMessage() { return this->message; }
		/// @brief Gets the exception type.
		/// @return The exception type.
		inline virtual String getType() { return "Exception"; }

		DEPRECATED_ATTRIBUTE inline String getErrorText() { return this->message; }
		DEPRECATED_ATTRIBUTE inline String getErrorMessage() { return this->message; }
		
	protected:
		/// @brief Exception message.
		String message;
		/// @brief Sets internal message.
		/// @param[in] message Exception message.
		/// @param[in] sourceFile Name of the source file.
		/// @param[in] lineNumber Number of the line.
		/// @note Should be used only when setting the error message from within the class.
		void _setInternalMessage(const String& message, const char* sourceFile, int lineNumber);

	};
	/// @brief Alias for simpler code.
	#define Exception(message) hltypes::_Exception(message, __FILE__, __LINE__)

	/// @brief Defines a file-could-not-open exception.
	class hltypesExport _FileCouldNotOpenException : public _Exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] filename Name of the file.
		/// @param[in] sourceFile Name of the source file.
		/// @param[in] lineNumber Number of the line.
		_FileCouldNotOpenException(const String& filename, bool isResource, const char* sourceFile, int lineNumber);
		~_FileCouldNotOpenException();
		/// @brief Gets the exception type.
		/// @return The exception type.
		inline String getType() { return "FileCouldNotOpenException"; }

	};
	/// @brief Alias for simpler code.
	#define FileCouldNotOpenException(filename) hltypes::_FileCouldNotOpenException(filename, false, __FILE__, __LINE__)
	/// @brief Alias for simpler code.
	#define ResourceFileCouldNotOpenException(filename) hltypes::_FileCouldNotOpenException(filename, true, __FILE__, __LINE__)

	/// @brief Defines a file-not-open exception.
	class hltypesExport _FileNotOpenException : public _Exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] filename Name of the file.
		/// @param[in] sourceFile Name of the source file.
		/// @param[in] lineNumber Number of the line.
		_FileNotOpenException(const String& filename, const char* sourceFile, int lineNumber);
		~_FileNotOpenException();
		/// @brief Gets the exception type.
		/// @return The exception type.
		inline String getType() { return "FileNotOpenException"; }

	};
	/// @brief Alias for simpler code.
	#define FileNotOpenException(filename) hltypes::_FileNotOpenException(filename, __FILE__, __LINE__)
	
	/// @brief Defines a file-not-writeable exception.
	class hltypesExport _FileNotWriteableException : public _Exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] filename Name of the file.
		/// @param[in] sourceFile Name of the source file.
		/// @param[in] lineNumber Number of the line.
		_FileNotWriteableException(const String& filename, const char* sourceFile, int lineNumber);
		~_FileNotWriteableException();
		/// @brief Gets the exception type.
		/// @return The exception type.
		inline String getType() { return "FileNotWriteableException"; }

	};
	/// @brief Alias for simpler code.
	#define FileNotWriteableException(filename) hltypes::_FileNotWriteableException(filename, __FILE__, __LINE__)
	
	/// @brief Defines a resource-not-exists exception.
	class hltypesExport _ResourceNotExistsException : public _Exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] type Type of the resource.
		/// @param[in] name Name of the resource.
		/// @param[in] container Name of the container.
		/// @param[in] sourceFile Name of the source file.
		/// @param[in] lineNumber Number of the line.
		_ResourceNotExistsException(const String& type, const String& name, const String& container, const char* sourceFile, int lineNumber);
		~_ResourceNotExistsException();
		/// @brief Gets the exception type.
		/// @return The exception type.
		inline String getType() { return "ResourceNotExistsException"; }

	};
	/// @brief Alias for simpler code.
	#define ResourceNotExistsException(type, name, container) hltypes::_ResourceNotExistsException(type, name, container, __FILE__, __LINE__)
	
	/// @brief Defines a resource-already-exists exception.
	class hltypesExport _ResourceAlreadyExistsException : public _Exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] type Type of the resource.
		/// @param[in] name Name of the resource.
		/// @param[in] container Name of the container.
		/// @param[in] sourceFile Name of the source file.
		/// @param[in] lineNumber Number of the line.
		_ResourceAlreadyExistsException(const String& type, const String& name, const String& container, const char* sourceFile, int lineNumber);
		~_ResourceAlreadyExistsException();
		/// @brief Gets the exception type.
		/// @return The exception type.
		inline String getType() { return "ResourceAlreadyExistsException"; }

	};
	/// @brief Alias for simpler code.
	#define ResourceAlreadyExistsException(type, name, container) hltypes::_ResourceNotExistsException(type, name, container, __FILE__, __LINE__)
	
	/// @brief Defines an index-error exception.
	class hltypesExport _ContainerIndexException : public _Exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] index Index of the entry.
		/// @param[in] sourceFile Name of the source file.
		/// @param[in] lineNumber Number of the line.
		_ContainerIndexException(int index, const char* sourceFile, int lineNumber);
		~_ContainerIndexException();
		/// @brief Gets the exception type.
		/// @return The exception type.
		inline String getType() { return "ContainerIndexException"; }

	};
	/// @brief Alias for simpler code.
	#define ContainerIndexException(index) hltypes::_ContainerIndexException(index, __FILE__, __LINE__)
	
	/// @brief Defines a random-error exception.
	class hltypesExport _ContainerEmptyException : public _Exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] functionName Name of the function.
		/// @param[in] sourceFile Name of the source file.
		/// @param[in] lineNumber Number of the line.
		_ContainerEmptyException(const String& functionName, const char* sourceFile, int lineNumber);
		~_ContainerEmptyException();
		/// @brief Gets the exception type.
		/// @return The exception type.
		inline String getType() { return "ContainerEmptyException"; }

	};
	/// @brief Alias for simpler code.
	#define ContainerEmptyException(functionName) hltypes::_ContainerEmptyException(functionName, __FILE__, __LINE__)
	
	/// @brief Defines an element-error exception.
	class hltypesExport _ContainerElementNotFoundException : public _Exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] sourceFile Name of the source file.
		/// @param[in] lineNumber Number of the line.
		_ContainerElementNotFoundException(const char* sourceFile, int lineNumber);
		~_ContainerElementNotFoundException();
		/// @brief Gets the exception type.
		/// @return The exception type.
		inline String getType() { return "ContainerElementNotFoundException"; }

	};
	/// @brief Alias for simpler code.
	#define ContainerElementNotFoundException() hltypes::_ContainerElementNotFoundException(__FILE__, __LINE__)
	
	/// @brief Defines a range-error exception.
	class hltypesExport _ContainerRangeException : public _Exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] start Start of the range.
		/// @param[in] count Number of elements in the range.
		/// @param[in] sourceFile Name of the source file.
		/// @param[in] lineNumber Number of the line.
		_ContainerRangeException(int start, int count, const char* sourceFile, int lineNumber);
		~_ContainerRangeException();
		/// @brief Gets the exception type.
		/// @return The exception type.
		inline String getType() { return "ContainerRangeException"; }

	};
	/// @brief Alias for simpler code.
	#define ContainerRangeException(start, count) hltypes::_ContainerRangeException(start, count, __FILE__, __LINE__)
	
	/// @brief Defines a key-error exception.
	class hltypesExport _ContainerKeyException : public _Exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] key Name of the key.
		/// @param[in] container Name of the container.
		/// @param[in] sourceFile Name of the source file.
		/// @param[in] lineNumber Number of the line.
		_ContainerKeyException(const String& key, const String& container, const char* sourceFile, int lineNumber);
		~_ContainerKeyException();
		/// @brief Gets the exception type.
		/// @return The exception type.
		inline String getType() { return "ContainerKeyException"; }

	};
	/// @brief Alias for simpler code.
	#define ContainerKeyException(key, container) hltypes::_ContainerKeyException(key, container, __FILE__, __LINE__)

	/// @brief Defines a key-error exception.
	class hltypesExport _ObjectCannotCopyException : public _Exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] name Class name.
		/// @param[in] sourceFile Name of the source file.
		/// @param[in] lineNumber Number of the line.
		_ObjectCannotCopyException(const String& name, const char* sourceFile, int lineNumber);
		~_ObjectCannotCopyException();
		/// @brief Gets the exception type.
		/// @return The exception type.
		inline String getType() { return "ObjectCannotCopyException"; }

	};
	/// @brief Alias for simpler code.
	#define ObjectCannotCopyException(name) hltypes::_ObjectCannotCopyException(name, __FILE__, __LINE__)

	/// @brief Defines a key-error exception.
	class hltypesExport _ObjectCannotAssignException : public _Exception
	{
	public:
		/// @brief Basic constructor.
		/// @param[in] name Class name.
		/// @param[in] sourceFile Name of the source file.
		/// @param[in] lineNumber Number of the line.
		_ObjectCannotAssignException(const String& name, const char* sourceFile, int lineNumber);
		~_ObjectCannotAssignException();
		/// @brief Gets the exception type.
		/// @return The exception type.
		inline String getType() { return "ObjectCannotAssignException"; }

	};
	/// @brief Alias for simpler code.
	#define ObjectCannotAssignException(name) hltypes::_ObjectCannotAssignException(name, __FILE__, __LINE__)

}

typedef hltypes::_Exception hexception;

#endif
