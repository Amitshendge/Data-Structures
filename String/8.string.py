
def split_specified(string,char):
    list1 = string.split(char)
    return list1[0]
    

if __name__ =='__main__':
    my_string = 'https://www.w3resource.com/python-exercises'
    print(split_specified(my_string,'-'))
