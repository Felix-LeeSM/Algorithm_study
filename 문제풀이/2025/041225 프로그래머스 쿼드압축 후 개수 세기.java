// https://school.programmers.co.kr/learn/courses/30/lessons/68936

import java.util.*;
import java.lang.*;

class Solution {
    public int[] solution(int[][] arr) {
        int n = arr.length;

        int[] answer = { 0, 0, 0 };

        switch (dc(arr, 0, 0, n, answer)) {
            case 0:
                answer[0] += 1;

                break;
            case 1:
                answer[1] += 1;

            default:
                break;
        }
        ;
        return Arrays.copyOfRange(answer, 0, 2);
    }

    public int dc(int[][] arr, int x, int y, int n, int[] ret) {
        if (n == 1) {
            return arr[x][y];
        }

        int one = dc(arr, x, y, n / 2, ret);
        int two = dc(arr, x + n / 2, y, n / 2, ret);
        int three = dc(arr, x, y + n / 2, n / 2, ret);
        int four = dc(arr, x + n / 2, y + n / 2, n / 2, ret);

        if (one == two && two == three && three == four) {
            return one;
        }
        ret[one]++;
        ret[two]++;
        ret[three]++;
        ret[four]++;

        return 2;

    }

    public static void main(String[] args) {
        System.out.println(Arrays.toString(new Solution().solution(new int[][] { new int[] { 1 } })));
    }

}