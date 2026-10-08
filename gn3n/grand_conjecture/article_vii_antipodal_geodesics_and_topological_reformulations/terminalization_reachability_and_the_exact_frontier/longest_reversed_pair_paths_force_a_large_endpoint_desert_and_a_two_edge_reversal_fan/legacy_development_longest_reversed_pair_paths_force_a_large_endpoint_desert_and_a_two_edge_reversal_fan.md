# Longest reversed-pair paths force a large endpoint desert and a two-edge reversal fan — preserved pre-item development

## Longest reversed-pair paths force a one-sided endpoint desert and a two-edge fan

Assume the odd uniform residue on \(n=2r+1\) vertices, with \(r\ge 3\): every \(r\)-set is Hamiltonian and every \((r+1)\)-set is non-Hamiltonian. Hence the global maximum tight-path order is exactly \(r\).

Suppose an ordered pair \((a,b)\) occurs as the initial pair of some maximum \(r\)-path and there exists at least one tight path ending in the reversed pair \((b,a)\). By the unused-vertex reversed-pair augmentation theorem, no maximum \(r\)-path can end in \((b,a)\). Choose a longest tight path with this fixed terminal pair,
\[
R=(c_1,c_2,\ldots,b,a),
\]
of order \(t\). Then \(3\le t\le r-1\).

### Universal prepend reversal

For every vertex \(x\notin V(R)\),
\[
(c_2,c_1,x)
\]
is tight.

Indeed, if \((x,c_1,c_2)\) were tight then \((x,R)\) would be a tight path of order \(t+1\) with the same terminal pair \((b,a)\), contradicting the choice of \(R\). Boundary antisymmetry gives the displayed reverse triple.

Thus the first displayed edge of a longest fixed-terminal-pair path is reversed through **every** exterior vertex.

### A large one-sided endpoint desert

Put \(E=V(H)\setminus V(R)\). Since \(t\le r-1\),
\[
|E|=2r+1-t\ge r+2.
\]
Let \(T\subseteq E\) have order \(r-1\), and set
\[
S=\{c_1\}\cup T.
\]
Then \(S\) is Hamiltonian by the odd uniform hypothesis, but **no** Hamilton order of \(S\) begins at \(c_1\).

For if
\[
Q=(c_1,d,q_3,\ldots,q_r)
\]
were a Hamilton order of \(S\), then \(d\in E\), so the universal prepend reversal gives \((c_2,c_1,d)\) tight. Hence
\[
(c_2,c_1,d,q_3,\ldots,q_r)
\]
would be a tight \((r+1)\)-path, contradiction.

Therefore every one of the \(\binom{|E|}{r-1}\) Hamiltonian \(r\)-supports \(\{c_1\}\cup T\) is simultaneously forbidden from using \(c_1\) as an initial endpoint. This is an ambient uniform endpoint obstruction, not a statement about one isolated support.

### Every exterior maximum path carries a two-edge reversal fan

Take any \(r\)-set \(B\subseteq E\), and any Hamilton order
\[
B=(d_1,\ldots,d_r).
\]
The universal prepend reversal gives \((c_2,c_1,d_i)\) tight for every \(i\).

If \((c_1,d_1,d_2)\) were tight, then
\[
(c_2,c_1,d_1,d_2,\ldots,d_r)
\]
would be a tight path of order \(r+2\), contradiction. Hence
\[
(d_2,d_1,c_1)
\]
is tight.

If \((c_1,d_2,d_3)\) were tight, then
\[
(c_2,c_1,d_2,d_3,\ldots,d_r)
\]
would be a tight path of order \(r+1\), contradiction. Hence
\[
(d_3,d_2,c_1)
\]
is tight.

Thus for **every** Hamilton order on **every** exterior \(r\)-set, the first two displayed edges are reversed through the same anchor \(c_1\):
\[
(d_2,d_1,c_1),\qquad (d_3,d_2,c_1).
\]

No analogous third edge is forced by this length count alone: starting the inherited tail at \(d_3\) would produce only an \(r\)-vertex path.

### How this enters the current frontier

The majority-coloring theorem supplies a maximum word beginning \((a,b)\) together with a genuine tight three-word ending \((b,a)\). Hence the hypotheses above occur in the odd uniform residue. The reversed-pair augmentation theorem prevents the fixed-terminal path from reaching order \(r\). Consequently the surviving odd-uniform branch contains a canonical large endpoint desert and a uniform two-edge reversal fan.

This is stronger than merely saying that a reversed three-prefix failed to grow. Any closure argument may now attack the simultaneous family of forbidden endpoint roles, or combine the common two-edge fan with a second maximum-support order to force a seam. No spanning two-cover is claimed here.
