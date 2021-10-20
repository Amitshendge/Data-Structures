def print_table(dict):
    for item in dict:
        print(item,'\t',dict[item])


if __name__ == '__main__':
    my_dict = {'Amit':55,'Mahesh':43,'Rajat':87}
    print_table(my_dict)
