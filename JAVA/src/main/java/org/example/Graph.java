package org.example;

import java.util.Optional;

public class Graph {
    public static Node goal;

    public static boolean isGoal(Node n) {
        return goal.equals(n);
    }

    public static Node[] neighbors(Node n, String order) {
        Node[] ret = new Node[4];

        for (int i = 0; i < order.length(); i++) {
            if (order.charAt(i) == 'L') ret[i] = L(n);
            else if (order.charAt(i) == 'R') ret[i] = R(n);
            else if (order.charAt(i) == 'U') ret[i] = U(n);
            else if (order.charAt(i) == 'D') ret[i] = D(n);
        }

        return ret;
    }

    public static Node L(Node n) {
        if (n.zero_x == 0) return null;
        Node ret = new Node(n);

        var temp = ret.table[ret.zero_y][ret.zero_x - 1];
        ret.table[ret.zero_y][ret.zero_x - 1] = 0;
        ret.table[ret.zero_y][ret.zero_x] = temp;

        ret.zero_x--;
        ret.path += 'L';

        return ret;
    }

    public static Node R(Node n) {
        if (n.zero_x == n.size_x - 1) return null;
        Node ret = new Node(n);

        var temp = ret.table[ret.zero_y][ret.zero_x + 1];
        ret.table[ret.zero_y][ret.zero_x + 1] = 0;
        ret.table[ret.zero_y][ret.zero_x] = temp;

        ret.zero_x++;
        ret.path += 'R';

        return ret;
    }

    public static Node U(Node n) {
        if (n.zero_y == 0) return null;
        Node ret = new Node(n);

        var temp = ret.table[ret.zero_y - 1][ret.zero_x];
        ret.table[ret.zero_y - 1][ret.zero_x] = 0;
        ret.table[ret.zero_y][ret.zero_x] = temp;

        ret.zero_y--;
        ret.path += 'U';

        return ret;
    }

    public static Node D(Node n) {
        if (n.zero_y == n.size_y - 1) return null;
        Node ret = new Node(n);

        var temp = ret.table[ret.zero_y + 1][ret.zero_x];
        ret.table[ret.zero_y + 1][ret.zero_x] = 0;
        ret.table[ret.zero_y][ret.zero_x] = temp;

        ret.zero_y++;
        ret.path += 'D';

        return ret;
    }


}
