//////////
// Modifications in the original code:
// 1.	Structure _complex is renamed into _complex_old. Therefore type complex now
//		equals to structure _complex_old and not to structure _complex as it is the
//		case in the original code. Structure _complex_old is also used in macros
//		realpart() and imagpart(). The change was done because structure _complex is
//		also defined in standard library math.h. 
// Author: Janez Puhan
//////////
// 2.	Function setenv() is defined in the stdlib.h standard library and therefore
//		does not need an extern declaration.
// Author: Arpad Buermen
//////////

/**********
Copyright 1990 Regents of the University of California.  All rights reserved.
Author: 1986 Wayne A. Christopher, U. C. Berkeley CAD Group
**********/

/*
 * Standard definitions. This file serves as the header file for std.c and
 * wlist.c
 */

#ifndef _STD_H_
#define _STD_H_

typedef int BOOL;

#include "misc.h"

#ifndef FILE
/* XXX Bogus */
#  include <stdio.h>
#endif

/* Doubly linked lists of words. */

struct wordlist {
    char *wl_word;
    struct wordlist *wl_next;
    struct wordlist *wl_prev;
	char wl_prot;
} ;

typedef struct wordlist wordlist;

/* Complex numbers. */

struct _complex_old {   /* IBM portability... */
    double cx_real;
    double cx_imag;
} ;

typedef struct _complex_old complex;

#define realpart(cval)  ((struct _complex_old *) (cval))->cx_real
#define imagpart(cval)  ((struct _complex_old *) (cval))->cx_imag

/* Externs defined in std.c */

extern char *getusername();
extern char *gethome();
extern char *tildexpand();
extern char *printnum();
extern int cp_numdgt;
extern void fatal();
// extern void setenv();	// Included in standard library stdlib.h.
extern void cp_printword(char *string, FILE *fp);

/* Externs from wlist.c */

extern char **wl_mkvec();
extern char *wl_flatten();
extern int wl_length();
extern void wl_free();
extern void wl_print();
extern void wl_sort();
extern wordlist *wl_append();
extern wordlist *wl_build();
extern wordlist *wl_copy();
extern wordlist *wl_range();
extern wordlist *wl_nthelem();
extern wordlist *wl_reverse();
extern wordlist *wl_splice();

#endif /* _STD_H_*/
