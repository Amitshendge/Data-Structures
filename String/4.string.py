'''
@Author: Amit Shendge
@Date: 20-10-2021 11:30PM
@Last Modified by: Amit Shendge
@Last Modified time: 20-10-2021 11:30PM
@Title : Strings in Python
'''

def ing_str(string):
    if string.__len__() >= 3:
        if string[-3:] == 'ing':
            return string + 'ly'
        else:
            return string + 'ing'

if __name__ =='__main__':
    print(ing_str('restarting'))
