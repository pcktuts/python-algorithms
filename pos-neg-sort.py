# Sort positives, keep negatives
# Write a function that sorts the positive numbers
# in ascending order and keep the negative numbers untouched
# Notes: 
# 1. If given empty list, you should return an empty list
# 2. Integers will be always positive or negative 0 is not included
# in the tests.
#
def pos_neg_sort(mylist):    
    sorted_list = mylist.copy()
    sorted_list.sort()
    result = filter(lambda x: x > 0, sorted_list) 
    new_list = list(result).copy()


    output = []
    for idx, val in enumerate(mylist, start=0):
        if val > 0 and new_list:
            output.append(new_list.pop(0))
        else:
            output.append(val)
    print("original list ")
    print(mylist)
    print("positive num sorted list")
    print(output)

mylist = [8, 1, -4, -6, 9, 3, -9]
pos_neg_sort(mylist)


# Sample output as executed in Mac

'''
python3 pos-neg-sort.py
original list 
[8, 1, -4, -6, 9, 3, -9]
positive num sorted list
[1, 3, -4, -6, 8, 9, -9]
'''
