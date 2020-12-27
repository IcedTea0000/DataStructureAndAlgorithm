class MyHashTable():
    def __init__(self, size):
        self.data = list()
        for counter in range(size):
            self.data.append(None)

    def __hash__(self, key):
        # O(1) or O(c)
        my_hash = 0
        for counter in range(0, len(key)):
            my_hash = (my_hash + ord(key[counter]) * counter) % len(key)
        return my_hash

    def __str__(self):
        return ('Data: {}'.format(self.data))
        pass

    def set(self, key, value):
        # O(1)
        address_to_store = self.__hash__(key)
        if self.data[address_to_store] is None:
            self.data[address_to_store] = []
        self.data[address_to_store].append([key, value])

    def get(self, key):
        # O(1)
        address_to_store = self.__hash__(key)
        current_bucket = self.data[address_to_store]
        if current_bucket is None:
            return None
        else:
            for element in current_bucket:
                if element[0] == key:
                    return element[1]

    def keys(self):
        # O(n)
        keys_list = []
        for bucket in self.data:
            if bucket is not None:
                for element in bucket:
                    keys_list.append(element[0])
        return keys_list

if __name__ == '__main__':
    myHashTable = MyHashTable(50)
    myHashTable.set('grapes', 'value1')
    myHashTable.set('grapess', 'value2')
    print(myHashTable)
    print(myHashTable.get('grapes'))
    print(myHashTable.keys())