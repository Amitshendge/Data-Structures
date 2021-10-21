'''
@Author: Amit Shendge
@Date: 20-10-2021 2:12PM
@Last Modified by: Amit Shendge
@Last Modified time: 20-10-2021 2:12PM
@Title : List in Python
'''
def sort_with(lst):
    temp = []
    temp.append(lst[0])
    for i in range(1,5):
        for item in range(temp.__len__()):
            if temp[item][1] > lst[i][1]:
                temp.insert(item, lst[i])
                break
    return temp
        


if __name__ == '__main__':
    my_list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
    print(sort_with(my_list))
