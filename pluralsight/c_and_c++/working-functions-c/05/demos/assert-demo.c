#include <assert.h>
#include <string.h>
#include <stdio.h>

int main(void) {
    assert(!strcmp("Hello World", "Hello World"));

    assert(!strcmp("Hello", "World"));

    // This assertion is never reached - the program is aborted after the assertion that is just above fails
    assert(strcmp("Hello", "World"));
    printf("Did we make it here?\n");

    return 0;
}
