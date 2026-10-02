# Spanning top-rank induction works after one vertex deletion in two residue classes

## Statement

Assume the dense-core all-special conjecture is true for forbidden length ell-1. Let H be a P_ell-free linear 3-graph on exactly 2ell-1 vertices with
  delta(H)>=k_ell:=floor(2ell/3)+1.
Then for every vertex w,
  H-w
is automatically P_{ell-1}-free and has minimum degree at least k_ell-1=floor(2ell/3).

If ell is congruent to 0 or 2 modulo 3, then
  floor(2ell/3) >= floor(2(ell-1)/3)+1,
so H-w lies above the dense-core threshold for ell-1. Consequently every edge of H-w is special.

If ell is congruent to 1 modulo 3, this implication misses by exactly one:
  floor(2ell/3)=floor(2(ell-1)/3),
whereas the strict ell-1 threshold is one larger.

Thus, under induction, a spanning top-rank counterexample can only retain genuinely nontrivial deletion structure in the residue class ell≡1 mod 3; in the other two residue classes every single-vertex deletion is all-special.

## Body

A linear (ell-1)-edge 3-uniform path uses 2(ell-1)+1=2ell-1 vertices. The graph H-w has only 2ell-2 vertices, so it is P_{ell-1}-free.

Deleting one vertex from a linear hypergraph removes at most one incident edge at any surviving vertex: two distinct edges containing both w and a surviving vertex u would violate linearity. Therefore
delta(H-w)>=delta(H)-1>=floor(2ell/3).

Now compare with the strict threshold for ell-1, namely
floor(2(ell-1)/3)+1.

Write ell modulo three.

If ell=3m, then floor(2ell/3)=2m and floor(2(ell-1)/3)+1=floor((6m-2)/3)+1=(2m-1)+1=2m.

If ell=3m+2, then floor(2ell/3)=2m+1 and floor(2(ell-1)/3)+1=floor((6m+2)/3)+1=2m+1.

If ell=3m+1, then floor(2ell/3)=2m while floor(2(ell-1)/3)+1=2m+1.

The claimed induction consequence follows.