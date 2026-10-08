# Audit: fixed-hole singleton-unanimity facets are automatic — preserved pre-item development

## Development

## Audit: the fixed-hole sparse-face alternative is automatic

Retain the fixed-hole Ky Fan notation. For a chamber
\[
\pi=(v_1,\ldots,v_n)
\]
with status word \(\epsilon_1,\ldots,\epsilon_{n-2}\), let
\[
p(\pi)=\min\{i:\epsilon_i=0\},\qquad
q(\pi)=\max\{i:\epsilon_i=1\}.
\]
The canonical partial two-cover uses the initial tight prefix through position \(p+1\) as its left support and the terminal reverse-tight suffix beginning at position \(q+1\) as its right support. Thus every vertex in position \(1\) or \(2\) is canonically left, and every vertex in position \(n\) is canonically right.

Let \(H\) be any counterexample, and fix any vertex \(x\). Consider the permutahedral facet
\[
F_x=\{x\}\mid(V(H)-\{x\}),
\]
whose chambers are precisely the spanning orders with \(x\) fixed in the first position and all other vertices freely permuted afterward.

For every chamber of \(F_x\), the vertex \(x\) lies in position \(1\), hence in the canonical left support. Therefore
\[
x\in A(F_x).
\]

Now let \(y\ne x\). Because the second block is freely permuted, there is a chamber of \(F_x\) with \(y\) in position \(2\), so \(y\) is canonically left in that chamber. There is also a chamber with \(y\) in position \(n\), so \(y\) is canonically right in that chamber. Consequently \(y\) is neither unanimously left nor unanimously right on \(F_x\). Hence
\[
A(F_x)\cup C(F_x)=\{x\}.
\]

Therefore:

> **Audit conclusion.** For every vertex \(x\) of every counterexample, the facet
> \[
> \{x\}\mid(V-x)
> \]
> is already a singleton-unanimity facet.

So the sparse-face alternative in [[fixed_hole_ky_fan_forces_every_balanced_deletion_state]] is automatic as currently stated. In particular, [[minimum_counterexamples_have_singleton_unanimity_facets_or_an_unanimity_free_face]] does not impose a new restriction on minimum counterexamples: its singleton-unanimity-facet branch is always available independently of the universal fixed-hole branch.

The Johnson-layer elimination of the universal branch remains correct **conditional on entering that branch**, but it cannot be used to conclude new structure from the fixed-hole Ky Fan dichotomy unless the sparse alternative is strengthened.

A nontrivial replacement must exclude these automatic extreme-position facets, for example by requiring additional carrier geometry, a lower bound on free-block size/dimension, or a sparse face whose unanimity defect is not explained solely by fixing the hole label at an extreme position.
