
def check_key_multiple(dict,string):
    list = string.split()
    for i in list:
        if i in dict.keys():
            print(i,' exists in Dictionary as key')
        else:
            print(i,' doesn\'t exist in Dictionary as key')
    



if __name__ == '__main__':
    my_dict = {'Amit':55,'Mahesh':43,'Rajat':87}
    check_key_multiple(my_dict,'Amit Ganesh')


