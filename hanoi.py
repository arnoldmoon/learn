"""
hanio tower
"""


# hanoi tower solution from internet search
def hanoi_tower(n):

    def move_tower(height, from_pole, to_pole, with_pole):
        if height >= 1:
            move_tower(height-1, from_pole, with_pole, to_pole)
            move_disc(from_pole, to_pole, height)
            move_tower(height-1, with_pole, to_pole, from_pole)

    def move_disc(fp, tp, height):
        tp.append(fp.pop())
        show_poles()

    def show_poles():
        line = ""
        line += '{:<{}s}'.format(str(A), str_len)
        line += '{:<{}s}'.format(str(B), str_len)
        line += '{:<{}s}'.format(str(C), str_len)
        print(line)

    A = list(range(n, 0, -1))
    B = []
    C = []
    str_len = len(str(A))

    show_poles()
    move_tower(n, A, C, B)
    print('\n')


hanoi_tower(5)


def memo(f):
    cache = {}
    def wrap(n):
        res = cache.get(n)
        if res is None:
            cache[n] = res = f(n)
        return res
    return wrap


@memo
def hanoi_moon(n):
    res = [[[]], [[]], [[]]]
    if n <= 0:
        return res
    last_step = hanoi_moon(n-1)
    res[0] = [[n] + i for i in last_step[0]] + last_step[1]
    res[1] = last_step[2] + last_step[0]
    res[2] = last_step[1] + [[n] + i for i in last_step[2]]
    
    return res


def show_poles(tower):
    str_len = len(str(tower[0][0]))
    for A, B, C in zip(*tower):
        line = ""
        line += '{:<{}s}'.format(str(A), str_len)
        line += '{:<{}s}'.format(str(B), str_len)
        line += '{:<{}s}'.format(str(C), str_len)
        print(line)
    print('\n')


show_poles(hanoi_moon(5))
