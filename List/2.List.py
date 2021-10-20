
def mul(lst):
    mul = 1
    for i in lst:
        mul = mul * i
    return mul

if __name__ == '__main__':
    my_list = [1,2,3,4,5,6,1,2,3]
    print(mul(my_list))
