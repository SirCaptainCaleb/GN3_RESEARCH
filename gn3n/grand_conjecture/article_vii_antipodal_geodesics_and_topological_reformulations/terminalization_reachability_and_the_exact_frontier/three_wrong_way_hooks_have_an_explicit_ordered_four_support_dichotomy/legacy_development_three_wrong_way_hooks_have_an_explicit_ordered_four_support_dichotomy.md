# Three wrong-way hooks have an explicit ordered four-support dichotomy — preserved pre-item development

## Development

## Three wrong-way hooks have an explicit ordered four-support dichotomy

Let \(x,y,t_1,t_2,t_3\) be distinct vertices and assume
\[
h(y,x,t_i)=1
\qquad(i=1,2,3).
\]
These are exactly the three wrong-way hooks arising when direct rooted corridor absorption through the interface pair \((x,y)\) fails.

Then one of the following holds.

### 1. Anchor-starting four-path

For some ordered pair \(i\ne j\),
\[
h(x,t_i,t_j)=1.
\]
Then
\[
(y,x,t_i,t_j)
\]
is a tight Hamiltonian four-path on
\[
\{y,x,t_i,t_j\},
\]
because its two consecutive triples are
\[
h(y,x,t_i)=1,
\qquad
h(x,t_i,t_j)=1.
\]
In particular the anchor pair \(y,x\) occurs in the prescribed order as the initial edge of the Hamilton path.

### 2. Hook-only four-support with \(x\) penultimate

Assume instead that
\[
h(x,t_i,t_j)=0
\qquad
\text{for every ordered pair }i\ne j.
\]
Boundary antisymmetry gives
\[
h(t_j,t_i,x)=1
\qquad(i\ne j).
\]
Fix \(t_1\). In particular
\[
h(t_1,t_2,x)=1,
\qquad
h(t_1,t_3,x)=1.
\]
Thus \(t_2,t_3\) are two parallel middle vertices between the fixed endpoints \(t_1,x\). By the two-parallel-middle lemma, one of
\[
(t_1,t_2,x,t_3),
\qquad
(t_1,t_3,x,t_2)
\]
is a tight Hamiltonian four-path on
\[
\{x,t_1,t_2,t_3\}.
\]
Hence \(x\) is penultimate in an explicit Hamilton order on the hook-only four-support.

Therefore:

> **Ordered three-hook dichotomy.** Three wrong-way hooks through one ordered anchor pair force either a Hamiltonian four-path beginning with the anchor pair \(y,x\), or a Hamiltonian four-path on \(x,t_1,t_2,t_3\) with \(x\) in the penultimate position.

No cyclic rotation, path reversal, edge-order representation, or minimum-counterexample hypothesis is used.

### Relevance to the rooted corridor frontier

In [[rooted_corridor_absorption_reduces_to_a_bounded_three_hook_residue]], the support-level conclusion was insufficient because the orientation of the Hamilton packet was uncontrolled. The present dichotomy supplies explicit orientations in both branches.

It does not by itself complete absorption: the direct splice wants a packet path ending at the shared interface vertex \(x\), whereas branch 1 starts with \(y,x\) and branch 2 places \(x\) penultimate. The remaining problem is therefore strictly narrower: convert one of these two ordered four-support forms into a repartition of the six-vertex endpoint packet, or show that failure of that repartition yields a protected outward move.
