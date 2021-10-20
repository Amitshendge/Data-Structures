def nested_dict(list):
    new_dict = current = {}
    for name in list:
        current[name] = {}
        current = current[name]
    print(new_dict)


if __name__ == '__main__':
    num_list = [1, 2, 3, 4]
    nested_dict(num_list)
