#include "replica.h"
#include "sorting.h"
#include "searching.h"
#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

// ����� ������� char
int lenchar(const char* array) {
    int count = 0;
    for (int i = 0; array[i] != '\0'; i++) {
        count++;
    }

    return count;
}

// �������� ����� �� �����
void SearchByName(fstream& file, ofstream& report, char name[maxsize]) {
    Replica temp;
    bool find = false;
    file.clear();
    file.seekg(0, ios::beg);
    while (file.read((char*)&temp, sizeof(Replica))) {
        if (mystrcmp(temp.name, name) == 0) {
            cout << "ID: " << temp.id << endl;
            cout << "����� �������: " << temp.branch << endl;
            cout << "��� ���������: " << temp.name << endl;
            cout << "�����: " << temp.phrase << endl;
            cout << "-----------------------" << endl;
            find = true;

            report << "������� ������� �������� �������!" << endl;
            report << "-----------------------" << endl;
            report << "ID: " << temp.id << endl;
            report << "����� �������: " << temp.branch << endl;
            report << "��� ���������: " << temp.name << endl;
            report << "�����: " << temp.phrase << endl;
            report << "-----------------------" << endl;
        }
    }
    if (!find) {
        cout << "��������� � ����� ������ �� ���� �������:(" << endl;

        report << "��������� � ����� ������ �� ���� �������:(" << endl;
    }
    file.clear();
}

// �������� ����� �� ID
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
            cout << "����� �������: " << temp.branch << endl;
            cout << "��� ���������: " << temp.name << endl;
            cout << "�����: " << temp.phrase << endl;
            
            report << "������� ������� ������� �������� �������!" << endl;
            report << "-----------------------" << endl;
            report << "ID: " << temp.id << endl;
            report << "����� �������: " << temp.branch << endl;
            report << "��� ���������: " << temp.name << endl;
            report << "�����: " << temp.phrase << endl;
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
    cout << "������� � ID " << searchID << " �� ������." << endl;

    report << "������� � ID " << searchID << " �� ������." << endl;
}

void InterpolationSearchByID(fstream& file, ofstream& report, int searchID) {
    file.clear();
    file.seekg(0, ios::end);
    int size = file.tellg() / sizeof(Replica);
    file.seekg(0, ios::beg);

    if (size == 0) {
        cout << "���� ����.\n";
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
        cout << "�����: " << arr[low].branch << "\n";
        cout << "���: " << arr[low].name << "\n";
        cout << "�����: " << arr[low].phrase << "\n";

        report << "���������������� �����: �������\n";
        report << "ID: " << arr[low].id << "\n";
        report << "�����: " << arr[low].branch << "\n";
        report << "���: " << arr[low].name << "\n";
        report << "�����: " << arr[low].phrase << "\n";
        report << "---------------------\n";
    }
    else {
        cout << "������� � ID " << searchID << " �� �������.\n";
        report << "���������������� �����: �� ������� ID " << searchID << "\n";
    }

    delete[] arr;
}

// ����� ���� ������ ���������
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
        cout << "��������� � ����� ������ �� ������� :(" << endl;
        report << "��������� � ����� ������ �� ������� :(" << endl;
        delete[] persons;
        return;
    }

    // ������� ���������� �� ����� �����
    QuickSortByPhraseLength(persons, 0, i - 1);

    for (int j = 0; j < i; j++) {
        cout << "ID: " << persons[j].id << endl;
        cout << "����� �������: " << persons[j].branch << endl;
        cout << "��� ���������: " << persons[j].name << endl;
        cout << "�����: " << persons[j].phrase << endl;
        cout << "-----------------------" << endl;

        report << "������� ��������� ������� �������!" << endl;
        report << "-----------------------" << endl;
        report << "ID: " << persons[j].id << endl;
        report << "����� �������: " << persons[j].branch << endl;
        report << "��� ���������: " << persons[j].name << endl;
        report << "�����: " << persons[j].phrase << endl;
        report << "-----------------------" << endl;
    }

    cout << "������� �������� �������� " << symbols << " ��������" << endl;
    report << "������� �������� �������� " << symbols << " ��������" << endl;

    delete[] persons;
}

// ���������� ���������� �������
void SaveReplica(fstream& file, streampos pos, Replica replica){
    file.clear();
    file.seekp(pos);
    if (!file.write((char*)&replica, sizeof(Replica))) {
        cerr << "������ ���������� �����!" << endl;
    }
    else {
        cout << "������� ������� ���������!" << endl;
    }
}

// �������������� ������� �� id
void EditReplica(fstream& file, ofstream& report, int editId) {
    int choice;
    Replica replica;
    bool found = false;
    streampos pos;

    file.clear();
    file.seekg(0, ios::beg);

    while (file.read((char*)&replica, sizeof(Replica))) {
        if (replica.id == editId) {
            cout << "������� �� ��������������" << endl;
            cout << "-----------------------" << endl;
            cout << "ID: " << replica.id << endl;
            cout << "����� �������: " << replica.branch << endl;
            cout << "��� ���������: " << replica.name << endl;
            cout << "�����: " << replica.phrase << endl;
            cout << "-----------------------" << endl;

            report << "������� �� ��������������" << endl;
            report << "-----------------------" << endl;
            report << "ID: " << replica.id << endl;
            report << "����� �������: " << replica.branch << endl;
            report << "��� ���������: " << replica.name << endl;
            report << "�����: " << replica.phrase << endl;
            report << "-----------------------" << endl;
            found = true;
            pos = file.tellg() - static_cast<streampos>(sizeof(Replica));
            break;
        }
    }

    if (!found) {
        cout << "������ � ID " << editId << " �� �������." << endl;

        report << "������ � ID " << editId << " �� �������." << endl;
        return;
    }

    while (true)
    {
        cout << "�������� ������������� ��������:" << endl;
        cout << "1 - id" << endl;
        cout << "2 - �������� ����� �������" << endl;
        cout << "3 - ��� ���������" << endl;
        cout << "4 - �����" << endl;
        cout << "0 - ����� �� ������ ��������������" << endl;
        cin >> choice;

        switch (choice){
        
        case 1:
            // �������� ����� ������ ID
            while (true) {
                cout << "������� ����� ID �������: ";
                int newId;
                cin >> newId;
                if (cin.fail()) {
                    cin.clear();
                    cin.ignore(1000, '\n');
                    cout << "�������� ����! ������� **������ �����**.\n";
                    continue;
                }
                cin.ignore(1000, '\n');

                // �������� ������������ ID
                bool exists = false;
                Replica temp;
                file.clear();
                file.seekg(0, ios::beg);
                while (file.read((char*)&temp, sizeof(Replica))) {
                    if (temp.id == newId && temp.id != editId) {
                        cout << "������� � ����� ID ��� ����������. ������� ������ ID.\n";
                        exists = true;
                        break;
                    }
                }

                if (!exists) {
                    replica.id = newId;
                    break;
                }
            }


            // ������
            SaveReplica(file, pos, replica);
            report << "ID ��� ������� �� " << replica.id << endl;

            break;

        case 2:
            // �������� �����
            while (true) {
                cout << "������� ����� �������� ����� �������: ";
                cin.getline(replica.branch, sizeof(replica.branch));
                replica.branch[sizeof(replica.branch) - 1] = '\0';

                int len = strlen(replica.branch);
                if (len == 0 || strspn(replica.branch, " \t") == len) {
                    cout << "���� �� ����� ���� ������! ��������� ����.\n";
                    continue;
                }
                break;
            }

            // ������
            SaveReplica(file, pos, replica);
            report << "Y������� ����� ���� �������� �� " << replica.branch << endl;
            break;

        case 3:
            // ��� ���������
            cin.ignore();
            while (true) {
                cout << "������� ����� ��� ���������: ";
                cin.getline(replica.name, sizeof(replica.name));
                replica.name[sizeof(replica.name) - 1] = '\0';

                int len = strlen(replica.name);
                if (len == 0 || strspn(replica.name, " \t") == len) {
                    cout << "��� �� ����� ���� ������! ��������� ����.\n";
                    continue;
                }
                break;
            }

            // ������
            SaveReplica(file, pos, replica);
            report << "B�� ��������� ���� �������� �� " << replica.name << endl;
            break;

        case 4:
            // �����
            while (true) {
                cout << "������� ����� �����: ";
                cin.getline(replica.phrase, sizeof(replica.phrase));
                replica.phrase[sizeof(replica.phrase) - 1] = '\0';

                int len = strlen(replica.phrase);
                if (len == 0 || strspn(replica.phrase, " \t") == len) {
                    cout << "����� �� ����� ���� ������! ��������� ����.\n";
                    continue;
                }
                break;
            }

            // ������
            SaveReplica(file, pos, replica);
            report << "�������� ����� ���� �������� �� " << replica.phrase << endl;
            break;

        case 0:
            cout << "������� ����� ��������������" << endl;
            cout << "-----------------------" << endl;
            cout << "ID: " << replica.id << endl;
            cout << "����� �������: " << replica.branch << endl;
            cout << "��� ���������: " << replica.name << endl;
            cout << "�����: " << replica.phrase << endl;
            cout << "-----------------------" << endl;

            report << "������� ����� ��������������" << endl;
            report << "-----------------------" << endl;
            report << "ID: " << replica.id << endl;
            report << "����� �������: " << replica.branch << endl;
            report << "��� ���������: " << replica.name << endl;
            report << "�����: " << replica.phrase << endl;
            report << "-----------------------" << endl;
            return;
        }
        
    }
}

// ����� �������� � ���������������
void DialogueScheme(fstream& file, ofstream& report) {
    Replica temp;
    int i = 0;
    file.clear();
    file.seekg(0, ios::end);
    int fileSize = file.tellg();
    int recordCount = fileSize / sizeof(Replica);
    if (recordCount == 0) {
        cout << "���� ����. ��� ������ ��� �����������." << endl;
        return;
    }

   
    Replica* replicas = new Replica[recordCount];

    file.seekg(0, ios::beg);
    while (file.read((char*)&temp, sizeof(Replica))) {
        if (i >= recordCount) {
            cerr << "������: ���������� ������� ��������� ���������!" << endl;
            break;
        }
        // ������������� ��������� ������
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

    // ���������� ������� ������� �� ����� �������, ����� �� ID
    for (int j = 0; j < i - 1; ++j) {
        for (int k = 0; k < i - j - 1; ++k) {
           
            int cmp_result = mystrcmp(replicas[k].branch, replicas[k + 1].branch);

            // ���������� �������� �����
            if (cmp_result > 0) {
                Replica temp = replicas[k];
                replicas[k] = replicas[k + 1];
                replicas[k + 1] = temp;
            }
            // ���� ����� �����, ���������� �� id
            else if (cmp_result == 0 && replicas[k].id > replicas[k + 1].id) {
                Replica temp = replicas[k];
                replicas[k] = replicas[k + 1];
                replicas[k + 1] = temp;
            }
        }
    }

    // ��������������� ����� � iomanip
    cout << setw(60) << setfill('=') << "" << endl;
    cout << setw(30) << setfill(' ') << "" << "����� ��������" << endl;
    cout << setw(60) << setfill('=') << "" << endl;
    for (int j = 0; j < i; ++j) {
        cout << setfill(' ') << setw(15) << left << "����� �������:" << replicas[j].branch << endl;
        cout << "  -> " << setw(5) << left << "ID:" << replicas[j].id << endl;
        cout << "     " << setw(5) << left << "���:" << replicas[j].name << endl;
        cout << "     " << setw(5) << left << "�����:" << replicas[j].phrase << endl << endl;

        if (j < i - 1 && mystrcmp(replicas[j].branch, replicas[j + 1].branch) != 0) {
            cout << setw(60) << setfill('-') << "" << endl;
        }
    }

    // ����� � �����
    report << setw(60) << setfill('=') << "" << endl;
    report << setw(30) << setfill(' ') << "" << "����� ��������" << endl;
    report << setw(60) << setfill('=') << "" << endl;
    for (int j = 0; j < i; ++j) {
        report << setfill(' ') << setw(15) << left << "����� �������:" << replicas[j].branch << endl;
        report << "  -> " << setw(5) << left << "ID:" << replicas[j].id << endl;
        report << "     " << setw(5) << left << "���:" << replicas[j].name << endl;
        report << "     " << setw(5) << left << "�����:" << replicas[j].phrase << endl << endl;

        if (j < i - 1 && mystrcmp(replicas[j].branch, replicas[j + 1].branch) != 0) {
            report << setw(60) << setfill('-') << "" << endl;
        }
    }

    // ����������� ������
    delete[] replicas;
}

void GroupByName(fstream& file, ofstream& report, int len) {
    Replica temp;
    file.clear();
    file.seekg(0, ios::end);
    int fileSize = file.tellg();
    int recordCount = fileSize / sizeof(Replica);

    if (recordCount == 0) {
        cout << "���� ����. ��� ������ ��� �����������." << endl;
        return;
    }

    Replica* replicas = new Replica[recordCount];
    file.seekg(0, ios::beg);
    int i = 0;

    while (file.read((char*)&temp, sizeof(Replica)) && i < recordCount) {
        replicas[i++] = temp;
    }

    // ����������: �� �����, ����� �� �����
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

    // �����
    cout << setw(70) << setfill('=') << "" << endl;
    cout << setw(30) << setfill(' ') << "" << "����������� �� �����" << endl;
    cout << setw(70) << setfill('=') << "" << endl;

    report << setw(70) << setfill('=') << "" << endl;
    report << setw(30) << setfill(' ') << "" << "����������� �� �����" << endl;
    report << setw(70) << setfill('=') << "" << endl;

    bool firstGroup = true;

    for (int j = 0; j < i; ++j) {
        if (lenchar(replicas[j].phrase) <= len) continue;

        // ����� ���� ��������� (���� ������ ��� ��� ���������� �� �����������)
        if (j == 0 || mystrcmp(replicas[j].name, replicas[j - 1].name) != 0) {
            if (!firstGroup) {
                cout << setw(70) << setfill('-') << "" << endl;
                report << setw(70) << setfill('-') << "" << endl;
            }
            else {
                firstGroup = false;
            }

            cout << "\n>>> ��������: " << replicas[j].name << " <<<\n" << endl;
            report << "\n>>> ��������: " << replicas[j].name << " <<<\n" << endl;
        }

        // �������
        cout << " �����   : " << replicas[j].branch << endl;
        cout << " ID      : " << replicas[j].id << endl;
        cout << " �����   : " << replicas[j].phrase << endl << endl;

        report << " �����   : " << replicas[j].branch << endl;
        report << " ID      : " << replicas[j].id << endl;
        report << " �����   : " << replicas[j].phrase << endl << endl;
    }

    delete[] replicas;
}