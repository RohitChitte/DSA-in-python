l = [4,38,17,21,25,11,32,9]

def selection_sort(l):
    for i in range(len(l)-1):
        for j in range(i+1,len(l)):
            if l[i]>l[j]:
                temp = l[i]
                l[i] = l[j]
                l[j] = temp
    return l

"""
print(selection_sort(l))
tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1,5,8,9],
        [234,3,1,56,34,12,9,12,1300],
        [78, 12, 15, 8, 61, 53, 23, 27],
        [5]
    ]
print("Sorted Lists")
for l in tests:
    print(selection_sort(l))
"""
# Exercise . 
lis = [
    {'First Name': 'Raj', 'Last Name': 'Nayyar'},
    {'First Name': 'Suraj', 'Last Name': 'Sharma'},
    {'First Name': 'Karan', 'Last Name': 'Kumar'},
    {'First Name': 'Jade', 'Last Name': 'Canary'},
    {'First Name': 'Raj', 'Last Name': 'Thakur'},
    {'First Name': 'Raj', 'Last Name': 'Sharma'},
    {'First Name': 'Kiran', 'Last Name': 'Kamla'},
    {'First Name': 'Armaan', 'Last Name': 'Kumar'},
    {'First Name': 'Jaya', 'Last Name': 'Sharma'},
    {'First Name': 'Ingrid', 'Last Name': 'Galore'},
    {'First Name': 'Jaya', 'Last Name': 'Seth'},
    {'First Name': 'Armaan', 'Last Name': 'Dadra'},
    {'First Name': 'Ingrid', 'Last Name': 'Maverick'},
    {'First Name': 'Aahana', 'Last Name': 'Arora'}
]

ord = ['First Name','Last Name']
def multilevel_selection_sort(lis,ord):
    #pref = ord[0]
    print(f"sorting with prefference of : {ord[0]}")
    for pref in ord[-1::-1]:    # this loop is used to sort elements on last prefference first to settle duplicate key in 1st prefference. 
        for i in range(len(lis)-1):
            for j in range(i+1,len(lis)):
                if lis[i][pref]>lis[j][pref]:
                    temp = lis[i]
                    lis[i] = lis[j]
                    lis[j] = temp
                    """
                elif lis[i][pref]==lis[j][pref]:
                    if lis[i][ord[1]]>lis[j][ord[1]]:
                        temp = lis[i]
                        lis[i] = lis[j]
                        lis[j] = temp
                    """
    return lis

result = multilevel_selection_sort(lis,ord)
for i in result:
    print(i)        
