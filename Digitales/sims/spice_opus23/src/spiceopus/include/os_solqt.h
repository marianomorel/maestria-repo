// Include file for Solaris operating system.
// 1.	#define statements are from os_sysv.h and changed. HAS_BSDRLIMIT and
//		HAS_BSDRUSAGE are more adequate then HAS_SYSVRLIMIT and HAS_SYSVRUSAGE.
// 2.	#define HAS_SYS_ERRLIST turn off the declaration sys_errlist in misc.h.
// 3.	Solaris has ieee logb so there is no need to declare it.
// 4.	Qt frontend support (HAS_QT_FTE) added.
// 5.	Define HAS_INTWAITSTATUS added.
// 6.	Undef HAS_BSDDIRS added.
// Author: Arpad Buermen

#include "os_unix.h"

#define HAS_SOLARIS_FLOAT
#define HAS_FILE_IPC
#undef  HAS_POSIXTTY		/* no <termios.h>			*/
#undef  HAS_ISATTY
#undef  HAS_BSDDIRS
#define HAS_SYSVDIRS		/* <dirent.h>				*/
#define HAS_BSDRLIMIT
#define HAS_BSDRUSAGE
#define HAS_STRCHR		/* strchr( ) instead of index( )	*/
#define HAS_FLOAT_H
#define HAS_ATRIGH		/* acosh( ), asinh( ), atanh( )         */
#define HAS_QT_FTE
#define HAS_LINUX_DLL
#define HAS_INTWAITSTATUS

#define HAS_BCOPY
#undef  HAS_NO_IEEE_LOGB
#define HAS_SYS_ERRLIST
