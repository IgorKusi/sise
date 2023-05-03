//
// Created by cheily on 03.05.2023.
//

#ifndef CPP_TYPEDEFS_H
#define CPP_TYPEDEFS_H

#include <functional>
class Node;

using OPERATOR = std::function<Node( Node )>;
using DETAILS = std::tuple<Node, OPERATOR>;
using SOLUTION_MAP = std::unordered_map< Node, DETAILS >;

#endif //CPP_TYPEDEFS_H
