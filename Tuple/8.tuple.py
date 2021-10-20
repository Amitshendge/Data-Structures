def remove_tuple(tup,element):
    list_tup = list(tup)
    list_tup.remove(element)
    return tuple(list_tup)
    

if __name__ == '__main__':
    tup = (1,2,3,6,5,2,3)
    print(remove_tuple(tup,6))
