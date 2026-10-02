# Every large staircase minimum has a Hamiltonian four-support with two-cover complement

## Statement

Let H be a minimum counterexample and let A|B|C be a globally quadratic-potential-minimal spanning three-cover with component orders (c+2,c+1,c), where c>=4. Then H contains a proper Hamiltonian four-vertex set W such that H-W is non-Hamiltonian with path-cover number two.

## Body

Choose any two distinct vertices L,R of H and any three-element set D disjoint from {L,R}; such a choice exists because a minimum counterexample has order greater than ten. By reversal_global_frontier01, two distinct vertices y,z in D make W={L,R,y,z} Hamiltonian and make H-W non-Hamiltonian with path-cover number two. Thus the conclusion holds without using the staircase-specific noninsertion, reversal, endpoint-synchronization, or five/six-support case analysis. The staircase hypotheses are retained only because this theorem replaces that proof branch; the conclusion is in fact available for every minimum counterexample.