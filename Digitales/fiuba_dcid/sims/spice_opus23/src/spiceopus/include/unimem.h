#ifndef __UNIMEM_H
#define __UNIMEM_H

#include <stdio.h>

// Global memory leak tracking switch
// Turn on (1) to debug memory anywhere in the engine
#ifndef MEMORY_STATUS_RECORD
#define MEMORY_STATUS_RECORD 1
#endif

//////////
// Do not use these
//////////
// Lowest level functions (shouldn't be used, except in QT frontend)
extern void free_pj(void *mem_address, const char *f, int l, int sw);	// Declarations of functions for memory management.
extern void *malloc_pj(size_t num_bytes, const char *f, int l, int sw);
extern void *realloc_pj(void *mem_address, size_t newsize, const char *f, int l, int sw);
extern void dbg_spice_memdump(FILE *);
extern char *copy_internal(char *, const char *, int, int);
extern void memtrack_set_switch(int);
extern int memtrack_switch();
extern void memtrack_annotate(void *, const char *, int);

//////////
// Do not use these
//////////
// Internal allocation functions with failsafe mechanism (error printout) 
// Use these always if possible
extern char *tmalloc_internal(size_t num, int clean, const char *f, int l, int sw);
extern char *trealloc_internal(char *str, size_t num, const char *f, int l, int sw);
extern void tfree_internal(char *ptr, const char *f, int l, int sw);

//////////
// Use these
//////////
// Real failsafe functions.
// These are used in conjunction with the qt frontend.
#define tmalloc(a) tmalloc_internal((a), 1, __FILE__, __LINE__, MEMORY_STATUS_RECORD)
#define trealloc(a,b) trealloc_internal((char *)(a), (b), __FILE__, __LINE__, MEMORY_STATUS_RECORD)
#define tfree(a) {tfree_internal((char *)(a), __FILE__, __LINE__, MEMORY_STATUS_RECORD); (a) = NULL;}
#define copy_string(a) copy_internal((a), __FILE__, __LINE__, MEMORY_STATUS_RECORD)

//////////
// You can also use these. Legacy code, avoid where possible.
//////////
// Some further macros (all of them use the failsafe allocation mechanism)
#define MALLOC(x) tmalloc(((unsigned)(x)))
#define REALLOC(x,y) trealloc(((char *)(x)),((unsigned)(y)))
#define FREE(x) tfree(x)
#define ZERO(PTR,TYPE)	(bzero((PTR),sizeof(TYPE)))

#define	alloc(TYPE)	((TYPE *) tmalloc(sizeof(TYPE)))

#endif
