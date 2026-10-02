# Above order seventeen a Hamiltonian six-support with path-cover-two complement already descends or disagrees

## Statement

Let H be a minimum counterexample of order n>=18. If U is a proper Hamiltonian six-vertex set and H-U is non-Hamiltonian with path-cover number two, then H contains explicit order disagreement or a spanning three-cover lying in a pairwise-repartition component with strictly smaller quadratic potential. Consequently, in hardreversal_six_or_disagree01 the Hamiltonian-six alternative can be consumed directly above order seventeen; no two-label square analysis is needed.

## Body

Choose a Hamilton tight path U=(u_0,u_1,u_2,u_3,u_4,u_5) and put W=U-{u_0}. Then W is a Hamiltonian five-set. Let K=H-U. If K+u_0 were Hamiltonian, its Hamilton path together with the inherited Hamilton path on W would form a spanning two-cover of H, impossible. Since K+u_0 is a proper induced subtournament of the minimum counterexample, it has path-cover number two. Thus W is a proper Hamiltonian five-set with non-Hamiltonian path-cover-two complement. Apply ham5_large_escape01, valid for n>=18, to obtain strict quadratic descent in the move component of W|P|Q for a two-cover P|Q of H-W, or explicit order disagreement.