# The memory lift and exact antipodal geodesics

**Summary:** The stronger one-change spanning-order problem becomes a genuine one-change antipodal geodesic problem after adding two-step memory.

## Statement

A fixed ranked antipodal memory-lift graph has pole geodesics exactly equal to spanning orders, with edge colors equal to the consecutive-triple status word; geodesicity is exactly the no-coordinate-reuse condition.

## Cold composition

## The memory lift, antipodality, and zero detour


### The memory-lift graph

The staircase triangulation identifies spanning orders with cube geodesics, but the GN3 color at one step depends on three successive directions. Introduce a ranked graph \(\Gamma_n\) that stores precisely this missing memory.

Its vertices are poles \(s,t\) and states
\[
(\sigma,S,u,v),
\]
where \(\sigma\in\{0,1\}\), \(u\ne v\), and
\[
S\subseteq V\setminus\{u,v\}.
\]
Give such a state rank \(|S|+1\), with \(r(s)=0\) and \(r(t)=n\).

Join \(s\) to every state
\[
(\sigma,\varnothing,u,v).
\]
Join
\[
(\sigma,S,u,v)
\longrightarrow
(\sigma,S\cup\{u\},v,w)
\]
whenever
\[
w\notin S\cup\{u,v\},
\]
and join every rank-\((n-1)\) state to \(t\).

Color a source edge by \(\sigma\), an internal edge by
\[
h(u,v,w),
\]
and a terminal edge by \(1-\sigma\).

The underlying graph depends only on \(n\). The boundary tournament enters only through the internal edge colors.

### Antipodal involution and cube projection

Define
\[
A(s)=t,\qquad A(t)=s,
\]
and
\[
A(\sigma,S,u,v)
=
\bigl(
\sigma,\,
V\setminus(S\cup\{u,v\}),\,
v,u
\bigr).
\]
This is fixed-point-free.

An internal edge carrying \(u,v,w\), when mapped by \(A\) and read in increasing-rank direction, carries \(w,v,u\). Hence its color is complemented by
\[
h(w,v,u)=1-h(u,v,w).
\]
Source and terminal colors are also complementary.

There is an antipodal projection to the cube,
\[
p(s)=\varnothing,\qquad
p(t)=V,\qquad
p(\sigma,S,u,v)=S\cup\{u\}.
\]
Every edge projects to a cube edge and
\[
p(Ax)=V\setminus p(x).
\]

Thus \(\Gamma_n\) is a finite two-step-memory lift of the cube.

### Pole geodesics are spanning orders

Every edge changes rank by one, so
\[
d(s,t)\ge n.
\]
Given
\[
\pi=(v_1,\ldots,v_n)
\]
and \(\sigma\in\{0,1\}\), there is a length-\(n\) path
\[
s,\,
(\sigma,S_0,v_1,v_2),\,
(\sigma,S_1,v_2,v_3),\ldots,t,
\]
with the obvious indexing
\[
S_i=\{v_1,\ldots,v_i\}.
\]

Conversely, every \(s\)-\(t\) geodesic must increase rank at every step, so it chooses each label exactly once and therefore determines a unique permutation and copy index.

Hence pole geodesics are in bijection with pairs \((\sigma,\pi)\), and their color words are
\[
\sigma,\,
h(v_1,v_2,v_3),\ldots,
h(v_{n-2},v_{n-1},v_n),\,
1-\sigma.
\]

Therefore a spanning order whose internal word changes color at most once is exactly a pole geodesic with at most one internal change after choosing the appropriate copy.

### Geodesicity is the no-reuse condition

The strengthened Norine analogy becomes exact at this point.

For an arbitrary \(s\)-\(t\) walk \(W\), let \(m_v\) be the number of projected cube edges using coordinate \(v\). Since the projection joins antipodal cube vertices, every \(m_v\) is odd. Thus
\[
|W|
=
\sum_{v\in V}m_v
=
n+
2\sum_{v\in V}\frac{m_v-1}{2}.
\]

Consequently
\[
\boxed{
W\text{ is geodesic}
\iff
m_v=1\text{ for every }v.
}
\]

Zero detour is exactly the requirement that each original vertex, or each cube dimension, be used once.

This is the sharp distinction between the desired theorem and a generic antipodal-path theorem. A one-change antipodal walk that repeats a coordinate does not encode a spanning order. A theorem whose antipodal endpoints are allowed to vary likewise does not solve the distinguished-pole problem.

The topology must preserve simultaneously:

1. the prescribed poles;
2. geodesicity;
3. the two-step memory carried by the state.

### The stronger problem represented exactly

The memory lift gives an exact graph formulation of the stronger one-change spanning-order target:

\[
\boxed{
H\text{ has a one-change spanning order}
\iff
\Gamma_n(H)\text{ has a one-change pole geodesic}.
}
\]

This equivalence is useful but must not be confused with the original two-cover conjecture. A two-cover need not itself appear as a one-change spanning order of \(H\).

That distinction is the point at which the next Section begins.

> **Transition.** The memory lift makes one-change spanning orders into genuine one-change antipodal geodesics, but on \(H\) this remains potentially stronger than the two-cover conjecture. We now remove that discrepancy.


## Metadata

- ID: memory_lift_and_exact_antipodal_geodesics
- Kind: section
- Version: 3
- Math version: 2
- Audit: unaudited
- Refutation: unrefuted
- Composition version: 1
- Composition stale: False

## Development tree

- [Subsection 1 — The memory lift, antipodality, and zero detour](../SUBSECTIONS/memory_lift_and_exact_antipodal_geodesics_subsection_a.md) (`memory_lift_and_exact_antipodal_geodesics_subsection_a`; development v3; composition v1; stale=False)
- [Subsection 2 — Further developments](../SUBSECTIONS/memory_lift_and_exact_antipodal_geodesics_subsection_b.md) (`memory_lift_and_exact_antipodal_geodesics_subsection_b`; development v1; composition vNone; stale=True)
