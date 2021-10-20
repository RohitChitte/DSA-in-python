# Memory Optimised i.e returns the original list in sorted manner . no creation of extra list to put  sorted elements. 

def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr)//2

    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)

def merge_two_sorted_lists(a,b,arr):
    len_a = len(a)
    len_b = len(b)

    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i+=1
        else:
            arr[k] = b[j]
            j+=1
        k+=1

    while i < len_a:
        arr[k] = a[i]
        i+=1
        k+=1

    while j < len_b:
        arr[k] = b[j]
        j+=1
        k+=1


test_cases = [
    [10, 3, 15, 7, 8, 23, 98, 29],
    [],
    [3],
    [9,8,7,2],
    [1,2,3,4,5]
]

for arr in test_cases:
    merge_sort(arr)
    print(arr)


"""
# no memory optimisation i.e this functions returns new sorted list. 
def merge_two_sorted_lists(a,b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = 0
    while i < len_a and j < len_b:  # if this loop is terminated it menas either of the condiotins is true
        if a[i] > b[j]:               # if lengthe of lists is different condition for smaller list will get false and loop will terminate
            sorted_list.append(b[j])  # at last itereate throw bigger list that is condtion which is yet to become false
            j += 1 
           
        else: 
            sorted_list.append(a[i])
            i += 1 
        
    while i<len_a:
        sorted_list.append(a[i])
        i += 1
    while j<len_b:
        sorted_list.append(b[j])
        j += 1

        
    return sorted_list

def merge_sort(arr):
    if len(arr) <= 1 :
        return arr
    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge_two_sorted_lists(left,right)

#a = [5,8,12,56]
#b = [7,9,45,51]
#print(merge_two_sorted_lists(a,b))

lis = [10, 3, 15, 7, 8, 23, 98, 29]
print(merge_sort(lis))

"""