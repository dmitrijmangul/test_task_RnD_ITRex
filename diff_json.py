import json
import sys


with open(sys.argv[1], 'r') as file_a, open(sys.argv[2], 'r') as file_b:
    data_a = json.load(file_a)
    data_b = json.load(file_b)


def diff_json(a, b):
    '''
    This function recursively (in case of nested dictionaries) compares
    each key of the first file with each key of the second file.
    '''
    global diff
    global output_list  # a variable outside the function so that recursion does not nullify it
    for key_a, value_a in a.items():
        if type(value_a) is dict:  # recursion
            diff_json(a=value_a, b=b)
        key_a_norm = ''.join(char for char in key_a if char.isalpha()).lower()  # one style to compare
        if key_a_norm not in set_keys_norm_b:  # checking for a mutual key
            output_list.append([f'file A: {key_a} - {value_a}', f'file B: not set'])
        for key_b, value_b in b.items():
            if type(value_b) is dict:  # recursion
                diff_json(a={key_a: value_a}, b=value_b)
            key_b_norm = ''.join(char for char in key_b if char.isalpha()).lower()  # one style to compare
            if key_a_norm == key_b_norm and value_a != value_b and type(value_b) is not dict:  # difference
                diff = True
                output_list.append([f'file A: {key_a} - {value_a}', f'file B: {key_b} - {value_b}'])
            if key_b_norm not in set_keys_norm_a:  # checking for a mutual key
                output_list.append([f'file A: not set', f'file B: {key_b} - {value_b}'])


def set_keys_norm(x):
    '''
    This function recursively (in the case of nested dictionaries) selects all keys converted to the same style.
    '''
    global helper_set  # a variable outside the function so that recursion does not nullify it
    for key_x, value_x in x.items():
        if type(value_x) is dict:
            set_keys_norm(x=value_x)
        key_x_norm = ''.join(char for char in key_x if char.isalpha()).lower()
        helper_set |= {key_x_norm}
    return helper_set


helper_set = set()
set_keys_norm_a = set_keys_norm(data_a)
helper_set = set()
set_keys_norm_b = set_keys_norm(data_b)

print('\nThe difference between two input JSON files:', end='\n\n')

diff = False  # a flag to check for a difference in files

output_list = list()
diff_json(data_a, data_b)

if not diff:
    print('both files are identical')

# to filter out repetitions.
helper_list = []
for i in output_list:
    if i not in helper_list:
        print(*i, sep='\n', end='\n\n')
    helper_list.append(i)

print('The comparison is complete.', end='\n\n')
