'''
@Author: Amit Shendge
@Date: 20-10-2021 12:32PM
@Last Modified by: Amit Shendge
@Last Modified time: 20-10-2021 12:32PM
@Title : Dictionary in Python
'''
def string_to_dict(string):
    lst = list(string)
    set_lst = set(lst)
    dict = {}
    for i in set_lst:
        dict[i] = lst.count(i)
    return dict


if __name__ == '__main__':
    sample_string =  'w3resource'
    print(string_to_dict(sample_string))