//
// Created by cheily on 03.05.2023.
//

#include "Node.h"
#include "NodeHelper.h"

std::string NodeHelper::to_string(const Node &n) {
    std::string ret;
    for (int y = 0; y < n.size_y; ++y) {
        for (int x = 0; x < n.size_x; ++x) {
            ret += std::to_string((unsigned short) n.table[y][x]);
            ret += ' ';
        }
        ret += '\n';
    }

    return ret;
}

std::string NodeHelper::to_string(Node &n) {
    std::string ret;
    for (int y = 0; y < n.size_y; ++y) {
        for (int x = 0; x < n.size_x; ++x) {
            ret += std::to_string((unsigned short) n.table[y][x]);
            ret += ' ';
        }
        ret += '\n';
    }

    return ret;
}