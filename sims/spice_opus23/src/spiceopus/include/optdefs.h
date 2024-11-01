//////////
// Modifications in the original code:
// 1.	Macros OPT_ICSTEP, OPT_RMAX, OPT_RMIN, OPT_FS, OPT_FT, OPT_LVLTIM,
//		OPT_XMU, OPT_XMUMULT, OPT_TRAPRATIO, OPT_INTEGDEBUG, OPT_SCALE, OPT_PZITER,
//		OPT_DEFPD, OPT_DEFPS, OPT_DEFNRD, OPT_DEFNRS, OPT_NOSRCLIFT, OPT_NOINITSRCL,
//		OPT_OPDEBUG, OPT_SOLLIMDEBUG, OPT_GMINPRIORITY, OPT_SRCSPRIORITY,
//		OPT_SRCLPRIORITY, OPT_NSFACTOR, OPT_NSSTEPS, OPT_MATRIXCHECK,
//		OPT_VOLTAGELIMIT, OPT_CMIN, OPT_CMINSTEPS, OPT_CSHUNT, OPT_SOLLIM,
//		OPT_SOLLIMITER, OPT_NOCONVITER, OPT_DEFMODCHECK, OPT_DEFINSTCHECK,
//		OPT_NOFLOATNODESCHECK, OPT_DCAP, OPT_NOPREDICTOR, OPT_NEWTRUNC, OPT_RELQ,
//		OPT_LTERELTOL, OPT_LTEABSTOL, OPT_ACCT, OPT_OPTS, OPT_GMINDC,
//		OPT_NOAUTOCONV, OPT_SLOPETOL, OPT_ABSVAR, OPT_RELVAR, OPT_SSSETOL and
//		OPT_RESMIN added for icstep, rmax, rmin, fs, ft, lvltim, xmu, xmumult,
//		trapratio, integdebug, scale, pziter, defpd, defps, defnrd, defnrs,
//		nosrclift, noinitsrcl, opdebug, sollimdebug, gminpriority, srcspriority,
//		srclpriority, nsfactor, nssteps, matrixcheck, voltagelimit, cmin, cminsteps,
//		cshunt, sollim, sollimiter, noconviter, defmodcheck, definstcheck,
//		nofloatnodescheck, dcap, nopredictor, newtrunc, relq, ltereltol, lteabstol,
//		acct, opts, gmindc, noautoconv, slopetol, absvar, relvar, sssetol and resmin
//		options.
// 2.	Option minbreak is obsolete and therefore commented out.
// Author: Janez Puhan
//////////
// 3.	Added UIC tran convergence helper options (srcl).
// Author: Arpad Buermen
//////////

/**********
Copyright 1990 Regents of the University of California.  All rights reserved.
Author: 1985 Thomas L. Quarles
**********/

#ifndef OPT
#define OPT "optdefs.h $Revision: 1.6 $  on $Date: 92/08/11 19:08:44 $ "

    /* structure used to describe the statistics to be collected */

typedef struct {

    int STATnumIter;    /* number of total iterations performed */
    int STATtranIter;   /* number of iterations for transient analysis */
    int STAToldIter;    /* number of iterations at the end of the last point */
                        /* used to compute iterations per point */

    int STATtimePts;    /* total number of timepoints */
    int STATaccepted;   /* number of timepoints accepted */
    int STATrejected;   /* number of timepoints rejected */

    double STATtotAnalTime;     /* total time for analysis */
    double STATtranTime;    /* transient analysis time */
    double STATloadTime;    /* time spent in device loading */
    double STATdecompTime;  /* total time spent in LU decomposition */
    double STATsolveTime;   /* total time spent in F-B subst. */
    double STATreorderTime; /* total time spent reordering */
    double STATtranDecompTime;  /* time spent in transient LU decomposition */
    double STATtranSolveTime;   /* time spent in transient F-B Subst. */

} STATistics;

#define OPT_GMIN 1
#define OPT_RELTOL 2
#define OPT_ABSTOL 3
#define OPT_VNTOL 4
#define OPT_TRTOL 5
#define OPT_CHGTOL 6
#define OPT_PIVTOL 7
#define OPT_PIVREL 8
#define OPT_TNOM 9
#define OPT_ITL1 10
#define OPT_ITL2 11
#define OPT_ITL3 12
#define OPT_ITL4 13
#define OPT_ITL5 14
#define OPT_DEFL 15
#define OPT_DEFW 16
#define OPT_DEFAD 17
#define OPT_DEFAS 18
#define OPT_BYPASS 19
#define OPT_MAXORD 20

#define OPT_ITERS 21
#define OPT_TRANIT 22
#define OPT_TRANPTS 23
#define OPT_TRANACCPT 24
#define OPT_TRANRJCT 25
#define OPT_TOTANALTIME 26
#define OPT_TRANTIME 27
#define OPT_LOADTIME 28
#define OPT_DECOMP 29
#define OPT_SOLVE 30
#define OPT_TRANDECOMP 31
#define OPT_TRANSOLVE 32
#define OPT_TEMP 33
#define OPT_OLDLIMIT 34
#define OPT_TRANCURITER 35
#define OPT_SRCSTEPS 36
#define OPT_GMINSTEPS 37
// #define OPT_MINBREAK 38	// Not used.
#define OPT_RMIN 38	// For rmin option.
#define OPT_NOOPITER 39
#define OPT_EQNS 40
#define OPT_REORDTIME 41
#define OPT_METHOD 42
#define OPT_TRYTOCOMPACT 43
#define OPT_BADMOS3 44
#define OPT_KEEPOPINFO 45
#define OPT_NOSRCLIFT 46	// For nosrclift option.
#define OPT_ICSTEP 47	// For icstep option.
#define OPT_SCALE 48	// For scale option.
#define OPT_PZITER 49	// For pziter option.
#define OPT_SRCLMAXITER 50	// For srclmaxiter option.
#define OPT_SRCLCONVITER 51	// For srclconviter option.
#define OPT_SRCLRISEITER 52	// For srclriseiter option.
#define OPT_OPDEBUG 53	// For opdebug option.
#define OPT_SRCLRISETIME 54	// For srclrisetime option.
#define OPT_SRCLMAXTIME 55	// For srclmaxtime option.
#define OPT_SRCLMINSTEP 56	// For srclminstep option.
#define OPT_RMAX 57	// For rmax option.
#define OPT_DEFPD 58	// For defpd option.
#define OPT_DEFPS 59	// For defps option.
#define OPT_DEFNRD 60	// For defnrd option.
#define OPT_DEFNRS 61	// For defnrs option.
#define OPT_GMINPRIORITY 62	// For gminpriority option.
#define OPT_SRCSPRIORITY 63	// For srcspriority option.
#define OPT_SRCLPRIORITY 64	// For srclpriority option.
#define OPT_NSFACTOR 65	// For nsfactor option.
#define OPT_NSSTEPS 66	// For nssteps option.
#define OPT_MATRIXCHECK 67	// For matrixcheck option.
#define OPT_VOLTAGELIMIT 68	// For voltagelimit option.
#define OPT_CMIN 69	// For cmin option.
#define OPT_CMINSTEPS 70	// For cminsteps option.
#define OPT_SOLLIM 71	// For sollim option.
#define OPT_SOLLIMITER 72	// For sollimiter option.
#define OPT_NOINITSRCL 73	// For noinitsrcl option.
#define OPT_CSHUNT 74	// For cshunt option.
#define OPT_DEFMODCHECK 75	// For defmodcheck option.
#define OPT_DEFINSTCHECK 76	// For definstcheck option.
#define OPT_NOFLOATNODESCHECK 77	// For nofloatnodescheck option.
#define OPT_SOLLIMDEBUG 78	// For sollimdebug option.
#define OPT_DCAP 79	// For dcap option.
#define OPT_NOPREDICTOR 80	// For nopredictor option.
#define OPT_RELQ 81	// For relq option.
#define OPT_ACCT 82	// For acct option.
#define OPT_OPTS 83	// For opts option.
#define OPT_GMINDC 84	// For gmindc option.
#define OPT_NOAUTOCONV 85	// For noautoconv option.
#define OPT_ABSVAR 86	// For absvar option.
#define OPT_RELVAR 87	// For relvar option.
#define OPT_FS 88	// For fs option.
#define OPT_FT 89	// For ft option.
#define OPT_LVLTIM 90	// For lvltim option.
#define OPT_NOCONVITER 91	// For noconviter option.
#define OPT_SLOPETOL 92	// For slopetol option.
#define OPT_NEWTRUNC 93	// For newtrunc option.
#define OPT_LTERELTOL 94	// For ltereltol option.
#define OPT_LTEABSTOL 95	// For lteabstol option.
#define OPT_RESMIN 96	// For resmin option.
#define OPT_XMU 97	// For xmu option.
#define OPT_XMUMULT 98	// For xmumult option.
#define OPT_TRAPRATIO 99	// For trapratio option.
#define OPT_SSSETOL 100	// For ssseoption option.
#define OPT_INTEGDEBUG 101	// For integdebug option.
/* gtri - begin - wbk - add new options */
//////////
// Original code:
//	#define OPT_ENH_NOOPALTER           100
//	#define OPT_ENH_RAMPTIME            101
//	#define OPT_EVT_MAX_EVT_PASSES      102
//	#define OPT_EVT_MAX_OP_ALTER        103
//	#define OPT_ENH_CONV_LIMIT          104
//	#define OPT_ENH_CONV_ABS_STEP       105
//	#define OPT_ENH_CONV_STEP           106
//	#define OPT_MIF_AUTO_PARTIAL        107
//	#define OPT_ENH_RSHUNT              108
//////////
// GTRI option numbers changed.
#define OPT_ENH_NOOPALTER		200
#define OPT_ENH_RAMPTIME		201
#define OPT_EVT_MAX_EVT_PASSES	202
#define OPT_EVT_MAX_OP_ALTER	203
#define OPT_ENH_CONV_LIMIT		204
#define OPT_ENH_CONV_ABS_STEP	205
#define OPT_ENH_CONV_STEP		206
#define OPT_MIF_AUTO_PARTIAL	207
#define OPT_ENH_RSHUNT			208
/* gtri - end   - wbk - add new options */

#endif /*OPT*/
