
def list_as_value(dict):
    count=0
    list=[]
    for i in dict:
        if type(dict[i]) == type(list):
            count = count + 1
    return count
        

if __name__ == '__main__':
    my_dict = {'Amit':[55,23],'Mahesh':[43,67],'Rajat':87}
    print(list_as_value(my_dict))
