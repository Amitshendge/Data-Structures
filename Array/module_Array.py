'''
@Author: Amit Shendge
@Date: 20-10-2021 11:32AM
@Last Modified by: Amit Shendge
@Last Modified time: 20-10-2021 11:32AM
@Title : Arrays in Python
'''

import array as arr

my_array = arr.array('i',[1,2,3,4,5])

#1.Print Array
def print_array(arr):
    for i in range(arr.__len__()):
        print(arr[i],end=" ")
    print()

#2.Reversed Array
def reverse_array(arr):
    for i in reversed(range(arr.__len__())):
        print(arr[i],end=" ")
    print()

#3.Count in Array
def count(arr,element):
    occurance = 0
    for i in arr:
        if i == element:
            occurance =+1
    return occurance

#4.Remove first occurance
def remove_first_occurance(arr,element):
    for i in arr:
        if i == element:
            arr.remove(element)
            return arr


if __name__ == '__main__':
    my_array.extend((2,34,55))
    print('Our Array is : ', end="")
    print_array(my_array)
    print('Our Reversed Array is : ', end="")
    reverse_array(my_array)
    print('Count in Array is : ',count(my_array,2))
    print('Our modified Array is : ', end="")
    print_array(remove_first_occurance(my_array,2))
    

