class HashTable:
    def __init__(self,size=100):
        '''
        Coalesced chaining
        '''
        self.__size = size
        self.__length = 0
        self.__table = [[] for i in range(size)]

    def __hash(self,key):
        return hash(key)%self.__size #we get a nr in [0,size)

    def get(self, key):
        hashKey = self.__hash(key)
        for pair in self.__table[hashKey]:
            if pair == key:
                return pair
        return None

    def add(self, key):
        hashKey = self.__hash(key)
        for pair in self.__table[hashKey]:
            if pair == key:
                return hashKey
        self.__table[hashKey].append(key) #adds the element to the last position of the list
        self.__length += 1
        return hashKey

    def __str__(self):
        s = ''
        for index in range(len(self.__table)):
            if len(self.__table[index]) != 0:
                s += str(index) + " -> " + str(self.__table[index]) + "\n"
        return s

