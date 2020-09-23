#ifndef lint
static const char yysccsid[] = "@(#)yaccpar	1.9 (Berkeley) 02/21/93";
#endif

#define YYBYACC 1
#define YYMAJOR 1
#define YYMINOR 9
#define YYPATCH 20130304

#define YYEMPTY        (-1)
#define yyclearin      (yychar = YYEMPTY)
#define yyerrok        (yyerrflag = 0)
#define YYRECOVERING() (yyerrflag != 0)

#define YYPREFIX "yy"

#define YYPURE 0

#line 6 "cexpr.y"
#include <stdio.h>
int alphabet[26];
int max = 2147483647;
void dump();
void clear();
int error=0;
int temp=0;
#line 15 "cexpr.y"
#ifdef YYSTYPE
#undef  YYSTYPE_IS_DECLARED
#define YYSTYPE_IS_DECLARED 1
#endif
#ifndef YYSTYPE_IS_DECLARED
#define YYSTYPE_IS_DECLARED 1
typedef union {
  int num;
  char var;
} YYSTYPE;
#endif /* !YYSTYPE_IS_DECLARED */
#line 39 "y.tab.c"

/* compatibility with bison */
#ifdef YYPARSE_PARAM
/* compatibility with FreeBSD */
# ifdef YYPARSE_PARAM_TYPE
#  define YYPARSE_DECL() yyparse(YYPARSE_PARAM_TYPE YYPARSE_PARAM)
# else
#  define YYPARSE_DECL() yyparse(void *YYPARSE_PARAM)
# endif
#else
# define YYPARSE_DECL() yyparse(void)
#endif

/* Parameters sent to lex. */
#ifdef YYLEX_PARAM
# define YYLEX_DECL() yylex(void *YYLEX_PARAM)
# define YYLEX yylex(YYLEX_PARAM)
#else
# define YYLEX_DECL() yylex(void)
# define YYLEX yylex()
#endif

/* Parameters sent to yyerror. */
#ifndef YYERROR_DECL
#define YYERROR_DECL() yyerror(const char *s)
#endif
#ifndef YYERROR_CALL
#define YYERROR_CALL(msg) yyerror(msg)
#endif

extern int YYPARSE_DECL();

#define NUM 257
#define VAR 258
#define DUMP 259
#define CLEAR 260
#define YYERRCODE 256
static const short yylhs[] = {                           -1,
    0,    0,    9,    9,    9,    1,    2,    2,    2,    2,
    2,    2,    2,    2,    2,    2,    2,    2,    3,    3,
    3,    3,    4,    4,    4,    5,    5,    5,    6,    6,
    6,    6,    7,    7,    7,    8,    8,    8,
};
static const short yylen[] = {                            2,
    0,    2,    2,    2,    2,    1,    1,    3,    4,    4,
    4,    4,    4,    5,    5,    4,    4,    4,    1,    3,
    3,    3,    1,    4,    4,    1,    3,    3,    1,    3,
    3,    3,    1,    2,    2,    3,    1,    1,
};
static const short yydefred[] = {                         1,
    0,   38,    0,    0,    0,    0,    0,    0,    0,    6,
    0,    0,    0,    0,   29,   33,    2,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    4,    5,
   37,   34,   35,    0,    3,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    8,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,   36,    0,    0,    0,
    0,    0,    0,    0,   30,   31,   32,    9,   10,   11,
   12,   13,    0,    0,   16,   17,   18,    0,    0,   14,
   15,
};
static const short yydgoto[] = {                          1,
    9,   10,   11,   12,   13,   14,   15,   16,   17,
};
static const short yysindex[] = {                         0,
  -40,    0,  -25,  -52,  -49,  -32,  -32,  -36,  -28,    0,
   -9,  -46,  -20,   17,    0,    0,    0,  -36,  -42,   -1,
    7,   26,   32,   -8,    4,   47,   49,   50,    0,    0,
    0,    0,    0,   71,    0,  -34,  -34,  -34,   58,   55,
  -34,  -34,  -34,  -34,  -34,    0,  -36,  -36,  -36,  -36,
  -36,   59,   61,  -36,  -36,  -36,    0,  -46,  -46,  -46,
  -34,  -34,   17,   17,    0,    0,    0,    0,    0,    0,
    0,    0,  -36,  -36,    0,    0,    0,  -20,  -20,    0,
    0,
};
static const short yyrindex[] = {                         0,
    0,    0,  -26,    0,    0,    0,    0,    0,    0,    0,
   -3,   35,    3,  -17,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,   37,   43,   57,
    0,    0,  -11,   12,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,   20,   29,    0,
    0,
};
static const short yygindex[] = {                         0,
  111,   91,    0,  -35,  -22,    5,   60,   94,    0,
};
#define YYTABLESIZE 226
static const short yytable[] = {                          8,
   58,   59,   60,    8,    6,    8,   29,    8,    6,   30,
    6,   23,   26,   39,   37,   40,   21,   19,   47,   20,
   26,   22,   41,   26,   42,   26,   27,   26,   36,   27,
   35,   27,   37,   27,   24,   18,   25,    7,   78,   79,
   23,   26,   26,   23,   26,   63,   64,   27,   27,   28,
   27,   52,   28,   45,   28,    7,   28,   24,   43,   48,
   24,   23,   23,   44,   23,   53,   25,   49,   27,   25,
   28,   28,   19,   28,   20,   19,   26,   20,   24,   24,
   21,   24,   27,   21,   37,    7,   50,   25,   25,    7,
   25,    7,   51,   19,   22,   20,   23,   22,   28,   32,
   33,   21,   65,   66,   67,   28,   26,   54,   46,   55,
   56,   57,   27,   24,   38,   22,   62,   61,   34,   73,
    0,   74,   25,    0,    0,    0,   23,    0,   19,    0,
   20,    0,    0,    0,    0,   28,   21,   68,   69,   70,
   71,   72,    0,   24,   75,   76,   77,    0,    0,    0,
   22,    0,   25,    0,    0,    0,    0,    0,   19,    0,
   20,    0,    0,   80,   81,    0,   21,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
   22,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    0,    0,    0,    0,
    0,    0,    0,    0,    0,    0,    2,    3,    4,    5,
    2,    3,    2,   31,    2,   31,
};
static const short yycheck[] = {                         40,
   36,   37,   38,   40,   45,   40,   59,   40,   45,   59,
   45,   37,   38,   60,   41,   62,   42,   43,   61,   45,
   38,   47,   43,   41,   45,   43,   38,   45,   38,   41,
   59,   43,   59,   45,   60,   61,   62,   41,   61,   62,
   38,   59,   60,   41,   62,   41,   42,   59,   60,   38,
   62,   60,   41,   37,   43,   59,   45,   38,   42,   61,
   41,   59,   60,   47,   62,   62,   38,   61,   94,   41,
   59,   60,   38,   62,   38,   41,   94,   41,   59,   60,
   38,   62,   94,   41,   94,  126,   61,   59,   60,  126,
   62,  126,   61,   59,   38,   59,   94,   41,  124,    6,
    7,   59,   43,   44,   45,   94,  124,   61,   18,   61,
   61,   41,  124,   94,  124,   59,   62,   60,    8,   61,
   -1,   61,   94,   -1,   -1,   -1,  124,   -1,   94,   -1,
   94,   -1,   -1,   -1,   -1,  124,   94,   47,   48,   49,
   50,   51,   -1,  124,   54,   55,   56,   -1,   -1,   -1,
   94,   -1,  124,   -1,   -1,   -1,   -1,   -1,  124,   -1,
  124,   -1,   -1,   73,   74,   -1,  124,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
  124,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,   -1,
   -1,   -1,   -1,   -1,   -1,   -1,  257,  258,  259,  260,
  257,  258,  257,  258,  257,  258,
};
#define YYFINAL 1
#ifndef YYDEBUG
#define YYDEBUG 0
#endif
#define YYMAXTOKEN 260
#if YYDEBUG
static const char *yyname[] = {

"end-of-file",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,"'%'","'&'",0,"'('","')'","'*'","'+'",0,"'-'",0,"'/'",0,0,0,0,0,0,0,0,0,0,
0,"';'","'<'","'='","'>'",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,"'^'",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,"'|'",0,
"'~'",0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,"NUM","VAR","DUMP","CLEAR",
};
static const char *yyrule[] = {
"$accept : commands",
"commands :",
"commands : commands command",
"command : expr ';'",
"command : DUMP ';'",
"command : CLEAR ';'",
"expr : equal",
"equal : logic_expr",
"equal : VAR '=' equal",
"equal : VAR '+' '=' equal",
"equal : VAR '-' '=' equal",
"equal : VAR '*' '=' equal",
"equal : VAR '/' '=' equal",
"equal : VAR '%' '=' equal",
"equal : VAR '<' '<' '=' equal",
"equal : VAR '>' '>' '=' equal",
"equal : VAR '&' '=' equal",
"equal : VAR '^' '=' equal",
"equal : VAR '|' '=' equal",
"logic_expr : shift_expr",
"logic_expr : logic_expr '&' shift_expr",
"logic_expr : logic_expr '^' shift_expr",
"logic_expr : logic_expr '|' shift_expr",
"shift_expr : add_sub_expr",
"shift_expr : shift_expr '<' '<' add_sub_expr",
"shift_expr : shift_expr '>' '>' add_sub_expr",
"add_sub_expr : mul_div_expr",
"add_sub_expr : add_sub_expr '+' mul_div_expr",
"add_sub_expr : add_sub_expr '-' mul_div_expr",
"mul_div_expr : neg_not_expr",
"mul_div_expr : mul_div_expr '*' neg_not_expr",
"mul_div_expr : mul_div_expr '/' neg_not_expr",
"mul_div_expr : mul_div_expr '%' neg_not_expr",
"neg_not_expr : pren",
"neg_not_expr : '-' pren",
"neg_not_expr : '~' pren",
"pren : '(' expr ')'",
"pren : VAR",
"pren : NUM",

};
#endif

int      yydebug;
int      yynerrs;

int      yyerrflag;
int      yychar;
YYSTYPE  yyval;
YYSTYPE  yylval;

/* define the initial stack-sizes */
#ifdef YYSTACKSIZE
#undef YYMAXDEPTH
#define YYMAXDEPTH  YYSTACKSIZE
#else
#ifdef YYMAXDEPTH
#define YYSTACKSIZE YYMAXDEPTH
#else
#define YYSTACKSIZE 10000
#define YYMAXDEPTH  500
#endif
#endif

#define YYINITSTACKSIZE 500

typedef struct {
    unsigned stacksize;
    short    *s_base;
    short    *s_mark;
    short    *s_last;
    YYSTYPE  *l_base;
    YYSTYPE  *l_mark;
} YYSTACKDATA;
/* variables for the parser stack */
static YYSTACKDATA yystack;
#line 224 "cexpr.y"


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
#line 309 "y.tab.c"

#if YYDEBUG
#include <stdio.h>		/* needed for printf */
#endif

#include <stdlib.h>	/* needed for malloc, etc */
#include <string.h>	/* needed for memset */

/* allocate initial stack or double stack size, up to YYMAXDEPTH */
static int yygrowstack(YYSTACKDATA *data)
{
    int i;
    unsigned newsize;
    short *newss;
    YYSTYPE *newvs;

    if ((newsize = data->stacksize) == 0)
        newsize = YYINITSTACKSIZE;
    else if (newsize >= YYMAXDEPTH)
        return -1;
    else if ((newsize *= 2) > YYMAXDEPTH)
        newsize = YYMAXDEPTH;

    i = (int) (data->s_mark - data->s_base);
    newss = (short *)realloc(data->s_base, newsize * sizeof(*newss));
    if (newss == 0)
        return -1;

    data->s_base = newss;
    data->s_mark = newss + i;

    newvs = (YYSTYPE *)realloc(data->l_base, newsize * sizeof(*newvs));
    if (newvs == 0)
        return -1;

    data->l_base = newvs;
    data->l_mark = newvs + i;

    data->stacksize = newsize;
    data->s_last = data->s_base + newsize - 1;
    return 0;
}

#if YYPURE || defined(YY_NO_LEAKS)
static void yyfreestack(YYSTACKDATA *data)
{
    free(data->s_base);
    free(data->l_base);
    memset(data, 0, sizeof(*data));
}
#else
#define yyfreestack(data) /* nothing */
#endif

#define YYABORT  goto yyabort
#define YYREJECT goto yyabort
#define YYACCEPT goto yyaccept
#define YYERROR  goto yyerrlab

int
YYPARSE_DECL()
{
    int yym, yyn, yystate;
#if YYDEBUG
    const char *yys;

    if ((yys = getenv("YYDEBUG")) != 0)
    {
        yyn = *yys;
        if (yyn >= '0' && yyn <= '9')
            yydebug = yyn - '0';
    }
#endif

    yynerrs = 0;
    yyerrflag = 0;
    yychar = YYEMPTY;
    yystate = 0;

#if YYPURE
    memset(&yystack, 0, sizeof(yystack));
#endif

    if (yystack.s_base == NULL && yygrowstack(&yystack)) goto yyoverflow;
    yystack.s_mark = yystack.s_base;
    yystack.l_mark = yystack.l_base;
    yystate = 0;
    *yystack.s_mark = 0;

yyloop:
    if ((yyn = yydefred[yystate]) != 0) goto yyreduce;
    if (yychar < 0)
    {
        if ((yychar = YYLEX) < 0) yychar = 0;
#if YYDEBUG
        if (yydebug)
        {
            yys = 0;
            if (yychar <= YYMAXTOKEN) yys = yyname[yychar];
            if (!yys) yys = "illegal-symbol";
            printf("%sdebug: state %d, reading %d (%s)\n",
                    YYPREFIX, yystate, yychar, yys);
        }
#endif
    }
    if ((yyn = yysindex[yystate]) && (yyn += yychar) >= 0 &&
            yyn <= YYTABLESIZE && yycheck[yyn] == yychar)
    {
#if YYDEBUG
        if (yydebug)
            printf("%sdebug: state %d, shifting to state %d\n",
                    YYPREFIX, yystate, yytable[yyn]);
#endif
        if (yystack.s_mark >= yystack.s_last && yygrowstack(&yystack))
        {
            goto yyoverflow;
        }
        yystate = yytable[yyn];
        *++yystack.s_mark = yytable[yyn];
        *++yystack.l_mark = yylval;
        yychar = YYEMPTY;
        if (yyerrflag > 0)  --yyerrflag;
        goto yyloop;
    }
    if ((yyn = yyrindex[yystate]) && (yyn += yychar) >= 0 &&
            yyn <= YYTABLESIZE && yycheck[yyn] == yychar)
    {
        yyn = yytable[yyn];
        goto yyreduce;
    }
    if (yyerrflag) goto yyinrecovery;

    yyerror("syntax error");

    goto yyerrlab;

yyerrlab:
    ++yynerrs;

yyinrecovery:
    if (yyerrflag < 3)
    {
        yyerrflag = 3;
        for (;;)
        {
            if ((yyn = yysindex[*yystack.s_mark]) && (yyn += YYERRCODE) >= 0 &&
                    yyn <= YYTABLESIZE && yycheck[yyn] == YYERRCODE)
            {
#if YYDEBUG
                if (yydebug)
                    printf("%sdebug: state %d, error recovery shifting\
 to state %d\n", YYPREFIX, *yystack.s_mark, yytable[yyn]);
#endif
                if (yystack.s_mark >= yystack.s_last && yygrowstack(&yystack))
                {
                    goto yyoverflow;
                }
                yystate = yytable[yyn];
                *++yystack.s_mark = yytable[yyn];
                *++yystack.l_mark = yylval;
                goto yyloop;
            }
            else
            {
#if YYDEBUG
                if (yydebug)
                    printf("%sdebug: error recovery discarding state %d\n",
                            YYPREFIX, *yystack.s_mark);
#endif
                if (yystack.s_mark <= yystack.s_base) goto yyabort;
                --yystack.s_mark;
                --yystack.l_mark;
            }
        }
    }
    else
    {
        if (yychar == 0) goto yyabort;
#if YYDEBUG
        if (yydebug)
        {
            yys = 0;
            if (yychar <= YYMAXTOKEN) yys = yyname[yychar];
            if (!yys) yys = "illegal-symbol";
            printf("%sdebug: state %d, error recovery discards token %d (%s)\n",
                    YYPREFIX, yystate, yychar, yys);
        }
#endif
        yychar = YYEMPTY;
        goto yyloop;
    }

yyreduce:
#if YYDEBUG
    if (yydebug)
        printf("%sdebug: state %d, reducing by rule %d (%s)\n",
                YYPREFIX, yystate, yyn, yyrule[yyn]);
#endif
    yym = yylen[yyn];
    if (yym)
        yyval = yystack.l_mark[1-yym];
    else
        memset(&yyval, 0, sizeof yyval);
    switch (yyn)
    {
case 3:
#line 43 "cexpr.y"
	{ 
                        if(error!=0){
                           printf("");
                           error=0;
                        }else{
                           printf("%d\n", yystack.l_mark[-1].num); 
                        }
                     }
break;
case 4:
#line 51 "cexpr.y"
	{dump();}
break;
case 5:
#line 52 "cexpr.y"
	{clear();}
break;
case 8:
#line 60 "cexpr.y"
	{
                        if(error==0){
                           alphabet[yystack.l_mark[-2].var] = yystack.l_mark[0].num; 
                           yyval.num=alphabet[yystack.l_mark[-2].var]; 
                        }
                     }
break;
case 9:
#line 67 "cexpr.y"
	{
                        if(error==0){
                           alphabet[yystack.l_mark[-3].var]+=yystack.l_mark[0].num;
                           yyval.num=alphabet[yystack.l_mark[-3].var];
                        }
                     }
break;
case 10:
#line 74 "cexpr.y"
	{
                        if(error==0){
                           alphabet[yystack.l_mark[-3].var]-=yystack.l_mark[0].num; 
                           yyval.num=alphabet[yystack.l_mark[-3].var];
                        }
                     }
break;
case 11:
#line 81 "cexpr.y"
	{
                        if(error==0){
                           alphabet[yystack.l_mark[-3].var]*=yystack.l_mark[0].num; 
                           yyval.num=alphabet[yystack.l_mark[-3].var];
                        }
                     }
break;
case 12:
#line 88 "cexpr.y"
	{
                        if(error==0 && yystack.l_mark[0].num!=0){
                           alphabet[yystack.l_mark[-3].var]/=yystack.l_mark[0].num; 
                           yyval.num=alphabet[yystack.l_mark[-3].var];
                        }else{
                           error=1;
                           printf("dividebyzero\n");
                        }
                     }
break;
case 13:
#line 98 "cexpr.y"
	{
                        if(yystack.l_mark[0].num!=0 && error==0){
                           alphabet[yystack.l_mark[-3].var]%=yystack.l_mark[0].num; 
                           yyval.num=alphabet[yystack.l_mark[-3].var];
                        }else{
                           error=1;
                           printf("dividebyzero\n");
                        }
                     }
break;
case 14:
#line 108 "cexpr.y"
	{
                        if(error==0){
                           alphabet[yystack.l_mark[-4].var]<<=yystack.l_mark[0].num; 
                           yyval.num=alphabet[yystack.l_mark[-4].var];
                        }
                     }
break;
case 15:
#line 115 "cexpr.y"
	{
                        if(error==0){
                           alphabet[yystack.l_mark[-4].var]>>=yystack.l_mark[0].num; 
                           yyval.num=alphabet[yystack.l_mark[-4].var];
                        }
                     }
break;
case 16:
#line 122 "cexpr.y"
	{
                        if(error==0){
                           alphabet[yystack.l_mark[-3].var]&=yystack.l_mark[0].num; 
                           yyval.num=alphabet[yystack.l_mark[-3].var];
                        }
                     }
break;
case 17:
#line 129 "cexpr.y"
	{
                        if(error==0){
                           alphabet[yystack.l_mark[-3].var]^=yystack.l_mark[0].num; 
                           yyval.num=alphabet[yystack.l_mark[-3].var];
                        }
                     }
break;
case 18:
#line 136 "cexpr.y"
	{
                        if(error==0){
                           alphabet[yystack.l_mark[-3].var]|=yystack.l_mark[0].num; 
                           yyval.num=alphabet[yystack.l_mark[-3].var];
                        }
                     }
break;
case 20:
#line 145 "cexpr.y"
	{if(error==0) yyval.num=yystack.l_mark[-2].num & yystack.l_mark[0].num;}
break;
case 21:
#line 146 "cexpr.y"
	{if(error==0) yyval.num=yystack.l_mark[-2].num ^ yystack.l_mark[0].num;}
break;
case 22:
#line 147 "cexpr.y"
	{if(error==0) yyval.num=yystack.l_mark[-2].num | yystack.l_mark[0].num;}
break;
case 24:
#line 151 "cexpr.y"
	{if(error==0) yyval.num=yystack.l_mark[-3].num<<yystack.l_mark[0].num;}
break;
case 25:
#line 152 "cexpr.y"
	{if(error==0) yyval.num=yystack.l_mark[-3].num>>yystack.l_mark[0].num;}
break;
case 27:
#line 157 "cexpr.y"
	{
                        if(error==0){
                           if(yystack.l_mark[0].num<0){
                              temp=(-yystack.l_mark[0].num);
                           }else{
                              temp=yystack.l_mark[0].num;
                           }
                           if(yystack.l_mark[-2].num <= max - temp){
                              yyval.num = yystack.l_mark[-2].num + yystack.l_mark[0].num; 
                           }else{
                              printf("overflow\n");
                              error=1;
                           }
                        }
                     }
break;
case 28:
#line 172 "cexpr.y"
	{yyval.num = yystack.l_mark[-2].num - yystack.l_mark[0].num;}
break;
case 30:
#line 177 "cexpr.y"
	{
                        if(error==0){
                           if(yystack.l_mark[0].num<0){
                              temp=(-yystack.l_mark[0].num);
                           }else{
                              temp=(yystack.l_mark[0].num);
                           }
                           if(yystack.l_mark[0].num==0){
                              yyval.num=0;
                           }else if(yystack.l_mark[-2].num <= max / temp){
                              yyval.num = yystack.l_mark[-2].num * yystack.l_mark[0].num; 
                           }else{
                              printf("overflow\n");
                           }
                        }
                     }
break;
case 31:
#line 194 "cexpr.y"
	{
                        if(yystack.l_mark[0].num!=0 && error ==0){
                           yyval.num=yystack.l_mark[-2].num/yystack.l_mark[0].num;
                        }else{
                           error=1;
                           printf("dividebyzero\n");
                        }
                     }
break;
case 32:
#line 203 "cexpr.y"
	{
                        if(yystack.l_mark[0].num!=0 && error ==0){
                           yyval.num=yystack.l_mark[-2].num%yystack.l_mark[0].num;
                        }else{
                           error=1;
                           printf("dividebyzero\n");
                        }
                     }
break;
case 34:
#line 214 "cexpr.y"
	{if(error==0) yyval.num = -yystack.l_mark[0].num;}
break;
case 35:
#line 215 "cexpr.y"
	{if(error==0) yyval.num =~yystack.l_mark[0].num;}
break;
case 36:
#line 218 "cexpr.y"
	{ if(error==0) yyval.num = yystack.l_mark[-1].num; }
break;
case 37:
#line 219 "cexpr.y"
	{ if(error==0) yyval.num = alphabet[yystack.l_mark[0].var]; }
break;
case 38:
#line 220 "cexpr.y"
	{ if(error==0) yyval.num = yystack.l_mark[0].num; }
break;
#line 742 "y.tab.c"
    }
    yystack.s_mark -= yym;
    yystate = *yystack.s_mark;
    yystack.l_mark -= yym;
    yym = yylhs[yyn];
    if (yystate == 0 && yym == 0)
    {
#if YYDEBUG
        if (yydebug)
            printf("%sdebug: after reduction, shifting from state 0 to\
 state %d\n", YYPREFIX, YYFINAL);
#endif
        yystate = YYFINAL;
        *++yystack.s_mark = YYFINAL;
        *++yystack.l_mark = yyval;
        if (yychar < 0)
        {
            if ((yychar = YYLEX) < 0) yychar = 0;
#if YYDEBUG
            if (yydebug)
            {
                yys = 0;
                if (yychar <= YYMAXTOKEN) yys = yyname[yychar];
                if (!yys) yys = "illegal-symbol";
                printf("%sdebug: state %d, reading %d (%s)\n",
                        YYPREFIX, YYFINAL, yychar, yys);
            }
#endif
        }
        if (yychar == 0) goto yyaccept;
        goto yyloop;
    }
    if ((yyn = yygindex[yym]) && (yyn += yystate) >= 0 &&
            yyn <= YYTABLESIZE && yycheck[yyn] == yystate)
        yystate = yytable[yyn];
    else
        yystate = yydgoto[yym];
#if YYDEBUG
    if (yydebug)
        printf("%sdebug: after reduction, shifting from state %d \
to state %d\n", YYPREFIX, *yystack.s_mark, yystate);
#endif
    if (yystack.s_mark >= yystack.s_last && yygrowstack(&yystack))
    {
        goto yyoverflow;
    }
    *++yystack.s_mark = (short) yystate;
    *++yystack.l_mark = yyval;
    goto yyloop;

yyoverflow:
    yyerror("yacc stack overflow");

yyabort:
    yyfreestack(&yystack);
    return (1);

yyaccept:
    yyfreestack(&yystack);
    return (0);
}
