#include "cartesian_product.h"

void cartesianHelper(const std::vector<std::vector<SetElement>>& sets,
    std::vector<SetElement>& currentTuple,
    std::vector<std::vector<SetElement>>& result,
    size_t index) {
    if (index == sets.size()) {
        result.push_back(currentTuple);
        return;
    }
    for (const auto& element : sets[index]) {
        currentTuple.push_back(element);
        cartesianHelper(sets, currentTuple, result, index + 1);
        currentTuple.pop_back();
    }
}

std::vector<std::vector<SetElement>> cartesianProduct(const std::vector<std::vector<SetElement>>& sets) {
    std::vector<std::vector<SetElement>> result;
    std::vector<SetElement> currentTuple;
    cartesianHelper(sets, currentTuple, result, 0);
    return result;
}