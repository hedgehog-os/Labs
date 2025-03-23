#include <iostream>
#include <random>
using namespace std;

struct Stack
{
	int data;
	Stack* next;
} *stackbegin = nullptr, * temp = nullptr;


Stack* AddToStack(Stack* top, int in)
{
	temp = new Stack;
	temp->data = in;
	temp->next = top;
	return temp;
}


void View(Stack* top)
{
	temp = top;
	while (temp != NULL)
	{
		cout << temp->data << " ";
		temp = temp->next;
	}
}


void DeleteAll(Stack** top)
{
	while (*top != NULL) {
		temp = *top;
		*top = (*top)->next;
		delete temp;
	}
}


void DeleteOddNums(Stack** top) {

	while (*top != nullptr && (*top)->data % 2 != 0) {
		temp = *top;
		*top = (*top)->next;
		delete temp;
	}

	Stack* current = *top;
	Stack* prev = nullptr;


	while (current != nullptr) {
		if (current->data % 2 != 0) {

			if (prev != nullptr) {
				prev->next = current->next;
			}
			delete current;

			if (prev != nullptr) {
				current = prev->next;
			}
			else {
				current = *top;
			}

		}
		else {
			prev = current;
			current = current->next;
		}
	}
}


Stack* SortStack(Stack* top) {
	if (top == nullptr) {
		return nullptr;
	}


	Stack* index = nullptr;
	int number;


	for (temp = top; temp != nullptr; temp = temp->next) {

		for (index = temp->next; index != nullptr; index = index->next) {
			if (temp->data > index->data) {
				number = temp->data;
				temp->data = index->data;
				index->data = number;
			}
		}
	}

	return top;
}


void main() {
	setlocale(LC_ALL, "ru");
	int n, in, amount;


	while (true) {

		cout << "\n1 - Добавить элементы в стек\n2 - Просмотр стека\n3 - Удалить нечетные элементы стека\n4 - Отсортировтаь стек\n0 - Выход\n";
		cin >> n;


		switch (n)
		{


		case 1: {
			cout << "Введите количество новых элементов в стеке: ";
			cin >> amount;
			for (int i = 0; i < amount; i++) {
				in = rand() % 101 - 50;
				stackbegin = AddToStack(stackbegin, in);
			}
			break;
		}


		case 2: {
			View(stackbegin);
			break;
		}


		case 3: {
			DeleteOddNums(&stackbegin);
			break;
		}


		case 4: {
			SortStack(stackbegin);
			break;
		}

		case 0: {
			if (stackbegin != NULL)
				DeleteAll(&stackbegin);
			return;
		}

		default:
			cout << "Некорректный выбор, попробуйте еще...";
			break;
		}
	}


	return;
}