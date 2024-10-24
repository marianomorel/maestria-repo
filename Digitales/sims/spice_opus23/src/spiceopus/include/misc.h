//////////
// Modifications in the original code:
// 1.	Macro definition eq() which calls strcmp() function was modified. Neither of
//		the parameters passed to strcmp() function must be NULL or the function
//		crashes. The macro is modified so the NULL parameters are allowed.
// 2.	Random number generator is added in the file misc/random.c. Therefore
//		srand() and rand() functions are no longer needed. The code is properly
//		modified for that reason. Extern declarations for new functions ran(),
//		gauss(), read_state() and write_state() are added.
// 3.	Function number_limit() checking double number for not a number, positive or
//		negative infinity and correcting (limiting) it added in number.c. Extern
//		declaration is added here.
// 4.	Fixed buffer length BSIZE_SP temporarily increased. Begging for trouble here
//		by using fixed length buffers. Should get rid of them in future.
// 5.	Extern declarations for functions read_calculated() and write_calculated()
//		added. They implement reading and writing of calculated points in previous
//		optimisation runs, which are used for determining new initial point
//		(initial_guess option).
// Author: Janez Puhan
//////////
// 6.	#ifdef HAS_BCOPY fix weird behaviour at compiling. This was noticed and
//		reported by Linux user who first ported Berkeley's Spice3f4 source code to
//		Linux. Sorry, but I forgot his name.
// 7.	#ifndef HAS_SYSERRLIST prevent repeated declaration of sys_errlist which is
//		already declared in stdio.h.
// Author: Arpad Buermen
//////////

/**********
Copyright 1990 Regents of the University of California.  All rights reserved.
**********/

#include "port.h"

#ifndef MISC_H
#define MISC_H

// #define BSIZE_SP      4096	// Original code.
#define BSIZE_SP 16384	// BSIZE_SP increased.

#ifdef HAS_EXIT1
#  define EXIT_NORMAL 1
#  define EXIT_BAD    0
#else
#  define EXIT_NORMAL 0
#  define EXIT_BAD    1
#endif

#ifdef HAS_CTYPE
#  ifndef isalpha
#    include <ctype.h>
#  endif
#endif

// #define eq(a,b) (!strcmp((a), (b)))	// Original code.
// NULL parameters are now allowed in eq() macro.
#define eq(a,b) (((a) && (b)) ? !strcmp((a), (b)) : ((!(a) && !(b)) ? 1 : 0))
#define eqc(a,b)  (cieq((a), (b)))
#define isalphanum(c)   (isalpha(c) || isdigit(c))
#define hexnum(c) ((((c) >= '0') && ((c) <= '9')) ? ((c) - '0') : ((((c) >= \
        'a') && ((c) <= 'f')) ? ((c) - 'a' + 10) : ((((c) >= 'A') && \
        ((c) <= 'F')) ? ((c) - 'A' + 10) : 0)))

#include "strext.h"

#include "unimem.h"

extern char *copy_internal();
extern char *gettok();
extern void appendc(char *s, char c);
extern int scannum();
extern int prefix();
extern int ciprefix();
extern int cieq();
extern void strtolower();
extern int substring();
extern char *tilde_expand( );
extern void cp_printword();

extern char *datestring();
extern double seconds();
extern double clock_seconds();

extern char *smktemp();

extern void setran(long int);
extern long int getran();
extern double ran();	// Declaration of functions for generating random numbers.
extern double gauss();
extern void read_state(FILE *file);
extern void write_state(FILE *file);
// Reading and writing of calculated points in previous optimisation runs.
extern void read_calculated(FILE *file);
extern void write_calculated(FILE *file);
extern void number_limit();	// Declaration for double number checking function.

int isAbsolutePath(char *);
int getCurrentDir(char *, int);
void slashToLocalPath(char *);
void localPathToSlash(char *);
void stripFileName(char *);
char *dirCat(char *, char *);

/* Externs from libc */

#ifdef HAS_UNISTD
#  include <unistd.h>
#endif

#ifdef HAS_STDLIB

#  ifndef _STDLIB_INCLUDED
#    define _STDLIB_INCLUDED
#    include <stdlib.h>
#  endif
//////////
// Original code (not needed any more since we have new random number generator):
//	#  ifndef HAS_BSDRAND
//		#    define random	rand
//		#    define srandom	srand
//	#  endif
//////////
#  ifdef HAS_DOSDIRS
// char *getcwd( );
#include <direct.h>
#  endif

#else

//////////
// Original code (not needed any more since we have new random number generator):
//	#  ifdef HAS_BSDRAND
//	extern long random();
//	extern void srandom();
//	#  else
//	#    define random	rand
//	#    define srandom	srand
//	#  endif
//////////

// extern char *calloc();
// extern char *malloc();
// extern char *realloc();
extern char *getenv();
extern int errno;
//////////
// Declaration of  sys_errlist is sometimes not needed since it is already declared
// in stdio.h.
//////////
#ifndef HAS_SYS_ERRLIST
extern char *sys_errlist[];
#endif
extern char *getenv();
extern char *getwd();
// extern int rand();
// extern int srand();
extern int atoi();
extern int kill();
// extern int getpid();
// extern int qsort();
#  ifdef notdef
extern void exit();
#  endif

#  ifdef HAS_GETCWD
extern char *getcwd( );
#  endif

#  ifdef HAS_CLEARERR
#    ifndef clearerr
extern void clearerr();
#    endif /* clearerr */
#  endif /* HAS_CLEARERR */

#ifndef HAS_BCOPY	// Added for compiling under Linux.
#  ifndef bzero
extern int bzero();
#  endif
#  ifndef bcopy
extern void bcopy();
#  endif
#endif	// HAS_BCOPY

#  ifndef index
#    ifdef HAS_INDEX
extern char *rindex();
extern char *index();
#    else
#      ifdef HAS_STRCHR
extern char *strchr();
extern char *strrchr();
#      else
#      endif
#    endif
#  endif

#endif	/* else STDLIB */

#ifndef HAS_INDEX
#  ifndef index
#    ifdef HAS_STRCHR
#      define	index	strchr
#      define	rindex	strrchr
#    endif
#  endif
#endif

#ifdef HAS_TIME_
#  ifdef HAS_BSDTIME
extern char *timezone();
#  endif
extern char *asctime();
extern struct tm *localtime();
#endif
//////////
// Original code:
//	#ifndef HAS_MEMAVL
//	#  ifdef HAS_RLIMIT_
//		extern char *sbrk();
//	#  endif
//	#endif
//////////
#define false 0
#define true 1

#ifdef HAS_DOSDIRS
typedef	int	DIR;
struct direct {
	int	d_reclen;
	short	d_ino;
	short	d_namelen;
	char	d_name[20];
	};

#  ifdef __STDC__
extern DIR *opendir(char *);
extern struct direct *readdir(DIR *);
#  else
extern DIR *opendir( );
extern struct direct *readdir( );
#  endif

#endif

#ifndef HAS_STRICMP
#define stricmp(a,b) strcasecmp(a,b)
#endif

#endif /* MISC_H */
