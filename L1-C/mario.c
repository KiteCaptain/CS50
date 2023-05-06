#include <cs50.h>
#include <stdio.h>

// Prototype
int main(void)
{
    int w;
    int h;
    w = get_int("Width: ");
    h = get_int("Height: ");
    for (int i = 0; i < h; i++)
    {
        for (int j = 0; j < w; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}