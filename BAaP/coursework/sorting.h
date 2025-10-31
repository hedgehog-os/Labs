#ifndef SORTING_H
#define SORTING_H

#include "replica.h"
#include <fstream>
using namespace std;

// ��������� ������� ����������
void BubbleSortByName(fstream& file, ofstream& report);
void SelectionSortByDialogueBranchName(fstream& file, ofstream& report);
void InsertionSortByID(fstream& file, ofstream& report);
void QuickSortByPhraseLength(Replica arr[], int left, int right);

// ������� ��� ��������� �����
int mystrcmp(const char* str1, const char* str2);

#endif
