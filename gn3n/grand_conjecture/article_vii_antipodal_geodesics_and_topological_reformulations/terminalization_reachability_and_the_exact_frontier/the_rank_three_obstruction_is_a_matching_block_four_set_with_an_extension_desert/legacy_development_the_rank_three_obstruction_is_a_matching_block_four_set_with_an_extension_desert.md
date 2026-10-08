# The rank-three obstruction is a matching-block four-set with an extension desert — preserved pre-item development

## The rank-three obstruction is a matching-block four-set with an exterior extension desert

Continue in the exceptional branch of [[rank_three_support_pair_carriers_reduce_to_one_extreme_non_hamiltonian_four_block]].

Thus a rank-three permutahedron face has one extreme block
\[
W,\qquad |W|=4,
\]
with \(H[W]\) non-Hamiltonian, while the opposite common support
\[
B_F\neq\varnothing
\]
survives.

### 1. Any usable Hamiltonian five-extension kills the carrier obstruction

If \(z\notin W\) satisfies
\[
H[W\cup\{z\}]\text{ Hamiltonian}
\]
and
\[
B_F-\{z\}\neq\varnothing,
\]
choose \(b\in B_F-\{z\}\). Then
\[
(W\cup\{z\},\{b\})\in\widehat{\mathcal P}(H).
\]
The singleton-allowed carrier may transfer \(z\) from the opposite side if necessary and retain \(b\) as the opposite support. Hence the exceptional face is coned after this mixed-support enlargement.

Therefore a genuine obstruction requires
\[
\boxed{
H[W\cup\{z\}]\text{ non-Hamiltonian for every }z\notin W
\text{ with }B_F-\{z\}\neq\varnothing.
}
\]
In particular, if \(|B_F|\ge2\), every \(z\notin W\) is required to be a bad five-extension.

### 2. The four-block must be edge-orderable of matching-block type

The audited small-set theorem says that the cyclic non-Hamiltonian four-vertex configuration is Hamilton-extended by every fifth vertex. Hence the extension-desert branch cannot use that configuration.

Consequently \(H[W]\) is represented by an edge order on \(K_W\), and its three opposite-edge perfect matchings occur as strict blocks
\[
M_{\rm low}<M_{\rm mid}<M_{\rm high}.
\]

Thus the first possible support-pair obstruction is not an arbitrary non-Hamiltonian four-set: it is a matching-block \(K_4\).

### 3. Every bad exterior label has the matching-block extension signature

Let \(d\notin W\) be one of the required bad five-extensions. The small-set extension theorem gives:

- at least one edge of \(M_{\rm high}\) is outgoing from \(d\);
- no edge of \(M_{\rm high}\) is incoming to \(d\);
- at least one edge of \(M_{\rm low}\) is incoming to \(d\);
- no edge of \(M_{\rm low}\) is outgoing from \(d\);
- after choosing an incident high/low normalization, the two middle matching edges have opposite directions relative to \(d\).

So every exterior label in a genuine rank-three desert carries a rigid finite matching-block boundary signature.

### 4. Two bad exterior labels already have a six-label dichotomy

Let \(a,b\notin W\) be distinct labels whose five-extensions
\[
W+a,\qquad W+b
\]
are both non-Hamiltonian. The established two-bad-extension theorem gives:

either

1. the full six-set
   \[
   W\cup\{a,b\}
   \]
   is edge-orderable;

or

2. it contains a Hamiltonian support \(R\) with
   \[
   \{a,b\}\subseteq R\subseteq W\cup\{a,b\},
   \qquad 4\le |R|\le6.
   \]

Thus failure of the direct five-extension cone does not return to arbitrary endpoint surgery. It immediately enters one of two structured support-pair branches: a mixed Hamiltonian support through both exterior labels, or a common edge-order representation of the whole six-label packet.

### 5. A stronger two-exterior forcing condition

In the matching-block normalization, if distinct exterior vertices \(u,v\) satisfy
\[
h(x,u,v)=h(u,v,x)=1
\qquad\text{for every }x\in W,
\]
then the small-set theorem forces either \(W+u\) or \(W+u+v\) to be Hamiltonian. In the desert branch \(W+u\) is forbidden, so
\[
\boxed{W\cup\{u,v\}\text{ is Hamiltonian}.}
\]

Hence a genuine rank-three obstruction must also forbid every exterior ordered pair having this uniform two-sided relation to the four-block.

### Strategic consequence

The first unresolved higher carrier is therefore completely localized to:

- one matching-block edge-ordered \(K_4\);
- a family of exterior vertices all giving non-Hamiltonian five-extensions;
- their forced low/middle/high matching signatures;
- and six-label packets which must either remain globally edge-orderable or create mixed Hamiltonian supports.

This is the correct place to reuse the late six-shadow and extension machinery. The remaining task is no longer to analyze arbitrary permutahedron three-cells, but to show that this matching-block extension desert cannot carry the required relative equivariant obstruction in a minimum counterexample.
