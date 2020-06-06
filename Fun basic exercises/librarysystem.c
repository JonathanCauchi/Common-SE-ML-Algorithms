#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct book{
        char name[50];
        char author[50];
        int id;
        int available;
};

int main()
{
        struct book b[100];
        int flag = 0;
        int option;
        int keepcount = 0;
        int id_update, id_lookup;
        char name_lookup[50], author_lookup[50];

        while(flag!=1)
        {
        printf("Enter option from below\n");
        printf("1.Add book to database\n");
        printf("2.List all books in database\n");
        printf("3.Update book in database\n");
        printf("4.Lookup particular book ID\n");
        printf("5.Lookup particular book/s by Author Name\n");
        printf("6.Lookup particular book book name\n");
        printf("7.EXIT\n");


        scanf("%d",&option);
        switch(option)
        {
        case 1:

        printf("Enter name of book:\n");
        scanf("%s",b[keepcount].name); //use fgets(inputStr,64,stdin), scanf doesnt allow spaces in the string
        printf("Enter name of author:\n");
        scanf("%s",b[keepcount].author);
        b[keepcount].id = keepcount;
        keepcount++;
        break;

        case 2:
        printf("Below are all books in the database:\n");
        for(int i=0; i<keepcount; i++)
        {
            printf("ID: %d , Name = %s, Author %s\n",b[i].id, b[i].name, b[i].author);
        }
        break;

        case 3:
        printf("Enter ID of book you want to update:\n ");
        scanf("%d",&id_update);
        printf("Enter new name of book:\n");
        scanf("%s",b[id_update].name);
        printf("Enter new name of author:\n");
        scanf("%s",b[id_update].author);
        break;

        case 4:
            printf("Enter ID of book you want to view:\n");
            scanf("%d",&id_lookup);
            printf("Book ID: %d, Book Name: %s, Book Author: %s\n",id_lookup, b[id_lookup].name, b[id_lookup].author);
            break;

        case 5:

            printf("Enter name of book: \n");
            scanf("%s",name_lookup);
            for(int i=0;i<keepcount;i++)
            {
                if(strcmp(name_lookup,b[i].name) == 0)
                    printf("Book ID: %d, Book Name: %s, Book Author: %s\n",b[i].id, b[i].name,b[i].author);
            }
            break;

        case 6:
            printf("Enter name of author: \n");
            scanf("%s",author_lookup);
            for(int i=0;i<keepcount;i++)
            {
                if(strcmp(author_lookup,b[i].author) == 0)
                    printf("Book ID: %d, Book Name: %s, Book Author: %s\n",b[i].id, b[i].name,b[i].author);
            }
            break;

        case 7:
            exit(0);
            break;
            }
        }//end switch


//end while
}//end main func









