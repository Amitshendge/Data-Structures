
def count_success(dict):
    count = 0
    for i in dict:
        if i['success'] == True:
            count = count + 1
    return count


if __name__ == '__main__':
    Sample_data = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]

    print(count_success(Sample_data))