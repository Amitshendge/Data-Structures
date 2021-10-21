'''
@Author: Amit Shendge
@Date: 20-10-2021 2:12PM
@Last Modified by: Amit Shendge
@Last Modified time: 20-10-2021 2:12PM
@Title : List in Python
'''
def split_list(lst):
    dict = {}
    for i in lst:
        if i[0] not in dict.keys():
            dict[i[0]] = [i]
        else:
            dict[i[0]].append(i)
    return dict

if __name__ == '__main__':
    my_list = ['Amit','Mahesh','Rajat','Ajit','Mass']
    print(split_list(my_list))
