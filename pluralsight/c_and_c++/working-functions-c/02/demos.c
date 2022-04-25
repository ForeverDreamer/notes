#include <stdio.h>
#include <stdbool.h>
#include <string.h>

// Helps make strcmp more usable
bool are_strings_equal(const char* str1, const char* str2) {
    // Calling a library function 
    return !strcmp(str1, str2);
}


int main(void){
    const char* friend_name = "Zach";

    // Calling a user-defined function
    bool names_are_equal = are_strings_equal(my_name, friend_name);

    printf("These names are equal: %s\n", names_are_equal ? "true" : "false");

    return 0;
}
