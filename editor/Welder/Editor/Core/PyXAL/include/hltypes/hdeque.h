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
/// Encapsulates std::deque and adds high level methods.

#ifndef HLTYPES_DEQUE_H
#define HLTYPES_DEQUE_H

#include <deque>

#include "hcontainer.h"
#include "hexception.h"
#include "hltypesUtil.h"
#include "hstring.h"

/// @brief Provides a simpler syntax to iterate through a Deque.
#define foreach_q(type, name, container) for (hdeque< type >::iterator_t name = (container).begin(); name != (container).end(); ++name)
#define foreachc_q(type, name, container) for (hdeque< type >::const_iterator_t name = (container).begin(); name != (container).end(); ++name)
/// @brief Provides a simpler syntax to reverse iterate through a Deque.
#define foreach_qr(type, name, container) for (hdeque< type >::reverse_iterator_t name = (container).rbegin(); name != (container).rend(); ++name)
#define foreachc_qr(type, name, container) for (hdeque< type >::const_reverse_iterator_t name = (container).rbegin(); name != (container).rend(); ++name)

namespace hltypes
{
	/// @brief Encapsulates std::deque and adds high level methods.
	template <class T>
	class Deque : public Container<std::deque<T>, T>
	{
	public:
		/// @brief Empty constructor.
		inline Deque() : Container<std::deque<T>, T>()
		{
		}
		/// @brief Copy constructor.
		/// @param[in] other Container to copy.
		inline Deque(const Container<std::deque<T>, T>& other) : Container<std::deque<T>, T>(other)
		{
		}
		/// @brief Constructor from single element.
		/// @param[in] element Element to insert.
		inline Deque(const T& element) : Container<std::deque<T>, T>(element)
		{
		}
		/// @brief Constructor from single element.
		/// @param[in] element Element to insert.
		/// @param[in] times Number of times to insert element.
		inline Deque(const T& element, int times) : Container<std::deque<T>, T>(element, times)
		{
		}
		/// @brief Constructor from another Container.
		/// @param[in] other Container to copy.
		/// @param[in] count Number of elements to copy.
		inline Deque(const Container<std::deque<T>, T>& other, const int count) : Container<std::deque<T>, T>(other, count)
		{
		}
		/// @brief Constructor from another Container.
		/// @param[in] other Container to copy.
		/// @param[in] start Start index of elements to copy.
		/// @param[in] count Number of elements to copy.
		inline Deque(const Container<std::deque<T>, T>& other, const int start, const int count) : Container<std::deque<T>, T>(other, start, count)
		{
		}
		/// @brief Constructor from C-type array.
		/// @param[in] other C-type array to copy.
		/// @param[in] count Number of elements to copy.
		inline Deque(const T other[], const int count) : Container<std::deque<T>, T>(other, count)
		{
		}
		/// @brief Constructor from C-type array.
		/// @param[in] other C-type array to copy.
		/// @param[in] start Start index of elements to copy.
		/// @param[in] count Number of elements to copy.
		inline Deque(const T other[], const int start, const int count) : Container<std::deque<T>, T>(other, start, count)
		{
		}
		/// @brief Destructor.
		inline ~Deque()
		{
		}
		/// @brief Gets all indexes of the given element.
		/// @param[in] element Element to search for.
		/// @return All indexes of the given element.
		inline Deque<int> indexesOf(const T& element) const
		{
			return this->template _indexesOf<Deque<int> >(element);
		}
		/// @brief Removes element at given index.
		/// @param[in] index Index of element to remove.
		/// @return The removed element.
		inline T removeAt(int index)
		{
			return Container<std::deque<T>, T>::removeAt(index);
		}
		/// @brief Removes n elements at given index of Deque.
		/// @param[in] index Start index of elements to remove.
		/// @param[in] count Number of elements to remove.
		/// @return Deque of all removed elements.
		/// @note Elements in the returned Deque are in the same order as in the orignal Deque.
		inline Deque<T> removeAt(int index, int count)
		{
			return this->template _removeAt<Deque<T> >(index, count);
		}
		/// @brief Removes first element of Deque.
		/// @return The removed element.
		inline T removeFirst()
		{
			return Container<std::deque<T>, T>::removeFirst();
		}
		/// @brief Removes n elements from the beginning of Deque.
		/// @param[in] count Number of elements to remove.
		/// @return Deque of all removed elements.
		/// @note Elements in the returned Deque are in the same order as in the orignal Deque.
		inline Deque<T> removeFirst(const int count)
		{
			return this->template _removeFirst<Deque<T> >(count);
		}
		/// @brief Removes last element of Deque.
		/// @return The removed element.
		inline T removeLast()
		{
			return Container<std::deque<T>, T>::removeLast();
		}
		/// @brief Removes n elements from the end of Deque.
		/// @param[in] count Number of elements to remove.
		/// @return Deque of all removed elements.
		/// @note Elements in the returned Deque are in the same order as in the orignal Deque.
		inline Deque<T> removeLast(const int count)
		{
			return this->template _removeLast<Deque<T> >(count);
		}
		/// @brief Gets a random element in Deque and removes it.
		/// @return Random element.
		inline T removeRandom()
		{
			return Container<std::deque<T>, T>::removeRandom();
		}
		/// @brief Gets an Deque of random elements selected from this one and removes them.
		/// @param[in] count Number of random elements.
		/// @param[in] unique Whether to force all random values to be unique.
		/// @return Deque of random elements selected from this one.
		inline Deque<T> removeRandom(const int count)
		{
			return this->template _removeRandom<Deque<T> >(count);
		}
		/// @brief Gets a random element in Deque.
		/// @return Random element.
		inline T random() const
		{
			return Container<std::deque<T>, T>::random();
		}
		/// @brief Gets an Deque of random elements selected from this one.
		/// @param[in] count Number of random elements.
		/// @param[in] unique Whether to force all random values to be at unique positions.
		/// @return Deque of random elements selected from this one.
		inline Deque<T> random(int count, bool unique = true)
		{
			return this->template _random<Deque<T> >(count, unique);
		}
		/// @brief Creates new Deque with reversed order of elements.
		/// @return A new Deque.
		inline Deque<T> reversed() const
		{
			return this->template _reversed<Deque<T> >();
		}
		/// @brief Creates new Deque without duplicates.
		/// @return A new Deque.
		inline Deque<T> removedDuplicates() const
		{
			return this->template _removedDuplicates<Deque<T> >();
		}
		/// @brief Creates new sorted Deque.
		/// @return A new Deque.
		/// @note The sorting order is ascending.
		inline Deque<T> sorted() const
		{
			return this->template _sorted<Deque<T> >();
		}
		/// @brief Creates new sorted Deque.
		/// @param[in] compareFunction Function pointer with comparison function that takes two elements of type T and returns bool.
		/// @return A new Deque.
		/// @note The sorting order is ascending.
		/// @note compareFunction should return true if first element is less than the second element.
		inline Deque<T> sorted(bool(*compareFunction)(T, T)) const
		{
			return this->template _sorted<Deque<T> >(compareFunction);
		}
		/// @brief Creates a new Deque with randomized order of elements.
		/// @return A new Deque.
		inline Deque<T> randomized() const
		{
			return this->template _randomized<Deque<T> >();
		}
		/// @brief Creates a new Deque as union of this Deque with an element.
		/// @param[in] element Element to unite with.
		/// @return A new Deque.
		/// @note Removes duplicates.
		inline Deque<T> united(const T& element) const
		{
			return this->template _united<Deque<T> >(element);
		}
		/// @brief Creates a new Deque as union of this Deque with another one.
		/// @param[in] other Deque to unite with.
		/// @return A new Deque.
		/// @note Removes duplicates.
		inline Deque<T> united(const Deque<T>& other) const
		{
			return this->template _united<Deque<T> >(other);
		}
		/// @brief Creates a new Deque as intersection of this Deque with another one.
		/// @param[in] other Deque to intersect with.
		/// @return A new Deque.
		/// @note Does not remove duplicates.
		inline Deque<T> intersected(const Deque<T>& other) const
		{
			return this->template _intersected<Deque<T> >(other);
		}
		/// @brief Creates a new Deque as difference of this Deque with an element.
		/// @param[in] other Element to differentiate with.
		/// @return A new Deque.
		/// @note Unlike remove, this method ignores if the element is not in this Deque.
		/// @note Does not remove duplicates.
		inline Deque<T> differentiated(const T& element) const
		{
			return this->template _differentiated<Deque<T> >(element);
		}
		/// @brief Creates a new Deque as difference of this Deque with another one.
		/// @param[in] other Deque to differentiate with.
		/// @return A new Deque.
		/// @note Unlike remove, this method ignore elements of other Deque that are not in this one.
		/// @note Does not remove duplicates.
		inline Deque<T> differentiated(const Deque<T>& other) const
		{
			return this->template _differentiated<Deque<T> >(other);
		}
		/// @brief Finds and returns new Deque of elements that match the condition.
		/// @param[in] conditionFunction Function pointer with condition function that takes one element of type T and returns bool.
		/// @return New Deque with all matching elements.
		inline Deque<T> findAll(bool (*conditionFunction)(T)) const
		{
			return this->template _findAll<Deque<T> >(conditionFunction);
		}
		/// @brief Returns a new Deque with all elements cast into type S.
		/// @return A new Deque with all elements cast into type S.
		/// @note Make sure all elements in the Deque can be cast into type S.
		template <class S>
		inline Deque<S> cast() const
		{
			return this->template _cast<Deque<S>, S>();
		}
		/// @brief Returns a new Deque with all elements dynamically cast into type S.
		/// @param[in] includeNulls Whether to include NULLs that failed to cast.
		/// @return A new Deque with all elements cast into type S.
		/// @note Be careful not to use this function with non-pointers and classes that don't have virtual functions.
		template <class S>
		inline Deque<S> dynamicCast(bool includeNulls = false) const
		{
			return this->template _dynamicCast<Deque<S>, S>(includeNulls);
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
		/// @brief Returns a subdeque.
		/// @param[in] start Start index of the elements to copy.
		/// @param[in] count Number of elements to copy.
		/// @return Subdeque created from the current Deque.
		inline Deque<T> operator()(int start, const int count) const
		{
			return this->template _sub<Deque<T> >(start, count);
		}
		/// @brief Same as equals.
		/// @see equals
		inline bool operator==(const Deque<T>& other) const
		{
			return this->equals(other);
		}
		/// @brief Same as nequals.
		/// @see nequals
		inline bool operator!=(const Deque<T>& other) const
		{
			return this->nequals(other);
		}
		/// @brief Same as add.
		/// @see add(const T& element)
		inline Deque<T>& operator<<(const T& element)
		{
			this->add(element);
			return (*this);
		}
		/// @brief Same as add.
		/// @see add(const Deque<T>& other)
		inline Deque<T>& operator<<(const Deque<T>& other)
		{
			this->add(other);
			return (*this);
		}
		/// @brief Same as add.
		/// @see add(const T& element)
		inline Deque<T>& operator+=(const T& element)
		{
			this->add(element);
			return (*this);
		}
		/// @brief Same as add.
		/// @see add(const Deque<T>& other)
		inline Deque<T>& operator+=(const Deque<T>& other)
		{
			this->add(other);
			return (*this);
		}
		/// @brief Same as remove.
		/// @see remove(T element)
		inline Deque<T>& operator-=(T element)
		{
			this->remove(element);
			return (*this);
		}
		/// @brief Same as remove.
		/// @see remove(const Deque<T>& other)
		inline Deque<T>& operator-=(const Deque<T>& other)
		{
			this->remove(other);
			return (*this);
		}
		/// @brief Same as unite.
		/// @see unite(const T& element)
		inline Deque<T>& operator|=(const T& element)
		{
			this->unite(element);
			return (*this);
		}
		/// @brief Same as unite.
		/// @see unite(const Deque<T>& other)
		inline Deque<T>& operator|=(const Deque<T>& other)
		{
			this->unite(other);
			return (*this);
		}
		/// @brief Same as intersect.
		/// @see intersect(const Deque<T>& other)
		inline Deque<T>& operator&=(const Deque<T>& other)
		{
			this->intersect(other);
			return (*this);
		}
		/// @brief Same as differentiate.
		/// @see differentiate(const T& element)
		inline Deque<T>& operator/=(const T& element)
		{
			this->differentiate(element);
			return (*this);
		}
		/// @brief Same as differentiate.
		/// @see differentiate(const Deque<T>& other)
		inline Deque<T>& operator/=(const Deque<T>& other)
		{
			this->differentiate(other);
			return (*this);
		}
		/// @brief Merges a Deque with an element.
		/// @param[in] element Element to merge with.
		/// @return New Deque with element added at the end of Deque.
		inline Deque<T> operator+(const T& element) const
		{
			Deque<T> result(*this);
			result += element;
			return result;
		}
		/// @brief Merges two Deques.
		/// @param[in] other Second Deque to merge with.
		/// @return New Deque with elements of second Deque added at the end of first Deque.
		inline Deque<T> operator+(const Deque<T>& other) const
		{
			Deque<T> result(*this);
			result += other;
			return result;
		}
		/// @brief Removes element from Deque.
		/// @param[in] element Element to remove.
		/// @return New Deque with elements of first Deque without given element.
		inline Deque<T> operator-(T element) const
		{
			Deque<T> result(*this);
			result -= element;
			return result;
		}
		/// @brief Removes second Deque from first Deque.
		/// @param[in] other Deque to remove.
		/// @return New Deque with elements of first Deque without the elements of second Deque.
		inline Deque<T> operator-(const Deque<T>& other) const
		{
			Deque<T> result(*this);
			result -= other;
			return result;
		}
		/// @brief Same as united.
		/// @see united(const T& element)
		inline Deque<T> operator|(const T& element) const
		{
			return this->united(element);
		}
		/// @brief Same as united.
		/// @see united(const Deque<T>& other)
		inline Deque<T> operator|(const Deque<T>& other) const
		{
			return this->united(other);
		}
		/// @brief Same as intersected.
		/// @see intersected(const Deque<T>& other)
		inline Deque<T> operator&(const Deque<T>& other) const
		{
			return this->intersected(other);
		}
		/// @brief Same as differentiated.
		/// @see differentiated(const T& element)
		inline Deque<T> operator/(const T& element) const
		{
			return this->differentiated(element);
		}
		/// @brief Same as differentiated.
		/// @see differentiated(const Deque<T>& other)
		inline Deque<T> operator/(const Deque<T>& other) const
		{
			return this->differentiated(other);
		}

		// DEPRECATED
		DEPRECATED_ATTRIBUTE inline Deque<int> indexes_of(const T& element) const							{ return this->indexesOf(element); }
		DEPRECATED_ATTRIBUTE inline Deque<T> removed_duplicates() const										{ return this->removedDuplicates(); }
		DEPRECATED_ATTRIBUTE inline T pop(int index)														{ return this->removeAt(index); }
		DEPRECATED_ATTRIBUTE inline Deque<T> pop(int index, int count)										{ return this->removeAt(index, count); }
		DEPRECATED_ATTRIBUTE inline T pop_at(int index)														{ return this->removeAt(index); }
		DEPRECATED_ATTRIBUTE inline Deque<T> pop_at(int index, int count)									{ return this->removeAt(index, count); }
		DEPRECATED_ATTRIBUTE inline T pop_front()															{ return this->removeFirst(); }
		DEPRECATED_ATTRIBUTE inline Deque<T> pop_front(const int count)										{ return this->removeFirst(count); }
		DEPRECATED_ATTRIBUTE inline T pop_first()															{ return this->removeFirst(); }
		DEPRECATED_ATTRIBUTE inline Deque<T> pop_first(const int count)										{ return this->removeFirst(count); }
		DEPRECATED_ATTRIBUTE inline T pop_back()															{ return this->removeLast(); }
		DEPRECATED_ATTRIBUTE inline Deque<T> pop_back(const int count)										{ return this->removeLast(count); }
		DEPRECATED_ATTRIBUTE inline T pop_last()															{ return this->removeLast(); }
		DEPRECATED_ATTRIBUTE inline Deque<T> pop_last(const int count)										{ return this->removeLast(count); }
		DEPRECATED_ATTRIBUTE inline T pop_all(T& element)													{ return this->removeAll(element); }
		DEPRECATED_ATTRIBUTE inline Deque<T> pop_all(const Deque<T>& other)									{ return this->removeAll(other); }
		DEPRECATED_ATTRIBUTE inline T remove_at(int index)													{ return this->removeAt(index); }
		DEPRECATED_ATTRIBUTE inline Deque<T> remove_at(int index, int count)								{ return this->removeAt(index, count); }
		DEPRECATED_ATTRIBUTE inline T remove_front()														{ return this->removeFirst(); }
		DEPRECATED_ATTRIBUTE inline Deque<T> remove_front(const int count)									{ return this->removeFirst(count); }
		DEPRECATED_ATTRIBUTE inline T remove_first()														{ return this->removeFirst(); }
		DEPRECATED_ATTRIBUTE inline Deque<T> remove_first(const int count)									{ return this->removeFirst(count); }
		DEPRECATED_ATTRIBUTE inline T remove_back()															{ return this->removeLast(); }
		DEPRECATED_ATTRIBUTE inline Deque<T> remove_back(const int count)									{ return this->removeLast(count); }
		DEPRECATED_ATTRIBUTE inline T remove_last()															{ return this->removeLast(); }
		DEPRECATED_ATTRIBUTE inline Deque<T> remove_last(const int count)									{ return this->removeLast(count); }
		DEPRECATED_ATTRIBUTE inline T pop_random()															{ return this->removeRandom(); }
		DEPRECATED_ATTRIBUTE inline Deque<T> pop_random(int count, bool unique = false)						{ return this->removeRandom(count, unique); }
		DEPRECATED_ATTRIBUTE inline T remove_random()														{ return this->removeRandom(); }
		DEPRECATED_ATTRIBUTE inline Deque<T> remove_random(int count, bool unique = false)					{ return this->removeRandom(count, unique); }
		DEPRECATED_ATTRIBUTE inline Deque<T> find_all(bool (*conditionFunction)(T)) const					{ return this->findAll(conditionFunction); }
		template <class S> DEPRECATED_ATTRIBUTE inline Deque<S> dyn_cast(bool includeNulls = false) const	{ return this->dynamicCast<S>(includeNulls); }

	};
	
}

/// @brief Alias for simpler code.
#define hdeque hltypes::Deque

#endif
