//////////
// 1. Added MIFunsetup prototype.
// Author: Arpad Buermen
//////////

#ifndef MIFPROTO
#define MIFPROTO

/* ===========================================================================
FILE    MIFproto.h

MEMBER OF process XSPICE

Copyright 1991
Georgia Tech Research Corporation
Atlanta, Georgia 30332
All Rights Reserved

PROJECT A-8503

AUTHORS

    9/12/91  Bill Kuhn

MODIFICATIONS

    <date> <person name> <nature of modifications>

SUMMARY

    This file contains ANSI C function prototypes for functions in the
    MIF package.

INTERFACES

    None.

REFERENCED FILES

    None.

NON-STANDARD FEATURES

    None.

=========================================================================== */



#include "ifsim.h"
#include "inpdefs.h"
#include "smpdefs.h"
#include "cktdefs.h"
#include "miftypes.h"



extern void MIF_INP2A(
    GENERIC      *ckt,      /* circuit structure to put mod/inst structs in */
    INPtables    *tab,      /* symbol table for node names, etc.            */
    card         *current   /* the card we are to parse                     */
);


extern char * MIFgetMod(
    GENERIC   *ckt,
    char      **name,
    INPmodel  **model,
    INPtables *tab 
);


extern IFvalue * MIFgetValue(
    GENERIC   *ckt,
    char      **line,
    int       type,
    INPtables *tab,
    char      **err 
);


extern int MIFsetup(
    SMPmatrix     *matrix,
    GENmodel      *inModel,
    CKTcircuit    *ckt,
    int           *state 
);

// Added by Arpad Buermen
extern int MIFunsetup(GENmodel*, CKTcircuit*);

extern int MIFload(
    GENmodel      *inModel,
    CKTcircuit    *ckt 
);


extern int MIFmParam(
    int param_index,
    IFvalue *value,
    GENmodel *inModel 
);

extern int MIFask(
    CKTcircuit *ckt,
    GENinstance *inst,
    int param_index,
    IFvalue *value,
    IFvalue *select
);

extern int MIFmAsk(
    CKTcircuit *ckt,
    GENmodel *inModel,
    int param_index,
    IFvalue *value
);

extern int MIFtrunc(
    GENmodel   *inModel,
    CKTcircuit *ckt,
    double     *timeStep
);

extern int MIFconvTest(
    GENmodel   *inModel,
    CKTcircuit *ckt
);

extern int MIFdelete(
    GENmodel *inModel,
    IFuid    name,
    GENinstance  **inst
);

extern int MIFmDelete(
    GENmodel **inModel,
    IFuid    modname,
    GENmodel *model
);

extern void MIFdestroy(
    GENmodel **inModel
);

extern char  *MIFgettok(
    char **s
);


extern char  *MIFget_token(
    char **s,
    Mif_Token_Type_t *type
);


extern Mif_Cntl_Src_Type_t MIFget_cntl_src_type(
    Mif_Port_Type_t in_port_type,
    Mif_Port_Type_t out_port_type
);

extern char *MIFcopy(char *);


#endif  /* MIFPROTO */
