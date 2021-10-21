'''
@Author: Amit Shendge
@Date: 20-10-2021 11:30PM
@Last Modified by: Amit Shendge
@Last Modified time: 20-10-2021 11:30PM
@Title : Strings in Python
'''

def lower_firstn(string,n):
    temp = string[:n]
    
    return temp.lower() + string[n:]


if __name__ =='__main__':
    my_string = 'Note: This is a System-Generated e-mail'
    print(lower_firstn(my_string,9))