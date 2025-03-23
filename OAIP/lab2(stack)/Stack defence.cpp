#include <iostream>
using namespace std;

struct Stack {
    int data;
    Stack* next;
};

Stack* AddToStack(Stack* top, int in) {
    Stack* temp = new Stack; // Локальная переменная
    temp->data = in;
    temp->next = top;
    return temp;
}

void View(Stack* top) {
    Stack* temp = top; // Локальная переменная
    while (temp != nullptr) {
        cout << temp->data << " ";
        temp = temp->next;
    }
    cout << endl; // Для корректного отображения
}

Stack* DeleteEverySecond(Stack* top) {
    if (top == nullptr || top->next == nullptr) {
        // Если список пустой или в нем только один элемент, возвращаем его.
        return top;
    }

    Stack* current = top;
    Stack* toDelete = nullptr;

    while (current != nullptr && current->next != nullptr) {
        toDelete = current->next;
        current->next = toDelete->next; // Пропускаем удаляемый элемент
        delete toDelete;
        current = current->next; // Переходим к следующему элементу
    }

    return top;
}

int main() {
    setlocale(LC_ALL, "ru");
    int amount, n;
    Stack* begin = nullptr;

    cout << "Введите количество новых элементов в стеке: ";
    cin >> amount;

    if (amount <= 0) {
        cout << "Количество элементов должно быть больше нуля!" << endl;
        return 0;
    }

    cout << "Введите элементы: ";
    for (int i = 0; i < amount; i++) {
        cin >> n;
        begin = AddToStack(begin, n);
    }

    cout << "Стек до удаления: ";
    View(begin);

    begin = DeleteEverySecond(begin); // Удаляем каждый второй элемент

    cout << "Стек после удаления каждого второго элемента: ";
    View(begin);

    return 0;
}
