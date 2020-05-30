#include <iostream>
#include <string>
#include <cstring>
#include <stdlib.h>
#include <math.h>


using namespace std;

int main()
{
    char sentence[50];
    int i;
    int counter = 0;
    cout << "Enter sentence to check if palindrome: \n";
    scanf("%s",&sentence);
    int size = strlen(sentence);
    if(size <= 3)
    {
        exit(0);
    }
    else
    {
    if(size % 2 == 0)
    {
        for(i=0;i<(size/2); i++)
        {
            if(sentence[i]==sentence[size-i-1])
            {
                counter++;
            }


        }

        if(counter == size/2)
        {
            printf("String is palindrome");
        }else{
            printf("Not palindrome");
        }

    }
    else if(size%2==1)
    {
        for(i=0;i<round(size/2)-1;i++)
        {
            if(sentence[i]==sentence[size-i-1])
            {
                counter++;
            }
        }
        if(counter == round(size/2)-1)
        {
            printf("String is palindrome");
        }else{
            printf("Not palindrome");
        }

    }
    }


    return 0;
}
