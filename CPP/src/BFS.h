//
// Created by cheily on 02.05.2023.
//

#ifndef CPP_BFS_H
#define CPP_BFS_H
#define SUCCESS(x) {x}
#define FAILURE {}

#include <string>
#include <deque>
#include <unordered_set>
#include "Node.h"
#include "Graph.h"

class BFS {
public:
    static std::optional<Node> bfs(unsigned short size_y, unsigned short size_x, const std::string &order, unsigned short max_depth = 7) {
        Node n(size_y, size_x);
        if (Graph::isGoal(n)) return SUCCESS(n);

        std::deque<Node> dq;
        std::unordered_set<Node> set;
        dq.push_back(n);
        set.insert(n);

        while (!dq.empty()) {
            Node elem = dq.back();
            dq.pop_back();

            std::array<std::optional<Node>, 4> neighbors = Graph::neighbors(elem, order);
            for (auto neighbor: neighbors) {
                if (!neighbor.has_value()) continue;

                if (!set.count(neighbor.value())) {
                    if (Graph::isGoal(neighbor.value()))
                        return SUCCESS(neighbor);

                    dq.push_back(neighbor.value());
                    set.insert(neighbor.value());

                }
            }

        }

        return FAILURE;
    }


};

#endif //CPP_BFS_H