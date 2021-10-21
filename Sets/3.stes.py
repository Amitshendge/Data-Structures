'''
@Author: Amit Shendge
@Date: 20-10-2021 4:30PM
@Last Modified by: Amit Shendge
@Last Modified time: 20-10-2021 4:30PM
@Title : Sets in Python
'''
def add_in_set(set,string):
    list = string.split()
    for i in list:
        set.add(i)
    return set


if __name__ == '__main__':
    my_set = {'Amit','Mahesh','Rajat','Ganesh'}
    print(add_in_set(my_set,'Akhilesh'))