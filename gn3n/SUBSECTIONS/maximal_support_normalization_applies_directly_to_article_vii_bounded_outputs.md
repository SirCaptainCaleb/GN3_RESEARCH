# Maximal-support normalization applies directly to Article VII bounded outputs

## Metadata

- ID: maximal_support_normalization_applies_directly_to_article_vii_bounded_outputs
- Parent Section: article_vii_synthesis_and_exact_frontier
- Position: 61
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Maximal-support normalization is valid once a two-coverable complement is known

Let \(H\) be a boundary tournament with no spanning two-cover. Suppose there exists a proper Hamiltonian support \(S_0\subsetneq V(H)\) such that \(H-S_0\) has a two-cover. This hypothesis is supplied in several Article VII bounded-output branches, including the same-signature central four-support branch.

Among all proper Hamiltonian supports \(S\) whose complement is two-coverable, choose one of maximum cardinality. Fix a Hamilton order
\[
S=(s_1,\ldots,s_k)
\]
and a two-cover
\[
H-S=P\mid Q,
\qquad
P=(p_1,\ldots,p_m),\quad Q=(q_1,\ldots,q_t).
\]

Because \(H\) itself has no two-cover, \(H-S\) is not Hamiltonian; hence both displayed components are nonempty.

### Every displayed complementary endpoint reverses both ends of \(S\)

Let \(z\) be any displayed endpoint of \(P\) or \(Q\). If \(S\cup\{z\}\) were Hamiltonian, deleting \(z\) from its displayed complementary path would leave a two-cover of
\[
H-(S\cup\{z\}).
\]
The support \(S\cup\{z\}\) is proper because the other complementary component is nonempty. This contradicts maximality of \(|S|\).

Therefore
\[
H[S\cup\{z\}]
\]
is non-Hamiltonian. By the endpoint-replacement/truncation dichotomy, \(z\) is noninsertable at every position of the displayed Hamilton order of \(S\). In particular
\[
h(z,s_1,s_2)=0,
\qquad
h(s_{k-1},s_k,z)=0.
\]
Boundary antisymmetry gives
\[
\boxed{
h(s_2,s_1,z)=1,
\qquad
h(z,s_k,s_{k-1})=1.
}
\]
Thus all four exposed endpoints of \(P\mid Q\) (when the two paths have order at least two) are simultaneous double reversers of the same Hamiltonian support \(S\).

No minimum-counterexample induction is used.

### Three-way size bound

The displayed paths \(P\) and \(Q\) are themselves admissible Hamiltonian supports with two-coverable complements:
\[
H-P=S\mid Q,
\qquad
H-Q=S\mid P.
\]
Therefore maximality of \(S\) gives
\[
\boxed{m\le k,\qquad t\le k.}
\]
Consequently
\[
|V(H)|=k+m+t\le3k,
\qquad
k\ge\left\lceil\frac{|V(H)|}{3}\right\rceil.
\]

### Sandwich-splice thresholds require only maximality

Consider \(P\). Every consecutive triple in
\[
(s_2,s_1,p_1,\ldots,p_m,s_k,s_{k-1})
\]
is known tight except possibly
\[
(s_1,p_1,p_2),
\qquad
(p_{m-1},p_m,s_k).
\]
If both are tight, the displayed sequence is a Hamilton path on a support of order \(m+4\), and its complement is covered by
\[
(s_3,\ldots,s_{k-2})\mid Q.
\]
Hence, whenever
\[
m+4>k,
\]
maximality forbids both junctions from being tight. Therefore at least one boundary flip occurs:
\[
\boxed{
h(p_2,p_1,s_1)=1
\quad\text{or}\quad
h(s_k,p_m,p_{m-1})=1.
}
\]

More sharply, if
\[
m+2>k,
\]
then both flips occur. Indeed, if \(h(s_1,p_1,p_2)=1\), then
\[
(s_2,s_1,p_1,\ldots,p_m)
\]
is a Hamilton support of order \(m+2>k\) whose complement is covered by
\[
(s_3,\ldots,s_k)\mid Q,
\]
contradicting maximality. Thus
\[
h(p_2,p_1,s_1)=1.
\]
The other end is symmetric:
\[
h(s_k,p_m,p_{m-1})=1.
\]

The same statements hold for \(Q\).

Hence if either complementary path has order at least \(k-1\), both endpoints of \(S\) reverse the two end edges of that path, while the endpoints of that path already reverse both end edges of \(S\). This creates a mutual four-end reversal rectangle between two large Hamiltonian supports.

### Article VII consequence

Once a genuine two-deletion or minimum-hole branch produces any Hamiltonian four- or five-support with a two-coverable complement, one may replace that local support by the maximal \(S\) above. The residual problem is no longer arbitrary rerooting: it is a three-path state
\[
S\mid P\mid Q
\]
with
\[
|P|,|Q|\le|S|,
\]
all complementary endpoints reversing both ends of \(S\), and any complementary path within one vertex of \(|S|\) mutually reversed at both ends by \(S\).

This imports the useful part of the Article IV maximal-support/sandwich machinery into Article VII without invoking the prohibited unbounded minimum-counterexample calculus.
