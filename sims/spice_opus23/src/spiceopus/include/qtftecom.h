#ifndef __QTFTECOMM_DEFINED
#define __QTFTECOMM_DEFINED

#include <stdio.h>
#include "qtftepld.h"

// Top level commands
// Escape code
#define SPTC_escape      27
#define MSG_ESC			 SPTC_escape
#define MSG_CMD			 28
// These follow the escape code
#define SPTC_backspace   40
#define SPTC_cr_left     41
#define SPTC_cr_right    42
#define SPTC_cr_up       43
#define SPTC_cr_down     44
#define SPTC_cr_ctrlup   45
#define SPTC_cr_ctrldown 46
#define SPTC_cr_home     47
#define SPTC_cr_end      48
#define SPTC_delete      49
#define SPTC_esckey      50
#define SPTC_jump_left   51
#define SPTC_jump_right  52
// Obsolete
#define FTE_cmd          35

// CMD processor commands (a sequence of these follows FTE_cmd)
#define CMD_plot           0
#define CMD_exit	       1
#define CMD_wmprocevt      2
#define CMD_dialog         3
#define CMD_done		   (char)0xfe
#define CMD_none           0xff

// Dialog subcommands
#define DIALOG_optimize    0
#define DIALOG_show        1

// Plot subcommands
#define PLOT_create        0
#define PLOT_name          1
#define PLOT_xname         2
#define PLOT_yname         3
#define PLOT_type          4
#define PLOT_axistype      5
#define PLOT_displaymode   7
#define PLOT_xpaper       10
#define PLOT_ypaper       11
#define PLOT_xindices     12
#define PLOT_xcompress    13
#define PLOT_xdelta       14
#define PLOT_ydelta       15
#define PLOT_pointtype    16
#define PLOT_pointsize    17
#define PLOT_linetype     18
#define PLOT_linewidth    19
#define PLOT_drawgrid     20
#define PLOT_colorbg      21
#define PLOT_colorgrid    22
#define PLOT_addvec       23
#define PLOT_nextvec      24
#define PLOT_selectvec    25
#define PLOT_addmpnt      26
#define PLOT_addmscalepnt 27
#define PLOT_repaint      28
#define PLOT_autoscale    29
#define PLOT_autoscalewr  30
#define PLOT_destroy      31
#define PLOT_show         32
#define PLOT_hide         33
#define PLOT_setwinwidth  34
#define PLOT_setwinheight 35
#define PLOT_showinfo     36
#define PLOT_autoident    37
#define PLOT_append       38
#define PLOT_select       40
#define PLOT_aspect       41
#define PLOT_units        42
#define PLOT_print_wmm    43
#define PLOT_print_hmm    44
#define PLOT_print_pwmm   45
#define PLOT_print_phmm   46
#define PLOT_print_mamm   47
#define PLOT_print_hpos   48
#define PLOT_print_vpos   49
#define PLOT_print_title  50
#define PLOT_print_time   51
#define PLOT_print        52

#endif
