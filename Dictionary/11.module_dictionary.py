'''
@Author: Amit Shendge
@Date: 20-10-2021 12:32PM
@Last Modified by: Amit Shendge
@Last Modified time: 20-10-2021 12:32PM
@Title : Dictionary in Python
'''
def nested_dict(list):
    new_dict = current = {}
    for name in list:
        current[name] = {}
        current = current[name]
    print(new_dict)


if __name__ == '__main__':
    num_list = [1, 2, 3, 4]
    nested_dict(num_list)
