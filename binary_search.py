lis = [1,2,3,4,5,6,7,8,9,10,11]

def binary_search(lis, key):
    start = 0
    end = len(lis)-1
    while start < end and (start < len(lis) and end > 0):
        middle = (start+end)//2
        if lis[middle]==key:
            return middle
        elif key>lis[middle]:
            start = middle + 1
        else :
            end = middle - 1
    return "Element Not found."

def recursive_binary_search(lis,key,start,end):
    if start <= end:
        middle = (start + end )//2 
        if lis[middle] ==  key:
            return middle 
        elif key>middle:
            start = middle + 1
            return recursive_binary_search(lis,key,start,end)
        else :
            end = middle - 1
            return recursive_binary_search(lis,key,start,end)

def find_all_occurances(numbers, number_to_find):
    index = binary_search(numbers, number_to_find)
    indices = [index]
    # find indices on left hand side
    i = index-1
    while i >=0:
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i - 1

    # find indices on right hand side
    i = index + 1
    while i<len(numbers):
        if numbers[i] == number_to_find:
            indices.append(i)
        else:
            break
        i = i + 1

    return sorted(indices)

    
#print(binary_search(lis,3))
#lis1 = [i for i in range(100)]
#print(recursive_binary_search(lis,11,0,len(lis)-1))
numbers = [1,4,6,9,11,15,15,15,17,21,34,34,56]
find_all_occurances(numbers,15)