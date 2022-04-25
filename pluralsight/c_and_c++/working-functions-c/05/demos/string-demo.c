#include <string.h>
#include <stdio.h>
#include <errno.h>

int main(void) {

    /*
    * String Manipulation
    */

    /**
    * Watch out!
    * The strcpy function can be very dangerous and poses a security risk as it
    * is possible to overflow the "destination" buffer if it is not large enough
    * to hold what is contained in the "source" buffer.
    */
    char source_str[] = "My C string.";
    char destination_str[strlen(source_str) + 1]; // Make sure our destination string is large enough.

    // Remember - strcpy copies over the null terminator, \0, as well
    strcpy(destination_str, source_str);  

    // Note: If you are using BSD libc (macOS, OpenBSD, etc.) - you can use strlcpy as a safe alternative

    // This behavior is undefined as the destination string is too small...
    // This might result in an "illegal hardware instruction" error or others depending
    // upon the overwritten memory

    // char destination_str2[5];
    // strcpy(destination_str2, source_str);

    char my_name[] = "Zachary Bennett";
    char my_first_name[8];

    // Fill our destination string with null terminators
    memset(my_first_name, '\0', strlen(my_first_name) + 1); 
    strncpy(my_first_name, my_name, 7); // Remember - strncpy does not copy over the null terminator!


    /**
    * Watch out!
    * The strcat function can be very dangerous and poses a security risk as it
    * is possible to overflow the "destination" buffer if it is not large enough
    * to hold what is contained in both the "source" and "destination" buffers 
    * or if the "destination" string buffer does not include a null terminator.
    * 
    * You might be able to use strlcat (BSD libc) instead!
    */
   char name[16] = "Zachary ";
   char last_name[] = "Bennett";
   strcat(name, last_name); // Destination string has enough room to contain the source string

   // This results in undefined behavior and overflows the destination string buffer
   /*
    char overflow_name[] = "Zachary ";
    char overflow_last_name[] = "Bennett";
    strcat(overflow_name, overflow_last_name); // Remember - strcat copies over the null terminator
   */

    // Note: If you are using BSD libc (macOS, OpenBSD, etc.) - you can use strlcat as a safe alternative


    // This  will fail.. not enough room in the destination buffer
    /*
        char dog_name[] = "My dog Nico is ";
        char dog_age[] = "2 years old";
        strncat(dog_name, dog_age, strlen(dog_age) - 1);
    */


    size_t hello_buffer_max = 20;
    char destination_hello[hello_buffer_max];
    char source_hello[] = "Hello ";

    int new_str_len = strxfrm(destination_hello, source_hello, hello_buffer_max);

    // Notice how the length is up until the null terminator - not up to the size of the buffer itself.
    printf("Destination string length: %d\n", new_str_len); 


    char my_long_str[] = "This_is_snake_case.";
    char delimiter[] = "_";
    char* token = strtok(my_long_str, delimiter);

    while(token) {
        printf("Next Token: %s\n", token);

        // Pass a NULL pointer in order to keep parsing rest of the tokens from the original string.
        token = strtok(NULL, delimiter); 
    }

    /*
    * String Comparison 
    */
    const char str1[] = "Hello world";
    const char str2[] = "Hello world";
    // Note the "bang" operator here which is used to negate the falsey presence
    // of zero which indicates two strings are equal
    if (!strcmp(str1, str2)) {
        printf("These strings are equal!\n");
    }

    const char substr1[] = "ABCDEF";
    const char substr2[] = "AB DEF";
    if (!strncmp(substr1, substr2, 2)) {
        printf("These substrings are equal!\n");
    }

    if (strncmp(substr1, substr2, 3)) {
        printf("These substrings are not equal!\n");
    }

    const char coll_str1[] = "XYZ";
    const char coll_str2[] = "XYZ";
    // This function works the same as strcmp except that it will take into
    // account the value of the LC_COLLATE, locale macro
    strcoll(coll_str1, coll_str2);

    /*
    * String Metadata 
    */

    const char hello_world[] = "Hello World";
    char* rest_of_str_after_h = strchr(hello_world, 'e');
    printf("%s\n", rest_of_str_after_h);

    char* rest_of_str_after_last_o = strrchr(hello_world, 'o');
    printf("%s\n", rest_of_str_after_last_o);

    // Please note how the above two functions include the given search character in the final output.
    int matching_initial_chars = strspn(hello_world, "HelloWorld");
    printf("Matching characters: %d\n", matching_initial_chars);;


    // A quirky kind of function that gives you the count of unmatching characters
    // based on the first matching character
    int chars_before_first_match = strcspn(hello_world, "owdl");
    printf("Chars until 'l': %d\n", chars_before_first_match);

    char* first_match = strpbrk(hello_world, "owdl");
    printf("First match: %s\n", first_match);

    // The name of this function within the standard library of other programming languages
    // is usually called "substring"
    char base_str[] = "Nelson Mandela";
    char str_to_find[] = "Man";
    char* substring = strstr(base_str, str_to_find);
    printf("Found substring: %s\n", substring);

    /*
    * String Error Handling 
    */
    FILE *nonexistent_file = fopen("this_file_does_not_exist.md", "r");
    if (!nonexistent_file) {
        printf("%s\n", strerror(errno));
    }

    /*
    * Miscellaneous Memory  
    */

    // See line 28 for an example usage of "memset"

    int memcpy_max = 100;
    char my_dest[memcpy_max];
    char my_source[] = "Testing Testing 123";
    strcpy(my_dest, "Testing");

    // We account for the null terminator here by adding one to 'strlen'
    memcpy(my_dest, my_source, strlen(my_source) + 1); 

    // Note that the original string is overwritten.
    printf("%s\n", my_dest);

    // Accomplishes the same thing as memcpy except it is safer when working
    // with overlapping memory addresses
    char my_source2[] = "ABC123";
    memmove(my_dest, my_source2, strlen(my_source2) + 1);
    printf("%s\n", my_dest);


    char test_str1[] = "123456";
    char test_str2[] = "123456";
    if (!memcmp(test_str1, test_str2, strlen(test_str1))) {
        printf("The data contained within these blocks of memory are equal!\n");
    }

    char base[] = "123456789abcdef";
    char search = '4';
    char* match_1 = (char*)memchr(base, search, 3);
    char* match_2 = (char*)memchr(base, search, 4);

    printf("memchr match one: %s\n", match_1); // This one turns out to be a NULL pointer!
    printf("memchr match two: %s\n", match_2);

    return 0;
}
