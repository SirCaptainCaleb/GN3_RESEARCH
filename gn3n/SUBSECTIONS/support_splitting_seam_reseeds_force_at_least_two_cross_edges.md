# Support-splitting seam reseeds force at least two cross edges

## Metadata

- ID: support_splitting_seam_reseeds_force_at_least_two_cross_edges
- Parent Section: article_vii_synthesis_and_exact_frontier
- Position: 117
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## A support-splitting seam reseed has at least two support-complement crossings

Let \(H\) be a no-two-cover boundary tournament, let
\[
S
\]
be a globally maximal Hamiltonian support with two-coverable complement, and let
\[
K\subseteq V(H)-S
\]
be a Hamiltonian seam four-support in the reseed branch. Fix a two-cover
\[
H-K=A\mid B.
\]

Assume this reseed is genuinely support-splitting:
\[
A\cap S\ne\varnothing,\qquad B\cap S\ne\varnothing.
\]

Put
\[
C=V(H)-(S\cup K).
\]
Because \(K\) arises from a displayed complementary two-cover of \(S\), the set \(C\) is covered by at most two inherited tight paths. If \(H[C]\) were Hamiltonian, then
\[
H-K=S\mid C
\]
would be a support-preserving reseed, contrary to the assumption that we are in the genuinely support-splitting branch. Therefore
\[
\boxed{\operatorname{pc}(H[C])=2.}
\]

Now view
\[
T=A\mid B
\]
as a two-path cover of \(H-K\) and cut every ordinary path edge of \(T\) having one endpoint in \(S\) and the other in \(C\). Let
\[
b_S(T),\qquad b_C(T)
\]
be the numbers of resulting nonempty blocks on the two sides.

Since both cover components \(A,B\) meet \(S\), at least one \(S\)-block lies in each component, so
\[
b_S(T)\ge2.
\]
Since those \(C\)-blocks form a path cover of \(H[C]\) and \(\operatorname{pc}(H[C])=2\),
\[
b_C(T)\ge2.
\]

The transition-count identity from [[coversurg01]] gives
\[
t_{S|C}(T)=b_S(T)+b_C(T)-2.
\]
Hence
\[
\boxed{t_{S|C}(A\mid B)\ge2.}
\]

Therefore:

> **Two-crossing theorem.** Every genuinely support-splitting seam reseed contains at least two ordinary path edges crossing between the old maximal support \(S\) and the residual complement \(C\).

In particular the remaining reseed branch is not a one-cut split of the old Hamilton path. It necessarily contains a genuine two-sided support-partition disturbance.

If equality
\[
t_{S|C}=2
\]
holds, then necessarily
\[
b_S=b_C=2.
\]
Thus each of the two reseed components contains exactly one \(S\)-block and exactly one \(C\)-block, joined by a single crossing edge. Any larger transition count is an even stronger block-interleaving disturbance.

This conclusion uses only the path-cover transition identity and the distinction between support-preserving and support-splitting reseeds; no path reversal, cyclic permutation, or minimum-counterexample induction is used.
