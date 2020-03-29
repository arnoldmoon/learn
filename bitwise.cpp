#include <iostream>
#include <bitset>
#include <limits>

using std::cout;
using std::endl;
using std::numeric_limits;
using std::bitset;

#define bit_length(t) numeric_limits<t>::is_signed\
                      ? numeric_limits<t>::digits + 1\
                      : numeric_limits<t>::digits

template <class t>
bitset<bit_length(t)>
complement(t input) {
    return ~bitset<bit_length(t)>(input);
}

template <class t>
int
parity(t input) {
    int i = bit_length(t);
    while (i > 1) {
        i *= 0.5;
        input ^= (input >> i);
    }
    return input & 1;
}


bool
is_power_of_two(int x) {
    return (x & (x - 1)) == 0;
}


int64_t
propagate_right_most_on_to_lesser(int64_t x) {
    return x | (x - 1);
}


int
mod_of_power_of_two(int x, int y) {
    return x  & (y - 1);
}


uint64_t
get_quotient(uint64_t x, uint64_t y) {
    uint64_t q = 0;
    int k = bit_length(uint64_t);
    while (x > y) {
        while (x < (y << k)) {
            --k;
        }
        x -= y << k;
        q += 1 << k;
    }
    // cout << "%= " << x << endl;
    return q;
}


int main() {
    int64_t i;
    i = 5;
    cout << "input      : " << bitset<bit_length(int64_t)>(i) << endl;
    cout << "complement : " << complement(i) << endl;
    cout << "parity     : " << parity(i) << endl;
    i = 4;
    cout << "input      : " << bitset<bit_length(int64_t)>(i) << endl;
    cout << "complement : " << complement(i) << endl;
    cout << "parity     : " << parity(i) << endl;
    cout << endl;
    cout << "is power of two : 2 " << is_power_of_two(2) << endl;
    cout << "is power of two : 6 " << is_power_of_two(6) << endl;
    cout << "is power of two : 8 " << is_power_of_two(8) << endl;
    cout << endl;
    cout << "input      : " << bitset<bit_length(int64_t)>(20) << endl;
    cout << "propagate->: " << bitset<bit_length(int64_t)>(
                               propagate_right_most_on_to_lesser(20)) << endl;
    cout << endl;
    cout << 70 << " % " << 64 << " = " << mod_of_power_of_two(70, 64) << endl;
    cout << 70 << " % " << 64 << " = " << (70 % 64) << endl;
    cout << 77 << " % " << 16 << " = " << mod_of_power_of_two(77, 16) << endl;
    cout << 77 << " % " << 16 << " = " << (77 % 16) << endl;

    cout << 10 << " / " << 3 << " = " << get_quotient(10, 3) << endl;
    cout << 200 << " / " << 3 << " = " << get_quotient(200, 3) << endl;
    return 0;
}
