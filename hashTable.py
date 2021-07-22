class hashTable:

    def __init__(self, length):
        self.len = length *2
        self.buckets = [None] * self.len

    def getIndex(self, key):
        index = hash(key) % self.len
        return index

    def set(self, key, value):
        index = self.getIndex(key)
        if self.buckets[index] is None:
            self.buckets[index] = []
            self.buckets[index].append([key, value])
        else:
            for kvp in self.buckets[index]:
                if kvp == key:
                    kvp[1] = value
            else:
                self.buckets[index].append([key, value])

    def get(self, key):
        index = self.getIndex(key)
        if self.buckets[index] is None:
            print('key', key, 'not found')
            raise KeyError
        if self.buckets[index][0][0] == key:
            return self.buckets[index][0][1]
        else:
            for kvp in self.buckets[index]:
                if kvp[0] == key:
                    return kvp[1]
            else:
                print('key', key, 'not found')
                raise KeyError
            print('key', key, 'not found')
            raise KeyError

    def remove(self, key):
        index = self.getIndex(key)
        if self.buckets[index] is None:
            print('key', key, 'not found')
            raise KeyError
        for kvp in self.buckets[index]:
            if kvp[0] == key:
                del kvp[0]
                return
        else:
            print('key', key, 'not found')
            raise KeyError


# jake = hashTable(25)
#
# jake.set(33, 'wingus')
# jake.set(133, 'bringus')
# print(jake.get(33))
# print(jake.get(133))
# jake.set(55, 'amongus')
# print(jake.get(55))
# jake.remove(55)
