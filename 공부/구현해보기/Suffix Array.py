class SuffixArrayNaive:
    suffix_array: list[int]

    def __init__(self, text: str):
        suffixes = [(text[i:], i) for i in range(len(text))]
        suffixes.sort()

        self.suffix_array = [idx for (_suffix, idx) in suffixes]


class SuffixArrayPrefixDoubling:
    """Manber-Myers Prefix Doubling Algorithm (O(n log n))"""
    suffix_array: list[int]

    def __init__(self, text: str):
        length = len(text)
        suffix_array = list(range(length))

        ranks = [ord(c) for c in text]
        temp_ranks = [0] * length

        def rank_key(idx, step):
            return (ranks[idx], ranks[idx + step] if (idx + step < length) else -1)

        for expo in range(1_000):
            step = 1 << expo
            suffix_array.sort(key=lambda i: rank_key(i, step))

            temp_ranks[suffix_array[0]] = 0
            for i in range(length-1):
                temp_ranks[suffix_array[i+1]] = temp_ranks[suffix_array[i]]
                if rank_key(suffix_array[i+1], step) != rank_key(suffix_array[i], step):
                    temp_ranks[suffix_array[i+1]] += 1

            ranks = temp_ranks[:]
            if ranks[suffix_array[-1]] == length - 1 or length <= step:
                break

        self.suffix_array = suffix_array
# 1개 문자만 비교하기
# 1개 문자와 그 다음 문자 비교하기 (각 자리는 2개 문자를 기준으로 정렬됨.)
# 2개 문자와 그 다음 2개 문자 비교하기 (각 자리는 4개의 문자를 기준으로 정렬됨.)
# 4개 문자와 그 다음 4개 문자 비교하기 (각 자리는 8개의 문자를 기준으로 정렬됨.)
# ... O(nLogn)


if __name__ == "__main__":
    test_cases = [
        ("banana", [5, 3, 1, 0, 4, 2]),
        ("mississippi", [10, 7, 4, 1, 0, 9, 8, 6, 3, 5, 2]),
        ("abracadabra", [10, 7, 0, 3, 5, 8, 1, 4, 6, 9, 2]),
        ("abcabcabc", [6, 3, 0, 7, 4, 1, 8, 5, 2]),
        ("aaaaaa", [5, 4, 3, 2, 1, 0]),
        ("bbbb", [3, 2, 1, 0]),
    ]

    for text, expected in test_cases:
        # Naive
        sa_naive = SuffixArrayNaive(text)
        assert expected == sa_naive.suffix_array, f'naive suffix array failure, {text}'

        # Prefix Doubling
        sa_pd = SuffixArrayPrefixDoubling(text)
        assert expected == sa_pd.suffix_array, f'prefix doubling suffix array failure, {text}'
