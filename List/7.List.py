import copy

def copy_list(lst):
    return copy.deepcopy(lst)


if __name__ == '__main__':
    my_list = [1,2,3,4,5]
    copied_list = copy_list(my_list)
    print(copied_list)