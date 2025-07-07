#include "set_parser.h"
#include <stack>

std::string SetElement::toString() const {
    if (isAtomic) return value;
    std::string result = "{";
    for (size_t i = 0; i < subset.size(); ++i) {
        result += subset[i].toString();
        if (i < subset.size() - 1) result += ",";
    }
    result += "}";
    return result;
}

std::vector<SetElement> parseSet(const std::string& input) {
    std::stack<std::vector<SetElement>> stack;
    std::vector<SetElement> currentSet;
    std::string buffer;

    for (size_t i = 0; i < input.length(); ++i) {
        char c = input[i];
        if (c == '{') {
            stack.push(currentSet);
            currentSet.clear();
        }
        else if (c == '}') {
            if (!buffer.empty()) {
                currentSet.emplace_back(buffer);
                buffer.clear();
            }
            SetElement newSet(currentSet);
            currentSet = stack.top();
            stack.pop();
            currentSet.push_back(newSet);
        }
        else if (c == ',' && !buffer.empty()) {
            currentSet.emplace_back(buffer);
            buffer.clear();
        }
        else if (c != ' ' && c != ',') {
            buffer += c;
        }
    }
    if (!buffer.empty()) currentSet.emplace_back(buffer);
    return currentSet;
}