#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;
string n;
vector<int> list;

int main() {
    int cn = 0;
    int total = 0;
    while(1) {
        getline(cin, n);
        if(n == "quit") break;
        if(n.length() == 0) {
            list.push_back(cn);
            cn = 0;
        } else {
            cn += stoi(n);
        }
    }
    sort(list.rbegin(), list.rend());
    total = list[0] + list[1] + list[2];
    cout << "total: " << total << endl;
}