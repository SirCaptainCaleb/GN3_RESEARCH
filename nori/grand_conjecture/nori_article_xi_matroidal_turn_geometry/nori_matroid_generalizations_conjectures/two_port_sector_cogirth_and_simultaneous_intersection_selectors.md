# Two-port sector cogirth and simultaneous intersection selectors

# NORI Article XI — Two-Port Sector Cogirth and Simultaneous Intersection Selectors

**Research status (October 12, 2026):** The sector-girth formulas and the two-cycle identities below are proved. The rank-growing selector is conjectural.

## Theorem 1: Identical Cogirth in Both Port Sectors

Let \(D^{(2)}\) be the dual of the binary matroid represented by
\[
\begin{pmatrix}
B_H & 0 & 0\\
a & 1 & 0\\
\lambda & 0 & 1
\end{pmatrix},
\]
with distinguished ports \(p,q\), where \(a\) is the two-cover monodromy class and \(\lambda\) its canonical orientation-curvature class.

Define \(g_{pq}\) to be the smallest cocircuit size among cocircuits containing both \(p,q\), and \(g_{p\bar q}\) among those containing \(p\) but not \(q\).

| Family | \(g_{pq}\) | \(g_{p\bar q}\) |
|---|---:|---:|
| Antipodal \(n\)-cube (\(n\ge3\)) | \(n+2\) | \(n+2\) |
| Boundary tournament (\(n\ge4\)) | \(5\) | \(5\) |

**Cube proof.** Every monodromy-one simple turn cycle \(C\) obeys
\[
|C|=n+s(C)+2u(C),
\]
where \(s(C)\) is the number of stationary contacts and \(u(C)\ge0\) is repeated-coordinate excess. Curvature satisfies \(\lambda(C)\equiv 1+s(C)\pmod2\). The both-port sector (\(\lambda=1\)) permits \(s=0\), achieved by an antipodal geodesic of length \(n\); adding both ports gives \(n+2\). The \(p\)-only sector (\(\lambda=0\)) requires odd \(s\), giving turn length at least \(n+1\). At the first internal turn of the standard monotone cube geodesic, insert the incident cube edge in coordinate three; this is a new antipodal edge orbit, producing a simple odd-monodromy turn cycle of length \(n+1\) and precisely one stationary contact. Adding \(p\) gives \(n+2\).

**Boundary proof.** Every monodromy-one triangle in the quotient \(L^2(K_n)\) is a star triangle of curvature one. It produces a both-port cocircuit of size \(3+2=5\). No monodromy-one triangle has curvature zero. The following four-turn cycle has monodromy one and curvature zero:
\[
(1,0,2), (2,0,3), (1,0,3), (0,1,3)
\]
where each triple denotes its reversal orbit. One lift is
\[
(1,0,2),(3,0,2),(3,0,1),(0,1,3),(2,0,1).
\]
The orientation-defect bits are \(1,1,0,0\). Adjoining only \(p\) yields a cocircuit of size \(4+1=5\).

**Consequence.** For every boundary-tournament coloring cycle \(X_d\), every sector-minimum \(p\)-only cocircuit and every sector-minimum both-port cocircuit meets \(X_d\) in **two or four elements** by binary cycle–cocircuit orthogonality. Thus port membership and sector-minimality still cannot enforce a long tight path.

## Theorem 2: Simultaneous Coloring and Orientation Objectives

An admissible deck-odd coloring determines \(d=a+\delta f\) and a binary cycle
\[
X_d=\operatorname{supp}(d)\cup\{p\}.
\]
The orientation curvature row determines a second binary cycle
\[
X_{\mathrm{or}}=\operatorname{supp}(\lambda)\cup\{q\}.
\]
For a cocircuit \(Y_C=C\cup\{p\}\) from an odd-monodromy, curvature-zero simple turn cycle \(C\),
\[
|X_d\cap Y_C|=1+\sum_{t\in C}d(t),\qquad
|X_{\mathrm{or}}\cap Y_C|=\sum_{t\in C}\lambda(t)
\]
with integer sums.

The second intersection vanishes **if and only if every turn is locally coherently oriented** (one incoming edge, one outgoing edge). This is stronger than the zero-curvature parity condition, which allows two or more incoherent turns.

The previously established identity \([\lambda]=[a]+[\kappa_F]\) implies
\[
[d+\lambda]=[\kappa_F],
\]
so \(X_d\triangle X_{\mathrm{or}}\) has a cover-independent turn-cohomology class, although it includes both ports.

## Theorem 3: Coherent Directed Closing Criterion

For a simple odd-monodromy cycle \(C\) of \(H=L(F)\), suppose every local orientation defect is zero and \(s(C)=1\). Reindex the cycle at its unique stationary edge and choose the deck sheet so that the stationary contact occurs at that edge's head. Every subsequent edge must then be traversed from tail to head: the opposite-sense condition at its predecessor and successor forces continuity of the prescribed orientation. The lift is a coherently directed state-edge path ending at the deck reversal of its starting state.

Conversely a coherently directed twisted closing walk has zero local orientation defects and its sole stationary contact occurs at the closing seam.

The resource-simple prefix must still be specified separately. In boundary tournaments it requires independent projected \(K_n\)-edge labels in the graphic matroid \(M(K_n)\). A coherently directed closure can repeat original vertices even when its orientation defect is zero.

## Conjectural Next Step

A unified theorem should select a marked cocircuit \(Y\), for every admissible coloring cycle \(X_d\), with:

1. Bounded color intersection \(|X_d\cap Y|\le q_{\mathrm{seam}}+1\).
2. Zero orientation intersection \(|X_{\mathrm{or}}\cap Y|=0\) in the directed boundary-tournament model.
3. A coherent pre-seam gallery whose projected resources form an independent set of rank at least \(n^{2/(q_{\mathrm{seam}}+1)}\).

The cube uses a full-rank, both-port witness and seam width one. The boundary tournament uses a \(p\)-only coherent witness and seam width three. Proving a rank-increasing, independence-preserving and orientation-defect-preserving exchange/splicing principle is the principal missing step.

**Finite cross-check:** Enumeration of the boundary \(n=4\) quotient turn graph gives 32 triangles (four in monodromy-one/curvature-one sector) and 81 four-cycles (24 in monodromy-one/curvature-zero sector), consistent with the claimed lower bounds. These counts are corroborating checks, not hypotheses of the proofs.
