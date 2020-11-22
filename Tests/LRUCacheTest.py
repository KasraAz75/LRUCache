#!/usr/bin/env python
# LRUCacheTest.py

import unittest
from collections import OrderedDict
from LRUCache import LRUCache


class LRUCacheTest(unittest.TestCase):
    """
    Unit tests for common cases in LRUCache class
    """

    def test_put(self):
        """ Test if Put function add or update the value of a key correctly. """

        cache = LRUCache(2)
        cache.put(1, 1)
        self.assertEqual(cache.cache, OrderedDict([(1, 1)]),
                         f"The result must be {OrderedDict([(1, 1)])} instead of {cache.cache}")
        cache.put(2, 2)
        self.assertEqual(cache.cache, OrderedDict([(1, 1), (2, 2)]),
                         f"The result must be {OrderedDict([(1, 1), (2, 2)])} instead of {cache.cache}")
        cache.put(3, 3)
        self.assertEqual(cache.cache, OrderedDict([(2, 2), (3, 3)]),
                         f"The result must be {OrderedDict([(2, 2), (3, 3)])} instead of {cache.cache}")

    def test_get(self):
        """ Test if Get function returns the value of a key correctly. """

        cache = LRUCache(2)
        self.assertEqual(cache.get(1), -1,
                         "It must return -1 (i.e. key doesn't exist in the cache")
        cache.put(1, 1)
        self.assertEqual(cache.get(1), 1,
                         "It must return 1 (i.e. key exists in the cache")
        cache.put(2, 2)
        cache.get(1)
        self.assertEqual(cache.cache, OrderedDict([(2, 2), (1, 1)]),
                         f"The result must be {OrderedDict([(2, 2), (1, 1)])} instead of {cache.cache}")
        cache.get(2)
        self.assertEqual(cache.get(2), 2,
                         "It must return 2 (i.e. key exists in the cache")

    def test_delete(self):
        """ Test if Delete function actually deletes the (key, value) pair from the cache. """

        cache = LRUCache(2)
        cache.put(1, 1)
        cache.delete(2)
        self.assertEqual(cache.cache, OrderedDict([(1, 1)]),
                         f"The result must be {OrderedDict([(1, 1)])} instead of {cache.cache}")
        cache.delete(1)
        self.assertEqual(cache.cache, OrderedDict(),
                         f"The result must be {OrderedDict()} instead of {cache.cache}")

    def test_reset(self):
        """ Test if Reset function removes all items in the cache. """

        cache = LRUCache(2)
        cache.put(1, 1)
        cache.reset()
        self.assertEqual(cache.cache, OrderedDict(),
                         f"The result must be {OrderedDict()} instead of {cache.cache}")
        cache.put(1, 1)
        cache.put(2, 2)
        cache.reset()
        self.assertEqual(cache.cache, OrderedDict(),
                         f"The result must be {OrderedDict()} instead of {cache.cache}")

    def test_all(self):
        """ Test all functions! """

        cache = LRUCache(2)
        cache.put(1, 1)
        cache.put(2, 2)
        cache.get(1)
        cache.put(3, 3)
        cache.get(2)
        cache.get(3)
        cache.delete(3)
        cache.reset()
        cache.put(4, 4)
        self.assertEqual(cache.cache, OrderedDict([(4, 4)]),
                         f"The result must be {OrderedDict([(4, 4)])} instead of {cache.cache}")

if __name__ == '__main__':
    unittest.main()
