'''
@Author: Amit Shendge
@Date: 20-10-2021 2:12PM
@Last Modified by: Amit Shendge
@Last Modified time: 20-10-2021 2:12PM
@Title : List in Python
'''
def remove_repeat(lst):
    result = []
    for i in lst:
        if result.count(i) == 0:
            result.append(i)
    return list(result)

if __name__ == '__main__':
    my_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
    print(remove_repeat(my_list))
