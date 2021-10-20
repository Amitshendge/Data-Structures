
def count_with_sameEnding(lst):
    temp = []
    for i in lst:
        if i.__len__() >+ 2:
            temp.append(i[0] + i[-1])
    for item in temp:
        if temp.count(item) != 1:
            return temp.count(item)
        else:
            return 'Nothing found as conditioned'


if __name__ == '__main__':
    my_list = ['abc', 'xyz', 'azc', '1221']
    print(count_with_sameEnding(my_list))
