# Terminal-pair completion rank is closure-circular as stated

## Statement

The terminal-pair completion rank conjecture ba48cdda95aa is circular as a route to the grand two-cover theorem. Any feasible witness counted by R(u,v)—a set S supporting a tight path and a Hamiltonian complement V(H)-S—already is a spanning two-cover of H. Therefore in any counterexample to the grand theorem every R(u,v) has an empty feasible set (equivalently rank zero/undefined under any natural convention), so there is no nontrivial rank distribution to exploit before the theorem is already proved.

## Body

# Proof

By definition, a feasible witness for R(u,v) is a vertex set S containing u,v such that

1. H[S] has a tight path P ending in (u,v); and
2. H[V(H)-S] is Hamiltonian.

Let Q be a Hamilton path on V(H)-S.

The paths P and Q are vertex-disjoint, and their vertex sets partition V(H). Therefore

P | Q

is a spanning path cover of H with at most two tight paths.

Thus the existence of even one feasible witness for any ordered pair (u,v) is already the conclusion of the grand two-cover conjecture for H.

Consequently, if H is a counterexample to the grand theorem, no ordered pair admits any feasible witness. Hence every R(u,v) is undefined, or equals the chosen default bottom value if one is imposed. In particular there are no positive ranks to orient, compare, or count.

So a theorem bounding equal-rank in-neighborhoods cannot bootstrap toward the first positive rank: positivity itself is exactly the desired two-cover.

A noncircular replacement would have to relax the complement condition—for example requiring the complement merely to have path-cover number two, bounded deficit, or another near-Hamiltonian certificate—so that the rank is defined nontrivially inside a hypothetical counterexample.