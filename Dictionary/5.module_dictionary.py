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