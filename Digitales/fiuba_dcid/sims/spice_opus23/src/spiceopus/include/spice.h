//////////
// Modifications in the original code:
// 1.	Extern declaration of Spice_Version is modified. Spice_Version is now array
//		of strings corresponding to different versions.
// 2.	Extern declaration of global variables light_version and
//		optimisation_included added to distinguish among different compilation
//		types.
// Authors: Janez Puhan, Arpad Buermen
//////////

/*
 *	Portability, global externs, kitchen sink (yuk).
 *	In future releases this will include things from misc.h and util.h,
 *	   which duplicate each other in places
 */

#include <math.h>

#ifndef	M_PI
#  define M_PI		3.14159265358979323846
#endif
#ifndef	M_E
#  define M_E  	   2.7182818284590452354
#endif
#ifndef	M_LOG2E
#  define M_LOG2E		1.4426950408889634074
#endif
#ifndef	M_LOG10E
#  define M_LOG10E        0.43429448190325182765
#endif

#include "port.h"
#include "hw.h"
#include "config.h"
#include "capabil.h"
#include <stdio.h>

#define	NUMELEMS(ARRAY)	(sizeof(ARRAY)/sizeof(*ARRAY))

extern void error_msg_out(const char *);

extern char *iof_fgets(char *, int, FILE *);

extern FILE *spice_out;
extern FILE *spice_in;
extern FILE *spice_err;
extern FILE *cmd_out; 

extern void sp_exit(int);
extern void sp_key();

extern char *Spice_Exec_Dir;
extern char *Spice_Lib_Dir;
extern char *Spice_Lock_Name;
extern char Spice_OptChar;
extern char *Def_Editor;
extern char *Bug_Addr;
extern int AsciiRawFile;
extern char *Spice_Host;
extern char *Spiced_Log;

extern char Spice_Notice[ ];
// extern char Spice_Version[ ];	// Original code.
extern char *Spice_Version[];	// Spice_Version is now array of strings.
extern char Spice_Build_Date[ ];

extern char *News_File;
extern char *Default_MFB_Cap;
extern char *Spice_Path;
extern char *Help_Path;
extern char *Lib_Path;
extern int  Patch_Level;

extern int light_version, optimisation_included;	// For compilation type.
