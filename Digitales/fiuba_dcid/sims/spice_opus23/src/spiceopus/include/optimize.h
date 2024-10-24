// General header file for optimize command implementation.
// Author: Janez Puhan

#include <stdio.h>
#include "spice.h"
#include "util.h"
#include "ftedefs.h"

struct method	// Structure with optimisation method properties.
{
	char *name;	// Method's name.
	char **num_names;	// Array with names of numerical parameters.
	double *num_vals;	// Array with values of numerical parameters.
	int num_no;	// Number of numerical parameters.
	char **str_names;	// Array with names of string parameters.
	char **str_vals;	// Array with values of string parameters.
	int str_no;	// Number of string parameters.
};

struct parameter	// Structure with explicit constraints, initial value etc. for a particular parameter.
{
	char *name;	// Optimisation parameter name.
	int name_given;
	double low;	// Explicit constraints.
	int low_given;
	double high;
	int high_given;
	double initial;	// Initial parameter value.
	int initial_given;
	double increment;	// Increment step value at discrete parameter space.
	int increment_given;
	double mean;	// Mean value at normal distribution.
	int mean_given;
	double deviation;	// Standard deviation.
	int deviation_given;
	double abs_tol;	// Absolute tolerance.
	int abs_tol_given;
	double rel_tol;	// Relative tolerance.
	int rel_tol_given;
	int log;	// Logarithmic scale.
	double original;	// Parameter value before starting the optimisation process.
};

extern void setparams(); // Sets the parameters to the last values in the results table.
extern void set_params(struct wordlist *command);	// Function sets the parameters of the optimisation method.
extern void scan_set(struct wordlist *word);	// Function sets the parameters for scanning the parameter space through a selected point in axes directions.
extern void axis_set(struct wordlist *word);	// Function sets the parameters of the axis search optimisation method.
extern void simplex_set(struct wordlist *word);	// Function sets the parameters of the complex optimisation method.
//----------------------------------------------------------------------------
extern void comtrust_set(struct wordlist *word);	// Function sets the parameters of the hybrid complex-trust region optimisation method.
//----------------------------------------------------------------------------
extern void dfp_set(struct wordlist *word);	// Function sets the parameters of the Davidon-Fletcher-Powell optimisation method.
extern void genetic_set(struct wordlist *word);	// Function sets the parameters of the genetic algorithm.
extern void grid_set(struct wordlist *word);	// Function sets the parameters of the grid search optimisation method.
extern void hj_set(struct wordlist *word);	// Function sets the parameters of the Hooke-Jeeves optimisation method.
extern void monte_set(struct wordlist *word);	// Function sets the parameters of the Monte Carlo optimisation method.
extern void newton_set(struct wordlist *word);	// Function sets the parameters of the Newton optimisation method.
extern void space_set(struct wordlist *word);	// Function sets the parameters of the brute force optimisation method.
extern void powell_set(struct wordlist *word);	// Function sets the parameters of the Powell optimisation method.
extern void simulated_annealing_set(struct wordlist *word);	// Function sets the parameters of the simulated annealing optimisation method.
extern void steepest_set(struct wordlist *word);	// Function sets the parameters of the steepest descent optimisation method.

extern void free_population(int message);	// Function frees memory with current or last population in genetic algorithm.
extern void free_pts();	// Function frees memory with array of points calculated in previous optimisation runs.
extern void free_method();	// Function frees memory with optimisation method parameters. It also frees genetic algorithm's population if one exists.

extern void optimize();	// Function starts optimisation loop.
extern double evaluate(double *point);	// Function sets the circuit into given point, perform requested analyses and calculate cost function value in that point.
extern void new_params(double *point, int discrete);	// Function sets new parameter values.
extern int org_value(int i);	// Function reads i-th parameter's value. It returns one if successful and zero otherwise.
extern double round(double x);	// Function rounds double value.
extern void set_max_iter(unsigned long int num);	// Function verifies authentication and then sets max_iter variable to a given value.

extern double* grad(double *grad, double *point, double cost);	// Function calculates the cost function gradient in given point. Returns derivative values of the transformation from constrained to unconstrained space.
extern double new_direction(double *direction, double **matrix, double *grad, double *deriv);	// Function multiplies the cost function gradient with given matrix and therefore changes the search direction. Returns the length of initial step in new direction.
extern double norm(double *direction, double* deriv);	// Function norms length in given direction and returns initial step size in that direction.
extern void transform(double *unconstrained, double *constrained, char *transformation);	// Function transforms point from unconstrained into explicitly constrained space.

extern double fibonacci(double *first, double cnst, double first_val, double third_val, double *best, double *grad, double init_step);	// Function search for the minimum in the given direction with Fibonacci method. Returns minimum cost value.
extern double tra_fib(double *first, double cnst, double first_val, double third_val, double *best, double *grad, double init_step);	// Function search for the minimum in the given direction with Fibonacci method. Before the analyses are performed the transformation from unconstrained to constrained space is done. Returns minimum cost value.
extern double golden(double *first, double cnst, double first_val, double third_val, double *best, double *grad, double init_step);	// Function search for the minimum in the given direction with golden ratio method. Returns minimum cost value.
extern double tra_gold(double *first, double cnst, double first_val, double third_val, double *best, double *grad, double init_step);	// Function search for the minimum in the given direction with golden ratio method. Before the analyses are performed the transformation from unconstrained to constrained space is done. Returns minimum cost value.
extern double qaudratic(double *first, double cnst, double first_val, double second_val, double third_val, double *best, double *grad, double init_step);	// Function search for the minimum in the given direction with quadratic method. Returns minimum cost value.
extern double tra_quad(double *first, double cnst, double first_val, double second_val, double third_val, double *best, double *grad, double init_step);	// Function search for the minimum in the given direction with quadratic method. Before the analyses are performed the transformation from unconstrained to constrained space is done. Returns minimum cost value.

extern void results(double *optimum, double init_time, double lowest);	// Function prints some data about optimisation loop and results.
extern char *new_name(char *name);	// Function deletes all '@' and ']' chars and '[' are changed into '_' in input string. Input string remains unchanged, memory is reserved for output string.

extern void scan(double init_time);	// Check parameter space in co-ordinate directions through given point.
extern void axis(int *plot, double init_time);	// Axis search algorithm.
extern void simplex(int *plot, double init_time);	// Constrained simplex algorithm.
//----------------------------------------------------------------------------
extern void comtrust(int *plot, double init_time);	// Hybrid simplex-trust region algorithm.
//----------------------------------------------------------------------------
extern void dfp(int *plot, double init_time);	// Davidon-Fletcher-Powell's algorithm.
extern void genetic(double init_time);	// Genetic algorithm.
extern void grid(int *plot, double init_time);	// Grid search algorithm.
extern void hj(int *plot, double init_time);	// Hooke-Jeeves's algorithm.
extern void monte_carlo(int *plot, double init_time);	// Random search.
extern void newton(int *plot, double init_time);	// Newton's algorithm.
extern void space(double init_time);	// Brute force.
extern void powell(int *plot, double init_time);	// Powell's algorithm.
extern void simulated_annealing(int *plot, double init_time);	// Simulated annealing algorithm.

//---------------------------
// Jernej Olensek
extern void psade_set(struct wordlist *word);
extern void psade(int *plot, double init_time);

extern void sa_set(struct wordlist *word);
extern void sa(int *plot, double init_time);

extern void de_set(struct wordlist *word);
extern void de(int *plot, double init_time);
//---------------------------


extern void steepest(int *plot, double init_time);	// Steepest descent algorithm.

extern double *new_init();	// Function reviews all calculated points in parameter space and gives new initial trial where parameter space was not checked yet.

extern void read_initials(FILE *file);	// Read initial values from dump file.
extern void write_initials(FILE *file);	// Write initial values to dump file.

extern struct wordlist **analyses;	// Pointer to analysis array.
extern int analyses_size;	// Size of analysis array.
extern struct wordlist **implicits;	// Pointer to implicit constraints array.
extern int implicits_size;	// Size of implicit constraints array.
extern struct parameter *params;	// Pointer to parameter array.
extern int params_size;	// Size of parameter array.
extern struct wordlist *cost_func;	// Pointer to cost function.
extern struct method cur_method;	// Current optimisation method.
extern double **results_array;	// Pointer to results array, where the results are saved during the optimisation run.
extern unsigned long int results_size;	// Current size of results array.
extern unsigned long int max_iter;	// Maximum allowed number of iterations regardless unconvergence of the optimisation method.
extern unsigned long int iter;	// Number of iterations performed.
extern double **calculated;	// Array of already calculated points in parameter space.
extern unsigned long int calculated_size;	// Size of array of already calculated points.
extern int weight;	// Weight of point with maximum cost function value.
extern int init_warn;	// Flag for printing initial_guess warning.
extern struct plot *opt_plot;	// Pointer to the plot optimize created during the optimisation process.
extern struct individual *population;	// Last population of the genetic algorithm. It continues from this population, if one exists.
extern double stop_cost;	// Stop criterion.
extern int center;	// Flag for cost function evaluating inside tolerances.
extern int discrete_space;	// Flag for discrete optimisation parameter space.
