#include <signal.h>
#include <stdbool.h>
#include <stdlib.h>
#include <stdio.h>

void handle_process_abort(int signal);

typedef struct CoffeeGrinder {
    int   setting;
    bool  is_running;
    char* serial_no;
} CoffeeGrinder;

// Global resource in order to test the cleaning of global resources using a signal handler
CoffeeGrinder* my_grinder;

int main(void) {

    // Show how to use the SIG_IGN predefined function to ignore a signal
    signal(SIGABRT, SIG_IGN);
    raise(SIGABRT); // Signal process abort

    my_grinder = (CoffeeGrinder*)malloc(sizeof(my_grinder));

    if (my_grinder) {
        my_grinder->setting = 2;
        my_grinder->is_running = false;
        my_grinder->serial_no = "abc123";
    } else {
        printf("Coffee grinder resource not allocated... not enough memory available\n");
    }
    
    signal(SIGABRT, &handle_process_abort);

    raise(SIGABRT);

}


void handle_process_abort(int signal) {
    printf("This program is exiting early - this should not happen!\n");
    if (my_grinder) {
        printf("Cleaning up global resource for coffee grinder: %s\n", my_grinder->serial_no);
        free(my_grinder);
    }

}
