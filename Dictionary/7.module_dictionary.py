'''
@Author: Amit Shendge
@Date: 20-10-2021 12:32PM
@Last Modified by: Amit Shendge
@Last Modified time: 20-10-2021 12:32PM
@Title : Dictionary in Python
'''
def unique_values(dict):
    uniqueValues = set(dict.values())
    return uniqueValues

if __name__ == '__main__':
    sample_data = {"VA":"S001", "VB":"S002", "VI":"S001", "VC":"S005", "VII":"S005", "V":"S009", "VIII":"S007"}
    print(unique_values(sample_data))