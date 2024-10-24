//////////
// Modifications in the original code:
// 1.	Macro flag DGEN_ALL_OUTPUT_PARAMS added. It is used in all_show() and
//		param_forall() functions. The flag is added for all_output option in show
//		and showmod commands. The option causes printout of all device or model
//		parameters which are defined as output parameters.
// Author: Janez Puhan
//////////

typedef struct st_dgen dgen;

struct st_dgen {
	GENcircuit	*ckt;
	wordlist	*dev_list;
	int		flags;
	int		dev_type_no;
	int		dev;
	GENinstance	*instance;
	GENmodel	*model;
};


#define	DGEN_ALL	0x00e
#define	DGEN_TYPE	0x002
#define	DGEN_MODEL	0x004
#define	DGEN_INSTANCE	0x008
#define	DGEN_INIT	0x010

#define	DGEN_DEFDEVS	0x020
#define	DGEN_ALLDEVS	0x040

#define	DGEN_DEFPARAMS			0x001
#define	DGEN_ALLPARAMS			0x002
#define	DGEN_ALL_OUTPUT_PARAMS	0x004	// For option all_output.

extern	dgen	*dgen_init( );
