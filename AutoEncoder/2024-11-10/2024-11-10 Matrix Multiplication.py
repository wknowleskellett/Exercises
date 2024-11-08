import random as rd


EX_1A = \
[
    [ 1, 2, ],
    [ 3, 4, ],
]

EX_1B = \
[
    [ 2, 0, ],
    [ 1, 2, ],
]

EX_1C = \
[
    [  4, 4, ],
    [ 10, 8, ],
]

EX_2A = \
[
    [ 13, 27, 2, ],
    [  3,  4, 5, ],
]

EX_2B = \
[
    [ 9,  0, 8, ],
    [ 1,  2, 2, ],
    [ 5, -7, 1, ],
]

EX_2C = \
[
    [ 154,  40, 160, ],
    [  56, -27,  37, ],
]

EX_3A = \
[
    [ 13, 27, 2, ],
]

EX_3B = \
[
    [ 9, ],
    [ 1, ],
    [ 5, ],
]

EX_3C = \
[
    [ 154, ],
]


def matrix_multiply(mat_a, mat_b):
    # vvvv  Put your code here vvvv

    # I'll give you a hint: use the `transpose(matrix)` function I provided below.

    # ^^^^  Put your code here ^^^^

    return result


def transpose(mat):
    return list(list(column) for column in zip(*mat))


def matrix_to_strings(mat):
    if not(validate_matrix(mat)):
        return [repr(mat)+' (not a proper matrix- must be a 2D array with equal width rows)']
    
    mat_t = transpose(mat)
    width = len(mat_t)
    height = len(mat)

    # Turn the matrix into a table before adding brackets
    row_strings = list('' for _ in mat)

    # Find the width of the cells for all but the leftmost column
    # Since the columns are right-aligned, this assures equal spacing
    column_widths = [max(max(len(str(val)) for val in column) for column in mat_t)+1]*width

    # Find the width of the leftmost column
    column_widths[0] = max(len(str(val)) for val in mat_t[0])
    
    for column, column_width in zip(mat_t, column_widths):
        for row_num, val in enumerate(column):
            row_strings[row_num] += str(val).rjust(column_width)

    box_width = len(row_strings[0])+2
    box_strings = ['┌' + ' '*box_width+'┐']
    for row_string in row_strings:
        box_strings.append('│ '+row_string+' │')
    box_strings.append('└' + ' '*box_width+'┘')
    
    return box_strings


def validate_matrix(mat):
    if not(hasattr(mat, '__iter__') and hasattr(mat[0], '__iter__')):
        return False
    width = len(mat[0])
    for row in mat[1:]:
        if len(row) != width:
            return False
    return True


def print_matrix(mat):
    print('\n'.join(matrix_to_strings(mat)))


def print_matrix_multiplication(mat_a, mat_b):
    mat_c = matrix_multiply(mat_a, mat_b)


    strs_a = matrix_to_strings(mat_a)
    strs_b = matrix_to_strings(mat_b)
    strs_eq = [' = ']
    strs_c = matrix_to_strings(mat_c)
    
    total_height = max(len(strs) for strs in (strs_a, strs_b, strs_eq, strs_c))

    for strs in (strs_a, strs_b, strs_eq, strs_c):
        pad = total_height - len(strs)
        pad_above = pad // 2
        pad_below = pad - pad_above

        pad_string = ' '*len(strs[0])
        for _ in range(pad_above):
            strs.insert(0, pad_string)
        for _ in range(pad_below):
            strs.append(pad_string)

    for str_a, str_b, str_eq, str_c in zip(strs_a, strs_b, strs_eq, strs_c):
        print(str_a, str_b, str_eq, str_c, sep='')


if __name__ == '__main__':
    height_c = rd.randint(1, 4)
    width_c = rd.randint(1, 4)
    missing_dimension = rd.randint(1, 4)

    mat_a = list(list(rd.randint(-12, 12) for _ in range(missing_dimension)) for _ in range(height_c))
    mat_b = list(list(rd.randint(-12, 12) for _ in range(width_c)) for _ in range(missing_dimension))
    mat_b_t = transpose(mat_b)
    mat_c = list(list(sum(val_a*val_b for val_a, val_b in zip(row_a, col_b)) for col_b in mat_b_t) for row_a in mat_a)
    
    problems = [
        (EX_1A, EX_1B, EX_1C),
        (EX_2A, EX_2B, EX_2C),
        (EX_3A, EX_3B, EX_3C),
        (mat_a, mat_b, mat_c),
    ]
    
    for i, (mat_a, mat_b, mat_c) in enumerate(problems):
        print(f'Problem {i}:')
        print_matrix_multiplication(mat_a, mat_b)
        print('\nCorrect answer:')
        print_matrix(mat_c)
        print()
