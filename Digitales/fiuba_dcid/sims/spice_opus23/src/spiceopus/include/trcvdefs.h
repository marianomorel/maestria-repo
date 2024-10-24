//////////
// Modifications in the original code:
// 1.	Added sweep for arbitrary non-vector model/instance parameter (TRCVswType[]
//		and TRCVvpName[]).
// Author: Arpad Buermen
//////////

/**********
Copyright 1990 Regents of the University of California.  All rights reserved.
Author: 1985 Thomas L. Quarles
**********/
/*
 */
#ifndef DCTR
#define DCTR "trcvdefs.h $Revision: 1.1 $  on $Date: 91/04/02 11:26:46 $ "


#include "jobdefs.h"
#include "tskdefs.h"
#include "gendefs.h"
    /*
     * structures used to describe D.C. transfer curve analyses to
     * be performed.
     */

#define TRCVNESTLEVEL 2 /* depth of nesting of curves - 2 for spice2 */

typedef struct {
    int JOBtype;
    JOB *JOBnextJob;
    char *JOBname;
    double TRCVvStart[TRCVNESTLEVEL];   /* starting voltage/current */
    double TRCVvStop[TRCVNESTLEVEL];    /* ending voltage/current */
    double TRCVvStep[TRCVNESTLEVEL];    /* voltage/current step */
    double TRCVvSave[TRCVNESTLEVEL];    /* voltage of this source BEFORE 
                                         * analysis-to restore when done */
    int TRCVgSave[TRCVNESTLEVEL];    /* dcGiven flag; as with vSave */
    IFuid TRCVvName[TRCVNESTLEVEL];     /* source (instance/model) being varied */
    GENinstance *TRCVvElt[TRCVNESTLEVEL];   /* pointer to source */
    int TRCVvType[TRCVNESTLEVEL];   /* type of element being varied */
    int TRCVset[TRCVNESTLEVEL];     /* flag to indicate this nest level used */
    int TRCVnestLevel;      /* number of levels of nesting called for */
    int TRCVnestState;      /* iteration state during pause */
	int TRCVswType[TRCVNESTLEVEL];		// Sweep type (0=instance, 1=model)
	IFuid TRCVvpName[TRCVNESTLEVEL];	// Parameter name
	int TRCVvecIndex[TRCVNESTLEVEL];    // Vector parameter index
	int TRCVparIndex[TRCVNESTLEVEL];    // Parameter index in inst/mod par. table
	GENmodel *TRCVvMod[TRCVNESTLEVEL];   /* pointer to source */
	int TRCVswScale[TRCVNESTLEVEL];     // 0=lin, 1=linstep, 2=decstep, 3=octstep
	int TRCVswPts[TRCVNESTLEVEL];       // sweep points
} TRCV;

#define DCT_START1 1
#define DCT_STOP1 2
#define DCT_STEP1 3
#define DCT_NAME1 4
#define DCT_TYPE1 5
#define DCT_START2 6
#define DCT_STOP2 7
#define DCT_STEP2 8
#define DCT_NAME2 9
#define DCT_TYPE2 10
#define DCT_SWTYPE1 11
#define DCT_SWTYPE2 12
#define DCT_PARNAME1 13
#define DCT_PARNAME2 14
#define DCT_INDEX1 15
#define DCT_INDEX2 16
#define DCT_STT1 17
#define DCT_STT2 18
#define DCT_PTS1 19
#define DCT_PTS2 20

#define DCT_LIN     0
#define DCT_LINSTEP 1
#define DCT_DECSTEP 2
#define DCT_OCTSTEP 3

#endif /*DCTR*/
