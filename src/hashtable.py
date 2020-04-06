# '''
# Linked List hash table key/value pair
# '''
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity
        self.count = 0

    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.
        '''        
        if self.count >= self.capacity:
            self.resize()

        # Shift everything at index to the right
        if key > self.count:
            print("ERROR: Out of range")
            return

        for i in range(self.count, key, -1):
            self.storage[i] = self.storage[i - 1]
        self.storage[key] = value
        self.count += 1



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.
        '''
        if key >= self.count:
            print("ERROR: Out of range")
            return

        # Shift everything to the left
        for i in range(key, self.count - 1, 1):
            self.storage[i] = self.storage[i+1]
        self.count -= 1



    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        pass


    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.
        '''

        self.capacity *= 2
        new_storage = [None] * self.capacity

        for i in range(self.count):
            new_storage[i] = self.storage[i]

        self.storage = new_storage



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert(1, "Tiny hash table")
    ht.insert(2, "Filled beyond capacity")
    ht.insert(3, "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve(1))
    print(ht.retrieve(2))
    print(ht.retrieve(3))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve(1))
    print(ht.retrieve(2))
    print(ht.retrieve(3))

    print("")
