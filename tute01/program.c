#include <stdio.h>    // trailing whitespace here:    

#define MSG "Hello from a macro!"	 	

int main(void) {
    printf("%s\n", MSG);

    // This line contains a # but is NOT a preprocessor command:
    printf("This is not a directive: # just a character in a string\n");

    // Another non-directive # (comment text):
    // # not a directive because it’s inside a comment

    return 0;     
}
