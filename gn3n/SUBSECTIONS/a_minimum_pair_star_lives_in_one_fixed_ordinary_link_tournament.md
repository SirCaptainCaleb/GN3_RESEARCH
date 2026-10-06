# A minimum-pair star lives in one fixed ordinary link tournament

## Metadata

- ID: a_minimum_pair_star_lives_in_one_fixed_ordinary_link_tournament
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 237
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## The fixed-hole link tournament applies simultaneously to an entire minimum-pair star

Let \(H\) satisfy
\[
\kappa_2(H)=2,
\]
and let \(M\) be the minimum-pair graph
\[
xy\in E(M)
\quad\Longleftrightarrow\quad
H-\{x,y\}\text{ has a two-cover}.
\]

Fix one vertex \(x\in V(H)\). Define the ordinary link tournament
\[
T_x
\]
on \(V(H)-\{x\}\) by
\[
u\to_x v
\quad\Longleftrightarrow\quad
h(u,x,v)=1.
\]

Then the deletion-distance-one link-tournament theorem applies **simultaneously to every edge \(xy\) of \(M\) incident with \(x\)**, using this same tournament \(T_x\).

### Proof

Fix
\[
y\in N_M(x).
\]
Put
\[
J=H-y.
\]
Because \(xy\in E(M)\),
\[
J-x=H-\{x,y\}
\]
has a two-cover, so
\[
\kappa_2(J)\le1.
\]
But \(J\) itself cannot have a two-cover: otherwise deleting the single vertex \(y\) from \(H\) would produce a two-cover, contradicting
\[
\kappa_2(H)=2.
\]
Hence
\[
\boxed{\kappa_2(J)=1,}
\]
with \(x\) a valid one-hole deletion label.

Choose any displayed deletion cover
\[
H-\{x,y\}=P_y\mid Q_y,
\]
where
\[
P_y=(p_1,\ldots,p_r),
\qquad
Q_y=(q_1,\ldots,q_s).
\]
Let
\[
L_y=\{p_1,q_1\},
\qquad
R_y=\{p_r,q_s\}.
\]

Apply [[fixed_hole_reverse_rectangles_are_cuts_in_an_ordinary_link_tournament]] to the boundary tournament \(J=H-y\), with fixed hole \(x\). Exactly one of the useful alternatives occurs:

1. some
   \[
   a\in L_y,\qquad b\in R_y
   \]
   satisfy
   \[
   h(a,x,b)=1,
   \]
   and the four-end reversal relations produce the corresponding rooted five-path through \(x\); or

2. every cross orientation is blocked:
   \[
   h(a,x,b)=0
   \qquad
   (a\in L_y,\ b\in R_y),
   \]
   equivalently
   \[
   \boxed{R_y\to_x L_y}
   \]
   is a complete directed \(2\)-by-\(2\) cut.

The link tournament used inside \(J\) is just the restriction of the global \(T_x\) to
\[
V(H)-\{x,y\}.
\]
Therefore varying \(y\) does **not** vary the ambient ordinary tournament.

Hence:

> **Minimum-pair star compression.** For fixed \(x\), every incident minimum-pair edge \(xy\) either produces a rooted five-support through \(x\), or determines a complete directed endpoint cut
> \[
> R_y\to_x L_y
> \]
> in one fixed ordinary tournament \(T_x\).

### Strategic significance

This moves the link-tournament abstraction strictly earlier in the proof line.

Previously the fixed-hole theorem was treated as a tool for the \(\kappa_2=1\) frontier after the two-deletion problem had somehow been solved. But every edge of the \(\kappa_2=2\) minimum-pair graph already *becomes* a \(\kappa_2=1\) state after deleting its other endpoint. Thus the theorem applies edgewise before the \(\kappa_2=2\) branch is closed.

More importantly, it removes the main nuisance of dissimilar deletion covers around a common hole. Their support partitions and Hamilton orders may be unrelated, but their hard endpoint data are all represented as directed cuts in the same ordinary tournament \(T_x\).

This suggests a new closure target for the first Smith extension:
- rooted-five alternatives feed the existing mixed-support/seed machinery;
- otherwise the star \(N_M(x)\) gives a family of near-balanced complete \(2\)-by-\(2\) cuts in \(T_x\);
- the task is to show that such a family cannot realize the top-rank Smith obstruction without either producing a deficiency-one support pair or a mixed support-pair filling.

The minimum-pair graph should therefore be studied together with the family of fixed tournaments \(\{T_x\}\), rather than through pairwise comparison of deletion-cover orders.

## Frontier

- Development version when composed: None
- Development version now: 1
