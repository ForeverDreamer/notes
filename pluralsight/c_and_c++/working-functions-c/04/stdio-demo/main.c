#include <stdio.h>
#include <stdarg.h>
#include <stdlib.h>
#include <string.h>

void demo_vfprint(FILE* file, const char* format, ...) {
    va_list arguments;
    va_start(arguments, format);

    vfprintf(file, format, arguments);

    va_end(arguments);
}

int main(void) {

    FILE* test_file = fopen("stdio_test_file.txt", "w+");

    /**
     *
     * FORMATTED I/O
     *
     **/
    int max_str_len = 50;
    char scan_string_one[max_str_len], scan_string_two[max_str_len];
    int my_fav_number, user_fav_number;

    char my_formatted_str[max_str_len];

    fprintf(test_file, "Favorite number: %d\n", 10);

    rewind(test_file); // Reset the file position to the beginning of the file

    fscanf(test_file, "%s %s %d", scan_string_one, scan_string_two, &my_fav_number);

    printf("Here is my favorite number read from 'fscanf': %d\n", my_fav_number);

    printf("Please enter a number: \n");
    scanf("%d", &user_fav_number);

    printf("Here is the user's favorite number that was read using 'scanf': %d\n", user_fav_number);

    sprintf(my_formatted_str, "Favorite number comparison: %d | %d\n", my_fav_number, user_fav_number);

    printf("%s", my_formatted_str);

    /**
     *
     * FILE OPERATIONS
     *
     **/
    fclose(test_file);
    freopen("stdio_test_file.txt", "w+", test_file); // Note: this erases current content within the file
    // For a full listing of file modes to use with freopen and fopen:
    // https://en.wikibooks.org/wiki/C_Programming/stdio.h/fopen

    fclose(test_file);

    FILE* new_file = fopen("new_file.txt", "w+");

    char str_buffer[2];
    memset(str_buffer, '\0', sizeof(str_buffer));

    // Set buffer of the stdout stream. _IOFBF indicates that data will be written once the buffer is full.
    // _IOLBF indicates that data is written when a newline character is reached or the buffer is full.
    // _IONBF indicates that no buffer is used - write everything as soon as possible!
    setvbuf(stdout, str_buffer, _IOFBF, 400);

    fprintf(stdout, "Printing to a buffer!\n");

    fprintf(stdout, "Printing to a buffer again\n");

    // Flush the buffer and cause output to be written even though the buffer is not full yet.
    fflush(stdout);

    // Reset standard output so that it doesn't use a buffer anymore
    setvbuf(stdout, NULL, _IONBF, 0);

    // fclose(new_file);

    // rename("new_file.txt", "new_file_renamed.txt");
    // remove("new_file_renamed.txt");

    FILE* tmp = tmpfile();

    fclose(tmp);

    // Deprecated!
    // char temp_name_str[L_tmpnam];
    // tmpnam(temp_name_str)

    char tmp_file_name[] = "/tmp/temp_file_for_me-XXXXXX"; // This must be a character array
    mkstemp(tmp_file_name);
    // This function is actually from stdlib.h - for Windows, use tmpnam_s(char* str, size_t str_size)
    FILE* tmp_file = fopen(tmp_file_name, "r");

    printf("Closing tmp file\n");
    fclose(tmp_file);

    /**
     *
     * CHARACTER I/O
     *
     **/
    freopen("stdio_test_file.txt", "w+", test_file);

    fputc('a', test_file);

    fputs("long long long string", test_file);

    rewind(test_file);

    char next_char = (char)fgetc(test_file);
    printf("Char: %c\n", next_char);

    char next_str[5];
    if( fgets(next_str, 5, test_file) != NULL ) {
      puts(next_str);
   }

    rewind(test_file);

    // Write a character back on to the stream
    ungetc('a', test_file);

    // Read the same character off of the stream
    next_char = (char)fgetc(test_file);
    printf("Char: %c\n", next_char);

    char user_input_from_getchar = getchar();
    printf("Char: %c\n\n", user_input_from_getchar);

    printf("Putting char....\n");
    putchar('a');
    putchar('\n');

    printf("Input a character please: \n");
    user_input_from_getchar = getchar();
    printf("Char: %c\n\n", user_input_from_getchar);


    fclose(test_file);

    /**
     *
     * FILE I/O
     *
     **/

    freopen("stdio_test_file.txt", "w+", test_file);


    char block_write_str[] = "This string will be written into the file.";
    size_t str_size = strlen(block_write_str) + 1;
    char read_buffer[str_size];

    fwrite(block_write_str, str_size, 1, test_file);

    rewind(test_file);

    fread(read_buffer, str_size, 1, test_file);

    printf("%s\n", read_buffer);

    fclose(test_file);

    /**
     *
     * FILE POSITIONING
     *
     **/
    freopen("stdio_test_file.txt", "w+", test_file);

    fpos_t test_file_pos;

    fgetpos(test_file, &test_file_pos);
    fputs("Woohoo!", test_file); // This adjusts the position of the file pointer
    fsetpos(test_file, &test_file_pos); // Reset the position
    fputs("Woohoooooo!!!!", test_file); // Overwrite "Woohoo!" with "Woohoooooo!!!!"

    long total_file_size = ftell(test_file);
    printf("Total file size: %li\n", total_file_size);

    fseek(test_file, (int)(total_file_size / 2), 0);
    long half_file_size = ftell(test_file);

    printf("Half of total file size: %li\n", half_file_size);

    rewind(test_file);

    fclose(test_file);

    /**
     *
     * ERROR HANDLING / INDICATORS
     *
     **/
    freopen("stdio_test_file.txt", "w+", test_file);

    if (feof(test_file) > 0) {
        printf("The end of the file has been reached!");
    }

    // Let's try to read from an empty file
    FILE* empty_file = fopen("empty_file.txt", "w");
    fgetc(empty_file);

    if (ferror(empty_file) > 0) {
        printf("An error associated with this file pointer has occurred!\n");
        clearerr(empty_file);
    }

    if (ferror(empty_file) == 0) {
        printf("The error was cleared!\n");
    }

    fclose(empty_file);
    fclose(test_file);

    remove("stdio_test_file.txt");
    remove("empty_file.txt");

    // Let's try to open a nonexistent file in order to read from it
    FILE* nonexistent_file = fopen("no_file_here.txt", "r");
    if (nonexistent_file == NULL) {
        perror("This error occurred");
    }

    fclose(nonexistent_file);
}

