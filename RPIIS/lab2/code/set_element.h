#ifndef SET_ELEMENT_H
#define SET_ELEMENT_H

#include <string>
#include <vector>

class SetElement {
public:
    bool isAtomic; // true, если это атомарный элемент, false, если множество
    std::string value; // значение, если атомарный элемент
    std::vector<SetElement> subset; // подмножество, если это множество

    SetElement(std::string val) : isAtomic(true), value(val) {}
    SetElement(std::vector<SetElement> elements) : isAtomic(false), subset(elements) {}

    std::string toString() const; // для вывода элемента
};

#endif