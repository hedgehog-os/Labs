#include <iostream>
#include <cmath>

double compute_y(int n) {
	double result = sqrt(n);
	for (int k = n - 1; k >= 1; --k) {
		result = sqrt(k + result);
	}
	return result;
}

int main() {
	int n;
	std::cout << "Введите положительное целое число n: ";
	std::cin >> n;
	double y = compute_y(n);
	std::cout << "y(" << n << ") = " << y << std::endl;
	return 0;
}