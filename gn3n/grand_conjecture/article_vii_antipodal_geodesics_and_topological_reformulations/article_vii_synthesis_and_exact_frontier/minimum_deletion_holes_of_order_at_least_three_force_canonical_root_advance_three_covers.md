# Minimum deletion holes of order at least three force canonical root-advance three-covers

## Composition

### A good pair in every large minimum hole

Let \(X\) be a minimum deletion set of order at least three and \(H-X=P\mid Q\). By four-end synchronization, every label of \(X\) reverses the exposed initial edges of both \(P\) and \(Q\). Applying the one-step root-advance lemma to any three labels gives a pair \(x,y\in X\) for which the induced graph obtained by restoring \(x,y\) contains a rooted Hamiltonian five-path crossing the two exposed roots. This is the only conclusion used here; no recursive three-cover lift is assumed.

## Development

## Elevation of minimum-hole synchronization by the three-reverser lemma

Let
\[
X\subseteq V(H),\qquad |X|=k=\kappa_2(H),
\]
be a minimum two-cover deletion set, and let
\[
H-X=P\mid Q
\]
be a two-cover. Orient the two displayed paths from their exposed hole-facing endpoints outward:
\[
P=(p_1,p_2,\ldots),\qquad Q=(q_1,q_2,\ldots).
\]

By [[topological_recurrence_to_local_gn3_structure_subsection_d]], every hole vertex
\[
x\in X
\]
is a common reverser of the same two exposed path edges:
\[
h(p_2,p_1,x)=h(q_2,q_1,x)=1.
\]

Assume
\[
k\ge3
\]
and choose any three distinct hole vertices
\[
x_1,x_2,x_3\in X.
\]
They satisfy the hypotheses of [[three_common_initial_reversers_force_a_root_advancing_five_path]]. Hence two of them, say \(x_i,x_j\), produce a tight five-path of one of the forms
\[
(p_2,p_1,x_i,q_1,x_j),\qquad
(p_2,p_1,x_j,q_1,x_i),
\]
or the symmetric forms rooted at \(q_2\).

Thus:

> **Minimum-hole root-advance lemma.** Every three-element subset of a minimum deletion hole contains a pair which, together with the two exposed corridor roots, forms a root-advancing tight five-path.

Equivalently, define a graph \(G_X\) on \(X\) by joining \(x,y\) whenever the pair occurs in one of these root-advancing five-paths. Then
\[
\boxed{\alpha(G_X)\le2.}
\]

This is stronger than the older pointwise four-support conclusion: it couples distinct hole vertices and moves one corridor root through the opposite component.

### Three-cover consequence

Fix a good pair \(x,y\in X\), and suppose for definiteness that
\[
R=(p_2,p_1,x,q_1,y)
\]
is tight. Delete the remaining hole vertices
\[
X-\{x,y\}.
\]
The surviving graph has the explicit three-path cover
\[
R
\ \mid\
(p_3,p_4,\ldots)
\ \mid\
(q_2,q_3,\ldots),
\]
with the evident omission of an empty tail.

Therefore
\[
\boxed{\kappa_3(H)\le k-2}
\]
in the sense that deletion of \(k-2\) vertices leaves a three-cover, and that three-cover contains a distinguished five-component coupled to both old two-cover components.

This does not yet contradict minimality of \(k=\kappa_2(H)\), because the three displayed paths need not merge to two. But it imports the entire Article VI / pairwise-repartition toolkit into the symmetric zero-root branch: whenever \(k\ge3\), minimum-hole synchronization automatically creates a five-component beside the two inherited tails.

The natural next elevation is therefore to apply the established five-side-versus-long-path repartition lemmas to this canonical three-cover, rather than attack the zero-root hole as an arbitrary set.
