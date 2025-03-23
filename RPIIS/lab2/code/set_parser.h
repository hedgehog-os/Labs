#ifndef SET_PARSER_H
#define SET_PARSER_H

#include "set_element.h"
#include <string>
#include <vector>

std::vector<SetElement> parseSet(const std::string& input);
SetElement parseElement(std::string element);
#endif