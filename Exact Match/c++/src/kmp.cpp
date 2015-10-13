/**
 * Example of usage:
 * g++ kmp.cpp -o kmp.out
 * ./kmp.out -t big.txt -p herself
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

char* getCmdOption(char ** begin, char ** end, const string & option) {
    char ** itr = find(begin, end, option);
    if (itr != end && ++itr != end) {
        return *itr;
    }
    return 0;
}

bool cmdOptionExists(char** begin, char** end, const string & option) {
    return find(begin, end, option) != end;
}

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
    createPrefix(pat);

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

int main(int argc, char * argv[]) {
    char * text_filename = getCmdOption(argv, argv + argc, "-t");
    char * pattern = getCmdOption(argv, argv + argc, "-p");

    if (text_filename && pattern) {
        //printf("Pattern is: %s\n", pattern.c_str());
        cout << kmpInFile(pattern, text_filename) << "\n";
    }
    return 0;
}
