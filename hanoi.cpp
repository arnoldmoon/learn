#include <iostream>
#include <bitset>
#include <vector>

#define MAX_BIT 16

using namespace std;

void
hanoi(const int& n,
        vector< bitset<MAX_BIT>* >* tower_a,
        vector< bitset<MAX_BIT>* >* tower_b,
        vector< bitset<MAX_BIT>* >* tower_c){
    if (n <= 0){
        tower_a->clear();
        tower_b->clear();
        tower_c->clear();
        tower_a->push_back(new bitset<MAX_BIT>(0));
        tower_b->push_back(new bitset<MAX_BIT>(0));
        tower_c->push_back(new bitset<MAX_BIT>(0));
        return;
    }
    hanoi(n-1, tower_a, tower_b, tower_c);
    auto new_tower_a = new vector< bitset<MAX_BIT>* >();   
    auto new_tower_b = new vector< bitset<MAX_BIT>* >();   
    auto new_tower_c = new vector< bitset<MAX_BIT>* >();   
    for(auto i:*tower_a){
        auto new_i = new bitset<MAX_BIT>(*i);
        *new_i |= 1 << (n - 1); 
        new_tower_a->push_back(new_i);
    }
    for(auto i:*tower_c){
        new_tower_b->push_back(new bitset<MAX_BIT>(*i));
    }
    for(auto i:*tower_b){
        new_tower_c->push_back(new bitset<MAX_BIT>(*i));
    }
    
    for(auto i:*tower_b){
        new_tower_a->push_back(new bitset<MAX_BIT>(*i));
    }
    for(auto i:*tower_a){
        new_tower_b->push_back(new bitset<MAX_BIT>(*i));
    }
    for(auto i:*tower_c){
        auto new_i = new bitset<MAX_BIT>(*i);
        *new_i |= 1 << (n - 1); 
        new_tower_c->push_back(new_i);
    }

    for(size_t i=0; i<new_tower_a->size();++i){
        std::cout << *(new_tower_a->at(i)) << "\t"; 
        std::cout << *(new_tower_b->at(i)) << "\t"; 
        std::cout << *(new_tower_c->at(i)) << "\t"; 
        std::cout << std::endl;
    }
    std::cout << std::endl;
}

int main(){
    vector< bitset<MAX_BIT>* > tower_a(0);
    vector< bitset<MAX_BIT>* > tower_b(0);
    vector< bitset<MAX_BIT>* > tower_c(0);
    hanoi(2, &tower_a, &tower_b, &tower_c);
    return 0;
}
