%{
#include "y.tab.h"
%}

%%

[ \t\n]   ;

[0-9]+  { 
            sscanf(yytext, "%d", &yylval.num);
            return NUM; 
        }
[a-z]    { 
            yylval.num = *yytext - 'a';
            return VAR; 
        }




.      { return yytext[0]; }

dump   { return DUMP; }

clear  { return CLEAR; }

