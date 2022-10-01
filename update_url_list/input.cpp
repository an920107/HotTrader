#include <iostream>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

void reader(const string str, set<string> &se) {
    freopen(str.c_str(), "r", stdin);
    string s;
    while (cin >> s) {
		s = s.substr(0, s.find('?'));
        se.insert(s);
    }
    cin.clear();
    fclose(stdin);
}

int main() {
    string line;
    set<string> st;
    reader("url_list.txt", st);
    reader("url_list_new.txt", st);
    freopen("url_list.txt", "w", stdout);
    for (string str : st) {
        cout << str << '\n';
        cerr << str << '\n';
    }
}

