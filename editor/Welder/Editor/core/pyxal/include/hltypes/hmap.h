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
/// Encapsulates std::map and adds high level methods.

#ifndef HLTYPES_MAP_H
#define HLTYPES_MAP_H

#include <map>

#include "harray.h"
#include "hstring.h"

/// @brief Provides a simpler syntax to iterate through a Map.
#define foreach_map(type_key, type_value, name, container) for (hltypes::Map< type_key, type_value >::iterator_t name = (container).begin(); name != (container).end(); ++name)
#define foreachc_map(type_key, type_value, name, container) for (hltypes::Map< type_key, type_value >::const_iterator_t name = (container).begin(); name != (container).end(); ++name)
/// @brief Provides a simpler syntax to iterate through a Map with String as key.
#define foreach_m(type, name, container) for (hltypes::Map< hltypes::String, type >::iterator_t name = (container).begin(); name != (container).end(); ++name)
#define foreachc_m(type, name, container) for (hltypes::Map< hltypes::String, type >::const_iterator_t name = (container).begin(); name != (container).end(); ++name)
/// @brief Internal provider for simpler syntax to iterate through a Map with String as key.
#define __foreach_this_map_it(name) for (const_iterator_t name = this->begin(); name != this->end(); ++name)
/// @brief Internal provider for simpler syntax to iterate through a Map with String as key.
#define __foreach_other_map_it(name, other) for (const_iterator_t name = other.begin(); name != other.end(); ++name)

namespace hltypes
{
	/// @brief Encapsulates std::map and adds high level methods.
	template <class K, class V>
	class Map : public std::map<K, V>
	{
	public:
		/// @brief Iterator type exposure.
		typedef typename std::map<K, V>::iterator iterator_t;
		/// @brief Iterator type exposure.
		typedef typename std::map<K, V>::const_iterator const_iterator_t;
		/// @brief Iterator type exposure.
		typedef typename std::vector<K>::iterator kiterator_t;
		/// @brief Iterator type exposure.
		typedef typename std::vector<K>::const_iterator const_kiterator_t;
		/// @brief Empty constructor.
		inline Map() : std::map<K, V>()
		{
		}
		/// @brief Copy constructor.
		/// @param[in] other Map to copy.
		inline Map(const Map<K, V>& other) : std::map<K, V>(other)
		{
		}
		/// @brief Destructor.
		inline ~Map()
		{
		}
		/// @brief Returns value with specified key.
		/// @param[in] key Key of the value.
		/// @return Value with specified key.
		inline V& operator[](const K& key)
		{
			return std::map<K, V>::operator[](key);
		}
		/// @brief Same as key_of.
		/// @see key_of
		inline K operator()(const V& value) const
		{
			return this->keyOf(value);
		}
		/// @brief Same as equals.
		/// @see equals
		inline bool operator==(const Map<K, V>& other) const
		{
			return this->equals(other);
		}
		/// @brief Same as nequals.
		/// @see nequals
		inline bool operator!=(const Map<K, V>& other) const
		{
			return this->nequals(other);
		}
		/// @brief Returns the number of values in the Map.
		/// @return The number of values in the Map.
		inline int size() const
		{
			return (int)std::map<K, V>::size();
		}
		/// @brief Returns an Array with all keys.
		/// @return An Array with all keys.
		inline Array<K> keys() const
		{
			Array<K> result;
			__foreach_this_map_it(it)
			{
				result += it->first;
			}
			return result;
		}
		/// @brief Returns an Array with all values.
		/// @return An Array with all values.
		inline Array<V> values() const
		{
			Array<V> result;
			__foreach_this_map_it(it)
			{
				result += it->second;
			}
			return result;
		}
		/// @brief Returns an Array with all values in the same order as the given corresponding keys.
		/// @return An Array with all values in the same order as the given corresponding keys.
		inline Array<V> values(const Array<K> keys) const
		{
			Array<V> result;
			for (const_kiterator_t it = keys.begin(); it != keys.end(); ++it) // don't change, requires a const iterator
			{
				result += std::map<K, V>::operator[](*it);
			}
			return result;
		}
		/// @brief Returns an Array with all key-value pairs.
		/// @return An Array with all key-value pairs.
		inline Array<std::pair<K, V> > keyValuePairs() const
		{
			Array<std::pair<K, V> > result;
			__foreach_this_map_it(it)
			{
				result += (*it);
			}
			return result;
		}
		/// @brief Returns an Array with all key-value pairs in the same order as the given corresponding keys.
		/// @return An Array with all key-value pairs in the same order as the given corresponding keys.
		inline Array<std::pair<K, V> > keyValuePairs(const Array<K> keys) const
		{
			Array<std::pair<K, V> > result;
			for (const_kiterator_t it = keys.begin(); it != keys.end(); ++it) // don't change, requires a const iterator
			{
				result += std::pair<K, V>((*it), std::map<K, V>::operator[](*it));
			}
			return result;
		}
		/// @brief Compares the contents of two Maps for being equal.
		/// @param[in] other Another Map.
		/// @return True if number of keys and values are equal and all pairs of keys and values are equal.
		inline bool equals(const Map<K, V>& other) const
		{
			if (this->size() != other.size())
			{
				return false;
			}
			Array<K> keys = other.keys();
			if (!this->hasAllKeys(keys))
			{
				return false;
			}
			__foreach_this_map_it(it)
			{
				// making sure operator== is used, not !=
				if (!(it->second == other.find(it->first)->second))
				{
					return false;
				}
			}
			return true;
		}
		/// @brief Compares the contents of two Maps for being not equal.
		/// @param[in] other Another Map.
		/// @return True if number of keys and values are not equal or at least one pair of keys and values is not equal.
		inline bool nequals(const Map<K, V>& other) const
		{
			if (this->size() != other.size())
			{
				return true;
			}
			Array<K> keys = other.keys();
			if (!this->hasAllKeys(keys))
			{
				return true;
			}
			__foreach_this_map_it(it)
			{
				// making sure operator!= is used, not ==
				if (it->second != other.find(it->first)->second)
				{
					return true;
				}
			}
			return false;
		}
		/// @brief Returns key of specified value.
		/// @param[in] value Value with the given key.
		/// @return Key of specified value.
		inline K keyOf(const V& value) const
		{
			__foreach_this_map_it(it)
			{
				if (it->second == value)
				{
					return it->first;
				}
			}
			return std::map<K, V>::end()->first;
		}
		/// @brief Returns value of specified key.
		/// @param[in] key Key of the given value.
		/// @return Value of specified key.
		inline V valueOf(const K& key) const
		{
			return std::map<K, V>::find(key)->second;
		}
		/// @brief Checks for existence of a key.
		/// @param[in] key Key to check.
		/// @return True if key is present.
		inline bool hasKey(const K& key) const
		{
			return (std::map<K, V>::find(key) != std::map<K, V>::end());
		}
		/// @brief Checks for existence of a key within an Array of keys.
		/// @param[in] keys Array of keys to check.
		/// @return True if any key is present.
		inline bool hasAnyKey(const Array<K>& keys) const
		{
			const_iterator_t end = std::map<K, V>::end();
			for_iter (i, 0, keys.size())
			{
				if (std::map<K, V>::find(keys.at(i)) != end)
				{
					return true;
				}
			}
			return false;
		}
		/// @brief Checks for existence of a key within an Array of keys.
		/// @param[in] keys C-type array of keys to check.
		/// @param[in] count Number of keys to check.
		/// @return True if any key is present.
		inline bool hasAnyKey(const K keys[], const int count) const
		{
			const_iterator_t end = std::map<K, V>::end();
			for_iter (i, 0, count)
			{
				if (std::map<K, V>::find(keys[i]) != end)
				{
					return true;
				}
			}
			return false;
		}
		/// @brief Checks for existence of all keys.
		/// @param[in] keys Array of keys to check.
		/// @return True if all keys are present.
		inline bool hasAllKeys(const Array<K>& keys) const
		{
			const_iterator_t end = std::map<K, V>::end();
			for_iter (i, 0, keys.size())
			{
				if (std::map<K, V>::find(keys.at(i)) == end)
				{
					return false;
				}
			}
			return true;
		}
		/// @brief Checks for existence of all keys.
		/// @param[in] keys C-type array of keys to check.
		/// @param[in] count Number of keys to check.
		/// @return True if all keys are present.
		inline bool hasAllKeys(const K keys[], const int count) const
		{
			const_iterator_t end = std::map<K, V>::end();
			for_iter (i, 0, count)
			{
				if (std::map<K, V>::find(keys[i]) == end)
				{
					return false;
				}
			}
			return true;
		}
		/// @brief Checks for existence of a value.
		/// @param[in] value Value to check.
		/// @return True if value is present.
		inline bool hasValue(const V& value) const
		{
			__foreach_this_map_it(it)
			{
				if (it->second == value)
				{
					return true;
				}
			}
			return false;
		}
		/// @brief Checks for existence of a values in an Array of values.
		/// @param[in] values Array of values to check.
		/// @return True if any values are present.
		inline bool hasAnyValue(const Array<V>& values) const
		{
			for_iter (i, 0, values.size())
			{
				if (this->hasValue(values.at(i)))
				{
					return true;
				}
			}
			return false;
		}
		/// @brief Checks for existence of a values in an Array of values.
		/// @param[in] values C-type array of values to check.
		/// @param[in] count Number of values to check.
		/// @return True if any values are present.
		inline bool hasAnyValue(const V values[], const int count) const
		{
			for_iter (i, 0, count)
			{
				if (this->hasValue(values[i]))
				{
					return true;
				}
			}
			return false;
		}
		/// @brief Checks for existence of all values.
		/// @param[in] values Array of values to check.
		/// @return True if all values are present.
		inline bool hasAllValues(const Array<V>& values) const
		{
			for_iter (i, 0, values.size())
			{
				if (!this->hasValue(values.at(i)))
				{
					return false;
				}
			}
			return true;
		}
		/// @brief Checks for existence of all values.
		/// @param[in] values C-type array of values to check.
		/// @param[in] count Number of values to check.
		/// @return True if all values are present.
		inline bool hasAllValues(const V values[], const int count) const
		{
			for_iter (i, 0, count)
			{
				if (!this->hasValue(values[i]))
				{
					return false;
				}
			}
			return true;
		}
		/// @brief Adds a new pair of key and value into the Map.
		/// @param[in] key Key of the entry.
		/// @param[in] value Value of the entry.
		inline void insert(const K& key, const V& value)
		{
			std::map<K, V>::operator[](key) = value;
		}
		/// @brief Adds all pairs of keys and values from another Map into this one.
		/// @param[in] other Another Map.
		/// @note Entries with already existing keys will not be overwritten.
		inline void insert(const Map<K, V>& other)
		{
			std::map<K, V>::insert(other.begin(), other.end());
		}
		/// @brief Adds all pairs of keys and values from another Map into this one.
		/// @param[in] other Another Map.
		/// @note Entries with already existing keys will be overwritten. In comparison to insert, this function is doing a barrel roll.
		inline void inject(const Map<K, V>& other)
		{
			__foreach_other_map_it(it, other)
			{
				std::map<K, V>::operator[](it->first) = it->second;
			}
		}
		/// @brief Removes a pair of key and value specified by a key.
		/// @param[in] key Key of the entry.
		/// @return True if key was present and removed.
		inline bool removeKey(const K& key)
		{
			if (this->hasKey(key))
			{
				std::map<K, V>::erase(key);
				return true;
			}
			return false;
		}
		/// @brief Removes all pairs of key and value specified by an Array of keys.
		/// @param[in] keys Array of keys.
		/// @return How many keys were removed.
		inline int removeKeys(const Array<K>& keys)
		{
			int result = 0;
			for_iter (i, 0, keys.size())
			{
				if (this->hasKey(keys.at(i)))
				{
					std::map<K, V>::erase(keys.at(i));
					++result;
				}
			}
			return result;
		}
		/// @brief Removes a pair of key and value specified by a value.
		/// @param[in] value Value of the entry.
		/// @return True if value was present and removed.
		inline bool removeValue(const V& value)
		{
			if (this->hasValue(value))
			{
				K result = this->keyOf(value);
				std::map<K, V>::erase(result);
				return true;
			}
			return false;
		}
		/// @brief Removes all pairs of key and value specified by an Array of values.
		/// @param[in] values Array of values.
		/// @return How many values were removed.
		inline int removeValues(const Array<V>& values)
		{
			int result = 0;
			for_iter (i, 0, values.size())
			{
				__foreach_this_map_it(it)
				{
					if (it->second == values.at(i))
					{
						std::map<K, V>::erase(it->first);
						++result;
						break;
					}
				}
			}
			return result;
		}
		/// @brief Gets a random element in Map.
		/// @param[out] value Value of selected random entry.
		/// @return Random element or NULL if Map is empty.
		inline K random(V* value = NULL) const
		{
			if (this->size() == 0)
			{
				throw ContainerEmptyException("random()");
			}
			K key = this->keys()[hrand(this->size())];
			if (value != NULL)
			{
				*value = std::map<K, V>::find(key)->second;
			}
			return key;
		}
		/// @brief Gets a Map of random elements selected from this one.
		/// @param[in] count Number of random elements.
		/// @return Map of random elements selected from this one.
		inline Map<K, V> random(int count) const
		{
			if (count >= this->size())
			{
				return Map<K, V>(*this);
			}
			Map<K, V> result;
			if (count > 0)
			{
				Array<K> keys = this->keys();
				K key;
				for_iter (i, 0, count)
				{
					key = keys.remove_at(hrand(keys.size()));
					result[key] = std::map<K, V>::find(key)->second;
				}
			}
			return result;
		}
		/// @brief Gets a random element in Map and removes it.
		/// @param[out] value Value of selected random entry.
		/// @return Random element or NULL if Map is empty.
		inline K removeRandom(V* value = NULL)
		{
			if (this->size() == 0)
			{
				throw ContainerEmptyException("pop_random()");
			}
			K key = this->keys()[hrand(this->size())];
			if (value != NULL)
			{
				*value = std::map<K, V>::find(key);
			}
			std::map<K, V>::erase(key);
			return key;
		}
		/// @brief Gets a Map of random elements selected from this one and removes them.
		/// @param[in] count Number of random elements.
		/// @return Map of random elements selected from this one.
		inline Map<K, V> removeRandom(int count)
		{
			if (count >= this->size())
			{
				return Map<K, V>(*this);
			}
			Map<K, V> result;
			if (count > 0)
			{
				Array<K> keys = this->keys();
				K key;
				for_iter (i, 0, count)
				{
					key = keys.remove_at(hrand(keys.size()));
					result[key] = std::map<K, V>::find(key);
					std::map<K, V>::erase(key);
				}
			}
			return result;
		}
		/// @brief Finds and returns new Map with entries that match the condition.
		/// @param[in] conditionFunction Function pointer with condition function that takes a key of type K and a value of type V and returns bool.
		/// @return New Map with all matching elements.
		inline Map<K, V> findAll(bool (*conditionFunction)(K, V)) const
		{
			Map<K, V> result;
			__foreach_this_map_it(it)
			{
				if (conditionFunction(it->first, it->second))
				{
					result[it->first] = it->second;
				}
			}
			return result;
		}
		/// @brief Checks if at least one entry matches the condition.
		/// @param[in] conditionFunction Function pointer with condition function that takes a key of type K and a value of type V and returns bool.
		/// @return True if at least one entry matches the condition.
		inline bool matchesAny(bool (*conditionFunction)(K, V)) const
		{
			__foreach_this_map_it(it)
			{
				if (conditionFunction(it->first, it->second))
				{
					return true;
				}
			}
			return false;
		}
		/// @brief Checks if all entries match the condition.
		/// @param[in] conditionFunction Function pointer with condition function that takes a key of type K and a value of type V and returns bool.
		/// @return True if all entries match the condition.
		inline bool matchesAll(bool (*conditionFunction)(K, V)) const
		{
			__foreach_this_map_it(it)
			{
				if (!conditionFunction(it->first, it->second))
				{
					return false;
				}
			}
			return true;
		}
		/// @brief Returns a new Map with all keys and values cast into the type L and S.
		/// @return A new Map with all keys and values cast into the type L and S.
		/// @note Make sure all keys can be cast into type L and all values into type S.
		template <class L, class S>
		inline Map<L, S> cast() const
		{
			Map<L, S> result;
			__foreach_this_map_it(it)
			{
				result[(L)it->first] = (S)it->second;
			}
			return result;
		}
		/// @brief Returns a new Map with all keys and values dynamically cast into the type L and S.
		/// @param[in] includeNulls Whether to include value NULLs that failed to cast.
		/// @return A new Map with all keys and values cast into the type L and S.
		/// @note Be careful not to use this function with non-pointers and classes that don't have virtual functions.
		template <class L, class S>
		inline Map<L, S> dynamicCast(bool includeNulls = false) const
		{
			Map<L, S> result;
			L key;
			S value;
			__foreach_this_map_it(it)
			{
				key = dynamic_cast<L>(it->first);
				value = dynamic_cast<S>(it->second);
				if (key != NULL && (value != NULL || includeNulls))
				{
					result[key] = value;
				}
			}
			return result;
		}
		/// @brief Returns a new Map with all keys and values dynamically cast into the type L and non-dynamically into S.
		/// @return A new Map with all keys and values cast into the type L and S.
		/// @note If dynamic casting fails, it won't be included in the result.
		/// @note Be careful not to use this function with non-pointers and classes that don't have virtual functions.
		template <class L, class S>
		inline Map<L, S> dynamicCastKeys() const
		{
			Map<L, S> result;
			L key;
			__foreach_this_map_it(it)
			{
				key = dynamic_cast<L>(it->first);
				if (key != NULL)
				{
					result[key] = (S)it->second;
				}
			}
			return result;
		}
		/// @brief Returns a new Map with all keys and values cast into the type L and dynamically into S.
		/// @param[in] includeNulls Whether to include value NULLs that failed to cast.
		/// @return A new Map with all keys and values cast into the type L and S.
		/// @note Be careful not to use this function with non-pointers and classes that don't have virtual functions.
		template <class L, class S>
		inline Map<L, S> dynamicCastValues(bool includeNulls = false) const
		{
			Map<L, S> result;
			S value;
			__foreach_this_map_it(it)
			{
				value = dynamic_cast<S>(it->second);
				if (value != NULL || includeNulls)
				{
					result[(L)it->first] = value;
				}
			}
			return result;
		}
		/// @brief Finds and returns value stored at key. In case no value is found, returns the given default value.
		/// @param[in] key Key to retrieve the value of.
		/// @param[in] defaultValue Default value to return if key does not exist.
		/// @return Value stored at key or given default value.
		inline V tryGet(K key, V defaultValue) const
		{
			return (this->hasKey(key) ? std::map<K, V>::find(key)->second : defaultValue);
		}
		/// @brief Same as insert.
		/// @see insert(const Map<K, V>& other)
		inline Map<K, V>& operator+=(const Map<K, V>& other)
		{
			this->insert(other);
			return (*this);
		}
		/// @brief Merges two Mapss.
		/// @param[in] other Second Map to merge with.
		/// @return New Map with elements of second Map added at the end of first Map.
		/// @note Entries with already existing keys in the first map will not be overwritten.
		inline Map<K, V> operator+(const Map<K, V>& other) const
		{
			Map<K, V> result(*this);
			result += other;
			return result;
		}

		DEPRECATED_ATTRIBUTE inline K key_of(const V& value) const															{ return this->keyOf(value); }
		DEPRECATED_ATTRIBUTE inline V value_of(const K& key) const															{ return this->valueOf(key); }
		DEPRECATED_ATTRIBUTE inline bool has_key(const K& key) const														{ return this->hasKey(key); }
		DEPRECATED_ATTRIBUTE inline bool has_keys(const Array<K>& keys) const												{ return this->hasAllKeys(keys); }
		DEPRECATED_ATTRIBUTE inline bool has_keys(const K keys[], const int count) const									{ return this->hasAllKeys(keys, count); }
		DEPRECATED_ATTRIBUTE inline bool has_value(const V& value) const													{ return this->hasValue(value); }
		DEPRECATED_ATTRIBUTE inline bool has_values(const Array<V>& values) const											{ return this->hasAllValues(values); }
		DEPRECATED_ATTRIBUTE inline bool has_values(const V values[], const int count) const								{ return this->hasAllValues(values, count); }
		DEPRECATED_ATTRIBUTE inline bool remove_key(const K& key)															{ return this->removeKey(key); }
		DEPRECATED_ATTRIBUTE inline int remove_keys(const Array<K>& keys)													{ return this->removeKeys(keys); }
		DEPRECATED_ATTRIBUTE inline bool remove_value(const V& value)														{ return this->removeValue(value); }
		DEPRECATED_ATTRIBUTE inline int remove_values(const Array<V>& values)												{ return this->removeValues(values); }
		DEPRECATED_ATTRIBUTE inline K pop_random(V* value = NULL)															{ return this->removeRandom(value); }
		DEPRECATED_ATTRIBUTE inline Map<K, V> pop_random(int count)															{ return this->removeRandom(count); }
		DEPRECATED_ATTRIBUTE inline K remove_random(V* value = NULL)														{ return this->removeRandom(value); }
		DEPRECATED_ATTRIBUTE inline Map<K, V> remove_random(const int count)												{ return this->removeRandom(count); }
		DEPRECATED_ATTRIBUTE inline Map<K, V> find_all(bool(*conditionFunction)(K, V)) const								{ return this->findAll(conditionFunction); }
		DEPRECATED_ATTRIBUTE inline bool matches_any(bool(*conditionFunction)(K, V)) const									{ return this->matchesAny(conditionFunction); }
		DEPRECATED_ATTRIBUTE inline bool matches_all(bool(*conditionFunction)(K, V)) const									{ return this->matchesAll(conditionFunction); }
		DEPRECATED_ATTRIBUTE inline V try_get_by_key(K key, V defaultValue) const											{ return this->tryGet(key, defaultValue); }
		template <class L, class S> DEPRECATED_ATTRIBUTE inline Map<L, S> dyn_cast(bool includeNulls = false) const			{ return this->dynamicCast<L, S>(includeNulls); }
		template <class L, class S> DEPRECATED_ATTRIBUTE inline Map<L, S> dyn_cast_key() const								{ return this->dynamicCastKeys<L, S>(); }
		template <class L, class S> DEPRECATED_ATTRIBUTE inline Map<L, S> dyn_cast_value(bool includeNulls = false) const	{ return this->dynamicCastValues<L, S>(includeNulls); }

	};
	
}

/// @brief Alias for simpler code.
#define hmap hltypes::Map

#endif
