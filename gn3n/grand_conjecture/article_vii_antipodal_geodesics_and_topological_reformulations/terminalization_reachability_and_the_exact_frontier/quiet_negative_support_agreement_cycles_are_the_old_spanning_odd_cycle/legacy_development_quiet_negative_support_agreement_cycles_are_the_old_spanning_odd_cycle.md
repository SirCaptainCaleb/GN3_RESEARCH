# Quiet negative support agreement cycles are the old spanning odd cycle — preserved pre-item development

## Development

## A quiet negative support-agreement cycle is exactly the old spanning odd-cycle support geometry

Let \(H\) be a minimum counterexample and choose one deletion cover
\[
F_x
\]
for every vertex \(x\). Let \(G\) be the support-agreement graph of
[[two_connected_support_agreement_closes_except_for_a_negatively_signed_spanning_cycle]].

Assume \(G\) is the exceptional case: a spanning cycle
\[
x_0x_1\cdots x_{n-1}x_0
\]
whose support-identification signs
\[
\varepsilon_i\in\{\pm1\}
\]
have product
\[
\prod_i\varepsilon_i=-1.
\]

Suppose first that some adjacent pair \(F_{x_i},F_{x_{i+1}}\) has an order disagreement on a common support. Then the established order-disagreement theorem gives an external reversing triple, so we are already in the reversal interface.

Assume therefore that every adjacent pair is compatible, including support orders.

For one agreement edge \(x_ix_{i+1}\), let
\[
U\mid W
\]
be the common ordered support partition on
\[
H-\{x_i,x_{i+1}\}.
\]
The insertion-slot theorem for compatible deletion covers says that the two omitted labels are inserted into the same common support. Hence, after a local naming of the two parts,
\[
F_{x_i}=(U\cup\{x_{i+1}\})\mid W,
\qquad
F_{x_{i+1}}=(U\cup\{x_i\})\mid W.
\]
In particular the two deletion covers have the same unordered support-size multiset.

Choose signed names of the two supports around the cycle as in the signed-agreement theorem, and let
\[
d_i=|F_{x_i}^{+}|-|F_{x_i}^{-}|.
\]
Across the edge \(x_ix_{i+1}\), compatibility and same-side insertion give
\[
\boxed{d_{i+1}=\varepsilon_i d_i.}
\]
Multiplying around the spanning cycle yields
\[
d_0
=
\left(\prod_i\varepsilon_i\right)d_0
=
-d_0.
\]
Therefore
\[
\boxed{d_i=0\quad\text{for every }i.}
\]
Thus every selected deletion cover is exactly balanced, and consequently
\[
n-1
\]
is even, so \(n\) is odd.

Now consider the selected support graph \(J\) of Article I: its edge \(e_i\), labeled \(x_i\), joins the two actual supports of \(F_{x_i}\).

Because adjacent covers are compatible with same-side insertion, \(F_{x_i}\) and \(F_{x_{i+1}}\) share the unchanged support \(W_i\) exactly. Hence the selected edges
\[
e_i,\ e_{i+1}
\]
share a support vertex of \(J\).

No support vertex of \(J\) can lie on two nonconsecutive selected edges \(e_i,e_j\). If it did, the two deletion covers would share that support exactly; after removing the two omitted labels, their other supports are the common complement, so their support partitions would agree. This would make \(x_ix_j\) an edge of the support-agreement graph \(G\), a chord of the assumed cycle.

Therefore the \(n\) selected edges themselves form a simple cycle in \(J\). Since there is exactly one selected edge for each of the \(n\) deletion labels, there are no further selected edges. Hence
\[
\boxed{J\text{ is exactly the spanning }n\text{-cycle}.}
\]
Because \(n\) is odd, this is precisely the spanning odd-cycle support geometry already treated in
[[deletion_covers_and_the_support_graph_the_odd_cycle_case]].

Consequently:

> **Negative-cycle synthesis.** A negatively signed spanning support-agreement cycle either contains an adjacent order disagreement, hence an external reversal, or its quiet compatible branch is exactly the old spanning odd-cycle support graph with balanced deletion covers.

Thus the signed support-agreement theorem introduces no new global terminal geometry beyond the established reversal/bounded-support interfaces of Article I.
