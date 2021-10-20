
def sum(lst):
    sum = 0
    for i in lst:
        sum = sum + i
    return sum

if __name__ == '__main__':
    my_list = [1,2,3,4,5,6,1,2,3]
    print(sum(my_list))
