
'''
@Author: Amit Shendge
@Date: 20-10-2021 12:32PM
@Last Modified by: Amit Shendge
@Last Modified time: 20-10-2021 12:32PM
@Title : Dictionary in Python
'''
def list_as_value(dict):
    count=0
    list=[]
    for i in dict:
        if type(dict[i]) == type(list):
            count = count + 1
    return count
        

if __name__ == '__main__':
    my_dict = {'Amit':[55,23],'Mahesh':[43,67],'Rajat':87}
    print(list_as_value(my_dict))
