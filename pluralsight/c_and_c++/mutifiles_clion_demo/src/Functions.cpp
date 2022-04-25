#include <string.h>

// Helps make strcmp more usable
bool are_strings_equal(const char* str1, const char* str2) {
    // Calling a library function
    return !strcmp(str1, str2);
}