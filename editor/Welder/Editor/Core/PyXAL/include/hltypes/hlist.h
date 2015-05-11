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
/// Encapsulates std::list and adds high level methods.

#ifndef HLTYPES_LIST_H
#define HLTYPES_LIST_H

#include <algorithm>
#include <list>

#include "exception.h"
#include "hltypesUtil.h"
#include "hplatform.h"
#include "hstring.h"

/// @brief Provides a simpler syntax to iterate through a list.
#define foreach_l(type, name, container) for (std::list< type >::iterator name = (container).begin(); name != (container).end(); ++name)
#define foreachc_l(type, name, container) for (std::list< type >::const_iterator name = (container).begin(); name != (container).end(); ++name)
/// @brief Provides a simpler syntax to reverse iterate through a list.
#define foreach_lr(type, name, container) for (std::list< type >::reverse_iterator name = (container).rbegin(); name != (container).rend(); ++name)
#define foreachc_lr(type, name, container) for (std::list< type >::reverse_const_iterator name = (container).rbegin(); name != (container).rend(); ++name)
/// @brief Alias for simpler code.
#define stdlist std::list<T>

namespace hltypes
{
	/// @brief Encapsulates std::list and adds high level methods.
	template <class T>
	class List : public stdlist
	{
	private:
		typedef typename stdlist::iterator iterator_t;
		typedef typename stdlist::const_iterator const_iterator_t;
	public:
		/// @brief Empty constructor.
		inline List() : stdlist()
		{
		}
		/// @brief Copy constructor.
		/// @param[in] other List to copy.
		inline List(const List<T>& other) : stdlist(other)
		{
		}
		/// @brief Destructor.
		inline ~List()
		{
		}
		/// @brief Returns element at specified position.
		/// @param[in] index Index of the element.
		/// @return Element at specified position.
		/// @note Does not work with bool as T, use List::at directly instead.
		inline T& operator[](const int index)
		{
			if (index < 0)
			{
				return (*this->_iterator_plus(stdlist::begin(), this->size() + index));
			}
			return (*this->_iterator_plus(stdlist::begin(), index));
		}
		/// @brief Returns element at specified position.
		/// @param[in] index Index of the element.
		/// @return Element at specified position.
		/// @note Does not work with bool as T, use List::at directly instead.
		inline const T& operator[](const int index) const
		{
			if (index < 0)
			{
				return (*this->_const_iterator_plus(stdlist::begin(), this->size() + index));
			}
			return (*this->_const_iterator_plus(stdlist::begin(), index));
		}
		/// @brief Returns a sublist.
		/// @param[in] start Start index of the elements to copy.
		/// @param[in] count Number of elements to copy.
		/// @return Sublist created from the current List.
		inline List<T> operator()(const int start, const int count) const
		{
			List<T> result;
			if (count > 0)
			{
				if (start >= this->size() || start + count > this->size())
				{
					throw container_range_error(start, count);
				}
				const_iterator_t it = this->_const_iterator_plus(stdlist::begin(), start);
				result.assign(it, this->_const_iterator_plus(it, count));
			}
			return result;
		}
		/// @brief Same as equals.
		/// @see equals
		inline bool operator==(const List<T>& other) const
		{
			return this->equals(other);
		}
		/// @brief Same as nequals.
		/// @see nequals
		inline bool operator!=(const List<T>& other) const
		{
			return this->nequals(other);
		}
		/// @brief Returns the number of elements in the List.
		/// @return The number of elements in the List.
		inline int size() const
		{
			return (int)stdlist::size();
		}
		/// @brief Compares the contents of two Lists for being equal.
		/// @param[in] other Another List.
		/// @return True if number of elements are equal and all pairs of elements at the same positions are equal.
		inline bool equals(const List<T>& other) const
		{
			if (this->size() != other.size())
			{
				return false;
			}
			for_iter (i, 0, this->size())
			{
				// making sure operator== is used, not !=
				if (!(stdlist::at(i) == other.at(i)))
				{
					return false;
				}
			}
			return true;
		}
		/// @brief Compares the contents of two Lists for being not equal.
		/// @param[in] other Another List.
		/// @return True if number of elements are not equal or at least one pair of elements at the same positions is not equal.
		inline bool nequals(const List<T>& other) const
		{
			if (this->size() != other.size())
			{
				return true;
			}
			for_iter (i, 0, this->size())
			{
				// making sure operator!= is used, not ==
				if (stdlist::at(i) != other.at(i))
				{
					return true;
				}
			}
			return false;
		}
		/// @brief Gets index of the given element.
		/// @param[in] element Element to search for.
		/// @return Index of the given element or -1 if element could not be found.
		inline int index_of(T element) const
		{
			const_iterator_t it = stdlist::begin();
			for_iter (i, 0, this->size())
			{
				if (element == (*it))
				{
					return i;
				}
				++it;
			}
			return -1;
		}
		/// @brief Gets all indexes of the given element.
		/// @param[in] element Element to search for.
		/// @return Index of the given element or -1 if element could not be found.
		inline List<int> indexes_of(T element) const
		{
			List<int> result;
			const_iterator_t it = stdlist::begin();
			for_iter (i, 0, this->size())
			{
				if (element == (*it))
				{
					result.push_back(i);
				}
				++it;
			}
			return result;
		}
		/// @brief Checks existence of element in List.
		/// @param[in] element Element to search for.
		/// @return True if element is in List.
		inline bool contains(const T& element) const
		{
			return (this->index_of(element) >= 0);
		}
		/// @brief Checks existence of elements in List.
		/// @param[in] other List with elements to search for.
		/// @return True if all elements are in List.
		inline bool contains(const List<T>& other) const
		{
			int index;
			for_iter (i, 0, other.size())
			{
				index = this->index_of(other.at(i));
				if (index < 0)
				{
					return false;
				}
			}
			return true;
		}
		/// @brief Checks existence of elements in List.
		/// @param[in] other C-type array with elements to search for.
		/// @param[in] count How many elements the C-type array has.
		/// @return True if all elements are in List.
		inline bool contains(const T other[], int count) const
		{
			int index;
			for_iter (i, 0, count)
			{
				index = this->index_of(other[i]);
				if (index < 0)
				{
					return false;
				}
			}
			return true;
		}
		/// @brief Counts occurrences of element in List.
		/// @param[in] element Element to search for.
		/// @return Number of occurrences of given element.
		inline int count(T element) const
		{
			int result = 0;
			for_iter (i, 0, this->size())
			{
				if (element == stdlist::at(i))
				{
					++result;
				}
			}
			return result;
		}
		/// @brief Inserts new element at specified position n times.
		/// @param[in] index Position where to insert the new element.
		/// @param[in] element Element to insert.
		/// @param[in] times Number of times to insert element.
		inline void insert_at(const int index, const T& element, const int times = 1)
		{
			if (index > this->size())
			{
				throw container_index_error(index);
			}
			stdlist::insert(this->_iterator_plus(stdlist::begin(), index), times, element);
		}
		/// @brief Inserts all elements of another List into this one.
		/// @param[in] index Position where to insert the new elements.
		/// @param[in] other List of elements to insert.
		inline void insert_at(const int index, const List<T>& other)
		{
			if (index > this->size())
			{
				throw container_index_error(index);
			}
			stdlist::insert(this->_iterator_plus(stdlist::begin(), index), other.begin(), other.end());
		}
		/// @brief Inserts all elements of another List into this one.
		/// @param[in] index Position where to insert the new elements.
		/// @param[in] other List of elements to insert.
		/// @param[in] count Number of elements to insert.
		inline void insert_at(const int index, const List<T>& other, const int count)
		{
			if (index > this->size())
			{
				throw container_index_error(index);
			}
			if (count > other.size())
			{
				throw container_range_error(0, count);
			}
			const_iterator_t it = other.begin();
			stdlist::insert(this->_iterator_plus(stdlist::begin(), index), it, this->_const_iterator_plus(it, count));
		}
		/// @brief Inserts all elements of another List into this one.
		/// @param[in] index Position where to insert the new elements.
		/// @param[in] other List of elements to insert.
		/// @param[in] start Start index of the elements to insert.
		/// @param[in] count Number of elements to insert.
		inline void insert_at(const int index, const List<T>& other, const int start, const int count)
		{
			if (index > this->size())
			{
				throw container_index_error(index);
			}
			if (start >= other.size() || start + count > other.size())
			{
				throw container_range_error(start, count);
			}
			const_iterator_t it = this->_const_iterator_plus(other.begin(), start);
			stdlist::insert(this->_iterator_plus(stdlist::begin(), index), it, this->_const_iterator_plus(it, count));
		}
		/// @brief Inserts all elements of a C-type array into this List.
		/// @param[in] index Position where to insert the new elements.
		/// @param[in] other C-type array of elements to insert.
		/// @param[in] count Number of elements to insert.
		inline void insert_at(const int index, const T other[], const int count)
		{
			stdlist::insert(this->_iterator_plus(stdlist::begin(), index), other, other + count);
		}
		/// @brief Inserts all elements of a C-type array into this List.
		/// @param[in] index Position where to insert the new elements.
		/// @param[in] other C-type array of elements to insert.
		/// @param[in] start Start index of the elements to insert.
		/// @param[in] count Number of elements to insert.
		inline void insert_at(const int index, const T other[], const int start, const int count)
		{
			stdlist::insert(this->_iterator_plus(stdlist::begin(), index), other + start, other + (start + count));
		}
		/// @brief Removes element at given index.
		/// @param[in] index Index of element to remove.
		/// @return The removed element.
		inline T remove_at(const int index)
		{
			if (index >= this->size())
			{
				throw container_index_error(index);
			}
			T result = stdlist::at(index);
			stdlist::erase(stdlist::begin() + index);
			return result;
		}
		/// @brief Removes n elements at given index of List.
		/// @param[in] index Start index of elements to remove.
		/// @param[in] count Number of elements to remove.
		/// @return List of all removed elements.
		/// @note Elements in the returned List are in the same order as in the orignal List.
		inline List<T> remove_at(const int index, const int count)
		{
			if (index >= this->size() || index + count > this->size())
			{
				throw container_range_error(index, count);
			}
			List<T> result;
			iterator_t it = stdlist::begin();
			iterator_t begin = it + index;
			iterator_t end = it + (index + count);
			result.assign(begin, end);
			stdlist::erase(begin, end);
			return result;
		}
		/// @brief Removes first occurrence of element in List.
		/// @param[in] element Element to remove.
		inline void remove(T element)
		{
			int index = this->index_of(element);
			if (index < 0)
			{
				throw container_element_not_found();
			}
			stdlist::erase(_iterator_plus(stdlist::begin(), index));
		}
		/// @brief Removes first occurrence of each element in another List from this one.
		/// @param[in] other List of elements to remove.
		inline void remove(const List<T>& other)
		{
			int index;
			for_iter (i, 0, other.size())
			{
				index = this->index_of(other.at(i));
				if (index < 0)
				{
					throw container_element_not_found();
				}
				stdlist::erase(stdlist::begin() + index);
			}
		}
		/// @brief Removes all occurrences of element in List.
		/// @param[in] element Element to remove.
		/// @return Number of elements removed.
		inline int remove_all(const T& element)
		{
			List<int> indexes = this->indexes_of(element);
			iterator_t it = stdlist::begin();
			for_iter_r (i, indexes.size(), 0)
			{
				stdlist::erase(it + indexes[i]);
			}
			return indexes.size();
		}
		/// @brief Removes all occurrences of each element in another List from this one.
		/// @param[in] other List of elements to remove.
		/// @return Number of elements removed.
		inline int remove_all(const List<T>& other)
		{
			List<int> indexes;
			iterator_t it;
			int count = 0;
			for_iter (i, 0, other.size())
			{
				List<int> indexes = this->indexes_of(other.at(i));
				iterator_t it = stdlist::begin();
				for_iter_r (j, indexes.size(), 0)
				{
					stdlist::erase(it + indexes[j]);
				}
				count += indexes.size();
			}
			return count;
		}
		/// @brief Adds element at the end of List.
		/// @param[in] element Element to add.
		inline void push_back(const T& element)
		{
			stdlist::push_back(element);
		}
		/// @brief Adds element at the end of List n times.
		/// @param[in] element Element to add.
		/// @param[in] times Number of times to add the element.
		inline void push_back(const T& element, int times)
		{
			this->insert_at(this->size(), element, times);
		}
		/// @brief Adds all elements from another List at the end of this one.
		/// @param[in] other List of elements to add.
		inline void push_back(const List<T>& other)
		{
			this->insert_at(this->size(), other);
		}
		/// @brief Adds all elements from another List at the end of this one.
		/// @param[in] other List of elements to add.
		/// @param[in] count Number of elements to add.
		inline void push_back(const List<T>& other, const int count)
		{
			this->insert_at(this->size(), other, count);
		}
		/// @brief Adds all elements from another List at the end of this one.
		/// @param[in] other List of elements to add.
		/// @param[in] start Start index of the elements to add.
		/// @param[in] count Number of elements to add.
		inline void push_back(const List<T>& other, const int start, const int count)
		{
			this->insert_at(this->size(), other, start, count);
		}
		/// @brief Adds all elements from a C-type array at the end of List.
		/// @param[in] other C-type array of elements to add.
		/// @param[in] count Number of elements to add.
		inline void push_back(const T other[], const int count)
		{
			this->insert_at(this->size(), other, count);
		}
		/// @brief Adds all elements from a C-type array at the end of List.
		/// @param[in] other C-type array of elements to add.
		/// @param[in] start Start index of the elements to add.
		/// @param[in] count Number of elements to add.
		inline void push_back(const T other[], const int start, const int count)
		{
			this->insert_at(this->size(), other, start, count);
		}
		/// @brief Adds element at the beginning of List n times.
		/// @param[in] element Element to add.
		/// @param[in] times Number of times to add the element.
		inline void push_front(const T& element, int times = 1)
		{
			this->insert_at(0, element, times);
		}
		/// @brief Adds all elements from another List at the beginning of this one.
		/// @param[in] other List of elements to add.
		inline void push_front(const List<T>& other)
		{
			this->insert_at(0, other);
		}
		/// @brief Adds all elements from another List at the beginning of this one.
		/// @param[in] other List of elements to add.
		/// @param[in] count Number of elements to add.
		inline void push_front(const List<T>& other, const int count)
		{
			this->insert_at(0, other, count);
		}
		/// @brief Adds all elements from another List at the beginning of this one.
		/// @param[in] other List of elements to add.
		/// @param[in] start Start index of the elements to add.
		/// @param[in] count Number of elements to add.
		inline void push_front(const List<T>& other, const int start, const int count)
		{
			this->insert_at(0, other, start, count);
		}
		/// @brief Adds all elements from a C-type array at the beginning of List.
		/// @param[in] other C-type array of elements to add.
		/// @param[in] count Number of elements to add.
		inline void push_front(const T other[], const int count)
		{
			this->insert_at(0, other, count);
		}
		/// @brief Adds all elements from a C-type array at the beginning of List.
		/// @param[in] other C-type array of elements to add.
		/// @param[in] start Start index of the elements to add.
		/// @param[in] count Number of elements to add.
		inline void push_front(const T other[], const int start, const int count)
		{
			this->insert_at(0, other, start, count);
		}
		/// @brief Removes first element of List.
		/// @return The removed element.
		inline T pop_front()
		{
			if (this->size() == 0)
			{
				throw container_index_error(0);
			}
			return this->remove_at(0);
		}
		/// @brief Removes n elements from the beginning of List.
		/// @param[in] count Number of elements to remove.
		/// @return List of all removed elements.
		/// @note Elements in the returned List are in the same order as in the orignal List.
		inline List<T> pop_front(const int count)
		{
			if (count > this->size())
			{
				throw container_range_error(0, count);
			}
			List<T> result;
			iterator_t begin = stdlist::begin();
			iterator_t end = begin + count;
			result.assign(begin, end);
			stdlist::erase(begin, end);
			return result;
		}
		/// @brief Removes last element of List.
		/// @return The removed element.
		inline T pop_back()
		{
			if (this->size() == 0)
			{
				throw container_index_error(0);
			}
			T element = stdlist::back();
			stdlist::pop_back();
			return element;
		}
		/// @brief Removes n elements from the end of List.
		/// @param[in] count Number of elements to remove.
		/// @return List of all removed elements.
		/// @note Elements in the returned List are in the same order as in the orignal List.
		inline List<T> pop_back(const int count)
		{
			if (count > this->size())
			{
				throw container_range_error(0, count);
			}
			List<T> result;
			iterator_t end = stdlist::end();
			iterator_t begin = end - count;
			result.assign(begin, end);
			stdlist::erase(begin, end);
			return result;
		}
		/// @brief Unites elements of this List with an element.
		/// @param[in] element Element to unite with.
		inline void unite(const T& element)
		{
			this->insert_at(this->size(), element);
			this->remove_duplicates();
		}
		/// @brief Unites elements of this List with another one.
		/// @param[in] other List to unite with.
		inline void unite(const List<T>& other)
		{
			this->insert_at(this->size(), other);
			this->remove_duplicates();
		}
		/// @brief Creates a new List as union of this List with an element.
		/// @param[in] element Element to unite with.
		/// @return A new List.
		inline List<T> united(const T& element) const
		{
			List<T> result(*this);
			result.unite(element);
			return result;
		}
		/// @brief Creates a new List as union of this List with another one.
		/// @param[in] other List to unite with.
		/// @return A new List.
		inline List<T> united(const List<T>& other) const
		{
			List<T> result(*this);
			result.unite(other);
			return result;
		}
		/// @brief Intersects elements of this List with another one.
		/// @param[in] other List to intersect with.
		inline void intersect(const List<T>& other)
		{
			List<T> result;
			for_iter (i, 0, this->size())
			{
				if (other.contains(stdlist::at(i)))
				{
					result.push_back(stdlist::at(i));
				}
			}
			stdlist::assign(result.begin(), result.end());
		}
		/// @brief Creates a new List as intersection of this List with another one.
		/// @param[in] other List to intersect with.
		/// @return A new List.
		inline List<T> intersected(const List<T>& other) const
		{
			List<T> result(*this);
			result.intersect(other);
			return result;
		}
		/// @brief Differentiates elements of this List with an element.
		/// @param[in] other Element to differentiate with.
		/// @note Unlike remove, this method ignores if the element is not in this List.
		inline void differentiate(const T& element)
		{
			int index = 0;
			while (true)
			{
				index = this->index_of(element);
				if (index < 0)
				{
					break;
				}
				stdlist::erase(stdlist::begin() + index);
			}
		}
		/// @brief Differentiates elements of this List with another one.
		/// @param[in] other List to differentiate with.
		/// @note Unlike remove, this method ignore elements of other List that are not in this one.
		inline void differentiate(const List<T>& other)
		{
			int index;
			for_iter (i, 0, other.size())
			{
				while (true)
				{
					index = this->index_of(other.at(i));
					if (index < 0)
					{
						break;
					}
					stdlist::erase(stdlist::begin() + index);
				}
			}
		}
		/// @brief Creates a new List as difference of this List with an element.
		/// @param[in] other Element to differentiate with.
		/// @return A new List.
		/// @note Unlike remove, this method ignores if the element is not in this List.
		inline List<T> differentiated(const T& element) const
		{
			List<T> result(*this);
			result.differentiate(element);
			return result;
		}
		/// @brief Creates a new List as difference of this List with another one.
		/// @param[in] other List to differentiate with.
		/// @return A new List.
		/// @note Unlike remove, this method ignore elements of other List that are not in this one.
		inline List<T> differentiated(const List<T>& other) const
		{
			List<T> result(*this);
			result.differentiate(other);
			return result;
		}
		/// @brief Reverses order of elements.
		inline void reverse()
		{
			if (this->size() > 0)
			{
				std::reverse(stdlist::begin(), stdlist::end());
			}
		}
		/// @brief Creates new List with reversed order of elements.
		/// @return A new List.
		inline List<T> reversed() const
		{
			List<T> result(*this);
			result.reverse();
			return result;
		}
		/// @brief Removes duplicates in List.
		inline void remove_duplicates()
		{
			List<int> indexes;
			iterator_t it = stdlist::begin();
			for_iter (i, 0, this->size())
			{
				indexes = this->indexes_of(stdlist::at(i));
				for_iter_r (j, indexes.size(), 1)
				{
					stdlist::erase(it + indexes[j]);
				}
			}
		}
		/// @brief Creates new List without duplicates.
		/// @return A new List.
		inline List<T> removed_duplicates() const
		{
			List<T> result(*this);
			result.remove_duplicates();
			return result;
		}
		/// @brief Sorts elements in List.
		/// @note The sorting order is ascending.
		inline void sort()
		{
			if (this->size() > 0)
			{
				std::stable_sort(stdlist::begin(), stdlist::end());
			}
		}
		/// @brief Sorts elements in List.
		/// @param[in] compare_function Function pointer with comparison function that takes two elements of type T and returns bool.
		/// @note The sorting order is ascending.
		/// @note compare_function should return true if first element is less than the second element.
		inline void sort(bool (*compare_function)(T, T))
		{
			if (this->size() > 0)
			{
				std::stable_sort(stdlist::begin(), stdlist::end(), compare_function);
			}
		}
		/// @brief Creates new sorted List.
		/// @return A new List.
		/// @note The sorting order is ascending.
		inline List<T> sorted() const
		{
			List<T> result(*this);
			result.sort();
			return result;
		}
		/// @brief Creates new sorted List.
		/// @param[in] compare_function Function pointer with comparison function that takes two elements of type T and returns bool.
		/// @return A new List.
		/// @note The sorting order is ascending.
		/// @note compare_function should return true if first element is less than the second element.
		inline List<T> sorted(bool (*compare_function)(T, T)) const
		{
			List<T> result(*this);
			result.sort(compare_function);
			return result;
		}
		/// @brief Randomizes order of elements in List.
		inline void randomize()
		{
			std::random_shuffle(stdlist::begin(), stdlist::end());
		}
		/// @brief Creates a new List with randomized order of elements.
		/// @return A new List.
		inline List<T> randomized() const
		{
			List<T> result(*this);
			result.randomize();
			return result;
		}
		/// @brief Finds minimum element in List.
		/// @return Minimum Element.
		inline T min() const
		{
			if (this->size() == 0)
			{
				throw container_empty_error("min()");
			}
			return (*std::min_element(stdlist::begin(), stdlist::end()));
		}
		/// @brief Finds minimum element in List.
		/// @param[in] compare_function Function pointer with comparison function that takes two elements of type T and returns bool.
		/// @return Minimum Element.
		/// @note compare_function should return true if first element is less than second element.
		inline T min(bool (*compare_function)(T, T)) const
		{
			if (this->size() == 0)
			{
				throw container_empty_error("min()");
			}
			return (*std::min_element(stdlist::begin(), stdlist::end(), compare_function));
		}
		/// @brief Finds maximum element in List.
		/// @return Maximum Element.
		inline T max() const
		{
			if (this->size() == 0)
			{
				throw container_empty_error("max()");
			}
			return (*std::max_element(stdlist::begin(), stdlist::end()));
		}
		/// @brief Finds maximum element in List.
		/// @param[in] compare_function Function pointer with comparison function that takes two elements of type T and returns bool.
		/// @return Maximum Element.
		/// @note compare_function should return true if first element is greater than second element.
		inline T max(bool (*compare_function)(T, T)) const
		{
			if (this->size() == 0)
			{
				throw container_empty_error("max()");
			}
			return (*std::max_element(stdlist::begin(), stdlist::end(), compare_function));
		}
		/// @brief Gets a random element in List.
		/// @return Random element.
		inline T random() const
		{
			if (this->size() == 0)
			{
				throw container_empty_error("random()");
			}
			return stdlist::at(hrand(this->size()));
		}
		/// @brief Gets a List of random elements selected from this one.
		/// @param[in] count Number of random elements.
		/// @param[in] unique Whether to force all random values to be unique.
		/// @return List of random elements selected from this one.
		inline List<T> random(int count, bool unique = false) const
		{
			List<T> result;
			if (!unique)
			{
				for_iter (i, 0, count)
				{
					result.push_back(stdlist::at(hrand(this->size())));
				}
			}
			else if (count > 0)
			{
				if (count > this->size())
				{
					throw container_range_error(0, count);
				}
				if (count == this->size())
				{
					return this->randomized();
				}
				List<int> indexes;
				for_iter (i, 0, this->size())
				{
					indexes.push_back(i);
				}
				for_iter (i, 0, count)
				{
					result.push_back(stdlist::at(indexes.remove_at(hrand(indexes.size()))));
				}
			}
			return result;
		}
		/// @brief Gets a random element in List and removes it.
		/// @return Random element.
		inline T pop_random()
		{
			if (this->size() == 0)
			{
				throw container_empty_error("pop_random()");
			}
			T result = stdlist::at(hrand(this->size()));
			this->remove(result);
			return result;
		}
		/// @brief Gets a List of random elements selected from this one and removes them.
		/// @param[in] count Number of random elements.
		/// @param[in] unique Whether to force all random values to be unique.
		/// @return List of random elements selected from this one.
		inline List<T> pop_random(int count, bool unique = false)
		{
			List<T> result;
			if (!unique)
			{
				for_iter (i, 0, count)
				{
					result.push_back(stdlist::at(hrand(this->size())));
				}
			}
			else if (count > 0)
			{
				if (count > this->size())
				{
					throw container_range_error(0, count);
				}
				if (count == this->size())
				{
					return this->randomized();
				}
				List<int> indexes;
				for_iter (i, 0, this->size())
				{
					indexes.push_back(i);
				}
				for_iter (i, 0, count)
				{
					result.push_back(stdlist::at(indexes.remove_at(hrand(indexes.size()))));
				}
			}
			this->remove(result);
			return result;
		}
		/// @brief Joins all elements into a string.
		/// @param[in] separator Separator string between elements.
		/// @return String or joined elements separater by separator string.
		/// @note Make sure your elements can be cast into String or are already String.
		inline String join(const String& separator) const
		{
			String result;
			if (this->size() > 0)
			{
				result += String(stdlist::at(0));
				for_iter (i, 1, this->size())
				{
					result += separator + String(stdlist::at(i));
				}
			}
			return result;
		}
		/// @brief Finds and returns new List of elements that match the condition.
		/// @param[in] condition_function Function pointer with condition function that takes one element of type T and returns bool.
		/// @return New List with all matching elements.
		inline List<T> find_all(bool (*condition_function)(T))
		{
			List<T> result;
			for_iter (i, 0, this->size())
			{
				if (condition_function(stdlist::at(i)))
				{
					result.push_back(stdlist::at(i));
				}
			}
			return result;
		}
		/// @brief Finds and returns first occurrence of element that matches the condition.
		/// @param[in] condition_function Function pointer with condition function that takes one element of type T and returns bool.
		/// @return Pointer to element that matches the condition or NULL if no element was found.
		inline T* find_first(bool (*condition_function)(T))
		{
			for_iter (i, 0, this->size())
			{
				if (condition_function(stdlist::at(i)))
				{
					return &stdlist::at(i);
				}
			}
			return NULL;
		}
		/// @brief Checks if at least one element matches the condition.
		/// @param[in] condition_function Function pointer with condition function that takes one element of type T and returns bool.
		/// @return True if at least one element matches the condition.
		inline bool matches_any(bool (*condition_function)(T))
		{
			for_iter (i, 0, this->size())
			{
				if (condition_function(stdlist::at(i)))
				{
					return true;
				}
			}
			return false;
		}
		/// @brief Checks if all elements match the condition.
		/// @param[in] condition_function Function pointer with condition function that takes one element of type T and returns bool.
		/// @return True if all elements match the condition.
		inline bool matches_all(bool (*condition_function)(T))
		{
			for_iter (i, 0, this->size())
			{
				if (!condition_function(stdlist::at(i)))
				{
					return false;
				}
			}
			return true;
		}
		/// @brief Returns a new List with all elements cast into type S.
		/// @return A new List with all elements cast into type S.
		/// @note Make sure all elements in the List can be cast into type S.
		template <class S>
		inline List<S> cast()
		{
			List<S> result;
			for_iter (i, 0, this->size())
			{
				result.push_back((S)stdlist::at(i));
			}
			return result;
		}
		/// @brief Returns a new List with all elements dynamically cast into type S.
		/// @param[in] include_nulls Whether to include NULLs that failed to cast.
		/// @return A new List with all elements cast into type S.
		/// @note Be careful not to use this function with non-pointers and classes that don't have virtual functions.
		template <class S>
		inline List<S> dyn_cast(bool include_nulls = false)
		{
			List<S> result;
			S value;
			for_iter (i, 0, this->size())
			{
				// when seeing "dynamic_cast", I always think of fireballs
				value = dynamic_cast<S>(stdlist::at(i));
				if (value != NULL || include_nulls)
				{
					result.push_back(value);
				}
			}
			return result;
		}
		/// @brief Accesses first element of List.
		/// @return The first element.
		inline T& first()
		{
			return stdlist::front();
		}
		/// @brief Accesses last element of List.
		/// @return The last element.
		inline T& last()
		{
			return stdlist::back();
		}
		/// @brief Same as contains.
		/// @see contains(const T& element)
		inline bool includes(const T& element) const
		{
			return this->contains(element);
		}
		/// @brief Same as contains.
		/// @see contains(const List<T>& other)
		inline bool includes(const List<T>& other) const
		{
			return this->contains(other);
		}
		/// @brief Same as contains.
		/// @see contains(const T other[], int count)
		inline bool includes(const T other[], int count) const
		{
			return this->contains(other, count);
		}
		/// @brief Same as contains.
		/// @see contains(const T& element)
		inline bool has(const T& element) const
		{
			return this->contains(element);
		}
		/// @brief Same as contains.
		/// @see contains(const List<T>& other)
		inline bool has(const List<T>& other) const
		{
			return this->contains(other);
		}
		/// @brief Same as contains.
		/// @see contains(const T other[], int count)
		inline bool has(const T other[], int count) const
		{
			return this->contains(other, count);
		}
		/// @brief Same as contains.
		/// @see contains(const T& element)
		inline bool has_element(const T& element) const
		{
			return this->contains(element);
		}
		/// @brief Same as contains.
		/// @see contains(const List<T>& other)
		inline bool has_element(const List<T>& other) const
		{
			return this->contains(other);
		}
		/// @brief Same as contains.
		/// @see contains(const T other[], int count)
		inline bool has_element(const T other[], int count) const
		{
			return this->contains(other, count);
		}
		/// @brief Same as push_back.
		/// @see push_back(const T& element)
		inline void add(const T& element)
		{
			this->push_back(element);
		}
		/// @brief Same as push_back.
		/// @see push_back(const T& element, int times)
		inline void add(const T& element, int times)
		{
			this->push_back(element, times);
		}
		/// @brief Same as push_back.
		/// @see push_back(const List<T>& other)
		inline void add(const List<T>& other)
		{
			this->push_back(other);
		}
		/// @brief Same as push_back.
		/// @see push_back(const List<T>& other, const int count)
		inline void add(const List<T>& other, const int count)
		{
			this->push_back(other, count);
		}
		/// @brief Same as push_back.
		/// @see push_back(const List<T>& other, const int start, const int count)
		inline void add(const List<T>& other, const int start, const int count)
		{
			this->push_back(other, start, count);
		}
		/// @brief Same as push_back.
		/// @see push_back(const T other[], const int count)
		inline void add(const T other[], const int count)
		{
			this->push_back(other, count);
		}
		/// @brief Same as push_back.
		/// @see push_back(const T other[], const int start, const int count)
		inline void add(const T other[], const int start, const int count)
		{
			this->push_back(other, start, count);
		}
		/// @brief Same as push_back.
		/// @see push_back(const T& element)
		inline void append(const T& element)
		{
			this->push_back(element);
		}
		/// @brief Same as push_back.
		/// @see push_back(const T& element, int times)
		inline void append(const T& element, int times)
		{
			this->push_back(element, times);
		}
		/// @brief Same as push_back.
		/// @see push_back(const List<T>& other)
		inline void append(const List<T>& other)
		{
			this->push_back(other);
		}
		/// @brief Same as push_back.
		/// @see push_back(const List<T>& other, const int count)
		inline void append(const List<T>& other, const int count)
		{
			this->push_back(other, count);
		}
		/// @brief Same as push_back.
		/// @see push_back(const List<T>& other, const int start, const int count)
		inline void append(const List<T>& other, const int start, const int count)
		{
			this->push_back(other, start, count);
		}
		/// @brief Same as push_back.
		/// @see push_back(const T other[], const int count)
		inline void append(const T other[], const int count)
		{
			this->push_back(other, count);
		}
		/// @brief Same as push_back.
		/// @see push_back(const T other[], const int start, const int count)
		inline void append(const T other[], const int start, const int count)
		{
			this->push_back(other, start, count);
		}
		/// @brief Same as push_back.
		/// @see push_back(const T& element).
		inline void push_last(const T& element)
		{
			this->push_back(element);
		}
		/// @brief Same as push_back.
		/// @see push_back(const T& element, int times).
		inline void push_last(const T& element, int times)
		{
			this->push_back(element, times);
		}
		/// @brief Same as push_back.
		/// @see push_back(const List<T>& other).
		inline void push_last(const List<T>& other)
		{
			this->push_back(other);
		}
		/// @brief Same as push_back.
		/// @see push_back(const List<T>& other, const int count).
		inline void push_last(const List<T>& other, const int count)
		{
			this->push_back(other, count);
		}
		/// @brief Same as push_back.
		/// @see push_back(const List<T>& other, const int start, const int count).
		inline void push_last(const List<T>& other, const int start, const int count)
		{
			this->push_back(other, start, count);
		}
		/// @brief Same as push_back.
		/// @see push_back(const T other[], const int count).
		inline void push_last(const T other[], const int count)
		{
			this->push_back(other, count);
		}
		/// @brief Same as push_back.
		/// @see push_back(const T other[], const int start, const int count).
		inline void push_last(const T other[], const int start, const int count)
		{
			this->push_back(other, start, count);
		}
		/// @brief Same as push_front.
		/// @see push_front(const T& element, int times).
		inline void push_first(const T& element, int times = 1)
		{
			this->push_front(element, times);
		}
		/// @brief Same as push_front.
		/// @see push_front(const List<T>& other).
		inline void push_first(const List<T>& other)
		{
			this->push_front(other);
		}
		/// @brief Same as push_front.
		/// @see push_front(const List<T>& other, const int count).
		inline void push_first(const List<T>& other, const int count)
		{
			this->push_front(other, count);
		}
		/// @brief Same as push_front.
		/// @see push_front(const List<T>& other, const int start, const int count).
		inline void push_first(const List<T>& other, const int start, const int count)
		{
			this->push_front(other, start, count);
		}
		/// @brief Same as push_front.
		/// @see push_front(const T other[], const int count).
		inline void push_first(const T other[], const int count)
		{
			this->push_front(other, count);
		}
		/// @brief Same as push_front.
		/// @see push_front(const T other[], const int start, const int count).
		inline void push_first(const T other[], const int start, const int count)
		{
			this->push_front(other, start, count);
		}
		/// @brief Same as pop_front.
		/// @see pop_front().
		inline T pop_first()
		{
			return this->pop_front();
		}
		/// @brief Same as pop_front.
		/// @see pop_front(const int count).
		inline List<T> pop_first(const int count)
		{
			return this->pop_front(count);
		}
		/// @brief Same as pop_back.
		/// @see pop_back().
		inline T pop_last()
		{
			return this->pop_back();
		}
		/// @brief Same as pop_back.
		/// @see pop_back(const int count).
		inline List<T> pop_last(const int count)
		{
			return this->pop_back(count);
		}
		/// @brief Same as pop_front.
		/// @see pop_front().
		inline T remove_front()
		{
			return this->pop_front();
		}
		/// @brief Same as pop_front.
		/// @see pop_front(const int count).
		inline List<T> remove_front(const int count)
		{
			return this->pop_front(count);
		}
		/// @brief Same as pop_back.
		/// @see pop_back().
		inline T remove_back()
		{
			return this->pop_back();
		}
		/// @brief Same as pop_back.
		/// @see pop_back(const int count).
		inline List<T> remove_back(const int count)
		{
			return this->pop_back(count);
		}
		/// @brief Same as pop_front.
		/// @see pop_front().
		inline T remove_first()
		{
			return this->pop_front();
		}
		/// @brief Same as pop_front.
		/// @see pop_front(const int count).
		inline List<T> remove_first(const int count)
		{
			return this->pop_front(count);
		}
		/// @brief Same as pop_back.
		/// @see pop_back().
		inline T remove_last()
		{
			return this->pop_back();
		}
		/// @brief Same as pop_back.
		/// @see pop_back(const int count).
		inline List<T> remove_last(const int count)
		{
			return this->pop_back(count);
		}
		/// @brief Same as pop_random.
		/// @see pop_random().
		inline T remove_random()
		{
			return this->pop_random();
		}
		/// @brief Same as pop_random.
		/// @see pop_random(const int count).
		inline List<T> remove_random(const int count)
		{
			return this->pop_random(count);
		}
		/// @brief Same as remove_at.
		/// @see remove_at(const int index)
		inline T pop(const int index)
		{
			return this->remove_at(index);
		}
		/// @brief Same as remove_at.
		/// @see remove_at(const int index, const int count)
		inline List<T> pop(const int index, const int count)
		{
			return this->remove_at(index, count);
		}
		/// @brief Same as remove_at.
		/// @see remove_at(const int index)
		inline T pop_at(const int index)
		{
			return this->remove_at(index);
		}
		/// @brief Same as remove_at.
		/// @see remove_at(const int index, const int count)
		inline List<T> pop_at(const int index, const int count)
		{
			return this->remove_at(index, count);
		}
		/// @brief Same as remove_all.
		/// @see remove_all(T& element)
		inline int pop_all(T& element)
		{
			return this->remove_all(element);
		}
		/// @brief Same as remove_all.
		/// @see remove_all(const List<T>& other)
		inline int pop_all(const List<T>& other)
		{
			return this->remove_all(other);
		}
		/// @brief Same as push_back.
		/// @see push_back(const T& element)
		inline List<T>& operator<<(const T& element)
		{
			this->push_back(element);
			return (*this);
		}
		/// @brief Same as push_back.
		/// @see push_back(const List<T>& other)
		inline List<T>& operator<<(const List<T>& other)
		{
			this->push_back(other);
			return (*this);
		}
		/// @brief Same as push_back.
		/// @see push_back(const T& element)
		inline List<T>& operator+=(const T& element)
		{
			this->push_back(element);
			return (*this);
		}
		/// @brief Same as push_back.
		/// @see push_back(const List<T>& other)
		inline List<T>& operator+=(const List<T>& other)
		{
			this->push_back(other);
			return (*this);
		}
		/// @brief Same as remove.
		/// @see remove(T element)
		inline List<T>& operator-=(T element)
		{
			this->remove(element);
			return (*this);
		}
		/// @brief Same as remove.
		/// @see remove(const List<T>& other)
		inline List<T>& operator-=(const List<T>& other)
		{
			this->remove(other);
			return (*this);
		}
		/// @brief Same as unite.
		/// @see unite(const T& element)
		inline List<T>& operator|=(const T& element)
		{
			this->unite(element);
			return (*this);
		}
		/// @brief Same as unite.
		/// @see unite(const List<T>& other)
		inline List<T>& operator|=(const List<T>& other)
		{
			this->unite(other);
			return (*this);
		}
		/// @brief Same as intersect.
		/// @see intersect(const List<T>& other)
		inline List<T>& operator&=(const List<T>& other)
		{
			this->intersect(other);
			return (*this);
		}
		/// @brief Same as differentiate.
		/// @see differentiate(const T& element)
		inline List<T>& operator/=(const T& element)
		{
			this->differentiate(element);
			return (*this);
		}
		/// @brief Same as differentiate.
		/// @see differentiate(const List<T>& other)
		inline List<T>& operator/=(const List<T>& other)
		{
			this->differentiate(other);
			return (*this);
		}
		/// @brief Merges a List with an element.
		/// @param[in] element Element to merge with.
		/// @return New List with element added at the end of List.
		inline List<T> operator+(const T& element) const
		{
			List<T> result(*this);
			result += element;
			return result;
		}
		/// @brief Merges two Lists.
		/// @param[in] other Second List to merge with.
		/// @return New List with elements of second List added at the end of first List.
		inline List<T> operator+(const List<T>& other) const
		{
			List<T> result(*this);
			result += other;
			return result;
		}
		/// @brief Removes element from List.
		/// @param[in] element Element to remove.
		/// @return New List with elements of first List without given element.
		inline List<T> operator-(T element) const
		{
			List<T> result(*this);
			result -= element;
			return result;
		}
		/// @brief Removes second List from first List.
		/// @param[in] other List to remove.
		/// @return New List with elements of first List without the elements of second List.
		inline List<T> operator-(const List<T>& other) const
		{
			List<T> result(*this);
			result -= other;
			return result;
		}
		/// @brief Same as united.
		/// @see united(const T& element)
		inline List<T> operator|(const T& element) const
		{
			return this->united(element);
		}
		/// @brief Same as united.
		/// @see united(const List<T>& other)
		inline List<T> operator|(const List<T>& other) const
		{
			return this->united(other);
		}
		/// @brief Same as intersected.
		/// @see intersected(const List<T>& other)
		inline List<T> operator&(const List<T>& other) const
		{
			return this->intersected(other);
		}
		/// @brief Same as differentiated.
		/// @see differentiated(const T& element)
		inline List<T> operator/(const T& element) const
		{
			return this->differentiated(element);
		}
		/// @brief Same as differentiated.
		/// @see differentiated(const List<T>& other)
		inline List<T> operator/(const List<T>& other) const
		{
			return this->differentiated(other);
		}

	private:
		/// @brief Moves const iterator forward/backward by a number of elements.
		/// @param[in] it Current const iterator.
		/// @param[in] count Number of elements to move.
		/// @return Moved const iterator.
		inline const_iterator_t _const_iterator_plus(const_iterator_t it, int count) const
		{
			for_iter (i, 0, count)
			{
				++it;
			}
			for_iter (i, count, 0)
			{
				--it;
			}
			return it;
		}

		/// @brief Moves iterator forward/backward by a number of elements.
		/// @param[in] it Current iterator.
		/// @param[in] count Number of elements to move.
		/// @return Moved iterator.
		inline iterator_t _iterator_plus(iterator_t it, int count)
		{
			for_iter (i, 0, count)
			{
				++it;
			}
			for_iter (i, count, 0)
			{
				--it;
			}
			return it;
		}

	};
	
}

/// @brief Alias for simpler code.
#define hlist hltypes::List

#endif
