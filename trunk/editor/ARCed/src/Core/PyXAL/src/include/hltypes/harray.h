/// @file
/// @author  Boris Mikic
/// @author  Ivan Vucica
/// @version 1.4
/// 
/// @section LICENSE
/// 
/// This program is free software; you can redistribute it and/or modify it under
/// the terms of the BSD license: http://www.opensource.org/licenses/bsd-license.php
/// 
/// @section DESCRIPTION
/// 
/// Encapsulates std::vector and adds high level methods.

#ifndef HLTYPES_ARRAY_H
#define HLTYPES_ARRAY_H

#include <vector>
#include <algorithm>

#include "exception.h"
#include "hltypesUtil.h"
#include "hstring.h"

#ifdef _WIN32
	#undef min
	#undef max
#endif

/// @brief Provides a simpler syntax to iterate through an Array.
#define foreach(type, name, container) for (std::vector<type>::iterator name = (container).begin(); name != (container).end(); name++)
/// @brief Provides a simpler syntax to reverse iterate through an Array.
#define foreach_r(type, name, container) for (std::vector<type>::reverse_iterator name = (container).rbegin(); name != (container).rend(); name++)
/// @brief Alias for simpler code.
#define stdvector std::vector<T>

namespace hltypes
{
	/// @brief Encapsulates std::vector and adds high level methods.
	/// @author Boris Mikic
	/// @author Ivan Vucica
	template <class T> class Array : public stdvector
	{
	private:
		typedef typename std::vector<T>::iterator iterator_t;
		typedef typename std::vector<T>::const_iterator const_iterator_t;
	public:
		/// @brief Empty constructor.
		Array() : stdvector()
		{
		}
		/// @brief Copy constructor.
		/// @param[in] other Array to copy.
		Array(const Array<T>& other) : stdvector(other)
		{
		}
		/// @brief Constructor from single element.
		/// @param[in] element Element to insert.
		Array(const T& element) : stdvector()
		{
			this->insert_at(0, element);
		}
		/// @brief Constructor from single element.
		/// @param[in] element Element to insert.
		/// @param[in] times Number of times to insert element.
		Array(const T& element, int times) : stdvector()
		{
			this->insert_at(0, element, times);
		}
		/// @brief Constructor from another Array.
		/// @param[in] other Array to copy.
		/// @param[in] count Number of elements to copy.
		Array(const Array<T>& other, const int count) : stdvector()
		{
			this->insert_at(0, other, count);
		}
		/// @brief Constructor from another Array.
		/// @param[in] other Array to copy.
		/// @param[in] start Start index of elements to copy.
		/// @param[in] count Number of elements to copy.
		Array(const Array<T>& other, const int start, const int count) : stdvector()
		{
			this->insert_at(0, other, start, count);
		}
		/// @brief Constructor from C-type array.
		/// @param[in] other C-type array to copy.
		/// @param[in] count Number of elements to copy.
		Array(const T other[], const int count) : stdvector()
		{
			this->insert_at(0, other, count);
		}
		/// @brief Constructor from C-type array.
		/// @param[in] other C-type array to copy.
		/// @param[in] start Start index of elements to copy.
		/// @param[in] count Number of elements to copy.
		Array(const T other[], const int start, const int count) : stdvector()
		{
			this->insert_at(0, other, start, count);
		}
		/// @brief Destructor.
		~Array()
		{
		}
		/// @brief Returns element at specified position.
		/// @param[in] index Index of the element.
		/// @return Element at specified position.
		/// @note Does not work with bool as T, use Array::at directly instead.
		T& operator[](const int index)
		{
			if (index < 0)
			{
				return stdvector::at(this->size() + index);
			}
			return stdvector::at(index);
		}
		/// @brief Returns element at specified position.
		/// @param[in] index Index of the element.
		/// @return Element at specified position.
		/// @note Does not work with bool as T, use Array::at directly instead.
		const T& operator[](const int index) const
		{
			if (index < 0)
			{
				return stdvector::at(this->size() + index);
			}
			return stdvector::at(index);
		}
		/// @brief Returns a subarray.
		/// @param[in] start Start index of the elements to copy.
		/// @param[in] count Number of elements to copy.
		/// @return Subarray created from the current Array.
		Array<T> operator()(const int start, const int count) const
		{
			Array<T> result;
			const_iterator_t it = stdvector::begin();
			result.assign(it + start, it + (start + count));
			return result;
		}
		/// @brief Same as equals.
		/// @see equals
		bool operator==(const Array<T>& other) const
		{
			return this->equals(other);
		}
		/// @brief Same as nequals.
		/// @see nequals
		bool operator!=(const Array<T>& other) const
		{
			return this->nequals(other);
		}
		/// @brief Returns the number of elements in the Array.
		/// @return The number of elements in the Array.
		int size() const
		{
			return (int)stdvector::size();
		}
		/// @brief Compares the contents of two Arrays for being equal.
		/// @param[in] other Another Array.
		/// @return True if number of elements are equal and all pairs of elements at the same positions are equal.
		bool equals(const Array<T>& other) const
		{
			if (this->size() != other.size())
			{
				return false;
			}
			for_iter (i, 0, this->size())
			{
				// making sure operator== is used, not !=
				if (!(stdvector::at(i) == other.at(i)))
				{
					return false;
				}
			}
			return true;
		}
		/// @brief Compares the contents of two Arrays for being not equal.
		/// @param[in] other Another Array.
		/// @return True if number of elements are not equal or at least one pair of elements at the same positions is not equal.
		bool nequals(const Array<T>& other) const
		{
			if (this->size() != other.size())
			{
				return true;
			}
			for_iter (i, 0, this->size())
			{
				// making sure operator!= is used, not ==
				if (stdvector::at(i) != other.at(i))
				{
					return true;
				}
			}
			return false;
		}
		/// @brief Gets index of the given element.
		/// @param[in] element Element to search for.
		/// @return Index of the given element or -1 if element could not be found.
		int index_of(T element) const
		{
			for_iter (i, 0, this->size())
			{
				if (element == stdvector::at(i))
				{
					return i;
				}
			}
			return -1;
		}
		/// @brief Gets all indexes of the given element.
		/// @param[in] element Element to search for.
		/// @return Index of the given element or -1 if element could not be found.
		Array<int> indexes_of(T element) const
		{
			Array<int> result;
			for_iter (i, 0, this->size())
			{
				if (element == stdvector::at(i))
				{
					result.push_back(i);
				}
			}
			return result;
		}
		/// @brief Checks existence of element in Array.
		/// @param[in] element Element to search for.
		/// @return True if element is in Array.
		bool contains(const T& element) const
		{
			return (this->index_of(element) >= 0);
		}
		/// @brief Checks existence of elements in Array.
		/// @param[in] other Array with elements to search for.
		/// @return True if all elements are in Array.
		bool contains(const Array<T>& other) const
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
		/// @brief Checks existence of elements in Array.
		/// @param[in] other C-type array with elements to search for.
		/// @param[in] count How many elements the C-type array has.
		/// @return True if all elements are in Array.
		bool contains(const T other[], int count) const
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
		/// @brief Counts occurrences of element in Array.
		/// @param[in] element Element to search for.
		/// @return Number of occurrences of given element.
		int count(T element) const
		{
			int result = 0;
			for_iter (i, 0, this->size())
			{
				if (element == stdvector::at(i))
				{
					result++;
				}
			}
			return result;
		}
		/// @brief Inserts new element at specified position n times.
		/// @param[in] index Position where to insert the new element.
		/// @param[in] element Element to insert.
		/// @param[in] times Number of times to insert element.
		void insert_at(const int index, const T& element, const int times = 1)
		{
			stdvector::insert(stdvector::begin() + index, times, element);
		}
		/// @brief Inserts all elements of another Array into this one.
		/// @param[in] index Position where to insert the new elements.
		/// @param[in] other Array of elements to insert.
		void insert_at(const int index, const Array<T>& other)
		{
			stdvector::insert(stdvector::begin() + index, other.begin(), other.end());
		}
		/// @brief Inserts all elements of another Array into this one.
		/// @param[in] index Position where to insert the new elements.
		/// @param[in] other Array of elements to insert.
		/// @param[in] count Number of elements to insert.
		void insert_at(const int index, const Array<T>& other, const int count)
		{
			const_iterator_t it = other.begin();
			stdvector::insert(stdvector::begin() + index, it, it + count);
		}
		/// @brief Inserts all elements of another Array into this one.
		/// @param[in] index Position where to insert the new elements.
		/// @param[in] other Array of elements to insert.
		/// @param[in] start Start index of the elements to insert.
		/// @param[in] count Number of elements to insert.
		void insert_at(const int index, const Array<T>& other, const int start, const int count)
		{
			const_iterator_t it = other.begin();
			stdvector::insert(stdvector::begin() + index, it + start, it + (start + count));
		}
		/// @brief Inserts all elements of a C-type array into this Array.
		/// @param[in] index Position where to insert the new elements.
		/// @param[in] other C-type array of elements to insert.
		/// @param[in] count Number of elements to insert.
		void insert_at(const int index, const T other[], const int count)
		{
			stdvector::insert(stdvector::begin() + index, other, other + count);
		}
		/// @brief Inserts all elements of a C-type array into this Array.
		/// @param[in] index Position where to insert the new elements.
		/// @param[in] other C-type array of elements to insert.
		/// @param[in] start Start index of the elements to insert.
		/// @param[in] count Number of elements to insert.
		void insert_at(const int index, const T other[], const int start, const int count)
		{
			stdvector::insert(stdvector::begin() + index, other + start, other + (start + count));
		}
		/// @brief Removes element at given index.
		/// @param[in] index Index of element to remove.
		/// @return The removed element.
		T remove_at(const int index)
		{
			if (index >= this->size())
			{
				throw index_error(index);
			}
			T result = stdvector::at(index);
			stdvector::erase(stdvector::begin() + index);
			return result;
		}
		/// @brief Removes n elements at given index of Array.
		/// @param[in] index Start index of elements to remove.
		/// @param[in] count Number of elements to remove.
		/// @return Array of all removed elements.
		/// @note Elements in the returned Array are in the same order as in the orignal Array.
		Array<T> remove_at(const int index, const int count)
		{
			if (index >= this->size() || index + count > this->size())
			{
				throw range_error(index, count);
			}
			Array<T> result;
			iterator_t it = stdvector::begin();
			iterator_t begin = it + index;
			iterator_t end = it + (index + count);
			result.assign(begin, end);
			stdvector::erase(begin, end);
			return result;
		}
		/// @brief Removes first occurrence of element in Array.
		/// @param[in] element Element to remove.
		void remove(T element)
		{
			int index = this->index_of(element);
			if (index < 0)
			{
				throw element_not_found_error();
			}
			stdvector::erase(stdvector::begin() + index);
		}
		/// @brief Removes first occurrence of each element in another Array from this one.
		/// @param[in] other Array of elements to remove.
		void remove(const Array<T>& other)
		{
			int index;
			for_iter (i, 0, other.size())
			{
				index = this->index_of(other.at(i));
				if (index < 0)
				{
					throw element_not_found_error();
				}
				stdvector::erase(stdvector::begin() + index);
			}
		}
		/// @brief Removes all occurrences of element in Array.
		/// @param[in] element Element to remove.
		/// @return Number of elements removed.
		int remove_all(const T& element)
		{
			Array<int> indexes = this->indexes_of(element);
			iterator_t it = stdvector::begin();
			for_iter_r (i, indexes.size(), 0)
			{
				stdvector::erase(it + indexes[i]);
			}
			return indexes.size();
		}
		/// @brief Removes all occurrences of each element in another Array from this one.
		/// @param[in] other Array of elements to remove.
		/// @return Number of elements removed.
		int remove_all(const Array<T>& other)
		{
			Array<int> indexes;
			iterator_t it;
			int count = 0;
			for_iter (i, 0, other.size())
			{
				Array<int> indexes = this->indexes_of(other.at(i));
				iterator_t it = stdvector::begin();
				for_iter_r (j, indexes.size(), 0)
				{
					stdvector::erase(it + indexes[j]);
				}
				count += indexes.size();
			}
			return count;
		}
		/// @brief Adds element at the end of Array.
		/// @param[in] element Element to add.
		void push_back(const T& element)
		{
			stdvector::push_back(element);
		}
		/// @brief Adds element at the end of Array n times.
		/// @param[in] element Element to add.
		/// @param[in] times Number of times to add the element.
		void push_back(const T& element, int times)
		{
			this->insert_at(this->size(), element, times);
		}
		/// @brief Adds all elements from another Array at the end of this one.
		/// @param[in] other Array of elements to add.
		void push_back(const Array<T>& other)
		{
			this->insert_at(this->size(), other);
		}
		/// @brief Adds all elements from another Array at the end of this one.
		/// @param[in] other Array of elements to add.
		/// @param[in] count Number of elements to add.
		void push_back(const Array<T>& other, const int count)
		{
			this->insert_at(this->size(), other, count);
		}
		/// @brief Adds all elements from another Array at the end of this one.
		/// @param[in] other Array of elements to add.
		/// @param[in] start Start index of the elements to add.
		/// @param[in] count Number of elements to add.
		void push_back(const Array<T>& other, const int start, const int count)
		{
			this->insert_at(this->size(), other, start, count);
		}
		/// @brief Adds all elements from a C-type array at the end of Array.
		/// @param[in] other C-type array of elements to add.
		/// @param[in] count Number of elements to add.
		void push_back(const T other[], const int count)
		{
			this->insert_at(this->size(), other, count);
		}
		/// @brief Adds all elements from a C-type array at the end of Array.
		/// @param[in] other C-type array of elements to add.
		/// @param[in] start Start index of the elements to add.
		/// @param[in] count Number of elements to add.
		void push_back(const T other[], const int start, const int count)
		{
			this->insert_at(this->size(), other, start, count);
		}
		/// @brief Adds element at the beginning of Array n times.
		/// @param[in] element Element to add.
		/// @param[in] times Number of times to add the element.
		void push_front(const T& element, int times = 1)
		{
			this->insert_at(0, element, times);
		}
		/// @brief Adds all elements from another Array at the beginning of this one.
		/// @param[in] other Array of elements to add.
		void push_front(const Array<T>& other)
		{
			this->insert_at(0, other);
		}
		/// @brief Adds all elements from another Array at the beginning of this one.
		/// @param[in] other Array of elements to add.
		/// @param[in] count Number of elements to add.
		void push_front(const Array<T>& other, const int count)
		{
			this->insert_at(0, other, count);
		}
		/// @brief Adds all elements from another Array at the beginning of this one.
		/// @param[in] other Array of elements to add.
		/// @param[in] start Start index of the elements to add.
		/// @param[in] count Number of elements to add.
		void push_front(const Array<T>& other, const int start, const int count)
		{
			this->insert_at(0, other, start, count);
		}
		/// @brief Adds all elements from a C-type array at the beginning of Array.
		/// @param[in] other C-type array of elements to add.
		/// @param[in] count Number of elements to add.
		void push_front(const T other[], const int count)
		{
			this->insert_at(0, other, count);
		}
		/// @brief Adds all elements from a C-type array at the beginning of Array.
		/// @param[in] other C-type array of elements to add.
		/// @param[in] start Start index of the elements to add.
		/// @param[in] count Number of elements to add.
		void push_front(const T other[], const int start, const int count)
		{
			this->insert_at(0, other, start, count);
		}
		/// @brief Removes first element of Array.
		/// @return The removed element.
		T pop_front()
		{
			if (this->size() == 0)
			{
				throw index_error(0);
			}
			return this->remove_at(0);
		}
		/// @brief Removes n elements from the beginning of Array.
		/// @param[in] count Number of elements to remove.
		/// @return Array of all removed elements.
		/// @note Elements in the returned Array are in the same order as in the orignal Array.
		Array<T> pop_front(const int count)
		{
			if (count > this->size())
			{
				throw index_error(count);
			}
			Array<T> result;
			iterator_t begin = stdvector::begin();
			iterator_t end = begin + count;
			result.assign(begin, end);
			stdvector::erase(begin, end);
			return result;
		}
		/// @brief Removes last element of Array.
		/// @return The removed element.
		T pop_back()
		{
			if (this->size() == 0)
			{
				throw index_error(0);
			}
			T element = stdvector::back();
			stdvector::pop_back();
			return element;
		}
		/// @brief Removes n elements from the end of Array.
		/// @param[in] count Number of elements to remove.
		/// @return Array of all removed elements.
		/// @note Elements in the returned Array are in the same order as in the orignal Array.
		Array<T> pop_back(const int count)
		{
			if (count > this->size())
			{
				throw index_error(count);
			}
			Array<T> result;
			iterator_t end = stdvector::end();
			iterator_t begin = end - count;
			result.assign(begin, end);
			stdvector::erase(begin, end);
			return result;
		}
		/// @brief Unites elements of this Array with an element.
		/// @param[in] element Element to unite with.
		void unite(const T& element)
		{
			this->insert_at(this->size(), element);
			this->remove_duplicates();
		}
		/// @brief Unites elements of this Array with another one.
		/// @param[in] other Array to unite with.
		void unite(const Array<T>& other)
		{
			this->insert_at(this->size(), other);
			this->remove_duplicates();
		}
		/// @brief Creates a new Array as union of this Array with an element.
		/// @param[in] element Element to unite with.
		/// @return A new Array.
		Array<T> united(const T& element) const
		{
			Array<T> result(*this);
			result.unite(element);
			return result;
		}
		/// @brief Creates a new Array as union of this Array with another one.
		/// @param[in] other Array to unite with.
		/// @return A new Array.
		Array<T> united(const Array<T>& other) const
		{
			Array<T> result(*this);
			result.unite(other);
			return result;
		}
		/// @brief Intersects elements of this Array with another one.
		/// @param[in] other Array to intersect with.
		void intersect(const Array<T>& other)
		{
			Array<T> result;
			for_iter (i, 0, this->size())
			{
				if (other.contains(stdvector::at(i)))
				{
					result.push_back(stdvector::at(i));
				}
			}
			stdvector::assign(result.begin(), result.end());
		}
		/// @brief Creates a new Array as intersection of this Array with another one.
		/// @param[in] other Array to intersect with.
		/// @return A new Array.
		Array<T> intersected(const Array<T>& other) const
		{
			Array<T> result(*this);
			result.intersect(other);
			return result;
		}
		/// @brief Differentiates elements of this Array with an element.
		/// @param[in] other Element to differentiate with.
		/// @note Unlike remove, this method ignores if the element is not in this Array.
		void differentiate(const T& element)
		{
			int index = this->index_of(element);
			if (index >= 0)
			{
				stdvector::erase(stdvector::begin() + index);
			}
		}
		/// @brief Differentiates elements of this Array with another one.
		/// @param[in] other Array to differentiate with.
		/// @note Unlike remove, this method ignore elements of other Array that are not in this one.
		void differentiate(const Array<T>& other)
		{
			int index;
			for_iter (i, 0, other.size())
			{
				index = this->index_of(other.at(i));
				if (index >= 0)
				{
					stdvector::erase(stdvector::begin() + index);
				}
			}
		}
		/// @brief Creates a new Array as difference of this Array with an element.
		/// @param[in] other Element to differentiate with.
		/// @return A new Array.
		/// @note Unlike remove, this method ignores if the element is not in this Array.
		Array<T> differentiated(const T& element) const
		{
			Array<T> result(*this);
			result.differentiate(element);
			return result;
		}
		/// @brief Creates a new Array as difference of this Array with another one.
		/// @param[in] other Array to differentiate with.
		/// @return A new Array.
		/// @note Unlike remove, this method ignore elements of other Array that are not in this one.
		Array<T> differentiated(const Array<T>& other) const
		{
			Array<T> result(*this);
			result.differentiate(other);
			return result;
		}
		/// @brief Reverses order of elements.
		void reverse()
		{
			if (this->size() > 0)
			{
				std::reverse(stdvector::begin(), stdvector::end());
			}
		}
		/// @brief Creates new Array with reversed order of elements.
		/// @return A new Array.
		Array<T> reversed() const
		{
			Array<T> result(*this);
			result.reverse();
			return result;
		}
		/// @brief Removes duplicates in Array.
		void remove_duplicates()
		{
			Array<int> indexes;
			iterator_t it = stdvector::begin();
			for_iter (i, 0, this->size())
			{
				indexes = this->indexes_of(stdvector::at(i));
				for_iter_r (j, indexes.size(), 1)
				{
					stdvector::erase(it + indexes[j]);
				}
			}
		}
		/// @brief Creates new Array without duplicates.
		/// @return A new Array.
		Array<T> removed_duplicates() const
		{
			Array<T> result(*this);
			result.remove_duplicates();
			return result;
		}
		/// @brief Sorts elements in Array.
		/// @note The sorting order is ascending.
		void sort()
		{
			if (this->size() > 0)
			{
				std::stable_sort(stdvector::begin(), stdvector::end());
			}
		}
		/// @brief Sorts elements in Array.
		/// @param[in] compare_function Function pointer with comparison function that takes two elements of type T and returns bool.
		/// @note The sorting order is ascending.
		/// @note compare_function should return true if first element is less than the second element.
		void sort(bool (*compare_function)(T, T))
		{
			if (this->size() > 0)
			{
				std::stable_sort(stdvector::begin(), stdvector::end(), compare_function);
			}
		}
		/// @brief Creates new sorted Array.
		/// @return A new Array.
		/// @note The sorting order is ascending.
		Array<T> sorted() const
		{
			Array<T> result(*this);
			result.sort();
			return result;
		}
		/// @brief Creates new sorted Array.
		/// @param[in] compare_function Function pointer with comparison function that takes two elements of type T and returns bool.
		/// @return A new Array.
		/// @note The sorting order is ascending.
		/// @note compare_function should return true if first element is less than the second element.
		Array<T> sorted(bool (*compare_function)(T, T)) const
		{
			Array<T> result(*this);
			result.sort(compare_function);
			return result;
		}
		/// @brief Randomizes order of elements in Array.
		void randomize()
		{
			std::random_shuffle(stdvector::begin(), stdvector::end());
		}
		/// @brief Creates a new Array with randomized order of elements.
		/// @return A new Array.
		Array<T> randomized() const
		{
			Array<T> result(*this);
			result.randomize();
			return result;
		}
		/// @brief Finds minimum element in Array.
		/// @return Minimum Element.
		T min() const
		{
			if (this->size() == 0)
			{
				throw size_error("min()");
			}
			return (*std::min_element(stdvector::begin(), stdvector::end()));
		}
		/// @brief Finds minimum element in Array.
		/// @param[in] compare_function Function pointer with comparison function that takes two elements of type T and returns bool.
		/// @return Minimum Element.
		/// @note compare_function should return true if first element is less than second element.
		T min(bool (*compare_function)(T, T)) const
		{
			if (this->size() == 0)
			{
				throw size_error("min()");
			}
			return (*std::min_element(stdvector::begin(), stdvector::end(), compare_function));
		}
		/// @brief Finds maximum element in Array.
		/// @return Maximum Element.
		T max() const
		{
			if (this->size() == 0)
			{
				throw size_error("max()");
			}
			return (*std::max_element(stdvector::begin(), stdvector::end()));
		}
		/// @brief Finds maximum element in Array.
		/// @param[in] compare_function Function pointer with comparison function that takes two elements of type T and returns bool.
		/// @return Maximum Element.
		/// @note compare_function should return true if first element is greater than second element.
		T max(bool (*compare_function)(T, T)) const
		{
			if (this->size() == 0)
			{
				throw size_error("max()");
			}
			return (*std::max_element(stdvector::begin(), stdvector::end(), compare_function));
		}
		/// @brief Gets a random element in Array.
		/// @return Random element.
		T random() const
		{
			if (this->size() == 0)
			{
				throw size_error("random()");
			}
			return stdvector::at(hrand(this->size()));
		}
		/// @brief Gets an Array of random elements selected from this one.
		/// @param[in] count Number of random elements.
		/// @param[in] unique Whether to force all random values to be unique.
		/// @return Array of random elements selected from this one.
		Array<T> random(int count, bool unique = false) const
		{
			Array<T> result;
			if (!unique)
			{
				for_iter (i, 0, count)
				{
					result.push_back(stdvector::at(hrand(this->size())));
				}
			}
			else if (count > 0)
			{
				if (count >= this->size())
				{
					return this->randomized();
				}
				Array<int> indexes;
				for_iter (i, 0, this->size())
				{
					indexes.push_back(i);
				}
				for_iter (i, 0, count)
				{
					result.push_back(stdvector::at(indexes.remove_at(hrand(indexes.size()))));
				}
			}
			return result;
		}
		/// @brief Gets a random element in Array and removes it.
		/// @return Random element.
		T pop_random()
		{
			if (this->size() == 0)
			{
				throw size_error("pop_random()");
			}
			T result = stdvector::at(hrand(this->size()));
			this->remove(result);
			return result;
		}
		/// @brief Gets an Array of random elements selected from this one and removes them.
		/// @param[in] count Number of random elements.
		/// @param[in] unique Whether to force all random values to be unique.
		/// @return Array of random elements selected from this one.
		Array<T> pop_random(int count, bool unique = false)
		{
			Array<T> result;
			if (!unique)
			{
				for_iter (i, 0, count)
				{
					result.push_back(stdvector::at(hrand(this->size())));
				}
			}
			else if (count > 0)
			{
				if (count >= this->size())
				{
					return this->randomized();
				}
				Array<int> indexes;
				for_iter (i, 0, this->size())
				{
					indexes.push_back(i);
				}
				for_iter (i, 0, count)
				{
					result.push_back(stdvector::at(indexes.remove_at(hrand(indexes.size()))));
				}
			}
			this->remove(result);
			return result;
		}
		/// @brief Joins all elements into a string.
		/// @param[in] separator Separator string between elements.
		/// @return String or joined elements separater by separator string.
		/// @note Make sure your elements can be cast into String or are already String.
		hstr join(chstr separator) const
		{
			hstr result;
			if (this->size() > 0)
			{
				result += hstr(stdvector::at(0));
				for_iter (i, 1, this->size())
				{
					result += separator + hstr(stdvector::at(i));
				}
			}
			return result;
		}
		/// @brief Finds and returns new Array of elements that match the condition.
		/// @param[in] condition_function Function pointer with condition function that takes one element of type T and returns bool.
		/// @return New Array with all matching elements.
		Array<T> find_all(bool (*condition_function)(T))
		{
			Array<T> result;
			for_iter (i, 0, this->size())
			{
				if (condition_function(stdvector::at(i)))
				{
					result.push_back(stdvector::at(i));
				}
			}
			return result;
		}
		/// @brief Finds and returns first occurrence of element that matches the condition.
		/// @param[in] condition_function Function pointer with condition function that takes one element of type T and returns bool.
		/// @return Pointer to element that matches the condition or NULL if no element was found.
		T* find_first(bool (*condition_function)(T))
		{
			for_iter (i, 0, this->size())
			{
				if (condition_function(stdvector::at(i)))
				{
					return &stdvector::at(i);
				}
			}
			return NULL;
		}
		/// @brief Checks if at least one element matches the condition.
		/// @param[in] condition_function Function pointer with condition function that takes one element of type T and returns bool.
		/// @return True if at least one element matches the condition.
		bool matches_any(bool (*condition_function)(T))
		{
			for_iter (i, 0, this->size())
			{
				if (condition_function(stdvector::at(i)))
				{
					return true;
				}
			}
			return false;
		}
		/// @brief Checks if all elements match the condition.
		/// @param[in] condition_function Function pointer with condition function that takes one element of type T and returns bool.
		/// @return True if all elements match the condition.
		bool matches_all(bool (*condition_function)(T))
		{
			for_iter (i, 0, this->size())
			{
				if (!condition_function(stdvector::at(i)))
				{
					return false;
				}
			}
			return true;
		}
		/// @brief Returns a new Array with all elements cast into type S.
		/// @return A new Array with all elements cast into type S.
		/// @note Make sure all elements in the Array can be cast into type S.
		template <class S>
		Array<S> cast()
		{
			Array<S> result;
			for_iter (i, 0, this->size())
			{
				result.push_back((S)stdvector::at(i));
			}
			return result;
		}
		/// @brief Returns a new Array with all elements dynamically cast into type S.
		/// @param[in] include_nulls Whether to include NULLs that failed to cast.
		/// @return A new Array with all elements cast into type S.
		/// @note Be careful not to use this function with non-pointers and classes that don't have virtual functions.
		template <class S>
		Array<S> dyn_cast(bool include_nulls = false)
		{
			Array<S> result;
			S value;
			for_iter (i, 0, this->size())
			{
				// when seeing "dynamic_cast", I always think of fireballs
				value = dynamic_cast<S>(stdvector::at(i));
				if (value != NULL || include_nulls)
				{
					result.push_back(value);
				}
			}
			return result;
		}
		/// @brief Accesses first element of Array.
		/// @return The first element.
		T& first()
		{
			return stdvector::front();
		}
		/// @brief Accesses last element of Array.
		/// @return The last element.
		T& last()
		{
			return stdvector::back();
		}
		/// @brief Same as contains.
		/// @see contains(const T& element)
		bool includes(const T& element) const
		{
			return this->contains(element);
		}
		/// @brief Same as contains.
		/// @see contains(const Array<T>& other)
		bool includes(const Array<T>& other) const
		{
			return this->contains(other);
		}
		/// @brief Same as contains.
		/// @see contains(const T other[], int count)
		bool includes(const T other[], int count) const
		{
			return this->contains(other, count);
		}
		/// @brief Same as contains.
		/// @see contains(const T& element)
		bool has(const T& element) const
		{
			return this->contains(element);
		}
		/// @brief Same as contains.
		/// @see contains(const Array<T>& other)
		bool has(const Array<T>& other) const
		{
			return this->contains(other);
		}
		/// @brief Same as contains.
		/// @see contains(const T other[], int count)
		bool has(const T other[], int count) const
		{
			return this->contains(other, count);
		}
		/// @brief Same as contains.
		/// @see contains(const T& element)
		bool has_element(const T& element) const
		{
			return this->contains(element);
		}
		/// @brief Same as contains.
		/// @see contains(const Array<T>& other)
		bool has_element(const Array<T>& other) const
		{
			return this->contains(other);
		}
		/// @brief Same as contains.
		/// @see contains(const T other[], int count)
		bool has_element(const T other[], int count) const
		{
			return this->contains(other, count);
		}
		/// @brief Same as push_back.
		/// @see push_back(const T& element)
		void add(const T& element)
		{
			this->push_back(element);
		}
		/// @brief Same as push_back.
		/// @see push_back(const T& element, int times)
		void add(const T& element, int times)
		{
			this->push_back(element, times);
		}
		/// @brief Same as push_back.
		/// @see push_back(const Array<T>& other)
		void add(const Array<T>& other)
		{
			this->push_back(other);
		}
		/// @brief Same as push_back.
		/// @see push_back(const Array<T>& other, const int count)
		void add(const Array<T>& other, const int count)
		{
			this->push_back(other, count);
		}
		/// @brief Same as push_back.
		/// @see push_back(const Array<T>& other, const int start, const int count)
		void add(const Array<T>& other, const int start, const int count)
		{
			this->push_back(other, start, count);
		}
		/// @brief Same as push_back.
		/// @see push_back(const T other[], const int count)
		void add(const T other[], const int count)
		{
			this->push_back(other, count);
		}
		/// @brief Same as push_back.
		/// @see push_back(const T other[], const int start, const int count)
		void add(const T other[], const int start, const int count)
		{
			this->push_back(other, start, count);
		}
		/// @brief Same as push_back.
		/// @see push_back(const T& element)
		void append(const T& element)
		{
			this->push_back(element);
		}
		/// @brief Same as push_back.
		/// @see push_back(const T& element, int times)
		void append(const T& element, int times)
		{
			this->push_back(element, times);
		}
		/// @brief Same as push_back.
		/// @see push_back(const Array<T>& other)
		void append(const Array<T>& other)
		{
			this->push_back(other);
		}
		/// @brief Same as push_back.
		/// @see push_back(const Array<T>& other, const int count)
		void append(const Array<T>& other, const int count)
		{
			this->push_back(other, count);
		}
		/// @brief Same as push_back.
		/// @see push_back(const Array<T>& other, const int start, const int count)
		void append(const Array<T>& other, const int start, const int count)
		{
			this->push_back(other, start, count);
		}
		/// @brief Same as push_back.
		/// @see push_back(const T other[], const int count)
		void append(const T other[], const int count)
		{
			this->push_back(other, count);
		}
		/// @brief Same as push_back.
		/// @see push_back(const T other[], const int start, const int count)
		void append(const T other[], const int start, const int count)
		{
			this->push_back(other, start, count);
		}
		/// @brief Same as push_back.
		/// @see push_back(const T& element).
		void push_last(const T& element)
		{
			this->push_back(element);
		}
		/// @brief Same as push_back.
		/// @see push_back(const T& element, int times).
		void push_last(const T& element, int times)
		{
			this->push_back(element, times);
		}
		/// @brief Same as push_back.
		/// @see push_back(const Array<T>& other).
		void push_last(const Array<T>& other)
		{
			this->push_back(other);
		}
		/// @brief Same as push_back.
		/// @see push_back(const Array<T>& other, const int count).
		void push_last(const Array<T>& other, const int count)
		{
			this->push_back(other, count);
		}
		/// @brief Same as push_back.
		/// @see push_back(const Array<T>& other, const int start, const int count).
		void push_last(const Array<T>& other, const int start, const int count)
		{
			this->push_back(other, start, count);
		}
		/// @brief Same as push_back.
		/// @see push_back(const T other[], const int count).
		void push_last(const T other[], const int count)
		{
			this->push_back(other, count);
		}
		/// @brief Same as push_back.
		/// @see push_back(const T other[], const int start, const int count).
		void push_last(const T other[], const int start, const int count)
		{
			this->push_back(other, start, count);
		}
		/// @brief Same as push_front.
		/// @see push_front(const T& element, int times).
		void push_first(const T& element, int times = 1)
		{
			this->push_front(element, times);
		}
		/// @brief Same as push_front.
		/// @see push_front(const Array<T>& other).
		void push_first(const Array<T>& other)
		{
			this->push_front(other);
		}
		/// @brief Same as push_front.
		/// @see push_front(const Array<T>& other, const int count).
		void push_first(const Array<T>& other, const int count)
		{
			this->push_front(other, count);
		}
		/// @brief Same as push_front.
		/// @see push_front(const Array<T>& other, const int start, const int count).
		void push_first(const Array<T>& other, const int start, const int count)
		{
			this->push_front(other, start, count);
		}
		/// @brief Same as push_front.
		/// @see push_front(const T other[], const int count).
		void push_first(const T other[], const int count)
		{
			this->push_front(other, count);
		}
		/// @brief Same as push_front.
		/// @see push_front(const T other[], const int start, const int count).
		void push_first(const T other[], const int start, const int count)
		{
			this->push_front(other, start, count);
		}
		/// @brief Same as pop_front.
		/// @see pop_front().
		T pop_first()
		{
			return this->pop_front();
		}
		/// @brief Same as pop_front.
		/// @see pop_front(const int count).
		Array<T> pop_first(const int count)
		{
			return this->pop_front(count);
		}
		/// @brief Same as pop_back.
		/// @see pop_back().
		T pop_last()
		{
			return this->pop_back();
		}
		/// @brief Same as pop_back.
		/// @see pop_back(const int count).
		Array<T> pop_last(const int count)
		{
			return this->pop_back(count);
		}
		/// @brief Same as pop_front.
		/// @see pop_front().
		T remove_front()
		{
			return this->pop_front();
		}
		/// @brief Same as pop_front.
		/// @see pop_front(const int count).
		Array<T> remove_front(const int count)
		{
			return this->pop_front(count);
		}
		/// @brief Same as pop_back.
		/// @see pop_back().
		T remove_back()
		{
			return this->pop_back();
		}
		/// @brief Same as pop_back.
		/// @see pop_back(const int count).
		Array<T> remove_back(const int count)
		{
			return this->pop_back(count);
		}
		/// @brief Same as pop_front.
		/// @see pop_front().
		T remove_first()
		{
			return this->pop_front();
		}
		/// @brief Same as pop_front.
		/// @see pop_front(const int count).
		Array<T> remove_first(const int count)
		{
			return this->pop_front(count);
		}
		/// @brief Same as pop_back.
		/// @see pop_back().
		T remove_last()
		{
			return this->pop_back();
		}
		/// @brief Same as pop_back.
		/// @see pop_back(const int count).
		Array<T> remove_last(const int count)
		{
			return this->pop_back(count);
		}
		/// @brief Same as remove_at.
		/// @see remove_at(const int index)
		T pop(const int index)
		{
			return this->remove_at(index);
		}
		/// @brief Same as remove_at.
		/// @see remove_at(const int index, const int count)
		Array<T> pop(const int index, const int count)
		{
			return this->remove_at(index, count);
		}
		/// @brief Same as remove_at.
		/// @see remove_at(const int index)
		T pop_at(const int index)
		{
			return this->remove_at(index);
		}
		/// @brief Same as remove_at.
		/// @see remove_at(const int index, const int count)
		Array<T> pop_at(const int index, const int count)
		{
			return this->remove_at(index, count);
		}
		/// @brief Same as remove_all.
		/// @see remove_all(T& element)
		int pop_all(T& element)
		{
			return this->remove_all(element);
		}
		/// @brief Same as remove_all.
		/// @see remove_all(const Array<T>& other)
		int pop_all(const Array<T>& other)
		{
			return this->remove_all(other);
		}
		/// @brief Same as push_back.
		/// @see push_back(const T& element)
		Array<T>& operator<<(const T& element)
		{
			this->push_back(element);
			return (*this);
		}
		/// @brief Same as push_back.
		/// @see push_back(const Array<T>& other)
		Array<T>& operator<<(const Array<T>& other)
		{
			this->push_back(other);
			return (*this);
		}
		/// @brief Same as push_back.
		/// @see push_back(const T& element)
		Array<T>& operator+=(const T& element)
		{
			this->push_back(element);
			return (*this);
		}
		/// @brief Same as push_back.
		/// @see push_back(const Array<T>& other)
		Array<T>& operator+=(const Array<T>& other)
		{
			this->push_back(other);
			return (*this);
		}
		/// @brief Same as remove.
		/// @see remove(T element)
		Array<T>& operator-=(T element)
		{
			this->remove(element);
			return (*this);
		}
		/// @brief Same as remove.
		/// @see remove(const Array<T>& other)
		Array<T>& operator-=(const Array<T>& other)
		{
			this->remove(other);
			return (*this);
		}
		/// @brief Same as unite.
		/// @see unite(const T& element)
		Array<T>& operator|=(const T& element)
		{
			this->unite(element);
			return (*this);
		}
		/// @brief Same as unite.
		/// @see unite(const Array<T>& other)
		Array<T>& operator|=(const Array<T>& other)
		{
			this->unite(other);
			return (*this);
		}
		/// @brief Same as intersect.
		/// @see intersect(const Array<T>& other)
		Array<T>& operator&=(const Array<T>& other)
		{
			this->intersect(other);
			return (*this);
		}
		/// @brief Same as differentiate.
		/// @see differentiate(const T& element)
		Array<T>& operator/=(const T& element)
		{
			this->differentiate(element);
			return (*this);
		}
		/// @brief Same as differentiate.
		/// @see differentiate(const Array<T>& other)
		Array<T>& operator/=(const Array<T>& other)
		{
			this->differentiate(other);
			return (*this);
		}
		/// @brief Merges an Array with an element.
		/// @param[in] element Element to merge with.
		/// @return New Array with element added at the end of Array.
		Array<T> operator+(const T& element) const
		{
			Array<T> result(*this);
			result += element;
			return result;
		}
		/// @brief Merges two Arrays.
		/// @param[in] other Second Array to merge with.
		/// @return New Array with elements of second Array added at the end of first Array.
		Array<T> operator+(const Array<T>& other) const
		{
			Array<T> result(*this);
			result += other;
			return result;
		}
		/// @brief Removes element from Array.
		/// @param[in] element Element to remove.
		/// @return New Array with elements of first Array without given element.
		Array<T> operator-(T element) const
		{
			Array<T> result(*this);
			result -= element;
			return result;
		}
		/// @brief Removes second Array from first Array.
		/// @param[in] other Array to remove.
		/// @return New Array with elements of first Array without the elements of second Array.
		Array<T> operator-(const Array<T>& other) const
		{
			Array<T> result(*this);
			result -= other;
			return result;
		}
		/// @brief Same as united.
		/// @see united(const T& element)
		Array<T> operator|(const T& element) const
		{
			return this->united(element);
		}
		/// @brief Same as united.
		/// @see united(const Array<T>& other)
		Array<T> operator|(const Array<T>& other) const
		{
			return this->united(other);
		}
		/// @brief Same as intersected.
		/// @see intersected(const Array<T>& other)
		Array<T> operator&(const Array<T>& other) const
		{
			return this->intersected(other);
		}
		/// @brief Same as differentiated.
		/// @see differentiated(const T& element)
		Array<T> operator/(const T& element) const
		{
			return this->differentiated(element);
		}
		/// @brief Same as differentiated.
		/// @see differentiated(const Array<T>& other)
		Array<T> operator/(const Array<T>& other) const
		{
			return this->differentiated(other);
		}
		
	};
	
}

/// @brief Alias for simpler code.
#define harray hltypes::Array

#endif
