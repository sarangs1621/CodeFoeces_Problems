#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
    int N;
    cin >> N;
    if (N == 1) {
        printf("one");
    } else if (N == 2) {
        printf("two");
    } else if (N == 3) {
        printf("three");
    } else if (N == 4) {
        printf("four");
    } else if (N == 5) {
        printf("five");
    } else if (N == 6) {
        printf("six");
    } else if (N == 7) {
        printf("seven");
    } else if (N == 8) {
        printf("eight");
    } else if (N == 9) {
        printf("nine");
    } else {
        cout << "Greater than 9" << endl;
    }
 
   return 0;
}
