
def len_limit(lst,length):
    result = []
    for i in lst:
        if i.__len__() > length:
            result.append(i)
    return result


if __name__ == '__main__':
    my_list = ['Amit','Mahesh','Rajat','abc','ad']
    print(len_limit(my_list,3))