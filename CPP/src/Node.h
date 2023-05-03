//
// Created by cheily on 02.05.2023.
//

#ifndef CPP_NODE_H
#define CPP_NODE_H

#include <string>
#include "typedefs.h"


struct Node {
public:
    //ctor
    Node(unsigned short size_y, unsigned short size_x, unsigned char ** tab = nullptr);
    Node(std::string path);

    //cpy ctor
    Node(Node &n);
    Node(const Node &n);
    ~Node();

    //operators
    bool operator==(const Node & other) const;

    //fields
    unsigned char** table;
    unsigned char size_y;
    unsigned char size_x;
    unsigned char zero_y;
    unsigned char zero_x;
    std::string path;
};

template <>
struct std::hash<Node> {
    std::size_t operator()(const Node & n) const {
        std::size_t ret = 17;
        for (int y = 0; y < n.size_y; ++y) {
            for (int x = 0; x < n.size_x; ++x) {
                ret = ret * 31 + std::hash<unsigned char>()(n.table[y][x]);
            }
        }

        return ret;
    }
};

template <>
struct std::hash<DETAILS> {

};

std::ostream& operator<<(std::ostream & stream, const Node & n);

#endif //CPP_NODE_H
