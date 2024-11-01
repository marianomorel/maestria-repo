//////////
// Modifications in the original code:
// 1.	Added support for Windows operating systems.
// Author: Janez Puhan
//////////
// 2.	Added support for Linux and Solaris.
// Author: Arpad Burmen
//////////

/**********
Copyright 1990 Regents of the University of California.  All rights reserved.
**********/

/*
 *  Operating System
 */

#ifdef aix
#  include "os_aix.h"
#  define CONFIGURED
#endif

#ifdef bsd
#  include "os_bsd.h"
#  define CONFIGURED
#endif

#ifdef ultrix
#  include "os_ultrx.h"
#  define CONFIGURED
#endif

#ifdef sun
#  include "os_sun.h"
#  define CONFIGURED
#endif

#ifdef hpux
#  include "os_hpux.h"
#  define CONFIGURED
#endif

#ifdef sequent
#  include "os_dynix.h"
#  define CONFIGURED
#endif

#ifdef sgi
#  include "os_sysv.h"
#  define CONFIGURED
#endif

#ifdef ipsc
#  include "os_ipsc.h"
#  define CONFIGURED
#endif

#ifdef MSDOS
#  include "os_msdos.h"
#  define CONFIGURED
#endif

#ifdef WIN32	// Support for Windows operating systems.
#include "os_win32.h"
#define CONFIGURED
#endif

#ifdef NeXT
#  include "os_bsd.h"
#  define CONFIGURED
#endif

#ifdef THINK_C
#  include "os_mac.h"
#  define CONFIGURED
#endif

#ifdef alpha_osf
#  include "os_osf.h"
#  define CONFIGURED
#endif

#ifdef linux	// Added by Arpad Burmen.
#  include "os_linux.h"
#  define CONFIGURED
#endif

#ifdef lnxqt	// Added by Arpad Burmen.
#  include "os_lnxqt.h"
#  define CONFIGURED
#endif

#ifdef solqt	// Added by Arpad Burmen.
#  include "os_solqt.h"
#  define CONFIGURED
#endif


#ifndef CONFIGURED

error error error error

Operating system type unknown

error error error error

#endif
