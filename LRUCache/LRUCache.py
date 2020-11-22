#!/usr/bin/env python
# LRUCache.py

from collections import OrderedDict


class LRUCache:
    """
    A correctly constructed LRU Cache class performing four tasks:
    *** You must initialize the maximum size of the cache ***
    1. Put the value of a key
    2. Get the value of a key
    3. Delete the value of a key
    4. Reset the Cache (i.e. Delete the value of all keys in the cache)
    """

    # initialising capacity (The maximum size of the cache)
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def put(self, key: int, value: int) -> None:
        """ .put function add or update the value of a key """

        self.cache[key] = value

        # The most recently used key goes to the end of the cache
        self.cache.move_to_end(key)

        # Pop the least recently used key if the length of the cache passed its maximum
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)

    def get(self, key: int) -> int:
        """ .get function returns the value of a key that is queried in O(1) """

        # If the key doesn't exist, returns -1
        if key not in self.cache:
            return -1
        # Else, returns the value of the key and the key goes to the end of the cache (most recently used)
        else:
            self.cache.move_to_end(key)
            return self.cache[key]

    # ".delete" deletes the (key, value) pair
    def delete(self, key: int):
        """ .delete function deletes the (key, value) pair """

        # If the key doesn't exist, no-op (i.e. pass)
        if key not in self.cache:
            pass
        # Else, deletes the pair
        else:
            del self.cache[key]

    def reset(self):
        """ .reset function removes all items from the cache """

        self.cache.clear()
