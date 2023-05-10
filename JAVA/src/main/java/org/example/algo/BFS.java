package org.example.algo;

import org.example.Graph;
import org.example.Node;

import java.util.ArrayDeque;
import java.util.HashSet;
import java.util.List;

public class BFS extends Algorithm {

    public BFS() {
        this.visited_states = 1;
        this.processed_states = 1;
        this.max_depth_reached = 0;
    }

    @Override
    public Result apply(Node n, String strat) {
        return bfs(n, strat);
    }

    public Result bfs(Node n, String order) {
        if ( Graph.isGoal(n) ) return SUCCESS(n);

        ArrayDeque<Node> dqueue = new ArrayDeque<>();
        HashSet<Node> discovered = new HashSet<>();
        dqueue.addLast(n);
        discovered.add(n);

        while ( !dqueue.isEmpty() ) {
            Node elem = dqueue.pollFirst();

            List<Node> neighbors = Graph.neighbors(elem, order);
            neighbors.removeIf(discovered::contains);

            for (Node neighbor : neighbors) {
                //processing here
                ++processed_states;
                if ( neighbor.path.length() > max_depth_reached ) max_depth_reached = neighbor.path.length();
                if ( Graph.isGoal(neighbor) ) {
                    visited_states += discovered.size();
                    return SUCCESS(neighbor);
                }

                dqueue.addLast(neighbor);
                discovered.add(neighbor);
            }
        }

        return FAILURE();
    }

}
