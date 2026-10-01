# Every two-label core enlargement is non-Hamiltonian in the all-split cocycle branch

## Statement

In the all-three-split common-core support-switch branch of compatsupportham22, write V(H)=R disjoint-union S disjoint-union {a,b,c}. Then for every distinct x,y in {a,b,c}, both H[R union {x,y}] and H[S union {x,y}] are non-Hamiltonian. Consequently, in the two-core transposition residue c6e468569768, whenever two special labels share one internal insertion gap on a core, the resulting Hamiltonian four-set from the parallel-middle lemma lies inside a non-Hamiltonian two-label enlargement of that entire core; if the shared gap is an endpoint gap, the same pair is a common endpoint-extender pair. Thus each core of the surviving transposition residue has exactly this endpoint-extender versus Hamiltonian-four-kernel/non-Hamiltonian-enlargement dichotomy.

## Body

Fix distinct x,y and let z be the third special label. By compatsupportham22 in the all-three-split branch, S union {z} is Hamiltonian. If R union {x,y} were Hamiltonian, these two disjoint Hamiltonian supports would partition V(H), giving a spanning two-cover, contradiction. Therefore R union {x,y} is non-Hamiltonian. Interchanging R,S proves the symmetric assertion.

Now apply this to the shared-gap pair supplied on either core by c6e468569768. If the common gap is internal between consecutive core vertices u,v, individual insertion of x and y gives (u,x,v) and (u,y,v) tight, so the certified parallel-middle lemma yields a Hamiltonian four-set on {u,v,x,y}; nevertheless the whole core enlarged by {x,y} is non-Hamiltonian by the first paragraph. If the common gap is an endpoint gap, the two selected Hamilton paths simply exhibit x and y as common extenders of that endpoint. No claim of full-core Hamiltonicity is made from the internal four-set.
