# Project: 0x01. Caching

## Resources

### Read or watch:-

- [Cache replacement policies - FIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#Overview)
- [Cache replacement policies - LIFO](https://en.wikipedia.org/wiki/Cache_replacement_policies#Last_In_First_Out_%28LIFO%29)
- [Cache replacement policies - LRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_Recently_Used_%28LRU%29)
- [Cache replacement policies - MRU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Most_Recently_Used_%28MRU%29)
- [Cache replacement policies - LFU](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least-Frequently_Used_%28LFU%29)

## Learning Objectives

### General

- What a caching system is
- What FIFO means
- What LIFO means
- What LRU means
- What MRU means
- What LFU means
- What the purpose of a caching system
- What limits a caching system have

## More Info

### Parent class `BaseCaching`

All your classes must inherit from `BaseCaching` defined below:

```bash
$ cat base_caching.py
#!/usr/bin/python3
""" BaseCaching module
"""

class BaseCaching():
    """ BaseCaching defines:
      - constants of your caching system
      - where your data are stored (in a dictionary)
    """
    MAX_ITEMS = 4

    def __init__(self):
        """ Initiliaze
        """
        self.cache_data = {}

    def print_cache(self):
        """ Print the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print("{}: {}".format(key, self.cache_data.get(key)))

    def put(self, key, item):
        """ Add an item in the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """ Get an item by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
```

## Tasks

### 0. [Basic dictionary](./0-basic_cache.py) :-

Create a class `BasicCache` that inherits from `BaseCaching` and is a caching system:

- You must use `self.cache_data` - dictionary from the parent class `BaseCaching`
- This caching system doesn’t have limit
- `def put(self, key, item):`
  - Must assign to the dictionary `self.cache_data` the `item` value for the key `key`.
  - If `key` or `item` is `None`, this method should not do anything.
- `def get(self, key):`
  - Must return the value in `self.cache_data` linked to `key`.
  - If `key` is `None` or if the `key` doesn’t exist in `self.cache_data`, return `None`.

```bash
guillaume@ubuntu:~/0x01$ cat 0-main.py
#!/usr/bin/python3
""" 0-main """
BasicCache = __import__('0-basic_cache').BasicCache

my_cache = BasicCache()
my_cache.print_cache()
my_cache.put("A", "Hello")
my_cache.put("B", "World")
my_cache.put("C", "Holberton")
my_cache.print_cache()
print(my_cache.get("A"))
print(my_cache.get("B"))
print(my_cache.get("C"))
print(my_cache.get("D"))
my_cache.print_cache()
my_cache.put("D", "School")
my_cache.put("E", "Battery")
my_cache.put("A", "Street")
my_cache.print_cache()
print(my_cache.get("A"))

guillaume@ubuntu:~/0x01$ ./0-main.py
Current cache:
Current cache:
A: Hello
B: World
C: Holberton
Hello
World
Holberton
None
Current cache:
A: Hello
B: World
C: Holberton
Current cache:
A: Street
B: World
C: Holberton
D: School
E: Battery
Street
guillaume@ubuntu:~/0x01$ 
```

| Task | File |
| ---- | ---- |
| 1. FIFO caching | [1-fifo_cache.py](./1-fifo_cache.py) |
| 2. LIFO Caching | [2-lifo_cache.py](./2-lifo_cache.py) |
| 3. LRU Caching | [3-lru_cache.py](./3-lru_cache.py) |
| 4. MRU Caching | [4-mru_cache.py](./4-mru_cache.py) |
