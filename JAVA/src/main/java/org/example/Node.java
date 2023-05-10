package org.example;

import java.util.Arrays;

public class Node {
    public byte[][] table;
    public byte size_y;
    public byte size_x;
    public byte zero_y;
    public byte zero_x;
    public String path;

    public Node(Node other) {
        size_y = other.size_y;
        size_x = other.size_x;
        zero_y = other.zero_y;
        zero_x = other.zero_x;
        path = other.path;

        table = new byte[size_y][size_x];
        for (int y = 0; y < size_y; y++) {
            for (int x = 0; x < size_x; x++) {
                table[y][x] = other.table[y][x];
            }
        }

    }

    public Node(byte size_y, byte size_x) {
        this.size_y = size_y;
        this.size_x = size_x;
        this.zero_y = 3;
        this.zero_x = 3;
        byte[][] tab = new byte[size_y][size_x];

        for (int y = 0; y < size_y; y++) {
            for (int x = 0; x < size_x; x++) {
                tab[y][x] = (byte) (y * size_x + x + 1 == size_x * size_y ? 0 : y * size_x + x + 1);
            }
        }
        this.table = tab;
        path = "";
    }

    public Node(byte size_y, byte size_x, byte[][] initial_state) {
        this.size_y = size_y;
        this.size_x = size_x;
        this.path = "";
        this.table = initial_state;
        for (int y = 0; y < initial_state.length; y++)
            for (int x = 0; x < initial_state[ y ].length; x++)
                if ( initial_state[ y ][ x ] == 0 ) {
                    this.zero_y = (byte) y;
                    this.zero_x = (byte) x;
                    return;
                }

        throw new IllegalArgumentException("No zero cell in initial state");
    }

    @Override
    public boolean equals(Object o) {
        if ( this == o ) return true;
        if ( o == null || getClass() != o.getClass() ) return false;
        Node node = (Node) o;
        return Arrays.deepEquals(table, node.table);
    }

    @Override
    public int hashCode() {
        return Arrays.deepHashCode(table);
    }

    @Override
    public String toString() {
        StringBuilder ret = new StringBuilder(table.length);
        for (int y = 0; y < table.length; y++) {
            for (int x = 0; x < table[ 0 ].length; x++) {
                ret.append(table[y][x]).append(' ');
            }
            ret.append('\n');
        }

        return ret.toString().trim();
    }


    public String details() {
        return "Node{" +
                "table=" + Arrays.deepToString(table) +
                ", size_y=" + size_y +
                ", size_x=" + size_x +
                ", zero_y=" + zero_y +
                ", zero_x=" + zero_x +
                ", path='" + path + '\'' +
                ", hash=" + hashCode() +
                '}';
    }

    /**
     * @param cell_value to find
     * @return [y, x]
     */
    public int[] find_position(int cell_value) {
        for (int y = 0; y < size_y; y++) {
            for (int x = 0; x < size_x; x++) {
                if (table[y][x] == cell_value) return new int[]{y, x};
            }
        }
        return new int[]{-1, -1};
    }

}
