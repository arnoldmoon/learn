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


class Node:
    def __init__(self, data=None, priority=None, l=None, r=None):
        self.data = data
        self.priority = priority
        self.l = l
        self.r = None

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

        next_node.append(x, p)


class Tree:
    def __init__(self):
        self.head = Node()

    def append(self, x, p):
        return self.head.append(x, p)

    def traverse(self):
        def _helper(node):
            r = node.r
            if node.r is not None:
                _helper(node.r)
            result.append(node.data)
            l = node.l
            if node.l is not None:
                _helper(node.l)

        if self.head is None:
            return None
        result = []
        _helper(self.head)
        return result

def most_frequent_n(l, n):
    """
    from input list, returns n most frequent items as a non-sorted list.
    if input list is None, return value will be None,
    if input list is empty, return value will be an empty list.
    """
    if l is None:
        return None
    input_len = len(l)
    if input_len < 2:
        return l

    l_dict = {}

    for i in l:
        current = l_dict.get(i)
        l_dict[i] = count = 1 if current is None else current + 1

    result = Tree()
    for x, p in l_dict.items():
        result.append(x, p)

    return result.traverse()[:n]


l = [1, 2, 3, 5, 2, 3, 7, 8, 4, 6, 8, 10, 3, 3, 2, 4, 1, 4, 3, 3]
print(sorted(set(l), key = lambda X:l.count(X), reverse=True))

print(most_frequent(l))
print(most_frequent_n(l, 3))

