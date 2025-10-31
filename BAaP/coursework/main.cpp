#include <iostream>
#include <fstream>
#include "sorting.h"
#include "searching.h"

// Добавление реплики
void AddReplica(fstream& file, ofstream& report) {
    Replica replica = {};

    // Проверка ввода ID и на уникальность
    while (true) {
        cout << "Введите id реплики: ";
        cin >> replica.id;
        if (cin.fail() || cin.peek() != '\n') {
            cin.clear();
            cin.ignore(1000, '\n');
            cout << "Неверный ввод! Введите **только число**.\n";
            continue;
        }
        cin.ignore();

        // Проверка уникальности ID
        bool exists = false;
        Replica temp;
        file.clear();
        file.seekg(0, ios::beg);
        while (file.read((char*)&temp, sizeof(Replica))) {
            if (temp.id == replica.id) {
                cout << "Реплика с таким ID уже существует. Введите другой ID.\n";
                exists = true;
                break;
            }
        }

        if (!exists) break;
    }

    // Проверка ввода названия ветки диалога
    while (true) {
        cout << "Введите название ветки диалога: ";
        cin.getline(replica.branch, maxsize - 1);
        replica.branch[maxsize - 1] = '\0';

        int len = strlen(replica.branch);
        if (len == 0 || strspn(replica.branch, " \t") == len) {
            cout << "Поле не может быть пустым! Повторите ввод.\n";
            continue;
        }
        break;
    }

    // Проверка ввода имени персонажа
    while (true) {
        cout << "Введите имя персонажа: ";
        cin.getline(replica.name, maxsize - 1);
        replica.name[maxsize - 1] = '\0';

        int len = strlen(replica.name);
        if (len == 0 || strspn(replica.name, " \t") == len) {
            cout << "Имя не может быть пустым! Повторите ввод.\n";
            continue;
        }
        break;
    }

    cout << "Введите фразу: ";
    cin.getline(replica.phrase, maxsize - 1);
    replica.phrase[maxsize - 1] = '\0';

    // Запись в файл
    file.clear();
    file.seekp(0, ios::end);
    if (!file.write((char*)&replica, sizeof(Replica))) {
        cerr << "Ошибка записи в файл!" << endl;
    }
    else {
        cout << "Успешная запись файла!" << endl;
    }

    report << "Успешная запись реплики!" << endl;
    report << "-----------------------" << endl;
    report << "ID: " << replica.id << endl;
    report << "Ветка диалога: " << replica.branch << endl;
    report << "Имя персонажа: " << replica.name << endl;
    report << "Фраза: " << replica.phrase << endl;
    report << "-----------------------" << endl;
}

// Чтение реплик из файла
void ReadReplica(fstream& file, ofstream& report) {
    Replica temp;
    file.clear();
    file.seekg(0, ios::beg);
    while (file.read((char*)&temp, sizeof(Replica))) {
        cout << "ID: " << temp.id << endl;
        cout << "Ветка диалога: " << temp.branch << endl;
        cout << "Имя персонажа: " << temp.name << endl;
        cout << "Фраза: " << temp.phrase << endl;
        cout << "-----------------------" << endl;

        report << "Чтение из файла:" << endl;
        report << "ID: " << temp.id << endl;
        report << "Ветка диалога: " << temp.branch << endl;
        report << "Имя персонажа: " << temp.name << endl;
        report << "Фраза: " << temp.phrase << endl;
        report << "-----------------------" << endl;
    }
    file.clear();
}

// Удаление реплик из файла
void DeleteReplica(fstream& file, ofstream& report, int delete_id) {
    fstream tempFile("temp.bin", ios::out | ios::binary);
    if (!tempFile.is_open()) {
        cerr << "Ошибка: не удалось создать временный файл!" << endl;
        return;
    }
    Replica replica;
    bool found = false;
    file.clear();
    file.seekg(0, ios::beg);
    while (file.read((char*)&replica, sizeof(Replica))) {
        if (replica.id == delete_id) {
            found = true;
        }
        else {
            tempFile.write((char*)&replica, sizeof(Replica));
        }
    }
    tempFile.close();
    if (!found) {
        cout << "Запись с ID " << delete_id << " не найдена." << endl;
        remove("temp.bin");
        return;
    }
    file.close();
    remove("replicas.bin");
    if (rename("temp.bin", "replicas.bin") != 0) {
        cerr << "Ошибка: не удалось переименовать временный файл!" << endl;
        return;
    }
    file.open("replicas.bin", ios::in | ios::out | ios::binary);
    if (!file.is_open()) {
        cerr << "Ошибка: не удалось открыть файл после переименования!" << endl;
        return;
    }
    cout << "Запись с ID " << delete_id << " успешно удалена." << endl;

    report << "Запись с ID " << delete_id << " успешно удалена." << endl;
}


int main() {
    setlocale(LC_ALL, "ru");
    ofstream reportfile("report.txt", ios::app);
    if (!reportfile) {
        std::cerr << "Ошибка: не удалось создать или открыть отчет!" << std::endl;
        return 1;
    }
    fstream binaryfile("replicas.bin", ios::in | ios::out | ios::binary);
    if (!binaryfile.is_open()) {
        binaryfile.open("replicas.bin", ios::out | ios::binary);
        binaryfile.close();
        binaryfile.open("replicas.bin", ios::in | ios::out | ios::binary);
        if (!binaryfile.is_open()) {
            cerr << "Ошибка: не удалось создать или открыть файл!" << endl;
            return 1;
        }
    }
    int choice;
    while (true) {
        cout << "==============================" << endl;
        cout << "1 - Добавление реплики" << endl;
        cout << "2 - Чтение из файла" << endl;
        cout << "3 - Удаление реплики по ID" << endl;
        cout << "4 - Линейный поиск реплик по имени" << endl;
        cout << "5 - Бинарный поиск по ID (требует сортировки по ID)" << endl;
        cout << "6 - Сортировка пузырьком по имени" << endl;
        cout << "7 - Сортировка выбором по названию ветки в диалога" << endl;
        cout << "8 - Сортировка вставками по id" << endl;
        cout << "9 - Поиск всех реплик персонажа" << endl;
        cout << "10 - Схема диалогов" << endl;
        cout << "11 - Редактирование реплики" << endl;
        cout << "12 - Интерполяционный поиск реплики" << endl;
        cout << "13 - Группировка по имени" << endl;
        cout << "0 - Выход" << endl;
        cout << "==============================" << endl;
        cout << "Выберите пункт меню: ";
        cin >> choice;
        cin.ignore();
        cout << endl;
        switch (choice) {
        case 1:
            AddReplica(binaryfile,reportfile);
            break;
        case 2:
            ReadReplica(binaryfile, reportfile);
            break;
        case 3:
            int deleted_id;
            cout << "Введите id удаляемой реплики: ";

            while (true) {
                cin >> deleted_id;

                if (cin.fail() || cin.peek() != '\n') {
                    cin.clear();
                    cin.ignore(1000, '\n');
                    cout << "Неверный ввод! Введите **только число**.\n";
                }
                else {
                    cin.ignore();
                    break;
                }
            }

            DeleteReplica(binaryfile, reportfile, deleted_id);
            break;
        case 4:
            char searchname[maxsize];

            while (true) {
                cout << "Введите имя персонажа: ";
                cin.getline(searchname, maxsize - 1);
                searchname[maxsize - 1] = '\0';

                int len = strlen(searchname);
                if (len == 0 || strspn(searchname, " \t") == len) {
                    cout << "Имя не может быть пустым! Повторите ввод.\n";
                    continue;
                }
                break;
            }
            SearchByName(binaryfile, reportfile, searchname);
            break;
        case 5:
            int searchid;
            cout << "Введите ID искомой реплики: ";

            while (true) {
                cin >> searchid;

                if (cin.fail() || cin.peek() != '\n') {
                    cin.clear();
                    cin.ignore(1000, '\n');
                    cout << "Неверный ввод! Введите **только число**.\n";
                }
                else {
                    cin.ignore();
                    break;
                }
            }

            InsertionSortByID(binaryfile, reportfile);
            BinarySearchByID(binaryfile, reportfile, searchid);
            break;
        case 6:
            BubbleSortByName(binaryfile, reportfile);
            break;
        case 7:
            SelectionSortByDialogueBranchName(binaryfile, reportfile);
            break;
        case 8:
            InsertionSortByID(binaryfile, reportfile);
            break;
        case 9:
            char name[maxsize];
            cout << "Введите имя с искомыми репликами: ";

            while (true) {
                
                cin.getline(name, maxsize - 1);
                name[maxsize - 1] = '\0';

                int len = strlen(name);
                if (len == 0 || strspn(name, " \t") == len) {
                    cout << "Имя не может быть пустым! Повторите ввод.\n";
                    continue;
                }
                break;
            }

            SearchReplicas(binaryfile, reportfile, name);
            break;
        case 10: {
            DialogueScheme(binaryfile, reportfile);
            break;
        }
        case 11: {
            int edit_id;
            cout << "Введите ID редактируемой записи: ";
            cin >> edit_id;
            EditReplica(binaryfile, reportfile, edit_id);
            break;
        }
        case 12: {
            int searchid;
            cout << "Введите реплику с искомым id: ";
            cin >> searchid;
            InsertionSortByID(binaryfile, reportfile);
            InterpolationSearchByID(binaryfile, reportfile, searchid);
            break;
        }
        case 13:
            int length;
            cout << "Введите минимальную длины фраз: ";
            cin >> length;
            GroupByName(binaryfile, reportfile, length);
            break;
        case 0:
            binaryfile.close();
            reportfile.close();
            return 0;
        default:
            cout << "Неверный выбор. Попробуйте снова." << endl;
            break;
        }
    }
}