//
// Created by igor on 07.05.2023.
//

#ifndef CPP_ASTR_H
#define CPP_ASTR_H
#define SUCCESS(x) {x}
#define FAILURE {}

#include <string>
#include <queue>
#include <unordered_set>
#include "Node.h"
#include "Graph.h"



//TODO imo trzeba dac structa jakiegos na pare
// (w ktorej bedzie node i priority
// [które będzie wynikiem funkcji f
// {która będzie równa dotychczasowy koszt scieżki + heurystyka} ] ) ,
// przeciazyc operator "<" zeby móc powównywać po priority
// i przekazywac ta pare do pq

struct PrioPair{
    PrioPair(int prio, Node &n): priority(prio), node(n) {
    }

    int priority;
    Node node;

    bool operator<(const PrioPair &other) const{
        return priority < other.priority;
    }
};



// ale jak próbowałem to zrobić to XD sie zesrało i to solidnie pozdrawiam
class AStar {
public:
    enum class Heuristic {
        Manhattan,
        Hamming
    };

    static std::optional<Node> astar(Node& n, Heuristic heuristic) {
        std::priority_queue<PrioPair, std::vector<PrioPair>> pq;
        std::unordered_set<Node> set;
        PrioPair pair(0, n);

        //PLACEHOLDER PARA = (node, 0)
        pq.push(pair);


        while (!pq.empty()) {
            Node v = pq.top().node;
            pq.pop();

            if (Graph::isGoal(v)) {
                return SUCCESS(v);
            }

            if (!set.count(v)) {
                set.insert(v);

                for (const auto& n : Graph::neighbors(v, "LRUD")) {
                    if (!set.count(n.value())) {
                        int f = g(n.value()) + h(n.value(), heuristic);
                        PrioPair prioPair(f, &n.value());
                    }
                }
            }
        }

        return FAILURE;
    }

private:
    static int g(const Node& n) {
        return n.path.length();    //I guess????
    }

    static int h(const Node& n, Heuristic heuristic) {
        if (heuristic == Heuristic::Manhattan) {
            return h_manhattan(n);
        } else if (heuristic == Heuristic::Hamming) {
            return h_hamming(n);
        }
    }

    static int h_manhattan(const Node& n) {
        int distance = 0;
        //TODO MANHATAN
        return distance;
    }

    static int h_hamming(const Node& n) {
        int distance = 0;
        //TODO HAMMING
        return distance;
    }
};

#endif //CPP_ASTR_H
