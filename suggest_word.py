import string

class Node:
    def __init__(self, data=None, word_cnt=0, c={}):
        self.data = data
        self.c = c
        self.word_cnt = word_cnt

    def add_word(self, w, idx=0, w_len=None):
        if w_len == None:
            w_len = len(w)
        if idx == w_len:
            self.word_cnt += 1
            return

        n_char = w[idx]
        n_node = self.c.get(n_char)
        if n_node is None:
            n_node = self.c[n_char] = Node(data=n_char, word_cnt=0, c={})
        n_node.add_word(w, idx=idx+1, w_len=w_len)

    def find_node(self, w, idx=-1, w_len=None):
        if w_len == None:
            w_len = len(w)
        if idx == w_len - 1:
            return self
        n_char = w[idx+1]
        n_node = self.c.get(n_char)
        if n_node is None:
            return
        return n_node.find_node(w, idx=idx+1, w_len=w_len)


class DocTree:
    CHAR_SET = set(string.ascii_letters)
    def char_only(self, w):
        return "".join(c for c in w if c in DocTree.CHAR_SET)

    def traverse(self, node, prefix=''):
        res = {}
        def _walk(n, word=''):
            if n is None:
                return
            
            if n.word_cnt > 0:
                wset = res.get(n.word_cnt)
                if wset is not None:
                    wset.append(word)
                else:
                    wset = [word]
                    res[n.word_cnt] = wset

            for cn in n.c.values():
                _walk(cn, word=word+cn.data)

        _walk(node, word=prefix)
        return res

    def __init__(self, doc):
        self.head = Node()
        for w in doc.split():
            self.add_word(w)

    def add_word(self, w):
        self.head.add_word(self.char_only(w))

    def get_word_suggestion(self, w):
        end_node = self.head.find_node(w)
        return self.traverse(end_node, prefix=w)

doc_str = 'dog and cat and an animal. any ant andy ann'
doc_tree = DocTree(doc_str)
print(doc_tree.get_word_suggestion('an'))
