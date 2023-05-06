#include <cs50.h>
#include <stdio.h>

int main(void)
{
    char c = get_char("Do you agree (Y/n)?: ");
    if (c == 'Y' || c == 'y') {
        printf("Agreed. \n");
    }
    else if (c == 'n' || c == 'N') {
        printf("Not agreed. \n");
    }
    else {
        printf("invalid input! \n");
    }
}