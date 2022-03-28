#include <iostream>
using std::cout;

int main()
{
	cout << "Hello!" << '\n' << 2 + 2;

	cout << '\n' << '\n';

	int i;
	//fractional part will be lost
	i = 4.9;
	i = static_cast<int>(4.9);
	cout << i << '\n';

	auto  j = 5;
	cout << j << '\n';

	auto f = 4.9;
	j = f;
	j = static_cast<int>(f);
	cout << f << '\n';
	f = 9 / 5;
	cout << f << '\n';
	f = 9.0 / 5;
	cout << f << '\n';

	return 0;
}

