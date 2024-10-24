//////////
// Modifications in the original code:
// 1.	errMsg pointer has to be released before another use.
// Author: Janez Puhan
//////////

/**********
Copyright 1990 Regents of the University of California.  All rights reserved.
Author: 1985 Thomas L. Quarles
**********/

#ifndef UTIL
#define UTIL "util.h $Revision: 1.1 $  on $Date: 91/04/02 11:27:10 $ "

#ifdef HAS_STDLIB
#	ifndef _STDLIB_INCLUDED
#		define _STDLIB_INCLUDED
#		include <stdlib.h>
#	endif
#else
#endif

#include "unimem.h"

#define TRUE 1
#define FALSE 0

#ifdef DEBUG
#define DEBUGMSG(textargs) { fprintf(spice_out,textargs);fflush(spice_out); }
#else
#define DEBUGMSG(testargs) 
#endif

#ifdef HAS_NOINLINE
#define FABS(a) fabs(a)
double fabs();
#else
#define FABS(a) ( ((a)<0) ? -(a) : (a) )
#endif

#ifdef HAS_UNDERSCORE_ISNAN
#define isnan _isnan
#endif

/* XXX Move these into the above ifdef someday */
#define MIN(a,b) ((a) < (b) ? (a) : (b))
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define SIGN(a,b) ( b >= 0 ? (a >= 0 ? a : - a) : (a >= 0 ? - a : a))

#define ABORT() fflush(spice_err);fflush(spice_out);abort();

#define ERROR(CODE,MESSAGE)	{					      \
	FREE(errMsg);	\
	errMsg = MALLOC(strlen(MESSAGE) + 1);				      \
	strcpy(errMsg, (MESSAGE));					      \
	return (CODE);							      \
	}

#define	NEW(TYPE)	((TYPE *) MALLOC(sizeof(TYPE)))
#define	NEWN(TYPE,COUNT) ((TYPE *) MALLOC(sizeof(TYPE) * (COUNT)))

#ifndef PI
#define PI 3.14159265358979323846
#endif /*PI*/

#endif /*UTIL*/

#define	R_NORM(A,B) {							      \
	if ((A) == 0.0) {						      \
	    (B) = 0;							      \
	} else {							      \
	    while (FABS(A) > 1.0) {					      \
		(B) += 1;						      \
		(A) /= 2.0;						      \
	    }								      \
	    while (FABS(A) < 0.5) {					      \
		(B) -= 1;						      \
		(A) *= 2.0;						      \
	    }								      \
	}								      \
    }
