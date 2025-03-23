#ifndef SET_ELEMENT_H
#define SET_ELEMENT_H

#include <string>
#include <vector>

class SetElement {
public:
    bool isAtomic; // true, ���� ��� ��������� �������, false, ���� ���������
    std::string value; // ��������, ���� ��������� �������
    std::vector<SetElement> subset; // ������������, ���� ��� ���������

    SetElement(std::string val) : isAtomic(true), value(val) {}
    SetElement(std::vector<SetElement> elements) : isAtomic(false), subset(elements) {}

    std::string toString() const {
        if (isAtomic) return value;
        std::string result = "{";
        for (size_t i = 0; i < subset.size(); ++i) {
            result += subset[i].toString();
            if (i < subset.size() - 1) result += ",";
        }
        result += "}";
        return result;
    } // ��� ������ ��������
};

#endif