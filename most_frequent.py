def most_frequent(l):
    """
    from input list, returns most frequent item.
    if input list is None or empty, return value will be None.
    """
    input_len = 0 if l is None else len(l)
    if input_len == 0:
        return None
    if input_len < 3:
        return l[0]

    l_dict = {}
    half_total = input_len * 0.5

    result = None
    max_freq = 0

    for i in l:
        current = l_dict.get(i)
        l_dict[i] = count = 1 if current is None else current + 1

        if count > max_freq:
            max_freq = count
            result = i

        if count > half_total:
            break

    return result

def bubble_sort_by_val(d):
    if d is None:
        return None

    result = []
    result.extend(d.keys())
    d_len = len(result)

    while True:
        done = True
        i = 0
        while i < d_len - 1:
            x, y = result[i], result[i+1]
            a, b = d[x], d[y]
            if a < b:
                done = False
                result[i+1], result[i] = x, y
            i += 1

        if done:
            break

    return result

def most_frequent_n(l, n):
    """
    from input list, returns n most frequent items as a sorted list.
    if input list is None, return value will be None,
    if input list is empty, return value will be an empty list.
    """
    if l is None:
        return None
    input_len = len(l)
    if input_len < 2:
        return l

    elem_cnt = {}

    for i in l:
        cur_cnt = elem_cnt.get(i)
        elem_cnt[i] = cnt =\
            1 if cur_cnt is None else cur_cnt + 1

    result = bubble_sort_by_val(elem_cnt)
    return result[:n]


#additional practice
class Node:
    """
    modified binary insertion node class for most frequent function.
    instead of comparing self.data, self.priority will get compared
    for insertion.
    """
    def __init__(self, data=None, priority=None, l=None, r=None):
        self.data = data
        self.priority = priority
        self.l = l
        self.r = r

    def append(self, x, p):
        if self.data is None:
            self.data = x
            self.priority = p
            return self

        if p < self.priority:
            next_node = self.l
            if next_node is None:
                next_node = self.l = Node()
        else:
            next_node = self.r
            if next_node is None:
                next_node = self.r = Node()

        return next_node.append(x, p)


class BinaryInsertionSort:
    def __init__(self):
        self.head = Node()

    def append(self, x, p):
        return self.head.append(x, p)

    def traverse(self):
        """
        traverse is in-order so lowest priority will be returned first.
        """
        result = []
        def _helper(node):
            if node is None:
                return
            _helper(node.l)
            result.append(node.data)
            _helper(node.r)

        if self.head is None:
            return None

        _helper(self.head)
        return result


def bubble_sort(l):
    l_len = 0 if l is None else len(l)
    if l_len < 2:
        return l

    while True:
        done = True
        i = 0
        while i < l_len - 1:
            a, b = l[i], l[i+1]
            if a > b:
                done = False
                l[i+1], l[i] = a, b
            i += 1

        if done:
            break

    return l

def quick_sort(l):
    def _helper(x):
        if x is None or len(x) == 0:
            return []

        pivot_val = x[0]
        pivot = []
        l = []
        r = []
        while len(x) > 0:
            current = x.pop()
            if current < pivot_val:
                l.append(current)
                continue
            if current > pivot_val:
                r.append(current)
                continue
            pivot.append(current)
        return _helper(l)\
               + pivot\
               + _helper(r)

    return _helper(l)

def quick_sort_inplace(l):
    def _helper(x, left, right):
        if left >= right:
            return

        pivot_val = x[left]
        piv_head = left
        piv_tail = left
        idx = left + 1
        while idx <= right:
            current = x[idx]

            if current > pivot_val:
                idx += 1
                continue

            swap_idx = piv_tail + 1
            if idx != swap_idx:
                x[idx], x[swap_idx] = x[swap_idx], x[idx]

            if current == pivot_val:
                piv_tail += 1
                idx += 1
                continue

            if current < pivot_val:
                x[piv_head], x[swap_idx] = x[swap_idx], x[piv_head]
                piv_head += 1
                piv_tail += 1
                idx += 1
                continue

        _helper(x, left, piv_head-1)
        _helper(x, piv_tail+1, right)

    l_len = 0 if l is None else len(l)
    if l_len < 2:
        return l

    _helper(l, 0, l_len-1)
    return l


l = [5, 1, 5, 2, 7, 5, 3, 5, 8, 9, 2, 3]

print(l)
print(sorted(set(l), key = lambda X:l.count(X), reverse=True))

print(most_frequent(l))
print(most_frequent_n(l, 3))
print(bubble_sort(list(l)))
print(quick_sort(list(l)))
print(quick_sort_inplace(list(l)))
