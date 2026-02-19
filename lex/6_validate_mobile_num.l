%option noyywrap
%{
    #include <stdio.h>
    #include <stdlib.h>
%}

%%
^[6-9][0-9]{9}$    { printf("Valid Mobile Number\n"); exit(0); }
^[0-9]+$           { printf("Invalid Mobile Number\n"); exit(0); }
.|\n               { /* Ignore other characters */ }
%%

int main()
{
    printf("Enter Mobile Number: ");
    yylex();
    return 0;
}