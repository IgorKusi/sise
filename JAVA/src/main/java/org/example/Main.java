package org.example;

import org.example.algo.*;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class Main {
    public static void main(String[] args) {
        if ( args.length != 5 )
            throw new IllegalArgumentException("Wrong call params");

        String algo = args[ 0 ];
        String strat = args[ 1 ];
        Path in = Path.of(args[ 2 ]);
        Path out = Path.of(args[ 3 ]);
        Path stats = Path.of(args[ 4 ]);

        byte size_y, size_x;
        byte[][] initial_state;

        try ( BufferedReader br = Files.newBufferedReader(in) ) {
            String line = br.readLine();
            String[] buffer = line.split(("[\\t ]"));

            size_y = Byte.parseByte(buffer[ 0 ], 10);
            size_x = Byte.parseByte(buffer[ 1 ], 10);
            initial_state = new byte[ size_y ][ size_x ];

            int y = 0;
            while ( (line = br.readLine()) != null ) {
                buffer = line.split("[\\t ]");
                for (int x = 0; x < buffer.length; x++) {
                    initial_state[ y ][ x ] = Byte.parseByte(buffer[ x ], 10);
                }
                ++y;
            }

        } catch (IOException e) {
            throw new RuntimeException(e);
        }


        Graph.goal = new Node(size_y, size_x);

        Node startNode = new Node(size_y, size_x, initial_state);

        Algorithm alg = switch (algo) {
            case "bfs" -> new BFS();
            case "dfs" -> new DFS();
            case "astr" -> new ASTR();
            default -> throw new IllegalArgumentException("No such algorithm");
        };

        Result result = alg.measure(startNode, strat);

        try ( BufferedWriter bw = Files.newBufferedWriter(out) ) {
            bw.write(result.solution());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        try ( BufferedWriter bw = Files.newBufferedWriter(stats) ) {
            bw.write(result.stats());
        } catch (IOException e) {
            throw new RuntimeException(e);
        }


    }
}