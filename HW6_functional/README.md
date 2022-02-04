## HW6 - Modifications of functions

- **sequential_map** - the function takes any number of functions and one container as arguments and returns a list of consequent application of accepted functions to the values in container
- **consensus_filter** - the function takes any number of functions (which return True or False) and one container as arguments and returns list with only "True" values
- **conditional_reduce** - the function takes 2 functions (the first should take one argument and return True or False and the second should take two arguments and return the result) and one container as arguments and returns only one value as a result of the second function, applied to "True" values according to the first function
- **func_chain** - the function takes any number of functions as arguments and returns the united function (consequently applied)
