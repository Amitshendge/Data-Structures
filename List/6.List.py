def rem_duplicates(lst):
    return list(set(lst))


if __name__ == '__main__':
    my_list = [1,2,3,4,2,3,5]
    print(rem_duplicates(my_list))
