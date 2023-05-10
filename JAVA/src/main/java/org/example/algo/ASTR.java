package org.example.algo;

import org.example.Graph;
import org.example.Node;

import java.util.*;
import java.util.function.Function;

public class ASTR extends Algorithm {

    public ASTR() {
        this.visited_states = 0;
        this.processed_states = 0;
        this.max_depth_reached = 0;
    }
    public Function<Node, Integer> HEURISTIC;

    @Override
    public Result apply(Node n, String strat) {
        if (strat.equals("manh")) HEURISTIC = ASTR::H_MANHATTAN;
        else HEURISTIC = ASTR::H_HAMMING;

        return astr(n);
    }

    public Result astr(Node n) {
        if ( HEURISTIC == null ) throw new IllegalArgumentException("Heuristic cannot be null");

        PriorityQueue<Node> prioQ = new PriorityQueue<>(
                Comparator.comparingInt(o -> cost(o, HEURISTIC))
        );
        Set<Node> closed = new HashSet<>();
        prioQ.add(n);

        while ( !prioQ.isEmpty() ) {
            Node elem = prioQ.poll();
            ++processed_states;
            if ( elem.path.length() > max_depth_reached ) max_depth_reached = elem.path.length();
            if ( Graph.isGoal(elem) ) return SUCCESS(elem);

            if ( closed.contains(elem) ) continue;
            closed.add(elem);

            List<Node> neighbors = Graph.neighbors(elem);
            neighbors.removeIf(closed::contains);
            prioQ.addAll(neighbors);
            visited_states += neighbors.size();

        }

        return FAILURE();
    }

    public static int H_HAMMING(Node n) {
        int distance = 0;
        for (int y = 0; y < n.size_y; y++) {
            for (int x = 0; x < n.size_x; x++) {
                if ( n.table[ y ][ x ] != 0
                        && n.table[ y ][ x ] != Graph.goal.table[ y ][ x ]
                ) distance += 1;
            }
        }
        return distance;
    }

    public static int H_MANHATTAN(Node n) {
        int distance = 0;

        for (int y = 0; y < n.size_y; y++) {
            for (int x = 0; x < n.size_x; x++) {
                if ( n.table[ y ][ x ] != 0 ) {
                    int[] pos = n.find_position(Graph.goal.table[y][x]);
                    distance += Math.abs(pos[0] - y)
                                + Math.abs(pos[1] - x);
                }
            }
        }
        return distance;
    }

    private static int depth(Node n) {
        return n.path.length();
    }

    private static int cost(Node n, Function<Node, Integer> heuristic) {
        return heuristic.apply(n) + depth(n);
    }


}
