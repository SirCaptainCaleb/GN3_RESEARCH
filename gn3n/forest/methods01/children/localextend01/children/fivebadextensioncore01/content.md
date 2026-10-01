# Bad extensions of a Hamiltonian five-set have a common deletion core

## Statement

Let X be a Hamiltonian five-vertex set in a boundary tournament H, and let E be a set of vertices outside X such that H[X union {e}] is non-Hamiltonian for every e in E. For each e in E, at least three vertices x in X satisfy that H[(X-{x}) union {e}] is Hamiltonian. Consequently some x in X works for at least ceil(3|E|/5) vertices e in E. In particular, for two such exterior vertices one common x works for both, and for four such exterior vertices one common x works for at least three.

## Body

Fix e in E. The six-set X union {e} is non-Hamiltonian, but deleting e leaves the Hamiltonian five-set X. By the certified four-of-six theorem, at least four of the six one-vertex deletions of X union {e} are Hamiltonian. One is the deletion of e, so at least three deletions x in X give Hamiltonian five-sets (X-{x}) union {e}. Let I_e be this set; |I_e|>=3.

Count incidences (x,e) with x in I_e. There are at least 3|E| incidences over five possible x in X, so some x belongs to at least ceil(3|E|/5) sets I_e.

For |E|=2 this lower bound is 2, giving one four-vertex core X-{x} that Hamiltonizes with both exterior vertices. For |E|=4 it is 3, giving one common core for at least three of the four exterior vertices.

This abstracts the proof mechanisms of astra003fivecommoncore and astra003fivethreeendpoints. Their quadratic-minimal trapped-cover hypotheses are used only upstream to prove that the relevant six-set extensions X union {e} are non-Hamiltonian; once those local hypotheses are available, no repartition, minimality, or Astra assumption is used.