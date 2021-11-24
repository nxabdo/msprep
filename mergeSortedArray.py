class mergeSortedArray:
    def merge(self,array1, array2):
        if isinstance(array1,list) and isinstance(array2,list):
            mergedArray = array1 + array2
            print(mergedArray)
            length = len(mergedArray)-1
            tmp = mergedArray

            for i in range(0,length,1):
                    while mergedArray[i] > mergedArray[i+1]:
                        tmpVal = mergedArray[i+1]
                        mergedArray[i+1] = mergedArray[i]
                        mergedArray[i] = tmpVal
            print(mergedArray)

        else:
            print("Invalid input! Please try again.")

mergeObj = mergeSortedArray()
mergeObj.merge([0, 3, 4, 31], [4, 6, 30])
