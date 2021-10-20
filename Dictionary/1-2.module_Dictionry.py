#1.Sort Dictionary by Values
def sort_by_Values(dict,reverse = False):
    if reversed == False:
        values = sorted(dict.values())
    else:
        values = sorted(dict.values(),reverse=True)
    sorted_dict = {}
    for i in values:
        for key, value in dict.items():
            if i == value:
                sorted_dict[key] = value
    return sorted_dict

#2.Add Key to Dictionary
def add_to_dict(dict):
    key = input('Enter Key : ')
    value = input('Enter Value : ')
    dict[key] = value
    return dict

if __name__ == '__main__':
    my_dict = {'Amit':55,'Mahesh':43,'Rajat':87}
    print('Original Dictionary : ', end="")
    print(my_dict)
    print('Sorted Dictionary : ', end="")
    print(sort_by_Values(my_dict))
    print('New Dictionary : ', end="")
    print(add_to_dict(my_dict))
