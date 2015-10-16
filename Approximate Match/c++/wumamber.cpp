/**
 * Example of usage:
 * g++ wumamber.cpp -o wumamber.out
 * ./wumamber.out herself 2 big.txt [big2.txt big3.txt ...]
 */

#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <map>

using namespace std;

map<char, int> charMaskMap;

void charMask(map<char, int>& charMask, string pattern, string alph) {
    charMask.clear();
    int one = 1;
    int pos_mask=~one;
    for (int i = 0 ; i < alph.length(); i++) {
        charMask[alph[i]] = ~0;
    }
    for (int i = 0; i < pattern.length(); i++) {
        charMask[pattern[i]] &= pos_mask;
        pos_mask = (pos_mask<<1) | one;
    }
    //for(auto it = charMask.cbegin(); it != charMask.cend(); ++it) {
            //std::cout << it->first << " " << it->second << "\n";
    //}
}

string createAlphabet() {
    // From 0 to z.
    string alphabet = "";
    for (int i = 0; i < 256; i++) {
        alphabet += '0' + i;
    }
    return alphabet;
}

int wumamber(string fileName, string pattern, string alph, int err) {
    charMask(charMaskMap, pattern, alph);
    int m = pattern.size();
    int msb = 1<<(m-1);

    vector<int> s;
    s.push_back(((1<<m)-1));
    string occ="";

    for (int i = 1; i <= err; i++) {
        s.push_back(s[i-1]<<1);
    }
    //for(auto it = s.cbegin(); it != s.cend(); ++it) {
            //std::cout << *it << "\n";
    //}
    ifstream infile;
    infile.open(fileName.c_str());

    int temp1;
    int temp2;
    for (string line; getline(infile, line);) {
        for (int i = 0; i < line.size(); i++) {
            char letter = line[i];
            temp1 = s[0];
            s[0] = (s[0] << 1) | charMaskMap[letter];
            for (int j = 1; j <= err; j++) {
                temp2 = s[j];
                s[j]=((s[j]<<1) | charMaskMap[letter]) & (temp1<<1) & (s[j-1]<<1) & temp1;
                temp1 = temp2;
            }
            if (((s[err] & ((1<<m)-1)))<msb) {
                occ += i;
            }
        }
    }
    return occ.size();
}
int main(int argc, char* argv[]) {
    string alph = createAlphabet();
    char* pattern = argv[1];
    int err = atoi(argv[2]);
    int result = 0;
    for (int i = 3; i < argc; i++) {
        char* text_filename = argv[3];
        if (text_filename && pattern) {
            //printf("Pattern is: %s\n", pattern.c_str());
            result += wumamber(text_filename, pattern, alph, err);
        }
    }
    cout << result << "\n";

    return 0;

}
