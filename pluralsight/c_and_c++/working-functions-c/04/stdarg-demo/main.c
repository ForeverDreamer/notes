#include <stdio.h>
#include <stdarg.h>
#include <time.h>
#include <string.h>

static void wbc_print(const char* formatted_str, ...);

// Implement custom printf function for Wired Brain Coffee
static void wbc_print(const char* formatted_str, ...) {
    va_list argument_list;
    va_start(argument_list, formatted_str);

    time_t timestamp = time(NULL);
    char* time_str = asctime( gmtime(&timestamp) );

    // Get rid of the trailing newline character that "asctime" generates
    char *newline_ptr = strchr(time_str, '\n');
    if (newline_ptr) *newline_ptr = '\0';

    printf("WBC LOG (%s) ==> ", time_str );
    vprintf(formatted_str, argument_list);
    printf("\n");

    va_end(argument_list);
}

int main(void) {
    int one = 1, two = 2, three = 3;

    wbc_print("Initializing program execution...");
    wbc_print("Making awesome coffee... %d %d %d", one, two, three);

    return 0;
}
