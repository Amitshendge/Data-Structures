import copy

if __name__ =='__main__':
    my_tuple = (1,2,[5],6)
    colon_tuple = copy.deepcopy(my_tuple)
    colon_tuple[2].append(7)
    print(my_tuple)
    print(colon_tuple)