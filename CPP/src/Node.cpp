//
// Created by cheily on 03.05.2023.
//
#include <fstream>
#include "Node.h"
#include "NodeHelper.h"

Node::
Node(unsigned short size_y, unsigned short size_x, unsigned char ** tab) : size_y(size_y), size_x(size_x) {
    if (tab != nullptr) {
        table = tab;
        return;
    }

    table = new unsigned char*[size_y];
    for (int y = 0; y < size_y; ++y) {
        table[y] = new unsigned char[size_x];

        for (int x = 0; x < size_x; ++x) {
            table[y][x] = y * size_x + x + 1 == size_x * size_y ? 0 : y * size_x + x + 1;
        }
    }
    zero_y = 0;
    zero_x = 0;
}

Node::
Node(std::string path) {
    std::ifstream ifstream(path);
    std::string buffer;
    bool first_line = true;

    unsigned char size_y = 0, size_x = 0;
    unsigned char ** tab;

    while (std::getline(ifstream, buffer)) {
        if (first_line) {

        }
    }

}

Node::
Node(Node &n) : size_y(n.size_y), size_x(n.size_x), zero_y(n.zero_y), zero_x(n.zero_x), path(n.path) {
    table = new unsigned char*[size_y];
    for (int y = 0; y < size_y; ++y) {
        table[y] = new unsigned char[size_x];

        for (int x = 0; x < size_x; ++x) {
            table[y][x] = n.table[y][x];
        }
    }
}

Node::
Node(const Node &n) : size_y(n.size_y), size_x(n.size_x), zero_y(n.zero_y), zero_x(n.zero_x), path(n.path) {
    table = new unsigned char*[size_y];
    for (int y = 0; y < size_y; ++y) {
        table[y] = new unsigned char[size_x];

        for (int x = 0; x < size_x; ++x) {
            table[y][x] = n.table[y][x];
        }
    }
}

Node::
~Node() {
    for (int i = 0; i < size_y; ++i) {
        delete [] table[i];
    }
    delete [] table;
}

bool Node::
operator==(const Node & other) const {
    for (int y = 0; y < this->size_y; ++y) {
        for (int x = 0; x < this->size_x; ++x) {
            if (this->table[y][x] != other.table[y][x]) return false;
        }
    }
    return true;
}

bool Node::operator<(const Node &other) const {
    //TODO STL ty kurwo jebana
    return !operator==(other);
}

std::ostream &
operator<<(std::ostream & stream, const Node & n) {
    stream << NodeHelper::to_string(n);
    return stream;
}
