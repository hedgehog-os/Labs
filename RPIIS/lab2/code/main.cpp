#include "set_parser.h"
#include "cartesian_product.h"
#include <iostream>
#include <fstream>

int main() {
    std::ifstream file("sets.txt");
    if (!file.is_open()) {
        std::cout << "Не удалось открыть файл\n";
        return 1;
    }

    std::vector<std::vector<SetElement>> sets;
    std::string line;
    while (std::getline(file, line)) {
        sets.push_back(parseSet(line));
    }
    file.close();

    auto product = cartesianProduct(sets);
    for (const auto& tuple : product) {
        std::cout << "(";
        for (size_t i = 0; i < tuple.size(); ++i) {
            std::cout << tuple[i].toString();
            if (i < tuple.size() - 1) std::cout << ",";
        }
        std::cout << ")\n";
    }

    return 0;
}