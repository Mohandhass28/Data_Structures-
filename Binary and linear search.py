class Search:
    def __init__(self,arr):
        self.list1 = arr
        self.first = 0
        self.laste = len(arr)-1
        self.found = False

    def linear(self,data):
        lest = len(self.list1)
        for i in range(lest):
            if self.list1[i] == data:
                self.found = True
        if self.found == True:
            print('Data is found')
        else:
            print('Data is not found')

    def Binary_search(self,key):
        while self.first <= self.laste and not self.found:
            midpoint = (self.first + self.laste) // 2
            if key == self.list1[midpoint]:
                self.found = True
                print('Index of a key {}'.format(midpoint))
            elif key < self.list1[midpoint]:
                self.laste = midpoint - 1
            else:
                self.first = midpoint + 1
        if self.found == True:
            print('KEY is found')
        else:
            print('key not found')


list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
sea = Search(list2)
sea.Binary_search(7)


