#include <iostream>
using namespace std;

struct Queue {
	int data;
	Queue* next;
	Queue* prev;
};


//Добавление элемента в конец очереди
Queue* AddToQueueEnd(Queue*& begin, Queue*& end, int value) {
	Queue* temp = new Queue;
	temp->data = value;
	temp->next = nullptr;
	temp->prev = end;

	if (begin == nullptr && end == nullptr) {
		begin = end = temp;
	}
	else {
		end->next = temp;
		temp->prev = end;
		end = temp;
	}

	return temp;
}



//Добавление элемента в начало очереди
Queue* AddToQueueBegin(Queue*& begin, Queue*& end, int value) {
	Queue* temp = new Queue;
	temp->data = value;
	temp->next = begin;
	temp->prev = nullptr;

	if (begin == nullptr && end == nullptr) {
		begin = end = temp;
	}
	else {
		if (begin != nullptr) {
			begin->prev = temp;
		}
		begin = temp;
	}

	return temp;
}


//Просмотр очереди сначала
void ViewBegin(Queue* begin) {
	Queue* temp = begin;
	while (temp != nullptr) {
		cout << temp->data << " ";
		temp = temp->next;
	}
	cout << endl;
}


//Просмотр очереди с конца 
void ViewEnd(Queue* end) {
	Queue* temp = end;
	while (temp != nullptr) {
		cout << temp->data << " ";
		temp = temp->prev;
	}
	cout << endl;
}


//Удаление всех элементов очереди
void DeleteAll(Queue** begin)
{
	Queue* temp = new Queue;
	while (*begin != NULL) {
		temp = *begin;
		*begin = (*begin)->next;
		delete temp;
	}
}


//Удаление каждого 3 элемента
void DeleteEveryThird(Queue*& begin, Queue*& end) {
	Queue* current = begin;
	while (current != nullptr) {
		// Пропускаем два узла, чтобы найти третий
		Queue* temp = current;
		for (int i = 0; i < 2; i++) {
			if (temp == nullptr || temp->next == nullptr) {
				return; // Меньше трёх узлов, выходим
			}
			temp = temp->next;
		}
		// Теперь temp — это третий узел
		Queue* todelete = temp;

		// Обновляем связи (первый узел не удаляется, поэтому prev точно есть)
		todelete->prev->next = todelete->next;
		if (todelete->next != nullptr) {
			todelete->next->prev = todelete->prev;
		}
		else {
			end = todelete->prev; // Обновляем end, если удаляем последний узел
		}

		// Переходим к следующему узлу после удалённого
		current = todelete->next;
		delete todelete;
	}
}


int main() {
	setlocale(LC_ALL, "ru");
	Queue* begin = nullptr;
	Queue* end = nullptr;
	int choice;
	while (true) {
		cout << "1 - Добавить элемент в начало очереди" << endl <<
			"2 - Добавить элемент в конец очереди" << endl <<
			"3 - Просмотр очереди сначала" << endl <<
			"4 - Просмотр очереди с конца" << endl <<
			"5 - Удаление каждого 3 элемента очереди " << endl <<
			"6 - Выход" << endl;

		cin >> choice;

		switch (choice) {

		case 1: {
			int value;
			cout << "Введите значение: ";
			cin >> value;
			AddToQueueBegin(begin, end, value);
			break;
		}
		case 2: {
			int value;
			cout << "Введите значение: ";
			cin >> value;
			AddToQueueEnd(begin, end, value);
			break;
		}

		case 3: {
			ViewBegin(begin);
			break;
		}

		case 4: {
			ViewEnd(end);
			break;
		}

		case 5: {
			DeleteEveryThird(begin, end);
			break;
		}

		case 6: {
			DeleteAll(&begin);
			return 0;
		}
		}
	}
}