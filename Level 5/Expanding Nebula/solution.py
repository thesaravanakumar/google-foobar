import itertools


def solution(g):
    g = tuple(zip(*g))

    previous_row = {}
    for row in row_generator(len(g[0])):
        previous_row[row] = 1

    for i in range(len(g)):
        current_row = {}
        for row in row_generator(len(g[0])):
            for combination, count in previous_row.iteritems():
                if is_valid(row, combination, g[i]):
                    if row in current_row:
                        current_row[row] += count
                    else:
                        current_row[row] = count
        previous_row = current_row

    return sum(previous_row.values())


STATES = (0, 1)


def row_generator(row_len):
    return itertools.product(STATES, repeat=row_len+1)


def is_valid(r1, r2, row_check):
    for i in range(len(row_check)):
        sum_cells = r1[i] + r1[i+1] + r2[i] + r2[i+1]
        if (sum_cells == 1) != row_check[i]:
            return False
    return True