#include "cartesian_product.h"

std::vector<std::vector<SetElement>> cartesianProduct(const std::vector<std::vector<SetElement>>& sets) {
    std::vector<std::vector<SetElement>> result;

    // Если входной вектор пуст, возвращаем пустой результат
    if (sets.empty()) return result;

    // Если есть хотя бы одно пустое множество, результат пуст
    for (const auto& set : sets) {
        if (set.empty()) return result;
    }

    // Инициализируем результат первым множеством
    result.reserve(sets[0].size()); // Резервируем место для оптимизации
    for (const auto& element : sets[0]) {
        result.push_back({ element });
    }

    // Строим декартово произведение для остальных множеств
    for (size_t i = 1; i < sets.size(); ++i) {
        std::vector<std::vector<SetElement>> newResult;
        newResult.reserve(result.size() * sets[i].size()); // Оптимизация
        for (const auto& current : result) {
            for (const auto& element : sets[i]) {
                std::vector<SetElement> tuple = current;
                tuple.push_back(element);
                newResult.push_back(std::move(tuple));
            }
        }
        result = std::move(newResult);
    }

    return result;
}