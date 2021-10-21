'''
@Author: Amit Shendge
@Date: 20-10-2021 11:30PM
@Last Modified by: Amit Shendge
@Last Modified time: 20-10-2021 11:30PM
@Title : Strings in Python
'''

def countFreq(substring, string):
    len_substring = len(substring)
    len_string = len(string)
    res = 0

    for i in range(len_string - len_substring + 1):
        j = 0
        while j < len_substring:
            if (string[i + j] != substring[j]):
                break
            j += 1
        if (j == len_substring):
            res += 1
            j = 0
    return res
     

if __name__ == '__main__':
    string = "cricket is too good sport "
    substring = "oo"
    print(countFreq(substring, string))