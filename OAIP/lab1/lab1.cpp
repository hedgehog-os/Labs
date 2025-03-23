#include <iostream>
using namespace std;

double rec_function(int step) {
	if (step == 0) {
		return 0;
	}
	return 1 / (1 + rec_function(step - 1));
}


int main() {
	int n;
	cout << "Enter amount of steps: ";
	cin >> n;
	cout << rec_function(n);
}