class SearchingAlgorithms ():

    def sequantialSearchUnordered(self, unorderList,number):
        index = 0
        found = False
        while index < len(unorderList) and not found:
            if unorderList[index] == number:
                found = True
            else:
                index += 1
        return found
sorting = SearchingAlgorithms()
list = [1,2,34,5,78,98,900,23,45,36,89]
print(sorting(list,89))
    #def sequantialSearchOrdered(self, orderedList,number):
      #  pass
    #def binarySearch(self,orderedList,number):
       # pass



