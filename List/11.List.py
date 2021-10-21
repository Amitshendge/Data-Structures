'''
@Author: Amit Shendge
@Date: 20-10-2021 2:12PM
@Last Modified by: Amit Shendge
@Last Modified time: 20-10-2021 2:12PM
@Title : List in Python
'''
from itertools import permutations

def permutation(lst):
    permuted = list(permutations(lst))
    return permuted


if __name__ == '__main__':
    my_list = [1,2,3]
    print(permutation(my_list))
