/**********
Copyright 1990 Regents of the University of California.  All rights reserved.
**********/

#include "os_sysv.h"
#ifndef HPUXR9 /* latter version does not need following definitions */
#undef HAS_ATRIGH
#define void int

#define HAS_NO_IEEE_LOGB
#endif
