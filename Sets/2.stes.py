'''
@Author: Amit Shendge
@Date: 20-10-2021 4:30PM
@Last Modified by: Amit Shendge
@Last Modified time: 20-10-2021 4:30PM
@Title : Sets in Python
'''
def print_set(set):
    for i in set:
        print(i, end=' ')


if __name__ == '__main__':
    my_set = set([1,2,3,4,5,6])
    print_set(my_set)