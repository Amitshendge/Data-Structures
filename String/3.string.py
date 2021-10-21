'''
@Author: Amit Shendge
@Date: 20-10-2021 11:30PM
@Last Modified by: Amit Shendge
@Last Modified time: 20-10-2021 11:30PM
@Title : Strings in Python
'''

def replace_char(string):
    temp = list(string)
    for i in range(1,temp.__len__()):
        if temp[i] == temp[0]:
            temp[i] = '$'
    result = ''
    for i in temp:
        result = result + i
    return result

if __name__ =='__main__':
    print(replace_char('restart'))
