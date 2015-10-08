#include <iostream>
#include <string>

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

bool kmpFind() {
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
    std::cout << kmpFind() << std::endl;
}

