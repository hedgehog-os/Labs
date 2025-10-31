#include "replica.h"
#include "sorting.h"
#include "searching.h"
#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

// Длина массива char
int lenchar(const char* array) {
    int count = 0;
    for (int i = 0; array[i] != '\0'; i++) {
        count++;
    }

    return count;
}

// Линейный поиск по имени
void SearchByName(fstream& file, ofstream& report, char name[maxsize]) {
    Replica temp;
    bool find = false;
    file.clear();
    file.seekg(0, ios::beg);
    while (file.read((char*)&temp, sizeof(Replica))) {
        if (mystrcmp(temp.name, name) == 0) {
            cout << "ID: " << temp.id << endl;
            cout << "Ветка диалога: " << temp.branch << endl;
            cout << "Имя персонажа: " << temp.name << endl;
            cout << "Фраза: " << temp.phrase << endl;
            cout << "-----------------------" << endl;
            find = true;

            report << "Реплика найдена линейным поиском!" << endl;
            report << "-----------------------" << endl;
            report << "ID: " << temp.id << endl;
            report << "Ветка диалога: " << temp.branch << endl;
            report << "Имя персонажа: " << temp.name << endl;
            report << "Фраза: " << temp.phrase << endl;
            report << "-----------------------" << endl;
        }
    }
    if (!find) {
        cout << "Персонажа с таким именем не было найдено:(" << endl;

        report << "Персонажа с таким именем не было найдено:(" << endl;
    }
    file.clear();
}

// Бинарный поиск по ID
void BinarySearchByID(fstream& file, ofstream& report, int searchID) {
    Replica temp;
    file.clear();
    file.seekg(0, ios::end);
    int fileSize = file.tellg();
    int recordCount = fileSize / sizeof(Replica);
    int left = 0, right = recordCount - 1;
    while (left <= right) {
        int mid = (left + right) / 2;
        file.seekg(mid * sizeof(Replica), ios::beg);
        file.read((char*)&temp, sizeof(Replica));
        if (temp.id == searchID) {
            cout << "ID: " << temp.id << endl;
            cout << "Ветка диалога: " << temp.branch << endl;
            cout << "Имя персонажа: " << temp.name << endl;
            cout << "Фраза: " << temp.phrase << endl;
            
            report << "Реплика успешно найдена бинарным поиском!" << endl;
            report << "-----------------------" << endl;
            report << "ID: " << temp.id << endl;
            report << "Ветка диалога: " << temp.branch << endl;
            report << "Имя персонажа: " << temp.name << endl;
            report << "Фраза: " << temp.phrase << endl;
            report << "-----------------------" << endl;
            return;
        }
        else if (temp.id < searchID) {
            left = mid + 1;
        }
        else {
            right = mid - 1;
        }
    }
    cout << "Элемент с ID " << searchID << " не найден." << endl;

    report << "Элемент с ID " << searchID << " не найден." << endl;
}

void InterpolationSearchByID(fstream& file, ofstream& report, int searchID) {
    file.clear();
    file.seekg(0, ios::end);
    int size = file.tellg() / sizeof(Replica);
    file.seekg(0, ios::beg);

    if (size == 0) {
        cout << "Файл пуст.\n";
        return;
    }

    Replica* arr = new Replica[size];
    file.read((char*)arr, size * sizeof(Replica));

    int low = 0, high = size - 1;
    bool found = false;

    while (low <= high && searchID >= arr[low].id && searchID <= arr[high].id) {
        if (arr[low].id == arr[high].id) {
            if (arr[low].id == searchID) {
                found = true;
                high = low;
            }
            break;
        }

        int pos = low + ((searchID - arr[low].id) * (high - low)) / (arr[high].id - arr[low].id);

        if (pos < 0 || pos >= size) break;

        if (arr[pos].id == searchID) {
            found = true;
            low = high = pos;
            break;
        }

        if (arr[pos].id < searchID)
            low = pos + 1;
        else
            high = pos - 1;
    }

    if (found) {
        cout << "ID: " << arr[low].id << "\n";
        cout << "Ветка: " << arr[low].branch << "\n";
        cout << "Имя: " << arr[low].name << "\n";
        cout << "Фраза: " << arr[low].phrase << "\n";

        report << "Интерполяционный поиск: найдено\n";
        report << "ID: " << arr[low].id << "\n";
        report << "Ветка: " << arr[low].branch << "\n";
        report << "Имя: " << arr[low].name << "\n";
        report << "Фраза: " << arr[low].phrase << "\n";
        report << "---------------------\n";
    }
    else {
        cout << "Реплика с ID " << searchID << " не найдена.\n";
        report << "Интерполяционный поиск: не найдено ID " << searchID << "\n";
    }

    delete[] arr;
}

// Поиск всех реплик персонажа
void SearchReplicas(fstream& file, ofstream& report, char name[maxsize]) {
    Replica* persons = new Replica[maxsize];
    Replica temp;
    int i = 0, symbols = 0;
    bool find = false;

    file.clear();
    file.seekg(0, ios::beg);

    while (file.read((char*)&temp, sizeof(Replica))) {
        if (mystrcmp(temp.name, name) == 0) {
            persons[i] = temp;
            i++;
            symbols += lenchar(temp.phrase);
            find = true;
        }
    }

    if (!find) {
        cout << "Персонажа с таким именем не найдено :(" << endl;
        report << "Персонажа с таким именем не найдено :(" << endl;
        delete[] persons;
        return;
    }

    // Быстрая сортировка по длине фразы
    QuickSortByPhraseLength(persons, 0, i - 1);

    for (int j = 0; j < i; j++) {
        cout << "ID: " << persons[j].id << endl;
        cout << "Ветка диалога: " << persons[j].branch << endl;
        cout << "Имя персонажа: " << persons[j].name << endl;
        cout << "Фраза: " << persons[j].phrase << endl;
        cout << "-----------------------" << endl;

        report << "Реплика персонажа успешно найдена!" << endl;
        report << "-----------------------" << endl;
        report << "ID: " << persons[j].id << endl;
        report << "Ветка диалога: " << persons[j].branch << endl;
        report << "Имя персонажа: " << persons[j].name << endl;
        report << "Фраза: " << persons[j].phrase << endl;
        report << "-----------------------" << endl;
    }

    cout << "Реплики содержат суммарно " << symbols << " символов" << endl;
    report << "Реплики содержат суммарно " << symbols << " символов" << endl;

    delete[] persons;
}

// Сохранение обновлений реплики
void SaveReplica(fstream& file, streampos pos, Replica replica){
    file.clear();
    file.seekp(pos);
    if (!file.write((char*)&replica, sizeof(Replica))) {
        cerr << "Ошибка обновления файла!" << endl;
    }
    else {
        cout << "Реплика успешно обновлена!" << endl;
    }
}

// Редактирование реплики по id
void EditReplica(fstream& file, ofstream& report, int editId) {
    int choice;
    Replica replica;
    bool found = false;
    streampos pos;

    file.clear();
    file.seekg(0, ios::beg);

    while (file.read((char*)&replica, sizeof(Replica))) {
        if (replica.id == editId) {
            cout << "Реплика до редактирования" << endl;
            cout << "-----------------------" << endl;
            cout << "ID: " << replica.id << endl;
            cout << "Ветка диалога: " << replica.branch << endl;
            cout << "Имя персонажа: " << replica.name << endl;
            cout << "Фраза: " << replica.phrase << endl;
            cout << "-----------------------" << endl;

            report << "Реплика до редактирования" << endl;
            report << "-----------------------" << endl;
            report << "ID: " << replica.id << endl;
            report << "Ветка диалога: " << replica.branch << endl;
            report << "Имя персонажа: " << replica.name << endl;
            report << "Фраза: " << replica.phrase << endl;
            report << "-----------------------" << endl;
            found = true;
            pos = file.tellg() - static_cast<streampos>(sizeof(Replica));
            break;
        }
    }

    if (!found) {
        cout << "Запись с ID " << editId << " не найдена." << endl;

        report << "Запись с ID " << editId << " не найдена." << endl;
        return;
    }

    while (true)
    {
        cout << "Выберите редактируемый параметр:" << endl;
        cout << "1 - id" << endl;
        cout << "2 - название ветки даилога" << endl;
        cout << "3 - имя персонажа" << endl;
        cout << "4 - фразу" << endl;
        cout << "0 - выход из режима редактирования" << endl;
        cin >> choice;

        switch (choice){
        
        case 1:
            // Проверка ввода нового ID
            while (true) {
                cout << "Введите новый ID реплики: ";
                int newId;
                cin >> newId;
                if (cin.fail()) {
                    cin.clear();
                    cin.ignore(1000, '\n');
                    cout << "Неверный ввод! Введите **только число**.\n";
                    continue;
                }
                cin.ignore(1000, '\n');

                // Проверка уникальности ID
                bool exists = false;
                Replica temp;
                file.clear();
                file.seekg(0, ios::beg);
                while (file.read((char*)&temp, sizeof(Replica))) {
                    if (temp.id == newId && temp.id != editId) {
                        cout << "Реплика с таким ID уже существует. Введите другой ID.\n";
                        exists = true;
                        break;
                    }
                }

                if (!exists) {
                    replica.id = newId;
                    break;
                }
            }


            // Запись
            SaveReplica(file, pos, replica);
            report << "ID был изменен на " << replica.id << endl;

            break;

        case 2:
            // Название ветки
            while (true) {
                cout << "Введите новое название ветки диалога: ";
                cin.getline(replica.branch, sizeof(replica.branch));
                replica.branch[sizeof(replica.branch) - 1] = '\0';

                int len = strlen(replica.branch);
                if (len == 0 || strspn(replica.branch, " \t") == len) {
                    cout << "Поле не может быть пустым! Повторите ввод.\n";
                    continue;
                }
                break;
            }

            // Запись
            SaveReplica(file, pos, replica);
            report << "Yазвание ветки было изменено на " << replica.branch << endl;
            break;

        case 3:
            // Имя персонажа
            cin.ignore();
            while (true) {
                cout << "Введите новое имя персонажа: ";
                cin.getline(replica.name, sizeof(replica.name));
                replica.name[sizeof(replica.name) - 1] = '\0';

                int len = strlen(replica.name);
                if (len == 0 || strspn(replica.name, " \t") == len) {
                    cout << "Имя не может быть пустым! Повторите ввод.\n";
                    continue;
                }
                break;
            }

            // Запись
            SaveReplica(file, pos, replica);
            report << "Bмя персонажа было изменено на " << replica.name << endl;
            break;

        case 4:
            // Фраза
            while (true) {
                cout << "Введите новую фразу: ";
                cin.getline(replica.phrase, sizeof(replica.phrase));
                replica.phrase[sizeof(replica.phrase) - 1] = '\0';

                int len = strlen(replica.phrase);
                if (len == 0 || strspn(replica.phrase, " \t") == len) {
                    cout << "Фраза не может быть пустой! Повторите ввод.\n";
                    continue;
                }
                break;
            }

            // Запись
            SaveReplica(file, pos, replica);
            report << "Название фразы было изменено на " << replica.phrase << endl;
            break;

        case 0:
            cout << "Реплика после редактирования" << endl;
            cout << "-----------------------" << endl;
            cout << "ID: " << replica.id << endl;
            cout << "Ветка диалога: " << replica.branch << endl;
            cout << "Имя персонажа: " << replica.name << endl;
            cout << "Фраза: " << replica.phrase << endl;
            cout << "-----------------------" << endl;

            report << "Реплика после редактирования" << endl;
            report << "-----------------------" << endl;
            report << "ID: " << replica.id << endl;
            report << "Ветка диалога: " << replica.branch << endl;
            report << "Имя персонажа: " << replica.name << endl;
            report << "Фраза: " << replica.phrase << endl;
            report << "-----------------------" << endl;
            return;
        }
        
    }
}

// Схема диалогов с форматированием
void DialogueScheme(fstream& file, ofstream& report) {
    Replica temp;
    int i = 0;
    file.clear();
    file.seekg(0, ios::end);
    int fileSize = file.tellg();
    int recordCount = fileSize / sizeof(Replica);
    if (recordCount == 0) {
        cout << "Файл пуст. Нет данных для отображения." << endl;
        return;
    }

   
    Replica* replicas = new Replica[recordCount];

    file.seekg(0, ios::beg);
    while (file.read((char*)&temp, sizeof(Replica))) {
        if (i >= recordCount) {
            cerr << "Ошибка: Количество записей превышает ожидаемое!" << endl;
            break;
        }
        // Принудительно завершаем строки
        for (int j = 0; j < maxsize; j++) {
            if (temp.branch[j] == '\0') break;
            if (j == maxsize - 1) temp.branch[j] = '\0';
        }
        for (int j = 0; j < maxsize; j++) {
            if (temp.name[j] == '\0') break;
            if (j == maxsize - 1) temp.name[j] = '\0';
        }
        for (int j = 0; j < maxsize; j++) {
            if (temp.phrase[j] == '\0') break;
            if (j == maxsize - 1) temp.phrase[j] = '\0';
        }
        replicas[i] = temp;
        i++;
    }

    // Сортировка записей сначала по ветке диалога, затем по ID
    for (int j = 0; j < i - 1; ++j) {
        for (int k = 0; k < i - j - 1; ++k) {
           
            int cmp_result = mystrcmp(replicas[k].branch, replicas[k + 1].branch);

            // Сравниваем названия веток
            if (cmp_result > 0) {
                Replica temp = replicas[k];
                replicas[k] = replicas[k + 1];
                replicas[k + 1] = temp;
            }
            // Если ветки равны, сравниваем по id
            else if (cmp_result == 0 && replicas[k].id > replicas[k + 1].id) {
                Replica temp = replicas[k];
                replicas[k] = replicas[k + 1];
                replicas[k + 1] = temp;
            }
        }
    }

    // Форматированный вывод с iomanip
    cout << setw(60) << setfill('=') << "" << endl;
    cout << setw(30) << setfill(' ') << "" << "СХЕМА ДИАЛОГОВ" << endl;
    cout << setw(60) << setfill('=') << "" << endl;
    for (int j = 0; j < i; ++j) {
        cout << setfill(' ') << setw(15) << left << "Ветка диалога:" << replicas[j].branch << endl;
        cout << "  -> " << setw(5) << left << "ID:" << replicas[j].id << endl;
        cout << "     " << setw(5) << left << "Имя:" << replicas[j].name << endl;
        cout << "     " << setw(5) << left << "Фраза:" << replicas[j].phrase << endl << endl;

        if (j < i - 1 && mystrcmp(replicas[j].branch, replicas[j + 1].branch) != 0) {
            cout << setw(60) << setfill('-') << "" << endl;
        }
    }

    // Вывод в отчёт
    report << setw(60) << setfill('=') << "" << endl;
    report << setw(30) << setfill(' ') << "" << "СХЕМА ДИАЛОГОВ" << endl;
    report << setw(60) << setfill('=') << "" << endl;
    for (int j = 0; j < i; ++j) {
        report << setfill(' ') << setw(15) << left << "Ветка диалога:" << replicas[j].branch << endl;
        report << "  -> " << setw(5) << left << "ID:" << replicas[j].id << endl;
        report << "     " << setw(5) << left << "Имя:" << replicas[j].name << endl;
        report << "     " << setw(5) << left << "Фраза:" << replicas[j].phrase << endl << endl;

        if (j < i - 1 && mystrcmp(replicas[j].branch, replicas[j + 1].branch) != 0) {
            report << setw(60) << setfill('-') << "" << endl;
        }
    }

    // Освобождаем память
    delete[] replicas;
}

void GroupByName(fstream& file, ofstream& report, int len) {
    Replica temp;
    file.clear();
    file.seekg(0, ios::end);
    int fileSize = file.tellg();
    int recordCount = fileSize / sizeof(Replica);

    if (recordCount == 0) {
        cout << "Файл пуст. Нет данных для отображения." << endl;
        return;
    }

    Replica* replicas = new Replica[recordCount];
    file.seekg(0, ios::beg);
    int i = 0;

    while (file.read((char*)&temp, sizeof(Replica)) && i < recordCount) {
        replicas[i++] = temp;
    }

    // Сортировка: по имени, потом по фразе
    for (int j = 0; j < i - 1; ++j) {
        for (int k = 0; k < i - j - 1; ++k) {
            int cmp_name = mystrcmp(replicas[k].name, replicas[k + 1].name);
            int cmp_phrase = mystrcmp(replicas[k].phrase, replicas[k + 1].phrase);
            if (cmp_name > 0 || (cmp_name == 0 && cmp_phrase > 0)) {
                Replica temp = replicas[k];
                replicas[k] = replicas[k + 1];
                replicas[k + 1] = temp;
            }
        }
    }

    // Вывод
    cout << setw(70) << setfill('=') << "" << endl;
    cout << setw(30) << setfill(' ') << "" << "ГРУППИРОВКА ПО ИМЕНИ" << endl;
    cout << setw(70) << setfill('=') << "" << endl;

    report << setw(70) << setfill('=') << "" << endl;
    report << setw(30) << setfill(' ') << "" << "ГРУППИРОВКА ПО ИМЕНИ" << endl;
    report << setw(70) << setfill('=') << "" << endl;

    bool firstGroup = true;

    for (int j = 0; j < i; ++j) {
        if (lenchar(replicas[j].phrase) <= len) continue;

        // Новый блок персонажа (если первый или имя отличается от предыдущего)
        if (j == 0 || mystrcmp(replicas[j].name, replicas[j - 1].name) != 0) {
            if (!firstGroup) {
                cout << setw(70) << setfill('-') << "" << endl;
                report << setw(70) << setfill('-') << "" << endl;
            }
            else {
                firstGroup = false;
            }

            cout << "\n>>> ПЕРСОНАЖ: " << replicas[j].name << " <<<\n" << endl;
            report << "\n>>> ПЕРСОНАЖ: " << replicas[j].name << " <<<\n" << endl;
        }

        // Реплика
        cout << " Ветка   : " << replicas[j].branch << endl;
        cout << " ID      : " << replicas[j].id << endl;
        cout << " Фраза   : " << replicas[j].phrase << endl << endl;

        report << " Ветка   : " << replicas[j].branch << endl;
        report << " ID      : " << replicas[j].id << endl;
        report << " Фраза   : " << replicas[j].phrase << endl << endl;
    }

    delete[] replicas;
}