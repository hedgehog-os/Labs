#include "replica.h"
#include "sorting.h"
#include "searching.h"
#include <iostream>
#include <fstream>
using namespace std;

// ���������� ��������� �� �����
void BubbleSortByName(fstream& file, ofstream& report) {
    file.clear();
    file.seekg(0, ios::end);
    int fileSize = file.tellg();
    int recordCount = fileSize / sizeof(Replica);
    if (recordCount <= 0) {
        report << "������: ���� ���� ��� ������ �����������!" << endl;
        cerr << "������: ���� ���� ��� ������ �����������!" << endl;
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
    // ������������ ��������������� ������ � ��� �� ����
    file.seekp(0, ios::beg);

    report << "������� ������� ������������� ''���������'' �� �����!" << endl;

    for (int i = 0; i < recordCount; ++i) {
        file.write((char*)&replicas[i], sizeof(Replica));
        
        report << "-----------------------" << endl;
        report << "ID: " << replicas[i].id << endl;
        report << "����� �������: " << replicas[i].branch << endl;
        report << "��� ���������: " << replicas[i].name << endl;
        report << "�����: " << replicas[i].phrase << endl;
        report << "-----------------------" << endl;
    }
    delete[] replicas;
    file.flush();
    cout << "���� ������� ������������ �� ����� ���������!" << endl;
}

// ���������� ������� �� �������� �����
void SelectionSortByDialogueBranchName(fstream& file, ofstream& report) {
    file.clear();
    file.seekg(0, ios::end);
    int fileSize = file.tellg();

    int recordCount = fileSize / sizeof(Replica);
    if (recordCount <= 0) {
        cerr << "������: ���� ���� ��� ������ �����������!" << endl;
        return;
    }

    file.seekg(0, ios::beg);
    Replica* replicas = new Replica[recordCount];

    for (int i = 0; i < recordCount; ++i) {
        file.read((char*)&replicas[i], sizeof(Replica));
    }

    // ���������� �������
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

    report << "������� ������� ������������� ������� �� �������� ����� �������!" << endl;
    file.clear();
    file.seekp(0, ios::beg);
    for (int i = 0; i < recordCount; ++i) {
        file.write((char*)&replicas[i], sizeof(Replica));


        report << "-----------------------" << endl;
        report << "ID: " << replicas[i].id << endl;
        report << "����� �������: " << replicas[i].branch << endl;
        report << "��� ���������: " << replicas[i].name << endl;
        report << "�����: " << replicas[i].phrase << endl;
        report << "-----------------------" << endl;
    }

    // ������������ ������
    delete[] replicas;

    cout << "���������� ���������!" << endl;
}

// ���������� ��������� �� ID
void InsertionSortByID(fstream& file, ofstream& report) {
    file.clear();
    file.seekg(0, ios::end);
    int fileSize = file.tellg();

    int recordCount = fileSize / sizeof(Replica);
    if (recordCount <= 0) {
        cerr << "������: ���� ���� ��� ������ �����������!" << endl;
        return;
    }

    file.seekg(0, ios::beg);
    Replica* replicas = new Replica[recordCount];

    // ������ ���� ������� �� ����� � ������
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

    // ������ ��������������� ������ ������� � ����
    report << "������� ������� ������������� ��������� ID!" << endl;
    file.clear();
    file.seekp(0, ios::beg);
    for (int i = 0; i < recordCount; ++i) {
        file.write((char*)&replicas[i], sizeof(Replica));

        report << "-----------------------" << endl;
        report << "ID: " << replicas[i].id << endl;
        report << "����� �������: " << replicas[i].branch << endl;
        report << "��� ���������: " << replicas[i].name << endl;
        report << "�����: " << replicas[i].phrase << endl;
        report << "-----------------------" << endl;
    }

    // ������������ ������
    delete[] replicas;

    cout << "���������� ���������!" << endl;
}

// ������� ���������� �� ����� �����
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

// ������� ��������� ����� ��� ����������
int mystrcmp(const char* str1, const char* str2) {
    int i = 0, j = 0;

    // ���������� ������� ������� � ���������
    while (str1[i] != '\0' && (str1[i] == ' ' || str1[i] == '\t')) { i++; }
    while (str2[j] != '\0' && (str2[j] == ' ' || str2[j] == '\t')) { j++; }

    while (str1[i] != '\0' && str2[j] != '\0') {
        // �������������� � ������ �������
        char c1 = str1[i];
        if (c1 >= 'A' && c1 <= 'Z') {
            c1 += 32;
        }

        char c2 = str2[j];
        if (c2 >= 'A' && c2 <= 'Z') {
            c2 += 32;
        }

        // ��������� ��������
        if (c1 < c2) {
            return -1;
        }
        if (c1 > c2) {
            return 1;
        }

        i++;
        j++;
    }

    // ���������� ����������� �������
    while (str1[i] != '\0' && (str1[i] == ' ' || str1[i] == '\t')) { i++; }
    while (str2[j] != '\0' && (str2[j] == ' ' || str2[j] == '\t')) { j++; }

    // ��������� �������� �������� �����
    if (str1[i] == '\0' && str2[j] == '\0') {
        return 0;
    }
    if (str1[i] == '\0') {
        return -1;
    }
    return 1;
}