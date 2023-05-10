package org.example.algo;

import org.example.Node;

public abstract class Algorithm {
    protected int visited_states;
    protected int processed_states;
    protected int max_depth_reached;

    public static Result SUCCESS(Node n) {
        return new Result(n);
    }

    public static Result FAILURE() {
        return Result.FAILURE;
    }

    public abstract Result apply(Node n, String strat);

    public Result measure(Node n, String strat) {
        long t_0 = System.nanoTime();
        Result result = apply(n, strat);
        long t_f = System.nanoTime();

        result.time = ((t_f - t_0) / 1_000_000f);
        if ( result == FAILURE() ) {
            //copy the static variable
            result = new Result(result);
        } else {
            result.solution_length = result.node.path.length();
            result.solution_path = result.node.path;
        }
        result.max_depth = max_depth_reached;
        result.visited_states = visited_states;
        result.processed_states = processed_states;

        return result;
    }
}
