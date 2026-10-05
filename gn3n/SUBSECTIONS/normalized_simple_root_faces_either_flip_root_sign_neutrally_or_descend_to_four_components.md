# Normalized simple-root faces either flip root sign neutrally or descend to four-components

## Metadata

- ID: normalized_simple_root_faces_either_flip_root_sign_neutrally_or_descend_to_four_components
- Parent Section: article_vii_synthesis_and_exact_frontier
- Position: 59
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## A normalized simple-root minimum-hole face either flips root sign neutrally or descends to a four-component

Let \(X\) be a minimum two-cover deletion set of order \(k\), and choose a \(\Psi\)-minimal complementary two-cover
\[
H-X=P\mid Q,
\qquad
P=(p_1,\ldots,p_r),\quad Q=(q_1,\ldots,q_{r+1}),
\]
so the normalized minimum-hole face has adjacent simple exact root
\[
\psi=e_{r-1}-e_r.
\]

Consider the two endpoint extensions
\[
H[P\cup\{q_1\}],
\qquad
H[P\cup\{q_{r+1}\}].
\]

### Case 1: a long-side endpoint extends the short side

Suppose \(P\cup\{q\}\) is Hamiltonian for some
\[
q\in\{q_1,q_{r+1}\}.
\]
Deleting that endpoint from the displayed path \(Q\) leaves an inherited Hamiltonian path. Hence
\[
(P\cup\{q\})\mid(Q-\{q\})
\]
is another two-cover of \(H-X\), now with component orders
\[
(r+1)\mid r.
\]
Its quadratic potential is unchanged:
\[
(r+1)^2+r^2=r^2+(r+1)^2.
\]
Thus it is a neutral one-vertex repartition.

For the associated free-hole concatenation face, minimum-hole exactness gives the new root
\[
e_r-e_{r-1}=-\psi.
\]
Therefore a single legal neutral endpoint transfer reverses the adjacent simple exact root.

### Case 2: both endpoint extensions are non-Hamiltonian

Assume
\[
P\cup\{q_1\},
\qquad
P\cup\{q_{r+1}\}
\]
are both non-Hamiltonian. Since prepending or appending either endpoint to the displayed order of \(P\) would then give a Hamiltonian extension, all such endpoint attachments fail. Boundary antisymmetry gives, for
\[
q\in\{q_1,q_{r+1}\},
\]
the two reversal relations
\[
h(p_2,p_1,q)=1,
\qquad
h(q,p_r,p_{r-1})=1.
\]

Use the fixed pair
\[
T=\{p_1,p_r\}.
\]
Partition the two long-side endpoints by their orientation through \(T\):
\[
\theta(q)=h(p_1,q,p_r)\in\{0,1\}.
\]

If
\[
\theta(q_1)=\theta(q_{r+1}),
\]
the fixed-pair Hamiltonicity theorem gives
\[
\boxed{\{p_1,p_r,q_1,q_{r+1}\}\text{ Hamiltonian}.}
\]
Removing these four endpoints leaves the inherited tight paths
\[
(p_2,\ldots,p_{r-1}),
\qquad
(q_2,\ldots,q_r).
\]
Hence \(H-X\) has a spanning three-cover with an all-old Hamiltonian four-component.

If instead
\[
\theta(q_1)\ne\theta(q_{r+1}),
\]
then every hole label \(x\in X\) belongs to exactly one of the two orientation classes through \(T\). Let \(q(x)\in\{q_1,q_{r+1}\}\) be the endpoint with the same class as \(x\). The fixed-pair theorem gives
\[
\boxed{\{p_1,p_r,q(x),x\}\text{ Hamiltonian}.}
\]
Put
\[
G_x=H-(X-\{x\}).
\]
Minimum-hole heredity gives
\[
\kappa_2(G_x)=k-1.
\]
Moreover \(G_x\) has a spanning three-cover whose distinguished four-component is the displayed Hamiltonian set, while the other two components are the inherited interiors of \(P\) and \(Q-q(x)\).

Thus:

> **Simple-root sign-flip/four-component dichotomy.** A \(\Psi\)-normalized minimum-hole face with adjacent simple exact root either admits a neutral one-vertex repartition reversing the root sign, or it descends to a bounded Hamiltonian four-component, either already in \(H-X\) or in a canonical one-hole restoration of deletion distance \(k-1\).

Consequently the unbounded rank-one exact-root branch has only one genuinely new behavior beyond the bounded four-component interface: neutral transport between the two opposite adjacent simple roots.
