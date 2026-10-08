# Minimum balanced holes have a rank-one extension obstruction — preserved pre-item development

## Development

## Minimum balanced holes have a rank-one extension obstruction

Let H be a boundary 3-tournament with no spanning two-cover. Let
\[
H-X=P\mid Q,\qquad |P|=|Q|=r,
\]
be a balanced deletion cover with |X| minimum among all balanced deletion covers of H. No assumption that X is a minimum two-cover deletion set is made.

Define the support-extension incidence graph \(\Gamma_X\) with left class \(X\) and right class \(\{P,Q\}\):
\[
x\sim P \iff H[P\cup\{x\}]\text{ is Hamiltonian},
\qquad
x\sim Q \iff H[Q\cup\{x\}]\text{ is Hamiltonian}.
\]

### Theorem
\(\Gamma_X\) has matching number at most one.

Indeed, if distinct \(x,y\in X\) satisfy
\[
H[P\cup\{x\}]\text{ Hamiltonian},
\qquad
H[Q\cup\{y\}]\text{ Hamiltonian},
\]
then the two supports are disjoint and
\[
(P\cup\{x\})\sqcup(Q\cup\{y\})
=V(H)-(X-\{x,y\}).
\]
Both have order \(r+1\), so they give a balanced deletion cover with hole \(X-\{x,y\}\), contradicting the minimality of |X|. The same argument applies with P,Q interchanged. QED.

Since the right class has two vertices, the obstruction has an exact classification. Either

1. all extension edges are incident with only one of the two supports; or
2. there is a unique hole label z and every extension edge is incident with z.

Equivalently, if both supports admit an extension by hole labels, then
\[
L=\{x\in X:H[P\cup\{x\}]\text{ is Hamiltonian}\},\qquad
R=\{x\in X:H[Q\cup\{x\}]\text{ is Hamiltonian}\}
\]
satisfy \(L=R=\{z\}\), unless one of L,R is empty.

### Ordered-path consequence
If \(x\notin L\), then x is noninsertable into every Hamilton order of P at every gap; otherwise an insertion would exhibit a Hamilton path on \(P\cup\{x\}\). In particular x reverses both exposed end-edges of every displayed Hamilton order of P. The analogous statement holds for Q.

Hence every minimum balanced deletion state of hole size at least three has one of two global residues:

- **one-sided extension desert:** one balanced side is universally nonextendable by every hole label; or
- **single-root double-extension:** apart from at most one exceptional hole label z, every other hole label is simultaneously nonextendable into both balanced sides and therefore reverses all four exposed end-edges.

This is a scale-independent Hall obstruction on actual Hamiltonian supports. It identifies the exact structure that any attempt to compress a large balanced hole must defeat.

### Relation to the audited zero-root frontier
A zero exact root does not by itself imply that its hole is a minimum balanced deletion set, so this theorem must not be applied to an arbitrary zero-root chamber. It applies after minimizing the balanced deletion number \(\zeta_2(H)\), or whenever independent arguments certify minimality of the balanced hole.

For a minimum counterexample, \(\kappa_2(H)=1\). Thus any route that supplies a balanced deletion state can minimize it and reduce all larger balanced holes to the two extension-desert residues above. A matching of size two is already a terminating improvement: it lowers the balanced hole by two.
