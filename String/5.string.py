
def len_word(lst):
    result = []
    for i in lst:
        result.append(i.__len__())
    result_index = result.index(max(result))
    return lst[result_index]

if __name__ =='__main__':
    my_list = ['amit','mahesh','rajat']
    print(len_word(my_list))
