package org.example.algo;

import org.example.Node;

//
public class Result {
    public static Result FAILURE = new Result(-1);
    public int solution_length;
    public Node node;
    public String solution_path;
    public int visited_states;
    public int processed_states;
    public int max_depth;
    public float time;

    public Result(int solution_length, Node node, String solution_path, int visited_states, int processed_states, int max_depth, float time) {
        this.solution_length = solution_length;
        this.node = node;
        this.solution_path = solution_path;
        this.visited_states = visited_states;
        this.processed_states = processed_states;
        this.max_depth = max_depth;
        this.time = time;
    }

    public Result(Node node) {
        this.node = node;
    }

    private Result(int solution_length) {
        this.solution_length = solution_length;
    }

    public Result(Result other) {
        this.solution_length = other.solution_length;
        this.node = other.node;
        this.solution_path = other.solution_path;
        this.visited_states = other.visited_states;
        this.processed_states = other.processed_states;
        this.max_depth = other.max_depth;
        this.time = other.time;
    }

    @Override
    public String toString() {
        return "Result{" +
                "\nsolution_length=" + solution_length +
                "\nnode=" + node.details() +
                "\nsolution_path='" + solution_path + '\'' +
                "\nvisited_states=" + visited_states +
                "\nprocessed_states=" + processed_states +
                "\nmax_depth=" + max_depth +
                "\ntime=" + time +
                "\n}";
    }

    public String solution() {
        return String.valueOf(solution_length)
                + '\n' + solution_path;
    }

    public String stats() {
        return String.valueOf(solution_length)
                + '\n' + visited_states
                + '\n' + processed_states
                + '\n' + max_depth
                + '\n' + String.valueOf(time).formatted("%.3f");
    }
}