'''
@Author: Amit Shendge
@Date: 20-10-2021 2:12PM
@Last Modified by: Amit Shendge
@Last Modified time: 20-10-2021 2:12PM
@Title : List in Python
'''
def check_common(lst1,lst2):
    for i in lst1:
        if i in lst2:
            return True
    return False


if __name__ == '__main__':
    my_list1 = [1,2,3,4,5,6]
    my_list2 = [7,8,9,4,0]
    print(check_common(my_list1,my_list2))