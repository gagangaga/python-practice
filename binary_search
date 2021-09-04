def binary_search(array,item):
    start = 0
    end = len(array)-1
    while start<=end:
        midpoint = start+(end-start)//2
        midvalue = array[midpoint]
        if midvalue==item:
            return midpoint
        elif midvalue<item:
            start = midpoint+1
        else:
            end = midpoint-1
    return None

array = [2,3,4,4,5,5,6,7,8,9]
item = 8
print(binary_search(array,item))
