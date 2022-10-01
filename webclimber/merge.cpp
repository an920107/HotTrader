#include <iostream>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

void reader(const string str, set<string> &se) {
    freopen(str.c_str(), "r", stdin);
    string s;
    while (cin >> s) {
		int index = s.find('?');
		if (index != string::npos)
			s = s.substr(0, index);
        se.insert(s);
    }
    cin.clear();
    fclose(stdin);
}

int main() {
    string line;
    set<string> st;
    reader("hot_traders.txt", st);
    reader("hot_traders_new.txt", st);
    freopen("hot_traders.txt", "w", stdout);
    for (string str : st) {
        cout << str << '\n';
//        cerr << str << '\n';
    }
}

