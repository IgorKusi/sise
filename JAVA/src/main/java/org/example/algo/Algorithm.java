package org.example.algo;

import org.example.Node;

public abstract class Algorithm {
    public static Node SUCCESS(Node n) {
        return n;
    }

    public static Node FAILURE() {
        return null;
    }
}
