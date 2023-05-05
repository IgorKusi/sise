cmake_minimum_required(VERSION 3.24)
project(CPP)

set(CMAKE_CXX_STANDARD 17)

include_directories(src)
include_directories(tclap-1.4.0-rc1/include)
add_executable(CPP src/main.cpp src/Node.h src/Solutions.h src/BFS.h src/Graph.cpp src/Graph.h src/NodeHelper.cpp src/Solutions.cpp src/typedefs.h src/Node.cpp src/Util.cpp src/Util.h src/DFS.h)
