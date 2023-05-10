package org.example.algo;

import org.example.Graph;
import org.example.Node;

import java.util.HashSet;
import java.util.List;
import java.util.Set;

public class DFS extends Algorithm {
    public DFS() {
        this.visited_states = 1;
        this.processed_states = 0;
        this.max_depth_reached = 0;
    }

    private final Set<Node> closed = new HashSet<>();
    public byte MAX_DEPTH = (byte) 21;

    @Override
    public Result apply(Node n, String strat) {
        return dfs(n, strat);
    }

    public Result dfs(Node n, String order) {
        closed.clear();
        return dfs(n, order, (byte) 0);
    }

    public Result dfs(Node n, String order, byte cur_depth) {
        if ( n.path.length() > max_depth_reached ) max_depth_reached = n.path.length();
        ++processed_states;
        if ( Graph.isGoal(n) ) return SUCCESS(n);
        closed.add(n);

        if ( cur_depth >= MAX_DEPTH ) return FAILURE();
        ++cur_depth;

        List<Node> neighbors = Graph.neighbors(n, order);
        neighbors.removeIf(closed::contains);
        visited_states += neighbors.size();

        for (Node neighbor : neighbors) {
            Result result = dfs(neighbor, order, cur_depth);
            if ( result != FAILURE() ) return result;
        }

        return FAILURE();
    }

}
