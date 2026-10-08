# Double-hole endpoint certificates force cross-tail five-supports — preserved pre-item development

## Development

## Double-hole endpoint certificates synchronize across the two tails

Let
\[
Y\mid P\mid Q
\]
be a spanning three-cover with \(|Y|=5\), where \(Y\) contains two distinguished labels \(x,y\), and let
\[
N=Y-\{x,y\},\qquad |N|=3.
\]
Assume both \(P\) and \(Q\) have order at least six, and that the rooted five-component analysis is in the non-transfer branch for the endpoint tests under consideration.

Apply [[rooted_five_components_synchronize_through_a_nonhole_or_double_hole_endpoint]] to \(Y\) against each tail. Suppose neither tail gives the hole-preserving common-core alternative. Then for each tail there is a selected endpoint,
\[
e_P\in\{\text{the two displayed endpoints of }P\},\qquad
e_Q\in\{\text{the two displayed endpoints of }Q\},
\]
such that both hole deletions are good:
\[
(Y-\{x\})\cup\{e_P\},\quad (Y-\{y\})\cup\{e_P\}
\]
are Hamiltonian, and likewise
\[
(Y-\{x\})\cup\{e_Q\},\quad (Y-\{y\})\cup\{e_Q\}
\]
are Hamiltonian.

Thus the two four-sets
\[
C_x=Y-\{x\},\qquad C_y=Y-\{y\}
\]
are simultaneous common endpoint cores for the pair \(\{e_P,e_Q\}\):
\[
C_x+e_P,\ C_x+e_Q,\ C_y+e_P,\ C_y+e_Q
\]
are all Hamiltonian.

Now fix \(z\in\{x,y\}\) and put
\[
S_z=C_z\cup\{e_P,e_Q\},
\qquad |S_z|=6.
\]
If \(H[S_z]\) is Hamiltonian, then the two selected tail endpoints and the four-core already lie in one bounded Hamiltonian support.

Otherwise apply the four-of-six theorem to \(S_z\). The two deletions
\[
S_z-\{e_P\}=C_z+e_Q,\qquad
S_z-\{e_Q\}=C_z+e_P
\]
are already Hamiltonian. At least four of the six vertex-deleted five-sets are Hamiltonian, so at least two further Hamiltonian deletions remove vertices of \(C_z\). Hence there exist at least two distinct
\[
r\in C_z
\]
for which
\[
\boxed{(C_z-\{r\})\cup\{e_P,e_Q\}\text{ is Hamiltonian}.}
\]

Therefore:

> **Cross-tail synchronization theorem.** If both tails of a rooted five-component fall into the double-hole endpoint branch, then for each hole-deleted four-core \(C_x,C_y\), either \(C_z+\{e_P,e_Q\}\) is Hamiltonian or at least two of its four three-vertex subcores extend with both selected tail endpoints to Hamiltonian five-supports.

This produces a bounded support simultaneously spanning the two complementary tails. In particular, the double-hole alternative cannot remain as two unrelated one-tail certificates: it automatically yields a cross-tail five/six-support interface on at most six labels.

For the genuine two-deletion five-component state, this is the natural next input for endpoint handoff. A successful repartition using one of these cross-tail supports consumes one endpoint from each inherited tail at once; failure can now be analyzed by the existing prescribed-endpoint and order-disagreement lemmas on a six-label support rather than by separate long-tail arguments.
