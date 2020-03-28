"""Hanio tower."""


def hanoi_tower(n):
    """Grabbed from online as a validation tool."""
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
        line += '{:<{}s}'.format(str(a), str_len)
        line += '{:<{}s}'.format(str(b), str_len)
        line += '{:<{}s}'.format(str(c), str_len)
        print(line)

    a = list(range(n, 0, -1))
    b = []
    c = []
    str_len = len(str(a))

    show_poles()
    move_tower(n, a, c, b)
    print('\n')


def memo(f):
    """Memoize and return."""
    cache = {}

    def wrap(n):
        res = cache.get(n)
        if res is None:
            cache[n] = res = f(n)
        return res
    return wrap


@memo
def hanoi_moon(n):
    """
    Construct hanoi tower sequence and return as a nested list.

    argument:
    n: initial number of discs at 'from' pole.

    @return: discs on a pole for each step x each poles.
             [[[], []...[]],
              [[], []...[]],
              [[], []...[]]]
    """
    res = [[[]], [[]], [[]]]
    if n <= 0:
        return res
    last_step = hanoi_moon(n-1)
    res[0] = [[n] + i for i in last_step[0]] + last_step[1]
    res[1] = last_step[2] + last_step[0]
    res[2] = last_step[1] + [[n] + i for i in last_step[2]]

    return res


def show_poles(tower):
    """Format hanoi_moon and print."""
    str_len = len(str(tower[0][0]))
    for a, b, c in zip(*tower):
        line = ""
        line += '{:<{}s}'.format(str(a), str_len)
        line += '{:<{}s}'.format(str(b), str_len)
        line += '{:<{}s}'.format(str(c), str_len)
        print(line)
    print('\n')


show_poles(hanoi_moon(1))
show_poles(hanoi_moon(2))
show_poles(hanoi_moon(3))
show_poles(hanoi_moon(4))


@memo
def hanoi_moon_bit(n):
    """
    Construct hanoi tower sequence and return as a list.

    argument:
    n: initial number of discs at 'from' pole.

    @return: int with each bit represents if the coresponding disc is
             present of not.
             [[int, int...int],
              [int, int...int],
              [int, int...int]]
    """
    res = [[0], [0], [0]]
    solution_n = 0
    while solution_n < n:
        # ignore larges disc and move whole tower to middle pole
        res[1], res[2] = res[2], res[1]
        last_seq_len = len(res[0])
        # move whole tower from middle pole to target pole
        # if largest disc were present under source pole for the first half
        # the sequence then under target pole for the later half,
        # solution is complete.
        for i in range(last_seq_len):
            res[0].append(res[2][i])
            res[1].append(res[0][i])
            res[2].append(res[1][i])
            res[0][i] |= 1 << solution_n
            res[2][i+last_seq_len] |= 1 << solution_n
        solution_n += 1
    return res


def show_poles_bin(tower, n):
    """Format binary from hanoi_moon_bit and print."""
    def format_bin(b):
        return format(b, 'b').zfill(n)

    for a, b, c in zip(*tower):
        print(format_bin(a), format_bin(b), format_bin(c))
    print('\n')


show_poles_bin(hanoi_moon_bit(1), 1)
show_poles_bin(hanoi_moon_bit(2), 2)
show_poles_bin(hanoi_moon_bit(3), 3)
show_poles_bin(hanoi_moon_bit(4), 4)
