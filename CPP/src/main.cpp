#include <iostream>
#include "tclap/CmdLine.h"
#include "Node.h"
#include "Graph.h"
#include "BFS.h"
#include <map>
#include <fstream>

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
        cout << buffer << endl;

    } catch (const exception & ignored) {
    }



    Node n(4, 4);
    Graph::goal = &n;

//    cout << NodeHelper::to_string(n) <<endl <<endl;
//    std::string direc;
//
//    Node rotated = Graph::U(Graph::L(Graph::D(Graph::R(n))));
//    cout << NodeHelper::to_string(rotated) << endl << direc;

    cout << BFS::bfs(4, 4, "LRUD").value();


    return 0;
}
