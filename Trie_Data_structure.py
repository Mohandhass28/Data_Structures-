class Trie(object):
    class trienode(object):
        def __init__(self):
            self.chi = [None for _ in range(26)]
            self.end = False
    def __init__(self):
        self.root = self.trienode()
    def insert(self,word):
        cur = self.root
        for i in word:
            ch = ord(i) - ord('a')
            if cur.chi[ch] == None:
                cur.chi[ch] = self.trienode()
            cur = cur.chi[ch]
        cur.end = True
    def searching(self,word):
        cur = self.root
        for i in word:
            ch = ord(i) - ord('a')
            if cur.chi[ch] == None:
                return False
            cur = cur.chi[ch]
        return cur.end
    def prefix(self,word):
        cur = self.root
        for i in word:
            ch = ord(i) - ord('a')
            if cur.chi[ch] == None:
                return False
            cur = cur.chi[ch]
        return True


che = Trie()
che.insert('mohan')
p= che.searching('mohan')
o = che.prefix('mo')
print(o)