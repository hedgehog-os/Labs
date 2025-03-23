#include "cartesian_product.h"

std::vector<std::vector<SetElement>> cartesianProduct(const std::vector<std::vector<SetElement>>& sets) {
    std::vector<std::vector<SetElement>> result;

    // ���� ������� ������ ����, ���������� ������ ���������
    if (sets.empty()) return result;

    // ���� ���� ���� �� ���� ������ ���������, ��������� ����
    for (const auto& set : sets) {
        if (set.empty()) return result;
    }

    // �������������� ��������� ������ ����������
    result.reserve(sets[0].size()); // ����������� ����� ��� �����������
    for (const auto& element : sets[0]) {
        result.push_back({ element });
    }

    // ������ ��������� ������������ ��� ��������� ��������
    for (size_t i = 1; i < sets.size(); ++i) {
        std::vector<std::vector<SetElement>> newResult;
        newResult.reserve(result.size() * sets[i].size()); // �����������
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