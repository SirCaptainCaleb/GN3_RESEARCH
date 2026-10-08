# Zero exit is exactly an endpoint-reversal certificate — preserved pre-item development

## Development

## Zero exit is exactly an endpoint-reversal certificate

Retain the separated terminal-pair enlargement model with fixed following labels
\[
z,z_1,z_2,\ldots
\]
and define the exit status of a movable label \(y\) by
\[
\delta(y)=h(y,z_1,z_2).
\]

Boundary antisymmetry gives
\[
h(y,z_1,z_2)+h(z_2,z_1,y)=1.
\]
Therefore
\[
\boxed{\delta(y)=0\iff h(z_2,z_1,y)=1.}
\]

Thus the zero-exit condition required by
[[a_four_cycle_has_an_exact_six_label_repair_classification_with_one_exterior_label]],
[[two_opposite_nonzero_exits_admit_independent_two_label_repair]], and
[[sequential_zero_exit_vertex_replacement_fills_protected_pair_cycles]]
has an exact combinatorial interpretation:

> a zero-exit repair label is precisely an exterior label reversing the oriented exit edge \(z_1z_2\).

No additional orientation convention is involved; this is the actual boundary flip and not a cyclic permutation.

### Consequence for maximal-support certificates

Let
\[
S=(s_1,\ldots,s_k)
\]
be a maximal Hamiltonian support with two-coverable complement. Every exposed endpoint \(e\) of the complementary two-cover satisfies
\[
h(s_2,s_1,e)=1.
\]
Hence if a protected carrier enlargement is positioned so that its exit edge is
\[
(z_1,z_2)=(s_1,s_2),
\]
then every exposed complementary endpoint has
\[
\delta(e)=h(e,s_1,s_2)=0.
\]

Likewise, at the opposite end, the maximal-support relation
\[
h(e,s_k,s_{k-1})=1
\]
says that \(e\) has zero exit for a carrier whose oriented exit edge is
\[
(z_1,z_2)=(s_{k-1},s_k).
\]

Thus maximal-support normalization automatically supplies up to four zero-exit candidate repair labels at either support end. The remaining condition in the protected-cycle repair problem is entirely the terminal-pair adjacency condition:
for a bad cycle vertex \(v\) with current neighbors \(\ell,r\), find one of these zero-exit candidates \(e\) mutually admissible before the following label \(z\) with
\[
\ell,\quad v,\quad r.
\]

This isolates the exact bridge theorem still missing between the combinatorial and topological interfaces: **three-neighbor mutual admissibility**, not exit control.
