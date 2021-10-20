from itertools import permutations

def permutation(lst):
    permuted = list(permutations(lst))
    return permuted


if __name__ == '__main__':
    my_list = [1,2,3]
    print(permutation(my_list))
