# All-exchangeable Johnson blocks force the exact odd universal state — preserved pre-item development

## An all-exchangeable Johnson block is forced to the exact odd balanced threshold

Retain a minimum-degree saturated Johnson block U from [[minimum_degree_full_stars_form_saturated_johnson_blocks]], with full-star size d.

Assume first that U=V(H). Then every d-subset F of V is a full-star source. Hence:
- F is non-Hamiltonian;
- F-x is Hamiltonian for every x in F;
- C=V-F is Hamiltonian.

Put c=n-d.

### The complement is strictly smaller than the bad layer

If c>=d, choose any d-set F. Its complement C has order c and is Hamiltonian. A Hamilton order on C contains a contiguous d-vertex subpath, whose support is a Hamiltonian d-subset of V. But every d-subset is non-Hamiltonian. Contradiction.

Therefore
c<d.

### Antipodality creates a second full-star layer

The antipode of a selected edge
F -> F-{x}
is
(V-(F-{x})) -> (V-F),
that is
(C+{x}) -> C.

Since every d-set F is a full-star source, this shows that every (c+1)-set G is also a full-star source: for every x in G, take C=G-{x} and F=V-C.

Thus sources of positive outdegree c+1 exist. Since d was chosen as the minimum positive source outdegree,
d<=c+1.

Combining
c<d<=c+1
gives
d=c+1,
and therefore
n=d+c=2d-1.

Hence the all-exchangeable residue has the exact form
n=2r+1, d=r+1,
with:
- every r-set Hamiltonian;
- every (r+1)-set non-Hamiltonian.

Equivalently every vertex is in the universal fixed-hole branch: for fixed x, every balanced r|r bipartition of V-{x} has Hamiltonian sides, while adjoining x to either side produces a blocked (r+1)-set.

Therefore the all-exchangeable cubical obstruction is not a new general family. It is exactly the old odd universal balanced state, now derived canonically from minimum-degree cubical parity.

The remaining work in this branch is to eliminate that universal odd state using the later Johnson-order disagreement / isolated-root machinery.
