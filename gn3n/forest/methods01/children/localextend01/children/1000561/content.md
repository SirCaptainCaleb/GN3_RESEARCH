# A non-Hamiltonian six-set has adjacent good deletion pairs or a perfect-matching good graph

## Statement

Let H be a minimum counterexample and let U be a non-Hamiltonian six-vertex set. Let D={d in U: U-{d} is Hamiltonian}, and define J on D by de in E(J) exactly when U-{d,e} is Hamiltonian. Then |D|>=4 and delta(J)>=1. Hence exactly one of the following holds. (1) J has two adjacent edges de,df. Then U-{d,e} and U-{d,f} are Hamiltonian four-sets meeting in three vertices; their complements are non-Hamiltonian with path-cover number two, so d9a4b66724d2 yields a Hamiltonian five-set on their union or at least four Hamiltonian four-subsets of that five-set, all with path-cover-two complements. (2) J has no adjacent edges. Then J is a perfect matching on D; in particular |D| is 4 or 6.

## Body

Apply d2205c472e75. It gives |D|>=4 and delta(J)>=1, and every J-edge de corresponds to a Hamiltonian four-set U-{d,e} whose complement is non-Hamiltonian with path-cover number two. If J has adjacent edges de and df, the corresponding four-sets intersect in U-{d,e,f}, which has order three. Apply d9a4b66724d2 to obtain alternative (1). If J has no adjacent edges, every vertex has degree at most one. Together with delta(J)>=1, every vertex has degree exactly one, so J is a perfect matching. Since D is a subset of the six-set U and |D|>=4, the even cardinality of a perfect matching forces |D| in {4,6}.
