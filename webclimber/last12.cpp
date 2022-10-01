#include <bits/stdc++.h>
using namespace std;

int main() {
    string line;
    freopen("hot_traders_new.txt", "r", stdin);
    freopen("last_12_id", "w", stdout);
    while (getline(cin, line)) {
        for (int i = 0; i < line.length() - 1; i ++) {
            if (line[i] == '/' && line[i + 1] >= '0' && line[i + 1] <= '9') {
                cout << line.substr(i + 1, line.length() - i - 2) << '\n';
                break;
            }
        }
    }
}
