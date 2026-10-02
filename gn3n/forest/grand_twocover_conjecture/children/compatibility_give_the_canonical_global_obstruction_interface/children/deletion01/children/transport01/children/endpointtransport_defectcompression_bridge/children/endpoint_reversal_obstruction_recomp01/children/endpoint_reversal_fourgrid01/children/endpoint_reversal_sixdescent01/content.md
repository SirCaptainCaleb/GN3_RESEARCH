# The maximal endpoint-reversal residue enters bounded six-window structure or strict descent

## Statement

Let H be a minimum counterexample containing a maximal unresolved endpoint reversal as in adecd58bef3d. Then either one of the bounded four-vertex or Hamiltonian four/five-support alternatives already supplied by adecd58bef3d occurs, or |V(H)|<=14, or H has a spanning three-cover admitting explicit strict quadratic-potential descent, or H contains a bounded six-vertex set which is Hamiltonian or whose Hamiltonian one-vertex deletion paths exhibit explicit order disagreement. In particular, for order at least fifteen the residual endpoint-reversal configuration always yields one of these bounded conclusions.

## Body

Apply endpoint_reversal_fourgrid01. If one of the earlier bounded four-vertex or Hamiltonian four/five-support alternatives occurs, we are done. Otherwise, with Y=V(H)-(V(P) union {x}), one has |Y|>=3 and every pair of distinct y,z in Y gives a Hamiltonian four-set W={p_0,p_m,y,z} with non-Hamiltonian path-cover-two complement.

Choose any distinct y,z in Y and write a two-cover H-W=A|B. Apply the certified anchored-four-window theorem independent_reconstruction to W|A|B. It gives exactly one of the following: a bounded six-vertex set U for which either H[U] is Hamiltonian or H[U] is non-Hamiltonian and Hamiltonian one-vertex deletion paths exhibit order disagreement; a legal endpoint transfer producing a spanning three-cover with strictly smaller quadratic potential; or |V(H)|<=14.

These are precisely the remaining alternatives claimed here.