
def min(lst):
    temp = lst[0]
    for i in range(1,lst.__len__()):
        if temp > lst[i]:
            temp = lst[i]
    return temp

if __name__ == '__main__':
    my_list = [34,56,78,12,64]
    print(min(my_list))
