# LRUCache
LRUCache implements a **Least-Recently Used** (LRU) Cache capable of performing four tasks:

1. **put:** It adds or updates the value of a key in the cache.
2. **get:**  It returns the value of a key in the cache. If the key does not exist, it returns -1 (i.e. the key doesn't exist).
3. **delete:** It receives a key as its input and removes the (key, value) pair from the cache. If the key does not exist, no-op (i.e. does nothing).
4. **reset:** It removes all items from the cache.

## Other information
A correctly constructed LRU Cache will have its maximum capacity set at the time of the construction, and when adding new keys that cause the capacity to be exceeded, the “least recently used” item needs to be identified and discarded.

- [```LRUCache:```](https://github.com/KasraAz75/LRUCache/blob/main/LRUCache/LRUCache.py)implements **LRU** cache and its four functions after initializing the maximum capacity of the cache.

- [```LRUCacheTest:```](https://github.com/KasraAz75/LRUCache/blob/main/Tests/LRUCacheTest.py)includes all common unit tests of LRUCache




## Dependencies
- [collections](https://docs.python.org/3/library/collections.html):
  - [OrderedDirect](https://docs.python.org/3/library/collections.html#collections.OrderedDict)


## Basic Usage
```ruby
from LRUCache import LRUCache

# Initialising a cache with the maximum size of 2
lRUCache = LRUCache(2)

lRUCache.put(1, 1)  # cache is {1=1}
lRUCache.put(2, 2)  # cache is {1=1, 2=2}
lRUCache.get(1)     # return 1
lRUCache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
lRUCache.get(2)     # returns -1 (not found)
lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
lRUCache.get(1)     # return -1 (not found)
lRUCache.get(3)     # return 3
lRUCache.get(4)     # return 4
lRUCache.delete(3)  # cache is {3=3}
lRUCache.put(2, 2)  # cache is {3=3, 2=2}
lRUCache.reset()    # cache is {} (i.e. empty)
```

## Contact
If you want to contact me you can reach me at [kasra.azizbaigi@gmail.com](mailto:kasra.azizbaigi@gmail.com)

## License
This project uses the following license: [GNU General Public License v3.0](https://github.com/KasraAz75/LRUCache/blob/main/LICENSE).
