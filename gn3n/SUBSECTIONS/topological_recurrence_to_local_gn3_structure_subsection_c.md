# Exact-deficiency sharpening: the one-hole four-support handoff

## Metadata

- ID: topological_recurrence_to_local_gn3_structure_subsection_c
- Parent Section: topological_recurrence_to_local_gn3_structure
- Position: 3
- Row version: 3
- Development version: 3
- Composition version: 1
- Composition stale: False

## Cold composition


### Exact deficiency one in a minimum counterexample

The exact inversion coordinates from [[spanning_orders_and_defect_helly]] sharpen the minimum-span conclusion further. For a spanning order \(\pi\), write
\[
p(\pi)=\min\{i:\epsilon_i=0\},\qquad
q(\pi)=\max\{i:\epsilon_i=1\},
\]
and
\[
\delta(\pi)=q(\pi)-p(\pi)-1.
\]
By the exact inversion-window criterion,
\[
\operatorname{pc}(H)\le2
\iff
\exists\pi\text{ with }\delta(\pi)\le0.
\]
Thus every spanning order of a counterexample has \(\delta\ge1\).

**Theorem 7.9 (minimum exact deficiency is one).** Let \(H\) be a minimum counterexample to the two-cover conjecture. Then
\[
\min_\pi\delta(\pi)=1.
\]
More precisely, for every \(x\in V(H)\) and every displayed two-cover
\[
H-x=P\mid Q
\]
with \(P=(p_1,\ldots,p_r)\) and \(Q=(q_1,\ldots,q_s)\), the spanning order
\[
\pi=(p_1,\ldots,p_r,x,q_s,\ldots,q_1)
\]
has \(\delta(\pi)=1\).

**Proof.** First \(r,s\ge3\). Indeed, if one deletion-cover component had order at most two, adjoining \(x\) would give a set of order at most three, hence a Hamiltonian tight path; together with the other displayed component this would two-cover \(H\).

In \(\pi\), every status wholly inside \(P\) is \(1\), while every status wholly inside \(Q^{\rm rev}\) is \(0\). Hence only the three junction statuses
\[
(p_{r-1},p_r,x),\qquad
(p_r,x,q_s),\qquad
(x,q_s,q_{s-1})
\]
can interrupt the pattern \(1^*0^*\). Consequently
\[
p(\pi)\ge r-1,\qquad q(\pi)\le r+1,
\]
so
\[
\delta(\pi)=q(\pi)-p(\pi)-1\le1.
\]
Since \(H\) is a counterexample, the exact inversion-window criterion gives \(\delta(\pi)\ge1\). Therefore \(\delta(\pi)=1\). \(\square\)

Equality forces
\[
p(\pi)=r-1,\qquad q(\pi)=r+1.
\]
Thus the first and third junction statuses are forced:
\[
(p_{r-1},p_r,x)\text{ is non-tight},
\qquad
(x,q_s,q_{s-1})\text{ is tight}.
\]
By boundary reversal,
\[
(x,p_r,p_{r-1})
\]
is tight as well. Hence the omitted vertex \(x\) reverses the displayed terminal edge of each deletion path:
\[
(x,p_r,p_{r-1}),\qquad
(x,q_s,q_{s-1})
\quad\text{are tight}.
\]

This is exactly the deficiency-one instance of the canonical partial-cover construction in [[convex_root_balance_and_bourgin_yang]]: the exact root carries a two-path cover with one missing vertex, and the missing vertex controls both exposed terminal edges.

### The exact geodesic handoff is a four-support

The preceding double reversal has an immediate bounded consequence.

**Corollary 7.10 (canonical four-support from exact deficiency one).** Let \(H\) be a minimum counterexample. For every deletion cover
\[
H-x=P\mid Q,
\]
the terminal edges of \(P\) and \(Q\), together with \(x\), contain a Hamiltonian four-support. Its complement is non-Hamiltonian and has path-cover number exactly two.

**Proof.** Write the terminal edges of the displayed tight paths as
\[
\ldots,a_0,a_1,
\qquad
\ldots,b_0,b_1.
\]
Theorem 7.9 gives
\[
(x,a_1,a_0),\qquad(x,b_1,b_0)
\]
tight. Exactly one of
\[
(a_1,x,b_1),\qquad(b_1,x,a_1)
\]
is tight. In the first case
\[
(a_1,x,b_1,b_0)
\]
is a tight Hamiltonian four-path; in the second,
\[
(b_1,x,a_1,a_0)
\]
is.

Let \(K\) be this four-set. It is proper, since otherwise \(H\) itself would be Hamiltonian. By minimality, \(H-K\) has path-cover number at most two. It cannot be Hamiltonian, because a Hamilton path on \(H-K\) together with the displayed Hamilton path on \(K\) would two-cover \(H\). Hence
\[
\operatorname{pc}(H-K)=2
\]
and \(H-K\) is non-Hamiltonian. \(\square\)

This sharpens the minimum-counterexample endpoint of the geodesic investigation. The width-three switch-span formulation remains useful for arbitrary counterexamples and for the recurrent-face compression, but after minimum-counterexample induction the exact inversion coordinate removes the mixed-end ambiguity entirely:
\[
\boxed{
\text{minimum counterexample}
\Longrightarrow
\text{canonical Hamiltonian four-support with non-Hamiltonian two-coverable complement}.
}
\]

Thus no synchronization of an entire directed root cycle is needed to finish Article VII's own task. The exact-root coordinate already reaches the bounded local interface. What remains after this point is the local four-support/path-cover analysis, not an antipodal-geodesic obstruction.


## Development


### Exact deficiency one in a minimum counterexample

The exact inversion coordinates from [[spanning_orders_and_defect_helly]] sharpen the minimum-span conclusion further. For a spanning order \(\pi\), write
\[
p(\pi)=\min\{i:\epsilon_i=0\},\qquad
q(\pi)=\max\{i:\epsilon_i=1\},
\]
and
\[
\delta(\pi)=q(\pi)-p(\pi)-1.
\]
By the exact inversion-window criterion,
\[
\operatorname{pc}(H)\le2
\iff
\exists\pi\text{ with }\delta(\pi)\le0.
\]
Thus every spanning order of a counterexample has \(\delta\ge1\).

**Theorem 7.9 (minimum exact deficiency is one).** Let \(H\) be a minimum counterexample to the two-cover conjecture. Then
\[
\min_\pi\delta(\pi)=1.
\]
More precisely, for every \(x\in V(H)\) and every displayed two-cover
\[
H-x=P\mid Q
\]
with \(P=(p_1,\ldots,p_r)\) and \(Q=(q_1,\ldots,q_s)\), the spanning order
\[
\pi=(p_1,\ldots,p_r,x,q_s,\ldots,q_1)
\]
has \(\delta(\pi)=1\).

**Proof.** First \(r,s\ge3\). Indeed, if one deletion-cover component had order at most two, adjoining \(x\) would give a set of order at most three, hence a Hamiltonian tight path; together with the other displayed component this would two-cover \(H\).

In \(\pi\), every status wholly inside \(P\) is \(1\), while every status wholly inside \(Q^{\rm rev}\) is \(0\). Hence only the three junction statuses
\[
(p_{r-1},p_r,x),\qquad
(p_r,x,q_s),\qquad
(x,q_s,q_{s-1})
\]
can interrupt the pattern \(1^*0^*\). Consequently
\[
p(\pi)\ge r-1,\qquad q(\pi)\le r+1,
\]
so
\[
\delta(\pi)=q(\pi)-p(\pi)-1\le1.
\]
Since \(H\) is a counterexample, the exact inversion-window criterion gives \(\delta(\pi)\ge1\). Therefore \(\delta(\pi)=1\). \(\square\)

Equality forces
\[
p(\pi)=r-1,\qquad q(\pi)=r+1.
\]
Thus the first and third junction statuses are forced:
\[
(p_{r-1},p_r,x)\text{ is non-tight},
\qquad
(x,q_s,q_{s-1})\text{ is tight}.
\]
By boundary reversal,
\[
(x,p_r,p_{r-1})
\]
is tight as well. Hence the omitted vertex \(x\) reverses the displayed terminal edge of each deletion path:
\[
(x,p_r,p_{r-1}),\qquad
(x,q_s,q_{s-1})
\quad\text{are tight}.
\]

This is exactly the deficiency-one instance of the canonical partial-cover construction in [[convex_root_balance_and_bourgin_yang]]: the exact root carries a two-path cover with one missing vertex, and the missing vertex controls both exposed terminal edges.

### The exact geodesic handoff is a four-support

The preceding double reversal has an immediate bounded consequence.

**Corollary 7.10 (canonical four-support from exact deficiency one).** Let \(H\) be a minimum counterexample. For every deletion cover
\[
H-x=P\mid Q,
\]
the terminal edges of \(P\) and \(Q\), together with \(x\), contain a Hamiltonian four-support. Its complement is non-Hamiltonian and has path-cover number exactly two.

**Proof.** Write the terminal edges of the displayed tight paths as
\[
\ldots,a_0,a_1,
\qquad
\ldots,b_0,b_1.
\]
Theorem 7.9 gives
\[
(x,a_1,a_0),\qquad(x,b_1,b_0)
\]
tight. Exactly one of
\[
(a_1,x,b_1),\qquad(b_1,x,a_1)
\]
is tight. In the first case
\[
(a_1,x,b_1,b_0)
\]
is a tight Hamiltonian four-path; in the second,
\[
(b_1,x,a_1,a_0)
\]
is.

Let \(K\) be this four-set. It is proper, since otherwise \(H\) itself would be Hamiltonian. By minimality, \(H-K\) has path-cover number at most two. It cannot be Hamiltonian, because a Hamilton path on \(H-K\) together with the displayed Hamilton path on \(K\) would two-cover \(H\). Hence
\[
\operatorname{pc}(H-K)=2
\]
and \(H-K\) is non-Hamiltonian. \(\square\)

This sharpens the minimum-counterexample endpoint of the geodesic investigation. The width-three switch-span formulation remains useful for arbitrary counterexamples and for the recurrent-face compression, but after minimum-counterexample induction the exact inversion coordinate removes the mixed-end ambiguity entirely:
\[
\boxed{
\text{minimum counterexample}
\Longrightarrow
\text{canonical Hamiltonian four-support with non-Hamiltonian two-coverable complement}.
}
\]

Thus no synchronization of an entire directed root cycle is needed to finish Article VII's own task. The exact-root coordinate already reaches the bounded local interface. What remains after this point is the local four-support/path-cover analysis, not an antipodal-geodesic obstruction.
