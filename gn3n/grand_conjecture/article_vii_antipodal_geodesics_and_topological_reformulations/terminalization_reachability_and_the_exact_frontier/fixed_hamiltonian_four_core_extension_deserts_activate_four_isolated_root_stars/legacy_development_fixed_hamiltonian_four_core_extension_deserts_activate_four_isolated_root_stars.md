# Fixed Hamiltonian four-core extension deserts activate four isolated-root stars — preserved pre-item development

## Composition

(none yet)

## Development

## A fixed Hamiltonian four-core extension desert activates four isolated-root stars

Let \(A\) be a Hamiltonian four-set in a boundary tournament \(H\), and let
\[
Y\subseteq V(H)-A
\]
satisfy
\[
H[A\cup\{y\}]\text{ is non-Hamiltonian}
\qquad(y\in Y).
\]

For each \(x\in A\), put
\[
D_x=A-\{x\},
\]
and define
\[
Y_x=\{y\in Y:H[D_x\cup\{y\}]\text{ is Hamiltonian}\}.
\]

### Three-of-four incidence

For every \(y\in Y\),
\[
|\{x\in A:y\in Y_x\}|\ge3.
\]

Proof. The five-set \(A+y\) is non-Hamiltonian. The audited small-set theorem says a non-Hamiltonian five-set has at most one non-Hamiltonian four-subset. Its four subsets
\[
D_x+y,\qquad x\in A,
\]
therefore include at least three Hamiltonian ones. \(\square\)

Consequently
\[
\sum_{x\in A}|Y_x|\ge3|Y|.
\]
In particular one \(Y_x\) has order at least \(3|Y|/4\), and some pair \(x,x'\) satisfies
\[
|Y_x\cap Y_{x'}|\ge |Y|/2,
\]
because each exterior label belongs to at least three of the four \(Y_x\)'s and hence contributes to at least three of the six pairwise intersections.

### Each \(Y_x\) is exactly an isolated-root extension star

Fix \(x\in A\). Then

- \(D_x+x=A\) is Hamiltonian;
- \(D_x+y\) is Hamiltonian for every \(y\in Y_x\);
- \(D_x+x+y=A+y\) is non-Hamiltonian for every \(y\in Y_x\).

Therefore [[isolated_root_extension_stars_synchronize_to_one_core_endpoint_or_disturb]] applies directly.

For every \(x\in A\), one obtains:

1. an order-disagreement certificate; or
2. a positioned reversal; or
3. a Hamiltonian four-support on an internal core edge with \(x\) and some \(y\); or
4. a quiet synchronized branch in which \(x\) and every \(y\in Y_x\) insert into the same endpoint gap of one Hamilton order of \(D_x\).

In the quiet branch, [[synchronized_isolated_roots_force_complete_fixed_pair_four_and_five_supports]] strengthens this further: there is an endpoint
\[
d_x\in D_x
\]
such that for every distinct
\[
y,z\in Y_x,
\]
the four-set
\[
\{d_x,x,y,z\}
\]
is Hamiltonian.

### Consequence

A fixed Hamiltonian \(K_4\) with a large family of bad one-vertex extensions is therefore not a featureless extension desert. Either the late reversal/order machinery fires immediately, or the exterior labels organize into up to four highly overlapping root families, each supporting a complete graph of Hamiltonian four-sets through one fixed core pair.

Since every exterior label belongs to at least three root families, the quiet residue has dense overlap between these fixed-pair Hamiltonian-support systems. This supplies exactly the kind of mixed support-pair filling data that is invisible if one records only whether \(A+y\) itself is Hamiltonian.

This is an upstream reuse of the late isolated-root theory at the rank-four support-carrier frontier.
