def bubble_sort(numbers):
    for i in  range(len(numbers)-1):
        for j in range(len(numbers)-1-i):
            if numbers[j]>numbers[j+1]:
                numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
    return numbers


def bubble_sort_on_dictionary(numbers,key):
    for i in  range(len(numbers)-1):
        for j in range(len(numbers)-1-i):
            if numbers[j][key]>numbers[j+1][key]:
                numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
    return numbers


lis = [5,4,3,2,1]
print(bubble_sort(lis))
elements = [
        { 'name': 'mona',   'transaction_amount': 1000, 'device': 'iphone-10'},
        { 'name': 'dhaval', 'transaction_amount': 400,  'device': 'google pixel'},
        { 'name': 'kathy',  'transaction_amount': 200,  'device': 'vivo'},
        { 'name': 'aamir',  'transaction_amount': 800,  'device': 'iphone-8'},
    ]
for i in bubble_sort_on_dictionary(elements,'transaction_amount'):
    print(i)

for i in bubble_sort_on_dictionary(elements,'name'):
    print(i)

for i in bubble_sort_on_dictionary(elements,'device'):
    print(i)