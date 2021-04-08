def binarySearch(dataList,searchData,objKey):
    try:
       lowerBound = 0
       upperBound = len(dataList) - 1
       while lowerBound <= upperBound:
           mid = (lowerBound + upperBound) // 2
           if(dataList[mid][objKey] == searchData):
              return dataList[mid]
           else:
              if dataList[mid][objKey] < searchData:
                 lowerBound = mid + 1
              if dataList[mid][objKey] > searchData:
                 upperBound = mid - 1
       return {}
    except Exception as e:
       return e

#the list must be sorted
listData = [{"name":"aa"},{"name":"bb"},{"name":"ca"},{"name":"d"}]

#provide the key and value to search
print(binarySearch(listData,"aa","name"))
print(binarySearch(listData,"bb","name"))
print(binarySearch(listData,"xyz","name"))
print(binarySearch(listData,"ca","name"))
