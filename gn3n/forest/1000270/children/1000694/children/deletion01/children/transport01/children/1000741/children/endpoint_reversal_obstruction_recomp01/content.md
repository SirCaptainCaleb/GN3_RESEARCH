# Endpoint reversals reduce to a bounded four-vertex frontier or a universal two-end obstruction family

## Statement


Let H be a minimum counterexample. Then either H contains one of the bounded four-vertex configurations arising from the reversed-edge classification—a Hamiltonian four-set with non-Hamiltonian path-cover-two complement, the exceptional cyclic non-Hamiltonian four-set, or the non-Hamiltonian matching-block four-set with its forced reverse fan—or there is a tight path P=(p_0,...,p_m), m>=2, and an exterior vertex x with (p_1,p_0,x) tight, chosen with |P| maximal among all such unresolved initial-end reversal pairs, such that for every y outside V(P) with y!=x both (p_1,p_0,y) and (y,p_m,p_{m-1}) are tight, and for each such y either H has a proper Hamiltonian support of order four or five containing y and the two ends of P whose complement is non-Hamiltonian with path-cover number two, or (p_m,y,p_0) is tight. Consequently, if no such small Hamiltonian support occurs, at least three vertices y outside V(P), distinct from x, simultaneously satisfy (p_1,p_0,y), (p_m,y,p_0), and (y,p_m,p_{m-1}) tight. The terminal-end version holds symmetrically.


## Body


Take the reversal supplied by 7ba450ffcfe5 on a tight path. If the reversed displayed edge is internal, apply 53005a4e0315. Its Hamiltonian, cyclic, and matching-block alternatives give the bounded four-vertex frontier; in the matching-block case 4f2ce6135f9c supplies the forced reverse fan. Thus only endpoint-edge reversals remain.

At an initial endpoint, the orientation (x,p_1,p_0) is classified by the same successor-side four-vertex argument: with the inherited triple (p_0,p_1,p_2), the four vertices {x,p_0,p_1,p_2} are Hamiltonian, cyclic, or matching-block with the same forced reverse fan. Hence, outside the bounded frontier, the only unresolved initial orientation is (p_1,p_0,x). The terminal endpoint is analogous, leaving only (x,p_m,p_{m-1}).

Choose an unresolved initial pair (P,x) with |P| maximal. Assume the bounded four-vertex frontier does not occur, and let y lie outside V(P) with y!=x. If (y,p_0,p_1) were tight, then prepending y would produce a longer tight path while x remained exterior and reversed the now-internal edge p_0p_1; 53005a4e0315 would then give the bounded frontier, contradiction. Boundary antisymmetry therefore gives (p_1,p_0,y) tight.

If (p_{m-1},p_m,y) were tight, appending y would give a longer unresolved pair with the same exterior witness x, contradicting maximality. Hence boundary antisymmetry gives (y,p_m,p_{m-1}) tight.

Now test (p_0,y,p_m). If it is tight, then for m>=3 the sequence (p_1,p_0,y,p_m,p_{m-1}) is a tight Hamilton path on five distinct vertices, while for m=2 the sequence (p_1,p_0,y,p_m) is a tight Hamilton path on four distinct vertices. The support is proper, and minimum-counterexample calculus makes its complement non-Hamiltonian with path-cover number two. If (p_0,y,p_m) is not tight, boundary antisymmetry yields (p_m,y,p_0) tight.

Finally every tight path in a minimum counterexample leaves at least four vertices. Since x is one exterior vertex, at least three further exterior vertices satisfy the displayed three-triple pattern whenever the bounded frontier and small-support alternatives are absent. The terminal-end statement follows by the corresponding end-exchanged argument, without reversing the displayed path.
