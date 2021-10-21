
def count_char(string):
    string1 = list(string)
    temp = set(string1)
    temp = list(temp)
    result = {}
    for i in temp:
        result[i] = string1.count(i)
    return result

if __name__ =='__main__':
    print(count_char('google.com'))
