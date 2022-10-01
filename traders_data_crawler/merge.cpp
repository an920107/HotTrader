#include <bits/stdc++.h>
using namespace std;

map<string, set<string>> tradersData;

int main() {

    system("mkdir -p data");

    const string PREFIX = "data/";
    string line, currentId;
    set<string> emptySet;

    freopen("traders_data.txt", "r", stdin);
    while (getline(cin, line)) {
        if (line[0] >= '0' && line[0] <= '9') {
            currentId = line;
            tradersData.insert(make_pair(currentId, emptySet));
        }
        else {
            tradersData[currentId].insert(line);
        }
    }
    cin.clear();

    for (auto p : tradersData) {
        freopen((PREFIX + p.first).c_str(), "r", stdin);
        while (getline(cin, line)) {
            p.second.insert(line);
        }
        cin.clear();
        freopen((PREFIX + p.first).c_str(), "w", stdout);
        for (auto s : p.second) {
            cout << s << '\n';
        }
        cout.clear();
    }
}
