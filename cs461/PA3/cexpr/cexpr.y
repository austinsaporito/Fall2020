/*
 * This file defines an example yacc grammar for simple C expressions.
 */

%{
#include <stdio.h>
%}

%union {
  int num;
}

%token <num> NUM
%token <num> VAR
%token <string>DUMP
%token <string>CLEAR

  
%type <num> add_expr
%type <num> mul_expr
%type <num> equal
%type <num> val

%{
   int alphabet[26];
   int INT_MAX = 2147483647;
   void dump();
   void clear();

%}
%%
   
commands:
	|	commands command
	;

command	:	equal ';'      { printf("%d\n", $1); }
     |  DUMP  ';'   {dump();}
 //  |  CLEAR ';'   {clear();}
	  ;

equal :  VAR '=' equal  { alphabet[$1] = $3; $$ = alphabet[$1]; }
      |  add_expr           { $$ = $1; }


add_expr	:	add_expr '+' add_expr   { $$ = $1 + $3; }
      |  add_expr '-' add_expr      {$$ = $1 - $3;}
	   |	mul_expr                 { $$ = $1; }
	   ;

mul_expr :  mul_expr '*' mul_expr { $$ = $1 * $3; }
      |  val           { $$ = $1; }
 
 val  :  NUM             { $$ = $1; }
      |  VAR             { $$ = alphabet[$1]; }
      ;

%%


main()
{
   if (yyparse())
      printf("\nInvalid expression.\n");
   else
      printf("\nCalculator off.\n");
}

yyerror(s)
char *s;
{
   fprintf(stderr, "%s\n", s);
}

void dump(){

   printf("dumped");
}
