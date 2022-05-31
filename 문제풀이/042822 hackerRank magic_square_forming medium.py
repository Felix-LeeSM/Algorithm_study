'''
We define a magic square to be an  matrix of distinct positive integers from  to  where the sum of any row, column, or diagonal of length  is always equal to the same number: the magic constant.

You will be given a  matrix  of integers in the inclusive range . We can convert any digit  to any other digit  in the range  at cost of . Given , convert it into a magic square at minimal cost. Print this cost on a new line.

Note: The resulting magic square must contain distinct integers in the inclusive range .

Example

$s = [[5, 3, 4], [1, 5, 8], [6, 4, 2]]

The matrix looks like this:

5 3 4
1 5 8
6 4 2
We can convert it to the following magic square:

8 3 4
1 5 9
6 7 2
This took three replacements at a cost of abs(5 - 8) + abs(8 - 9) + abs(4 - 7) = 7.

Function Description

Complete the formingMagicSquare function in the editor below.

formingMagicSquare has the following parameter(s):

int s[3][3]: a  array of integers
Returns

int: the minimal total cost of converting the input square to a magic square
Input Format

Each of the  lines contains three space-separated integers of row .

Constraints

Sample Input 0
4 9 2
3 5 7
8 1 5
Sample Output 0
1


Sample Input 1
4 8 2
4 5 7
6 1 6
Sample Output 1
4

'''


def formingMagicSquare(s):

    def rotate(s):
        return [[s[i][2-j] for i in range(3)] for j in range(3)]

    def flip_side(s):
        return [[s[i][j] for j in range(-1, -4, -1)] for i in range(3)]

    def flip_up(s):
        return [[s[i][j] for j in range(3)] for i in range(-1, -4, -1)]

    def check(p):
        return sum([sum([abs(s[i][j]-p[i][j]) for i in range(3)]) for j in range(3)])

    ans = 72
    test = [[8, 3, 4], [1, 5, 9], [6, 7, 2]]
    for r in range(4):
        test = rotate(test)
        for f_u in range(2):
            test = flip_up(test)
            for f_s in range(2):
                test = flip_side(test)
                ans = min(check(test), ans)
    return ans
