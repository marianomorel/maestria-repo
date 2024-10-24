//////////
// Modifications in the original code:
// 1.	Extern declarations of functions com_optimize(), com_nodeset(), com_ic(),
//		com_copyplot() and com_scktparams() added (for optimize, nodeset, ic,
//		copyplot and scktparams commands respectively).
// 2.	Extern declarations of functions cx_integrate() and ft_integrate() added.
//		They are needed for performing integrate() function. Also extern declaration
//		of function cx_area() needed for performing area() function is added.
// 3.	Extern declaration for if_ssseparams() and com_ssse() functions added for
//		steady state analysis by shooting with extrapolation.ž
// Author: Janez Puhan
//////////
// 4.	Extern declaration of function com_spec() added (for spec command).
// Author: Anthony Parker
//////////
// 5.	Extern declarations of functions com_siminfo(), com_cmload() and com_gui()
//		added (for siminfo, cmload and gui commands respectively).
// 6.	Added horizontal vector join operation (op_hjv).
// 7.	Added nameplot command.
// 8.	Added cx_sum(), cx_min(), cx_max(), floor(), ceil() and round() functions.
// 9.	inp_spsource() returns now int (0 on success, 1 otherwise).
// 10.	inp_readall() returns now int. If read fails, a nonzero value is returned.
// 11.	Added cursor control command.
// 12.	Added destroyto command.
// 13.	Added evt command.
// 14.	Added epl() function.
// Author: Arpad Buermen
//////////

/**********
Copyright 1990 Regents of the University of California.  All rights reserved.
Author: 1986 Wayne A. Christopher, U. C. Berkeley CAD Group
**********/

/*
 * Definitions for all external symbols in FTE.
 */

#ifndef FTEext_h
#define FTEext_h

/* needed to find out what the interface structures look like */
#include "ifsim.h"
#include "fteparse.h"
#include "cpdefs.h"
#include "ftedefs.h"
#include "fteinp.h"

/* agraf.c */

extern void ft_agraf();

/* arg.c */

extern int arg_plot();
extern int arg_display();
extern int arg_print();
extern int arg_let();
extern int arg_load();
extern int arg_set();
extern void outmenuprompt();

/* aspice.c */

extern void com_aspice();
extern void com_jobs();
extern void com_rspice();
extern void ft_checkkids();

/* binary.c */

extern void braw_write();
extern struct plot *braw_read();

/* breakpoint.c */

extern BOOL ft_bpcheck();
extern void com_delete();
extern void com_iplot();
extern void com_save();
extern void com_step();
extern void com_stop();
extern void com_sttus();
extern void com_trce();
extern void ft_trquery();
extern void dbfree( );

/* circuits.c */

extern struct circ *ft_curckt;
extern struct circ *ft_circuits;
extern struct subcirc *ft_subcircuits;
extern void ft_setccirc();
extern void ft_newcirc();
extern void ft_newsubcirc();

/* clip.c */

extern BOOL clip_line();
extern BOOL clip_to_circle();

/* cmath1.c */

extern double unwraptol;
extern BOOL cx_degrees;
extern char *cx_mag(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_ph(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_unwrap(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_j(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_real(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_imag(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_pos(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_db(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_log(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_ln(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_exp(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_sqrt(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_sin(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_cos(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_timer(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_clock(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_area(char *data, short int type, int length, int *new_length, short int *new_type);	// For area() function.


/* cmath2.c */

extern char *cx_tan(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_atan(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_norm(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_uminus(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_rnd(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_rndunif(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_rndgauss(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_mean(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_sum(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_min(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_max(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_floor(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_ceil(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_round(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_length(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_vector(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_unitvec(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_plus(char *data1, char *data2, short datatype1, short datatype2, int length);
extern char *cx_minus(char *data1, char *data2, short datatype1, short datatype2, int length);
extern char *cx_times(char *data1, char *data2, short datatype1, short datatype2, int length);
extern char *cx_mod(char *data1, char *data2, short datatype1, short datatype2, int length);
extern char *cx_epl(char *data, short type, int length, int *newlength, short *newtype);	// For evt() function.

/* cmath3.c */

extern char *cx_divide(char *data1, char *data2, short datatype1, short datatype2, int length);
extern char *cx_comma(char *data1, char *data2, short datatype1, short datatype2, int length);
extern char *cx_power(char *data1, char *data2, short datatype1, short datatype2, int length);
extern char *cx_eq(char *data1, char *data2, short datatype1, short datatype2, int length);
extern char *cx_gt(char *data1, char *data2, short datatype1, short datatype2, int length);
extern char *cx_lt(char *data1, char *data2, short datatype1, short datatype2, int length);
extern char *cx_ge(char *data1, char *data2, short datatype1, short datatype2, int length);
extern char *cx_le(char *data1, char *data2, short datatype1, short datatype2, int length);
extern char *cx_ne(char *data1, char *data2, short datatype1, short datatype2, int length);

/* cmath4.c */

extern char *cx_and(char *data1, char *data2, short datatype1, short datatype2, int length);
extern char *cx_or(char *data1, char *data2, short datatype1, short datatype2, int length);
extern char *cx_not(char *data, short type, int length, int *newlength, short *newtype);
extern char *cx_interpolate(char *data, short type, int length, int *newlength, short *newtype, struct plot *pl, struct plot *newpl, int grouping);
extern char *cx_deriv(char *data, short type, int length, int *newlength, short *newtype, struct plot *pl, struct plot *newpl, int grouping);
extern char *cx_integrate(char *data, short type, int length, int *new_length, short *new_type, struct plot *pl, struct plot *new_pl, int grouping);	// For integrate() function.

/* cmdtab.c */

extern struct comm *cp_coms;

/* compose.c */

extern void com_compose();

/* cpinterface.c symbols declared in CPextern.h */

/* debugcoms.c */

extern void com_dump();
extern void com_state();

/* define.c */

extern struct pnode *ft_substdef();
extern void com_define();
extern void com_undefine();
extern void ft_pnode();

/* device.c */

extern void com_show();
extern void com_showmod();
extern void com_alter();

/* diff.c */

extern void com_diff();

/* doplot.c */

extern void com_asciiplot();
extern void com_hardcopy();
extern void com_plot();
extern void com_xgraph();

/* dotcards.c */

extern BOOL ft_acctprint;
extern BOOL ft_listprint;
extern BOOL ft_nopage;
extern BOOL ft_nomod;
extern BOOL ft_nodesprint;
extern BOOL ft_optsprint;
extern int ft_cktcoms();
extern void ft_dotsaves();
extern int ft_savedotargs();

/* error.c */

extern void fatal();
extern void fperror();
extern void ft_sperror();
extern char ErrorMessage[];

/* evaluate.c */

extern struct dvec *op_and(struct pnode *arg1, struct pnode *arg2);
extern struct dvec *op_comma(struct pnode *arg1, struct pnode *arg2);
extern struct dvec *op_divide(struct pnode *arg1, struct pnode *arg2);
extern struct dvec *op_eq(struct pnode *arg1, struct pnode *arg2);
extern struct dvec *ft_evaluate();
extern struct dvec *op_ge(struct pnode *arg1, struct pnode *arg2);
extern struct dvec *op_gt(struct pnode *arg1, struct pnode *arg2);
extern struct dvec *op_le(struct pnode *arg1, struct pnode *arg2);
extern struct dvec *op_lt(struct pnode *arg1, struct pnode *arg2);
extern struct dvec *op_minus(struct pnode *arg1, struct pnode *arg2);
extern struct dvec *op_mod(struct pnode *arg1, struct pnode *arg2);
extern struct dvec *op_ne(struct pnode *arg1, struct pnode *arg2);
extern struct dvec *op_not(struct pnode *arg1, struct pnode *arg2);
extern struct dvec *op_or(struct pnode *arg1, struct pnode *arg2);
extern struct dvec *op_ind(struct pnode *arg1, struct pnode *arg2);
extern struct dvec *op_plus(struct pnode *arg1, struct pnode *arg2);
extern struct dvec *op_power(struct pnode *arg1, struct pnode *arg2);
extern struct dvec *op_times(struct pnode *arg1, struct pnode *arg2);
extern struct dvec *op_uminus(struct pnode *arg1, struct pnode *arg2);
extern struct dvec *op_range(struct pnode *arg1, struct pnode *arg2);
extern struct dvec *op_hjv(struct pnode *arg1, struct pnode *arg2);
extern struct dvec *op_cursorrd(struct pnode *arg1, struct pnode *arg2);

/* fourier.c */

extern void com_fourier();

/* spec.c */

extern void com_spec();	// Function for spec command.

/* ginterface.c */

extern BOOL gi_init();
extern BOOL gi_endpause;
extern BOOL gi_rottext;
extern int gi_fntheight;
extern int gi_fntwidth;
extern int gi_maxx;
extern int gi_maxy;
extern int gi_nolst;
extern int gi_nocolors;
extern int gi_package;
extern void gi_arc();
extern void gi_clearscreen();
extern void gi_close();
extern void gi_drawline();
extern void gi_redraw();
extern void gi_setcolor();
extern void gi_resetcolor();
extern void gi_setlinestyle();
extern void gi_text();
extern void gi_update();

/* graf.c */

extern BOOL gr_gmode;
extern BOOL gr_hmode;
extern BOOL gr_init();
extern void gr_clean();
extern void gr_end();
extern void gr_iplot();
extern void gr_iplot_end();
extern void gr_pmsg();
extern void gr_point();
extern void gr_start();
extern double gr_xrange[2];
extern double gr_yrange[2];
extern int gr_xmargin;
extern int gr_ymargin;
extern int gr_xcenter;
extern int gr_ycenter;
extern int gr_radius;
extern BOOL gr_circular;

/* grid.c */

extern void gr_fixgrid();

/* inp.c */

extern void com_edit();
extern void com_listing();
extern void com_source();
extern int  inp_dodeck();
extern void inp_source();
extern int  inp_spsource();
extern void inp_casefix();
extern void inp_list();
extern int  inp_readall();
extern FILE *inp_pathopen();

/* nutinp.c */

extern void inp_nutsource();
extern void nutinp_dodeck();
extern void nutcom_source();

/* interpolate.c */

extern BOOL ft_interpolate();
extern BOOL ft_polyfit();
extern double ft_peval();
extern void ft_polyderiv( );
extern void com_linearize();
extern BOOL ft_integrate(double *data, double *new_data, double *scale, int len, double *new_scale, int new_len, int degree);	// For integrate() function.

/* mfbinterface.c */

extern void mi_arc();
extern BOOL mi_init();
extern void mi_clearscreen();
extern void mi_close();
extern void mi_drawline();
extern void mi_resetcolor();
extern void mi_setcolor();
extern void mi_setlinestyle();
extern void mi_text();
extern void mi_update();

/* misccoms.c */

extern void com_bug();
extern void com_ahelp();
extern void com_ghelp();
extern void com_help();
extern void com_quit();
extern void com_version();
extern int hcomp(const void *element1, const void *element2);
extern void com_where();

/* numparse.c */

extern BOOL ft_strictnumparse;
extern double *ft_numparse();

// optimize.c
extern void com_optimize();	// Function for optimize command.

// nodeset.c
extern void com_nodeset(wordlist *command);	// Function for nodeset command.

// ic.c
extern void com_ic();	// Function for ic command.

// siminfo.c
extern void com_siminfo();	// Function for siminfo command.

// cmdynld.c
extern void com_cmload();	// Function for cmload command.

// circuits.c
extern struct circ *ft_findcirc();
extern void com_delcirc();
extern void ft_setccirc();
extern void ft_delcirc();
extern void ft_delparsedcirc();
extern void ft_newcirc();

// netclass.c
extern void com_netclass();
extern void com_scktreparse();
extern void com_scktparams();	// Function implementing scktparams command.
extern void com_netlist();

// evt.c
extern void com_evt();

// copyplot.c
extern void com_copyplot();	// Function implementing copyplot command.
/* options.c */

extern BOOL ft_simdb;
extern BOOL ft_parsedb;
extern BOOL ft_evdb;
extern BOOL ft_vecdb;
extern BOOL ft_grdb;
extern BOOL ft_gidb;
extern BOOL ft_controldb;
extern BOOL ft_asyncdb;
extern char *ft_setkwords[];
extern struct card *inp_getopts();
extern struct variable *cp_enqvar();
extern struct variable *cp_uservars();
extern int cp_userset();

/* parse.c */

extern struct func ft_funcs[];
extern struct func func_not;
extern struct func func_uminus;
extern struct pnode *ft_getpnames(wordlist *wl, BOOL check, BOOL output);
extern struct pnode *copy_pnode(struct pnode *t);
extern void free_pnode();

/* plotcurve.c */

extern int ft_findpoint();
extern double *ft_minmax();
extern void ft_graf();

/* plotinterface.c */

extern void pi_arc();
extern BOOL pi_init();
extern void pi_clearscreen();
extern void pi_close();
extern void pi_drawline();
extern void pi_resetcolor();
extern void pi_setcolor();
extern void pi_setlinestyle();
extern void pi_text();
extern void pi_update();

/* cursors.c */
extern void com_cursor();
double getdvalue();
double *getdvector();

/* gui.c */
extern void com_gui();

/* pvm.c */
extern void com_pvm();

/* script.c */
extern void com_script();

/* postcoms.c */

extern void com_cross();
extern void com_display();
extern void com_let();
extern void com_unlet();
extern void com_load();
extern void com_print();
extern void com_write();
extern void com_destroy();
extern void com_splot();
extern void com_setscale();
extern void com_transpose();

extern void com_nameplot();
extern void com_pushplot();
extern void com_popplot();
extern void com_plotstack();

extern int isInPlotStack(struct plot *);
extern struct plot *getPlotStackTop();
void resetPlotStack();

extern void com_destroyto();

/* rawfile.c */

extern int raw_prec;
extern void raw_write();
extern struct plot *raw_read();

/* resource.c */

extern void com_rusage();
extern void ft_ckspace();
extern void init_rlimits();

/* runcoms.c */

extern void com_ac();
extern void com_dc();
extern void com_op();
extern void com_pz();
extern void com_sens();
extern void com_rset();
extern void com_resume();
extern void com_run();
extern void com_tran();
extern void com_ssse();	// For steady state analysis by shooting with extrapolation.
extern void com_tf();
extern void com_scirc();
extern void com_namecirc();
extern void com_disto();
extern void com_noise();
extern int ft_dorun();

/* spice.c & nutmeg.c */

extern BOOL menumode;
extern BOOL ft_invisible;
extern BOOL ft_batchmode;
extern BOOL ft_nutmeg;
extern BOOL ft_servermode;
extern IFsimulator *ft_sim;
extern char *ft_rawfile;
extern char *cp_program;
extern SIGNAL_TYPE ft_sigintr();
extern SIGNAL_TYPE sigfloat();
extern SIGNAL_TYPE sigstop();
extern SIGNAL_TYPE sigquit();
extern SIGNAL_TYPE sigill();
extern SIGNAL_TYPE sigbus();
extern SIGNAL_TYPE sigsegv();
extern SIGNAL_TYPE sig_sys();
extern int main(int, char **);

/* spiceif.c & nutmegif.c */

extern BOOL if_tranparams();
extern BOOL if_ssseparams();	// For steady state analysis.
extern char *if_errstring();
extern char *if_inpdeck();
extern int if_run();
extern int if_sens_run();
extern struct variable *(*if_getparam)();
extern struct variable *nutif_getparam();
extern struct variable *spif_getparam();
extern void if_cktfree();
extern void if_inptabfree();
extern void if_cktstructfree(char *ckt);
extern void if_dump();
extern int if_option();
extern void if_setndnames();
extern void if_setparam();
extern struct variable *if_getstat();
extern IFparm *if_parm();

/* subckt.c */

// extern struct line *inp_deckcopy();
// extern struct line *inp_subcktexpand();
// extern int inp_numnodes();

/* types.c */

extern void com_dftype();
extern void com_stype();
extern char *ft_typabbrev();
extern char *ft_typenames();
extern char *ft_plotabbrev();
extern int ft_typnum();
extern void ft_typeinit();

/* vectors.c */

extern BOOL vec_eq();
extern int plot_num;
extern struct dvec *vec_fromplot();
extern struct dvec *vec_copy();
extern struct dvec *vec_get();
extern struct dvec *vec_mkfamily();
extern struct plot *plot_cur;
extern struct plot *plot_alloc();
extern struct plot *plot_list;
extern int plotl_changed;
extern void plot_add();
extern void vec_free();
extern void vec_gc();
extern void ft_loadfile();
extern void vec_new();
extern void plot_docoms();
extern void vec_remove();
extern void ft_sdatafree();
extern void plot_setcur();
extern void plot_new();
extern char *vec_basename();
extern BOOL plot_prefix();
extern void vec_transpose();
extern void *ft_plotpath();
extern void ft_setplotpath();
extern void ft_setfullgc(int a);
extern int ft_getfullgc();

/* writedata.c */

extern volatile BOOL ft_intrpt;
extern BOOL ft_setflag;
extern int wrd_close();
extern int wrd_command();
extern int wrd_cptime;
extern int wrd_end();
extern int wrd_init();
extern int wrd_limpts;
extern int wrd_open();
extern int wrd_output();
extern int wrd_point();
extern int wrd_pt2();
extern int wrd_run();
extern int wrd_stopnow();
extern void wrd_chtrace();
extern void wrd_error();
extern void wrd_version();
extern wordlist *wrd_saves;

/* xinterface.c */

extern void xi_arc();
extern BOOL xi_init();
extern BOOL xi_dump();
extern void xi_clearscreen();
extern void xi_close();
extern void xi_drawline();
extern void xi_resetcolor();
extern void xi_setcolor();
extern void xi_setlinestyle();
extern void xi_text();
extern void xi_update();
extern void xi_zoomdata();
extern struct screen *screens;
extern void com_clearplot();

/* newcoms.c */
extern void com_reshape();

/* dimens.c */
extern char *dimstring();
extern int atodims();
extern char *indexstring();
extern int incindex( );

#endif /* FTEext_h */
