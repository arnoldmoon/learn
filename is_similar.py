
import numpy
import random
import string

class Keyboard:
    KEYB_MAP = [['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'],
                ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'],
                ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'],
                ['z', 'x', 'c', 'v', 'b', 'n', 'm']]
    KEYB_TABLE = dict((key, numpy.array((row, col), dtype=numpy.double))
                      for row, row_keys in enumerate(KEYB_MAP)
                      for col, key in enumerate(row_keys))

    @staticmethod
    def dist(x, y, case_penalty=0.5):
        if x == y:
            return 0.0
        _x = x.lower()
        _y = y.lower()
        if _x == _y:
            return case_penalty
        return numpy.linalg.norm(Keyboard.KEYB_TABLE[_x]
                                 - Keyboard.KEYB_TABLE[_y])

class Util:
    @staticmethod
    def compare_optimizer(func):
        memo = {}
        def wrapper(x, y, **kwargs):
            cached = memo.get((x, y))
            if cached is not None:
                return cached

            if x == y:
                memo[(x, y)] = result = 1.0
                return result

            common_set = set(x).intersection(y)
            if len(common_set) == 0:
                memo[(x, y)] = result =  0.0
                return result

            memo[(x, y)] = result = func(x, y, **kwargs)
            return result
        return wrapper


class SComp:
    '''
    custom string compare methods.
    '''

    @staticmethod
    @Util.compare_optimizer
    def length(x, y):
        '''
        compare two words using word length.
        return value will be normalized between 0 - 1,
        larger value means more similarity between two input words.
        @usage : length(x:str, y:str) -> float
        @return: float normalized proximity.
        '''
        x_len = len(x)
        y_len = len(y)
        diff = abs(x_len - y_len)
        rel_diff = float(diff) / max(x_len, y_len)
        return 1 - rel_diff

    @staticmethod
    @Util.compare_optimizer
    def matching_subsequence(x, y):
        '''
        compare two words using common characters with matching order.
        ie "abcde" and "abecd" has four common characters,
        return value will be normalized between 0 - 1,
        larger value means more similarity between two input words.
        @usage : matching_subsequence(x:str, y:str) -> float
        @return: float normalized proximity.
        '''
        memo={}
        len_x = len(x)
        len_y = len(y)

        def helper(_x, _y, l_x=0, l_y=0):
            cached = memo.get((l_x, l_y))
            if cached is not None:
                return cached

            if l_x >= len_x or l_y >= len_y:
                memo[(l_x, l_y)] = 0
                return 0

            result = max(helper(_x, _y, l_x=l_x+1, l_y=l_y),
                         helper(_x, _y, l_x=l_x, l_y=l_y+1),
                         helper(_x, _y, l_x=l_x+1, l_y=l_y+1)
                         + (1 if _x[l_x] == _y[l_y] else 0))
            memo[(l_x, l_y)] = result
            return result

        return float(helper(x, y)) / max(len_x, len_y)

    @staticmethod
    @Util.compare_optimizer
    def matching_substring(x, y):
        '''
        compare two words using longest matching substring.
        return value will be normalized between 0 - 1,
        larger value means more similarity between two input words.
        @usage : matching_substring(x:str, y:str) -> float
        @return: float normalized proximity.
        '''
        def helper(_x, _y):
            len_x = len(_x)
            len_y = len(_y)
            l_x = l_y = temp = 0
            result = 0

            while True:
                if temp > result:
                    result = temp

                if l_x >= len_x or l_y >= len_y:
                    break

                if _x[l_x] == _y[l_y]:
                    temp += 1
                    l_x += 1
                    l_y += 1
                    continue

                l_x += 1
                l_y = 0
                temp = 0
            return result

        max_len = max(len(x), len(y))
        return float(max(helper(x, y), helper(y, x))) / max_len

    @staticmethod
    @Util.compare_optimizer
    def moon_typo_dist(x, y, max_dist=1.4142):
        '''
        compare two words using physical key position, further
        the non-matching character on a keyboard, more penalty.
        return value will be normalized between 0 - 1,
        larger value means more similarity between two input words.
        @usage : moon_typo_dist(x:str, y:str, max_dist=float) -> float
        @return: float normalized proximity.
        '''
        memo = {}
        len_x = len(x)
        len_y = len(y)

        def helper(_x, _y, l_x=0, l_y=0):
            cached = memo.get((l_x, l_y))
            if cached is not None:
                return cached

            if l_x >= len_x or l_y >= len_y:
                result = abs((len_x - l_x) - (len_y - l_y)) * max_dist
            else:
                result = min(helper(_x, _y, l_x=l_x+1, l_y=l_y) + max_dist,
                             helper(_x, _y, l_x=l_x, l_y=l_y+1) + max_dist,
                             helper(_x, _y, l_x=l_x+1, l_y=l_y+1)\
                             + min(Keyboard.dist(_x[l_x], _y[l_y]), max_dist))

            memo[(l_x, l_y)] = result
            return result

        worst_dist = max_dist * max(len(x), len(y))
        return 1 - (helper(x, y) / worst_dist)

    @staticmethod
    @Util.compare_optimizer
    def matching_components(x, y):
        '''
        compare two words using how many times each character appears
        among the two input words.
        return value will be normalized between 0 - 1,
        larger value means more similarity between two input words.
        @usage : matching_components(x:str, y:str) -> float
        @return: float normalized proximity.
        '''
        all_compo = dict((c, 0) for c in set(x + y))

        for c in x:
            all_compo[c] += 1
        for c in y:
            all_compo[c] -= 1

        len_all = len(x) + len(y)
        diff = sum(abs(i) for i in all_compo.values())
        return 1 - (float(diff) / len_all)

    @staticmethod
    def moon_compare(x, y):
        result = []
        result.append(SComp.length(x, y))
        result.append(SComp.moon_typo_dist(x, y))
        result.append(SComp.matching_substring(x, y))
        result.append(SComp.matching_subsequence(x, y))
        result.append(SComp.matching_components(x, y))
        return result


class Validation:
    '''
    class for validating custom methods against established algorithms.
    '''
    CHARS = string.ascii_letters + string.digits
    MIN_LENGTH = 3
    MAX_LENGTH = 10

    @staticmethod
    def random_string(min_length=None, max_length=None, seed=None):
        if seed is None:
            seed = random.random()
        random.seed(seed)
        length = random.randint(
            min_length if min_length is not None else Validation.MIN_LENGTH,
            max_length if max_length is not None else Validation.MAX_LENGTH)
        result = ''
        for i in range(length):
            random.seed(i + seed)
            result += random.choice(Validation.CHARS)
        return result

    @staticmethod
    def validate(func, v_func, num_samples=50, seed=None):
        def match(a, b, i, num_samples, rev=False):
            match_samples = int(num_samples * i)
            if not rev:
                l = 0
                r = match_samples
            else:
                l = num_samples - match_samples
                r = num_samples
            sample_a = set(a[l:r])
            sample_b = set(b[l:r])
            num_match = len(sample_a.intersection(sample_b))
            return float(num_match) / match_samples

        if seed is not None:
            random.seed(seed + 0.1)
            seed_a = random.random()
            random.seed(seed + 0.2)
            seed_b = random.random()
        else:
            seed_a = random.random()
            seed_b = random.random()
        x = Validation.random_string(seed=seed_a)
        word_pool = [Validation.random_string(seed=i+seed_b)
                     for i in range(num_samples)]
        v_result = [v_func(x, y) for y in word_pool]
        v_idx = sorted(range(num_samples), key=lambda X:v_result[X])
        f_result = [func(x, y) for y in word_pool]
        f_idx = sorted(range(num_samples), key=lambda X:f_result[X])
        print('{} vs {}'.format(func.__name__, v_func.__name__))
        print('{:.2%} match for top 25%'
            .format(match(v_idx, f_idx, 0.25, num_samples)))
        print('{:.2%} match for top 50%'
            .format(match(v_idx, f_idx, 0.5, num_samples)))
        print('{:.2%} match for bottom 25%'
            .format(match(v_idx, f_idx, 0.25, num_samples, rev=True)))
        print()

    @staticmethod
    def l_dist(x, y):
        memo = {}
        len_x = len(x)
        len_y = len(y)
        def helper(_x, _y, l_x=0, l_y=0):
            cached = memo.get((l_x, l_y))
            if cached is not None:
                return cached
            if l_x >= len_x or l_y >= len_y:
                result = abs((len_x - l_x) - (len_y - l_y))
            else:
                result = min(helper(_x, _y, l_x=l_x+1, l_y=l_y) + 1,
                             helper(_x, _y, l_x=l_x, l_y=l_y+1) + 1,
                             helper(_x, _y, l_x=l_x+1, l_y=l_y+1)
                             + (0 if _x[l_x] == _y[l_y] else 1))
            memo[(l_x, l_y)] = result
            return result
        return helper(x, y)

    @staticmethod
    def cosign(x, y):
        import numpy
        axis = set(x).union(set(y))
        axis_len = len(axis)
        axis_idx = dict((w, idx) for idx, w in enumerate(axis))
        vector_x = [0] * axis_len
        vector_y = [0] * axis_len
        for i in x:
            vector_x[axis_idx[i]] += 1
        for i in y:
            vector_y[axis_idx[i]] += 1
        return numpy.dot(vector_x, vector_y)\
               / (numpy.linalg.norm(vector_x) * numpy.linalg.norm(vector_y))

    @staticmethod
    def trigram(x, y):
        _x = '_' + x + '_'
        _y = '_' + y + '_'
        x_tg = set([_x[i:i+3] for i in range(len(x))])
        y_tg = set([_y[i:i+3] for i in range(len(y))])
        n_unique = len(x_tg.union(y_tg))
        n_intersect = len(x_tg.intersection(y_tg))
        return float(n_intersect) / n_unique

    @staticmethod
    def jaro_dist(x, y):
        match = []
        y_compo = set(y)
        match_idx = dict((i, []) for i in y_compo)
        for idx in range(len(y)-1, -1, -1):
            i = y[idx]
            match_idx[i].append(idx)
        for i in x:
            if i not in match_idx.keys():
                continue
            m_idx = match_idx[i]
            match.append(m_idx.pop())
            if len(m_idx) == 0:
                match_idx.pop(i)
        t = 0.0
        m = len(match)
        for i, j in zip(match, sorted(match)):
            if i == j:
                continue
            t += 0.5
        if m == 0:
            return 0
        t = int(t)
        return (m / len(x) + m / len(y) + (m - t) / m) / 3


seed = random.random()
Validation.validate(SComp.moon_compare, Validation.l_dist, num_samples=1000, seed=seed)
Validation.validate(SComp.moon_compare, Validation.cosign, num_samples=1000, seed=seed)
Validation.validate(SComp.moon_compare, Validation.trigram, num_samples=1000, seed=seed)
Validation.validate(SComp.moon_compare, Validation.jaro_dist, num_samples=1000, seed=seed)
