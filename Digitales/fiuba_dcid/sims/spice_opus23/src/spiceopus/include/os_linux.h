// Include file for Linux operating system.
// 1.	#define statements are from os_sysv.h and changed. HAS_POSIXTTY is defined
//		instead of HAS_SYSVTTY. The output from Spice does not confuse the terminal
//		and shell commands works correctly as well. HAS_BSDRLIMIT and HAS_BSDRUSAGE
//		are more adequate then HAS_SYSVRLIMIT and HAS_SYSVRUSAGE.
// 2.	#define HAS_SYS_ERRLIST turn off the declaration sys_errlist in misc.h.
// 3.	Linux has ieee logb so there is no need to declare it.
// Author: Arpad Buermen

#include "os_unix.h"

#define HAS_POSIXTTY		/* <termios.h>				*/
#define HAS_SYSVDIRS		/* <dirent.h>				*/
#define HAS_BSDRLIMIT
#define HAS_BSDRUSAGE
#define HAS_STRCHR		/* strchr( ) instead of index( )	*/
#define HAS_FLOAT_H
#define HAS_ATRIGH		/* acosh( ), asinh( ), atanh( )         */
#define HAS_STDLIB
#define HAS_LINUX_DLL

#define HAS_BCOPY
// #define HAS_NO_IEEE_LOGB
#define HAS_SYS_ERRLIST
