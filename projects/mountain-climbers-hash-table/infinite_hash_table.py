from __future__ import annotations
from typing import Generic, TypeVar

from data_structures.linked_stack import LinkedStack
from data_structures.referential_array import ArrayR

K = TypeVar("K")
V = TypeVar("V")


class InfiniteHashTable(Generic[K, V]):
    """
    Infinite Hash Table.

    Type Arguments:
        - K:    Key Type. In most cases should be string.
                Otherwise `hash` should be overwritten.
        - V:    Value Type.

    Unless stated otherwise, all methods have O(1) complexity.
    """

    TABLE_SIZE = 27

    def __init__(self) -> None:
        """
        Initialization

        Args:
        - None

        Returns:
        - None

        Complexity:
        - Worst case: O(n), for the initialization of an ArrayR
        - Best case: O(1), for the initialization of an ArrayR
        """
        self.hash_table: ArrayR[tuple[K, V]] = ArrayR(self.TABLE_SIZE)
        self.level = 0
        self.count = 0

    def hash(self, key: K) -> int:
        """
        hash function for all keys

        Args:
        - key: the key to be hashed 

        Returns:
        - the position of where the key can be placed in

        Complexity:
        - Worst case: O(1)
        - Best case: O(1)
        """
        if self.level < len(key):
            return ord(key[self.level]) % (self.TABLE_SIZE - 1)
        return self.TABLE_SIZE - 1

    def __getitem__(self, key: K) -> V:
        """
        Get the value at a certain key

        Args:
        - key: the key that is used to get the item 

        Returns:
        - the value for the given key

        Raises:
        - KeyError: when the key doesn't exist

        Complexity:
        - Worst case: O(N * comp(K)), where N is the maximum depth of the hash_table. A lot of traversal into the value of the hash_table.
          Omitted Big O Notation: O(N)
        - Best case: O(1 * comp(K)), where there is no traversal into the hash_table value.
          Omitted Big O Notation: O(1)
        """
        curr_table = self.hash_table

        while True:  # O(N), where N is the depth of the hash_table
            key_pos = self.hash(key)
            if curr_table[key_pos] is not None:  # O(comp(K))
                item = curr_table[key_pos]
                if item[0] == key and type(item[1]) is not ArrayR:
                    # Check if the value is the data of the key or another hash_table
                    self.level = 0
                    return item[1]
                elif type(item[1]) is ArrayR:
                    # There are clashing keys, dive deeper into hierarchy
                    self.level += 1
                    curr_table = item[1]
                else:
                    raise KeyError(key)

    def __setitem__(self, key: K, value: V) -> None:
        """
        Set an (key, value) pair in our hash table.

        Args:
        - key: the key to set the item to 
        - value: the value to be set onto the key

        Returns:
        - None

        Complexity:
        - Worst case: O(N * comp[K] * N), where N is the maximum depth of the hash_table. A lot of traversal into the value 
          of the hash_table. A lot of reinsert action for resolving the collisions of key-value pair by making more hash tables.
          Omitted Big O Notation: O(N^2)
        - Best case: O(1 * comp[K]), where there is no traversal into the hash_table value.
          Omitted Big O Notation: O(1)
        """
        item_stack = LinkedStack(self.TABLE_SIZE)
        curr_table = self.hash_table

        while True:  # O(N), where N is the depth of the hash_table
            key_pos = self.hash(key)
            if curr_table[key_pos] is None:  # Position is empty, O(comp(K))
                curr_table[key_pos] = (key, value)  # insert (key, value)
                self.count += 1  # Add count
                if not item_stack.is_empty():  # More keys to insert
                    # Continue While loop
                    key, value = item_stack.pop()
                    curr_table = self.hash_table
                    self.level = 0
                else:
                    self.level = 0
                    break
            else:  # Position has (key, data)
                if type(curr_table[key_pos][1]) is not ArrayR:  # Conflicting (key, value)
                    if not curr_table[key_pos][0] == key:  # Check for duplicate key, O(comp(K))
                        item_stack.push(curr_table[key_pos])  # Stash (key, data) into stack
                        self.count -= 1  # Update count
                    # Create new hash_table as value
                    curr_table[key_pos] = (key[:self.level + 1], ArrayR(self.TABLE_SIZE))
                # Traverse deeper into the hash_table
                self.level += 1
                curr_table = curr_table[key_pos][1]

    def __delitem__(self, key: K) -> None:
        """
        Deletes a (key, value) pair in the hash table.

        Args:
        - key: the key to be deleted

        Returns:
        - None

        Complexity:
        - Worst case: O(N + M * N^2), where N is the depth of the hash_table, and M is the number of elements in the key_lst.
          Omitted Big O Notation: O(MN^2)
        - Best case: O(1) when deleting a single key-value pair within the parent table.
        """

        # Check if deleted key is in parent table
        key_pos = self.hash(key)
        if type(self.hash_table[key_pos][1]) is not ArrayR and self.hash_table[key_pos][0] is key:
            self.hash_table[key_pos] = None
            self.count -= 1
        else:
            # Get all (key, value) and reinsert.
            # Do not keep deleted key
            curr_table = self.hash_table[key_pos][1]
            key_lst = self._key_recursion(curr_table, [], key)  # O(N), where N is the depth of the hash table
            self.hash_table[key_pos] = None
            # Minus self.count
            self.count -= 1

            # Reinsert keys and minus self.count, O(M), where M is the number of items in the key_lst to insert
            for item in key_lst:
                key, data = item
                self[key] = data
                self.count -= 1

    def _key_recursion(self, curr_table: ArrayR, lst: list, del_key) -> list:
        """
        Recursion used in delete item to find the list of keys

        Args:
        - curr_table: the current position of the table
        - lst: list of items used to stores key and value pairs
        - del_key: the key to be deleted

        Returns:
        - lst: list of items that stores key and value pairs

        Complexity:
        - Worst case: O(N), where N is the depth of the hash table
        - Best case: O(N), where N is the depth of the hash table
        """

        for item in curr_table:
            if item is not None:
                key, data = item
                if type(data) is ArrayR:
                    self._key_recursion(data, lst, del_key)
                else:
                    if key is not del_key:
                        lst += [(key, data)]
        return lst

    def __len__(self) -> int:
        """
        finds the number of elements in the infinite hash table

        Args:
        - None

        Returns:
        - the total number of elements in the infinite hash table

        Complexity:
        - Worst case: O(N), where N is the number of elements in the infinite hash table
        - Best case: O(N), where N is the number of elements in the infinite hash table
        """
        return self.count

    def __str__(self) -> str:
        """
        String representation

        Args:
        - None

        Returns:
        - ret_str: the string representation of the infinite hash table

        Complexity:
        - Worst case: O(N * M) + O(P), where N is the size of the parent table, M is the depth of the hash_table, and P is 
          the number of elements in ret_lst.
        - Best case: O(N * M) + O(P), where N is the size of the parent table, M is the depth of the hash_table, and P is the 
          number of elements in ret_lst.
        """

        ret_lst = self._str_recursion(self.hash_table, [])
        ret_str = ""
        if ret_lst is not None:
            for item in ret_lst:
                key, data = item
                ret_str += "({}, {})\n".format(key, data)
        return ret_str

    def _str_recursion(self, curr_hash_table: ArrayR, lst: list) -> list:
        """
        Recursion function used for string representation

        Args:
        - curr_hash_table: the current position in the hash table
        - lst: list of elements

        Returns:
        - lst: list of elements to be represented

        Complexity:
        - Worst case: O(N * M), where N is the size of the parent table, and M is the depth of the hash_table
        - Best case: O(N * M), where N is the size of the parent table, and M is the depth of the hash_table
        """
        for item in curr_hash_table:
            if item is not None:
                key, data = item
                if type(data) is ArrayR:
                    self._str_recursion(data, lst)
                else:
                    lst += [(key, data)]
        return lst

    def get_location(self, key) -> list:
        """
        Get the sequence of positions required to access this key

        Args:
        - key: the key to be searched for 

        Returns:
        - ret_lst: the list that stores key positions

        Raises:
        - KeyError: when the key doesn't exist

        Complexity:
        - Worst case: O(N * comp(K)), where N is the depth of the hash table, where the searched key is in the deepest part 
          of the hash table or does not exist.
          Omitted Big O Notation: O(N)
        - Best case: O(1 * comp(K)), where the location of the searched key is in the parent table.
          Omitted Big O Notation: O(1)
        """
        ret_lst = []
        curr_table = self.hash_table
        while True:
            key_pos = self.hash(key)
            if curr_table[key_pos] is not None:
                item = curr_table[key_pos]
                if item[0] is key and type(item[1]) is not ArrayR:
                    self.level = 0
                    ret_lst += [key_pos]
                    return ret_lst
                elif type(item[1]) is ArrayR:
                    self.level += 1
                    ret_lst += [key_pos]
                    curr_table = item[1]
                else:
                    raise KeyError(key)

    def __contains__(self, key: K) -> bool:
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
if __name__ == "__main__":
    pass