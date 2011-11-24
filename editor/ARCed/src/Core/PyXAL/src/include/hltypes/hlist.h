/// @file
/// @author  Boris Mikic
/// @version 1.4
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://www.opensource.org/licenses/bsd-license.php
/// 
/// @section DESCRIPTION
/// 
/// Encapsulates std::list and adds high level methods.

#ifndef HLTYPES_LIST_H
#define HLTYPES_LIST_H

#include <list>

/// @brief Provides a simpler syntax to iterate through a llist.
#define foreach_l(type, name, container) for (std::list<type>::iterator name = (container).begin(); name != (container).end(); name++)
/// @brief Provides a simpler syntax to reverse iterate through a List.
#define foreach_lr(type, name, container) for (std::list<type>::reverse_iterator name = (container).rbegin(); name != (container).rend(); name++)
/// @brief Alias for simpler code.
#define stdlist std::list<T>

namespace hltypes
{
	/// @brief Encapsulates std::list and adds high level methods.
	/// @author Boris Mikic
	template <class T> class List : public stdlist
	{
	public:
		/// @brief Empty constructor.
		List() : stdlist()
		{
		}
		/// @brief Copy constructor.
		/// @param[in] other List to copy.
		List(const List<T>& other) : stdlist(other)
		{
		}
		/// @brief Destructor.
		~List()
		{
		}
		/// @brief Returns the number of elements in the List.
		/// @return The number of elements in the List.
		int size() const
		{
			return (int)stdlist::size();
		}
		/// @brief Same as push_back.
		/// @see push_back(const T& element)
		List<T>& operator<<(const T& element)
		{
			this->push_back(element);
			return (*this);
		}
		/// @brief Same as push_back.
		/// @see push_back(const List<T>& other)
		List<T>& operator<<(const List<T>& other)
		{
			this->push_back(other);
			return (*this);
		}
		/// @brief Same as push_back.
		/// @see push_back(const T& element)
		List<T>& operator+=(const T& element)
		{
			this->push_back(element);
			return (*this);
		}
		/// @brief Same as push_back.
		/// @see push_back(const List<T>& other)
		List<T>& operator+=(const List<T>& other)
		{
			this->push_back(other);
			return (*this);
		}
		/// @brief Same as remove.
		/// @see remove(T element)
		List<T>& operator-=(T element)
		{
			this->remove(element);
			return (*this);
		}
		/// @brief Same as remove.
		/// @see remove(const List<T>& other)
		List<T>& operator-=(const List<T>& other)
		{
			this->remove(other);
			return (*this);
		}
		/// @brief Merges an List with an element.
		/// @param[in] element Element to merge with.
		/// @return New List with element added at the end of List.
		List<T> operator+(const T& element) const
		{
			List<T> result(*this);
			result += element;
			return result;
		}
		/// @brief Merges two Lists.
		/// @param[in] other Second List to merge with.
		/// @return New List with elements of second List added at the end of first List.
		List<T> operator+(const List<T>& other) const
		{
			List<T> result(*this);
			result += other;
			return result;
		}
		/// @brief Removes element from List.
		/// @param[in] element Element to remove.
		/// @return New List with elements of first List without given element.
		List<T> operator-(T element) const
		{
			List<T> result(*this);
			result -= element;
			return result;
		}
		/// @brief Removes second List from first List.
		/// @param[in] other List to remove.
		/// @return New List with elements of first List without the elements of second List.
		List<T> operator-(const List<T>& other) const
		{
			List<T> result(*this);
			result -= other;
			return result;
		}

	};
	
}

/// @brief Alias for simpler code.
#define hlist hltypes::List

#endif
