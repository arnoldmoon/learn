#include <iostream>
#include <string>

using namespace std;

void _reverse(string *s, int l, int r){
    if (l >= r){
        return;
    }
    float mid = (l + r) * 0.5;
    int idx = 0;
    while (l + idx < mid){
        swap(s->at(l + idx), s->at(r - idx));
        idx ++;
    }
    return;
}

void reverse_word_order(string* s) {
    int r = s->length() - 1;
    int l = 0;
    _reverse(s, l, r);
    int idx = 0;
    for (const char &c:*s){
        if (c == ' '){
            _reverse(s, l, idx - 1);
            l = idx + 1;
        }
        idx ++;
    }
    _reverse(s, l, r);
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
