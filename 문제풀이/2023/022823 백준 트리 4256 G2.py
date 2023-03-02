from sys import argv, stdin
input = stdin.readline


def solution(nodes: int, preOrder: list[int], inOrder: list[int]) -> str:
    def recursion(subRoot: int, start: int, end: int, postOrder: list[int] = []) -> None:

        if start > end:
            return

        for idx in range(start, end):
            if inOrder[idx] == preOrder[subRoot]:

                recursion(subRoot + 1, start, idx, postOrder)
                recursion(subRoot-start + idx + 1, idx+1, end, postOrder)

                postOrder.append(preOrder[subRoot])
                break

        return postOrder

    postOrder = recursion(0, 0, nodes)

    return postOrder


def main(args=argv) -> int:

    TestCase = int(input())

    for case in range(TestCase):
        nodes = int(input())
        preOrder = list(map(int, input().split()))
        inOrder = list(map(int, input().split()))

        answer = solution(nodes, preOrder, inOrder)
        print(*answer)

    return 1


if __name__ == '__main__':
    main()
