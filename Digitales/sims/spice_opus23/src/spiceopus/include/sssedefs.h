// Definitions for steady state analysis by shooting with extrapolation.
// Author: Janez Puhan

#ifndef SSSE

#define SSSE

#include "jobdefs.h"
#include "cktdefs.h"

typedef struct
{
	int JOBtype;
	JOB *JOBnextJob;
	char *JOBname;
	IFnode SSSEposNode;
	IFnode SSSEnegNode;
	double SSSElevel;
	double SSSEstep;
	double SSSEskip;
	int SSSEperiods;
	int SSSEhistory;
	GENERIC *SSSEplot;
} SSSEan;

#define SSSE_POSNODE	1
#define SSSE_NEGNODE	2
#define SSSE_LEVEL		3
#define SSSE_STEP		4
#define SSSE_SKIP		5
#define SSSE_PERIODS	6
#define SSSE_HISTORY	7

extern int SSSEaskQuest();
extern void collect_results(CKTcircuit *ckt, double *out1, double *out2, int *level,
	int *direction, int *wait, int new_level);
extern void check_level(CKTcircuit *ckt, double *prev, double *out1, double *t1,
	double *out2, double *t2, int level, int direction, int *wait, int *new_level,
	int *timestep);

#endif	// SSSE
