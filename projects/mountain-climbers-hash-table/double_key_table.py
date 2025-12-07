from __future__ import annotations

from typing import Generic, TypeVar, Iterator
from data_structures.hash_table import LinearProbeTable, FullError
from data_structures.referential_array import ArrayR

K1 = TypeVar('K1')
K2 = TypeVar('K2')
V = TypeVar('V')


class DoubleKeyTable(Generic[K1, K2, V]):
    """ 
    Double Hash Table.

    Type Arguments:
        - K1:   1st Key Type. In most cases should be string.
                Otherwise `hash1` should be overwritten.
        - K2:   2nd Key Type. In most cases should be string.
                Otherwise `hash2` should be overwritten.
        - V:    Value Type.

    Unless stated otherwise, all methods have O(1) complexity.
    """

    # No test case should exceed 1 million entries.
    TABLE_SIZES = [5, 13, 29, 53, 97, 193, 389, 769, 1543, 3079, 6151, 12289, 24593, 49157, 98317, 196613, 393241,
                   786433, 1572869]

    HASH_BASE = 31

    def __init__(self, sizes: list | None = None, internal_sizes: list | None = None) -> None:
        """
        Initialization, creation of the underlying array.

        Args:
        - sizes: a list of sizes for the outer hash table
        - internal_sizes: a list of size of the inner hash table

        Returns:
        - None

        Complexity:
        - Worst case: O(1), where the initialization occurs
        - Best case: O(1), where the initialization occurs
        """
        self.size_index = 0
        self.hash_table = LinearProbeTable(sizes)
        self.internal_sizes = internal_sizes
        self.internal_rehash_key = None
        self.internal_rehash_key_pos = None

    def hash1(self, key: K1) -> int:
        """
        Hash the 1st key for insert/retrieve/update into the hash table.

        Args:
        - key: list of keys

        Returns:
        - value: the resulting key for insert/retrieve/update into the hashtable.

        Complexity:
        - Worst case: O(len(key)), in which the loop occurs the amount of times following the amount of elements in key list.
        - Best case: O(len(key)), in which the loop occurs the amount of times following the amount of elements in key list.
        """

        value = 0
        a = 31415
        for char in key:
            value = (ord(char) + a * value) % self.table_size
            a = a * self.HASH_BASE % (self.table_size - 1)
        return value

    def hash2(self, key: K2, sub_table: LinearProbeTable[K2, V]) -> int:
        """
        Hash the 2nd key for insert/retrieve/update into the hash table.

        Args:
        - key: list of keys
        - sub_table: the inner hash table

        Returns:
        - value: the resulting key for insert/retrieve/update into the hashtable.

        Complexity:
        - Worst case: O(len(key)), in which the loop occurs the amount of times following the amount of elements in key list.
        - Best case: O(len(key)), in which the loop occurs the amount of times following the amount of elements in key list.
        """

        value = 0
        a = 31415
        for char in key:
            value = (ord(char) + a * value) % sub_table.table_size
            a = a * self.HASH_BASE % (sub_table.table_size - 1)
        return value

    def _linear_probe(self, key1: K1, key2: K2, is_insert: bool) -> tuple[int, int]:
        """
        Find the correct position for this key in the hash table using linear probing. Index to access in the top-level table, 
        followed by Index to access in the low-level table In a tuple.
        Create the internal hash table if is_insert is true and this is the first pair with key1.

        Args:
        - key1: first key
        - key2: second key
        - is_insert: boolean to check if this function is used to insert item or not

        Returns:
        - a tuple of the first key position, and the second key position

        Raises:
        - KeyError: when the key pair is not in the table, but is_insert is False
        - FullError: when the table is full and nothing can be inserted

        Complexity:
        - Worst case: O(hash1(key1) + N*comp(K1)) + O(hash2(key2) + M*comp(K2)) when we've searched the table of both outer and 
          internal table where N is the table size of outer table, and M is the table size of inner table.
          Omitted Big O notation is O(N + M)
        - Best case: O(hash1(key1) + comp(K1)) + O(hash2(key2) + comp(K2)) index of key1 position of outer table is found at 
          first hashed position, index of key2 position of inner table is found at first hashed position.
          Omitted Big O notation is O(1)
        """
        # Find key1_position
        key1_pos = self._outer_linear_probe(key1, is_insert)
        if self.hash_table.array[key1_pos] is None:
            # Found empty. Create internal hash table
            self.hash_table.array[key1_pos] = (key1, LinearProbeTable(self.internal_sizes))
            self.hash_table.count += 1  # Increase hash_table count

        # Find key2_position
        key2_pos = self._internal_linear_probe(key1_pos, key2, is_insert)
        return key1_pos, key2_pos

    def _internal_linear_probe(self, key1_pos: int, key2: K2, is_insert: bool) -> int:
        """
        Find the correct position for this key in the internal hash table using linear probing.

        Args:
        - key1_pos: integer value for the first key's position
        - key2: second key
        - is_insert: boolean to check if this function is used to insert item or not

        Returns:
        - key2_pos: the position for the key in the inner hash table

        Raises:
        - KeyError: when the key pair is not in the table, but is_insert is False
        - FullError: when the table is full and nothing can be inserted

        Complexity:
        - Worst case: O((hash2(key2) + N*comp(K2)) where N means we've searched the entire table size
          Omitted Big O Notation is O(N)
        - Best case: O(hash2(key2) + comp(K2)) index of key2 position is found at the first hashed position.
          Omitted Big O Notation is O(1)
        """

        # Initial position of key2
        sub_table = self.hash_table.array[key1_pos][1]
        key2_pos = self.hash2(key2, sub_table)

        # Find correct position for key2
        for _ in range(sub_table.table_size):
            if sub_table.array[key2_pos] is None:
                if is_insert:
                    return key2_pos
                else:
                    # raise KeyError if retrieving
                    raise KeyError(key2)
            elif sub_table.array[key2_pos][0] == key2:
                return key2_pos  # Key has been found
            else:
                # Taken by something else. Time to linear probe.
                key2_pos = (key2_pos + 1) % sub_table.table_size

        if is_insert:
            raise FullError("Table is full!")
        else:
            raise KeyError(key2)

    def _outer_linear_probe(self, key1: K1, is_insert: bool) -> int:
        """
        Find the correct position for this key in the hash table using linear probing.

        Args:
        - key1: first key
        - is_insert: boolean to check if this function is used to insert item or not

        Returns:
        - key1_pos: the position for the key in the hash table

        Raises:
        - KeyError: when the key is not in the table, but is_insert is False
        - FullError: when the table is full and nothing can be inserted

        Complexity:
        - Worst case: O(hash1(key1) + N*comp(K1)) where N means we've searched the entire table size.
          Omitted Big O Notation is O(N)
        - Best case: O(hash1(key1) + comp(K1)) first position is empty
          Omitted Big O Notation is O(1)
        """
        # Initial position of key1
        key1_pos = self.hash1(key1)

        for _ in range(self.hash_table.table_size):  # Start traversing
            if self.hash_table.array[key1_pos] is None:
                if is_insert:
                    return key1_pos
                else:
                    # raise KeyError if retrieving from empty spot
                    raise KeyError(key1)
            elif self.hash_table.array[key1_pos][0] == key1:
                return key1_pos  # Key has been found
            else:
                # Taken by something else. Time to linear probe.
                key1_pos = (key1_pos + 1) % self.hash_table.table_size

        if is_insert:
            raise FullError("Table is full!")
        else:
            raise KeyError(key1)

    def iter_keys(self, key: K1 | None = None) -> Iterator[K1 | K2]:
        """
        Returns the iterator object

        Args:
        - key: the key for the top level hash table or None

        Returns:
        - an iterator object for keys

        Complexity:
        - Worst case: O(1), in the return statement
        - Best case: O(1), in the return statement
        """
        return IteratorKey(self, key)

    def keys(self, key: K1 | None = None) -> list[K1]:
        """
        Gathers all the top level keys in the hash table if it is None. If the key is not None, it gathers all the low-level
        keys for the specified top level hash table's key.

        Args:
        - key: the key for the top level hash table or None

        Returns:
        - key_lst: the list of all the keys to be returned

        Complexity:
        - Worst case: O(hash1(key) + N*comp(K1) + O(M)) when we've searched the entirety of the hash table where N is the 
          self.table_size of outer table, and M is the table size of the inner table.
          Omitted Big O Notation is O(N + M)
        - Best case: O(N) where N is self.table_size.
        """

        key_lst = []
        if key is None:
            # :complexity: O(N) where N is self.table_size
            key_lst = self.hash_table.keys()
        else:
            # :complexity: O(hash1(key)) + O(N) where N is self.table_size
            key1_pos = self.hash1(key)  # Use this key first, best case: O(1) complexity
            for _ in range(self.hash_table.table_size):  # Start traversing
                item = self.hash_table.array[key1_pos]
                if item is not None and item[0] is key:
                    key_lst += item[1].keys()  # Key has been found
                    break
                else:
                    # Wrong key. Time to linear probe.
                    key1_pos = (key1_pos + 1) % self.hash_table.table_size
        return key_lst

    def iter_values(self, key: K1 | None = None) -> Iterator[V]:
        """
        Returns the iterator object

        Args:
        - key: the key for the top level hash table or None

        Returns:
        - an iterator object for values

        Complexity:
        - Worst case: O(1), in the return statement
        - Best case: O(1), in the return statement
        """
        return IteratorValue(self, key)

    def values(self, key: K1 | None = None) -> list[V]:
        """
        Gathers all the top level values in the hash table if it is None. If the key is not None, it gathers all the low-level
        keys for the specified top level hash table's key.

        Args:
        - key: the key for the top level hash table or None

        Returns:
        - value_lst: the list of all the values to be returned

        Complexity:
        - Worst case: O(N * M) where N is the table size in the outer array, and M is the table size of the inner array. OR
          O(hash1(key) + N*comp(K1)) + O(M) where N is the table size of the outer table, and M is the table size of the
          inner table, lots of probing.
          Omitted Big O Notation is O(N * M)
        - Best case: O(hash1(key) + comp(K1)) + O(M) where M is the table size of the inner table, no probing.
          Omitted Big O Notation is O(M)
        """
        value_lst = []
        if key is None:
            for item in self.hash_table.array:
                if item is not None:
                    key, sub_table = item
                    # :complexity: O(N) where N is self.table_size.
                    value_lst += sub_table.values()
        else:
            key1_pos = self.hash1(key)  # Use this key first, best case: O(1) complexity
            for _ in range(self.hash_table.table_size):
                # Start traversing
                # :complexity: N*comp(K)
                item = self.hash_table.array[key1_pos]
                if item is not None and item[0] is key:
                    value_lst += item[1].values()  # Key has been found
                    break
                else:
                    # Wrong key. Time to linear probe.
                    key1_pos = (key1_pos + 1) % self.hash_table.table_size
        return value_lst

    def __contains__(self, key: tuple[K1, K2]) -> bool:
        """
        Checks to see if the given key is in the Hash Table

        :complexity: See linear probe.
        """
        try:
            _ = self[key]
        except KeyError:
            return False
        else:
            return True

    def __getitem__(self, key: tuple[K1, K2]) -> V:
        """
        Get the value at a certain key

        Args:
        - key: a tuple that contains the key for the top level hash table, and the low level hash table to be found

        Returns:
        - value the value for the given key

        Raises:
        - KeyError: when the key does not exist

        Complexity:
        - Worst case: O(N + M), where search of the table of both outer and internal table where N is the table size of outer 
          table, and M is the table size of inner table. 
        - Best case: O(1), where index of key1 position of outer table is found at first hashed position, and index of 
          key2 position of inner table is found at first hashed position.
        """

        key1, key2 = key
        key1_pos, key2_pos = self._linear_probe(key1, key2, False)
        sub_table = self.hash_table.array[key1_pos][1]
        return sub_table.array[key2_pos][1]

    def __setitem__(self, key: tuple[K1, K2], data: V) -> None:
        """
        Set a (key, value) pair in our hash table

        Args:
        - key: a tuple that contains the key for the top level hash table, and the low level hash table to be found
        - data: the value to be set to

        Returns:
        - None

        Complexity:
        - Worst case: O(N + M) + O(N^3), where N is the table size of the outer/inner hash table.
          See linear probe and rehash functions
        - Best case: O(1) + O(N), where N is the table size of the outer/inner hash table. There is no probing in linear probe and 
          rehash.
          Omitted Big O Notation: O(N)
        """
        key1, key2 = key
        key1_pos, key2_pos = self._linear_probe(key1, key2, True)
        # complexity best: O(1)
        # complexity worst: O(N + M), N is table size of outer table, M is table size of inner table
        # (key, data) of hash_table has already been inserted through _linear_probe

        # Insert (key, data) into sub_table
        sub_table = self.hash_table.array[key1_pos][1]
        if sub_table.array[key2_pos] is None:
            sub_table.count += 1

        # Insert (key, data) into inner table of hash_table
        sub_table.array[key2_pos] = (key2, data)

        # Rehash if internal hash_table load factor is > 0.5
        if len(sub_table) > sub_table.table_size / 2:
            self.internal_rehash_key = key1
            self.internal_rehash_key_pos = key1_pos
            # :complexity best: O(N)
            # :complexity worst: O(N^3)
            self._rehash()

        # Rehash if outer hash_table load factor is > 0.5
        if len(self.hash_table) > self.table_size / 2:
            self.internal_rehash_key = None
            self.internal_rehash_key_pos = None
            self._rehash()

    def __delitem__(self, key: tuple[K1, K2]) -> None:
        """
        Deletes a (key, value) pair in our hash table

        Args:
        - key: a tuple that contains the key for the top level hash table, and the low level hash table to be deleted

        Returns:
        - None

        Raises:
        - KeyError: when the key doesn't exist

        Complexity:
        - Worst case: O(N + M) + O(N) + O(M), where N is the table size of the outer hash table and M is the table size of 
          the inner hash table
          Omitted Big O Notation: O(N + M)
        - Best case: O(1) + O(N) + O(M), where N is the table size of the outer hash table and M is the table size of the 
          inner hash table.
          Omitted Big O Notation: O(N + M)
        """

        key1, key2 = key
        # complexity best: O(1)
        # complexity worst: O(N + M), N is table size of inner hash table, M is table size of outer hash table
        key1_pos, key2_pos = self._linear_probe(key1, key2, False)

        # Remove the element, complexity: O(1)
        sub_table = self.hash_table.array[key1_pos][1]
        sub_table.array[key2_pos] = None
        sub_table.count -= 1

        # Move sub_table cluster if needed
        if not sub_table.count == 0:
            # :complexity: O(N)
            self._sub_table_move_cluster(key1, key1_pos, key2_pos)

        # If key1 key2 is last pair, clear out internal table for new key1
        if sub_table.count == 0:
            self.hash_table.array[key1_pos] = None
            # Move hash_table cluster
            # :complexity: O(N)
            self._hash_table_move_cluster(key2, key1_pos)

    def _hash_table_move_cluster(self, key2, key1_pos) -> None:
        """
        Move the cluster in the hash table

        Args:
        - key2: The key for the bottom level hash table
        - key1_pos: The position of the key in the top level hash table

        Returns:
        - None

        Complexity:
        - Worst case: O(N), where N is the table size of the hash table
        - Best case: O(N), where N is the table size of the hash table
        """
        # Start moving over the cluster
        key1_pos = (key1_pos + 1) % self.table_size
        while self.hash_table.array[key1_pos] is not None:
            key1, sub_table = self.hash_table.array[key1_pos]
            self.hash_table.array[key1_pos] = None
            # Reinsert.
            new_key1_pos, _ = self._linear_probe(key1, key2, True)
            self.hash_table.array[new_key1_pos] = (key1, sub_table)
            key1_pos = (key1_pos + 1) % self.table_size

    def _sub_table_move_cluster(self, key1, key1_pos, key2_pos) -> None:
        """
        Moce the cluster of the internal table of a key in the hash table

        Args:
        - key1: The key for the top level hash table
        - key1_pos: The position of the key in the top level hash table
        - key2_pos: The position of the key in the bottom level hash table

        Returns:
        - None

        Complexity:
        - Worst case: O(N), where N is the table size of the internal hash table
        - Best case: O(N), where N is the table size of the internal hash table
        """
        # Start moving over the cluster
        sub_table = self.hash_table.array[key1_pos][1]
        key2_pos = (key2_pos + 1) % sub_table.table_size
        while sub_table.array[key2_pos] is not None:
            key2, value = sub_table.array[key2_pos]
            sub_table.array[key2_pos] = None
            # Reinsert.
            _, new_key2_pos = self._linear_probe(key1, key2, True)
            sub_table.array[new_key2_pos] = (key2, value)
            key2_pos = (key2_pos + 1) % sub_table.table_size

    def _rehash(self) -> None:
        """
        Need to resize table and reinsert all values. Every key in the hash_table is checked if the internal hash table requires 
        resizing. This function provides the boolean to assess the need to resize the tables within the hash_table.

        Args:
        - None

        Returns:
        - None

        Complexity:
        - Worst case: O(N^3), where N is the table size of the inner hash_table
        - Best case: O(N), where N is the table size of the outer/inner hash table
        """
        # Resize the hash_table
        if self.internal_rehash_key is None and self.internal_rehash_key_pos is None:
            self._hash_table_resizing()
            return
        else:
            # Resize the sub_table
            self._sub_table_resizing(self.internal_rehash_key, self.internal_rehash_key_pos)

    def _sub_table_resizing(self, key1: K1, key1_pos: int) -> None:
        """
        Resizes the sub_table of specific hash_table

        Args:
        - key1: the top level key list
        - key1_pos: the position of the given top level key

        Returns:
        - None

        Complexity:
        - Worst case: O(N * (N+M)), where N is the size of the outer hash table, and M is the table size of the inner hash table
        - Best case: O(N), where N is the table size of the outer hash table
        see linear probe for more understanding of complexity
        """
        sub_table = self.hash_table.array[key1_pos][1]
        old_array = sub_table.array
        sub_table.size_index += 1
        if sub_table.size_index >= len(sub_table.TABLE_SIZES):
            # Cannot be resized further.
            return
        sub_table.array = ArrayR(sub_table.TABLE_SIZES[sub_table.size_index])
        sub_table.count = 0

        # Loop the old_array and reinsert back into new hash sub_table
        # :complexity: O(N), where N is the table size of the inner hash table
        for item in old_array:
            if item is not None:
                key2, data = item
                # :complexity best: O(1)
                # :complexity worse: O(N + M)
                self[key1, key2] = data

    def _hash_table_resizing(self) -> None:
        """
        Resizes the hash table

        Args:
        - None

        Returns:
        - None

        Complexity:
        - Worst case: O(N * (len(self) + N^2*comp(K)) ), where N is the length of the table size. Involves lots of probing.
          Omitted Big O Notation: O(N * N^2comp(K))
        - Best case: O(N * (len(key) + comp(key))), where N is the table size of the outer hash table. No probing.
          Omitted Big O Notation: O(N)
        """
        old_array = self.hash_table.array
        self.hash_table.size_index += 1
        if self.hash_table.size_index >= len(self.hash_table.TABLE_SIZES):
            # Cannot be resized further.
            return
        self.hash_table.array = ArrayR(self.hash_table.TABLE_SIZES[self.hash_table.size_index])
        self.hash_table.count = 0

        # Loop the old_array and reinsert back into new hash_table
        for item in old_array:
            if item is not None:
                key, data = item
                # complexity: O(len(key))
                key1_pos = self.hash1(key)
                # Reinsert values into hash_table
                for _ in range(self.table_size):
                    if self.hash_table.array[key1_pos] is None:
                        self.hash_table.array[key1_pos] = (key, data)
                        break
                    else:
                        # Taken by something else. Time to linear probe.
                        key1_pos = (key1_pos + 1) % self.table_size

    @property
    def table_size(self) -> int:
        """
        Return the current size of the table (different from the length)

        Args:
        - None

        Returns:
        - the table size

        Complexity
        - Worst case: O(1), returning the length of the hash table.
        - Best case: O(1), returning the length of the hash table.
        """
        return len(self.hash_table.array)

    def __len__(self) -> int:
        """
        Returns number of elements in the hash table

        Args:
        - None

        Returns:
        - The number of elements in the hash table

        Complexity: 
        - Worst case: O(n), where n is the number of elements in the hash table
        - Best case: O(n), where n is the number of elements in the hash table
        """
        return self.hash_table.count

    def __str__(self) -> str:
        """
        Returns all they key/value pairs in our hash table (no particular order).

        Args:
        - None

        Returns:
        - None

        Complexity:
        - Worst case: O(N * (str(key1) + (M * str(key2) + str(value))) where N is the hash_table size and M is the sub_table within
          each position of hash_table
        - Best case: O(N * (str(key1) + (M * str(key2) + str(value))) where N is the hash_table size and M is the sub_table within
          each position of hash_table
        """
        result = ""
        for item in self.hash_table.array:
            if item is not None:
                (key1, table) = item
                for sub_item in table.array:
                    if sub_item is not None:
                        (key2, data) = sub_item
                        result += "(" + str(key1) + "," + str(key2) + "," + str(data) + ")\n"
        return result


class IteratorValue:
    """
    Class Iterator for value
    """
    def __init__(self, double_key_table: DoubleKeyTable, key:K1|None) -> None:
        """
        Initialization

        Args:
        - double_key_table: type DoubleKeyTable, that is the double hash table
        - key: The top-level hash table's key

        Returns:
        - None

        Complexity:
        - Worst case: O(1), for each initialization.
        - Best case: O(1), for each initailization.
        """
        self.double_key_table = double_key_table
        self.key = key 
        self.index = 0
        self.temporary_table = None

    def __next__(self) -> V:
        """
        Magic method that will return they next value.

        Args:
        - None

        Returns:
        - the next value

        Raises: 
        - StopIteration: when the iteration completed, and no more values can be iterated

        Complexity:
        - Worst case: O(N*M), where N is the table size in the outer array, and M is the table size of the inner array.
                      OR
                      O(hash1(key) + N*comp(K1)) + O(M) where N is the table size of the outer table, and M is the table size of the
                      inner table, lots of probing.
                      Omitted Big O Notation is O(N * M)
        - Best case: O(hash1(key) + comp(K1)) + O(M), where M is the table size of the inner table, no probing.
                     Omitted Big O Notation is O(M)

        Both cases occurs when the .values is being called.
        """
        self.index += 1 # O(1)
        iter_list = self.double_key_table.values(self.key) # O(hash1(key) + comp(K1)) + O(M)    
        if self.temporary_table == iter_list : # O(1)
            pass
        else :
            self.index = 0
            self.temporary_table = iter_list

        try :
            iter_list[self.index - 1] 
        except :
            raise StopIteration
        
        return iter_list[self.index - 1] 

    def __iter__(self) -> IteratorValue:
        """
        Returns an iterator object

        Args:
        - None

        Returns:
        - iterator object

        Complexity:
        - Worst case: O(1), the return
        - Best case: O(1), the return
        """
        return self # O(1)
    
class IteratorKey:
    """
    Class Iterator for key
    """
    def __init__(self, double_key_table: DoubleKeyTable, key:K1|None) -> None:
        """
        Initialization

        Args:
        - double_key_table: type DoubleKeyTable, that is the double hash table
        - key: The top-level hash table's key

        Returns:
        - None

        Complexity:
        - Worst case: O(1), for each initialization.
        - Best case: O(1), for each initailization.
        """
        self.double_key_table = double_key_table
        self.key = key 
        self.index = 0
        self.temporary_table = None

    def __next__(self) -> K1|K2:
        """
        Magic method that will return they next key.

        Args:
        - None

        Returns:
        - the next key

        Raises: 
        - StopIteration: when the iteration completed, and no more keys can be iterated

        Complexity:
        - Worst case: O(hash1(key) + N*comp(K1) + O(M)) when we've searched the entirety of the hash table where N
                      is the self.table_size of outer table, and M is the table size of the inner table.
                      Omitted Big O Notation is O(N + M)
        - Best case: O(N) where N is self.table_size.

        Both cases occurs when the .keys is being called.
        """
        self.index += 1
        iter_list = self.double_key_table.keys(self.key)
        if self.temporary_table == iter_list :
            pass
        else :
            self.index = 0
            self.temporary_table = iter_list

        try :
            iter_list[self.index - 1] 
        except :
            raise StopIteration
        
        return iter_list[self.index - 1] 

    def __iter__(self) -> IteratorKey:
        """
        Returns an iterator object

        Args:
        - None

        Returns:
        - iterator object

        Complexity:
        - Worst case: O(1), the return
        - Best case: O(1), the return
        """
        return self

if __name__ == "__main__":
    pass