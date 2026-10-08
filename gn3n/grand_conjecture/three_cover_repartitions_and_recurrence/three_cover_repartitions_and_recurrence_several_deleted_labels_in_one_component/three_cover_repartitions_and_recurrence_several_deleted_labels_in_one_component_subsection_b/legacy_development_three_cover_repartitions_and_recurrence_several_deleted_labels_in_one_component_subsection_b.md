# Support-graph shadow of neutral recurrence — preserved pre-item development

## Development

### Compatibility cycles project to the support graph

Fix one selected deletion cover (F_d) for each label (d), and let (J) be the selected support graph. Let (K) be the graph on labels in which (ab) is an edge when (F_a,F_b) are compatible.

**Lemma 6 (line-graph shadow).** If (abin E(K)), then the selected support edges (e_a,e_bin E(J)) share a support vertex. Consequently
[
Ksubseteq L(J),
]
after identifying each label (d) with its selected support edge (e_d).

**Proof.** Compatibility of (F_a,F_b) gives two common ordered supports (P,Q) on
[
H-{a,b}.
]
By the insertion-slot lemma, the restored vertices (a,b) are inserted into the same common support, say (P). Hence
[
F_a=(P+b)mid Q,
qquad
F_b=(P+a)mid Q.
]
Thus the selected support edges
[
e_a=(P+b)Q,
qquad
e_b=(P+a)Q
]
are both incident with the exact support (Q). (square)

This makes closed neutral recurrence globally rigid.

**Corollary 7 (recurrence-cycle routing).** Let
[
d_0d_1cdots d_{m-1}d_0
]
be a simple cycle in the compatibility graph (K).

1. If (J) is a forest, then all selected edges
   [
   e_{d_0},ldots,e_{d_{m-1}}
   ]
   are incident with one common support (Q). Hence the deletion covers on the cycle are pairwise support-compatible.

   If (mge4), then either (H) has a two-cover or two of these covers have an order disagreement on their common domain. In the latter case the path-order disagreement machinery yields a tight triple reversing an edge of a displayed path.

   Thus a forest recurrence cycle not already returning to a reversal or two-cover has length exactly three.

2. If (J) is the spanning odd cycle from the support-graph dichotomy, then any simple cycle in (Ksubseteq L(J)) is the whole line graph (L(J)), which is again that same odd cycle. Hence a closed neutral recurrence in this case is not a new residue: it is exactly the global odd-cycle support geometry of Article I.

**Proof.** Suppose first that (J) is a forest. The line graph of a forest is a block graph: every simple cycle lies inside the clique formed by the edges incident with one vertex of the forest. Lemma 6 therefore gives one support (Q) incident with every selected edge on the recurrence cycle.

Write
[
X=V(H)-Q.
]
Since (e_{d_i}) is incident with (Q) and omits exactly (d_i), its other endpoint is necessarily
[
X-{d_i}.
]
Thus
[
F_{d_i}=(X-{d_i})mid Q
]
for every (i), so the family is pairwise support-compatible.

If (mge4) and the covers are pairwise compatible, compatibility gluing gives a two-cover of (H). Otherwise some pair is support-compatible but not compatible, so their common-support orders disagree. The reversal-from-order-disagreement theorem then gives a displayed-edge reversal.

Now suppose (J) is the spanning odd cycle. Its line graph is another cycle of the same odd length, and a proper subgraph of a cycle contains no simple cycle. Therefore any simple cycle of (Ksubseteq L(J)) must use every edge of (L(J)). (square)

Hence indefinite neutral omission-swap recurrence has only two genuine global destinations:

- a three-cover compatibility triangle around one support vertex in the forest case;
- the spanning odd-cycle support geometry.

Every longer forest recurrence already yields a two-cover or a fresh reversal. Neutral omission swaps therefore do not create an unrestricted new state space.
