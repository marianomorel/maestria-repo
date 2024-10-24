//////////
// Modifications in the original code:
// 1.	Added filehiertree structure pointer to line structure. It tells which file
//		this line belongs to.
// 2.	Removed struct line.
// Author: Arpad Buermen
//////////

/**********
Copyright 1990 Regents of the University of California.  All rights reserved.
Author: 1985 Wayne A. Christopher, U. C. Berkeley CAD Group
**********/

/*
 *
 * Note that this definition must be the same as struct card in INPdefs.h...
 */

#ifndef FTEinput_h
#define FTEinput_h

#include "inpdefs.h"

// We don't need struct line anymore.
/*
struct line {
	int li_linenum;
	char *li_line;
	char *li_error;
	struct line *li_next;
	struct line *li_actual;
	struct FileHierTree *li_file;
} ;
*/

/* Listing types. */

#define LS_LOGICAL  1
#define LS_PHYSICAL 2
#define LS_DECK  3

#endif /* FTEinput_h */

