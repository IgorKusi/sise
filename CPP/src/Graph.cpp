//
// Created by cheily on 03.05.2023.
//
#include "Graph.h"


Node * Graph::goal = nullptr;

bool Graph::
isGoal(const Node & n) {
    for (int y = 0; y < n.size_y; ++y) {
        for (int x = 0; x < n.size_x; ++x) {
            if (n.table[y][x] != goal->table[y][x]) return false;
        }
    }
    return true;
}

std::array< std::optional<Node>, 4 > Graph::
neighbors(Node n, std::string order) {
    std::array< std::optional<Node>, 4 > ret;
    for (int i = 0; i < order.length(); i++) {
        if (order[i] == 'L') ret[i] = L(n);
        else if (order[i] == 'R') ret[i] = R(n);
        else if (order[i] == 'U') ret[i] = U(n);
        else if (order[i] == 'D') ret[i] = D(n);
    }

    return ret;
}

std::optional<Node> Graph::
L(Node n) {
    if (n.zero_x == 0) return {};
    Node ret(n);

    unsigned char temp = ret.table[ret.zero_y][ret.zero_x - 1];
    ret.table[ret.zero_y][ret.zero_x - 1] = 0;
    ret.table[ret.zero_y][ret.zero_x] = temp;

    ret.zero_x--;
    ret.path += 'L';

    return {ret};
}

std::optional<Node> Graph::
R(Node n) {
    if (n.zero_x == n.size_x - 1) return {};
    Node ret(n);

    unsigned char temp = ret.table[ret.zero_y][ret.zero_x + 1];
    ret.table[ret.zero_y][ret.zero_x + 1] = 0;
    ret.table[ret.zero_y][ret.zero_x] = temp;

    ret.zero_x++;
    ret.path += 'R';

    return {ret};
}

std::optional<Node> Graph::
U(Node n) {
    if (n.zero_y == 0) return {};
    Node ret(n);

    unsigned char temp = ret.table[ret.zero_y - 1][ret.zero_x];
    ret.table[ret.zero_y - 1][ret.zero_x] = 0;
    ret.table[ret.zero_y][ret.zero_x] = temp;

    ret.zero_y--;
    ret.path += 'U';

    return {ret};
}

std::optional<Node> Graph::
D(Node n) {
    if (n.zero_y == n.size_y - 1) return {};
    Node ret(n);

    unsigned char temp = ret.table[ret.zero_y + 1][ret.zero_x];
    ret.table[ret.zero_y + 1][ret.zero_x] = 0;
    ret.table[ret.zero_y][ret.zero_x] = temp;

    ret.zero_y++;
    ret.path += 'D';

    return {ret};
}

