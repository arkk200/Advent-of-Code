#include <iostream>

using namespace std;

int main() {
    int total = 0;
    int a, b, c, d;
    while(true) {
        scanf("%d-%d,%d-%d", &a, &b, &c, &d);
        if(a == -1) break;
        if(
            (min(c, d) <= a && a <= max(c, d)) ||
            (min(c, d) <= b && b <= max(c, d)) || 
            (min(a, b) <= c && c <= max(a, b)) ||
            (min(a, b) <= d && d <= max(a, b))
        ) {
            total++;
        }
    }
    cout << total << endl;
}