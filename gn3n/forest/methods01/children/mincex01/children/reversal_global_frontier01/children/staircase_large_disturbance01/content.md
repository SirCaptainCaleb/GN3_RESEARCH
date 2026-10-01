# From order eighteen staircase minima yield order disagreement, strict descent, or a lower-state cross-component edge

## Statement

Let H be a minimum counterexample with a globally Phi-minimal staircase three-cover of component orders (c+2,c+1,c), where c>=5, so n=3c+3>=18. Then at least one of the following occurs: (1) order disagreement between Hamiltonian paths on overlapping supports; (2) a spanning three-cover in the relevant pairwise-repartition component has strictly smaller quadratic potential Phi; (3) in a lower state of a Hamiltonian-four-core two-label path-cover-two square, some two-cover contains an ordinary edge whose endpoints lie in two different components of the corresponding three-path cover.

## Body

Apply reversal_global_frontier01 to obtain a proper Hamiltonian four-set W whose complement is non-Hamiltonian with path-cover number two.

Since n>=18, apply 7bab8dd31d87 to W. It yields strict Phi descent, order disagreement, or a proper Hamiltonian six-set U with non-Hamiltonian path-cover-two complement.

In the six-set branch, apply ham6goodsquare01. It gives distinct d,e in U and the Hamiltonian four-core D=U-{d,e} such that, with K=H-U, all four states K, K+d, K+e, K+d+e are non-Hamiltonian with path-cover number two, while D+d and D+e are Hamiltonian. Because n>=18, ham4squareescape01 applies. It yields either a lower square state whose two-cover contains an ordinary edge with endpoints in two different components of the corresponding three-path cover, strict Phi descent, or order disagreement.

These alternatives are exactly the three outcomes in the statement.
