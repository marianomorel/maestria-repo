#ifndef __COMITF_DEFINED
#define __COMITF_DEFINED

// Make macros for stdio functions. They translate stdio functions 
// to ctransport functions. Include ctransport header. 
// Make extern declarations for dummy streams and DataPipes. 

#include "ctransport.h"

// getc() and putc() remain macros operating on ordinary streams
// ctransport is bypassed when calling getc and putc. 
// We use getc() and putc() only when speed is critical and
// we are working on ordinary streams (either stdin, stdout, 
// stderr, or streams opened by fopen()). 

#undef fgetc
// #undef getc
#undef fgets
#undef fread
#undef fputc
// #undef putc
#undef fputs
#undef fwrite
#undef fprintf
#undef fflush

#define fgetc CTRfgetc
// #define getc CTRfgetc
#define fgets CTRfgets
#define fread CTRfread
#define fputc CTRfputc
// #define putc CTRfputc
#define fputs CTRfputs
#define fwrite CTRfwrite
#define fprintf CTRfprintf
#define fflush CTRfflush

#endif
