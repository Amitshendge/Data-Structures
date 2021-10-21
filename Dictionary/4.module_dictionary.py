'''
@Author: Amit Shendge
@Date: 20-10-2021 12:32PM
@Last Modified by: Amit Shendge
@Last Modified time: 20-10-2021 12:32PM
@Title : Dictionary in Python
'''
def find_key(dict,element):
    for item in dict:
        if element == dict[item]:
            return item

def find_value(dict,element):
    for item in dict:
        if element == item:
            return dict[item]



if __name__ == '__main__':
    my_dict = {'Amit':55,'Mahesh':43,'Rajat':87}
    print(find_value(my_dict,'Amit'))
    print(find_key(my_dict,55))