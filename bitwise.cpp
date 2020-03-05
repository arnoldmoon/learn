#include <iostream>
#include <bitset>
#include <limits>

using namespace std;

#define bit_length(t) numeric_limits<t>::is_signed\
                      ? numeric_limits<t>::digits + 1\
                      : numeric_limits<t>::digits

template <class t>
bitset<bit_length(t)> comp(t input){
    return ~bitset<bit_length(t)>(input);
}

template <class t>
short parity(t input){
    const short l = bit_length(t);
    bitset<l> bs(input);
    int i = l;
    while (i > 1){
        i *= 0.5;
        bs ^= (bs >> i);
    }
    return bs[0];
}

int main(){
    long i;
    i = 5;
    cout << "input      : " << bitset <bit_length(long)>(i) << endl;
    cout << "compliment : " << comp(i) << endl;
    cout << "parity     : " << parity(i) << endl;
    i = 4;
    cout << "input      : " << bitset <bit_length(long)>(i) << endl;
    cout << "compliment : " << comp(i) << endl;
    cout << "parity     : " << parity(i) << endl;
    return 1;
}