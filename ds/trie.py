class TrieNode:
    def __init__(self):
        self.trie = {}
        self.is_end_of_word = False
        self.word_count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        p_root = self.root
        for k in key:
            if k not in p_root.trie:
                p_root.trie[k] = TrieNode()
            p_root = p_root.trie[k]

        p_root.is_end_of_word = True
        p_root.word_count += 1

    def search(self, key):
        p_root = self.root
        for k in key:
            if k not in p_root.trie:
                return False
            p_root = p_root.trie[k]
        return True if p_root.is_end_of_word else False

    def delete(self, key, p_root):
        if len(key) == 0:
            if not p_root.is_end_of_word:
                return False

            if p_root.word_count > 1:
                p_root.word_count -= 1
                return False
            p_root.is_end_of_word = False
            return len(p_root.trie) == 0

        if key[0] not in p_root.trie:
            return False

        p_root = p_root.trie[key[0]]
        key = key[1:]

        is_delete_node = self.delete(key, p_root)

        if is_delete_node:
            if len(p_root.trie):
                return False
            else:
                del(p_root.trie)
                return True
        return False

strings = ["abc", "abgl", "cdf", "abcd", "lmn", "abcd"]

MyTrie = Trie()

for s in strings:
    print "\"{}\" - added".format(s)
    MyTrie.insert(s)

s = "abc"
print "\"{}\" - Delete".format(s)
MyTrie.delete(s, MyTrie.root)
print "\"{}\" - Found".format(s) if MyTrie.search(s) else "\"{}\" - Not found".format(s)

s = "abg"
print "\"{}\" - Found".format(s) if MyTrie.search(s) else "\"{}\" - Not found".format(s)

s = "abcd"
print "\"{}\" - Delete".format(s)
MyTrie.delete(s, MyTrie.root)
print "\"{}\" - Found".format(s) if MyTrie.search(s) else "\"{}\" - Not found".format(s)

