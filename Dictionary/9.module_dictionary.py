'''
@Author: Amit Shendge
@Date: 20-10-2021 12:32PM
@Last Modified by: Amit Shendge
@Last Modified time: 20-10-2021 12:32PM
@Title : Dictionary in Python
'''
def print_table(dict):
    for item in dict:
        print(item,'\t',dict[item])


if __name__ == '__main__':
    my_dict = {'Amit':55,'Mahesh':43,'Rajat':87}
    print_table(my_dict)
