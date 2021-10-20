
def difference(lst1,lst2):
    result = []
    for i in lst1:
        if i not in lst2:
            result.append(i)
    for j in lst2:
        if j not in lst1:
            result.append(i)
    return result

if __name__ == '__main__':
    my_list1 = [1,2,3]
    my_list2 = [3,4,5]

    print(difference(my_list1,my_list2))
