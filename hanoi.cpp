#include <iostream>
#include <bitset>
#include <vector>

#define MAX_BIT 16

using namespace std;

void
hanoi(const int& n,
      vector< vector< int >* >* tower)
{
    if (n <= 0){
        tower->at(0)->clear();
        tower->at(1)->clear();
        tower->at(2)->clear();
        tower->at(0)->push_back(0);
        tower->at(1)->push_back(0);
        tower->at(2)->push_back(0);
        return;
    }
    
    hanoi(n-1, tower);
    int prev_seq_size = tower->at(0)->size();

    // for now ignore the largest disc,
    // use n-1 sequence and move whole tower to middle pole.
    swap(tower->at(1), tower->at(2));

    // again move whole tower to target pole.
    for(int i=0; i<prev_seq_size; ++i){
        tower->at(0)->push_back(tower->at(2)->at(i));
        tower->at(1)->push_back(tower->at(0)->at(i));
        tower->at(2)->push_back(tower->at(1)->at(i));
    }

    // sneak in the largest disc under n-1 tower and we are done.
    for(int i=0; i<prev_seq_size; ++i){
        (tower->at(0)->at(i)) |= (1 << (n - 1));
        (tower->at(2)->at(i+prev_seq_size)) |= (1 << (n - 1));
    }
    
    for(size_t i=0; i<tower->at(0)->size(); ++i){
        std::cout << bitset<MAX_BIT>(tower->at(0)->at(i)) << "\t"; 
        std::cout << bitset<MAX_BIT>(tower->at(1)->at(i)) << "\t"; 
        std::cout << bitset<MAX_BIT>(tower->at(2)->at(i)) << "\t"; 

        std::cout << std::endl;
    }
    std::cout << std::endl;
    return;
}

int main(){
    vector< int > tower_a(0);
    vector< int > tower_b(0);
    vector< int > tower_c(0);
    vector< vector<int>* > tower{&tower_a, &tower_b, &tower_c};
    hanoi(3, &tower);
    return 0;
}
