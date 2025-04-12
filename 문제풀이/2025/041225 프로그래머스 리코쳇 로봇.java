// https://school.programmers.co.kr/learn/courses/30/lessons/169199

import java.util.*;

enum Cell {
    Empty,
    Block,
    Goal
}

class Point {
    int x;
    int y;

    public Point(int x, int y) {
        this.x = x;
        this.y = y;
    }
}

class Tuple<A, B> {
    A first;
    B second;

    public Tuple(A first, B second) {
        this.first = first;
        this.second = second;
    }
}

class Solution {
    public int solution(String[] board) {
        int n = board.length;
        int m = board[0].length();

        List<List<Cell>> map = new ArrayList<>();

        Point start = null;

        for (int i = 0; i < board.length; i++) {
            String line = board[i];
            List<Cell> mapLine = new ArrayList<>();

            for (int j = 0; j < line.length(); j++) {
                char c = line.charAt(j);

                switch (c) {
                    case 'R':
                        start = new Point(i, j);
                        mapLine.add(Cell.Empty);
                        break;
                    case 'D':
                        mapLine.add(Cell.Block);
                        break;
                    case '.':
                        mapLine.add(Cell.Empty);
                        break;
                    case 'G':
                        mapLine.add(Cell.Goal);
                        break;
                    default:
                        throw new IllegalArgumentException();
                }
            }
            map.add(mapLine);
        }

        int[] dr = { 0, 0, 1, -1 };
        int[] dc = { 1, -1, 0, 0 };

        Queue<Tuple<Integer, Integer>> queue = new LinkedList();
        queue.add(new Tuple(start.x, start.y));

        int[][] visited = new int[n][m];
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                visited[i][j] = 1_000_007;
            }
        }
        visited[start.x][start.y] = 0;

        while (!queue.isEmpty()) {
            Tuple<Integer, Integer> point = queue.poll();
            int r = point.first;
            int c = point.second;

            for (int d = 0; d < 4; d++) {
                int nr = r;
                int nc = c;

                while (true) {
                    nr += dr[d];
                    nc += dc[d];

                    if (nr < 0 || nc < 0 || n <= nr || m <= nc || map.get(nr).get(nc).equals(Cell.Block)) {
                        nr -= dr[d];
                        nc -= dc[d];
                        break;
                    }
                }

                if (visited[r][c] + 1 < visited[nr][nc]) {
                    visited[nr][nc] = visited[r][c] + 1;
                    queue.add(new Tuple(nr, nc));

                    if (map.get(nr).get(nc).equals(Cell.Goal)) {
                        return visited[nr][nc];
                    }
                }

            }

        }

        return -1;
    }
}