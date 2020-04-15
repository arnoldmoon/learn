#include <iostream>

using std::cout;
using std::endl;

namespace {

uint64_t
add(uint64_t a, uint64_t b){
    while (b){
        uint64_t c = (a & b) << 1;
        a ^= b;
        b = c;
    }
    return a;
}

} // namespace

int main(){
    cout << 2 << " + " << 3 << " = "
         << add(2, 3) << endl;
    return 0;
}
