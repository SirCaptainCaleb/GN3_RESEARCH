# A Hamiltonian five-set with three exterior labels yields a six-set or a common four-core

## Statement

Let H be a minimum counterexample. Let X be a Hamiltonian five-vertex set and let E be a set of at least three vertices outside X. Then either some X union {z}, z in E, is Hamiltonian, in which case H contains a proper Hamiltonian six-set with non-Hamiltonian path-cover-two complement, or there is a four-set C and three distinct vertices r1,r2,r3 outside C such that each C union {ri} is Hamiltonian and each complement is non-Hamiltonian with path-cover number two.

## Body

If some z in E makes X union {z} Hamiltonian, then X union {z} is proper because E has at least three vertices. Its complement cannot be Hamiltonian in a minimum counterexample, and minimality gives path-cover number two. Otherwise every six-set X union {z}, z in E, is non-Hamiltonian. Apply fivebadextensioncore01. Some x in X has at least ceil(3|E|/5)>=2 distinct labels z1,z2 in E such that (X-{x}) union {zi} is Hamiltonian. Put C=X-{x}. Then C union {x}=X, C union {z1}, and C union {z2} are three Hamiltonian five-sets. Each is proper; the same minimum-counterexample argument gives non-Hamiltonian path-cover-two complements.
