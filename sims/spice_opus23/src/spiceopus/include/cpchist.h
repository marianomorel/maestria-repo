#ifndef __CURSOR_HIST
#define __CURSOR_HIST

// This file is about cursor controlled history access for QT frontend.
// Written by Arpad Buermen

extern void cp_cursor_hist_reset();
extern void cp_cursor_hist_go_latest();
extern void cp_cursor_hist_go_previous();
extern void cp_cursor_hist_go_next();
extern void cp_cursor_hist_go_oldest();
extern int cp_cursor_hist_valid();
extern int cp_cursor_hist_send(FILE *, char *, int);

#endif
