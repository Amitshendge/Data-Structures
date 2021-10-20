
def split_list(lst1,lst2):
    result=[]
    temp = lst1*2
    temp_index=0
    if lst1.__len__() != lst2.__len__():
        return False
    else:
        if result.__len__() != lst1.__len__():
            for i in lst2:
                for j in range(temp_index,temp.__len__()):
                    if i == temp[j]:
                        result.append(j)
                        temp_index=j
                        break
        new_result = set(result)
        new_result = list(new_result)
        for i in range(lst1.__len__()-1):
            if new_result[i+1]-new_result[i] == 1:
                pass
            else:
                return False

        return True
    

if __name__ == '__main__':
    list1 = [1,2,3]
    list2 = [2,3,1]
    print(split_list(list1,list2))
