#include <iostream>
#include "tclap/CmdLine.h"
#include "Node.h"
#include "Graph.h"
#include "BFS.h"
#include "Util.h"
#include <map>
#include <fstream>
#include <chrono>

using std::chrono::high_resolution_clock;
using std::chrono::duration_cast;
using std::chrono::duration;
using std::chrono::seconds;
using std::chrono::milliseconds;
using namespace std;

int main(int argc, char * argv[]) {
    try {
        TCLAP::CmdLine cmd("Args");
        TCLAP::UnlabeledValueArg<string> algo("algorithm", "", true, "", "string");
        TCLAP::UnlabeledValueArg<string> strat("strategy", "", true, "", "string");
        TCLAP::UnlabeledMultiArg<string> paths("paths", "", true, "string");

        cmd.add(algo);
        cmd.add(strat);
        cmd.add(paths);

        cmd.parse(argc, argv);


        cout << algo.getValue() << endl << strat.getValue() << endl << paths.getValue().at(0) << endl << paths.getValue().at(1) << endl << paths.getValue().at(2) << endl;

        string buffer;
        ifstream ifstr(paths.getValue()[0]);
        getline(ifstr, buffer);

        vector<string> spl = Util::split(buffer, '\t');
        for (auto & str : spl)
            cout << str << '\t';

        int size_y = stoi(spl[0]);
        int size_x = stoi(spl[1]);
        cout << size_y << endl << size_x << endl;
        auto ** initial_state = new unsigned char * [size_y];

        int y = 0;
        while( getline(ifstr, buffer) ) {
            initial_state[y] = new unsigned char[size_x];
            spl.clear();
            spl = Util::split(buffer, '\t');

            for (int x = 0; x < spl.size(); ++x) {
                initial_state[y][x] = stoi(spl[x]);
            }

            y++;
        }


        for (int y = 0; y < size_y; ++y) {
            for (int x = 0; x < size_x; ++x) {
                cout << (int) initial_state[y][x] << '\t';
            }
            cout << endl;
        }

        Graph::goal = new Node(size_y, size_x);
        optional<Node> solved;

        Node a(size_y, size_x, initial_state);
        cout << "GOAL:\n" << *Graph::goal << endl;
        cout << "INITIAL STATE:\n" << a << endl;

//        cout << Graph::L(a).value();
////        cout << Graph::R(a).value();
//        cout << Graph::U(a).value();
//        cout << Graph::D(a).value();

        auto t_0 = high_resolution_clock::now();
        solved = BFS::bfs(a, strat.getValue());
        auto t_f = high_resolution_clock::now();
        cout << "SOLVED:\n" << solved.value() << endl;
        cout << "PATH:\t" << solved->path << endl;
        cout << "TIME: " << duration_cast<seconds>(t_f - t_0).count() << " sec (" << duration_cast<milliseconds>(t_f - t_0).count() << " ms)";


        delete Graph::goal;

    } catch (const exception & ignored) {
    }



//    Node n(4, 4);
//    Graph::goal = &n;
//
////    cout << NodeHelper::to_string(n) <<endl <<endl;
////    std::string direc;
////
////    Node rotated = Graph::U(Graph::L(Graph::D(Graph::R(n))));
////    cout << NodeHelper::to_string(rotated) << endl << direc;
//
//    cout << BFS::bfs(4, 4, "LRUD").value();


    return 0;
}
