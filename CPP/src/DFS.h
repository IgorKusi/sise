//
// Created by igor on 05.05.2023.
//

#ifndef CPP_DFS_H
#define CPP_DFS_H
#define SUCCESS(x) {x}
#define FAILURE {}

#include <string>
#include <deque>
#include <stack>
#include <unordered_set>
#include "Node.h"
#include "Graph.h"

class DFS {
public:
    static std::optional<Node> dfs(Node &n, const std::string &order, unsigned short max_depth = 7) {
        if (Graph::isGoal(n)) return SUCCESS(n);
        std::stack<Node> st;
        std::unordered_set<Node> set;
        st.push(n);
        set.insert(n);

        while (!st.empty()) {
            Node elem = st.top();
            st.pop();

            if (!set.count(elem)) {
                set.insert(elem);
            }

            std::array<std::optional<Node>, 4> neighbors = Graph::neighbors(elem, order);
            for (auto it = neighbors.rbegin(); it != neighbors.rend(); ++it) {
                auto neighbor = *it;
                if (!neighbor.has_value()) continue;

                if (!set.count(neighbor.value())) {

                    std::cout << neighbor->path << std::endl;
                    if (Graph::isGoal(neighbor.value()))
                        return SUCCESS(neighbor);

                    st.push(neighbor.value());
                    set.insert(neighbor.value());
                }
            }
        }

        return FAILURE;
    }
};
#endif //CPP_DFS_H
