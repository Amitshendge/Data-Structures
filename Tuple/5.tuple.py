def repeat_tuple(tup):
    result = set()
    for i in tup:
        if  tup.count(i) != 1:
            result.add(i)
    return result
    

if __name__ == '__main__':
    tup = (1,2,3,6,5,2,3)
    print(repeat_tuple(tup))
