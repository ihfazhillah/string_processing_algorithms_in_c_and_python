/**
 * Example of usage:
 * g++ kmp.cpp -o kmp.out
 * ./kmp.out herself big.txt [big2.txt big3.txt ...]
 */

#include <iostream>
#include <string>
#include <fstream>
#include <vector>

using namespace std;

string text = "";
string pat = "";
int n = -1;
int m = -1;
vector<int> pre;

void createPrefix(string pat) {
    int i = 0;
    int j = -1;

    // Setting M
    m = pat.size();
    pre.resize(m);
    pre[0] = -1;

    while (i < m) {
        while (j >= 0 && pat[i] != pat[j]) {
            j = pre[j];
        }
        i++;
        j++;
        //printf("Assigning %d to pre[%d].", j, i);
        pre[i] = j;
    }
}

int kmp(string pat, string line) {
    int i = 0;
    int j = 0;
    int matches = 0;
    while (i < n) {
        //printf("Pattern size is: %d, %d\n", i, j);
        while (j >= 0 && j <= m && line[i] != pat[j]) {
            j = pre[j];
        }
        i++;
        j++;
        if (j == m) matches++; // match!
    }
    return matches;
}

int kmpInFile(string pat, string fileName) {
    ifstream infile;
    infile.open(fileName);

    int result = 0;
    int lineNr = 0;
    for (string line; getline(infile, line);) {
        lineNr++;
        // Setting N
        n = line.size();
        //printf("Line number %d has size %d.\n", lineNr, n);
        result += kmp(pat, line);
    }
    return result;
}

int main(int argc, char* argv[]) {

    char* pattern = argv[1];
    createPrefix(pattern);

    int result = 0;
    for (int i = 2; i < argc; i++) {
        char* text_filename = argv[i];
        if (text_filename && pattern) {
            //printf("Pattern is: %s\n", pattern.c_str());
            result += kmpInFile(pattern, text_filename);
        }
    }
    cout << result << "\n";

    return 0;
}

