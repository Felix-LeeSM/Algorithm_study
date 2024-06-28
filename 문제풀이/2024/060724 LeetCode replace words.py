from typing import Dict, List


class TrieNode:
    def __init__(self):

        self.trie: Dict[str, TrieNode] = {}
        self.val = None

    def __setitem__(self, key: str, value: str):
        node = self
        for char in key:
            if char not in node.trie:
                node.trie[char] = TrieNode()
            node = node.trie[char]
        node.val = value

    def __getitem__(self, word: str):
        node = self
        for char in word:
            if char not in node.trie:
                return word
            node = node.trie[char]

            if node.val is not None:
                return node.val
        return word


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root = TrieNode()

        for word in dictionary:
            root[word] = word

        return ' '.join(map(root.__getitem__, sentence.split()))


assert "a b c d" == Solution()\
    .replaceWords(
        ["a", "b", "c", "d"],
        "aadsfasf bsbs cbbab dcadsfafs")
assert "the cat was rat by the bat" == Solution()\
    .replaceWords(
        ["cat", "bat", "rat"],
        "the cattle was rattled by the battery")
