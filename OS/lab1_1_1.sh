#!/bin/bash

# Проверка аргументов
if [ $# -ne 2 ]; then
  echo "Использование: $0 <строка> <каталог>"
  exit 1
fi

SEARCH_STRING="$1"
SEARCH_DIR="$2"

if [ ! -d "$SEARCH_DIR" ]; then
  echo "Ошибка: $SEARCH_DIR не является каталогом"
  exit 1
fi

grep -rl "$SEARCH_STRING" "$SEARCH_DIR" 2>/dev/null | while read -r file; do
  size=$(stat -c%s "$file")
  echo "Файл: $file | Размер: $size байт"
done
