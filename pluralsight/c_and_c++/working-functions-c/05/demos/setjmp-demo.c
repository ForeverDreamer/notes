#include <setjmp.h>
#include <stdio.h>

int main(void) {
    jmp_buf my_jump_buffer;

    // setjmp returns 0 here so the "else" block is visited on the first go around
    if (setjmp(my_jump_buffer) == 2) {
        printf("This will run after longjmp is called using 'my_jump_buffer'\n");
    } else {
        printf("longjmp'ing!\n");
        longjmp(my_jump_buffer, 2);
    }

    // In general, try to stay away from setjmp/longjmp unless you have a very good reason for it.
    // setjmp/longjmp functionality is very similar to "goto". Using it can make your code very hard to read.
    
    // setjmp is like "try" and longjmp is like "throw" in other high-level languages like C# or JavaScript

    /*  For a well-respected article on how to implement
        try/catch/throw/finally in C using macros and setjmp/longjmp,
        check out this website: http://groups.di.unipi.it/~nids/docs/longjump_try_trow_catch.html
    */
    return 0;
}
