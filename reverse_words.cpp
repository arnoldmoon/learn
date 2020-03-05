#include <iostream>
#include <string>

using namespace std;

void _reverse(string *s, int l, int r){
    // if (l >= r){
    //     return;
    // }
    while (l < r){
        swap(s->at(l), s->at(r));
        l ++;
        r --;
    }
    return;
}

void reverse_word_order(string* s) {
    _reverse(s, 0, s->length() - 1);
    int l = 0;
    int r = 0;
    for (const char &c:*s){
        if (c == ' '){
            _reverse(s, l, r - 1);
            l = r + 1;
        }
        r ++;
    }
    _reverse(s, l, r - 1);
    return;
}

int main() {
    string input;
    input = "to be or not to be.";
    cout << input << endl;
    reverse_word_order(&input);
    cout << input << endl;
    return 1;
}
