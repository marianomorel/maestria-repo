//////////
// Modifications in the original code:
// 1.	CKTinternals pointer to list of unsetuped internal nodes with defined
//		nodeset or ic conditions is added to CKTcircuit structure. The internal node
//		with defined nodeset or ic is added into the CKTinternals list when it is
//		deleted by CKTdltNNum() function called by device's unsetup function. On the
//		other hand when an internal node is created by CKTmkCur() or CKTmkVolt()
//		functions called by device's setup function its nodeset and ic conditions
//		are set from the identical node in CKTinternals list if one exists and it is
//		removed from the list. CKTinternals list is destroyed when the circuit is
//		deleted. All this voo-doo is needed to allow setting nodesets and ic
//		conditions for internal nodes as well as for ordinary nodes.
// 2.	Options icstep, rmax, rmin, fs, ft, lvltim, itl3, xmu, xmumult, trapratio,
//		integdebug, scale, pziter, defpd, defps, defnrd, defnrs, nosrclift, opdebug,
//		sollimdebug, gminpriority, srcspriority, srclpriority, nsfactor, nssteps,
//		matrixcheck, voltagelimit, noinitsrcl, cmin, cminsteps, sollim, sollimiter,
//		noconviter, cshunt, defmodcheck, definstcheck, nofloatnodescheck, dcap,
//		nopredictor, newtrunc, relq, gmindc, noautoconv, slopetol, absvar, relvar,
//		sssetol and resmin added into the CKTcircuit structure. Extern declaration
//		of global variables for voltagelimit and xmumult options also added.
// 3.	CKTdoNotUseIcAndNodesets flag added to CKTcircuit structure. It is used to
//		prevent using initial conditions and nodesets in convergence aid algorithms
//		when calculating the operating point.
// 4.	CKTsolutionLimit flag added to CKTcircuit structure. The flag is set before
//		call to NIiter() function to indicate that solution limiting should be used
//		in NiconvTest() function. Solution limiting modifies (limits) the solution
//		which is not inside tolerances and fails the convergence test. It is used in
//		very small steps of gmin and source stepping, when we know that new solution
//		is really close to the old one but the Newton-Raphson algorithm probably get
//		caught into a limiting cycle.
// 5.	CKTnumSolOsc added to CKTcircuit structure. It counts direction changes of
//		the first vector on which solution limiting is performed. Counting takes
//		place only is noautoconv option is not set. The count number answers
//		questions: was solution limiting performed in the last gmin or source step
//		and did the oscillations (limiting cycle) occured.
// 6.	CKTsrclNodesets pointer added to CKTcircuit structure. It points to an array
//		of nodeset values which are used after source lifting.
// 7.	CKTcminCap, CKTcminList and CKTcshuntList added into the CKTcircuit
//		structure. The first is current cmin capacitance value, the second and the
//		third are lists of cmins or cshunts added into the circuit. A cshunt
//		structure for capacitance lists is also defined.
// 8.	CKTnodeGroups added into the CKTcircuit structure. It points to a list of
//		groups of nodes which are connected together in dc domain. The array is used
//		during circuit setup to verify circuit topology. Also declarations of
//		functions CKTaddGroup() and CKTaddNodeToGroup() added.
// 9.	CKTmaxFreq added into the CKTcircuit structure. It holds the highest sin or
//		sffm frequency given by the independent voltage or current sources. It is
//		needed for calculating initial and maximal time step in the transient
//		analysis. It is set when a time point is accepted (CKTaccept() function -
//		see ckt/cktaccpt.c).
// 10.	CKTsaveDelta is not used anymore in DCtran() function. Therefore it is
//		commented out.
// 11.	Values for CKTcurrentAnalysis moved from tskdefs.h.
// 12.	Macros NEWTRUNC and PREDICTOR are obsolete. They are replaced by newtrunc
//		and nopredictor options.
// 13.	Declaration for function CKTarea() added. It is needed in area() Nutmeg
//		function.
// 14.	NIpred() and CKTdvdt() function declarations added for predictor corrector
//		and dvdt timstep algorithm.
// 15.	SSSEinit() and DCssse() function declarations added for steady state
//		analysis by shooting with extrapolation. Also CKTposNode, CKTnegNode,
//		CKTlevel, CKTskip, CKTperiods, CKThistory, CKTcallFromSSSE, and CKTssseEps
//		elements added into CKTcircuit structure for that purpose.
// 16.	CKTrhsIcGiven vector of flags added into the CKTcircuit structure. If
//		initial condition is given for the i-th (i is index in CKTrhs vector) node
//		then CKTrhsIcGiven[i] is not zero. Complete information about initial
//		conditions is otherwise in CKTnodes linked list
// Author: Janez Puhan
//////////
// 16.	Added UIC tran convergence helper options (srcl).
// 17.	Added CKTlteCoeff member for the LTE coefficient. 
// 18.	Added CKTlteCoeff member for the LTE coefficient of the predictor. 
// Author: Arpad Buermen
//////////

/*
 * Copyright (c) 1985 Thomas L. Quarles
 */
#ifndef CKT
#define CKT "cktdefs.h $Revision: 1.4 $  on $Date: 91/12/31 11:36:00 $ "

// #define MAXNUMDEVS 32 // Not in xspice

// Added from xspice
/* gtri - evt - wbk - 5/20/91 - add event-driven and enhancements data */
#include "evt.h"
#include "enh.h"
/* gtri - evt - wbk - 5/20/91 - add event-driven and enhancements data */
// End added

extern int DEVmaxnum;
#define MAXNUMDEVNODES 4

#include "smpdefs.h"
#include "ifsim.h"
#include "acdefs.h"
#include "gendefs.h"
#include "trcvdefs.h"
#include "optdefs.h"
#include "sen2defs.h" // This is sendefs.h in xspice
#include "pzdefs.h"

struct cshunt	// For composing capacitance list.
{
	int node;	// Node number (the other node is always ground).
	double *ptr;	// Pointer to the diagonal matrix element.
	int state;	// Indeks in state vectors.
	struct cshunt *next;	// Next capacitance in the list.
};

typedef struct sCKTnode {
    IFuid name;
    int type;

#define SP_VOLTAGE 3
#define SP_CURRENT 4
#define NODE_VOLTAGE SP_VOLTAGE
#define NODE_CURRENT SP_CURRENT

    int number;
    double ic;
    double nodeset;
    double *ptr;
    struct sCKTnode *next;
    unsigned int icGiven:1;
    unsigned int nsGiven:1;
} CKTnode;

/* defines for node parameters */
#define PARM_NS 1
#define PARM_IC 2
#define PARM_NODETYPE 3

struct CKTnodeGroup	// An element in list of node groups.
{
	int num;	// Number of nodes in this group (without ground).
	int *nodes;	// Node numbers.
	int floating;	// If ground was in this group then floating is zero.
	struct CKTnodeGroup *next;	// Next node group.
};

// Number of capacitances where numericall oscillations can occur.
extern unsigned short int num_of_trouble_caps;
extern double voltagelimit_option;	// For voltagelimit option.

typedef struct {
/* gtri - begin - wbk - change declaration to allow dynamic sizing */

/* An associated change is made in CKTinit.c to alloc the space */
/* required for the pointers.  No changes are needed to the source */
/* code at the 3C1 level, although the compiler will generate */
/* slightly different code for references to this data. */

/*  GENmodel *CKThead[MAXNUMDEVS];  */
    GENmodel **CKThead;

/* gtri - end   - wbk - change declaration to allow dynamic sizing */

	int CKTforceZeroTimeValue;	// Source lifting options.
	int CKTsrclPriority;	// For srclpriority option.
	int CKTsrclMaxIter;
	int CKTsrclConvIter;
	int CKTsrclRiseIter;
	double CKTsrclRiseTime;
	double CKTsrclMaxTime;
	double CKTsrclMinStep;
	double *CKTsrclNodesets;	// Nodeset values used after source lifting.
    STATistics *CKTstat;
    double *(CKTstates[8]);
#define CKTstate0 CKTstates[0]
#define CKTstate1 CKTstates[1]
#define CKTstate2 CKTstates[2]
#define CKTstate3 CKTstates[3]
#define CKTstate4 CKTstates[4]
#define CKTstate5 CKTstates[5]
#define CKTstate6 CKTstates[6]
#define CKTstate7 CKTstates[7]
    double CKTtime;
    double CKTdelta;
    double CKTdeltaOld[7];
    double CKTtemp;
    double CKTnomTemp;
    double CKTvt;
    double CKTag[7];        /* the gear variable coefficient matrix */
// #ifdef PREDICTOR	// Original code.
    double CKTagp[7];       /* the gear predictor variable coefficient matrix */
// #endif /*PREDICTOR*/	// Original code
	double CKTlteCoeff;		// The LTE estimation coefficient of the integration algorithm
	double CKTltePredCoeff;	// The LTE estimation coefficient of the predictor
    int CKTorder;           /* the integration method order */
    int CKTmaxOrder;        /* maximum integration method order */
    int CKTintegrateMethod; /* the integration method to be used */

/* known integration methods */
#define TRAPEZOIDAL 1
#define GEAR 2

    SMPmatrix *CKTmatrix;   /* pointer to sparse matrix */
    int CKTniState;         /* internal state */
    double *CKTrhs;         /* current rhs value - being loaded */
    double *CKTrhsOld;      /* previous rhs value for convergence testing */
    double *CKTrhsSpare;    /* spare rhs value for reordering */
    double *CKTirhs;        /* current rhs value - being loaded (imag) */
    double *CKTirhsOld;     /* previous rhs value (imaginary)*/
    double *CKTirhsSpare;   /* spare rhs value (imaginary)*/
	int *CKTrhsIcGiven;	// Information about ic ordered by indices in RHS.
	double **CKTssseEps;	// Results needed in steady state analysis.
// #ifdef PREDICTOR	// Original code.
    double *CKTpred;        /* predicted solution vector */
    double *CKTsols[8];     /* previous 8 solutions */
// #endif /* PREDICTOR */	// Original code.

    double *CKTrhsOp;      /* opearating point values */
    double *CKTsenRhs;      /* current sensitivity rhs  values */
    double *CKTseniRhs;      /* current sensitivity rhs  values (imag)*/


/*
 *  symbolic constants for CKTniState
 *      Note that they are bitwise disjoint
 */

#define NISHOULDREORDER 0x1
#define NIREORDERED 0x2
#define NIUNINITIALIZED 0x4
#define NIACSHOULDREORDER 0x10
#define NIACREORDERED 0x20
#define NIACUNINITIALIZED 0x40
#define NIDIDPREORDER 0x100
#define NIPZSHOULDREORDER 0x200

    int CKTmaxEqNum;
    int CKTcurrentAnalysis; /* the analysis in progress (if any) */

/* defines for the value of  CKTcurrentAnalysis */
/* are in TSKdefs.h */
// Defines for the value of CKTcurrentAnalysis are now here.
#define DOING_DCOP 1
#define DOING_TRCV 2
#define DOING_AC   4
#define DOING_TRAN 8
    CKTnode *CKTnodes;
    CKTnode *CKTlastNode;
    CKTnode *CKTinternals;	// List of unsetuped internal nodes.
    // List of node groups connected together in dc domain.
	struct CKTnodeGroup *CKTnodeGroups;
	struct cshunt *CKTcminList;	// List of cmins added into the circuit.
	struct cshunt *CKTcshuntList;	// List of cshunts added into the circuit.
#define NODENAME(ckt,nodenum) CKTnodName(ckt,nodenum)
    int CKTnumStates;
    long CKTmode;

/* defines for CKTmode */

/* old 'mode' parameters */
#define MODE 0x3
#define MODETRAN 0x1
#define MODEAC 0x2

/* old 'modedc' parameters */
#define MODEDC 0x70
#define MODEDCOP 0x10
#define MODETRANOP 0x20
#define MODEDCTRANCURVE 0x40

/* old 'initf' parameters */
#define INITF 0x3f00
#define MODEINITFLOAT 0x100
#define MODEINITJCT 0x200
#define MODEINITFIX 0x400
#define MODEINITSMSIG 0x800
#define MODEINITTRAN 0x1000
#define MODEINITPRED 0x2000

/* old 'nosolv' paramater */
#define MODEUIC 0x10000l

    int CKTbypass;
    int CKTdcMaxIter;       /* iteration limit for dc op.  (itl1) */
    int CKTdcTrcvMaxIter;   /* iteration limit for dc tran. curv (itl2) */
	int CKTtranMinIter;	// For itl3 option.
    int CKTtranMaxIter;     /* iteration limit for each timepoint for tran*/
                            /* (itl4) */
	double CKTmaxFreq;	// Highest frequency of sin and sffm independent sources.
	double CKTxmu;	// Trapeziodal integration algorithm coefficient.
	double CKTxmuMult;	// Multiplicator of xmu in case of numerical oscillations.
	double CKTtrapRatio;	// Ratio for detecting numerical oscillations.
	unsigned int CKTintegDebug : 1;	// Print numerical oscillations messages flag.
    int CKTbreakSize;
    int CKTbreak;
	// double CKTsaveDelta;	// Not used.
    double CKTminBreak;
    double *CKTbreaks;
    double CKTabstol;
    double CKTpivotAbsTol;
    double CKTpivotRelTol;
    double CKTreltol;
    double CKTchgtol;
    double CKTvoltTol;
	double CKTslopeTol;	// For slopetol option.
	double CKTabsVar;	// For absvar option.
	double CKTrelVar;	// For relvar option.
    double CKTssseTol;	// Tolerance multiplier for steady state analysis.
	// Maximal voltage in per-iteration voltage limit functions.
	double CKTvoltageLimit;
	double CKTrelQ;	// For relq option.
// #ifdef NEWTRUNC	// Original code.
    double CKTlteReltol;
    double CKTlteAbstol;
// #endif /* NEWTRUNC */	// Original code.
	int CKTnewTrunc;	// For newtrunc option.
	int CKTnoPredictor;	// For nopredictor option.
	int CKTdcap;	// For dcap option.
    double CKTgmin;
	double CKTgmindc;	// For gmindc option.
	double CKTresmin;	// For resmin option.
	double CKTcmin;	// For cmin option.
	double CKTcshunt;	// For cshunt option.
    double CKTdelmin;
    double CKTtrtol;
    double CKTfinalTime;
    double CKTstep;
    double CKTmaxStep;
    double CKTinitTime;
	IFnode CKTposNode;	// For steady state analysis by shooting with extrapolation.
	IFnode CKTnegNode;
	double CKTlevel;
	double CKTskip;
	int CKTperiods;
	int CKThistory;
	unsigned int CKTcallFromSSSE : 1;
    double CKTomega;
    double CKTsrcFact;
    double CKTdiagGmin;
    double CKTcminCap;	// Current cmin value.
    int CKTnumSrcSteps;
    int CKTsrcsPriority;	// For srcspriority option.
    int CKTnumGminSteps;
    int CKTgminPriority;	// For gminpriority option.
	int CKTnumCminSteps;	// For cminsteps option.
    int CKTnoncon;
    double CKTdefaultMosL;
    double CKTdefaultMosW;
    double CKTdefaultMosAD;
    double CKTdefaultMosAS;
	double CKTdefaultMosPD;	// For defpd option.
	double CKTdefaultMosPS;	// For defps option.
	double CKTdefaultMosNRD;	// For defnrd option.
	double CKTdefaultMosNRS;	// For defnrs option.
	int CKTdefaultModCheck;	// For defmodcheck option.
	int CKTdefaultInstCheck;	// For definstcheck option.
	double CKTicStep;	// For icstep option.
	int CKTlvlTim;	// For lvltim option.
	double CKTrMax;	// For rmax option.
	double CKTrMin;	// For rmin option.
	double CKTfs;	// For fs option.
	double CKTft;	// For ft option.
	double CKTscale;	// For scale option.
	int CKTpzIter;	// For pziter option.
	double CKTnsFactor;	// For nsfactor option.
	double CKTnsFactorPart;	// Additional variable used with nsfactor option.
	int CKTnsSteps;	// For nssteps option.
    unsigned int CKThadNodeset:1;
	// To explicitly avoid using initial conditions and nodesets.
	unsigned int CKTdoNotUseIcAndNodesets : 1;
	unsigned int CKTsolutionLimit : 1;	// To turn on solution limiting.
	int CKTnoConvIter;	// For noconviter option.
	double CKTsolLim;	// For sollim option.
	int CKTsolLimIter;	// For sollimiter option.
	int CKTnumSolOsc;	// Direction change counter during solution limiting.
    unsigned int CKTfixLimit:1; /* flag to indicate that the limiting of 
                                 * MOSFETs should be done as in SPICE2 */
    unsigned int CKTnoOpIter:1; /* flag to indicate not to try the operating
                                 * point brute force, but to use gmin stepping
                                 * first */
	//////////
	// Flag CKTnoSrcLift indicate to skip source lifting in transient domain in
	// operating point analysis.
	//////////
	unsigned int CKTnoSrcLift : 1;
	// Flag CKTnoInitSrcl indicate to skip initial source lifting without cmins.
	unsigned int CKTnoInitSrcl : 1;
	//////////
	// Flag to print debug messages in convergence aids for calculating operating
	// point.
	//////////
	unsigned int CKTopDebug : 1;
	//////////
	// Flag to print result of first component outside tolerances in each iteration
	// when solution limiting is on.
	//////////
	unsigned int CKTsolLimDebug : 1;
	unsigned int CKTmatrixCheck : 1;	// Flag to check matrix after load.
	// Flag to indicate not to check circuit topology during setup.
	unsigned int CKTnoFloatNodesCheck : 1;
	// Flag to indicate not to set options automatically to achieve convergence.
	unsigned int CKTnoAutoConv : 1;
    unsigned int CKTisSetup:1;  /* flag to indicate if CKTsetup done */ // Not in xspice
    JOB *CKTcurJob;

    SENstruct *CKTsenInfo;	/* the sensitivity information */
    double *CKTtimePoints;	/* list of all accepted timepoints in the
				   current transient simulation */
    double *CKTdeltaList;	/* list of all timesteps in the current
				   transient simulation */
    int CKTtimeListSize;	/* size of above lists */
    int CKTtimeIndex;		/* current position in above lists */
    int CKTsizeIncr;		/* amount to increment size of above arrays
				   when you run out of space */
    unsigned int CKTtryToCompact:1; /* try to compact past history for LTRA
				   lines */
    unsigned int CKTbadMos3:1; /* Use old, unfixed MOS3 equations */
    unsigned int CKTkeepOpInfo:1; /* flag for small signal analyses */
    int CKTtroubleNode;		/* Non-convergent node number */
    GENinstance *CKTtroubleElt;	/* Non-convergent device instance */

/* gtri - evt - wbk - 5/20/91 - add event-driven and enhancements data */

    Evt_Ckt_Data_t *evt;  /* all data about event driven stuff */
    Enh_Ckt_Data_t *enh;  /* data used by general enhancements */

/* gtri - evt - wbk - 5/20/91 - add event-driven and enhancements data */


} CKTcircuit;

#ifdef __STDC__
int ACan( CKTcircuit *, int );
int ACaskQuest( CKTcircuit *, GENERIC *, int , IFvalue *);
int ACsetParm( CKTcircuit *, GENERIC *, int , IFvalue *);
int CKTacDump( CKTcircuit *, double , GENERIC *);
int CKTacLoad( CKTcircuit *);
int CKTaccept( CKTcircuit *);
int CKTacct( CKTcircuit *, GENERIC *, int , IFvalue *);
int CKTask( GENERIC *, GENERIC *, int , IFvalue *, IFvalue *);
int CKTaskAnalQ(GENERIC *,GENERIC *, int, IFvalue *, IFvalue *);
int CKTaskNodQst(GENERIC *, int, IFvalue *);
int CKTbindNode(GENERIC *, int, GENERIC *);
void CKTbreakDump( CKTcircuit *);
int CKTclrBreak( CKTcircuit *);
int CKTconvTest( CKTcircuit *);
int CKTcrtElt( GENERIC *, GENERIC *, GENERIC **, IFuid );
int CKTgetEltType(GENERIC *, int *);
int CKTdelTask(GENERIC *, GENERIC *);
int CKTdestroy( GENERIC *);
int CKTdltAnal( GENERIC *, GENERIC *, GENERIC *);
int CKTdltInst( GENERIC *, GENERIC *);
int CKTdltMod( GENERIC *, GENERIC *);
int CKTdltNod( GENERIC *, GENERIC *);
int CKTdoJob( GENERIC *, int , GENERIC *);
void CKTdump( CKTcircuit *, double, GENERIC *);
int CKTfndAnal( GENERIC *, int *, GENERIC **, IFuid , GENERIC *, IFuid );
int CKTfndBranch( CKTcircuit *, IFuid);
int CKTfndDev( GENERIC *, int *, GENERIC **, IFuid , GENERIC *, IFuid );
int CKTfndMod( GENERIC *, int *, GENERIC **, IFuid );
int CKTfndNode( GENERIC *, GENERIC **, IFuid );
int CKTfndTask( GENERIC *, GENERIC **, IFuid  );
int CKTground( GENERIC *, GENERIC **, IFuid );
int CKTic( CKTcircuit *);
int CKTinit( GENERIC **);
int CKTinst2Node( GENERIC *, GENERIC *, int , GENERIC **, IFuid *);
int CKTlinkEq(CKTcircuit*,CKTnode*);
int CKTload( CKTcircuit *);
int CKTmapNode( GENERIC *, GENERIC **, IFuid );
int CKTmkCur( CKTcircuit  *, CKTnode **, IFuid , char *);
int CKTmkNode(CKTcircuit*,CKTnode**);
int CKTmkVolt( CKTcircuit  *, CKTnode **, IFuid , char *);
int CKTmodAsk( GENERIC *, GENERIC *, int , IFvalue *, IFvalue *);
int CKTmodCrt( GENERIC *, int , GENERIC **, IFuid );
int CKTgetModType(GENERIC *, int *);
int CKTmodParam( GENERIC *, GENERIC *, int , IFvalue *, IFvalue *);
int CKTnames(CKTcircuit *, int *, IFuid **);
int CKTnewAnal( GENERIC *, int , IFuid , GENERIC **, GENERIC *);
int CKTnewEq( GENERIC *, GENERIC **, IFuid );
int CKTnewNode( GENERIC *, GENERIC **, IFuid );
int CKTnewTask( GENERIC *, GENERIC **, IFuid );
IFuid CKTnodName( CKTcircuit *, int );
void CKTnodOut( CKTcircuit *);
CKTnode * CKTnum2nod( CKTcircuit *, int );
int CKTop(CKTcircuit *, long, long, int );
int CKTpModName( char *, IFvalue *, CKTcircuit *, int , IFuid , GENmodel **);
int CKTpName( char *, IFvalue *, CKTcircuit *, int , char *, GENinstance **);
int CKTparam( GENERIC *, GENERIC *, int , IFvalue *, IFvalue *);
int CKTpzFindZeros( CKTcircuit *, PZtrial **, int * ); // Not in xspice
int CKTpzLoad( CKTcircuit *, SPcomplex *);
// int CKTpzLoad( CKTcircuit *, SPcomplex *, int); // Could be obsolete (from xspice)
int CKTpzSetup( CKTcircuit *, int); // int not in xspice
int CKTsenAC( CKTcircuit *);
int CKTsenComp( CKTcircuit *);
int CKTsenDCtran( CKTcircuit *);
int CKTsenLoad( CKTcircuit *);
void CKTsenPrint( CKTcircuit *);
int CKTsenSetup( CKTcircuit *);
int CKTsenUpdate( CKTcircuit *);
int CKTsetAnalPm( GENERIC *, GENERIC *, int , IFvalue *, IFvalue *);
int CKTsetBreak( CKTcircuit *, double );
int CKTsetNodPm( GENERIC *, GENERIC *, int , IFvalue *, IFvalue *);
int CKTsetOpt( GENERIC *, GENERIC *, int , IFvalue *);
int CKTsetup( CKTcircuit *);
struct CKTnodeGroup *CKTaddGroup(CKTcircuit *);	// For adding node group.
void CKTaddNodeToGroup(struct CKTnodeGroup *, int);	// For adding node to group.
int CKTunsetup( CKTcircuit *);
int CKTtemp( CKTcircuit *);
char *CKTtrouble(GENERIC *, char *);
void CKTterr( int , CKTcircuit *, double *);
int CKTtrunc( CKTcircuit *, double *);
// Added for dvdt timestep algorithm.
double CKTdvdt(CKTcircuit *, double *, double, double, double *, double *);
int CKTtypelook( char *);
int CKTarea(GENERIC*, double*);	// Added for area calculation.
int DCOaskQuest( CKTcircuit *, GENERIC *, int , IFvalue *);
int DCOsetParm( CKTcircuit  *, GENERIC *, int , IFvalue *);
int DCTaskQuest( CKTcircuit *, GENERIC *, int , IFvalue *);
int DCTsetParm( CKTcircuit  *, GENERIC *, int , IFvalue *);
int DCop( CKTcircuit *);
int DCtrCurv( CKTcircuit *, int );
int DCtran( CKTcircuit *, int );
int DCssse(CKTcircuit *, int);	// For steady state analysis.
int DISTOan(CKTcircuit *, int);
int NOISEan(CKTcircuit *, int);
int PZan( CKTcircuit *, int );
int PZinit( CKTcircuit * );
int PZpost( CKTcircuit * );
int PZaskQuest( CKTcircuit *, GENERIC *, int , IFvalue *);
int PZsetParm( CKTcircuit *, GENERIC *, int , IFvalue *);
int SENaskQuest( CKTcircuit *, GENERIC *, int , IFvalue *);
void SENdestroy( SENstruct *);
int SENsetParm( CKTcircuit *, GENERIC *, int , IFvalue *);
int SENstartup( CKTcircuit *);
int SPIinit( IFfrontEnd *, IFsimulator **);
char * SPerror( int );
int TFanal( CKTcircuit *, int );
int TFaskQuest( CKTcircuit *, GENERIC *, int , IFvalue *);
int TFsetParm( CKTcircuit *, GENERIC *, int , IFvalue *);
int TRANaskQuest( CKTcircuit *, GENERIC *, int , IFvalue *);
int TRANsetParm( CKTcircuit *, GENERIC *, int , IFvalue *);
int TRANinit(CKTcircuit *, JOB *);
int SSSEinit(CKTcircuit *, JOB *);	// For steady state analysis.
int NIpred(CKTcircuit *);
int NIacIter( CKTcircuit * );
int NIcomCof( CKTcircuit * ); 
int NIconvTest(CKTcircuit * );
void NIdestroy(CKTcircuit * );
int NIinit( CKTcircuit  * );
int NIintegrate( CKTcircuit *, double *, double *, double , int );
int NIiter( CKTcircuit * , int );
int NIpzMuller(PZtrial **, PZtrial *);
int NIpzComplex(PZtrial **, PZtrial *);
int NIpzSym(PZtrial **, PZtrial *);
int NIpzSym2(PZtrial **, PZtrial *);
// int NIpzMuller( CKTcircuit *, root **, int ); // From xspice (probably obsolete)
// int NIpzSolve( CKTcircuit *, SPcomplex *, root *, SPcomplex *, int , int *); // Added from xspice
int NIreinit( CKTcircuit *);
int NIsenReinit( CKTcircuit *);
#else /* stdc */
int ACan();
int ACaskQuest();
int ACsetParm();
int CKTacDump();
int CKTacLoad();
int CKTaccept();
int CKTacct();
int CKTask();
int CKTaskAnalQ();
int CKTaskNodQst();
int CKTbindNode();
void CKTbreakDump();
int CKTclrBreak();
int CKTcrtElt();
int CKTgetEltType();
int CKTdelTask();
int CKTdestroy();
int CKTdltAnal();
int CKTdltInst();
int CKTdltMod();
int CKTdltNod();
int CKTdoJob();
void CKTdump();
int CKTfndAnal();
int CKTfndBranch();
int CKTfndDev();
int CKTfndMod();
int CKTfndNode();
int CKTfndTask();
int CKTground();
int CKTic();
int CKTinit();
int CKTinst2Node();
int CKTlinkEq();
int CKTload();
int CKTmapNode();
int CKTmkCur();
int CKTmkNode();
int CKTmkVolt();
int CKTmodAsk();
int CKTmodCrt();
int CKTgetModType();
int CKTmodParam();
int CKTnames();
int CKTnewAnal();
int CKTnewEq();
int CKTnewNode();
int CKTnewTask();
IFuid CKTnodName();
void CKTnodOut();
CKTnode * CKTnum2nod();
int CKTop();
int CKTpModName();
int CKTpName();
int CKTparam();
int CKTpzLoad();
int CKTpzSetup();
int CKTsenAC();
int CKTsenComp();
int CKTsenDCtran();
int CKTsenLoad();
void CKTsenPrint();
int CKTsenSetup();
int CKTsenUpdate();
int CKTsetAnalPm();
int CKTsetBreak();
int CKTsetNodPm();
int CKTsetOpt();
int CKTsetup();
struct CKTnodeGroup *CKTaddGroup();	// For adding node group.
void CKTaddNodeToGroup();	// For adding node to group.
int CKTunsetup();
int CKTpzSetup();
int CKTtemp();
char *CKTtrouble( );
void CKTterr();
int CKTtrunc();
double CKTdvdt();	// Added for dvdt timestep algorithm.
int CKTtypelook();
int CKTarea();	// Added for area calculation.
int DCOaskQuest();
int DCOsetParm();
int DCTaskQuest();
int DCTsetParm();
int DCop();
int DCtrCurv();
int DCtran();
int DCssse();	// For steady state analysis.
int DISTOan();
int NOISEan();
int PZan();
int PZaskQuest();
int PZsetParm();
int SENaskQuest();
void SENdestroy();
int SENsetParm();
int SENstartup();
int SPIinit();
char * SPerror();
int TFanal();
int TFaskQuest();
int TFsetParm();
int TRANaskQuest();
int TRANsetParm();
int TRANinit( );
int SSSEinit();	// For steady state analysis.
int NIpred();
int NIacIter();
int NIcomCof(); 
int NIconvTest();
void NIdestroy();
int NIinit();
int NIintegrate();
int NIiter();
int NIpzMuller();
int NIpzSolve();
int NIreinit();
int NIsenReinit();
#endif /* stdc */

extern IFfrontEnd *SPfrontEnd;

#endif /*CKT*/
