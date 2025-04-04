from typing import List

MOD1 = 1_000_000_007
P1 = 31
MOD2 = 1_000_000_009
P2 = 37
MOD3 = 1_000_000_021
P3 = 41


class Solution:
    def findAnswer(self, parents: List[int], s: str) -> List[bool]:
        n = len(parents)
        children = [[] for _ in range(n)]
        for i, p in enumerate(parents):
            if p != -1:
                children[p].append(i)

        for i in range(n):
            children[i].sort()

        answer = [False] * n

        pows1 = [1] * (n + 1)
        pows2 = [1] * (n + 1)
        pows3 = [1] * (n + 1)

        for i in range(1, n + 1):
            pows1[i] = (pows1[i-1] * P1) % MOD1
            pows2[i] = (pows2[i-1] * P2) % MOD2
            pows3[i] = (pows3[i-1] * P3) % MOD3

        def compute_hashes(node):
            child_results = []
            for child in children[node]:
                child_results.append(compute_hashes(child))

            h1, h2, h3 = 0, 0, 0
            current_len = 0

            for ch1, ch2, ch3, _, _, _, clen in child_results:
                h1 = (h1 + ch1 * pows1[current_len]) % MOD1
                h2 = (h2 + ch2 * pows2[current_len]) % MOD2
                h3 = (h3 + ch3 * pows3[current_len]) % MOD3
                current_len += clen

            node_char_val = ord(s[node])
            h1 = (h1 + node_char_val * pows1[current_len]) % MOD1
            h2 = (h2 + node_char_val * pows2[current_len]) % MOD2
            h3 = (h3 + node_char_val * pows3[current_len]) % MOD3
            total_len = current_len + 1

            rh1 = node_char_val % MOD1
            rh2 = node_char_val % MOD2
            rh3 = node_char_val % MOD3
            current_rev_len = 1
            for _, _, _, crh1, crh2, crh3, clen in reversed(child_results):
                rh1 = (rh1 + crh1 * pows1[current_rev_len]) % MOD1
                rh2 = (rh2 + crh2 * pows2[current_rev_len]) % MOD2
                rh3 = (rh3 + crh3 * pows3[current_rev_len]) % MOD3
                current_rev_len += clen

            answer[node] = (h1 == rh1 and h2 == rh2 and h3 == rh3)

            result = (h1, h2, h3, rh1, rh2, rh3, total_len)
            return result

        compute_hashes(0)

        return answer


assert [True, True, False, True, True, True] ==\
    Solution()\
    .findAnswer([-1, 0, 0, 1, 1, 2], "aababa")

assert [True, True, True, True, True] ==\
    Solution()\
    .findAnswer([-1, 0, 0, 0, 0], "aabcb")
