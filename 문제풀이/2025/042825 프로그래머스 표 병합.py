from sys import maxsize

UPDATE = 'UPDATE'
MERGE = 'MERGE'
UNMERGE = 'UNMERGE'
PRINT = 'PRINT'
EMPTY = 0


def solution(commands):
    board = [[EMPTY] * 51 for _ in range(51)]
    merge = [[EMPTY] * 51 for _ in range(51)]

    def merge_val(val1, val2):
        if val1 == EMPTY:
            return val2
        return val1

    def id_gen():
        for i in range(1, maxsize):
            yield i

    next_id = id_gen().__next__

    answer = []

    for command in map(lambda cmd: cmd.split(), commands):
        if command[0] == UPDATE and len(command) == 4:
            _, r, c, val = command
            r, c = int(r), int(c)

            merge_id = merge[r][c] or -1

            for i in range(1, 51):
                for j in range(1, 51):
                    if merge_id == merge[i][j]:
                        board[i][j] = val

            board[r][c] = val

        elif command[0] == UPDATE and len(command) == 3:
            _, val1, val2 = command
            for i in range(1, 51):
                for j in range(1, 51):
                    if board[i][j] == val1:
                        board[i][j] = val2

        elif command[0] == MERGE and len(command) == 5:
            _, r1, c1, r2, c2 = command
            r1, c1, r2, c2 = int(r1), int(c1), int(r2), int(c2)

            merge_id = next_id()
            target_ids = (merge[r1][c1] or -1, merge[r2][c2] or -1)
            val = board[r1][c1] or board[r2][c2]

            merge[r1][c1] = merge_id
            merge[r2][c2] = merge_id
            board[r1][c1] = val
            board[r2][c2] = val

            for i in range(1, 51):
                for j in range(1, 51):
                    if merge[i][j] in target_ids:
                        merge[i][j] = merge_id
                        board[i][j] = val

        elif command[0] == UNMERGE:
            _, r, c = command
            r, c = int(r), int(c)

            merge_id = merge[r][c]
            prev_val = board[r][c]

            if merge_id != EMPTY:
                for i in range(1, 51):
                    for j in range(1, 51):
                        if merge[i][j] == merge_id:
                            merge[i][j] = EMPTY
                            board[i][j] = EMPTY

                board[r][c] = prev_val
            pass

        elif command[0] == PRINT:
            _, r, c = command
            r, c = int(r), int(c)
            answer.append(board[r][c] if board[r][c] != EMPTY else 'EMPTY')
            pass

    return answer


assert ["EMPTY", "group"] == \
    solution(
    [
        "UPDATE 1 1 menu",
        "UPDATE 1 2 category",
        "UPDATE 2 1 bibimbap",
        "UPDATE 2 2 korean",
        "UPDATE 2 3 rice",
        "UPDATE 3 1 ramyeon",
        "UPDATE 3 2 korean",
        "UPDATE 3 3 noodle",
        "UPDATE 3 4 instant",
        "UPDATE 4 1 pasta",
        "UPDATE 4 2 italian",
        "UPDATE 4 3 noodle",
        "MERGE 1 2 1 3",
        "MERGE 1 3 1 4",
        "UPDATE korean hansik",
        "UPDATE 1 3 group",
        "UNMERGE 1 4",
        "PRINT 1 3",
        "PRINT 1 4"])


assert ["d", "EMPTY"] == \
    solution(["UPDATE 1 1 a",
              "UPDATE 1 2 b",
              "UPDATE 2 1 c",
              "UPDATE 2 2 d",
              "MERGE 1 1 1 2",
              "MERGE 2 2 2 1",
              "MERGE 2 1 1 1",
              "PRINT 1 1",
              "UNMERGE 2 2",
              "PRINT 1 1"])
