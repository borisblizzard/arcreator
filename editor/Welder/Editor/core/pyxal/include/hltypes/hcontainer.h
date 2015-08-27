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
/// Encapsulates all containers and adds high level methods.

#ifndef HLTYPES_CONTAINER_H
#define HLTYPES_CONTAINER_H

#include <algorithm>
#include <vector>

#include "hexception.h"
#include "hltypesUtil.h"
#include "hplatform.h"
#include "hstring.h"

namespace hltypes
{
	/// @brief Encapsulates container functionality and adds high level methods.
	template <class STD, class T>
	class Container : STD
	{
	public:
		/// @brief Iterator type exposure.
		typedef typename STD::iterator iterator_t;
		/// @brief Iterator type exposure.
		typedef typename STD::const_iterator const_iterator_t;
		/// @brief Iterator type exposure.
		typedef typename STD::reverse_iterator riterator_t;
		/// @brief Iterator type exposure.
		typedef typename STD::const_reverse_iterator const_riterator_t;
		/// @brief Empty constructor.
		inline Container() : STD()
		{
		}
		/// @brief Copy constructor.
		/// @param[in] other Container to copy.
		inline Container(const Container& other) : STD()
		{
			this->insertAt(0, other);
		}
		/// @brief Constructor from single element.
		/// @param[in] element Element to insert.
		inline Container(const T& element) : STD()
		{
			this->insertAt(0, element);
		}
		/// @brief Constructor from single element.
		/// @param[in] element Element to insert.
		/// @param[in] times Number of times to insert element.
		inline Container(const T& element, int times) : STD()
		{
			this->insertAt(0, element, times);
		}
		/// @brief Constructor from another Container.
		/// @param[in] other Container to copy.
		/// @param[in] count Number of elements to copy.
		inline Container(const Container& other, const int count) : STD()
		{
			this->insertAt(0, other, count);
		}
		/// @brief Constructor from another Container.
		/// @param[in] other Container to copy.
		/// @param[in] start Start index of elements to copy.
		/// @param[in] count Number of elements to copy.
		inline Container(const Container& other, const int start, const int count) : STD()
		{
			this->insertAt(0, other, start, count);
		}
		/// @brief Constructor from C-type array.
		/// @param[in] other C-type array to copy.
		/// @param[in] count Number of elements to copy.
		inline Container(const T other[], const int count) : STD()
		{
			this->insertAt(0, other, count);
		}
		/// @brief Constructor from C-type array.
		/// @param[in] other C-type array to copy.
		/// @param[in] start Start index of elements to copy.
		/// @param[in] count Number of elements to copy.
		inline Container(const T other[], const int start, const int count) : STD()
		{
			this->insertAt(0, other, start, count);
		}
		/// @brief Destructor.
		inline ~Container()
		{
		}
		/// @brief Returns the number of elements in the Container.
		/// @return The number of elements in the Container.
		inline int size() const
		{
			return (int)STD::size();
		}
		/// @brief Check if Container is empty.
		/// @return True if Container is empty.
		inline bool isEmpty() const
		{
			return STD::empty();
		}
		/// @brief Removes all data from this Container.
		inline void clear()
		{
			return STD::clear();
		}
		/// @brief Gets the iterator at the beginning.
		/// @return The iterator object.
		inline iterator_t begin()
		{
			return STD::begin();
		}
		/// @brief Gets the iterator at the beginning.
		/// @return The iterator object.
		inline const_iterator_t begin() const
		{
			return STD::begin();
		}
		/// @brief Gets the iterator at the end.
		/// @return The iterator object.
		inline iterator_t end()
		{
			return STD::end();
		}
		/// @brief Gets the iterator at the end.
		/// @return The iterator object.
		inline const_iterator_t end() const
		{
			return STD::end();
		}
		/// @brief Gets the reverse iterator at the beginning.
		/// @return The iterator object.
		inline riterator_t rbegin()
		{
			return STD::rbegin();
		}
		/// @brief Gets the reverse iterator at the beginning.
		/// @return The iterator object.
		inline const_riterator_t rbegin() const
		{
			return STD::rbegin();
		}
		/// @brief Gets the reverse iterator at the end.
		/// @return The iterator object.
		inline riterator_t rend()
		{
			return STD::rend();
		}
		/// @brief Gets the reverse iterator at the end.
		/// @return The iterator object.
		inline const_riterator_t rend() const
		{
			return STD::rend();
		}
		/// @brief Compares the contents of two Containers for being equal.
		/// @param[in] other Another Container.
		/// @return True if number of elements are equal and all pairs of elements at the same positions are equal.
		inline bool equals(const Container& other) const
		{
			int size = this->size();
			if (size != other.size())
			{
				return false;
			}
			for_iter (i, 0, size)
			{
				// making sure operator== is used, not !=
				if (!(this->at(i) == other.at(i)))
				{
					return false;
				}
			}
			return true;
		}
		/// @brief Compares the contents of two Containers for being not equal.
		/// @param[in] other Another Container.
		/// @return True if number of elements are not equal or at least one pair of elements at the same positions is not equal.
		inline bool nequals(const Container& other) const
		{
			int size = this->size();
			if (size != other.size())
			{
				return true;
			}
			for_iter (i, 0, size)
			{
				// making sure operator!= is used, not ==
				if (this->at(i) != other.at(i))
				{
					return true;
				}
			}
			return false;
		}
		/// @brief Returns element at specified position.
		/// @param[in] index Index of the element.
		/// @return Element at specified position.
		/// @note This does not support bool.
		inline T& at(int index)
		{
			int size = this->size();
			if (index < 0)
			{
				index += size;
			}
			if (index < 0 || index >= size)
			{
				throw ContainerIndexException(index);
			}
			return *this->_itAdvance(STD::begin(), index);
		}
		/// @brief Returns element at specified position.
		/// @param[in] index Index of the element.
		/// @return Element at specified position.
		/// @note This does not support bool.
		inline const T& at(int index) const
		{
			int size = this->size();
			if (index < 0)
			{
				index += size;
			}
			if (index < 0 || index >= size)
			{
				throw ContainerIndexException(index);
			}
			return *this->_itAdvance(STD::begin(), index);
		}
		/// @brief Accesses first element of Container.
		/// @return The first element.
		inline T& first()
		{
			return STD::front();
		}
		/// @brief Accesses last element of Container.
		/// @return The last element.
		inline T& last()
		{
			return STD::back();
		}
		/// @brief Gets index of the given element.
		/// @param[in] element Element to search for.
		/// @return Index of the given element or -1 if element could not be found.
		inline int indexOf(const T& element) const
		{
			for_iter (i, 0, this->size())
			{
				if (element == this->at(i))
				{
					return i;
				}
			}
			return -1;
		}
		/// @brief Checks existence of element in Container.
		/// @param[in] element Element to search for.
		/// @return True if element is in Container.
		inline bool has(const T& element) const
		{
			return (this->indexOf(element) >= 0);
		}
		/// @brief Checks existence of elements in Container.
		/// @param[in] other Container with elements to search for.
		/// @return True if all elements are in Container.
		inline bool has(const Container& other) const
		{
			int size = other.size();
			for_iter (i, 0, size)
			{
				if (this->indexOf(other.at(i)) < 0)
				{
					return false;
				}
			}
			return true;
		}
		/// @brief Checks existence of elements in Container.
		/// @param[in] other C-type array with elements to search for.
		/// @param[in] count How many elements the C-type array has.
		/// @return True if all elements are in Container.
		inline bool has(const T other[], int count) const
		{
			for_iter (i, 0, count)
			{
				if (this->indexOf(other[i]) < 0)
				{
					return false;
				}
			}
			return true;
		}
		/// @brief Counts occurrences of element in Container.
		/// @param[in] element Element to search for.
		/// @return Number of occurrences of given element.
		inline int count(T element) const
		{
			int result = 0;
			int size = this->size();
			for_iter (i, 0, size)
			{
				if (element == this->at(i))
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
		inline void insertAt(const int index, const T& element, const int times = 1)
		{
			if (index < 0 || index > this->size())
			{
				throw ContainerIndexException(index);
			}
			STD::insert(this->_itAdvance(STD::begin(), index), times, element);
		}
		/// @brief Inserts all elements of another Container into this one.
		/// @param[in] index Position where to insert the new elements.
		/// @param[in] other Container of elements to insert.
		inline void insertAt(const int index, const Container& other)
		{
			if (index < 0 || index > this->size())
			{
				throw ContainerIndexException(index);
			}
			STD::insert(this->_itAdvance(STD::begin(), index), other.begin(), other.end());
		}
		/// @brief Inserts all elements of another Container into this one.
		/// @param[in] index Position where to insert the new elements.
		/// @param[in] other Container of elements to insert.
		/// @param[in] count Number of elements to insert.
		inline void insertAt(const int index, const Container& other, const int count)
		{
			if (index < 0 || index > this->size())
			{
				throw ContainerIndexException(index);
			}
			if (count > other.size())
			{
				throw ContainerRangeException(0, count);
			}
			const_iterator_t it = other.begin();
			STD::insert(this->_itAdvance(STD::begin(), index), it, this->_itAdvance(it, count));
		}
		/// @brief Inserts all elements of another Container into this one.
		/// @param[in] index Position where to insert the new elements.
		/// @param[in] other Container of elements to insert.
		/// @param[in] start Start index of the elements to insert.
		/// @param[in] count Number of elements to insert.
		inline void insertAt(const int index, const Container& other, const int start, const int count)
		{
			if (index < 0 || index > this->size())
			{
				throw ContainerIndexException(index);
			}
			if (start < 0 || start >= other.size() || start + count > other.size())
			{
				throw ContainerRangeException(start, count);
			}
			const_iterator_t it = this->_itAdvance(other.begin(), start);
			STD::insert(this->_itAdvance(STD::begin(), index), it, this->_itAdvance(it, count));
		}
		/// @brief Inserts all elements of a C-type array into this Container.
		/// @param[in] index Position where to insert the new elements.
		/// @param[in] other C-type array of elements to insert.
		/// @param[in] count Number of elements to insert.
		inline void insertAt(const int index, const T other[], const int count)
		{
			STD::insert(this->_itAdvance(STD::begin(), index), other, other + count);
		}
		/// @brief Inserts all elements of a C-type array into this Container.
		/// @param[in] index Position where to insert the new elements.
		/// @param[in] other C-type array of elements to insert.
		/// @param[in] start Start index of the elements to insert.
		/// @param[in] count Number of elements to insert.
		inline void insertAt(const int index, const T other[], const int start, const int count)
		{
			STD::insert(this->_itAdvance(STD::begin(), index), other + start, other + (start + count));
		}
		/// @brief Adds element at the end of Container.
		/// @param[in] element Element to add.
		inline void add(const T& element)
		{
			STD::push_back(element);
		}
		/// @brief Adds element at the end of Container n times.
		/// @param[in] element Element to add.
		/// @param[in] times Number of times to add the element.
		inline void add(const T& element, int times)
		{
			this->insertAt(this->size(), element, times);
		}
		/// @brief Adds all elements from another Container at the end of this one.
		/// @param[in] other Container of elements to add.
		inline void add(const Container& other)
		{
			this->insertAt(this->size(), other);
		}
		/// @brief Adds all elements from another Container at the end of this one.
		/// @param[in] other Container of elements to add.
		/// @param[in] count Number of elements to add.
		inline void add(const Container& other, const int count)
		{
			this->insertAt(this->size(), other, count);
		}
		/// @brief Adds all elements from another Container at the end of this one.
		/// @param[in] other Container of elements to add.
		/// @param[in] start Start index of the elements to add.
		/// @param[in] count Number of elements to add.
		inline void add(const Container& other, const int start, const int count)
		{
			this->insertAt(this->size(), other, start, count);
		}
		/// @brief Adds all elements from a C-type array at the end of Container.
		/// @param[in] other C-type array of elements to add.
		/// @param[in] count Number of elements to add.
		inline void add(const T other[], const int count)
		{
			this->insertAt(this->size(), other, count);
		}
		/// @brief Adds all elements from a C-type array at the end of Container.
		/// @param[in] other C-type array of elements to add.
		/// @param[in] start Start index of the elements to add.
		/// @param[in] count Number of elements to add.
		inline void add(const T other[], const int start, const int count)
		{
			this->insertAt(this->size(), other, start, count);
		}
		/// @brief Adds element at the beginning of Container n times.
		/// @param[in] element Element to add.
		/// @param[in] times Number of times to add the element.
		inline void addFirst(const T& element, int times = 1)
		{
			this->insertAt(0, element, times);
		}
		/// @brief Adds all elements from another Container at the beginning of this one.
		/// @param[in] other Container of elements to add.
		inline void addFirst(const Container& other)
		{
			this->insertAt(0, other);
		}
		/// @brief Adds all elements from another Container at the beginning of this one.
		/// @param[in] other Container of elements to add.
		/// @param[in] count Number of elements to add.
		inline void addFirst(const Container& other, const int count)
		{
			this->insertAt(0, other, count);
		}
		/// @brief Adds all elements from another Container at the beginning of this one.
		/// @param[in] other Container of elements to add.
		/// @param[in] start Start index of the elements to add.
		/// @param[in] count Number of elements to add.
		inline void addFirst(const Container& other, const int start, const int count)
		{
			this->insertAt(0, other, start, count);
		}
		/// @brief Adds all elements from a C-type array at the beginning of Container.
		/// @param[in] other C-type array of elements to add.
		/// @param[in] count Number of elements to add.
		inline void addFirst(const T other[], const int count)
		{
			this->insertAt(0, other, count);
		}
		/// @brief Adds all elements from a C-type array at the beginning of Container.
		/// @param[in] other C-type array of elements to add.
		/// @param[in] start Start index of the elements to add.
		/// @param[in] count Number of elements to add.
		inline void addFirst(const T other[], const int start, const int count)
		{
			this->insertAt(0, other, start, count);
		}
		/// @brief Removes element at given index.
		/// @param[in] index Index of element to remove.
		/// @return The removed element.
		inline T removeAt(int index)
		{
			int size = this->size();
			if (index < 0)
			{
				index -= size;
			}
			if (index < 0 || index >= size)
			{
				throw ContainerIndexException(index);
			}
			iterator_t it = this->_itAdvance(STD::begin(), index);
			T result = (*it);
			STD::erase(it);
			return result;
		}
		/// @brief Removes first occurrence of element in Container.
		/// @param[in] element Element to remove.
		inline void remove(T element)
		{
			int index = this->indexOf(element);
			if (index < 0)
			{
				throw ContainerElementNotFoundException();
			}
			STD::erase(this->_itAdvance(STD::begin(), index));
		}
		/// @brief Removes first occurrence of each element in another Container from this one.
		/// @param[in] other Container of elements to remove.
		inline void remove(const Container& other)
		{
			int size = other.size();
			int index = 0;
			for_iter (i, 0, size)
			{
				index = this->indexOf(other.at(i));
				if (index < 0)
				{
					throw ContainerElementNotFoundException();
				}
				STD::erase(this->_itAdvance(STD::begin(), index));
			}
		}
		/// @brief Removes first element of Container.
		/// @return The removed element.
		inline T removeFirst()
		{
			return this->removeAt(0);
		}
		/// @brief Removes last element of Container.
		/// @return The removed element.
		inline T removeLast()
		{
			if (this->size() == 0)
			{
				throw ContainerIndexException(0);
			}
			T element = STD::back();
			STD::pop_back();
			return element;
		}
		/// @brief Gets a random element in Container and removes it.
		/// @return Random element.
		inline T removeRandom()
		{
			int size = this->size();
			if (size == 0)
			{
				throw ContainerEmptyException("removeRandom()");
			}
			int index = hrand(size);
			T result = this->at(index);
			this->removeAt(index);
			return result;
		}
		/// @brief Removes all occurrences of element in Container.
		/// @param[in] element Element to remove.
		/// @return Number of elements removed.
		inline int removeAll(const T& element)
		{
			Container<std::vector<int>, int> indexes = this->_indexesOf<Container<std::vector<int>, int> >(element);
			iterator_t it = STD::begin();
			int size = indexes.size();
			for_iter_r (i, size, 0)
			{
				STD::erase(this->_itAdvance(it, indexes.at(i)));
			}
			return size;
		}
		/// @brief Removes all occurrences of each element in another Container from this one.
		/// @param[in] other Container of elements to remove.
		/// @return Number of elements removed.
		inline int removeAll(const Container& other)
		{
			Container<std::vector<int>, int> indexes;
			iterator_t it;
			int indexesSize = 0;
			int count = 0;
			for_iter (i, 0, other.size()) // has to stay other.size() here
			{
				indexes = this->_indexesOf<Container<std::vector<int>, int> >(other.at(i));
				it = STD::begin();
				indexesSize = indexes.size();
				for_iter_r (j, indexesSize, 0)
				{
					STD::erase(this->_itAdvance(it, indexes.at(j)));
				}
				count += indexesSize;
			}
			return count;
		}
		/// @brief Finds minimum element in Container.
		/// @return Minimum Element.
		inline T min() const
		{
			if (this->size() == 0)
			{
				throw ContainerEmptyException("min()");
			}
			return (*std::min_element(STD::begin(), STD::end()));
		}
		/// @brief Finds minimum element in Container.
		/// @param[in] compareFunction Function pointer with comparison function that takes two elements of type T and returns bool.
		/// @return Minimum Element.
		/// @note compareFunction should return true if first element is less than second element.
		inline T min(bool (*compareFunction)(T, T)) const
		{
			if (this->size() == 0)
			{
				throw ContainerEmptyException("min()");
			}
			return (*std::min_element(STD::begin(), STD::end(), compareFunction));
		}
		/// @brief Finds maximum element in Container.
		/// @return Maximum Element.
		inline T max() const
		{
			if (this->size() == 0)
			{
				throw ContainerEmptyException("max()");
			}
			return (*std::max_element(STD::begin(), STD::end()));
		}
		/// @brief Finds maximum element in Container.
		/// @param[in] compareFunction Function pointer with comparison function that takes two elements of type T and returns bool.
		/// @return Maximum Element.
		/// @note compareFunction should return true if first element is greater than second element.
		inline T max(bool (*compareFunction)(T, T)) const
		{
			if (this->size() == 0)
			{
				throw ContainerEmptyException("max()");
			}
			return (*std::max_element(STD::begin(), STD::end(), compareFunction));
		}
		/// @brief Gets a random element in Container.
		/// @return Random element.
		inline T random() const
		{
			int size = this->size();
			if (size == 0)
			{
				throw ContainerEmptyException("random()");
			}
			return this->at(hrand(size));
		}
		/// @brief Reverses order of elements.
		inline void reverse()
		{
			if (this->size() > 0)
			{
				std::reverse(STD::begin(), STD::end());
			}
		}
		/// @brief Removes duplicates in Container.
		inline void removeDuplicates()
		{
			Container<std::vector<int>, int> indexes;
			iterator_t it = STD::begin();
			int indexesSize = 0;
			for_iter (i, 0, this->size()) // has to stay this->size() here
			{
				indexes = this->_indexesOf<Container<std::vector<int>, int> >(this->at(i));
				indexesSize = indexes.size();
				for_iter_r (j, indexesSize, 1)
				{
					STD::erase(this->_itAdvance(it, indexes.at(j)));
				}
			}
		}
		/// @brief Sorts elements in Container.
		/// @note The sorting order is ascending.
		inline void sort()
		{
			if (this->size() > 0)
			{
				std::stable_sort(STD::begin(), STD::end());
			}
		}
		/// @brief Sorts elements in Container.
		/// @param[in] compareFunction Function pointer with comparison function that takes two elements of type T and returns bool.
		/// @note The sorting order is ascending.
		/// @note compareFunction should return true if first element is less than the second element.
		inline void sort(bool (*compareFunction)(T, T))
		{
			if (this->size() > 0)
			{
				std::stable_sort(STD::begin(), STD::end(), compareFunction);
			}
		}
		/// @brief Randomizes order of elements in Container.
		inline void randomize()
		{
			std::random_shuffle(STD::begin(), STD::end());
		}
		/// @brief Unites elements of this Container with an element.
		/// @param[in] element Element to unite with.
		/// @note Removes duplicates.
		inline void unite(const T& element)
		{
			this->insertAt(this->size(), element);
			this->removeDuplicates();
		}
		/// @brief Unites elements of this Container with another one.
		/// @param[in] other Container to unite with.
		/// @note Removes duplicates.
		inline void unite(const Container& other)
		{
			this->insertAt(this->size(), other);
			this->removeDuplicates();
		}
		/// @brief Intersects elements of this Container with another one.
		/// @param[in] other Container to intersect with.
		/// @note Does not remove duplicates.
		inline void intersect(const Container& other)
		{
			Container result;
			int size = this->size();
			for_iter (i, 0, size)
			{
				if (other.has(this->at(i)))
				{
					result.add(this->at(i));
				}
			}
			STD::assign(result.begin(), result.end());
		}
		/// @brief Differentiates elements of this Container with an element.
		/// @param[in] other Element to differentiate with.
		/// @note Unlike remove, this method ignores if the element is not in this Container.
		/// @note Does not remove duplicates.
		inline void differentiate(const T& element)
		{
			int index = 0;
			while (true)
			{
				index = this->indexOf(element);
				if (index < 0)
				{
					break;
				}
				STD::erase(this->_itAdvance(STD::begin(), index));
			}
		}
		/// @brief Differentiates elements of this Container with another one.
		/// @param[in] other Container to differentiate with.
		/// @note Unlike remove, this method ignores elements of other Container that are not in this one.
		/// @note Does not remove duplicates.
		inline void differentiate(const Container& other)
		{
			int index = 0;
			int size = other.size();
			for_iter (i, 0, size)
			{
				while (true)
				{
					index = this->indexOf(other.at(i));
					if (index < 0)
					{
						break;
					}
					STD::erase(this->_itAdvance(STD::begin(), index));
				}
			}
		}
		/// @brief Joins all elements into a string.
		/// @param[in] separator Separator string between elements.
		/// @return String or joined elements separater by separator string.
		/// @note Make sure your elements can be cast into String or are already String.
		inline String joined(const String& separator) const
		{
			String result;
			int size = this->size();
			if (size > 0)
			{
				result += String(this->at(0));
				for_iter (i, 1, size)
				{
					result += separator + String(this->at(i));
				}
			}
			return result;
		}
		/// @brief Finds and returns first occurrence of element that matches the condition.
		/// @param[in] conditionFunction Function pointer with condition function that takes one element of type T and returns bool.
		/// @return Pointer to element that matches the condition or NULL if no element was found.
		inline T* findFirst(bool (*conditionFunction)(T))
		{
			int size = this->size();
			for_iter (i, 0, size)
			{
				if (conditionFunction(this->at(i)))
				{
					return &this->at(i);
				}
			}
			return NULL;
		}
		/// @brief Checks if at least one element matches the condition.
		/// @param[in] conditionFunction Function pointer with condition function that takes one element of type T and returns bool.
		/// @return True if at least one element matches the condition.
		inline bool matchesAny(bool (*conditionFunction)(T))
		{
			int size = this->size();
			for_iter (i, 0, size)
			{
				if (conditionFunction(this->at(i)))
				{
					return true;
				}
			}
			return false;
		}
		/// @brief Checks if all elements match the condition.
		/// @param[in] conditionFunction Function pointer with condition function that takes one element of type T and returns bool.
		/// @return True if all elements match the condition.
		inline bool matchesAll(bool (*conditionFunction)(T))
		{
			int size = this->size();
			for_iter (i, 0, size)
			{
				if (!conditionFunction(this->at(i)))
				{
					return false;
				}
			}
			return true;
		}

		// DEPRECATED
		DEPRECATED_ATTRIBUTE inline T& front()																					{ return this->first(); }
		DEPRECATED_ATTRIBUTE inline T& back()																					{ return this->last(); }
		DEPRECATED_ATTRIBUTE inline int index_of(const T& element) const														{ return this->indexOf(element); }
		DEPRECATED_ATTRIBUTE inline void insert_at(const int index, const T& element, const int times = 1)						{ this->insertAt(index, element, times); }
		DEPRECATED_ATTRIBUTE inline void insert_at(const int index, const Container& other)										{ this->insertAt(index, other); }
		DEPRECATED_ATTRIBUTE inline void insert_at(const int index, const Container& other, const int count)					{ this->insertAt(index, other, count); }
		DEPRECATED_ATTRIBUTE inline void insert_at(const int index, const Container& other, const int start, const int count)	{ this->insertAt(index, other, start, count); }
		DEPRECATED_ATTRIBUTE inline void insert_at(const int index, const T other[], const int count)							{ this->insertAt(index, other, count); }
		DEPRECATED_ATTRIBUTE inline void insert_at(const int index, const T other[], const int start, const int count)			{ this->insertAt(index, other, start, count); }
		DEPRECATED_ATTRIBUTE inline void push_front(const T& element, int times = 1)											{ this->addFirst(element, times); }
		DEPRECATED_ATTRIBUTE inline void push_front(const Container& other)														{ this->addFirst(other); }
		DEPRECATED_ATTRIBUTE inline void push_front(const Container& other, const int count)									{ this->addFirst(other, count); }
		DEPRECATED_ATTRIBUTE inline void push_front(const Container& other, const int start, const int count)					{ this->addFirst(other, start, count); }
		DEPRECATED_ATTRIBUTE inline void push_front(const T other[], const int count)											{ this->addFirst(other, count); }
		DEPRECATED_ATTRIBUTE inline void push_front(const T other[], const int start, const int count)							{ this->addFirst(other, start, count); }
		DEPRECATED_ATTRIBUTE inline void push_back(const T& element)															{ this->add(element); }
		DEPRECATED_ATTRIBUTE inline void push_back(const T& element, int times)													{ this->add(element, times); }
		DEPRECATED_ATTRIBUTE inline void push_back(const Container& other)														{ this->add(other); }
		DEPRECATED_ATTRIBUTE inline void push_back(const Container& other, const int count)										{ this->add(other, count); }
		DEPRECATED_ATTRIBUTE inline void push_back(const Container& other, const int start, const int count)					{ this->add(other, start, count); }
		DEPRECATED_ATTRIBUTE inline void push_back(const T other[], const int count)											{ this->add(other, count); }
		DEPRECATED_ATTRIBUTE inline void push_back(const T other[], const int start, const int count)							{ this->add(other, start, count); }
		DEPRECATED_ATTRIBUTE inline void push_first(const T& element, int times = 1)											{ this->addFirst(element, times); }
		DEPRECATED_ATTRIBUTE inline void push_first(const Container& other)														{ this->addFirst(other); }
		DEPRECATED_ATTRIBUTE inline void push_first(const Container& other, const int count)									{ this->addFirst(other, count); }
		DEPRECATED_ATTRIBUTE inline void push_first(const Container& other, const int start, const int count)					{ this->addFirst(other, start, count); }
		DEPRECATED_ATTRIBUTE inline void push_first(const T other[], const int count)											{ this->addFirst(other, count); }
		DEPRECATED_ATTRIBUTE inline void push_first(const T other[], const int start, const int count)							{ this->addFirst(other, start, count); }
		DEPRECATED_ATTRIBUTE inline void push_last(const T& element)															{ this->add(element); }
		DEPRECATED_ATTRIBUTE inline void push_last(const T& element, int times)													{ this->add(element, times); }
		DEPRECATED_ATTRIBUTE inline void push_last(const Container& other)														{ this->add(other); }
		DEPRECATED_ATTRIBUTE inline void push_last(const Container& other, const int count)										{ this->add(other, count); }
		DEPRECATED_ATTRIBUTE inline void push_last(const Container& other, const int start, const int count)					{ this->add(other, start, count); }
		DEPRECATED_ATTRIBUTE inline void push_last(const T other[], const int count)											{ this->add(other, count); }
		DEPRECATED_ATTRIBUTE inline void push_last(const T other[], const int start, const int count)							{ this->add(other, start, count); }
		DEPRECATED_ATTRIBUTE inline int remove_all(const T& element)															{ return this->removeAll(element); }
		DEPRECATED_ATTRIBUTE inline int remove_all(const Container& other)														{ return this->removeAll(other); }
		DEPRECATED_ATTRIBUTE inline void remove_duplicates()																	{ return this->removeDuplicates(); }
		DEPRECATED_ATTRIBUTE inline String join(const String& separator) const													{ return this->joined(separator); }
		DEPRECATED_ATTRIBUTE inline T* find_first(bool (*conditionFunction)(T)) const											{ return this->findFirst(conditionFunction); }
		DEPRECATED_ATTRIBUTE inline bool matches_any(bool (*conditionFunction)(T)) const										{ return this->matchesAny(conditionFunction); }
		DEPRECATED_ATTRIBUTE inline bool matches_all(bool (*conditionFunction)(T)) const										{ return this->matchesAll(conditionFunction); }

		DEPRECATED_ATTRIBUTE inline bool includes(const T& element) const														{ return this->has(element); }
		DEPRECATED_ATTRIBUTE inline bool includes(const Container& other) const													{ return this->has(other); }
		DEPRECATED_ATTRIBUTE inline bool includes(const T other[], int count) const												{ return this->has(other, count); }
		DEPRECATED_ATTRIBUTE inline bool contains(const T& element) const														{ return this->has(element); }
		DEPRECATED_ATTRIBUTE inline bool contains(const Container& other) const													{ return this->has(other); }
		DEPRECATED_ATTRIBUTE inline bool contains(const T other[], int count) const												{ return this->has(other, count); }
		DEPRECATED_ATTRIBUTE inline bool has_element(const T& element) const													{ return this->has(element); }
		DEPRECATED_ATTRIBUTE inline bool has_element(const Container& other) const												{ return this->has(other); }
		DEPRECATED_ATTRIBUTE inline bool has_element(const T other[], int count) const											{ return this->has(other, count); }
		DEPRECATED_ATTRIBUTE inline void append(const T& element)																{ this->add(element); }
		DEPRECATED_ATTRIBUTE inline void append(const T& element, int times)													{ this->add(element, times); }
		DEPRECATED_ATTRIBUTE inline void append(const Container& other)															{ this->add(other); }
		DEPRECATED_ATTRIBUTE inline void append(const Container& other, const int count)										{ this->add(other, count); }
		DEPRECATED_ATTRIBUTE inline void append(const Container& other, const int start, const int count)						{ this->add(other, start, count); }
		DEPRECATED_ATTRIBUTE inline void append(const T other[], const int count)												{ this->add(other, count); }
		DEPRECATED_ATTRIBUTE inline void append(const T other[], const int start, const int count)								{ this->add(other, start, count); }

	protected:
		/// @brief Gets all indexes of the given element.
		/// @param[in] element Element to search for.
		/// @return All indexes of the given element.
		template <class R>
		inline R _indexesOf(const T& element) const
		{
			R result;
			int size = this->size();
			for_iter (i, 0, size)
			{
				if (element == this->at(i))
				{
					result.add(i);
				}
			}
			return result;
		}
		/// @brief Returns a subarray of elements.
		/// @param[in] start Start index of the elements to copy.
		/// @param[in] count Number of elements to copy.
		/// @return Subarray created from the current Container.
		template <class R>
		inline R _sub(int start, int count) const
		{
			R result;
			if (count > 0)
			{
				int size = this->size();
				if (start < 0)
				{
					start += size;
				}
				if (start < 0 || start >= size || start + count > size)
				{
					throw ContainerRangeException(start, count);
				}
				const_iterator_t it = this->_itAdvance(STD::begin(), start);
				result.assign(it, this->_itAdvance(it, count));
			}
			return result;
		}
		/// @brief Removes n elements at given index of Container.
		/// @param[in] index Start index of elements to remove.
		/// @param[in] count Number of elements to remove.
		/// @return Container of all removed elements.
		/// @note Elements in the returned Container are in the same order as in the orignal Container.
		template <class R>
		inline R _removeAt(int index, int count)
		{
			int size = this->size();
			if (index < 0)
			{
				index -= size;
			}
			if (index < 0 || index >= size || index + count > size)
			{
				throw ContainerRangeException(index, count);
			}
			R result;
			iterator_t it = STD::begin();
			iterator_t begin = this->_itAdvance(it, index);
			iterator_t end = this->_itAdvance(it, index + count);
			result.assign(begin, end);
			STD::erase(begin, end);
			return result;
		}
		/// @brief Removes n elements from the beginning of Container.
		/// @param[in] count Number of elements to remove.
		/// @return Container of all removed elements.
		/// @note Elements in the returned Container are in the same order as in the orignal Container.
		template <class R>
		inline R _removeFirst(const int count)
		{
			if (count > this->size())
			{
				throw ContainerRangeException(0, count);
			}
			R result;
			iterator_t begin = STD::begin();
			iterator_t end = this->_itAdvance(begin, count);
			result.assign(begin, end);
			STD::erase(begin, end);
			return result;
		}
		/// @brief Removes n elements from the end of Container.
		/// @param[in] count Number of elements to remove.
		/// @return Container of all removed elements.
		/// @note Elements in the returned Container are in the same order as in the orignal Container.
		template <class R>
		inline R _removeLast(const int count)
		{
			if (count > this->size())
			{
				throw ContainerRangeException(0, count);
			}
			R result;
			iterator_t end = STD::end();
			iterator_t begin = this->_itAdvance(end, -count);
			result.assign(begin, end);
			STD::erase(begin, end);
			return result;
		}
		/// @brief Gets an Container of random elements selected from this one and removes them.
		/// @param[in] count Number of random elements.
		/// @return Container of random elements selected from this one.
		template <class R>
		inline R _removeRandom(const int count)
		{
			R result = this->_random(count);
			this->remove(result);
			return result;
		}
		/// @brief Gets an Container of random elements selected from this one.
		/// @param[in] count Number of random elements.
		/// @param[in] unique Whether to force all random values to be at unique positions.
		/// @return Container of random elements selected from this one.
		template <class R>
		inline R _random(int count, bool unique = true) const
		{
			R result;
			int size = this->size();
			if (!unique)
			{
				for_iter (i, 0, count)
				{
					result.add(this->at(hrand(size)));
				}
			}
			else if (count > 0)
			{
				if (count > size)
				{
					throw ContainerRangeException(0, count);
				}
				if (count == size)
				{
					return this->randomized();
				}
				Container<std::vector<int>, int> indexes;
				for_iter (i, 0, size)
				{
					indexes.add(i);
				}
				for_iter (i, 0, count)
				{
					result.add(this->at(indexes.removeAt(hrand(indexes.size()))));
				}
			}
			return result;
		}
		/// @brief Creates new Container with reversed order of elements.
		/// @return A new Container.
		template <class R>
		inline R _reversed() const
		{
			R result(*this);
			result.reverse();
			return result;
		}
		/// @brief Creates new Container without duplicates.
		/// @return A new Container.
		template <class R>
		inline R _removedDuplicates() const
		{
			R result(*this);
			result.removeDuplicates();
			return result;
		}
		/// @brief Creates new sorted Container.
		/// @return A new Container.
		/// @note The sorting order is ascending.
		template <class R>
		inline R _sorted() const
		{
			R result(*this);
			result.sort();
			return result;
		}
		/// @brief Creates new sorted Container.
		/// @param[in] compareFunction Function pointer with comparison function that takes two elements of type T and returns bool.
		/// @return A new Container.
		/// @note The sorting order is ascending.
		/// @note compareFunction should return true if first element is less than the second element.
		template <class R>
		inline R _sorted(bool(*compareFunction)(T, T)) const
		{
			R result(*this);
			result.sort(compareFunction);
			return result;
		}
		/// @brief Creates a new Container with randomized order of elements.
		/// @return A new Container.
		template <class R>
		inline R _randomized() const
		{
			R result(*this);
			result.randomize();
			return result;
		}
		/// @brief Creates a new Container as union of this Container with an element.
		/// @param[in] element Element to unite with.
		/// @return A new Container.
		/// @note Removes duplicates.
		template <class R>
		inline R _united(const T& element) const
		{
			R result(*this);
			result.unite(element);
			return result;
		}
		/// @brief Creates a new Container as union of this Container with another one.
		/// @param[in] other Container to unite with.
		/// @return A new Container.
		/// @note Removes duplicates.
		template <class R>
		inline R _united(const R& other) const
		{
			R result(*this);
			result.unite(other);
			return result;
		}
		/// @brief Creates a new Container as intersection of this Container with another one.
		/// @param[in] other Container to intersect with.
		/// @return A new Container.
		/// @note Does not remove duplicates.
		template <class R>
		inline R _intersected(const R& other) const
		{
			R result(*this);
			result.intersect(other);
			return result;
		}
		/// @brief Creates a new Container as difference of this Container with an element.
		/// @param[in] other Element to differentiate with.
		/// @return A new Container.
		/// @note Unlike remove, this method ignores if the element is not in this Container.
		/// @note Does not remove duplicates.
		template <class R>
		inline R _differentiated(const T& element) const
		{
			R result(*this);
			result.differentiate(element);
			return result;
		}
		/// @brief Creates a new Container as difference of this Container with another one.
		/// @param[in] other Container to differentiate with.
		/// @return A new Container.
		/// @note Unlike remove, this method ignore elements of other Container that are not in this one.
		/// @note Does not remove duplicates.
		template <class R>
		inline R _differentiated(const R& other) const
		{
			R result(*this);
			result.differentiate(other);
			return result;
		}
		/// @brief Finds and returns new Container of elements that match the condition.
		/// @param[in] conditionFunction Function pointer with condition function that takes one element of type T and returns bool.
		/// @return New Container with all matching elements.
		template <class R>
		inline R _findAll(bool (*conditionFunction)(T)) const
		{
			R result;
			int size = this->size();
			for_iter (i, 0, size)
			{
				if (conditionFunction(this->at(i)))
				{
					result.add(this->at(i));
				}
			}
			return result;
		}
		/// @brief Returns a new Container with all elements cast into type S.
		/// @return A new Container with all elements cast into type S.
		/// @note Make sure all elements in the Container can be cast into type S.
		template <class R, class S>
		inline R _cast() const
		{
			R result;
			int size = this->size();
			for_iter (i, 0, size)
			{
				result.add((S)this->at(i));
			}
			return result;
		}
		/// @brief Returns a new Container with all elements dynamically cast into type S.
		/// @param[in] includeNulls Whether to include NULLs that failed to cast.
		/// @return A new Container with all elements cast into type S.
		/// @note Be careful not to use this function with non-pointers and classes that don't have virtual functions.
		template <class R, class S>
		inline R _dynamicCast(bool includeNulls = false) const
		{
			R result;
			S value;
			int size = this->size();
			for_iter (i, 0, size)
			{
				// when seeing "dynamic_cast", I always think of fireballs
				value = dynamic_cast<S>(this->at(i));
				if (value != NULL || includeNulls)
				{
					result.add(value);
				}
			}
			return result;
		}

	private:
		/// @brief Moves iterator forward/backward by a number of elements.
		/// @param[in] it Current iterator.
		/// @param[in] count Number of elements to move.
		/// @return Moved iterator.
		/// @note This is an internal utility function to make code easier to read.
		inline iterator_t _itAdvance(iterator_t it, int count)
		{
			std::advance(it, count);
			return it;
		}
		/// @brief Moves const iterator forward/backward by a number of elements.
		/// @param[in] it Current const iterator.
		/// @param[in] count Number of elements to move.
		/// @return Moved const iterator.
		/// @note This is an internal utility function to make code easier to read.
		inline const_iterator_t _itAdvance(const_iterator_t it, int count) const
		{
			std::advance(it, count);
			return it;
		}

	};

}

#endif
