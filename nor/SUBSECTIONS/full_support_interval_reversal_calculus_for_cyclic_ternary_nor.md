# Full-support interval reversal calculus for cyclic ternary NOR

## Metadata

- ID: full_support_interval_reversal_calculus_for_cyclic_ternary_nor
- Parent Section: higher_memory_norine_geodesics
- Position: 50
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Full-support interval reversal calculus for cyclic ternary NOR

Work in the directed translation-invariant sector of \(N_4\):
\[
h(a,b,c)\in\{0,1\},\qquad h(c,b,a)=1-h(a,b,c).
\]

Let
\[
C=(v_0,v_1,\ldots,v_{n-1})
\]
be a cyclic ordering, indices taken modulo \(n\), and put
\[
c_i=h(v_i,v_{i+1},v_{i+2}),\qquad d_i=c_i\oplus c_{i+1}.
\]
Thus \(q(C)=\sum_i d_i\) is the cyclic variation.

Choose a proper cyclic interval
\[
R=(v_a,v_{a+1},\ldots,v_b)
\]
containing at least three vertices and leaving at least two vertices outside it. Let \(C^R\) be the cyclic order obtained by reversing exactly this vertex interval and keeping every vertex of the ambient ground set.

### Lemma 1: internal change bits are preserved

Every ternary status window lying wholly inside \(R\) is sent to the reverse of an old status window. Hence, if
\[
I_j=h(v_j,v_{j+1},v_{j+2})
\]
is internal to \(R\), the corresponding new status is
\[
1-I_j.
\]
The internal status string is therefore reversed and complemented.

Consequently every transition bit between two consecutive windows wholly inside \(R\) is preserved, in reverse order:
\[
(1-I_{j+1})\oplus(1-I_j)=I_j\oplus I_{j+1}.
\]
All transition bits whose two adjacent windows lie wholly outside \(R\) are unchanged as well.

Thus an interval reversal cannot alter the cyclic variation in the interior of the reversed interval or in the untouched exterior. All change in \(q\) is confined to the two reconnection zones.

### Lemma 2: explicit boundary data

Write the local cyclic order as
\[
\ldots,p,a,x_1,x_2,\ldots,x_m,b,q,\ldots
\]
with \(R=(x_1,\ldots,x_m)\), \(m\ge3\). Before reversal, the four boundary statuses are
\[
h(p,a,x_1),\quad h(a,x_1,x_2),\quad
h(x_{m-1},x_m,b),\quad h(x_m,b,q).
\]
After reversal they become
\[
h(p,a,x_m),\quad h(a,x_m,x_{m-1}),\quad
h(x_2,x_1,b),\quad h(x_1,b,q).
\]
Every other changed status is an internal status of \(R\), hence belongs to the reversed-complemented block from Lemma 1.

Equivalently, the difference \(q(C^R)-q(C)\) is determined entirely by the six transition bits incident with these two pairs of boundary statuses. No proper subset of the ambient vertex set is introduced.

### Corollary 3: extremal cycles satisfy every interval-reversal inequality

If \(C\) has minimum cyclic variation among all cyclic coordinate orders on the same ground set, then for every proper interval \(R\),
\[
q(C^R)\ge q(C).
\]
By Lemma 1 this is a purely boundary inequality: the six new boundary transition bits contribute at least as much total variation as the six old boundary transition bits.

In particular, for a minimum directed-\(N_4\) counterexample, Section 20 supplies a cyclic order with \(q(C)=4\). That order is globally variation-minimal, so every full-support interval reversal satisfies the boundary non-improvement inequality.

### Why this is the right repair framework

The recent failed tail-propagation arguments truncated a deletion tail and then imported endpoint blocking from the full counterexample. Interval reversal avoids that defect completely: it is a permutation of the full ambient set. Therefore counterexamplehood and the global lower bound \(q\ge4\) apply after every such move.

The four-change profile from a deletion order has cyclic run lengths
\[
1,p,q,2
\]
up to rotation. Closure at ternary arity can therefore be attacked by choosing reversals whose endpoints straddle selected run boundaries and showing that the resulting boundary inequality cannot hold simultaneously for all choices.

This note does not assert that the resulting inequality system is already inconsistent. Its contribution is to replace truncation by a full-support move with an invariant interior and a finite boundary obligation.

## Frontier

- Development version when composed: None
- Development version now: 1
