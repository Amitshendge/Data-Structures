def remove(dict):
    while True:
        try:
            while True:
                try:
                    user_input = str(input('Enter Key : '))
                except ValueError:
                    print('Enter number only !!!')
                    continue
                else:
                    break
            dict.pop(user_input)
        except KeyError:
            print('Key invalid Plz Enter valid Key')
            continue
        else:
            break

    return dict


if __name__ == '__main__':
    my_dict = {'Amit':55,'Mahesh':43,'Rajat':87}

    print(remove(my_dict))