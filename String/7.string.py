
def sorted(lst):
    list1 = lst.split(',')
    result = []
    for i in list1:
        if i not in result:
            result.append(i)
    result.sort()
    return result
    

if __name__ =='__main__':
    my_string = 'amit,mahesh,rajat,amit,anil'
    print(sorted(my_string))
