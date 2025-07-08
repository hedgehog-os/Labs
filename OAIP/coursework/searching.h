#ifndef SEARCHING_H
#define SEARCHING_H

#include "replica.h"
#include <fstream>
using namespace std;

// Прототипы функций поиска
void SearchByName(fstream& file, ofstream& report, char name[maxsize]);
void BinarySearchByID(fstream& file, ofstream& report, int searchID);
void SearchReplicas(fstream& file, ofstream& report, char name[maxsize]);
void EditReplica(fstream& file, ofstream& report, int edit_id);
void DialogueScheme(fstream& file, ofstream& report);
void InterpolationSearchByID(fstream& file, ofstream& report, int searchID);
void GroupByName(fstream& file, ofstream& report, int len);

int lenchar(const char* array);

#endif
