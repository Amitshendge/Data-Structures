'''
@Author: Amit Shendge
@Date: 20-10-2021 12:32PM
@Last Modified by: Amit Shendge
@Last Modified time: 20-10-2021 12:32PM
@Title : Dictionary in Python
'''
#3.Concatenate Dictionary
def concat(dict1, dict2, dict3=None):
    try:
        dict1.update(dict2)
        dict1.update(dict3)
    except TypeError:
        return dict1
    else:
        return dict1


if __name__ == '__main__':
    dic1={1:10, 2:20}
    dic2={3:30, 4:40}
    dic3={5:50, 6:60}

    print(concat(dic1,dic2,dic3))