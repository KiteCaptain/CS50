#include <cs50.h>
#include <stdio.h>

// Prototype
void greetings(int n);

int main(void)
{
    int i = 0;
    while (i < 20) {
        greetings(4);
        i++;
    }
}
void greetings(int n)
{
    for (int i = 0; i < n; i++)
    printf("Hello world\n");
}