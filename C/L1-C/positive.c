#include <cs50.h>
#include <stdio.h>

// Prototypes
int get_positive_int(void);

int main(void)
{
    int i = get_positive_int();
    printf("%i is +ve\n", i);
}
int get_positive_int(void)
{
    int n;
    do
    {
        n = get_int("Input a positive integer: ");
    }
    while (n < 1);
    return n;
}