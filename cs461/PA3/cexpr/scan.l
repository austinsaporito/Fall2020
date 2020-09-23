%{
#include "y.tab.h"
%}
%%

[ \t\n]     ; 

[0-9]+|[0-9]*\.[0-9]+  { 
            sscanf(yytext, "%d", &yylval.num);
            return NUM; 
        }
[a-z]    { 
            printf("%c",*yytext);
            yylval.num = *yytext - 'a';
            return VAR; 
        }




.      { printf("%c",*yytext); return yytext[0]; }

dump   { return DUMP; }

clear  { return CLEAR; }

