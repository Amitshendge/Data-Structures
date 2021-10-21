'''
@Author: Amit Shendge
@Date: 20-10-2021 8:40PM
@Last Modified by: Amit Shendge
@Last Modified time: 20-10-2021 8:40PM
@Title : Tuples in Python
'''

def creat_tuple(list):
    return tuple(list)


if __name__ == '__main__':
    list = [1,2,3,'abc']
    print(creat_tuple(list))
