#include <stdio.h>

// Linear search using recursion

int linearsearch(int arr[], int size, int key)
{
    if (size == 0)
    {
        return -1;
    }
    if (arr[size - 1] == key)
    {
        return size - 1;
    }
    else
    {
        return linearsearch(arr, size - 1, key);
    }
}

int main(void)
{
    int arr[] = {5, 15, 6, 9, 4};
    int key = 15;
    int index = linearsearch(arr, sizeof(arr) / sizeof(int), key);
    if (index == -1)
    {
        printf("Key not found int the array.\n");
    }
    else
    {
        printf("The element %d is found at %d index of the given array\n", key, index);
    }
}