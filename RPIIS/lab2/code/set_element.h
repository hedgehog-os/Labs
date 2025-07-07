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

    std::string toString() const; // ��� ������ ��������
};

#endif