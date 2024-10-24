//////////
// Modifications in the original code:
// 1.	Static string groundname is changed to global variable, because it is used
//		in mif/mif_inp2a.c. Extern declaration of the string is therefore added.
// 2.	Added filehiertree structure pointer to line structure. It tells which file
//		this line belongs to.
// 3.	Further modificaions. Will have to comment them.
// Author: Arpad Buermen
//////////
// 4.	Structures INPsubcktParamSets, INPparamSet and INPparam added for list
//		containing different parameter sets.
// 5.	Function INPpas2() can change the option lines. Therefore it now takes
//		options as the fifth argument. The same goes for INP2dot() and INPdoOpts()
//		functions.
// 6.	Extern declaration for functions coef_to_num() converting scaling
//		coefficients and check_nodes_and_value() checking instance nodes and given
//		value added.
// Author: Janez Puhan
//////////

/**********
Copyright 1990 Regents of the University of California.  All rights reserved.
Author: 1985 Thomas L. Quarles
**********/

#ifndef INP
#define INP "inpdefs.h $Revision: 1.1 $  on $Date: 91/04/02 11:26:07 $ "

    /* structure declarations used by either/both input package */

#include "ifsim.h"
#include "gendefs.h"
#include "inpptree.h"
#include <stdio.h>

struct INPtab {
    char *t_ent;
    struct INPtab *t_next;
};

struct INPnTab {
    char *t_ent;
    GENERIC* t_node;
    struct INPnTab *t_next;
};

struct FileHierTree {
	struct FileHierTree **child;
	int inclusionline;
	int numchildren;
	struct FileHierTree *parent;
	char *filename;
	char *section;
};

typedef struct card {
    int linenum;
    char *line;
    struct card *nextcard;
	struct FileHierTree *file;
	char prot;
} card;

typedef struct sINPfpEntry {
	card *src;
	GENERIC *fast;
} INPfpEntry;

/* structure used to save models in after they are read during pass 1 */
typedef struct sINPmodel{
    IFuid INPmodName;   /* uid of model */
    int INPmodType;     /* type index of device type */
    struct sINPmodel *INPnextModel;  /* link to next model */
    int INPmodUsed;     /* flag to indicate it has already been used */
    card *INPmodLine;   /* pointer to line describing model */
    GENERIC *INPmodfast;   /* high speed pointer to model for access */
} INPmodel;

// Structure containing subcircuit info
typedef struct sINPsubckt {
	IFuid INPsubName;
	char **INPsubTerm;
	int INPsubTermCnt;
	card *cards;
	struct sINPsubcktInst *instances;
	struct sINPsubckt *next;
	int INPsubParCnt;
	char **INPsubParName;
	int *INPsubParDflType;
	IFvalue **INPsubParDfl;
	int INPsubExprCnt;
	char **INPsubExprName;
	char **INPsubExpr;
	card **INPsubExprCard;
} INPsubckt;

typedef struct sINPsubcktInst {
	IFuid INPinstName;
	struct sINPsubckt *model;
	char **INPsubConn;
	int INPsubConnCnt;
	char *INPsubPath;
	int *INPsubParType;
	IFvalue **INPsubPar;
	struct sINPsubcktInst *next;
	card *fromCard;
	// Arrays of cards that need to be reparsed on parameter modification
	INPfpEntry *INPfpModel;
	int INPfpMCnt;
	INPfpEntry *INPfpInst;
	int INPfpICnt;
	INPfpEntry *INPfpSubckt;
	int INPfpSCnt;
} INPsubcktInst;

// Structures for list of subcircuit parameter sets.
typedef struct sINPparam
{
	char *name;
	IFvalue *value;
	struct sINPparam *next;
} INPparam;

typedef struct sINPparamSet
{
	char *name;
	INPparam *values;
	struct sINPparamSet *next;
} INPparamSet;

typedef struct sINPsubcktParamSets
{
	char *name;
	INPparamSet *sets;
	struct sINPsubcktParamSets *next;
} INPsubcktParamSets;

typedef struct sINPnetclassDef {
	char *name;
	char **key;
	int numkeys;
	int active;	// Selected key.
	int parsed;	// Currently parsed key.
} INPnetclassDef;

typedef struct sINPtables{
    struct INPtab **INPsymtab;
    struct INPnTab **INPtermsymtab;
    int INPsize;
    int INPtermsize;
    GENERIC *defAmod;
    GENERIC *defBmod;
    GENERIC *defCmod;
    GENERIC *defDmod;
    GENERIC *defEmod;
    GENERIC *defFmod;
    GENERIC *defGmod;
    GENERIC *defHmod;
    GENERIC *defImod;
    GENERIC *defJmod;
    GENERIC *defKmod;
    GENERIC *defLmod;
    GENERIC *defMmod;
    GENERIC *defNmod;
    GENERIC *defOmod;
    GENERIC *defPmod;
    GENERIC *defQmod;
    GENERIC *defRmod;
    GENERIC *defSmod;
    GENERIC *defTmod;
    GENERIC *defUmod;
    GENERIC *defVmod;
    GENERIC *defWmod;
    GENERIC *defYmod;
    GENERIC *defZmod;
	// Added by OPUS
	INPsubckt *INPsubList;
	INPsubckt *INPsubTop;
	INPnetclassDef *INPnetclass;
	int INPnetclassCnt;
	int INPdidNetclasses;
	int INPcktFresh;
	INPmodel *modtab;
	char **INPglobal;
	int INPglobalCnt;
	struct FileHierTree *filetree;
	INPmodel *lastModel;
	GENERIC *lastInstance;
} INPtables;

extern char *errorcard;

extern int INPreparse;

/* listing types - used for debug listings */
#define LOGICAL 1
#define PHYSICAL 2

extern char *groundname;
extern GENERIC *groundnode;

struct parinfo {
	char *name;				// instance/model name
	char *par;				// parameter name
	int partype;			// 0=instance  1=model  2=simulator
	int vecdim;				// vector dimension
	int *vecindex;			// vector index table
	GENERIC *instmodptr;
};

struct parinfo *parinfoALLOC();
void parinfoFREE(struct parinfo *par);
struct parinfo *parparse(char *par);

#ifdef __STDC__
int INPmanualSubReparse();
void INPsetManualSubReparse(int);
int INPsubWriteParams(GENERIC *, INPtables *, char *);
int INPsubModelWriteParams(GENERIC *, INPtables *, char *);
int INPgetSubcktModel(INPtables *, GENERIC *, GENERIC **);
int INPfindSubcktInstance(INPtables *, GENERIC **, IFuid);
int INPfindSubcktModel(INPtables *, GENERIC **, IFuid);
IFparm *INPfindSubcktParameter(GENERIC *, char *);
IFparm *INPfindSubcktModelParameter(GENERIC *, char *);
int INPaskSubcktParameter(INPtables *, GENERIC *, int, IFvalue *);
int INPaskSubcktModelParameter(INPtables *, GENERIC *, int, IFvalue *);
int INPsetSubcktParameter(GENERIC *, INPtables *, GENERIC *, int, IFvalue *, int);
int INPsetSubcktModelParameter(GENERIC *, INPtables *, GENERIC *, int, IFvalue *, int);
int INPstartModelList(GENERIC *, INPtables *, char *);
char *INPnextModel();
int INPstartInstanceList(GENERIC *, INPtables *, char *);
char *INPnextInstance();
void IFvalueContentsDelete(union uIFvalue *, int);
void IFvalueDelete(union uIFvalue *, int);
struct card *INPdeckCopy(struct card *);
int INPsetNetclass(INPtables *, char *, int, char *, int, int);
void INPlistNetclass(INPtables *, char *, int);
int INPneedRebuild(INPtables *);
void INPlistGlobal(INPtables *);
void INPlistSub(INPtables *, char *);
void INPlistSubDef(INPtables *, char *);
void INPnodeTranslate(INPtables *, char **);
void INPinstTranslate(INPtables *, char **);
void INPmodTranslate(INPtables *, char **);
int INPmodGlobalize(INPtables *, char **);
void INPerrorReset();
int INPcheckIncludeRecursion(struct FileHierTree *, char *, char *);
void INPprintFileHier(FILE *, struct FileHierTree *, int);
void INPerrorPrint(struct card *);
int  INPgotError();
struct card *INPcardCopy(struct card *);
void INPcardDelete(struct card *);
void INPdeckDelete(struct card *);
void INPerrorPath(struct FileHierTree *, int);
void INPerrorLocation(card *);
struct FileHierTree *INPnewFile(struct FileHierTree *, char *, char *, int);
void INPdestroyFileHier(struct FileHierTree *);
int IFnewUid(GENERIC*,IFuid*,IFuid,char*,int,GENERIC**);
int IFdelUid(GENERIC*,IFuid,int);
int INPaName(char*,int*,IFvalue*,GENERIC*,int*,char*,GENERIC**,IFsimulator*,int*,
        IFvalue*);
int INPapName(GENERIC*,int,GENERIC*,char*,IFvalue*);
void INPcaseFix(char*);
char * INPdevParse(char**,GENERIC*,int,GENERIC*,double*,int*,INPtables*);
char *INPdomodel(GENERIC *,card*, INPtables*);
// void INPdoOpts(GENERIC*,GENERIC*,card*,INPtables*);	// Original code.
void INPdoOpts(GENERIC*, GENERIC*, card*, INPtables*, card**);	// Options added.
char *INPerrCat(char *, char *);
char *INPerror(int);
double INPevaluate(char**,int*,int);
char * INPfindLev(char*,int*);
char * INPgetMod(GENERIC*,char**,INPmodel**,INPtables*);
int INPgetTok(char**,char**,int);
void INPptdel(INPparseNode *);
void INPgetTree(char**,INPparseTree**,GENERIC*,INPtables*);
IFvalue * INPgetValue(GENERIC*,char**,int,INPtables*);
int INPgndInsert(GENERIC*,char**,INPtables*,GENERIC**);
int INPinsert(char**,INPtables*);
int INPremove(char*,INPtables*);
INPmodel *INPlookMod(char**,INPtables*);
int INPmakeMod(char*,int,card*,INPtables*);
char *INPmkTemp(char*);
int INPpas0(card*,INPtables*,card **);
int INPpas1(GENERIC*,card*,INPtables*);
// int INPpas2(GENERIC*,card*,INPtables*,GENERIC *);	// Original code.
int INPpas2(GENERIC*, card*, INPtables*, GENERIC*, card**);	// Options added.
int INPpas5(GENERIC*,card*,INPtables*,GENERIC *);
int INPpName(char*,IFvalue*,GENERIC*,int,GENERIC*);
int INPtermInsert(GENERIC*,char**,INPtables*,GENERIC**);
int INPmkTerm(GENERIC*,char**,INPtables*,GENERIC**);
int INPtypelook(char*);
void INP2B(GENERIC*,INPtables*,card*);
void INP2C(GENERIC*,INPtables*,card*);
void INP2D(GENERIC*,INPtables*,card*);
void INP2E(GENERIC*,INPtables*,card*);
void INP2F(GENERIC*,INPtables*,card*);
void INP2G(GENERIC*,INPtables*,card*);
void INP2H(GENERIC*,INPtables*,card*);
void INP2I(GENERIC*,INPtables*,card*);
void INP2J(GENERIC*,INPtables*,card*);
void INP2K(GENERIC*,INPtables*,card*);
void INP2L(GENERIC*,INPtables*,card*);
void INP2M(GENERIC*,INPtables*,card*);
void INP2O(GENERIC*,INPtables*,card*);
void INP2Q(GENERIC*,INPtables*,card*,GENERIC*);
void INP2R(GENERIC*,INPtables*,card*);
void INP2S(GENERIC*,INPtables*,card*);
void INP2T(GENERIC*,INPtables*,card*);
void INP2U(GENERIC*,INPtables*,card*);
void INP2V(GENERIC*,INPtables*,card*);
void INP2W(GENERIC*,INPtables*,card*);
void INP2Z(GENERIC*,INPtables*,card*);
// int INP2dot(GENERIC*,INPtables*,card*,GENERIC*,GENERIC*);	// Original code.
// Options added.
int INP2dot(GENERIC*, INPtables*, card*, GENERIC*, GENERIC*, card**);
INPtables *INPtabInit(int);
void INPkillMods(INPtables *tab);
void INPtabEnd(INPtables *);
void INPsubcktEnd(INPtables *);
void INPnetclassEnd(INPtables *);
void INPfilehierEnd(INPtables *);
void INPhashEnd(INPtables *);
void INPhashCleanup(INPtables *);
char *coef_to_num(char *line);	// Added.
void check_nodes_and_value(GENERIC*, GENERIC*, GENERIC*, GENERIC*, GENERIC*,
	GENERIC*, GENERIC*, int, char*);	// Added.
#else /* stdc */
int INPmanualSubReparse();
void INPsetManualSubReparse();
int INPsubWriteParams();
int INPsubModelWriteParams();
int INPgetSubcktModel();
int INPfindSubcktInstance();
int INPfindSubcktModel();
IFparm *INPfindSubcktParameter();
IFparm *INPfindSubcktModelParameter();
int INPaskSubcktParameter();
int INPaskSubcktModelParameter();
int INPsetSubcktParameter();
int INPsetSubcktModelParameter();
int INPstartModelList();
char *INPnextModel();
int INPstartInstanceList();
char *INPnextInstance();
void IFvalueContentsDelete();
void IFvalueDelete();
struct card *INPdeckCopy();
int INPsetNetclass();
void INPlistNetclass();
int INPneedRebuild();
void INPlistGlobal();
void INPlistSub();
void INPlistSubDef();
void INPnodeTranslate();
void INPinstTranslate();
void INPmodTranslate();
int INPmodGlobalize();
void INPprintFileHier();
int INPcheckIncludeRecursion();
void INPerrorReset();
void INPerrorPrint();
int INPgotError();
struct card *INPcardCopy();
void INPcardDelete();
void INPdeckDelete();
void INPerrorPath();
void INPerrorLocation();
struct FileHierTree *INPnewFile();
void INPdestroyFileHier();
int IFnewUid();
int IFdelUid();
int INPaName();
IFvalue * INPgetValue();
INPtables *INPtabInit();
char * INPdevParse();
char * INPdomodel();
char * INPerrCat();
char * INPfindLev();
char * INPgetMod();
char *INPerror();
char *INPmkTemp();
double INPevaluate();
int INPapName();
int INPgetTitle();
int INPgetTok();
int INPgndInsert();
INPmodel *INPlookMod();
int INPmakeMod();
int INPpName();
int INPreadAll();
int INPtermInsert();
int INPmkTerm();
int INPtypelook();
void INPcaseFix();
void INPdoOpts();
int INPinsert();
int INPremove();
void INPkillMods();
void INPlist();
int INPpas0();
int  INPpas1() ;
int  INPpas2() ;
int  INPpas5() ;
void INPtabEnd();
void INPhashCleanup();
void INPsubcktEnd();
void INPnetclassEnd();
void INPfilehierEnd();
void INPhashEnd();
void INPptPrint();
void INPptdel();
void INPgetTree();
void INP2B();
void INP2C();
void INP2D();
void INP2E();
void INP2F();
void INP2G();
void INP2H();
void INP2I();
void INP2J();
void INP2K();
void INP2L();
void INP2M();
void INP2O();
void INP2Q();
void INP2R();
void INP2S();
void INP2T();
void INP2U();
void INP2V();
void INP2W();
void INP2Z();
int INP2dot();
char *coef_to_num();	// Added.
void check_nodes_and_value();	// Added.
#endif /* stdc */

#endif /*INP*/
