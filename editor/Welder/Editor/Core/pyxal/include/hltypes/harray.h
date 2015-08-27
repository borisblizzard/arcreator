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
/// Encapsulates std::vector and adds high level methods.

#ifndef HLTYPES_ARRAY_H
#define HLTYPES_ARRAY_H

#include <vector>

#include "hcontainer.h"
#include "hexception.h"
#include "hltypesUtil.h"
#include "hstring.h"

/// @brief Provides a simpler syntax to iterate through an Array.
#define foreach(type, name, container) for (harray< type >::iterator_t name = (container).begin(); name != (container).end(); ++name)
#define foreachc(type, name, container) for (harray< type >::const_iterator_t name = (container).begin(); name != (container).end(); ++name)
/// @brief Provides a simpler syntax to reverse iterate through an Array.
#define foreach_r(type, name, container) for (harray< type >::riterator_t name = (container).rbegin(); name != (container).rend(); ++name)
#define foreachc_r(type, name, container) for (harray< type >::const_riterator_t name = (container).rbegin(); name != (container).rend(); ++name)

namespace hltypes
{
	/// @brief Encapsulates std::vector and adds high level methods.
	template <class T>
	class Array : public Container<std::vector<T>, T>
	{
	public:
		/// @brief Empty constructor.
		inline Array() : Container<std::vector<T>, T>()
		{
		}
		/// @brief Copy constructor.
		/// @param[in] other Container to copy.
		inline Array(const Container<std::vector<T>, T>& other) : Container<std::vector<T>, T>(other)
		{
		}
		/// @brief Constructor from single element.
		/// @param[in] element Element to insert.
		inline Array(const T& element) : Container<std::vector<T>, T>(element)
		{
		}
		/// @brief Constructor from single element.
		/// @param[in] element Element to insert.
		/// @param[in] times Number of times to insert element.
		inline Array(const T& element, int times) : Container<std::vector<T>, T>(element, times)
		{
		}
		/// @brief Constructor from another Container.
		/// @param[in] other Container to copy.
		/// @param[in] count Number of elements to copy.
		inline Array(const Container<std::vector<T>, T>& other, const int count) : Container<std::vector<T>, T>(other, count)
		{
		}
		/// @brief Constructor from another Container.
		/// @param[in] other Container to copy.
		/// @param[in] start Start index of elements to copy.
		/// @param[in] count Number of elements to copy.
		inline Array(const Container<std::vector<T>, T>& other, const int start, const int count) : Container<std::vector<T>, T>(other, start, count)
		{
		}
		/// @brief Constructor from C-type array.
		/// @param[in] other C-type array to copy.
		/// @param[in] count Number of elements to copy.
		inline Array(const T other[], const int count) : Container<std::vector<T>, T>(other, count)
		{
		}
		/// @brief Constructor from C-type array.
		/// @param[in] other C-type array to copy.
		/// @param[in] start Start index of elements to copy.
		/// @param[in] count Number of elements to copy.
		inline Array(const T other[], const int start, const int count) : Container<std::vector<T>, T>(other, start, count)
		{
		}
		/// @brief Destructor.
		inline ~Array()
		{
		}
		/// @brief Gets all indexes of the given element.
		/// @param[in] element Element to search for.
		/// @return All indexes of the given element.
		inline Array<int> indexesOf(const T& element) const
		{
			return this->template _indexesOf<Array<int> >(element);
		}
		/// @brief Removes element at given index.
		/// @param[in] index Index of element to remove.
		/// @return The removed element.
		inline T removeAt(int index)
		{
			return Container<std::vector<T>, T>::removeAt(index);
		}
		/// @brief Removes n elements at given index of Array.
		/// @param[in] index Start index of elements to remove.
		/// @param[in] count Number of elements to remove.
		/// @return Array of all removed elements.
		/// @note Elements in the returned Array are in the same order as in the orignal Array.
		inline Array<T> removeAt(int index, int count)
		{
			return this->template _removeAt<Array<T> >(index, count);
		}
		/// @brief Removes first element of Array.
		/// @return The removed element.
		inline T removeFirst()
		{
			return Container<std::vector<T>, T>::removeFirst();
		}
		/// @brief Removes n elements from the beginning of Array.
		/// @param[in] count Number of elements to remove.
		/// @return Array of all removed elements.
		/// @note Elements in the returned Array are in the same order as in the orignal Array.
		inline Array<T> removeFirst(const int count)
		{
			return this->template _removeFirst<Array<T> >(count);
		}
		/// @brief Removes last element of Array.
		/// @return The removed element.
		inline T removeLast()
		{
			return Container<std::vector<T>, T>::removeLast();
		}
		/// @brief Removes n elements from the end of Array.
		/// @param[in] count Number of elements to remove.
		/// @return Array of all removed elements.
		/// @note Elements in the returned Array are in the same order as in the orignal Array.
		inline Array<T> removeLast(const int count)
		{
			return this->template _removeLast<Array<T> >(count);
		}
		/// @brief Gets a random element in Array and removes it.
		/// @return Random element.
		inline T removeRandom()
		{
			return Container<std::vector<T>, T>::removeRandom();
		}
		/// @brief Gets an Array of random elements selected from this one and removes them.
		/// @param[in] count Number of random elements.
		/// @param[in] unique Whether to force all random values to be unique.
		/// @return Array of random elements selected from this one.
		inline Array<T> removeRandom(const int count)
		{
			return this->template _removeRandom<Array<T> >(count);
		}
		/// @brief Gets a random element in Array.
		/// @return Random element.
		inline T random() const
		{
			return Container<std::vector<T>, T>::random();
		}
		/// @brief Gets an Array of random elements selected from this one.
		/// @param[in] count Number of random elements.
		/// @param[in] unique Whether to force all random values to be at unique positions.
		/// @return Array of random elements selected from this one.
		inline Array<T> random(int count, bool unique = true)
		{
			return this->template _random<Array<T> >(count, unique);
		}
		/// @brief Creates new Array with reversed order of elements.
		/// @return A new Array.
		inline Array<T> reversed() const
		{
			return this->template _reversed<Array<T> >();
		}
		/// @brief Creates new Array without duplicates.
		/// @return A new Array.
		inline Array<T> removedDuplicates() const
		{
			return this->template _removedDuplicates<Array<T> >();
		}
		/// @brief Creates new sorted Array.
		/// @return A new Array.
		/// @note The sorting order is ascending.
		inline Array<T> sorted() const
		{
			return this->template _sorted<Array<T> >();
		}
		/// @brief Creates new sorted Array.
		/// @param[in] compareFunction Function pointer with comparison function that takes two elements of type T and returns bool.
		/// @return A new Array.
		/// @note The sorting order is ascending.
		/// @note compareFunction should return true if first element is less than the second element.
		inline Array<T> sorted(bool(*compareFunction)(T, T)) const
		{
			return this->template _sorted<Array<T> >(compareFunction);
		}
		/// @brief Creates a new Array with randomized order of elements.
		/// @return A new Array.
		inline Array<T> randomized() const
		{
			return this->template _randomized<Array<T> >();
		}
		/// @brief Creates a new Array as union of this Array with an element.
		/// @param[in] element Element to unite with.
		/// @return A new Array.
		/// @note Removes duplicates.
		inline Array<T> united(const T& element) const
		{
			return this->template _united<Array<T> >(element);
		}
		/// @brief Creates a new Array as union of this Array with another one.
		/// @param[in] other Array to unite with.
		/// @return A new Array.
		/// @note Removes duplicates.
		inline Array<T> united(const Array<T>& other) const
		{
			return this->template _united<Array<T> >(other);
		}
		/// @brief Creates a new Array as intersection of this Array with another one.
		/// @param[in] other Array to intersect with.
		/// @return A new Array.
		/// @note Does not remove duplicates.
		inline Array<T> intersected(const Array<T>& other) const
		{
			return this->template _intersected<Array<T> >(other);
		}
		/// @brief Creates a new Array as difference of this Array with an element.
		/// @param[in] other Element to differentiate with.
		/// @return A new Array.
		/// @note Unlike remove, this method ignores if the element is not in this Array.
		/// @note Does not remove duplicates.
		inline Array<T> differentiated(const T& element) const
		{
			return this->template _differentiated<Array<T> >(element);
		}
		/// @brief Creates a new Array as difference of this Array with another one.
		/// @param[in] other Array to differentiate with.
		/// @return A new Array.
		/// @note Unlike remove, this method ignore elements of other Array that are not in this one.
		/// @note Does not remove duplicates.
		inline Array<T> differentiated(const Array<T>& other) const
		{
			return this->template _differentiated<Array<T> >(other);
		}
		/// @brief Finds and returns new Array of elements that match the condition.
		/// @param[in] conditionFunction Function pointer with condition function that takes one element of type T and returns bool.
		/// @return New Array with all matching elements.
		inline Array<T> findAll(bool (*conditionFunction)(T)) const
		{
			return this->template _findAll<Array<T> >(conditionFunction);
		}

		/// @brief Returns a new Array with all elements cast into type S.
		/// @return A new Array with all elements cast into type S.
		/// @note Make sure all elements in the Array can be cast into type S.
		template <class S>
		inline Array<S> cast() const
		{
			return this->template _cast<Array<S>, S>();
		}
		/// @brief Returns a new Array with all elements dynamically cast into type S.
		/// @param[in] includeNulls Whether to include NULLs that failed to cast.
		/// @return A new Array with all elements cast into type S.
		/// @note Be careful not to use this function with non-pointers and classes that don't have virtual functions.
		template <class S>
		inline Array<S> dynamicCast(bool includeNulls = false) const
		{
			return this->template _dynamicCast<Array<S>, S>(includeNulls);
		}
		/// @brief Returns element at specified position.
		/// @param[in] index Index of the element.
		/// @return Element at specified position.
		/// @note Does not work with bool as T.
		inline T& operator[](int index)
		{
			return this->at(index);
		}
		/// @brief Returns element at specified position.
		/// @param[in] index Index of the element.
		/// @return Element at specified position.
		/// @note Does not work with bool as T.
		inline const T& operator[](int index) const
		{
			return this->at(index);
		}
		/// @brief Returns a subarray.
		/// @param[in] start Start index of the elements to copy.
		/// @param[in] count Number of elements to copy.
		/// @return Subarray created from the current Array.
		inline Array<T> operator()(int start, const int count) const
		{
			return this->template _sub<Array<T> >(start, count);
		}
		/// @brief Same as equals.
		/// @see equals
		inline bool operator==(const Array<T>& other) const
		{
			return this->equals(other);
		}
		/// @brief Same as nequals.
		/// @see nequals
		inline bool operator!=(const Array<T>& other) const
		{
			return this->nequals(other);
		}
		/// @brief Same as add.
		/// @see add(const T& element)
		inline Array<T>& operator<<(const T& element)
		{
			this->add(element);
			return (*this);
		}
		/// @brief Same as add.
		/// @see add(const Array<T>& other)
		inline Array<T>& operator<<(const Array<T>& other)
		{
			this->add(other);
			return (*this);
		}
		/// @brief Same as add.
		/// @see add(const T& element)
		inline Array<T>& operator+=(const T& element)
		{
			this->add(element);
			return (*this);
		}
		/// @brief Same as add.
		/// @see add(const Array<T>& other)
		inline Array<T>& operator+=(const Array<T>& other)
		{
			this->add(other);
			return (*this);
		}
		/// @brief Same as remove.
		/// @see remove(T element)
		inline Array<T>& operator-=(T element)
		{
			this->remove(element);
			return (*this);
		}
		/// @brief Same as remove.
		/// @see remove(const Array<T>& other)
		inline Array<T>& operator-=(const Array<T>& other)
		{
			this->remove(other);
			return (*this);
		}
		/// @brief Same as unite.
		/// @see unite(const T& element)
		inline Array<T>& operator|=(const T& element)
		{
			this->unite(element);
			return (*this);
		}
		/// @brief Same as unite.
		/// @see unite(const Array<T>& other)
		inline Array<T>& operator|=(const Array<T>& other)
		{
			this->unite(other);
			return (*this);
		}
		/// @brief Same as intersect.
		/// @see intersect(const Array<T>& other)
		inline Array<T>& operator&=(const Array<T>& other)
		{
			this->intersect(other);
			return (*this);
		}
		/// @brief Same as differentiate.
		/// @see differentiate(const T& element)
		inline Array<T>& operator/=(const T& element)
		{
			this->differentiate(element);
			return (*this);
		}
		/// @brief Same as differentiate.
		/// @see differentiate(const Array<T>& other)
		inline Array<T>& operator/=(const Array<T>& other)
		{
			this->differentiate(other);
			return (*this);
		}
		/// @brief Merges an Array with an element.
		/// @param[in] element Element to merge with.
		/// @return New Array with element added at the end of Array.
		inline Array<T> operator+(const T& element) const
		{
			Array<T> result(*this);
			result += element;
			return result;
		}
		/// @brief Merges two Arrays.
		/// @param[in] other Second Array to merge with.
		/// @return New Array with elements of second Array added at the end of first Array.
		inline Array<T> operator+(const Array<T>& other) const
		{
			Array<T> result(*this);
			result += other;
			return result;
		}
		/// @brief Removes element from Array.
		/// @param[in] element Element to remove.
		/// @return New Array with elements of first Array without given element.
		inline Array<T> operator-(T element) const
		{
			Array<T> result(*this);
			result -= element;
			return result;
		}
		/// @brief Removes second Array from first Array.
		/// @param[in] other Array to remove.
		/// @return New Array with elements of first Array without the elements of second Array.
		inline Array<T> operator-(const Array<T>& other) const
		{
			Array<T> result(*this);
			result -= other;
			return result;
		}
		/// @brief Same as united.
		/// @see united(const T& element)
		inline Array<T> operator|(const T& element) const
		{
			return this->united(element);
		}
		/// @brief Same as united.
		/// @see united(const Array<T>& other)
		inline Array<T> operator|(const Array<T>& other) const
		{
			return this->united(other);
		}
		/// @brief Same as intersected.
		/// @see intersected(const Array<T>& other)
		inline Array<T> operator&(const Array<T>& other) const
		{
			return this->intersected(other);
		}
		/// @brief Same as differentiated.
		/// @see differentiated(const T& element)
		inline Array<T> operator/(const T& element) const
		{
			return this->differentiated(element);
		}
		/// @brief Same as differentiated.
		/// @see differentiated(const Array<T>& other)
		inline Array<T> operator/(const Array<T>& other) const
		{
			return this->differentiated(other);
		}

		/// @brief Casts this Array into a C-array.
		/// @return The C-array.
		inline operator T*()
		{
			return &this->operator[](0);
		}
		/// @brief Casts this Array into a C-array.
		/// @return The C-array.
		inline operator const T*() const
		{
			return &this->operator[](0);
		}

		// DEPRECATED
		DEPRECATED_ATTRIBUTE inline Array<int> indexes_of(const T& element) const							{ return this->indexesOf(element); }
		DEPRECATED_ATTRIBUTE inline Array<T> removed_duplicates() const										{ return this->removedDuplicates(); }
		DEPRECATED_ATTRIBUTE inline T pop(int index)														{ return this->removeAt(index); }
		DEPRECATED_ATTRIBUTE inline Array<T> pop(int index, int count)										{ return this->removeAt(index, count); }
		DEPRECATED_ATTRIBUTE inline T pop_at(int index)														{ return this->removeAt(index); }
		DEPRECATED_ATTRIBUTE inline Array<T> pop_at(int index, int count)									{ return this->removeAt(index, count); }
		DEPRECATED_ATTRIBUTE inline T pop_front()															{ return this->removeFirst(); }
		DEPRECATED_ATTRIBUTE inline Array<T> pop_front(const int count)										{ return this->removeFirst(count); }
		DEPRECATED_ATTRIBUTE inline T pop_first()															{ return this->removeFirst(); }
		DEPRECATED_ATTRIBUTE inline Array<T> pop_first(const int count)										{ return this->removeFirst(count); }
		DEPRECATED_ATTRIBUTE inline T pop_back()															{ return this->removeLast(); }
		DEPRECATED_ATTRIBUTE inline Array<T> pop_back(const int count)										{ return this->removeLast(count); }
		DEPRECATED_ATTRIBUTE inline T pop_last()															{ return this->removeLast(); }
		DEPRECATED_ATTRIBUTE inline Array<T> pop_last(const int count)										{ return this->removeLast(count); }
		DEPRECATED_ATTRIBUTE inline T pop_all(T& element)													{ return this->removeAll(element); }
		DEPRECATED_ATTRIBUTE inline Array<T> pop_all(const Array<T>& other)									{ return this->removeAll(other); }
		DEPRECATED_ATTRIBUTE inline T remove_at(int index)													{ return this->removeAt(index); }
		DEPRECATED_ATTRIBUTE inline Array<T> remove_at(int index, int count)								{ return this->removeAt(index, count); }
		DEPRECATED_ATTRIBUTE inline T remove_front()														{ return this->removeFirst(); }
		DEPRECATED_ATTRIBUTE inline Array<T> remove_front(const int count)									{ return this->removeFirst(count); }
		DEPRECATED_ATTRIBUTE inline T remove_first()														{ return this->removeFirst(); }
		DEPRECATED_ATTRIBUTE inline Array<T> remove_first(const int count)									{ return this->removeFirst(count); }
		DEPRECATED_ATTRIBUTE inline T remove_back()															{ return this->removeLast(); }
		DEPRECATED_ATTRIBUTE inline Array<T> remove_back(const int count)									{ return this->removeLast(count); }
		DEPRECATED_ATTRIBUTE inline T remove_last()															{ return this->removeLast(); }
		DEPRECATED_ATTRIBUTE inline Array<T> remove_last(const int count)									{ return this->removeLast(count); }
		DEPRECATED_ATTRIBUTE inline T pop_random()															{ return this->removeRandom(); }
		DEPRECATED_ATTRIBUTE inline Array<T> pop_random(int count, bool unique = false)						{ return this->removeRandom(count, unique); }
		DEPRECATED_ATTRIBUTE inline T remove_random()														{ return this->removeRandom(); }
		DEPRECATED_ATTRIBUTE inline Array<T> remove_random(int count, bool unique = false)					{ return this->removeRandom(count, unique); }
		DEPRECATED_ATTRIBUTE inline Array<T> find_all(bool (*conditionFunction)(T)) const					{ return this->findAll(conditionFunction); }
		template <class S> DEPRECATED_ATTRIBUTE inline Array<S> dyn_cast(bool includeNulls = false) const	{ return this->dynamicCast<S>(includeNulls); }

	};
	
}

/// @brief Alias for simpler code.
#define harray hltypes::Array

#endif
