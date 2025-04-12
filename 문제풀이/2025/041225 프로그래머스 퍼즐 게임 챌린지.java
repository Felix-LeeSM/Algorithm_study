// https://school.programmers.co.kr/learn/courses/30/lessons/340212

import java.util.*;

class Solution {
    public int solution(int[] diffs, int[] times, long limit) {
        int left = 1;
        int right = 100_001;

        while (left < right) {
            int mid = (left + right) / 2;

            if (isReachable(diffs, times, limit, mid)) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }

        return left;

    }

    public boolean isReachable(int[] diffs, int[] times, long limit, int level) {
        long time = 0l;

        time += times[0];
        int prev_time = times[0];

        for (int i = 1; i < times.length; i++) {
            int diff = diffs[i];
            int cur_time = times[i];

            if (level < diff) {
                int wrong = diff - level;
                time += wrong * (cur_time + prev_time);
            }
            time += cur_time;
            prev_time = cur_time;

            if (time < 0 || limit < time) {
                return false;
            }

        }

        return true;
    }
}