
def split_list(lst):
    dict = {}
    for i in lst:
        if i[0] not in dict.keys():
            dict[i[0]] = [i]
        else:
            dict[i[0]].append(i)
    return dict

if __name__ == '__main__':
    my_list = ['Amit','Mahesh','Rajat','Ajit','Mass']
    print(split_list(my_list))
