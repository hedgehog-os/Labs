#include "set_parser.h"
#include "set_element.h"

std::vector<SetElement> parseSet(const std::string& input) {
    std::vector<SetElement> result;
    if (input.empty()) return result; // Пустой ввод — пустой результат

    std::string trimmed = input;
    // Удаляем пробелы для упрощения
    trimmed.erase(std::remove_if(trimmed.begin(), trimmed.end(), isspace), trimmed.end());

    // Проверяем сбалансированность скобок
    int braceCount = 0;
    for (char c : trimmed) {
        if (c == '{') braceCount++;
        if (c == '}') braceCount--;
        if (braceCount < 0) return {}; // Закрывающая скобка без открывающей — ошибка
    }
    if (braceCount != 0) return {}; // Несбалансированные скобки — ошибка

    // Разделяем элементы по запятым вне скобок
    std::string current;
    int depth = 0;
    for (char c : trimmed) {
        if (c == '{') depth++;
        if (c == '}') depth--;
        if (depth < 0) return {}; // Ошибка: лишняя закрывающая скобка
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

// Вспомогательная функция для парсинга одного элемента
SetElement parseElement(std::string element) {
    // Удаляем пробелы
    element.erase(std::remove_if(element.begin(), element.end(), isspace), element.end());

    if (element.empty()) return SetElement(""); // Пустой элемент

    if (element[0] == '{' && element.back() == '}') {
        // Это подмножество
        std::string subsetStr = element.substr(1, element.size() - 2);
        std::vector<SetElement> subset = parseSet(subsetStr);
        return SetElement(subset);
    }
    else {
        // Это атомарный элемент
        return SetElement(element);
    }
}