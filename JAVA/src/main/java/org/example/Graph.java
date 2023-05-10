package org.example;

import java.util.ArrayList;
import java.util.List;

public class Graph {
    private static final String default_order = "LRUD";
    public static Node goal;

    public static boolean isGoal(Node n) {
        return goal.equals(n);
    }

    public static List<Node> neighbors(Node n) {
        return neighbors(n, default_order);
    }

    public static List<Node> neighbors(Node n, String order) {
        List<Node> ret = new ArrayList<>(4);

        for (int i = 0; i < order.length(); i++) {
            Node elem = null;

            if ( order.charAt(i) == 'L' ) elem = L(n);
            else if ( order.charAt(i) == 'R' ) elem = R(n);
            else if ( order.charAt(i) == 'U' ) elem = U(n);
            else if ( order.charAt(i) == 'D' ) elem = D(n);

            if ( elem != null ) ret.add(elem);
        }

        return ret;
    }

    public static Node L(Node n) {
        if ( n.zero_x == 0 ) return null;
        Node ret = new Node(n);

        var temp = ret.table[ ret.zero_y ][ ret.zero_x - 1 ];
        ret.table[ ret.zero_y ][ ret.zero_x - 1 ] = 0;
        ret.table[ ret.zero_y ][ ret.zero_x ] = temp;

        ret.zero_x--;
        ret.path += 'L';

        return ret;
    }

    public static Node R(Node n) {
        if ( n.zero_x == n.size_x - 1 ) return null;
        Node ret = new Node(n);

        var temp = ret.table[ ret.zero_y ][ ret.zero_x + 1 ];
        ret.table[ ret.zero_y ][ ret.zero_x + 1 ] = 0;
        ret.table[ ret.zero_y ][ ret.zero_x ] = temp;

        ret.zero_x++;
        ret.path += 'R';

        return ret;
    }

    public static Node U(Node n) {
        if ( n.zero_y == 0 ) return null;
        Node ret = new Node(n);

        var temp = ret.table[ ret.zero_y - 1 ][ ret.zero_x ];
        ret.table[ ret.zero_y - 1 ][ ret.zero_x ] = 0;
        ret.table[ ret.zero_y ][ ret.zero_x ] = temp;

        ret.zero_y--;
        ret.path += 'U';

        return ret;
    }

    public static Node D(Node n) {
        if ( n.zero_y == n.size_y - 1 ) return null;
        Node ret = new Node(n);

        var temp = ret.table[ ret.zero_y + 1 ][ ret.zero_x ];
        ret.table[ ret.zero_y + 1 ][ ret.zero_x ] = 0;
        ret.table[ ret.zero_y ][ ret.zero_x ] = temp;

        ret.zero_y++;
        ret.path += 'D';

        return ret;
    }

    public static Node reverse(Node n, char operator) {
        if ( operator == 'D' ) return U(n);
        if ( operator == 'U' ) return D(n);
        if ( operator == 'L' ) return R(n);
        if ( operator == 'R' ) return L(n);
        return null;
    }


}
