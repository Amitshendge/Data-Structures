'''
@Author: Amit Shendge
@Date: 20-10-2021 2:12PM
@Last Modified by: Amit Shendge
@Last Modified time: 20-10-2021 2:12PM
@Title : List in Python
'''
def mul(lst):
    mul = 1
    for i in lst:
        mul = mul * i
    return mul

if __name__ == '__main__':
    my_list = [1,2,3,4,5,6,1,2,3]
    print(mul(my_list))
