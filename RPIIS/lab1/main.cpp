#include "BinarySearchTree.h"
#include <iostream>
#include <vector>

using namespace std;

void DisplayMenu() {
	cout << "���� �������� � �������� ������� ������:\n";
	cout << "1. �������� ����\n";
	cout << "2. ����� ����\n";
	cout << "3. ������� ����\n";
	cout << "4. ������������ (in-order) �����\n";
	cout << "5. ������ (pre-order) �����\n";
	cout << "6. �������� (post-order) �����\n";
	cout << "7. ��������� ������ �� �������\n";
	cout << "8. �������� ������\n";
	cout << "9. �����\n";
	cout << "������� ��� �����: ";
}

int main() {
	setlocale(LC_ALL, "ru");
	BinarySearchTree tree;
	int choice;
	int value;
	vector<int> values;

	do {
		DisplayMenu();
		cin >> choice;

		switch (choice) {
		case 1:
			cout << "������� �������� ��� �������: ";
			cin >> value;
			tree.Insert(value);
			cout << "�������� ���������.\n";
			break;
		case 2:
			cout << "������� �������� ��� ������: ";
			cin >> value;
			if (tree.Search(value)) {
				cout << "�������� " << value << " ������� � ������.\n";
			}
			else {
				cout << "�������� " << value << " �� ������� � ������.\n";
			}
			break;
		case 3:
			cout << "������� �������� ��� ��������: ";
			cin >> value;
			tree.Remove(value);
			cout << "�������� ������� (���� ��� ������������).\n";
			break;
		case 4:
			cout << "������������ (in-order) �����: ";
			tree.InOrderTraversal();
			break;
		case 5:
			cout << "������ (pre-order) �����: ";
			tree.PreOrderTraversal();
			break;
		case 6:
			cout << "�������� (post-order) �����: ";
			tree.PostOrderTraversal();
			break;
		case 7:
			cout << "������� ���������� ���������: ";
			int n;
			cin >> n;
			values.clear();
			values.resize(n);
			cout << "������� " << n << " ���������: ";
			for (int i = 0; i < n; ++i) {
				cout << "������� ������� " << i + 1 << ": ";
				cin >> values[i];
			}
			tree.BuildFromArray(values);
			cout << "������ ��������� �� �������.\n";
			break;
		case 8:
			tree.Clear();
			cout << "������ �������.\n";
			break;
		case 9:
			cout << "�����...\n";
			break;
		default:
			cout << "������������ �����. ����������, ���������� �����.\n";
			break;
		}
	} while (choice != 9);

	return 0;
}