import java.util.*;

class Node {
    int id;
    int x;
    int y;
    Node left;
    Node right;

    public Node(int id, int x, int y) {
        this.id = id;
        this.x = x;
        this.y = y;
    }
}

class Solution {

    public int[][] solution(int[][] nodeinfo) {
        int n = nodeinfo.length;

        List<Node> nodes = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            nodes.add(new Node(i + 1, nodeinfo[i][0], nodeinfo[i][1]));
        }

        nodes.sort(Comparator.comparingInt(node -> node.x));

        Node root = buildTree(nodes, 0, n - 1);

        List<Integer> preorderList = new ArrayList<>();
        List<Integer> postorderList = new ArrayList<>();
        search(root, preorderList, postorderList);

        int[][] answer = new int[2][n];
        for (int i = 0; i < n; i++) {
            answer[0][i] = preorderList.get(i);
            answer[1][i] = postorderList.get(i);
        }

        return answer;
    }

    private Node buildTree(List<Node> nodes, int left, int right) {
        if (left > right) {
            return null;
        }

        int maxYIndex = left;
        for (int i = left + 1; i <= right; i++) {
            if (nodes.get(i).y > nodes.get(maxYIndex).y) {
                maxYIndex = i;
            }
        }

        Node root = nodes.get(maxYIndex);

        root.left = buildTree(nodes, left, maxYIndex - 1);
        root.right = buildTree(nodes, maxYIndex + 1, right);

        return root;
    }

    private void search(Node node, List<Integer> preOrder, List<Integer> postOrder) {
        if (node != null) {
            preOrder.add(node.id);
            search(node.left, preOrder, postOrder);
            search(node.right, preOrder, postOrder);
            postOrder.add(node.id);
        }
    }

}