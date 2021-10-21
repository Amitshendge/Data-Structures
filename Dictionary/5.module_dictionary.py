'''
@Author: Amit Shendge
@Date: 20-10-2021 12:32PM
@Last Modified by: Amit Shendge
@Last Modified time: 20-10-2021 12:32PM
@Title : Dictionary in Python
'''
def square_dict(value):
    dict = {}
    for item in range(1,value+1):
        dict[item] = item*item
    return dict


if __name__ == '__main__':
    while True:
        try:
            user_input = int(input('Enter number : '))
        except ValueError:
            print('Enter number only !!!')
            continue
        else:
            break

    print(square_dict(user_input))