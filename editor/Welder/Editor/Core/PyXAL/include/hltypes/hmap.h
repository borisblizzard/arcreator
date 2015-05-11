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
/// Encapsulates std::map and adds high level methods.

#ifndef HLTYPES_MAP_H
#define HLTYPES_MAP_H

#include <map>

#include "harray.h"
#include "hstring.h"

/// @brief Provides a simpler syntax to iterate through a Map.
#define foreach_map(type_key, type_value, name, container) for (std::map< type_key, type_value >::iterator name = container.begin(); name != container.end(); ++name)
#define foreachc_map(type_key, type_value, name, container) for (std::map< type_key, type_value >::const_iterator name = container.begin(); name != container.end(); ++name)
/// @brief Provides a simpler syntax to iterate through a Map with String as key.
#define foreach_m(type, name, container) for (std::map< hstr, type >::iterator name = container.begin(); name != container.end(); ++name)
#define foreachc_m(type, name, container) for (std::map< hstr, type >::const_iterator name = container.begin(); name != container.end(); ++name)
/// @brief Internal provider for simpler syntax to iterate through a Map with String as key.
#define __foreach_this_map_it(name) for (iterator_map_t name = stdmap::begin(); name != stdmap::end(); ++name)
/// @brief Internal provider for simpler syntax to iterate through a Map with String as key.
#define __foreach_other_map_it(name, other) for (iterator_map_t name = other.begin(); name != other.end(); ++name)
/// @brief Alias for simpler code.
#define stdmap std::map<K, V>

namespace hltypes
{
	/// @brief Encapsulates std::map and adds high level methods.
	template <class K, class V>
	class Map : public stdmap
	{
	private:
		typedef typename stdmap::const_iterator iterator_map_t;
		typedef typename std::vector<K>::const_iterator iterator_map_key_t;
	public:
		/// @brief Empty constructor.
		inline Map() : stdmap()
		{
		}
		/// @brief Copy constructor.
		/// @param[in] other Map to copy.
		inline Map(const Map<K, V>& other) : stdmap(other)
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
			return stdmap::operator[](key);
		}
		/// @brief Same as key_of.
		/// @see key_of
		inline K operator()(const V& value) const
		{
			return this->key_of(value);
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
			return stdmap::size();
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
		inline Array<V> values(Array<K> keys)
		{
			Array<V> result;
			for (iterator_map_key_t it = keys.begin(); it != keys.end(); ++it) // don't change, requires a const iterator
			{
				result += stdmap::operator[](*it);
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
			if (!this->has_keys(keys))
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
			if (!this->has_keys(keys))
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
		inline K key_of(const V& value) const
		{
			__foreach_this_map_it(it)
			{
				if (it->second == value)
				{
					return it->first;
				}
			}
			return stdmap::end()->first;
		}
		/// @brief Returns value of specified key.
		/// @param[in] key Key of the given value.
		/// @return Value of specified key.
		inline V value_of(const K& key) const
		{
			return stdmap::find(key)->second;
		}
		/// @brief Checks for existence of a key.
		/// @param[in] key Key to check.
		/// @return True if key is present.
		inline bool has_key(const K& key) const
		{
			return (stdmap::find(key) != stdmap::end());
		}
		/// @brief Checks for existence of all keys.
		/// @param[in] keys Array of keys to check.
		/// @return True if all keys are present.
		inline bool has_keys(const Array<K>& keys) const
		{
			iterator_map_t end = stdmap::end();
			for_iter (i, 0, keys.size())
			{
				if (stdmap::find(keys.at(i)) == end)
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
		inline bool has_keys(const K keys[], const int count) const
		{
			iterator_map_t end = stdmap::end();
			for_iter (i, 0, count)
			{
				if (stdmap::find(keys[i]) == end)
				{
					return false;
				}
			}
			return true;
		}
		/// @brief Checks for existence of a value.
		/// @param[in] value Value to check.
		/// @return True if value is present.
		inline bool has_value(const V& value) const
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
		/// @brief Checks for existence of all values.
		/// @param[in] values Array of values to check.
		/// @return True if all values are present.
		inline bool has_values(const Array<V>& values) const
		{
			for_iter (i, 0, values.size())
			{
				if (!this->has_value(values.at(i)))
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
		inline bool has_values(const V values[], const int count) const
		{
			for_iter (i, 0, count)
			{
				if (!this->has_value(values[i]))
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
			stdmap::operator[](key) = value;
		}
		/// @brief Adds all pairs of keys and values from another Map into this one.
		/// @param[in] other Another Map.
		/// @note Entries with already existing keys will not be overwritten.
		inline void insert(const Map<K, V>& other)
		{
			stdmap::insert(other.begin(), other.end());
		}
		/// @brief Adds all pairs of keys and values from another Map into this one.
		/// @param[in] other Another Map.
		/// @note Entries with already existing keys will be overwritten. In comparison to insert, this function is doing a barrel roll.
		inline void inject(const Map<K, V>& other)
		{
			__foreach_other_map_it(it, other)
			{
				stdmap::operator[](it->first) = it->second;
			}
		}
		/// @brief Removes a pair of key and value specified by a key.
		/// @param[in] key Key of the entry.
		inline void remove_key(const K& key)
		{
			if (this->has_key(key))
			{
				stdmap::erase(key);
			}
		}
		/// @brief Removes all pairs of key and value specified by an Array of keys.
		/// @param[in] keys Array of keys.
		inline void remove_keys(const Array<K>& keys)
		{
			for_iter (i, 0, keys.size())
			{
				if (this->has_key(keys.at(i)))
				{
					stdmap::erase(keys.at(i));
				}
			}
		}
		/// @brief Removes a pair of key and value specified by a value.
		/// @param[in] value Value of the entry.
		inline void remove_value(const V& value)
		{
			if (this->has_value(value))
			{
				K result = this->key_of(value);
				stdmap::erase(result);
			}
		}
		/// @brief Removes all pairs of key and value specified by an Array of values.
		/// @param[in] values Array of values.
		inline void remove_values(const Array<V>& values)
		{
			for_iter (i, 0, values.size())
			{
				__foreach_this_map_it(it)
				{
					if (it->second == values.at(i))
					{
						stdmap::erase(it->first);
						break;
					}
				}
			}
		}
		/// @brief Gets a random element in Map.
		/// @param[out] value Value of selected random entry.
		/// @return Random element or NULL if Map is empty.
		inline K random(V* value = NULL) const
		{
			if (this->size() == 0)
			{
				throw container_empty_error("random()");
			}
			K key = this->keys()[hrand(this->size())];
			if (value != NULL)
			{
				*value = stdmap::find(key)->second;
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
					result[key] = stdmap::find(key)->second;
				}
			}
			return result;
		}
		/// @brief Gets a random element in Map and removes it.
		/// @param[out] value Value of selected random entry.
		/// @return Random element or NULL if Map is empty.
		inline K pop_random(V* value = NULL)
		{
			if (this->size() == 0)
			{
				throw container_empty_error("pop_random()");
			}
			K key = this->keys()[hrand(this->size())];
			if (value != NULL)
			{
				*value = stdmap::find(key);
			}
			stdmap::erase(key);
			return key;
		}
		/// @brief Gets a Map of random elements selected from this one and removes them.
		/// @param[in] count Number of random elements.
		/// @return Map of random elements selected from this one.
		inline Map<K, V> pop_random(int count)
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
					result[key] = stdmap::find(key);
					stdmap::erase(key);
				}
			}
			return result;
		}
		/// @brief Same as pop_random.
		/// @see pop_random().
		inline K remove_random(V* value = NULL)
		{
			return this->pop_random(value);
		}
		/// @brief Same as pop_random.
		/// @see pop_random(const int count).
		inline Map<K, V> remove_random(const int count)
		{
			return this->pop_random(count);
		}
		/// @brief Finds and returns new Map with entries that match the condition.
		/// @param[in] condition_function Function pointer with condition function that takes a key of type K and a value of type V and returns bool.
		/// @return New Map with all matching elements.
		inline Map<K, V> find_all(bool (*condition_function)(K, V)) const
		{
			Map<K, V> result;
			__foreach_this_map_it(it)
			{
				if (condition_function(it->first, it->second))
				{
					result[it->first] = it->second;
				}
			}
			return result;
		}
		/// @brief Checks if at least one entry matches the condition.
		/// @param[in] condition_function Function pointer with condition function that takes a key of type K and a value of type V and returns bool.
		/// @return True if at least one entry matches the condition.
		inline bool matches_any(bool (*condition_function)(K, V)) const
		{
			__foreach_this_map_it(it)
			{
				if (condition_function(it->first, it->second))
				{
					return true;
				}
			}
			return false;
		}
		/// @brief Checks if all entries match the condition.
		/// @param[in] condition_function Function pointer with condition function that takes a key of type K and a value of type V and returns bool.
		/// @return True if all entries match the condition.
		inline bool matches_all(bool (*condition_function)(K, V)) const
		{
			__foreach_this_map_it(it)
			{
				if (!condition_function(it->first, it->second))
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
		/// @param[in] include_nulls Whether to include value NULLs that failed to cast.
		/// @return A new Map with all keys and values cast into the type L and S.
		/// @note Be careful not to use this function with non-pointers and classes that don't have virtual functions.
		template <class L, class S>
		inline Map<L, S> dyn_cast(bool include_nulls = false) const
		{
			Map<L, S> result;
			L key;
			S value;
			__foreach_this_map_it(it)
			{
				key = dynamic_cast<L>(it->first);
				value = dynamic_cast<S>(it->second);
				if (key != NULL && (value != NULL || include_nulls))
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
		inline Map<L, S> dyn_cast_key() const
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
		/// @param[in] include_nulls Whether to include value NULLs that failed to cast.
		/// @return A new Map with all keys and values cast into the type L and S.
		/// @note Be careful not to use this function with non-pointers and classes that don't have virtual functions.
		template <class L, class S>
		inline Map<L, S> dyn_cast_value(bool include_nulls = false) const
		{
			Map<L, S> result;
			S value;
			__foreach_this_map_it(it)
			{
				value = dynamic_cast<S>(it->second);
				if (value != NULL || include_nulls)
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
		inline V try_get_by_key(K key, V defaultValue) const
		{
			return (this->has_key(key) ? stdmap::find(key)->second : defaultValue);
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

	};
	
}

/// @brief Alias for simpler code.
#define hmap hltypes::Map

#endif
