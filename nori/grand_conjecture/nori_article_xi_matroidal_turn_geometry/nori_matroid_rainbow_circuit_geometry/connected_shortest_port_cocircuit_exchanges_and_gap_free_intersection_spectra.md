# Connected shortest-port-cocircuit exchanges and gap-free intersection spectra

# Connected minimum port cocircuits and their intersection spectrum

Let \(n\ge3\). Write \(G_n=Q_n/\langle\tau\rangle\), \(H_n=L(G_n)\), and let \(D_n\) be the pointed binary matroid with distinguished element \(p\) whose cycles containing \(p\) are \(X_d=\operatorname{supp}(a+\delta f)\cup\{p\}\). Here \(a\) represents the nonzero covering monodromy on \(H_n\). Denote by
\[
\mathcal Y_n=\{Y\in\mathcal C^*(D_n):p\in Y,\ |Y|=n+1\}
\]
the minimum port-containing cocircuits. They are precisely \(Y_C=C\cup\{p\}\), with \(C\) the turn cycle of a full antipodal cube geodesic.

Two elements \(Y,Y'\in\mathcal Y_n\) are *adjacent* when they have representatives that are rooted full antipodal geodesics with the same initial cube vertex and direction orders differing by the interchange of two consecutive directions.

**Theorem 1 (connected bounded exchanges).** The adjacency graph on \(\mathcal Y_n\) is connected. For adjacent \(Y,Y'\),
\[
\boxed{|Y\triangle Y'|\le6,\qquad
p\notin Y\triangle Y',\qquad
Y\triangle Y'\in\ker\alpha\subseteq Z_1(H_n;\mathbb F_2).}
\tag{1}
\]
For every binary cycle \(X\) of \(D_n\) containing \(p\),
\[
\boxed{\bigl||X\cap Y|-|X\cap Y'|\bigr|\le2.}
\tag{2}
\]

*Proof.* Let a rooted full geodesic have direction order \((i_1,\ldots,i_n)\). Exchanging consecutive \(i_j,i_{j+1}\) replaces the two-edge cube-square route between the same endpoints. Its lifted cyclic sequence of turns changes only at the comparisons immediately before, between, and immediately after the two exchanged edges. Thus each of the two projected turn cycles has at most three turn edges absent from the other; the distinguished element \(p\) belongs to both. This proves the support bound in (1).

Both turn cycles have monodromy one. Their symmetric difference is an Eulerian binary edge chain with monodromy zero, proving the remaining assertions of (1).

To prove connectedness, work first with rooted pairs \((x,\pi)\), where \(x\in Q_n\) and \(\pi\in S_n\). Adjacent transpositions connect every pair of direction orders at fixed root. In addition, the operation
\[
(x,(i_1,i_2,\ldots,i_n))
\longmapsto
(x^{i_1},(i_2,\ldots,i_n,i_1))
\tag{3}
\]
preserves the projected cyclic turn cycle: it cyclically moves the root across the first edge and replaces that edge by its antipodal mate. To change a prescribed root \(x\) to \(x^j\), move \(j\) to the first position by adjacent transpositions, apply (3), and then reorder by adjacent transpositions. Single-coordinate root changes connect the entire cube, so any two rooted pairs are connected by such operations. After quotienting out operations (3), only adjacent-transposition moves remain; the graph of projected cycles, equivalently \(\mathcal Y_n\), is connected.

For any port-containing binary cycle \(X\), cycle–cocircuit orthogonality gives \(|X\cap Y|\equiv|X\cap Y'|\equiv0\pmod2\). Moreover, at most three elements leave and at most three enter the cocircuit during an adjacent exchange. The integer intersection counts therefore differ by at most three; their difference is even and hence has magnitude at most two. This proves (2). \(\square\)

**Theorem 2 (gap-free even intersection spectrum).** For every \(n\ge3\) and every binary cycle \(X\) of \(D_n\) containing \(p\), put
\[
I_{\min}(X)=\min_{Y\in\mathcal Y_n}|X\cap Y|,
\qquad
I_{\max}(X)=\max_{Y\in\mathcal Y_n}|X\cap Y|.
\]
Then
\[
\boxed{\{\,|X\cap Y|:Y\in\mathcal Y_n\,\}
=\{I_{\min}(X),I_{\min}(X)+2,\ldots,I_{\max}(X)\}.}
\tag{4}
\]
Equivalently, for an arbitrary antipodally odd coloring, the cyclic turn counts of full antipodal geodesics attain every odd integer between their minimum and maximum; their optimally rotated switch counts attain every even integer between the corresponding endpoints.

*Proof.* Choose cocircuits realizing the minimum and maximum, and join them by an adjacency path given by Theorem 1. All intersection numbers along this path are even and consecutive values differ by at most two. Every intermediate even integer must therefore appear. Conversely every intersection number belongs to the even interval between its extrema. For the coloring interpretation, if \(d=\mathbf1_{X\setminus\{p\}}\), the turn count of a full geodesic with cocircuit \(Y\) is \(|X\cap Y|-1\), and cyclic root rotation deletes a changed comparison to yield \(|X\cap Y|-2\) switches. \(\square\)

**Corollary 3 (interpolation from separate witnesses).** Suppose a port-containing cycle \(X\) has minimum cocircuits \(Y_-\) and \(Y_+\) satisfying
\[
|X\cap Y_-|\le2r,\qquad |X\cap Y_+|\ge2s
\]
for integers \(1\le r\le s\). Then every even integer between \(2r\) and \(2s\) occurs as \(|X\cap Y|\) for some \(Y\in\mathcal Y_n\). In particular, any lower bound on a *maximum* intersection furnished by local star statistics can be combined with a bound on the *minimum* to furnish witnesses at each intermediate switch count.

*Proof.* Apply (4); the two hypotheses put the interval \([2r,2s]\) inside the achieved spectrum. \(\square\)

Theorem 1 makes the minimum-port-cocircuit family a connected exchange system with local differences in the even-monodromy cycle space generated by star triangles and cube-square cycles. Theorem 2 is an unrestricted integer-valued consequence of this geometry; it does not require \(X\) to be a circuit and imposes no balance or affine-coloring hypothesis.
