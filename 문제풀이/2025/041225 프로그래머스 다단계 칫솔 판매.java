// https://school.programmers.co.kr/learn/courses/30/lessons/77486

import java.util.*;

class Solution {
    public int[] solution(String[] enroll, String[] referral, String[] seller, int[] amount) {

        HashMap<String, Integer> userIds = new HashMap<>();

        for (int i = 0; i < enroll.length; i++) {
            String user = enroll[i];
            userIds.put(user, i + 1);
        }

        int[] parents = new int[enroll.length + 1];

        int root = 0;

        for (int i = 0; i < referral.length; i++) {
            String refer = referral[i];
            String user = enroll[i];
            Integer userId = userIds.get(user);

            Integer referralId = refer.equals("-") ? root : userIds.get(refer);

            parents[userId] = referralId;
        }

        int[] earns = new int[enroll.length + 1];

        for (int i = 0; i < seller.length; i++) {
            String sell = seller[i];
            int money = amount[i] * 100;

            Integer userId = userIds.get(sell);

            while (userId != root) {

                earns[userId] += (money - money / 10);
                money /= 10;
                userId = parents[userId];

            }
        }

        return Arrays.copyOfRange(earns, 0, enroll.length + 1);
    }
}