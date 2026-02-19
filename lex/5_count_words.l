%option noyywrap
%{
#include<stdio.h>
extern FILE **yyin;
int count = 0;
%%}

%%
[a-zA-Z0-9]+  {count++;}
%%
int main()
{
	FILE *fp = fopen("5_Count_Words.txt", "r");
	if(!fp)
	{
		printf("Can Not Open File");
		return 1;
	}
	yyin = fp;
	yylex();
	printf("total number of words: %d\n", count);
	fclose(fp);
	return 0;
}