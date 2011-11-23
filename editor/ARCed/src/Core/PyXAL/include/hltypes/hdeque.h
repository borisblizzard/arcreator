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
/// Encapsulates std::deque and adds high level methods.

#ifndef HLTYPES_DEQUE_H
#define HLTYPES_DEQUE_H

#include <deque>

/// @brief Provides a simpler syntax to iterate through a ldeque.
#define foreach_q(type, name, container) for (std::deque<type>::iterator name = (container).begin(); name != (container).end(); name++)
/// @brief Provides a simpler syntax to reverse iterate through a Deque.
#define foreach_qr(type, name, container) for (std::deque<type>::reverse_iterator name = (container).rbegin(); name != (container).rend(); name++)
/// @brief Alias for simpler code.
#define stddeque std::deque<T>

namespace hltypes
{
	/// @brief Encapsulates std::deque and adds high level methods.
	/// @author Boris Mikic
	template <class T> class Deque : public stddeque
	{
	public:
		/// @brief Empty constructor.
		Deque() : stddeque()
		{
		}
		/// @brief Copy constructor.
		/// @param[in] other Deque to copy.
		Deque(const Deque<T>& other) : stddeque(other)
		{
		}
		/// @brief Destructor.
		~Deque()
		{
		}
		/// @brief Returns the number of elements in the Deque.
		/// @return The number of elements in the Deque.
		int size() const
		{
			return (int)stddeque::size();
		}
		/// @brief Same as push_back.
		/// @see push_back(const T& element)
		Deque<T>& operator<<(const T& element)
		{
			this->push_back(element);
			return (*this);
		}
		/// @brief Same as push_back.
		/// @see push_back(const Deque<T>& other)
		Deque<T>& operator<<(const Deque<T>& other)
		{
			this->push_back(other);
			return (*this);
		}
		/// @brief Same as push_back.
		/// @see push_back(const T& element)
		Deque<T>& operator+=(const T& element)
		{
			this->push_back(element);
			return (*this);
		}
		/// @brief Same as push_back.
		/// @see push_back(const Deque<T>& other)
		Deque<T>& operator+=(const Deque<T>& other)
		{
			this->push_back(other);
			return (*this);
		}
		/// @brief Same as remove.
		/// @see remove(T element)
		Deque<T>& operator-=(T element)
		{
			this->remove(element);
			return (*this);
		}
		/// @brief Same as remove.
		/// @see remove(const Deque<T>& other)
		Deque<T>& operator-=(const Deque<T>& other)
		{
			this->remove(other);
			return (*this);
		}
		/// @brief Merges an Deque with an element.
		/// @param[in] element Element to merge with.
		/// @return New Deque with element added at the end of Deque.
		Deque<T> operator+(const T& element) const
		{
			Deque<T> result(*this);
			result += element;
			return result;
		}
		/// @brief Merges two Deques.
		/// @param[in] other Second Deque to merge with.
		/// @return New Deque with elements of second Deque added at the end of first Deque.
		Deque<T> operator+(const Deque<T>& other) const
		{
			Deque<T> result(*this);
			result += other;
			return result;
		}
		/// @brief Removes element from Deque.
		/// @param[in] element Element to remove.
		/// @return New Deque with elements of first Deque without given element.
		Deque<T> operator-(T element) const
		{
			Deque<T> result(*this);
			result -= element;
			return result;
		}
		/// @brief Removes second Deque from first Deque.
		/// @param[in] other Deque to remove.
		/// @return New Deque with elements of first Deque without the elements of second Deque.
		Deque<T> operator-(const Deque<T>& other) const
		{
			Deque<T> result(*this);
			result -= other;
			return result;
		}

	};
	
}

/// @brief Alias for simpler code.
#define hdeque hltypes::Deque

#endif
