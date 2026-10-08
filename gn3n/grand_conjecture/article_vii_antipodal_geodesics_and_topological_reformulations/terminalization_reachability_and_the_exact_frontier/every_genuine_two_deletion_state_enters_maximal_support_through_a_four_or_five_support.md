# Every genuine two-deletion state enters maximal support through a four- or five-support

## Composition

(none yet)

## Development

## Every genuine two-deletion state has a four- or five-support with two-coverable complement

Let
\[
X=\{x,y\}
\]
be a minimum two-cover deletion pair and fix
\[
H-X=P\mid Q,
\qquad
P=(p_1,\ldots,p_s),\quad Q=(q_1,\ldots,q_t),
\]
with \(s,t\ge2\).

Put
\[
K=\{p_1,q_1,x,y\}.
\]

If \(H[K]\) is Hamiltonian, then its complement is covered by the two inherited paths
\[
(p_2,\ldots,p_s)\mid(q_2,\ldots,q_t).
\]
Hence \(K\) is already a Hamiltonian four-support with two-coverable complement.

Assume instead that \(H[K]\) is non-Hamiltonian. Add the next vertex \(p_2\) and put
\[
U=K\cup\{p_2\}.
\]

There are again two cases.

### Case 1: \(U\) is Hamiltonian

Then \(U\) is a Hamiltonian five-support, while
\[
H-U
\]
is covered by
\[
(p_3,\ldots,p_s)\mid(q_2,\ldots,q_t),
\]
with the usual convention that an empty inherited interval is omitted. Thus the complement is two-coverable.

### Case 2: \(U\) is non-Hamiltonian

By Section 7 of [[smallset01]], a non-Hamiltonian five-set has at most one non-Hamiltonian four-subset. One four-subset of \(U\), namely
\[
U-\{p_2\}=K,
\]
is already non-Hamiltonian. Therefore every other four-subset of \(U\) is Hamiltonian. In particular
\[
L=U-\{q_1\}=\{p_1,p_2,x,y\}
\]
is Hamiltonian.

Its complement is covered by
\[
(p_3,\ldots,p_s)\mid Q.
\]
Hence \(L\) is a Hamiltonian four-support with two-coverable complement.

We have proved:

> **Universal bounded-support entry theorem for \(\kappa_2=2\).** Every genuine minimum deletion pair together with any displayed complementary two-cover produces a Hamiltonian support of order four or five whose complement has path-cover number at most two.

No endpoint-signature hypothesis, same-signature pigeonhole, minimum-counterexample argument, or finite-order enumeration is used.

Since \(H\) itself has no two-cover in the genuine \(\kappa_2=2\) state, the displayed support cannot have Hamiltonian complement; hence its complement has path-cover number exactly two. Therefore the hypotheses of [[maximal_support_normalization_applies_directly_to_article_vii_bounded_outputs]] always hold.

### Consequence for Article VII

The earlier split into same-signature versus doubly endpoint-bad minimum pairs is unnecessary for the purpose of entering maximal-support theory. Every genuine two-deletion state canonically reaches that theory from one endpoint neighborhood on at most five labels.

Thus the combinatorial terminalization frontier can be reformulated globally:

\[
\boxed{
\kappa_2(H)=2
\Longrightarrow
\text{there exists a maximal Hamiltonian support }S
\text{ with }pc(H-S)=2,
}
\]
with the endpoint noninsertability, size inequalities, and sandwich-reversal conclusions already proved in [[maximal_support_normalization_applies_directly_to_article_vii_bounded_outputs]].

The six-label antipodal-signature routing analysis remains useful for protected/carrier compatibility, but it is no longer needed merely to obtain a bounded Hamiltonian support with two-coverable complement.
