package org.example.algo;

import org.example.Graph;
import org.example.Node;

import java.util.ArrayDeque;
import java.util.HashSet;

public class BFS extends Algorithm {
    public static Node bfs(Node n, String order) {
        return bfs(n, order, 7);
    }

    public static Node bfs(Node n, String order, int max_depth) {
        if ( Graph.isGoal(n) ) return SUCCESS(n);

        ArrayDeque<Node> dqueue = new ArrayDeque<>();
        HashSet<Node> discovered = new HashSet<>();
        dqueue.addLast(n);
        discovered.add(n);

        while ( !dqueue.isEmpty() ) {
            Node elem = dqueue.pollFirst();

            Node[] neighbors = Graph.neighbors(elem, order);
            for (Node neighbor : neighbors) {
                if ( neighbor == null || discovered.contains(neighbor) ) continue;

                if ( Graph.isGoal(neighbor) )
                    return SUCCESS(neighbor);

                dqueue.addLast(neighbor);
                discovered.add(neighbor);
            }
        }

        return FAILURE();
    }

}
