/*
 * This file defines an example yacc grammar for simple C expressions.
 */

%{
#include <stdio.h>
int alphabet[26];
int max = 2147483647;
void dump();
void clear();
int error=0;
int temp=0;
%}

%union {
  int num;
  char var;
}

%token <num> NUM
%token <var> VAR
%token DUMP
%token CLEAR

  
%type <num> expr
%type <num> equal
%type <num> and 
%type <num> or
%type <num> xor
%type <num> neg
%type <num> not
%type <num> shift_expr
%type <num> add_sub_expr
%type <num> mul_div_expr
%type <num> pren


%%
   
commands:
	|	commands command
	;

command: expr  ';'    
                     {
                        if(error!=0){
                           printf("");
                           error=0;
                        }else{
                           printf("%d\n", $1); 
                        }
                     }
      |  DUMP  ';'   {dump();}
      |  CLEAR ';'   {clear();}
	   ;

expr: equal
      ;

equal: or 
      |  VAR '=' equal  
                     {
                        if(error==0){
                           alphabet[$1-'a'] = $3; 
                           $$=alphabet[$1-'a']; 
                        }
                     }
      |  VAR '+''=' equal 
                     {
                        if(error==0){
                           if($4<0){
                              temp=(-$4);
                           }else{
                              temp=$4;
                           }
                           if(alphabet[$1-'a'] <= max - temp){
                              alphabet[$1-'a']+=$4;
                              $$=alphabet[$1-'a'];
                           }else{
                              printf("overflow\n");
                              error=1;
                           }
                        }
                     }
      |  VAR '-''=' equal 
                     {
                        if(error==0){
                           alphabet[$1-'a']-=$4; 
                           $$=alphabet[$1-'a'];
                        }
                     }
      |  VAR '*''=' equal 
                     {
                        if(error==0){
                           alphabet[$1-'a']*=$4; 
                           $$=alphabet[$1-'a'];
                        }
                     }
      |  VAR '/''=' equal 
                     {
                        if(error==0){
                           if($4!=0){
                              alphabet[$1-'a']/=$4; 
                              $$=alphabet[$1-'a'];
                           }else{
                              error=1;
                              printf("dividebyzero\n");
                           }
                        }
                     }
      |  VAR '%''=' equal 
                     {
                        if(error==0){
                           if($4!=0){
                              alphabet[$1-'a']%=$4; 
                              $$=alphabet[$1-'a'];
                           }else{
                              error=1;
                              printf("dividebyzero\n");
                           }
                        }
                     }
      |  VAR '>''>''=' equal 
                     {
                        if(error==0){
                           alphabet[$1-'a']>>=$5; 
                           $$=alphabet[$1-'a'];
                        }
                     }
      |  VAR '<''<''=' equal 
                     {
                        if(error==0){
                           alphabet[$1-'a']>>=$5; 
                           $$=alphabet[$1-'a'];
                        }
                     }
      |  VAR '&''=' equal 
                     {
                        if(error==0){
                           alphabet[$1-'a']&=$4; 
                           $$=alphabet[$1-'a'];
                        }
                     }
      |  VAR '^''=' equal 
                     {
                        if(error==0){
                           alphabet[$1-'a']^=$4; 
                           $$=alphabet[$1-'a'];
                        }
                     }
      |  VAR '|''=' equal 
                     {
                        if(error==0){
                           alphabet[$1-'a']|=$4; 
                           $$=alphabet[$1-'a'];
                        }
                     }
      ;

or: xor
      |  or '|' xor  {if(error==0) $$=$1 | $3;}
      |  VAR '|' xor  {if(error==0) $$=$1 | $3;}
      ;
xor: and
      |  xor '^' and  {if(error==0) $$=$1 ^ $3;}
      |  VAR '^' and  {if(error==0) $$=$1 ^ $3;}
      ;

and: shift_expr
      |  and '&' shift_expr  {if(error==0) $$=$1 & $3;}
      |  VAR '&' shift_expr  {if(error==0) $$=$1 & $3;}
      ;

shift_expr: add_sub_expr
      | shift_expr '>''>' add_sub_expr {if(error==0) $$=$1>>$4;}
      | VAR '>''>' add_sub_expr {if(error==0) $$=$1>>$4;}

      | shift_expr '<''<' add_sub_expr 
                     {
                        if(error==0){
                           temp=$1<<$4;
                           if(temp>$1){
                              $$=$1<<$4;
                           }else{
                              printf("overflow\n");
                              error=1; 
                           }
                        }
                     }
      | VAR '<''<' add_sub_expr 
                     {
                        if(error==0){
                           temp=$1<<$4;
                           if(temp>$1){
                              $$=$1<<$4;
                           }else{
                              printf("overflow\n");
                              error=1; 
                           }
                        }
                     }

      ;

add_sub_expr: mul_div_expr
      |  add_sub_expr '+' mul_div_expr   
                     {
                        if(error==0){
                           if($3<0){
                              temp=(-$3);
                           }else{
                              temp=$3;
                           }
                           if($1 <= max - temp){
                              $$ = $1 + $3; 
                           }else{
                              printf("overflow\n");
                              error=1;
                           }
                        }
                     }     
      |  VAR '+' mul_div_expr 
                     {
                        if(error==0){
                           if($3<0){
                              temp=(-$3);
                           }else{
                              temp=$3;
                           }
                           if($1 <= max - temp){
                              $$ = $1 + $3; 
                           }else{
                              printf("overflow\n");
                              error=1;
                           }
                        }
                     }
      |  add_sub_expr '-' mul_div_expr   {$$ = $1 - $3;}
      |  VAR '-' mul_div_expr   {$$ = $1 - $3;}
	   ;

mul_div_expr:  neg
      |  mul_div_expr '*' neg    
                     {
                        if(error==0){
                           if($3<0){
                              temp=(-$3);
                           }else{
                              temp=($3);
                           }
                           if($3==0){
                              $$=0;
                           }else if($1 <= max / temp){
                              $$ = $1 * $3; 
                           }else{
                              printf("overflow\n");
                           }
                        }
                     }
      |  VAR '*' neg    
                     {
                        if(error==0){
                           if($3<0){
                              temp=(-$3);
                           }else{
                              temp=($3);
                           }
                           if($3==0){
                              $$=0;
                           }else if($1 <= max / temp){
                              $$ = $1 * $3; 
                           }else{
                              printf("overflow\n");
                           }
                        }
                     }
      |  mul_div_expr '/' neg    
                     {
                        if(error ==0){
                           if($3!=0){
                              $$=$1/$3;
                           }else{
                              error=1;
                              printf("dividebyzero\n");
                           }
      						}
                     }
      |  VAR '/' neg    
                     {
                        if(error ==0){
                           if($3!=0){
                              $$=$1/$3;
                           }else{
                              error=1;
                              printf("dividebyzero\n");
                           }
      						}
                     }
      |  mul_div_expr '%' neg    
                     {
                        if(error ==0){
                           if($3!=0){
                              $$=$1%$3;
                           }else{
	                          error=1;
	                          printf("dividebyzero\n");
                           }
      						}
                     }
      |  VAR '%' neg    
                     {
                        if(error ==0){
                           if($3!=0){
                              $$=$1%$3;
                           }else{
	                          error=1;
	                          printf("dividebyzero\n");
                           }
      						}
                     }
      ;

neg: not
      |  '-' not {if(error==0) $$ =-$2;} 
      ;

not: pren
      |  '~' pren {if(error==0) $$ =~$2;}
      ;

pren: '(' expr ')'         { if(error==0) $$ = $2; }
      |  VAR               { if(error==0) $$ = alphabet[$1-'a']; }
      |  NUM               { if(error==0) $$ = $1; }
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
