
def reverse(string):
    len1 = len(string)
    result = ''
    for i in range(len1).__reversed__():
        result = result + string[i]
    return result

    

if __name__ =='__main__':
    my_string = 'https://www.w3resource.com/python-exercises'
    print(reverse(my_string))
