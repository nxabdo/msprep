class ListNode():
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None

class hashtable():
    size = 10
    def __init__(self):
        #Define size
        #Define hashtable
        self.size = 10
        self.hashTable = [None] * self.size

    def put(self, key, value):
        #Hashing function: remainder
        hashIndex = key % self.size
        if self.hashTable[hashIndex] == None:
            self.hashTable[hashIndex] = ListNode(key, value)
        else:
            #Current index in the hashtable
            current = self.hashTable[hashIndex]

            #infinite loop
            while True:
                #if the current pair's key ==  key being inserted
                #Impossible to have duplicate values
                if current.pair[0] == key:
                    current.pair = (key, value)
                    return
                #Otherwise if the next psoition is empty
                #break
                if current.next == None:
                    break
                #set the current node to the next node in the linked list

                current = current.next
            current.next = ListNode(key,value)

    def get(self, key):
        #Retrieve value of the index
        index = key % self.size
        #set current to the position of index in the hash table
        current =  self.hashTable[index]

        #while current is not equal to None
        while current:
            #If the value of the current node's pair is equal to the key then return the current pair
            if current.pair[0] == key:
                return current.pair[1]
            #otherwise move to the next node
            else:
                current = current.next
        return -1

    def remove(self, key):
        index = key % int(self.size)
        current = prev = self.hashTable[index]

        if not current:
            return None
        if current.pair[0] == key:
            self.hashTable[index] = current.next
        else:
            current = current.next
            while current:
                #Check if keys match
                if current.pair[0] == key:
                    #if keys match set current to none
                    prev.next = current.next
                    break
                else:
                    #otherwise move current to next node in the hash table
                    current = current.next
                    prev = prev.next

obj = hashtable()
obj.put(10, 5)
obj.put(9, 8)
obj.put(88, 3)
obj.put(4, 1)
obj.put(8, 2)
obj.put(7, 22)
getObj = obj.get(10)
obj.remove(4, 11)
print(obj.hashTable)