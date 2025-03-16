from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        overlap_indexs = [[] for _ in range(len(s))]
        for word in wordDict:
            for i in range(len(s) - len(word) + 1):
                if s[i:i+len(word)] == word:
                    overlap_indexs[i].append((word, i + len(word)))
        answer = []
        curr_words = []

        def dfs(curr_idx: int):
            if curr_idx == len(s):
                answer.append(" ".join(curr_words))
                return
            for word, next_idx in overlap_indexs[curr_idx]:
                curr_words.append(word)
                dfs(next_idx)
                curr_words.pop()

        dfs(0)
        return answer


if __name__ == '__main__':
    assert (
        sorted(Solution().wordBreak(
            "pineapplepenapple",
            ["apple", "pen", "applepen", "pine", "pineapple"]
        )),
        sorted(["pine apple pen apple", "pineapple pen apple", "pine applepen apple"])
    )
    assert (
        sorted(Solution().wordBreak(
            "catsanddog",
            ["cat", "cats", "and", "sand", "dog"]
        )),
        sorted(["cats and dog", "cat sand dog"])
    )
