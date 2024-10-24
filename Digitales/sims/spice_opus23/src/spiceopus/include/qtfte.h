#ifndef __QTFTE_H_DEFINED
#define __QTFTE_H_DEFINED

int qtfte_init(int argc, char **argv, 
				int invisible, int fontsize, char *outfile, 
				int (* engineEntry)(int, char **));

#endif
