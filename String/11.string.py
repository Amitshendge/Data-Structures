'''
@Author: Amit Shendge
@Date: 20-10-2021 11:30PM
@Last Modified by: Amit Shendge
@Last Modified time: 20-10-2021 11:30PM
@Title : Strings in Python
'''

def reverse(string):
    len1 = len(string)
    result = ''
    for i in range(len1).__reversed__():
        result = result + string[i]
    return result

    

if __name__ =='__main__':
    my_string = 'https://www.w3resource.com/python-exercises'
    print(reverse(my_string))
