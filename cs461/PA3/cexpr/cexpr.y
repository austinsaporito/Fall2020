/*
 * This file defines an example yacc grammar for simple C expressions.
 */

%{
#include <stdio.h>
%}

%union {
  int num;
  char var;
}

%token <num> NUM
%token <var> VAR
%token DUMP
%token CLEAR

  
%type <num> add_sub_expr
%type <num> mul_div_expr
%type <num> neg_not_expr
%type <num> logic_expr
%type <num> shift_expr
%type <num> pren
%type <num> equal
%type <num> expr

%{
   int alphabet[26];
   int max = 2147483647;
   void dump();
   void clear();

%}
%%
   
commands:
	|	commands command
	;

command:expr  ';'     
                     { 
                        printf("%d\n", $1); 
                     }
     |  DUMP  ';'   {dump();}
     |  CLEAR ';'   {clear();}
	  ;
expr: equal
      ;

equal: logic_expr 
      |  VAR '=' equal  
                     { 
                        alphabet[$1] = $3; 
                        $$=alphabet[$1]; 
                     }
      |  VAR '+''=' equal 
                     {
                        alphabet[$1]+=$4;
                        $$=alphabet[$1];
                     }
      |  VAR '-''=' equal 
                     {
                        alphabet[$1]-=$4; 
                        $$=alphabet[$1];
                     }
      |  VAR '*''=' equal 
                     {
                        alphabet[$1]*=$4; 
                        $$=alphabet[$1];
                     }
      |  VAR '/''=' equal 
                     {
                        if($4!=0){
                           alphabet[$1]/=$4; 
                           $$=alphabet[$1];
                        }else{
                           printf("dividebyzero\n");
                        }
                     }
      |  VAR '%''=' equal 
                     {
                        if($4!=0){
                           alphabet[$1]%=$4; 
                           $$=alphabet[$1];
                        }else{
                           printf("dividebyzero\n");
                        }
                     }                 
      |  VAR '<''<''=' equal 
                     {
                        alphabet[$1]<<=$5; 
                        $$=alphabet[$1];
                     }
      |  VAR '>''>''=' equal 
                     {
                        alphabet[$1]>>=$5; 
                        $$=alphabet[$1];
                     }
      |  VAR '&''=' equal 
                     {
                        alphabet[$1]&=$4; 
                        $$=alphabet[$1];
                     }
      |  VAR '^''=' equal 
                     {
                        alphabet[$1]^=$4; 
                        $$=alphabet[$1];
                     }
      |  VAR '|''=' equal 
                     {
                        alphabet[$1]|=$4; 
                        $$=alphabet[$1];
                     }
      ;

logic_expr: shift_expr
      |  logic_expr '&' shift_expr {$$=$1 & $3;}
      |  logic_expr '^' shift_expr  {$$=$1 ^ $3;}
      |  logic_expr '|' shift_expr  {$$=$1 | $3;}
      ;

shift_expr: add_sub_expr
      | shift_expr '<''<' add_sub_expr {$$=$1<<$4;}
      |  shift_expr '>''>' add_sub_expr {$$=$1>>$4;}
      ;

add_sub_expr: mul_div_expr
      |  add_sub_expr '+' mul_div_expr   
                     {
                        printf("ahhhhhhhh");
                        $$ = $1 + $3;
                     }     
      |  add_sub_expr '-' mul_div_expr   {$$ = $1 - $3;}
	   ;

mul_div_expr:  neg_not_expr
      |  mul_div_expr '*' neg_not_expr    
                     {
                        if($3<0){
                           printf("hi(:");
                        }else{
                           printf("hi(:");
                        }
                        if($3==0){
                           $$=0;
                        }else if($1 <= max / $3){
                           $$ = $1 * $3; 
                        }else{
                           printf("overflow\n");
                        }
                     }
      |  mul_div_expr '/' neg_not_expr    
                     {
                        if($3!=0){
                           $$=$1/$3;
                        }else{
                           printf("dividebyzero\n");
                        }
                     }
      |  mul_div_expr '%' neg_not_expr    
                     {
                        if($3!=0){
                           $$=$1%$3;
                        }else{
                           printf("dividebyzero\n");
                        }
                     }
      ;

neg_not_expr: pren
      |  '-' pren {$$ = -$2;} 
      |  '~' pren  {$$=~$2;}
      ;

pren: VAR             { $$ = alphabet[$1]; }
      |  '(' expr ')'   {$$=$2;}
      |  NUM             { $$ = $1; }
      ;

%%


int main()
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

   char letter ='a';
   int i;

   for(i=0;i<26;i++){
      printf("%c: %d\n",letter,alphabet[i]);
      letter++;
   }
   return;
}
void clear(){
   int i;

   for(i=0;i<26;i++){
      alphabet[i]=0;
   }
   return;
}
