# Every large staircase minimum has a Hamiltonian four-support with two-cover complement

## Statement


Let H be a minimum counterexample with a globally quadratic-potential-minimal staircase three-cover of component orders (c+2,c+1,c), c>=4. Then H contains a proper Hamiltonian four-vertex set W such that H-W is non-Hamiltonian with path-cover number two.


## Body


Choose the two endpoints L,R of the largest staircase component and any three vertices D disjoint from {L,R}. Since c>=4, the order is at least fifteen, so such a three-set exists. Apply reversal_global_frontier01 to L,R,D. It gives distinct y,z in D such that W={L,R,y,z} is Hamiltonian and H-W is non-Hamiltonian with path-cover number two. Thus the entire former staircase reversal chain is unnecessary for this conclusion.
