#include <iostream>
using std::cout;

#include "src/Functions.h"

int main(){
    const char* my_name = "Zach";
    const char* friend_name = "Zach";

    // Calling a user-defined function
    bool names_are_equal = are_strings_equal(my_name, friend_name);

    printf("These names are equal: %s\n", names_are_equal ? "true" : "false");

    return 0;
}

