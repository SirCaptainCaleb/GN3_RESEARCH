# Dense exchange matrix for the maximal braid — preserved pre-item development

## Development

## A dense exchange matrix for the maximal braid

Work in the residual order-eleven braid configuration
\[
V=T\sqcup\{a,b,c\},\qquad |T|=8.
\]
Let
\[
T=B\sqcup C,\qquad |B|=5,\quad |C|=3,
\]
and assume that \(B\) is Hamiltonian. For \(x\in B\) and \(y\in C\), put
\[
B_{x,y}=B-x+y,\qquad C_{x,y}=C-y+x.
\]

Fix one moving pair \(P\in\{ab,ac,bc\}\).

**Exchange-matrix lemma.**

1. If \(C\cup P\) is non-Hamiltonian, then for every \(x\in B\), at least two of the three vertices \(y\in C\) satisfy
\[
C_{x,y}\cup P\quad\text{Hamiltonian}.
\]
Equivalently, in the \(5\times3\) matrix indexed by \(B\times C\), at most five cells fail to repair this bad target, and at least ten repair it.

2. For every \(y\in C\), at least three of the five vertices \(x\in B\) satisfy
\[
B_{x,y}\quad\text{Hamiltonian}.
\]
Hence at least nine of the fifteen cells preserve the Hamiltonian complementary side.

**Proof.**
For (1), fix \(x\in B\) and apply the four-of-six theorem to the six-set
\[
(C\cup P)\cup\{x\}.
\]
Deleting \(x\) leaves the assumed non-Hamiltonian five-set \(C\cup P\). Since at least four of the six vertex deletions are Hamiltonian, among the other five deletions at most one is non-Hamiltonian. In particular, among the three deletions of vertices \(y\in C\), at most one is bad. These three deletions are exactly the sets \(C_{x,y}\cup P\). Thus at least two repair the target for each row \(x\).

For (2), fix \(y\in C\) and apply four-of-six to \(B\cup\{y\}\). Deleting \(y\) leaves the Hamiltonian five-set \(B\), so among the five other deletions at least three are Hamiltonian. Those five sets are exactly \(B_{x,y}\), \(x\in B\). Thus every column has at least three side-preserving cells. ∎

### Immediate overlap consequence

If \(C\cup P\) is bad, at least ten cells repair it and at least nine preserve the complementary Hamiltonian side. Since there are only fifteen cells, at least four swaps do both simultaneously:
\[
B_{x,y}\text{ and }C_{x,y}\cup P
\]
are Hamiltonian for at least four pairs \((x,y)\).

Thus a single bad member of the braid triple can always be removed while retaining a Hamiltonian complementary five-set, with at least four choices. The remaining difficulty is simultaneous control of the other two moving pairs.

If two of the three targets are bad, each bad target excludes at most one cell in every row. Therefore at least five of the fifteen swaps repair both bad targets simultaneously. The obstruction to a direct one-swap closure is now sharply localized: all such common repair cells could, in principle, lie among the at most six cells that destroy the Hamiltonian side \(B\). Any failure of the common-core braid lemma must therefore realize a near-extremal overlap between these three sparse failure matrices.

This reduces the maximal braid to a concrete \(5\times3\) finite incidence problem. No minimum-counterexample or disturbance argument is used.
