//////////
// Modifications in the original code:
// 1.	Removed struct subcirc.
// 2.	Changed struct line to struct card in circ.
// Author: Arpad Buermen
//////////

/**********
Copyright 1990 Regents of the University of California.  All rights reserved.
Author: 1985 Wayne A. Christopher, U. C. Berkeley CAD Group
**********/

/*
 *
 * General front end stuff.
 */
#ifndef FTEdefs_h
#define FTEdefs_h

#define DEF_WIDTH   80	/* Line printer width. */
#define DEF_HEIGHT  60  /* Line printer height. */
#define IPOINTMIN   20  /* When we start plotting incremental plots. */
#include "fteparse.h"
#include "fteinp.h"

/* The curcuits that are currently available to the user. */

struct circ {
	char *ci_name;    /* What the circuit's designator is. */
	char *ci_title;    /* What the circuit can be called. */
    char *ci_ckt;      /* The CKTcircuit structure. */
    INPtables *ci_symtab;    /* The INP symbol table. */
    struct card *ci_deck;   /* The input deck. */
	int ci_deck_errors;
    struct card *ci_origdeck;/* The input deck, before subckt expansion. */
	int ci_origdeck_errors;
    struct card *ci_options;/* The .option cards from the deck... */
	int ci_options_errors;
    struct variable *ci_vars; /* ... and the parsed versions. */
    BOOL ci_inprogress; /* We are in a break now. */
    BOOL ci_runonce;    /* So com_run can do a reset if necessary... */
    wordlist *ci_commands;  /* Things to do when this circuit is done. */
    struct circ *ci_next;   /* The next in the list. */
    char *ci_nodes;     /* ccom structs for the nodes... */
    char *ci_devices;   /* and devices in the circuit. */
    char *ci_filename;  /* Where this circuit came from. */
    char *ci_defTask;   /* the default task for this circuit */
    char *ci_specTask;  /* the special task for command line jobs */
    char *ci_curTask;   /* the most recent task for this circuit */
    char *ci_defOpt;    /* the default options anal. for this circuit */
    char *ci_specOpt;   /* the special options anal. for command line jobs */
    char *ci_curOpt;    /* the most recent options anal. for the circuit */
} ;

// struct subcirc {
//     char *sc_name;  /* Whatever... */
// } ;

struct save_info {
    char	*name;
    IFuid	*analysis;
    int		used;
};

#define mylog10(xx) (((xx) > 0.0) ? log10(xx) : (- log10(HUGE)))

#include "fteext.h"

#endif /* FTEdefs_h */
