def sparse_mult(A, B):
    o_rows = a_rows = len(A)
    a_cols = len(A[0])
    b_rows = len(B)
    o_cols = b_cols = len(B[0])
    res = [[0 for c in range(o_cols)] for r in range(o_rows)]

    A_set_bits = []
    B_set_bits = []

    for r in range(a_rows):
        set_bits = 0
        for c in range(a_cols):
            if A[r][c] != 0:
                set_bits += 1 << c
        A_set_bits.append(set_bits)

    for c in range(b_cols):
        set_bits = 0
        for r in range(b_rows):
            if B[r][c] != 0:
                set_bits += 1 << r
        B_set_bits.append(set_bits)

    for r in range(o_rows):
        a_set_bits = A_set_bits[r]
        if a_set_bits == 0:
            continue
        for c in range(o_cols):
            set_bits = a_set_bits & B_set_bits[c]
            if set_bits == 0:
                continue
            idx = 0
            dot = 0
            while set_bits:
                if set_bits & 1:
                    dot += A[r][idx] * B[idx][c]
                set_bits >>= 1
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
