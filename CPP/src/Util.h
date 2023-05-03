//
// Created by cheily on 04.05.2023.
//

#ifndef CPP_UTIL_H
#define CPP_UTIL_H


#include <string>
#include <vector>

class Util {
public:
    static std::vector<std::string> split(const std::string &s, char delim);
    static std::vector<std::string> split(std::string s, std::string delimiter);
};


#endif //CPP_UTIL_H
