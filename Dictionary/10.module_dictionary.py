
'''
@Author: Amit Shendge
@Date: 20-10-2021 12:32PM
@Last Modified by: Amit Shendge
@Last Modified time: 20-10-2021 12:32PM
@Title : Dictionary in Python
'''
def count_success(dict):
    count = 0
    for i in dict:
        if i['success'] == True:
            count = count + 1
    return count


if __name__ == '__main__':
    Sample_data = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]

    print(count_success(Sample_data))