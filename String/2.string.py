'''
@Author: Amit Shendge
@Date: 20-10-2021 11:30PM
@Last Modified by: Amit Shendge
@Last Modified time: 20-10-2021 11:30PM
@Title : Strings in Python
'''

def count_char(string):
    string1 = list(string)
    temp = set(string1)
    temp = list(temp)
    result = {}
    for i in temp:
        result[i] = string1.count(i)
    return result

if __name__ =='__main__':
    print(count_char('google.com'))
