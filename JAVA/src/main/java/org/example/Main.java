package org.example;

import org.example.algo.BFS;

import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class Main {
    public static void main(String[] args) {
        if ( args.length != 5 )
            throw new IllegalArgumentException("Wrong call params");

        String algo = args[0];
        String strat = args[1];
        Path in = Path.of(args[2]);
        Path out = Path.of(args[3]);
        Path stats = Path.of(args[4]);

        byte size_y, size_x;
        byte[][] initial_state;

        try ( BufferedReader br = Files.newBufferedReader(in)) {
            String line = br.readLine();
            String[] buffer = line.split(("[\\t ]"));

            size_y = Byte.parseByte(buffer[0], 10);
            size_x = Byte.parseByte(buffer[1], 10);
            initial_state = new byte[size_y][size_x];

            int y = 0;
            while ( (line = br.readLine()) != null ) {
                buffer = line.split("[\\t ]");
                for (int x = 0; x < buffer.length; x++) {
                    initial_state[y][x] = Byte.parseByte(buffer[x], 10);
                }
                ++y;
            }

            Graph.goal = new Node(size_y, size_x);

            System.out.println(Graph.goal);
            System.out.println(Graph.goal.details());

            Node startNode = new Node(size_y, size_x, initial_state);

            System.out.println(startNode);
            System.out.println(startNode.details());
            System.out.println();

            long t_0 = System.currentTimeMillis();
            System.out.println(BFS.bfs(startNode, strat).details());
            long t_f =  System.currentTimeMillis();
            System.out.println("Time: " + ((t_f - t_0) / 1000) + " sec (" + (t_f - t_0) + " ms)");

        } catch (IOException e) {
            throw new RuntimeException(e);
        }

//        Node n = new Node((byte) 4, (byte) 4);
//        System.out.println(n);
//        System.out.println(n.details());
//
//        System.out.println(Graph.L(n));
//        System.out.println(Graph.R(n).details());
//        System.out.println(Graph.U(n));
//        System.out.println(Graph.D(n).details());

    }
}