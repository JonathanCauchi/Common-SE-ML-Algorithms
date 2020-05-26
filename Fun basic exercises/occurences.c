#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
char sentence[100];
printf("Enter sentence (small letters, no numbers):\n");
fgets(sentence,100,stdin);
int size = strlen(sentence) -1;
int wordcount=0, spacecount=0, vowelcount=0, consonantcount=0;
for(int i=0; i<size; i++)
{
	if(sentence[i] == ' ')
	spacecount++;
	else if(sentence[i] == 'a'||sentence[i] == 'e'||sentence[i] == 'i'||sentence[i] == 'o'||sentence[i] == 'u')
        vowelcount++;
}
consonantcount = size - ((spacecount) + vowelcount);
wordcount = spacecount + 1;
printf("Size of string is %d\n",size);
printf("Total num of char without spaces is %d\n", size - spacecount );
printf("Word count is equal to %d\n", wordcount);
printf("Space count is equal to %d\n",spacecount);
printf("Vowel count is equal to %d\n",vowelcount);
printf("Consonant and special char count is equal to %d\n",consonantcount);
return 0;
}
