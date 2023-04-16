class Trinode:
    def __init__(self):
        self.child = {}
        self.endofwode = False

class Trie:
    def __init__(self):
        self.root = Trinode()

    def inserte(self, word):
        cur = self.root
        for i in word:
            if i not in cur.child:
                cur.child[i] = Trinode()
            cur = cur.child[i]
        cur.endofwode = True

    def search(self, wo):
        cur = self.root
        for i in wo:
            if i not in cur.child:
                return False
            cur = cur.child[i]
        return cur.endofwode

    def startwith(self, prefex):
        cur = self.root
        for i in prefex:
            if i not in cur.child:
                return False
            cur = cur.child[i]
        return True

tri = Trie()
tri.inserte('Mohan')
tri.search('Mohan')