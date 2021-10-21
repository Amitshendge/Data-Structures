'''
@Author: Amit Shendge
@Date: 20-10-2021 2:12PM
@Last Modified by: Amit Shendge
@Last Modified time: 20-10-2021 2:12PM
@Title : List in Python
'''
def common(lst1,lst2):
    result = []
    for i in lst1:
        if i in lst2:
            result.append(i)
    return result

if __name__ == '__main__':
    my_list1 = [1,2,3]
    my_list2 = [3,4,5]

    print(common(my_list1,my_list2))
