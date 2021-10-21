'''
@Author: Amit Shendge
@Date: 20-10-2021 2:12PM
@Last Modified by: Amit Shendge
@Last Modified time: 20-10-2021 2:12PM
@Title : List in Python
'''
def rem_duplicates(lst):
    return list(set(lst))


if __name__ == '__main__':
    my_list = [1,2,3,4,2,3,5]
    print(rem_duplicates(my_list))
