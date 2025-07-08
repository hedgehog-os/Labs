#include "replica.h"
#include "sorting.h"
#include "searching.h"
#include <iostream>
#include <fstream>
using namespace std;

// Сортировка пузырьком по имени
void BubbleSortByName(fstream& file, ofstream& report) {
    file.clear();
    file.seekg(0, ios::end);
    int fileSize = file.tellg();
    int recordCount = fileSize / sizeof(Replica);
    if (recordCount <= 0) {
        report << "Ошибка: файл пуст или данные некорректны!" << endl;
        cerr << "Ошибка: файл пуст или данные некорректны!" << endl;
        return;
    }
    file.seekg(0, ios::beg);
    Replica* replicas = new Replica[recordCount];
    for (int i = 0; i < recordCount; ++i) {
        file.read((char*)&replicas[i], sizeof(Replica));
    }
    for (int i = 0; i < recordCount - 1; ++i) {
        for (int j = 0; j < recordCount - i - 1; ++j) {
            if (mystrcmp(replicas[j].name, replicas[j + 1].name) > 0) {
                Replica temp = replicas[j];
                replicas[j] = replicas[j + 1];
                replicas[j + 1] = temp;
            }
        }
    }
    // Переписываем отсортированные данные в тот же файл
    file.seekp(0, ios::beg);

    report << "Реплики успешно отсортированы ''пузырьком'' по имени!" << endl;

    for (int i = 0; i < recordCount; ++i) {
        file.write((char*)&replicas[i], sizeof(Replica));
        
        report << "-----------------------" << endl;
        report << "ID: " << replicas[i].id << endl;
        report << "Ветка диалога: " << replicas[i].branch << endl;
        report << "Имя персонажа: " << replicas[i].name << endl;
        report << "Фраза: " << replicas[i].phrase << endl;
        report << "-----------------------" << endl;
    }
    delete[] replicas;
    file.flush();
    cout << "Файл успешно отсортирован по имени персонажа!" << endl;
}

// Сортировка выбором по названию ветки
void SelectionSortByDialogueBranchName(fstream& file, ofstream& report) {
    file.clear();
    file.seekg(0, ios::end);
    int fileSize = file.tellg();

    int recordCount = fileSize / sizeof(Replica);
    if (recordCount <= 0) {
        cerr << "Ошибка: файл пуст или данные некорректны!" << endl;
        return;
    }

    file.seekg(0, ios::beg);
    Replica* replicas = new Replica[recordCount];

    for (int i = 0; i < recordCount; ++i) {
        file.read((char*)&replicas[i], sizeof(Replica));
    }

    // Сортировка выбором
    for (int i = 0; i < recordCount - 1; ++i) {
        int minIndex = i;
        for (int j = i + 1; j < recordCount; ++j) {
            if (mystrcmp(replicas[j].branch, replicas[minIndex].branch) < 0) {
                minIndex = j;
            }
        }
        Replica temp = replicas[i];
        replicas[i] = replicas[minIndex];
        replicas[minIndex] = temp;
    }

    report << "Реплики успешно отсортированы выбором по названию ветки диалога!" << endl;
    file.clear();
    file.seekp(0, ios::beg);
    for (int i = 0; i < recordCount; ++i) {
        file.write((char*)&replicas[i], sizeof(Replica));


        report << "-----------------------" << endl;
        report << "ID: " << replicas[i].id << endl;
        report << "Ветка диалога: " << replicas[i].branch << endl;
        report << "Имя персонажа: " << replicas[i].name << endl;
        report << "Фраза: " << replicas[i].phrase << endl;
        report << "-----------------------" << endl;
    }

    // Освобождение памяти
    delete[] replicas;

    cout << "Сортировка завершена!" << endl;
}

// Сортировка вставками по ID
void InsertionSortByID(fstream& file, ofstream& report) {
    file.clear();
    file.seekg(0, ios::end);
    int fileSize = file.tellg();

    int recordCount = fileSize / sizeof(Replica);
    if (recordCount <= 0) {
        cerr << "Ошибка: файл пуст или данные некорректны!" << endl;
        return;
    }

    file.seekg(0, ios::beg);
    Replica* replicas = new Replica[recordCount];

    // Чтение всех записей из файла в массив
    for (int i = 0; i < recordCount; ++i) {
        file.read((char*)&replicas[i], sizeof(Replica));
    }

    for (int i = 1; i < recordCount; i++) {
        Replica temp = replicas[i];
        int j;

        for (j = i - 1; j >= 0 && replicas[j].id > temp.id; --j) {
            replicas[j + 1] = replicas[j];
        }
        replicas[j + 1] = temp;
    }

    // Запись отсортированных данных обратно в файл
    report << "Реплики успешно отсортированы вставками ID!" << endl;
    file.clear();
    file.seekp(0, ios::beg);
    for (int i = 0; i < recordCount; ++i) {
        file.write((char*)&replicas[i], sizeof(Replica));

        report << "-----------------------" << endl;
        report << "ID: " << replicas[i].id << endl;
        report << "Ветка диалога: " << replicas[i].branch << endl;
        report << "Имя персонажа: " << replicas[i].name << endl;
        report << "Фраза: " << replicas[i].phrase << endl;
        report << "-----------------------" << endl;
    }

    // Освобождение памяти
    delete[] replicas;

    cout << "Сортировка завершена!" << endl;
}

// Быстрая сортировка по длине фразы
void QuickSortByPhraseLength(Replica arr[], int left, int right) {
    if (left >= right) return;

    int i = left, j = right;
    int pivot = lenchar(arr[(left + right) / 2].phrase);

    while (i <= j) {
        while (lenchar(arr[i].phrase) < pivot) i++;
        while (lenchar(arr[j].phrase) > pivot) j--;

        if (i <= j) {
            Replica temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
            i++;
            j--;
        }
    }

    if (left < j) QuickSortByPhraseLength(arr, left, j);
    if (i < right) QuickSortByPhraseLength(arr, i, right);
}

// Функция сравнения строк для сортировки
int mystrcmp(const char* str1, const char* str2) {
    int i = 0, j = 0;

    // Пропускаем ведущие пробелы и табуляции
    while (str1[i] != '\0' && (str1[i] == ' ' || str1[i] == '\t')) { i++; }
    while (str2[j] != '\0' && (str2[j] == ' ' || str2[j] == '\t')) { j++; }

    while (str1[i] != '\0' && str2[j] != '\0') {
        // Преобразование в нижний регистр
        char c1 = str1[i];
        if (c1 >= 'A' && c1 <= 'Z') {
            c1 += 32;
        }

        char c2 = str2[j];
        if (c2 >= 'A' && c2 <= 'Z') {
            c2 += 32;
        }

        // Сравнение символов
        if (c1 < c2) {
            return -1;
        }
        if (c1 > c2) {
            return 1;
        }

        i++;
        j++;
    }

    // Пропускаем завершающие пробелы
    while (str1[i] != '\0' && (str1[i] == ' ' || str1[i] == '\t')) { i++; }
    while (str2[j] != '\0' && (str2[j] == ' ' || str2[j] == '\t')) { j++; }

    // Финальная проверка остатков строк
    if (str1[i] == '\0' && str2[j] == '\0') {
        return 0;
    }
    if (str1[i] == '\0') {
        return -1;
    }
    return 1;
}