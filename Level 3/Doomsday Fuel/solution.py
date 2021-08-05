import fractions
from fractions import Fraction, gcd


def solution(m):
    fr = calculate_fr(m)
    solution_frac = fr[0]

    lcm = 1  # least common multiple
    for num in solution_frac:
        lcm = abs(lcm * num.denominator) // gcd(lcm, num.denominator)
    solution_int = []
    for num in solution_frac:
        solution_int.append(int(num * lcm))
    solution_int.append(lcm)

    if sum(m[0]) == 0:
        terminal_solution = []
        for i in range(len(solution_int)):
            terminal_solution.append(0)
        terminal_solution[0] = 1
        terminal_solution[-1] = 1
        return terminal_solution
    return solution_int


def calculate_fr(m):
    non_absorbing_states = []
    absorbing_states = []
    fraction_matrix = []
    for i in range(len(m)):
        row = []
        sum = 0
        for num in m[i]:
            sum += num
        if sum == 0:
            absorbing_states.append(i)
            for num in m[i]:
                row.append(Fraction(0, 1))
        else:
            non_absorbing_states.append(i)
            for num in m[i]:
                row.append(Fraction(num, sum))
        fraction_matrix.append(row)

    q = []
    for i in non_absorbing_states:
        row = []
        for j in non_absorbing_states:
            row.append(fraction_matrix[i][j])
        q.append(row)

    r = []
    for i in non_absorbing_states:
        row = []
        for j in absorbing_states:
            row.append(fraction_matrix[i][j])
        r.append(row)

    f = []
    for i in range(len(q)):
        row = []
        for j in range(len(q)):
            if i != j:
                row.append(0 - q[i][j])
            else:
                row.append(1 - q[i][j])
        f.append(row)
    f = inverse_matrix(f)

    fr = []
    for i in range(len(f)):
        row = []
        for j in range(len(r[0])):
            sum = 0
            for k in range(len(r)):
                sum += f[i][k] * r[k][j]
            row.append(sum)
        fr.append(row)
    return fr


def inverse_matrix(m):
    d = determinant(m)
    if len(m) == 2:
        return [[m[1][1] / d, -1 * m[0][1] / d],
                [-1 * m[1][0] / d, m[0][0] / d]]
    adjoint = []
    for r in range(len(m)):
        row = []
        for c in range(len(m)):
            minor = get_minor_matrix(m, r, c)
            row.append(((-1) ** (r + c)) * determinant(minor) / d)
        adjoint.append(row)
    return map(list, zip(*adjoint))


def determinant(m):
    if len(m) == 2:
        return m[0][0] * m[1][1] - m[0][1] * m[1][0]
    determinant_ = 0
    for col in range(len(m)):
        determinant_ += ((-1) ** col) * m[0][col] * determinant(get_minor_matrix(m, 0, col))
    return determinant_


def get_minor_matrix(m, i, j):
    return [row[:j] + row[j + 1:] for row in (m[:i] + m[i + 1:])]
    