#include <iostream>
using namespace std;

int main() {
	char s = 's';
	void* x = ( void* ) &s;
	char name[7] = {'S','t','e','l','l','a','\0'};
	cout << name << endl;
	return 0;
}
