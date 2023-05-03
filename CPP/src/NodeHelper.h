//
// Created by cheily on 03.05.2023.
//

#ifndef CPP_NODEHELPER_H
#define CPP_NODEHELPER_H

#include <string>
class Node;

class NodeHelper {
public:
    static std::string to_string(const Node& n);
    static std::string to_string(Node& n);
};

#endif //CPP_NODEHELPER_H
