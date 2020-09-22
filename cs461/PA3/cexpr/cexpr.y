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
%token <string>ERR

  
%type <num> add_sub_expr
%type <num> mul_div_expr
%type <num> neg_not_expr
%type <num> logic_expr
%type <num> shift_expr
%type <num> pren
%type <num> equal
%type <num> val

%{
   yyerror(char *);
   int alphabet[26] = {0};
   int max = 2147483647;
   int flag=0;
   temp=0;
   void dump();
   void clear();

%}
%%
   
commands:
	|	commands command
	;

command	:	equal ';'      { if(flag==1){
                                 flag=0;
                                 printf("");
                              }else{
                                 printf("%d\n", $1); 
                              }
                           }
     |  DUMP  ';'   {dump();}
     |  CLEAR ';'   {clear();}
	  ;

equal :  VAR '=' equal  { alphabet[$1] = $3; 
                           $$=alphabet[$1]; }
      |  VAR '+''=' equal {alphabet[$1]+=$4;
                           $$=alphabet[$1];}
      |  VAR '-''=' equal {alphabet[$1]-=$4; 
                           $$=alphabet[$1];}
      |  VAR '*''=' equal {alphabet[$1]*=$4; 
                           $$=alphabet[$1];}
      |  VAR '/''=' equal {if($4!=0){
                              alphabet[$1]/=$4; 
                              $$=alphabet[$1];
                            }else{
                               printf("dividebyzero\n");
                               flag=1;
                            }
                           }
      |  VAR '%''=' equal {if($4!=0){
                              alphabet[$1]%=$4; 
                              $$=alphabet[$1];
                            }else{
                              printf("dividebyzero\n");
                              flag=1;
                            }
                           }                 
      |  VAR '<''<''=' equal {alphabet[$1]<<=$5; 
                           $$=alphabet[$1];}
      |  VAR '>''>''=' equal {alphabet[$1]>>=$5; 
                           $$=alphabet[$1];}
      |  VAR '&''=' equal {alphabet[$1]&=$4; 
                           $$=alphabet[$1];}
      |  VAR '^''=' equal {alphabet[$1]^=$4; 
                           $$=alphabet[$1];}
      |  VAR '|''=' equal {alphabet[$1]|=$4; 
                           $$=alphabet[$1];}
      |  logic_expr           { $$ = $1; }
      ;

logic_expr : logic_expr '&' logic_expr {$$=$1 & $3;}
      |  logic_expr '^' logic_expr  {$$=$1 ^ $3;}
      |  logic_expr '|' logic_expr  {$$=$1 | $3;}
      |  shift_expr           { $$ = $1; }
      ;

shift_expr  :  shift_expr '<''<' shift_expr {$$=$1<<$4;}
      |  shift_expr '>''>' shift_expr {$$=$1>>$4;}
      |  add_sub_expr           { $$ = $1; }
      ;

add_sub_expr	:	
      |  add_sub_expr '+' add_sub_expr   {if($3<0)
                                             temp=(-$3);
                                           else
                                             temp=$3;
                                           if($1 <= max - temp){
                                             $$ = $1 + $3; 
                                           }else{
                                             printf("overflow\n");
                                             flag=1;
                                           }
                                          }
      |  add_sub_expr '-' add_sub_expr   {$$ = $1 - $3;}
	   |	mul_div_expr                 { $$ = $1; }
	   ;

mul_div_expr :  
      |  mul_div_expr '*' mul_div_expr    {if($3<0)
                                             temp=(-$3);
                                            else
                                             temp=$3;
                                           if(temp==0){
                                              $$=$1*$3;
                                           }else if($1 <= max / temp){
                                              $$ = $1 * $3; 
                                           }else{
                                              printf("overflow\n");
                                              flag=1;
                                           }
                                          }
      |  mul_div_expr '/' mul_div_expr    {if($3!=0){
                                             $$=$1/$3;
                                           }else{
                                             printf("dividebyzero\n");
                                             flag=1;
                                           }
                                          }
      |  mul_div_expr '%' mul_div_expr    {if($3!=0){
                                             $$=$1%$3;
                                           }else{
                                             printf("dividebyzero\n");
                                             flag=1;
                                           }
                                          }
      |  neg_not_expr           { $$ = $1; }
      ;

neg_not_expr : '-' neg_not_expr {$$ = -$2;} 
      |  '~' neg_not_expr  {$$=~$2;}
      |  pren           { $$ = $1; }
      ;

pren  :  '(' logic_expr ')'   {$$=$2;}
      |  val            {$$=$1;}
      ;

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

   char letter ='a';
   int i;

   for(i=0;i<26;i++){
      printf("%c: %d\n",letter,alphabet[i]);
      letter++;
   }

}
void clear(){
   int i;

   for(i=0;i<26;i++){
      alphabet[i]=0;
   }

}
