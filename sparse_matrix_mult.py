def sparse_mult(A, B):
    o_rows = a_rows = len(A)
    a_cols = len(A[0])
    b_rows = len(B)
    o_cols = b_cols = len(B[0])
    res = [[0 for c in range(o_cols)] for r in range(o_rows)]

    A_non_zero = []
    B_non_zero = []

    for r in range(a_rows):
        non_zero = 0
        for c in range(a_cols):
            if A[r][c] != 0:
                non_zero += 1 << c
        A_non_zero.append(non_zero)

    for c in range(b_cols):
        non_zero = 0
        for r in range(b_rows):
            if B[r][c] != 0:
                non_zero += 1 << r
        B_non_zero.append(non_zero)

    for r in range(o_rows):
        row_non_zero = A_non_zero[r]
        if row_non_zero == 0:
            continue
        for c in range(o_cols):
            non_zero = row_non_zero & B_non_zero[c]
            if non_zero == 0:
                continue
            idx = 0
            dot = 0
            while non_zero:
                if non_zero & 1:
                    dot += A[r][idx] * B[idx][c]
                non_zero >>= 1
                idx += 1
            res[r][c] = dot
    return res


def show_m(l):
    for rows in zip(*l):
        for r in rows:
            for c in r:
                print(c, end=',\t')
            print(end='\t')
        print('')


A = [[1, 0, 0],
     [0, 2, 2],
     [6, 0, 0]]

B = [[0, 1, 0],
     [2, 1, 0],
     [0, 0, 0]]

show_m([A, B, sparse_mult(A, B)])
