def exist_in_tuple(tup,element):
    if element in tup:
        return str(element) + ' exists in given tuple'
    else:
        return str(element) + ' does no exist in given tuple'
    

if __name__ == '__main__':
    tup = (1,2,3,6,5,2,3)
    print(exist_in_tuple(tup,32))
