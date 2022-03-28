#include <iostream>
using std::cout;
using std::cin;

#include <string>
using std::string;

int main()
{
	string phrase1;
	string phrase2;

	//cout << "Enter a word ";
	//cin >> word1;
	cout << "Enter a phrase ";
	getline(cin, phrase1);


	//cout << "Enter another word ";
	//cin >> word2;
	cout << "Enter another phrase ";
	getline(cin, phrase2);

	if (phrase1.length() == phrase2.length())
	{
		cout << "They are the same length." << '\n';
	}

	if (phrase1.length() > phrase2.length())
	{
		cout << "The first word is longer." << '\n';
	}

	if (phrase1.length() < phrase2.length())
	{
		cout << "The second word is longer." << '\n';
	}

	return 0;
}

