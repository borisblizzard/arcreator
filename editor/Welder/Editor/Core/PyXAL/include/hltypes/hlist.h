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
/// Encapsulates std::list and adds high level methods.

#ifndef HLTYPES_LIST_H
#define HLTYPES_LIST_H

#include <list>

#include "hcontainer.h"
#include "hexception.h"
#include "hltypesUtil.h"
#include "hstring.h"

/// @brief Provides a simpler syntax to iterate through a List.
#define foreach_l(type, name, container) for (hlist< type >::iterator_t name = (container).begin(); name != (container).end(); ++name)
#define foreachc_l(type, name, container) for (hlist< type >::const_iterator_t name = (container).begin(); name != (container).end(); ++name)
/// @brief Provides a simpler syntax to reverse iterate through a List.
#define foreach_lr(type, name, container) for (hlist< type >::reverse_iterator_t name = (container).rbegin(); name != (container).rend(); ++name)
#define foreachc_lr(type, name, container) for (hlist< type >::const_reverse_iterator_t name = (container).rbegin(); name != (container).rend(); ++name)

namespace hltypes
{
	/// @brief Encapsulates std::list and adds high level methods.
	template <class T>
	class List : public Container<std::list<T>, T>
	{
	public:
		/// @brief Empty constructor.
		inline List() : Container<std::list<T>, T>()
		{
		}
		/// @brief Copy constructor.
		/// @param[in] other Container to copy.
		inline List(const Container<std::list<T>, T>& other) : Container<std::list<T>, T>(other)
		{
		}
		/// @brief Constructor from single element.
		/// @param[in] element Element to insert.
		inline List(const T& element) : Container<std::list<T>, T>(element)
		{
		}
		/// @brief Constructor from single element.
		/// @param[in] element Element to insert.
		/// @param[in] times Number of times to insert element.
		inline List(const T& element, int times) : Container<std::list<T>, T>(element, times)
		{
		}
		/// @brief Constructor from another Container.
		/// @param[in] other Container to copy.
		/// @param[in] count Number of elements to copy.
		inline List(const Container<std::list<T>, T>& other, const int count) : Container<std::list<T>, T>(other, count)
		{
		}
		/// @brief Constructor from another Container.
		/// @param[in] other Container to copy.
		/// @param[in] start Start index of elements to copy.
		/// @param[in] count Number of elements to copy.
		inline List(const Container<std::list<T>, T>& other, const int start, const int count) : Container<std::list<T>, T>(other, start, count)
		{
		}
		/// @brief Constructor from C-type array.
		/// @param[in] other C-type array to copy.
		/// @param[in] count Number of elements to copy.
		inline List(const T other[], const int count) : Container<std::list<T>, T>(other, count)
		{
		}
		/// @brief Constructor from C-type array.
		/// @param[in] other C-type array to copy.
		/// @param[in] start Start index of elements to copy.
		/// @param[in] count Number of elements to copy.
		inline List(const T other[], const int start, const int count) : Container<std::list<T>, T>(other, start, count)
		{
		}
		/// @brief Destructor.
		inline ~List()
		{
		}
		/// @brief Gets all indexes of the given element.
		/// @param[in] element Element to search for.
		/// @return All indexes of the given element.
		inline List<int> indexesOf(const T& element) const
		{
			return this->template _indexesOf<List<int> >(element);
		}
		/// @brief Removes element at given index.
		/// @param[in] index Index of element to remove.
		/// @return The removed element.
		inline T removeAt(int index)
		{
			return Container<std::list<T>, T>::removeAt(index);
		}
		/// @brief Removes n elements at given index of List.
		/// @param[in] index Start index of elements to remove.
		/// @param[in] count Number of elements to remove.
		/// @return List of all removed elements.
		/// @note Elements in the returned List are in the same order as in the orignal List.
		inline List<T> removeAt(int index, int count)
		{
			return this->template _removeAt<List<T> >(index, count);
		}
		/// @brief Removes first element of List.
		/// @return The removed element.
		inline T removeFirst()
		{
			return Container<std::list<T>, T>::removeFirst();
		}
		/// @brief Removes n elements from the beginning of List.
		/// @param[in] count Number of elements to remove.
		/// @return List of all removed elements.
		/// @note Elements in the returned List are in the same order as in the orignal List.
		inline List<T> removeFirst(const int count)
		{
			return this->template _removeFirst<List<T> >(count);
		}
		/// @brief Removes last element of List.
		/// @return The removed element.
		inline T removeLast()
		{
			return Container<std::list<T>, T>::removeLast();
		}
		/// @brief Removes n elements from the end of List.
		/// @param[in] count Number of elements to remove.
		/// @return List of all removed elements.
		/// @note Elements in the returned List are in the same order as in the orignal List.
		inline List<T> removeLast(const int count)
		{
			return this->template _removeLast<List<T> >(count);
		}
		/// @brief Gets a random element in List and removes it.
		/// @return Random element.
		inline T removeRandom()
		{
			return Container<std::list<T>, T>::removeRandom();
		}
		/// @brief Gets an List of random elements selected from this one and removes them.
		/// @param[in] count Number of random elements.
		/// @param[in] unique Whether to force all random values to be unique.
		/// @return List of random elements selected from this one.
		inline List<T> removeRandom(const int count)
		{
			return this->template _removeRandom<List<T> >(count);
		}
		/// @brief Gets a random element in List.
		/// @return Random element.
		inline T random() const
		{
			return Container<std::list<T>, T>::random();
		}
		/// @brief Gets an List of random elements selected from this one.
		/// @param[in] count Number of random elements.
		/// @param[in] unique Whether to force all random values to be at unique positions.
		/// @return List of random elements selected from this one.
		inline List<T> random(int count, bool unique = true)
		{
			return this->template _random<List<T> >(count, unique);
		}
		/// @brief Creates new List with reversed order of elements.
		/// @return A new List.
		inline List<T> reversed() const
		{
			return this->template _reversed<List<T> >();
		}
		/// @brief Creates new List without duplicates.
		/// @return A new List.
		inline List<T> removedDuplicates() const
		{
			return this->template _removedDuplicates<List<T> >();
		}
		/// @brief Creates new sorted List.
		/// @return A new List.
		/// @note The sorting order is ascending.
		inline List<T> sorted() const
		{
			return this->template _sorted<List<T> >();
		}
		/// @brief Creates new sorted List.
		/// @param[in] compareFunction Function pointer with comparison function that takes two elements of type T and returns bool.
		/// @return A new List.
		/// @note The sorting order is ascending.
		/// @note compareFunction should return true if first element is less than the second element.
		inline List<T> sorted(bool(*compareFunction)(T, T)) const
		{
			return this->template _sorted<List<T> >(compareFunction);
		}
		/// @brief Creates a new List with randomized order of elements.
		/// @return A new List.
		inline List<T> randomized() const
		{
			return this->template _randomized<List<T> >();
		}
		/// @brief Creates a new List as union of this List with an element.
		/// @param[in] element Element to unite with.
		/// @return A new List.
		/// @note Removes duplicates.
		inline List<T> united(const T& element) const
		{
			return this->template _united<List<T> >(element);
		}
		/// @brief Creates a new List as union of this List with another one.
		/// @param[in] other List to unite with.
		/// @return A new List.
		/// @note Removes duplicates.
		inline List<T> united(const List<T>& other) const
		{
			return this->template _united<List<T> >(other);
		}
		/// @brief Creates a new List as intersection of this List with another one.
		/// @param[in] other List to intersect with.
		/// @return A new List.
		/// @note Does not remove duplicates.
		inline List<T> intersected(const List<T>& other) const
		{
			return this->template _intersected<List<T> >(other);
		}
		/// @brief Creates a new List as difference of this List with an element.
		/// @param[in] other Element to differentiate with.
		/// @return A new List.
		/// @note Unlike remove, this method ignores if the element is not in this List.
		/// @note Does not remove duplicates.
		inline List<T> differentiated(const T& element) const
		{
			return this->template _differentiated<List<T> >(element);
		}
		/// @brief Creates a new List as difference of this List with another one.
		/// @param[in] other List to differentiate with.
		/// @return A new List.
		/// @note Unlike remove, this method ignore elements of other List that are not in this one.
		/// @note Does not remove duplicates.
		inline List<T> differentiated(const List<T>& other) const
		{
			return this->template _differentiated<List<T> >(other);
		}
		/// @brief Finds and returns new List of elements that match the condition.
		/// @param[in] conditionFunction Function pointer with condition function that takes one element of type T and returns bool.
		/// @return New List with all matching elements.
		inline List<T> findAll(bool (*conditionFunction)(T)) const
		{
			return this->template _findAll<List<T> >(conditionFunction);
		}
		/// @brief Returns a new List with all elements cast into type S.
		/// @return A new List with all elements cast into type S.
		/// @note Make sure all elements in the List can be cast into type S.
		template <class S>
		inline List<S> cast() const
		{
			return this->template _cast<List<S>, S>();
		}
		/// @brief Returns a new List with all elements dynamically cast into type S.
		/// @param[in] includeNulls Whether to include NULLs that failed to cast.
		/// @return A new List with all elements cast into type S.
		/// @note Be careful not to use this function with non-pointers and classes that don't have virtual functions.
		template <class S>
		inline List<S> dynamicCast(bool includeNulls = false) const
		{
			return this->template _dynamicCast<List<S>, S>(includeNulls);
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
		/// @brief Returns a sublist.
		/// @param[in] start Start index of the elements to copy.
		/// @param[in] count Number of elements to copy.
		/// @return Sublist created from the current List.
		inline List<T> operator()(int start, const int count) const
		{
			return this->template _sub<List<T> >(start, count);
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
		/// @brief Same as add.
		/// @see add(const T& element)
		inline List<T>& operator<<(const T& element)
		{
			this->add(element);
			return (*this);
		}
		/// @brief Same as add.
		/// @see add(const List<T>& other)
		inline List<T>& operator<<(const List<T>& other)
		{
			this->add(other);
			return (*this);
		}
		/// @brief Same as add.
		/// @see add(const T& element)
		inline List<T>& operator+=(const T& element)
		{
			this->add(element);
			return (*this);
		}
		/// @brief Same as add.
		/// @see add(const List<T>& other)
		inline List<T>& operator+=(const List<T>& other)
		{
			this->add(other);
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

		// DEPRECATED
		DEPRECATED_ATTRIBUTE inline List<int> indexes_of(const T& element) const							{ return this->indexesOf(element); }
		DEPRECATED_ATTRIBUTE inline List<T> removed_duplicates() const										{ return this->removedDuplicates(); }
		DEPRECATED_ATTRIBUTE inline T pop(int index)														{ return this->removeAt(index); }
		DEPRECATED_ATTRIBUTE inline List<T> pop(int index, int count)										{ return this->removeAt(index, count); }
		DEPRECATED_ATTRIBUTE inline T pop_at(int index)														{ return this->removeAt(index); }
		DEPRECATED_ATTRIBUTE inline List<T> pop_at(int index, int count)									{ return this->removeAt(index, count); }
		DEPRECATED_ATTRIBUTE inline T pop_front()															{ return this->removeFirst(); }
		DEPRECATED_ATTRIBUTE inline List<T> pop_front(const int count)										{ return this->removeFirst(count); }
		DEPRECATED_ATTRIBUTE inline T pop_first()															{ return this->removeFirst(); }
		DEPRECATED_ATTRIBUTE inline List<T> pop_first(const int count)										{ return this->removeFirst(count); }
		DEPRECATED_ATTRIBUTE inline T pop_back()															{ return this->removeLast(); }
		DEPRECATED_ATTRIBUTE inline List<T> pop_back(const int count)										{ return this->removeLast(count); }
		DEPRECATED_ATTRIBUTE inline T pop_last()															{ return this->removeLast(); }
		DEPRECATED_ATTRIBUTE inline List<T> pop_last(const int count)										{ return this->removeLast(count); }
		DEPRECATED_ATTRIBUTE inline T pop_all(T& element)													{ return this->removeAll(element); }
		DEPRECATED_ATTRIBUTE inline List<T> pop_all(const List<T>& other)									{ return this->removeAll(other); }
		DEPRECATED_ATTRIBUTE inline T remove_at(int index)													{ return this->removeAt(index); }
		DEPRECATED_ATTRIBUTE inline List<T> remove_at(int index, int count)									{ return this->removeAt(index, count); }
		DEPRECATED_ATTRIBUTE inline T remove_front()														{ return this->removeFirst(); }
		DEPRECATED_ATTRIBUTE inline List<T> remove_front(const int count)									{ return this->removeFirst(count); }
		DEPRECATED_ATTRIBUTE inline T remove_first()														{ return this->removeFirst(); }
		DEPRECATED_ATTRIBUTE inline List<T> remove_first(const int count)									{ return this->removeFirst(count); }
		DEPRECATED_ATTRIBUTE inline T remove_back()															{ return this->removeLast(); }
		DEPRECATED_ATTRIBUTE inline List<T> remove_back(const int count)									{ return this->removeLast(count); }
		DEPRECATED_ATTRIBUTE inline T remove_last()															{ return this->removeLast(); }
		DEPRECATED_ATTRIBUTE inline List<T> remove_last(const int count)									{ return this->removeLast(count); }
		DEPRECATED_ATTRIBUTE inline T pop_random()															{ return this->removeRandom(); }
		DEPRECATED_ATTRIBUTE inline List<T> pop_random(int count, bool unique = false)						{ return this->removeRandom(count, unique); }
		DEPRECATED_ATTRIBUTE inline T remove_random()														{ return this->removeRandom(); }
		DEPRECATED_ATTRIBUTE inline List<T> remove_random(int count, bool unique = false)					{ return this->removeRandom(count, unique); }
		DEPRECATED_ATTRIBUTE inline List<T> find_all(bool (*conditionFunction)(T)) const					{ return this->findAll(conditionFunction); }
		template <class S> DEPRECATED_ATTRIBUTE inline List<S> dyn_cast(bool includeNulls = false) const	{ return this->dynamicCast<S>(includeNulls); }

	};
	
}

/// @brief Alias for simpler code.
#define hlist hltypes::List

#endif
