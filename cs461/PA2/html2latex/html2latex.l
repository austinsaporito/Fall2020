%{
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int list_type;
%}

%option       noyywrap nounput yylineno
%x            COMMENT PARA PRE OL UL LI

%%


"<h1>"[^<]*"</h1>" {
    /**************************************************************************
     * Matched an HTML H1 header so print it out as a LateX section title.
     * The beginning and ending tags need to be stripped off before the
     * title can be formatted in LateX.
     *************************************************************************/
    yytext[yyleng-5] = 0;
    printf( "\\section{%s}", yytext+4 );
}
    /*
     * I just coppied h1 for h2 and h3 but instead just changed it to match what 
     * was needed.
    */
"<h2>"[^<]*"</h2>" {
    /**************************************************************************
     * Matched an HTML H1 header so print it out as a LateX section title.
     * The beginning and ending tags need to be stripped off before the
     * title can be formatted in LateX.
     *************************************************************************/
    yytext[yyleng-5] = 0;
    printf( "\\subsection{%s}", yytext+4 );
}
"<h3>"[^<]*"</h3>" {
    /**************************************************************************
     * Matched an HTML H1 header so print it out as a LateX section title.
     * The beginning and ending tags need to be stripped off before the
     * title can be formatted in LateX.
     *************************************************************************/
    yytext[yyleng-5] = 0;
    printf( "\\subsubsection{%s}", yytext+4 );
}

    /*
        If the analyser finds "<ol>" it begins the matching for OL and it will 
        continue to match based on other rules it finds with the "<OL>" format.
        if it is a formatting it replaces it with its respective match for latex 
        and if it a newline or possibly a newline with a carrage return (for windows)
        it will replace with a newline, and if it is any character it just prints out that character.
        it returns when it sees a "</ol>"
    */

"<ol>" {

    printf("\\begin{enumerate}");
    BEGIN OL;

}
<OL>[ \t] {

    printf("%s",yytext);

}

<OL>[\n](\r)? {

    printf( "\n" );
}

<OL>"<li>"  {printf("\\item ");}

<OL>"</li>"  {printf("\n");}

<OL>. {printf("%s",yytext);}

<OL>"<big>" {printf("{\\Large ");}

<OL>"</big>" {printf("}");}

<OL>"<small>" {printf("{\\scriptsize ");}

<OL>"</small>" {printf("}");}

<OL>"<i>" {printf("\\textit{");}

<OL>"</i>" {printf("}");}

<OL>"<b>" {printf("\\textbf{");}

<OL>"</b>" {printf("}");}

<OL>"<em>" {printf("\\emph{");}

<OL>"</em>" {printf("}");}

<OL>"<strong>" {printf("\\textmd{");}

<OL>"</strong>" {printf("}");}

<OL>"<sup>" {printf("\\textsuperscript{");}

<OL>"</sup>" {printf("}");}

<OL>"<sub>" {printf("\\textsubscript{");}

<OL>"</sub>" {printf("}");}

<OL>"</ol>" {

printf("\\end{enumerate}\n");
BEGIN 0;

}

    /*
        If the analyser finds "<ul>" it begins the matching for UL and it will 
        continue to match based on other rules it finds with the "<UL>" format.
        if it is a formatting it replaces it with its respective match for latex 
        and if it a newline or possibly a newline with a carrage return (for windows)
        it will replace with a newline, and if it is any character it just prints out that character.
        it returns when it sees a "</ul>"
    */

"<ul>" {

    printf("\\begin{itemize}");
    BEGIN UL;

}
<UL>[ \t] {

    printf("%s",yytext);

}

<UL>[\n](\r)? {

    printf( "\n" );
}

<UL>"<li>"  {printf("\\item ");}

<UL>"</li>"  {printf("\n");}

<UL>. {printf("%s",yytext);}

<UL>"<big>" {printf("{\\Large ");}

<UL>"</big>" {printf("}");}

<UL>"<small>" {printf("{\\scriptsize ");}

<UL>"</small>" {printf("}");}

<UL>"<i>" {printf("\\textit{");}

<UL>"</i>" {printf("}");}

<UL>"<b>" {printf("\\textbf{");}

<UL>"</b>" {printf("}");}

<UL>"<em>" {printf("\\emph{");}

<UL>"</em>" {printf("}");}

<UL>"<strong>" {printf("\\textmd{");}

<UL>"</strong>" {printf("}");}

<UL>"<sup>" {printf("\\textsuperscript{");}

<UL>"</sup>" {printf("}");}

<UL>"<sub>" {printf("\\textsubscript{");}

<UL>"</sub>" {printf("}");}

<UL>"</ul>" {

printf("\\end{itemize}\n");
BEGIN 0;

}

    /*
        finds the "<pre>" and because its formatted it prints everything it finds. It only ends when it 
        see's "</pre>"
    */

"<pre>" {

    printf("\\begin{verbatim}");
    BEGIN PRE;

}
<PRE>. {
    printf("%s",yytext);
}
<PRE>"</pre>" {

    printf("\\end{verbatim}\n");
    BEGIN 0;
}
    /*
        If the analyser finds "<p>" it begins the matching for PARA and it will 
        continue to match based on other rules it finds with the "<PARA>" format.
        if it is a formatting it replaces it with its respective match for latex 
        and if it a newline or possibly a newline with a carrage return (for windows)
        it will replace with a newline, and if it is any character it just prints out that character.
        it returns when it sees a "</p>"
    */

"<p>" {

    BEGIN PARA;
}

<PARA>[ \t] {

    printf("%s",yytext);

}

<PARA>[\n](\r)? {

    printf( "\n" );
}

<PARA>. {

    printf("%s",yytext);
}

<PARA>"<big>" {printf("{\\Large ");}

<PARA>"</big>" {printf("}");}

<PARA>"<small>" {printf("{\\scriptsize ");}

<PARA>"</small>" {printf("}");}

<PARA>"<i>" {printf("\\textit{");}

<PARA>"</i>" {printf("}");}

<PARA>"<b>" {printf("\\textbf{");}

<PARA>"</b>" {printf("}");}

<PARA>"<em>" {printf("\\emph{");}

<PARA>"</em>" {printf("}");}

<PARA>"<strong>" {printf("\\textmd{");}

<PARA>"</strong>" {printf("}");}

<PARA>"<sup>" {printf("\\textsuperscript{");}

<PARA>"</sup>" {printf("}");}

<PARA>"<sub>" {printf("\\textsubscript{");}

<PARA>"</sub>" {printf("}");}

<PARA>"</p>" {
    printf("\n\n");
    BEGIN 0;
}
    /*
        Below is what was given to us
    */
"<!--" {
    /**************************************************************************
     * Matched an HTML comment so print it out as a LateX comment. The
     * beginning and ending tags are stripped off before the LateX comment
     * is emitted.
     *************************************************************************/
    printf( "%% " );
    BEGIN COMMENT;
}

[ \t\n\r]+ {
    /**************************************************************************
     * Matched some whitespace that is not inside of an HTML tag. We
     * just ignore the whitespace.
     *************************************************************************/
}

. {
    /**************************************************************************
     * Matched something that we did not expect to see. Issue an error and
     * exit the program with a failure code.
     *************************************************************************/
    fprintf( stderr, "Unexpected input at line %d: '%s'\n", yylineno, yytext );
    exit( 1 );
}

<COMMENT>"-->" {
    /**************************************************************************
     * Matched an HTML end comment while parsing an HTML comment. Print out
     * a new line and resume normal parsing.
     *************************************************************************/
    printf( "\n" );
    BEGIN 0;
}

<COMMENT>[\n](\r)? {
    /**************************************************************************
     * Matched a newline while parsing an HTML comment. Print out a new
     * line making sure to mark the next line as a comment as well.
     *************************************************************************/
    printf( "\n%% " );
}

<COMMENT>[ \t] {
    /**************************************************************************
     * Matched some white space while parsing an HTML comment. Print out
     * the white space as is.
     *************************************************************************/
    printf( "%s", yytext );
}

<COMMENT>. {
    /**************************************************************************
     * Matched any other text while parsing an HTML comment. Print out
     * the text as is.
     *************************************************************************/
    printf( "%s", yytext );
}
%%

/**************************************************************************
 * The main function for the HTML to LateX converter. Here we do three
 * things:
 *  1. Print out the LateX document header.
 *  2. Invoke the lexer to print out the LateX document
 *  3. Print out the LateX footer.
 *************************************************************************/
 

int main( int argc, const char *argv[] ) {
    printf( "\\documentclass[12pt]{article}\n" );
    printf( "\\usepackage{fixltx2e}\n" );
    printf( "\n" );
    printf( "\\setlength{\\parindent}{0.0in}\n" );
    printf( "\\setlength{\\parskip}{0.125in}\n" );
    printf( "\n\n" );
    printf( "\\begin{document}\n" );
    yylex();
    printf( "\\end{document}\n" );
    return 0;
}
