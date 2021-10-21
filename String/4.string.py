
def ing_str(string):
    if string.__len__() >= 3:
        if string[-3:] == 'ing':
            return string + 'ly'
        else:
            return string + 'ing'

if __name__ =='__main__':
    print(ing_str('restarting'))
