//////////
// Modifications in the original code:
// 1.	Elements for options icstep, rmax, rmin, fs, ft, lvltim, itl3, xmu, xmumult,
//		trapratio, integdebug, scale, pziter, defpd, defps, defnrd, defnrs,
//		nosrclift, noinitsrcl, opdebug, sollimdebug, gminpriority, srcspriority,
//		srclpriority, nsfactor, nssteps, matrixcheck, voltagelimit, cmin, cminsteps,
//		cshunt, sollim, sollimiter, noconviter, defmodcheck, definstcheck,
//		nofloatnodescheck, dcap, nopredictor, newtrunc, relq, gmindc, noautoconv,
//		slopetol, absvar, relvar, sssetol and resmin added into structure TSKtask.
// 2.	Options minbreak and delmin are obsolete and therefore commented out.
// 3.	TSKbypassGiven, TSKrmaxGiven, TSKlvltimGiven and TSKslopetolGiven elements
//		added into structure TSKtask for automatic setting of bypass, rmax, lvltim
//		and slopetol options. Options bypass and lvltim are set regarding to method
//		option. Options rmax and slopetol are set regarding to lvltim option.
// 4.	Values for TSKcurrentAnalysis moved into cktdefs.h.
// 5.	Macro NEWTRUNC is obsolete. It is replaced by newtrunc option.
// Author: Janez Puhan
//////////
// 6.	Added UIC tran convergence helper options (srcl).
// Author: Arpad Buermen
//////////

/**********
Copyright 1990 Regents of the University of California.  All rights reserved.
Author: 1985 Thomas L. Quarles
**********/
/*
 */
#ifndef TSK
#define TSK "tskdefs.h $Revision: 1.1 $  on $Date: 91/04/02 11:26:47 $ "


#include "jobdefs.h"

typedef struct {
    JOB taskOptions;    /* job structure at the front to hold options */
    JOB *jobs;
    char *TSKname;
    double TSKtemp;
    double TSKnomTemp;
    int TSKmaxOrder;        /* maximum integration method order */
    int TSKintegrateMethod; /* the integration method to be used */
	// int TSKcurrentAnalysis; /* the analysis in progress (if any) */	// Not used.
//////////
// Moved to cktdefs.h.
//	/* defines for the value of  TSKcurrentAnalysis */
//	#define DOING_DCOP 1
//	#define DOING_TRCV 2
//	#define DOING_AC   4
//	#define DOING_TRAN 8
//////////
    int TSKbypass;
    int TSKdcMaxIter;       /* iteration limit for dc op.  (itl1) */
    int TSKdcTrcvMaxIter;   /* iteration limit for dc tran. curv (itl2) */
	int TSKtranMinIter;	// For itl3 option.
    int TSKtranMaxIter;     /* iteration limit for each timepoint for tran*/
                            /* (itl4) */
	double TSKxmu;	// Trapeziodal integration algorithm coefficient.
	double TSKxmuMult;	// Multiplicator of xmu in case of numerical oscillations.
	double TSKtrapRatio;	// Ratio for detecting numerical oscillations.
	unsigned int TSKintegDebug : 1;	// Print numerical oscillations messages flag.
    int TSKnumSrcSteps;     /* number of steps for source stepping */
	int TSKsrcsPriority;	// srcspriority option.
    int TSKnumGminSteps;    /* number of steps for Gmin stepping */
	int TSKgminPriority;	// gminpriority option.
	int TSKnumCminSteps;	// cminsteps option.
	// double TSKminBreak;	// Not used.
    double TSKabstol;
    double TSKpivotAbsTol;
    double TSKpivotRelTol;
    double TSKreltol;
    double TSKchgtol;
    double TSKvoltTol;
	double TSKslopeTol;	// slopetol option.
	double TSKabsVar;	// absvar option.
	double TSKrelVar;	// relvar option.
	double TSKssseTol;	// Tolerance multiplier for steady state analysis.
	// Maximal voltage in per-iteration voltage limit functions.
	double TSKvoltageLimit;
	double TSKrelQ;	// relq option.
// #ifdef NEWTRUNC	// Original code.
    double TSKlteReltol;
    double TSKlteAbstol;
// #endif /* NEWTRUNC */	// Original code.
	int TSKnewTrunc;	// For newtrunc option.
	int TSKnoPredictor;	// For nopredictor option.
	int TSKdcap;	// For dcap option.
    double TSKgmin;
	double TSKgmindc;	// gmindc option.
	double TSKresmin;	// resmin option.
	double TSKcmin;	// cmin option.
	double TSKcshunt;	// cshunt option.
	// double TSKdelmin;	// Not used.
    double TSKtrtol;
    double TSKdefaultMosL;
    double TSKdefaultMosW;
    double TSKdefaultMosAD;
    double TSKdefaultMosAS;
	double TSKdefaultMosPD;	// defpd option.
	double TSKdefaultMosPS;	// defps option.
	double TSKdefaultMosNRD;	// defnrd option.
	double TSKdefaultMosNRS;	// defnrs option.
	int TSKdefaultModCheck;	// defmodcheck option.
	int TSKdefaultInstCheck;	// definstcheck option.
	double TSKicStep;	// icstep option.
	int TSKlvlTim;	// lvltim option.
	double TSKrMax;	// rmax option.
	double TSKrMin;	// rmin option.
	double TSKfs;	// fs option.
	double TSKft;	// ft option.
	double TSKscale;	// scale option.
	int TSKpzIter;	// pziter option.
	int TSKsrclMaxIter;	// UIC tran convergence helper.
	int TSKsrclPriority;	// srclpriority option.
	int TSKsrclConvIter;
	int TSKsrclRiseIter;
	double TSKnsFactor;	// nsfactor option.
	double TSKnsFactorPart;	// Additional variable used with nsfactor option.
	int TSKnsSteps;	// nssteps option.
	int TSKnoConvIter;	// noconviter option.
	double TSKsolLim;	// sollim option.
	int TSKsolLimIter;	// sollimiter option.
	double TSKsrclRiseTime;
	double TSKsrclMaxTime;
	double TSKsrclMinStep;
    unsigned int TSKbypassGiven : 1;	// bypass option was explicitly given.
    unsigned int TSKrmaxGiven : 1;	// rmax option was explicitly given.
    unsigned int TSKlvltimGiven : 1;	// lvltim option was explicitly given.
    unsigned int TSKslopetolGiven : 1;	// slopetol option was explicitly given.
    unsigned int TSKfixLimit:1;
    unsigned int TSKnoOpIter:1; /* no OP iterating, go straight to gmin step */
    unsigned int TSKnoSrcLift : 1;	// Source lifting in time domain skipped.
    unsigned int TSKnoInitSrcl : 1;	// Skip initial source lifting without cmins.
	unsigned int TSKopDebug : 1;	// Print out messages during the op analysis.
	unsigned int TSKsolLimDebug : 1;	// Print results during solution limiting.
	unsigned int TSKmatrixCheck : 1;	// Check matrix after load.
	unsigned int TSKnoFloatNodesCheck : 1;	// No topology check during setup.
	unsigned int TSKnoAutoConv : 1;	// No automatic options setting.
    unsigned int TSKtryToCompact:1; /* flag for LTRA lines */
    unsigned int TSKbadMos3:1; /* flag for MOS3 models */
    unsigned int TSKkeepOpInfo:1; /* flag for small signal analyses */
}TSKtask;

#endif /*TSK*/
