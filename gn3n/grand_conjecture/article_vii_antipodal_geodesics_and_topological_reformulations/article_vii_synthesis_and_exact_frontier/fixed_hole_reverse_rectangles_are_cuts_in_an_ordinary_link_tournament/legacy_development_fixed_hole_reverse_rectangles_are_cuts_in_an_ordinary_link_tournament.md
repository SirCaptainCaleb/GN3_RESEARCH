# Fixed-hole reverse rectangles are cuts in an ordinary link tournament — preserved pre-item development

## Development

## The fixed-hole opposite-boundary obstruction is an ordinary link-tournament cut

Fix a vertex \(x\) of a boundary tournament \(H\). Define a directed graph \(T_x\) on
\[
V(H)-\{x\}
\]
by
\[
u\to_x v
\quad\Longleftrightarrow\quad
h(u,x,v)=1.
\]

Boundary antisymmetry gives
\[
h(u,x,v)+h(v,x,u)=1
\]
for every distinct \(u,v\ne x\). Hence exactly one of
\[
u\to_x v,\qquad v\to_x u
\]
holds. Therefore \(T_x\) is an ordinary tournament.

Now assume
\[
\kappa_2(H)=1,\qquad \operatorname{pc}(H)>2,
\]
and let
\[
H-x=P\mid Q,
\]
where
\[
P=(p_1,\ldots,p_r),\qquad Q=(q_1,\ldots,q_s).
\]
Put
\[
L=\{p_1,q_1\},\qquad R=\{p_r,q_s\}.
\]

By [[deletion_distance_one_has_root_advance_or_a_complete_reverse_rectangle]], exactly one of the following holds.

1. Some \(a\in L,b\in R\) satisfy
   \[
   h(a,x,b)=1,
   \]
   equivalently
   \[
   a\to_x b.
   \]
   Then four-end reversal produces the tight rooted five-path
   \[
   (a',a,x,b,b').
   \]

2. Every cross status is zero:
   \[
   h(a,x,b)=0
   \qquad(a\in L,b\in R).
   \]
   Equivalently every edge of the link tournament between \(L\) and \(R\) is oriented
   \[
   \boxed{R\to_x L.}
   \]

Thus:

> **Link-tournament endpoint-cut theorem.** For a fixed hole \(x\), every deletion cover \(P\mid Q\) either produces an opposite-boundary rooted five-path, or its two terminal endpoints completely dominate its two initial endpoints in the ordinary tournament \(T_x\).

### Ky Fan consequence

In the alternating-cover branch of [[kappa_one_role_balance_and_ky_fan]], some fixed vertex \(x\) is the hole in exponentially many balanced deletion states
\[
(x;\{P,Q\}).
\]

If none of those states yields the rooted-five-path alternative, then the same fixed ordinary tournament \(T_x\) must realize, for every one of those balanced states, a complete directed \(2\)-by-\(2\) endpoint cut
\[
\{p_r,q_s\}\to_x\{p_1,q_1\}.
\]

Hence the fixed-hole extremal target can be sharpened: one seeks an upper bound on complementary balanced Hamiltonian bipartitions whose chosen Hamilton orders have terminal endpoint pair completely dominating the initial endpoint pair in one fixed link tournament.

The hypergraph dependence on the hole has therefore been compressed into an ordinary tournament on \(n-1\) vertices.
