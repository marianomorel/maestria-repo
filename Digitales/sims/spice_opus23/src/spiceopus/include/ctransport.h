// C and C++ level acces to DataPipe, equivalents of stdio function, etc. 

#ifndef __CTRANSPORT_DEFINED
#define __CTRANSPORT_DEFINED

#include <stdarg.h>

#ifdef __cplusplus
#include <transport.h>
#define CLINKAGE extern "C"
#else
#define CLINKAGE extern
#endif

// ctransport's c interface
CLINKAGE int CTRinit(int);

CLINKAGE void CTRsetStreams(FILE *, FILE *, FILE *); 

CLINKAGE FILE *CTRgetIn();

CLINKAGE FILE *CTRgetOut();

CLINKAGE FILE *CTRgetErr();

CLINKAGE int CTRfflush(FILE *stream);

CLINKAGE int CTRfgetc(FILE *stream);

CLINKAGE char *CTRfgets(char *string, int n, FILE *stream);

CLINKAGE size_t CTRfread(void *buffer, size_t size, size_t count, FILE *stream);

CLINKAGE int CTRfputc(int c, FILE *stream);

CLINKAGE int CTRfputs(const char *string, FILE *stream);

CLINKAGE size_t CTRfwrite(const void *buffer, size_t size, size_t count, FILE *stream);

CLINKAGE int CTRinternalSprintf(char **buf, const char *format, va_list args); 

CLINKAGE int CTRfprintf(FILE *stream, const char *format, ...);

CLINKAGE int CTRstreamCheckData(FILE *stream);

CLINKAGE void *CTRmakeOrdinaryBlock(void *buf, int size);

CLINKAGE void CTRfreeOrdinaryBlock(void *buf);

CLINKAGE int CTRstreamSendMemBlock(FILE *stream, void *buf, int size);

CLINKAGE size_t CTRstreamSendChar(FILE *stream, char ch);

CLINKAGE size_t CTRstreamSendLong(FILE *stream, long l);

CLINKAGE size_t CTRstreamSendInt(FILE *stream, int l);

CLINKAGE size_t CTRstreamSendDouble(FILE *stream, double d);

CLINKAGE size_t CTRstreamSendString(FILE *stream, char *str);

CLINKAGE size_t CTRstreamSendDoubleArray(FILE *stream, double *d, int l);

CLINKAGE int CTRstartLogging(char *name);

CLINKAGE int CTRstopLogging();

CLINKAGE int CTRsuspendLogging();

CLINKAGE int CTRresumeLogging();

CLINKAGE int CTRlog(const char *);


// This is needed only in GUI (c++)

#ifdef __cplusplus

DataPipe *CTRgetDpIn();

DataPipe *CTRgetDpOut();

DataPipe *CTRgetDpErr();

int CTRdpPrintf(DataPipe *dp, const char *format, ...);

void *CTRdpRecvMemBlock(DataPipe *dp, int *size);

int CTRdpRecvChar(DataPipe *dp, char *ch);

int CTRdpRecvLong(DataPipe *dp, long *l);

int CTRdpRecvInt(DataPipe *dp, int *l);

int CTRdpRecvDouble(DataPipe *dp, double *d);

int CTRdpRecvString(DataPipe *dp, char **s, int *l);

int CTRdpRecvDoubleArray(DataPipe *dp, double **s, int *l);

#endif

#endif
