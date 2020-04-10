#include <iostream>
#pragma pack(push, 1)

class EmptyClass{
};

class PureVirtual{
 public:
    int i;
    virtual void my_class() = 0;
};

class PureVirtualDerived : public PureVirtual {
 public:
    char i;
    void my_class() override {
        return;
    }
};

#pragma pack(pop)
class Virtual {
 public:
    int i;
    virtual void my_class() {
        return;
    }
};

class VirtualDerived : public Virtual {
    char* j;
    void my_class() override {
        return;
    }
};

class Normal {
 public:
    char j;
};

int main() {
    std::cout << std::endl;
    std::cout << "EmptyClass        :" << sizeof(EmptyClass) << std::endl;
    std::cout << "PureVirtual       :" << sizeof(PureVirtual) << std::endl;
    std::cout << "PureVirtualDerived:" << sizeof(PureVirtualDerived) << std::endl;
    std::cout << "Virtual           :" << sizeof(Virtual) << std::endl;
    std::cout << "VirtualDerived    :" << sizeof(VirtualDerived) << std::endl;
    std::cout << "Normal            :" << sizeof(Normal) << std::endl;
    return 0;
}
