//
// Created by cheily on 02.05.2023.
//

#ifndef CPP_GRAPH_H
#define CPP_GRAPH_H

#include <iostream>
#include <optional>
#include "Node.h"
#include "Solutions.h"

class Graph {
public:
    static Node * goal;

    static bool isGoal(const Node & n);

    static std::array< std::optional<Node>, 4 > neighbors(Node n, std::string order);

    static std::optional<Node> L(Node n);
    static std::optional<Node> R(Node n);
    static std::optional<Node> U(Node n);
    static std::optional<Node> D(Node n);


};

#endif //CPP_GRAPH_H
