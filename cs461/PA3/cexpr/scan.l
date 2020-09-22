%{
#include "y.tab.h"
%}
%%
[0-9]+    { sscanf(yytext, "%d", &yylval.num);
            return NUM; }
[a-z]     { yylval.num = *yytext - 'a';
            return VAR; }
[ \n]+    
"dump"   {return DUMP;}
"clear"   {return CLEAR;}
.         {return yytext[0];}

