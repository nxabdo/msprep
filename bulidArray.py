class buildArray:

    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item
        self.length += 1
        return self.length

    def pop(self):
        lastItem = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return lastItem

    def delete(self, index):
        item = self.data[index]
        self.shiftItems(index)

    def shiftItems(self, index):
        for i in range (0, index, 1):
            self.data[i] = self.data[i+1]
            self.length -=1




newArray = buildArray()
newArray.push('hi')
newArray.push('you')
print(newArray.get(0))
print(newArray.get(1))
newArray.pop()
print(newArray.get(0))





