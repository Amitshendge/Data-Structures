
import copy


def appends(lst1,lst2):
    result = copy.copy(lst1)
    for i in lst2:
        result.append(i)
    return result

if __name__ == '__main__':
    my_list1 = [1,2,3]
    my_list2 = [3,4,5]

    print(appends(my_list1,my_list2))
