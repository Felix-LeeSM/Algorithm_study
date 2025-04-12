// https://school.programmers.co.kr/learn/courses/30/lessons/86971

import java.util.*;

class Solution {

    public int solution(int n, int[][] wires) {
        int[] children = new int[n + 1];

        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i <= n; i++) {
            graph.add(new ArrayList<>());
        }

        for (int[] edge : wires) {
            graph.get(edge[0]).add(edge[1]);
            graph.get(edge[1]).add(edge[0]);
        }

        int root = 1;
        boolean[] visited = new boolean[n + 1];
        dfs(root, graph, visited, children);
        children[root] = n;

        int gap = n;

        for (int child : children) {
            if (java.lang.Math.abs(n - 2 * child) < gap) {
                gap = java.lang.Math.abs(n - 2 * child);
            }
        }

        return gap;
    }

    public static int dfs(int node, List<List<Integer>> graph, boolean[] visited, int[] children) {
        if (visited[node]) {
            return 1;
        }

        visited[node] = true;

        int cnt = 0;

        for (int next : graph.get(node)) {
            cnt += dfs(next, graph, visited, children);

        }

        children[node] = cnt;
        return cnt;
    }
}