'''
@Author: Amit Shendge
@Date: 20-10-2021 2:12PM
@Last Modified by: Amit Shendge
@Last Modified time: 20-10-2021 2:12PM
@Title : List in Python
'''
def specified_list(lst):
    result = []
    specified = [0,4,5]
    for i in lst:
        if lst.index(i) not in specified:
            result.append(i)
    return result


if __name__ == '__main__':
    my_list1 = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
    print(specified_list(my_list1))