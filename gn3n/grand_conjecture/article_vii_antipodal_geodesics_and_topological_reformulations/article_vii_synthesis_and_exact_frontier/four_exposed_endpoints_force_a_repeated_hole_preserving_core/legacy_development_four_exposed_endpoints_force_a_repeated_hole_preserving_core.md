# Four exposed endpoints force a repeated hole-preserving core — preserved pre-item development

## Composition

(none yet)

## Development

## Four exposed endpoints force a repeated hole-preserving core

Let
\[
Y\mid P\mid Q
\]
be a spanning three-cover with \(|Y|=5\), where \(Y\) contains two distinguished hole labels \(x,y\), and write
\[
N=Y-\{x,y\},\qquad |N|=3.
\]
Assume both long paths \(P,Q\) have order at least six. For each displayed endpoint \(e\) of \(P\) or \(Q\), suppose the six-set \(Y\cup\{e\}\) is non-Hamiltonian, and define
\[
G_e=\{r\in Y:(Y-\{r\})\cup\{e\}\text{ is Hamiltonian}\}.
\]
The four-of-six theorem gives \(|G_e|\ge3\).

Since only two labels of \(Y\) are holes, every endpoint has at least one good ordinary deletion:
\[
A_e:=G_e\cap N\ne\varnothing.
\]

There are four exposed endpoints and only three ordinary labels in \(N\). Hence some
\[
r\in N
\]
belongs to \(A_e\) for at least two distinct endpoints. Equivalently, the same four-label core
\[
C=Y-\{r\},
\]
which still contains both distinguished hole labels, accepts at least two of the four exposed endpoints:
\[
C\cup\{e\}\text{ is Hamiltonian}
\]
for at least two endpoint choices \(e\).

Thus every hard rooted five-component has one of two stronger forms:

1. **same-tail repetition:** one hole-preserving four-core accepts both endpoints of one long tail; or
2. **cross-tail repetition:** one hole-preserving four-core accepts an endpoint of \(P\) and an endpoint of \(Q\).

This removes the possibility that all four endpoint cores are unrelated. The remaining handoff problem can be organized around a single four-core containing both holes and two ordinary labels, with only the placement of its two good endpoint incidences left to distinguish.
