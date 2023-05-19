#include <cs50.h>
#include <stdio.h>

// Divide two numbers
int main(void)
{
    int x = get_int("x: ");
    int y = get_int("y: ");

    float z = (float) x/ (float) y;

    printf("%f\n", z);
}
