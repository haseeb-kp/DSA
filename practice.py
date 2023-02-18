class TrieNode:
    def __init__(self):
        self.children = {}
        self.end_of_word = False
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        current.end_of_word = True
    
    def search(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return current.end_of_word

    def starts_with(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                return False
            current = current.children[letter]
        return True

    def auto_complete(self, word):
        current = self.root
        for letter in word:
            if letter not in current.children:
                return []
            current = current.children[letter]
        return self.dfs(current,word)
    
    def dfs(self,current, word):
        data = []
        if current.end_of_word:
            data.append(word)
        for letter in current.children:
            data.extend(self.dfs(current.children[letter], word + letter))
        return data

trie = Trie()
trie.insert("haseeb")
print(trie.auto_complete("has"))
# print(trie.starts_with("s"))