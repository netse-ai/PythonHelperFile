#include <stdio.h>
#include <stdbool.h>


int binarySearch(int alist[], bool found, int first, int last, int item)
{

    while (first <= last && ! found)
    {
        int midpoint = (first + last)/2;
        if (alist[midpoint] < item)
            first = midpoint + 1;
        else if (alist[midpoint] == item)
        {
            printf("found %d, at %d\n", item, midpoint);
            found = true;
            return found;
            break;
        }
        else if (alist[midpoint] > item)
        {
            last = midpoint + 1;
        }
    }
    return -1;
}

int main(void)
{
    int alist[] = {1, 2, 3, 4, 5, 6, 7, 8, 9,10};
    int first, last, item;
    bool found = false;

    item = 11;
    first = 0;
    last = sizeof(alist)/sizeof(alist[0]);
    printf("Last index: index '%d'\n", last);
    int result = binarySearch(alist, found, first, last, item);
    printf("result = %d\n", result);
    if (result == -1)
    {
        printf("Element is not present in array. Returns %d\n", result);
    }
    else if (result == 1)
    {
        printf("Element is in present array. Returns %d\n", result);
    }
    else
    {
        printf("Something went wrong\n");
    }
    return 0;
}
