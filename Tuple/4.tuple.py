'''
@Author: Amit Shendge
@Date: 20-10-2021 8:40PM
@Last Modified by: Amit Shendge
@Last Modified time: 20-10-2021 8:40PM
@Title : Tuples in Python
'''

import copy

if __name__ =='__main__':
    my_tuple = (1,2,[5],6)
    colon_tuple = copy.deepcopy(my_tuple)
    colon_tuple[2].append(7)
    print(my_tuple)
    print(colon_tuple)