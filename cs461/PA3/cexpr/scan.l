%{
#include "y.tab.h"
%}

%%


[ \t\n]+   ;

[0-9]+   { 
            sscanf(yytext, "%d", &yylval.num);
            return NUM; 
       	 }

"dump"   { return DUMP; }

"clear"  { return CLEAR; }

[a-z]    { 
			yylval.var=yytext[0];
            return VAR; 
		}

.      { return yytext[0]; }

