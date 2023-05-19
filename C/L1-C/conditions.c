#include <cs50.h>
#include <stdio.h>

// Divide two numbers
int main(void)
{
    // Compare x and y
    int x = get_int("x: ");
    int y = get_int("y: ");

    if (x < y)
    {
        printf("x is less than y \n");
    }
    else if (x > y)
    {
        printf("x is greator than y \n");
    }
    else
    {
        printf("x is equal to y \n");
    }

}
