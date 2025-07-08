#include <iostream>
#include <iomanip>
#include <cstring>

struct Car {
    char brand[100];
    int maxspeed;
    int year;
};

// Инициализация таблицы
void initialize(Car* hashtable, int tablesize) {
    for (int i = 0; i < tablesize; ++i) {
        hashtable[i].maxspeed = -1;  // метка пустого
        hashtable[i].year = -1;
        hashtable[i].brand[0] = '\0';
    }
}

// Двойное хеширование: вставка
void insertCar(const Car& car, Car* hashtable, int tablesize) {
    int i = car.maxspeed % tablesize;
    if (hashtable[i].maxspeed == -1) {
        hashtable[i] = car;
        return;
    }
    int step = 1 + (car.maxspeed % (tablesize - 2));
    int attempts = 0;
    while (attempts < tablesize) {
        i = (i - step + tablesize) % tablesize;
        if (hashtable[i].maxspeed == -1) {
            hashtable[i] = car;
            return;
        }
        attempts++;
    }
    std::cout << "Хеш-таблица переполнена!" << std::endl;
}

// Поиск по максимальной скорости
int findIndex(int maxspeed, Car* hashtable, int tablesize) {
    int i = maxspeed % tablesize;
    if (hashtable[i].maxspeed == maxspeed) return i;

    int step = 1 + (maxspeed % (tablesize - 2));
    int attempts = 0;
    while (attempts < tablesize) {
        i = (i - step + tablesize) % tablesize;
        if (hashtable[i].maxspeed == maxspeed) return i;
        if (hashtable[i].maxspeed == -1) break;  // пустой — дальше нет
        attempts++;
    }
    return -1;
}

void searchCar(int maxspeed, Car* hashtable, int tablesize) {
    int idx = findIndex(maxspeed, hashtable, tablesize);
    if (idx >= 0) {
        std::cout << "Машина найдена!" << std::endl;
        std::cout << "| " << std::left << std::setw(15) << "Марка"
            << "| " << std::setw(6) << "Год"
            << "| " << std::setw(8) << "Макс. скор." << "|" << std::endl;
        std::cout << std::string(40, '-') << std::endl;
        std::cout << "| " << std::setw(15) << hashtable[idx].brand
            << "| " << std::setw(6) << hashtable[idx].year
            << "| " << std::setw(8) << hashtable[idx].maxspeed << "|" << std::endl;
    }
    else {
        std::cout << "Машина не найдена :(" << std::endl;
    }
}

void deleteCar(int maxspeed, Car* hashtable, int tablesize) {
    int idx = findIndex(maxspeed, hashtable, tablesize);
    if (idx >= 0) {
        hashtable[idx].maxspeed = -1;
        hashtable[idx].year = -1;
        hashtable[idx].brand[0] = '\0';
        std::cout << "Машина удалена." << std::endl;
    }
    else {
        std::cout << "Машина для удаления не найдена." << std::endl;
    }
}

void displayTable(Car* hashtable, int tablesize) {
    std::cout << "Индекс | " << std::left << std::setw(15) << "Марка"
        << "| " << std::setw(6) << "Год"
        << "| " << std::setw(8) << "Макс. скор." << "|" << std::endl;
    std::cout << std::string(50, '=') << std::endl;
    for (int i = 0; i < tablesize; ++i) {
        std::cout << std::setw(6) << i << " | ";
        if (hashtable[i].maxspeed != -1) {
            std::cout << std::setw(15) << hashtable[i].brand << "| "
                << std::setw(6) << hashtable[i].year << "| "
                << std::setw(8) << hashtable[i].maxspeed << "|";
        }
        else {
            std::cout << std::setw(15) << "-" << "| "
                << std::setw(6) << "-" << "| "
                << std::setw(8) << "-" << "|";
        }
        std::cout << std::endl;
    }
}

int main() {
    setlocale(LC_ALL, "ru");
    int tablesize;
    std::cout << "Введите размер хеш-таблицы: ";
    std::cin >> tablesize;
    Car* hashtable = new Car[tablesize];
    initialize(hashtable, tablesize);

    int choice;
    do {
        std::cout << "\nМеню:\n";
        std::cout << "1. Вставить машину\n";
        std::cout << "2. Найти машину\n";
        std::cout << "3. Удалить машину\n";
        std::cout << "4. Показать таблицу\n";
        std::cout << "5. Выход\n";
        std::cout << "Ваш выбор: ";
        std::cin >> choice;

        switch (choice) {
        case 1: {
            Car car;
            std::cout << "Введите марку: ";
            std::cin >> std::setw(100) >> car.brand;
            std::cout << "Введите год выпуска: ";
            std::cin >> car.year;
            std::cout << "Введите макс. скорость: ";
            std::cin >> car.maxspeed;
            insertCar(car, hashtable, tablesize);
            break;
        }
        case 2: {
            int speed;
            std::cout << "Введите макс. скорость для поиска: ";
            std::cin >> speed;
            searchCar(speed, hashtable, tablesize);
            break;
        }
        case 3: {
            int speed;
            std::cout << "Введите макс. скорость для удаления: ";
            std::cin >> speed;
            deleteCar(speed, hashtable, tablesize);
            break;
        }
        case 4:
            displayTable(hashtable, tablesize);
            break;
        case 5:
            std::cout << "Выход..." << std::endl;
            break;
        default:
            std::cout << "Неверный выбор, попробуйте снова." << std::endl;
        }
    } while (choice != 5);

    delete[] hashtable;
    return 0;
}
