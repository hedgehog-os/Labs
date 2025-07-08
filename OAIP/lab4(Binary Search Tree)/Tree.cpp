#include <iostream>
#include <string>
using namespace std;

const int maxsize = 100;

struct Tree {
    int data;
    string comment;
    Tree* left;
    Tree* right;

    Tree(int value, string cmt = "") : data(value), comment(cmt), left(nullptr), right(nullptr) {}
};

void Insert(Tree*& node, int value, string comment = "") {
    if (!node) {
        node = new Tree(value, comment);
    }
    else if (value < node->data) {
        Insert(node->left, value, comment);
    }
    else if (value > node->data) {
        Insert(node->right, value, comment);
    }
}

bool Search(Tree* node, int value) {
    if (!node) return false;
    if (node->data == value) {
        cout << "Информацонная часть: " << node->comment << endl;
        return true;
    }
    if (value < node->data) return Search(node->left, value);
    return Search(node->right, value);
}

Tree* FindMin(Tree* node) {
    if (!node) return nullptr;
    while (node->left) node = node->left;
    return node;
}

Tree* Remove(Tree* node, int value) {
    if (!node) return nullptr;

    if (value < node->data) {
        node->left = Remove(node->left, value);
    }
    else if (value > node->data) {
        node->right = Remove(node->right, value);
    }
    else {
        if (!node->left) {
            Tree* temp = node->right;
            delete node;
            return temp;
        }
        else if (!node->right) {
            Tree* temp = node->left;
            delete node;
            return temp;
        }
        else {
            Tree* temp = FindMin(node->right);
            node->data = temp->data;
            node->comment = temp->comment;
            node->right = Remove(node->right, temp->data);
        }
    }
    return node;
}

void InOrderTraversal(Tree* node) {
    if (node) {
        InOrderTraversal(node->left);
        cout << node->data << " (" << node->comment << ") ";
        InOrderTraversal(node->right);
    }
}

void PreOrderTraversal(Tree* node) {
    if (node) {
        cout << node->data << " (" << node->comment << ") ";
        PreOrderTraversal(node->left);
        PreOrderTraversal(node->right);
    }
}

void PostOrderTraversal(Tree* node) {
    if (node) {
        PostOrderTraversal(node->left);
        PostOrderTraversal(node->right);
        cout << node->data << " (" << node->comment << ") ";
    }
}

void DeleteTree(Tree* node) {
    if (node) {
        DeleteTree(node->left);
        DeleteTree(node->right);
        delete node;
    }
}

void CollectNodes(Tree* node, int* values, string* comments, int& index) {
    if (node) {
        CollectNodes(node->left, values, comments, index);
        values[index] = node->data;
        comments[index] = node->comment;
        index++;
        CollectNodes(node->right, values, comments, index);
    }
}

int RemoveDuplicates(int* values, string* comments, int n) {
    if (n == 0) return 0;
    int newSize = 1;
    for (int i = 1; i < n; ++i) {
        if (values[i] != values[newSize - 1]) {
            values[newSize] = values[i];
            comments[newSize] = comments[i];
            ++newSize;
        }
    }
    return newSize;
}

void BuildFromArray(int* values, string* comments, int n, Tree*& root) {
    for (int i = 0; i < n; ++i) {
        Insert(root, values[i], comments[i]);
    }
}

Tree* BuildBalanced(int* values, string* comments, int left, int right) {
    if (left > right) return nullptr;
    int mid = (left + right) / 2;
    Tree* node = new Tree(values[mid], comments[mid]);
    node->left = BuildBalanced(values, comments, left, mid - 1);
    node->right = BuildBalanced(values, comments, mid + 1, right);
    return node;
}

Tree* BalanceTree(Tree* root) {
    int values[maxsize];
    string comments[maxsize];
    int index = 0;
    CollectNodes(root, values, comments, index);
    int n = RemoveDuplicates(values, comments, index);
    DeleteTree(root);

    return BuildBalanced(values, comments, 0, n - 1);
}

int CountRightSubtree(Tree* node) {
    if (!node) return 0;
    return 1 + CountRightSubtree(node->left) + CountRightSubtree(node->right);
}

void PrintTree(Tree* node, int depth = 0) {
    if (node) {
        PrintTree(node->right, depth + 1);
        for (int i = 0; i < depth; ++i) cout << "   ";
        cout << node->data << endl;
        PrintTree(node->left, depth + 1);
    }

    if (depth == 0) { // Когда достигли корня, выводим обходы
        cout << "\nПрямой обход (PreOrder): ";
        PreOrderTraversal(node);  // корень -> левое -> правое
        cout << "\nСимметричный обход (InOrder): ";
        InOrderTraversal(node);  // левое -> корень -> правое
        cout << "\nОбратный обход (PostOrder): ";
        PostOrderTraversal(node);  // левое -> правое -> корень
        cout << endl;
    }
}



void ShowMenu() {
    cout << "\nМеню:\n";
    cout << "1. Добавить элемент в дерево\n";
    cout << "2. Удалить элемент из дерева\n";
    cout << "3. Найти элемент в дереве\n";
    cout << "4. Вывести дерево\n";
    cout << "5. Сбалансировать дерево\n";
    cout << "6. Подсчитать количество узлов в правом поддереве\n";
    cout << "7. Очистить дерево\n";
    cout << "8. Выход\n";
    cout << "Выберите опцию (1-8): ";
}

int main(int argc, char* argv[]) {
    setlocale(LC_ALL, "ru");
    Tree* root = nullptr;
    int choice, value, n;
    int values[maxsize];
    string comments[maxsize];
    string comment;

    cout << "Хотите создать дерево из массива? (1 - да, 0 - нет): ";
    cin >> choice;
    if (choice == 1) {
        cout << "Введите количество элементов (не больше " << maxsize << "): ";
        cin >> n;
        if (n > maxsize || n < 0) {
            cout << "Недопустимое количество элементов!\n";
            return 1;
        }
        cout << "Введите " << n << " чисел и комментарии к ним:\n";
        for (int i = 0; i < n; i++) {
            cout << "Значение: ";
            cin >> values[i];
            cout << "Комментарий: ";
            cin.ignore();
            getline(cin, comments[i]);
        }
        BuildFromArray(values, comments, n, root);
        cout << "Дерево создано.\n";
    }

    while (true) {
        ShowMenu();
        cin >> choice;

        if (choice == 8) {
            break;
        }

        switch (choice) {
        case 1:
            cout << "Введите значение для добавления: ";
            cin >> value;
            cout << "Введите комментарий: ";
            cin.ignore();
            getline(cin, comment);
            Insert(root, value, comment);
            cout << "Элемент " << value << " добавлен.\n";
            break;

        case 2:
            cout << "Введите значение для удаления: ";
            cin >> value;
            if (Search(root, value)) {
                root = Remove(root, value);
                cout << "Элемент " << value << " удалён.\n";
            }
            else {
                cout << "Элемент " << value << " не найден в дереве.\n";
            }
            break;

        case 3:
            cout << "Введите значение для поиска: ";
            cin >> value;
            if (Search(root, value)) {
                cout << "Элемент " << value << " найден в дереве.\n";
            }
            else {
                cout << "Элемент " << value << " не найден в дереве.\n";
            }
            break;

        case 4:
            if (!root) {
                cout << "Дерево пусто.\n";
            }
            else {
                PrintTree(root);
            }
            break;

        case 5:
            if (!root) {
                cout << "Дерево пусто, нечего балансировать.\n";
            }
            else {
                root = BalanceTree(root);
                cout << "Дерево сбалансировано.\n";
            }
            break;

        case 6:
            if (!root) {
                cout << "Дерево пусто.\n";
            }
            else {
                cout << "Количество узлов в правом поддереве: " << CountRightSubtree(root->right) << endl;
            }
            break;

        case 7:
            DeleteTree(root);
            root = nullptr;
            cout << "Дерево очищено.\n";
            break;

        default:
            cout << "Неверный выбор! Пожалуйста, выберите опцию от 1 до 8.\n";
            break;
        }
    }

    DeleteTree(root);
    cout << "Программа завершена.\n";
    return 0;
}
