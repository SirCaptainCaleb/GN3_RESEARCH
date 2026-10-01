# Cheap outside packets force a low-degree survivor

## Statement

Let H be a vertex-minimal counterexample to the strengthened equality-layer assertion S_ell at density d=floor(2ell/3), and let O be the vertices outside a fixed nonspecial witness path. If a nonempty packet S⊆O satisfies |N(S)|<=d|S|, then H-S still has density at least d and retains the nonspecial witness, so H-S contains a vertex of degree at most d. No Hall-type packet expansion follows without an additional minimum-degree-preservation or lift-back argument.

## Body

Fix ell>=4 and d=floor(2ell/3). Let H be a vertex-minimal counterexample to the strengthened equality-layer assertion S_ell: H is P_ell-free, |E(H)|>=d|V(H)|, H contains a nonspecial edge, and H has no vertex of degree at most d.

Fix a longest witness path P ending in a nonspecial edge e, and let O be the set of vertices outside V(P).

For S subseteq O, let N(S) be the set of hyperedges meeting S. Suppose S is nonempty and
  |N(S)|<=d|S|.

Because S is disjoint from V(P), the path P survives in H-S. Deleting vertices cannot create a longer e-ending path; since P survives with its old length and entrance, the rank and unique entrance of e are unchanged. Thus e remains nonspecial in H-S.

Also
  |E(H-S)|
   =|E(H)|-|N(S)|
   >=d|V(H)|-d|S|
   =d|V(H-S)|.

Hence H-S satisfies the hypotheses of S_ell. It is smaller than H, so by vertex-minimality it is not a counterexample to S_ell. Therefore H-S contains a vertex u with
  d_{H-S}(u)<=d.

Thus every nonempty witness-avoiding packet S with |N(S)|<=d|S| necessarily exposes a low-degree survivor after deletion.

This is the correct packet-deletion conclusion. It does not imply
  |N(S)|>=d|S|+1
for every S, and therefore does not by itself yield the previously claimed Hall assignment of d incidence-disjoint edges per outside vertex. For singleton S={w}, the stronger lift-back conclusion of a7bc010274c9 applies under its hypotheses: the survivor has degree d+1 in H and is joined to w by a unique hyperedge.