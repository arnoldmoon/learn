import string

class Node:
    def __init__(self, data=None, end=0, c={}):
        self.data = data
        self.c = c
        self.end = end

    def add_word(self, w, idx=0):
        if idx == len(w):
            self.end += 1
            return
        n_char = w[idx]
        n_node = self.c.get(n_char)
        if n_node is None:
            n_node = self.c[n_char] = Node(data=n_char, end=0, c={})
        n_node.add_word(w, idx=idx+1)

    def get_word(self, w, idx=-1):
        if idx == len(w) - 1:
            return self
        next_c = w[idx+1]
        next_n = self.c.get(next_c)
        if next_n is None:
            return
        return next_n.get_word(w, idx=idx+1)


class DocTree:
    CHAR_SET = set(string.ascii_letters)
    def char_only(self, w):
        return "".join(c for c in w if c in DocTree.CHAR_SET)

    def traverse(self, node, s=''):
        res = {}
        def _walk(n, word='', pend=0):
            if n is None:
                return
            
            if n.end > 0:
                wset = res.get(n.end)
                if wset is not None:
                    wset.add(word)
                else:
                    wset = set([word])
                    res[n.end] = wset

            for cn in n.c.values():
                _walk(cn, word+cn.data)

        _walk(node, s)
        return res

    def __init__(self, doc):
        self.head = Node()
        for w in doc.split():
            self.add_word(w)

    def add_word(self, w):
        self.head.add_word(self.char_only(w))

    def get_word_suggestion(self, w):
        end_node = self.head.get_word(w)
        return self.traverse(end_node, w)

doc_str = 'dog and cat and an animal. any ant andy ann'
doc_tree = DocTree(doc_str)
print(doc_tree.get_word_suggestion('an'))
