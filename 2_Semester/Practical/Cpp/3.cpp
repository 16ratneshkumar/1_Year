/*3. Write a program that prints a table indicating the number of occurrences of each alphabet in the text entered as command line arguments.*/
#include <iostream.h>
#include <string.h>
 
void input();
void new_line();
const int size = 30;
 
int main()
{
      char string[size];
      char ans;
       
      do
      {
      cout<<"Please enter a line.\n";
      cin.getline(string, 30);
      cout<< string << endl;
      cout<< strlen(string) << endl;         
 
      cout<<"Yes/No\n";
      cin>> ans;
      new_line();
      }
      while((ans != 'n') && (ans != 'N'));
       return 0;
}

void new_line()
{
      char symbol;
      do
      {
            cin.get(symbol);
      }while(symbol != '\n');
}
