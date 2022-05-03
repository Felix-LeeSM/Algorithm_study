'''
2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.

제한 조건
행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
곱할 수 있는 배열만 주어집니다.
입출력 예
arr1	arr2	return
[[1, 4], [3, 2], [4, 1]]	[[3, 3], [3, 3]]	[[15, 15], [15, 15], [15, 15]]
[[2, 3, 2], [4, 2, 4], [3, 1, 4]]	[[5, 4, 3], [2, 4, 1], [3, 1, 1]]	[[22, 22, 11], [36, 28, 18], [29, 20, 14]]

'''


def solution(arr1, arr2):
    i_1 = len(arr1)
    i_2, j_2 = len(arr2), len(arr2[0])
    answer = [[0]*j_2 for _ in range(i_1)]
    for i in range(i_1):
        for j in range(j_2):
            # answer[i][j]를 구할 것이다.
            for r in range(i_2):
                # NxM, MxK 행렬은 NxK 행렬을 만들고 각 M회 더해서 칸을 만든다.
                answer[i][j] += arr1[i][r] * arr2[r][j]
    return answer
