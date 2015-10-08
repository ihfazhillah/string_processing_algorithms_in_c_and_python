#include <iostream>
#include <string>

// TODO:
// Read text and pattern from command line.
// Output all indexes instead of true or false.

using namespace std;

string text = "opaoaaaopa";
int n = 10;
int m = 3;
string pat = "opsa";
int pre[3];

void createPrefix() {
    int i = 0;
    int j = -1;
    pre[0] = -1;

    while (i < m) {
        while (j >= 0 && pat[i] != pat[j]) {
            j = pre[j];
        }
        i++;
        j++;
        pre[i] = j;
    }
}

bool kmp() {
    int i = 0;
    int j = 0;
    while (i < n) {
        while (j >= 0 && text[i] != pat[j]) {
            j = pre[j];
        }
        i++;
        j++;
        if (j == m) return true; // match!
    }
    return false;
}

int main() {
    createPrefix();
    std::cout << kmp() << std::endl;
}

