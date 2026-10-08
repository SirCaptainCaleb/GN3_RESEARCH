# Four-window adjacent-swap locality in every dimension

# Dimension-independent adjacent-order exchange law

Let \(n\ge4\), \(x\in Q_n\), and \(p=(p_1,\ldots,p_n)\) be a permutation of the coordinate directions. For \(1\le i\le n-2\), let \(W_i(x,p)\) be the *actual* ordered three-face window of the full geodesic from \(x\) following \(p\), and let \(w_i(x,p)=c(W_i(x,p))\) for an arbitrary binary ordered-face coloring \(c\). For \(1\le i\le n-3\), write \(d_i(x,p)=w_i(x,p)\oplus w_{i+1}(x,p)\). Let \(\tau_kp\) interchange adjacent directions \(p_k,p_{k+1}\), where \(1\le k\le n-1\).

**Theorem (four-window locality).** For every \(x,p,k\),
\[
W_i(x,\tau_kp)=W_i(x,p)
\quad\text{for }i\notin [k-2,k+1]\cap[1,n-2],
\tag{1}
\]
and therefore
\[
d_i(x,\tau_kp)=d_i(x,p)
\quad\text{for }i\notin[k-3,k+1]\cap[1,n-3].
\tag{2}
\]
In particular, a single adjacent swap can modify **at most four consecutive window colors** and **at most five consecutive seams**, independently of \(n\) and irrespective of exterior-face dependence.

For the two central potentially affected windows \(i=k-1\) and \(i=k\), whenever these indices exist, the underlying geometric three-face is unchanged by the swap, and only the ordering of its free directions changes. Explicitly, writing \(a=p_{k-1}\), \(b=p_k\), \(c=p_{k+1}\), \(d=p_{k+2}\), these central free-direction orders are
\[
(a,b,c)\longleftrightarrow(a,c,b),\qquad
(b,c,d)\longleftrightarrow(c,b,d),
\tag{3}
\]
at **identical exterior face positions**. The other potentially affected windows are the two neighboring positions \(k-2,k+1\), where the geometric free triple changes.

**Proof.** Before the swapped pair is reached, the two full geodesics traverse exactly the same ordered directions. After the pair is completed, they have traversed exactly the same *set* of directions and agree on the current cube vertex. Thus for every window whose three free positions avoid both swap positions, its ordered free triple and all previously traversed directions are the same for both paths. The two corresponding ordered faces coincide. A length-three interval intersects positions \(k,k+1\) exactly when its starting position belongs to \(\{k-2,k-1,k,k+1\}\), proving (1). Each change indicator is the XOR of two consecutive window colors, so it can change only if either endpoint window does, giving (2). For \(i=k-1\) and \(i=k\), both exchanged directions lie within the same free triple; the prefix preceding each such window is the same in both geodesics, so their exterior face positions coincide. The displayed direction orders follow immediately. \(\square\)

**Interaction with NORI antipodal reversal.** If \(c\) satisfies \(c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi)\), the established root-coupled reversal involution
\[
J(x,p)=(x,\operatorname{rev}p)
\]
obeys \(w_i(x,\operatorname{rev}p)=1\oplus w_{n-1-i}(x,p)\) and \(d_i(x,\operatorname{rev}p)=d_{n-2-i}(x,p)\). Adjacent swaps transform equivariantly under this involution:
\[
\operatorname{rev}(\tau_k p)=\tau_{n-k}(\operatorname{rev}p).
\tag{4}
\]
Thus the graph of full orders, with edges given by adjacent swaps, is the **permutohedron**, equipped with a free reversal involution and an antipodally equivariant, locally constrained word label. The NORI conjecture asks for some root and vertex in this coupled family of permutohedra whose word has at most one change.

**Research obligation.** This lemma gives a dimension-independent local move for a possible minimal-defect exchange/descent argument. It is not itself a decreasing-move theorem. A closure proof must show that the no-good-geodesic hypothesis, together with cross-root face-fiber incidence and antipodal reversal, forces either a strictly improving local exchange (possibly following a finite sequence of nonincreasing exchanges) or a topological obstruction to all local minima. Such a proof would apply uniformly to every dimension, unlike further Q7 subclass classifications.
