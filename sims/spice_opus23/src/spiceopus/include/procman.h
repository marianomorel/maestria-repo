#ifndef PROCMAN_H
#define PROCMAN_H

#ifdef WIN32
#include <windows.h>
typedef HANDLE phandle;
#define NULLph NULL
#else
#include <unistd.h>
typedef int phandle;
#define NULLph 0
#endif

phandle deployProcess(char *, int *);
int terminateProcess(phandle);

#endif
