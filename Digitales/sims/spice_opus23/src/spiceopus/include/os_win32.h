// Include file for Windows operating systems.
// Author: Janez Puhan

#define     DIR_CWD		"."
#define     DIR_PATHSEP		"\\"
#define     DIR_TERM		'\\'
#define	    TEMPFORMAT		"%s%d.tmp"

#define HAS_WINDOWS_FLOAT
#define HAS_FILE_IPC
#define HAS_ASCII
#define HAS_CHDIR		/* for tree filesystems, chdir( )	*/
#define HAS_CLEARERR		/* clearerr( ), should be in stdio	*/
#define HAS_CTYPE		/* <ctype.h>, iswhite( ), etc.		*/
#define HAS_DOSDIRS		/* Emulate opendir, etc.		*/
#define HAS_MEMAVL		/* Use _memavl( ) 			*/
#define HAS_ENVIRON
#define HAS_FTIME	// This is a brake. ftime() is ultraslow in Windows.
#define HAS_GETCWD		/* getcwd(buf, size)			*/
#define HAS_LOCALTIME
#define HAS_LONGJUMP		/* setjmp( ), longjmp( )		*/
#define HAS_NOINLINE
#define HAS_PCTERM
#define HAS_QSORT		/* qsort( )				*/
#define HAS_SHORTMACRO
#define HAS_STAT
#define HAS_STDLIB
#define HAS_STRCHR		/* strchr( ) instead of index( )	*/
#define HAS_SYSTEM
#define HAS_QT_FTE	// Graphic support is provided by QT.
// #define HAS_UNIX_SIGS	// Not used anymore, got exception handling.
#define HAS_UNLINK
#define HAS_LIMITS_H
#define HAS_FLOAT_H
#define HAS_NO_IEEE_LOGB
#define HAS_NO_ERFC
#define HAS_STRICMP
#define HAS_WIN32_DLL
#define HAS_UNDERSCORE_ISNAN	// Weird WIN32 syntax.
#define HAS_UNDERSCORE_FINITE

#define WANT_PCHARDCOPY
