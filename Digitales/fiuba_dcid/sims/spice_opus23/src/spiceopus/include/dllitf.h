/* 
   DLL load interface
   (c)2000 Arpad Buermen
*/

#ifndef __DLLITF_H
#define __DLLITF_H

#include "port.h"
#include "misc.h"
#include "mifproto.h"
#include "cmproto.h"


// This structure contains pointers to core SpiceOpus functions used in CMs and UDNs.
// A pointer to this structure is passed to the dll when the dll is loaded.

struct coreInfo_t {
	// MIF stuff
	void      ((*dllitf_MIF_INP2A)(GENERIC *, INPtables *, card *));
	char *    ((*dllitf_MIFgetMod)(GENERIC *, char **, INPmodel  **, INPtables *));
	IFvalue * ((*dllitf_MIFgetValue)(GENERIC *, char **, int, INPtables *, char **));
	int		  ((*dllitf_MIFsetup)(SMPmatrix *, GENmodel *, CKTcircuit *, int *));
	int		  ((*dllitf_MIFunsetup)(GENmodel *, CKTcircuit *));
	int       ((*dllitf_MIFload)(GENmodel *, CKTcircuit *));
	int       ((*dllitf_MIFmParam)(int, IFvalue *, GENmodel *));
	int       ((*dllitf_MIFask)(CKTcircuit *, GENinstance *, int, IFvalue *, IFvalue *));
	int       ((*dllitf_MIFmAsk)(CKTcircuit *, GENmodel *, int, IFvalue *));
	int       ((*dllitf_MIFtrunc)(GENmodel *, CKTcircuit *, double *));
	int       ((*dllitf_MIFconvTest)(GENmodel *, CKTcircuit *));
	int       ((*dllitf_MIFdelete)(GENmodel *, IFuid, GENinstance  **));
	int       ((*dllitf_MIFmDelete)(GENmodel **, IFuid, GENmodel *));
	void      ((*dllitf_MIFdestroy)(GENmodel **));
	char *    ((*dllitf_MIFgettok)(char **));
	char *    ((*dllitf_MIFget_token)(char **, Mif_Token_Type_t *));
	Mif_Cntl_Src_Type_t ((*dllitf_MIFget_cntl_src_type)(Mif_Port_Type_t, Mif_Port_Type_t));
	char *    ((*dllitf_MIFcopy)(char *));
	// CM stuff
	void      ((*dllitf_cm_climit_fcn)(double, double, double, double, double, double, 
		                               double, double, int, double *, double *, double *, 
								       double *));
	void      ((*dllitf_cm_smooth_corner)(double, double, double, double, double, double,
	                                      double *, double *));
	void      ((*dllitf_cm_smooth_discontinuity)(double, double, double, double, double, 
		                                         double *, double *));
	double    ((*dllitf_cm_smooth_pwl)(double, double *, double *, int, double, double *));
	double    ((*dllitf_cm_analog_ramp_factor)(void));
	void *    ((*dllitf_cm_analog_alloc)(int, int));
	void *    ((*dllitf_cm_analog_get_ptr)(int, int));
	int       ((*dllitf_cm_analog_integrate)(double, double *, double *));
	int       ((*dllitf_cm_analog_converge)(double *));
    int       ((*dllitf_cm_analog_set_temp_bkpt)(double));
    int       ((*dllitf_cm_analog_set_perm_bkpt)(double));
    void      ((*dllitf_cm_analog_not_converged)(void));
    void      ((*dllitf_cm_analog_auto_partial)(void));
	void *    ((*dllitf_cm_event_alloc)(int, int));
	void *    ((*dllitf_cm_event_get_ptr)(int, int));
	int       ((*dllitf_cm_event_queue)(double));
	char *    ((*dllitf_cm_message_get_errmsg)(void));
	int       ((*dllitf_cm_message_send)(char *));
	double    ((*dllitf_cm_netlist_get_c)(void));
	double    ((*dllitf_cm_netlist_get_l)(void));
	Complex_t ((*dllitf_cm_complex_set)(double, double));
	Complex_t ((*dllitf_cm_complex_add)(Complex_t, Complex_t));
	Complex_t ((*dllitf_cm_complex_subtract)(Complex_t, Complex_t));
	Complex_t ((*dllitf_cm_complex_multiply)(Complex_t, Complex_t));
	Complex_t ((*dllitf_cm_complex_divide)(Complex_t, Complex_t));
	int       ((*dllitf_cm_outprintf)(const char *, ...));
	void *    dummy;
	int       ((*dllitf_cm_errprintf)(const char *, ...));
	char *    ((*dllitf_tmalloc)(size_t,int,const char *,int,int));
	char *    ((*dllitf_trealloc)(char *,size_t,const char *,int,int));
	void      ((*dllitf_tfree)(char *,const char *,int,int));
};

#endif
