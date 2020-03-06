#include <iostream>
#include <bitset>
#include <limits>

using namespace std;

#define bit_length(t) numeric_limits<t>::is_signed\
                      ? numeric_limits<t>::digits + 1\
                      : numeric_limits<t>::digits

template <class t>
bitset<bit_length(t)> complement(t input){
    return ~bitset<bit_length(t)>(input);
}

template <class t>
short parity(t input){
    int i = bit_length(t);
    while (i > 1){
        i *= 0.5;
        input ^= (input >> i);
    }
    return input & 1;
}

int main(){
    long i;
    i = 5;
    cout << "input      : " << bitset <bit_length(long)>(i) << endl;
    cout << "complement : " << complement(i) << endl;
    cout << "parity     : " << parity(i) << endl;
    i = 4;
    cout << "input      : " << bitset <bit_length(long)>(i) << endl;
    cout << "complement : " << complement(i) << endl;
    cout << "parity     : " << parity(i) << endl;
    return 0;
}