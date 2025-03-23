#include "set_parser.h"
#include "set_element.h"

std::vector<SetElement> parseSet(const std::string& input) {
    std::vector<SetElement> result;
    if (input.empty()) return result; // ������ ���� � ������ ���������

    std::string trimmed = input;
    // ������� ������� ��� ���������
    trimmed.erase(std::remove_if(trimmed.begin(), trimmed.end(), isspace), trimmed.end());

    // ��������� ������������������ ������
    int braceCount = 0;
    for (char c : trimmed) {
        if (c == '{') braceCount++;
        if (c == '}') braceCount--;
        if (braceCount < 0) return {}; // ����������� ������ ��� ����������� � ������
    }
    if (braceCount != 0) return {}; // ������������������ ������ � ������

    // ��������� �������� �� ������� ��� ������
    std::string current;
    int depth = 0;
    for (char c : trimmed) {
        if (c == '{') depth++;
        if (c == '}') depth--;
        if (depth < 0) return {}; // ������: ������ ����������� ������
        if (c == ',' && depth == 0) {
            if (!current.empty()) {
                result.push_back(parseElement(current));
                current.clear();
            }
        }
        else {
            current += c;
        }
    }
    if (!current.empty()) {
        result.push_back(parseElement(current));
    }

    return result;
}

// ��������������� ������� ��� �������� ������ ��������
SetElement parseElement(std::string element) {
    // ������� �������
    element.erase(std::remove_if(element.begin(), element.end(), isspace), element.end());

    if (element.empty()) return SetElement(""); // ������ �������

    if (element[0] == '{' && element.back() == '}') {
        // ��� ������������
        std::string subsetStr = element.substr(1, element.size() - 2);
        std::vector<SetElement> subset = parseSet(subsetStr);
        return SetElement(subset);
    }
    else {
        // ��� ��������� �������
        return SetElement(element);
    }
}