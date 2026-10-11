# Dimension-five closure and cyclic windows

# Dimension five and the sharpness of unrestricted closure

An ordered three-face consists of a three-dimensional cube face and an ordering of its free coordinate directions. The color of this object may depend on all exterior fixed bits, but is independent of the traversal corner within the face. An antipodal geodesic in \(Q_n\) changes each coordinate exactly once, and its \(n-2\) consecutive ordered-three-face colors form its color word.

**Theorem 1 (unrestricted \(Q_5\)).** Every binary coloring of ordered three-faces of \(Q_5\) admits an antipodal geodesic whose three-window color word changes at most once.

**Proof.** If every five-direction geodesic failed, each color word would be \(010\) or \(101\), hence its first and third colors would agree. Fix a coordinate order \((a,b,c,d,e)\) and vary the starting bits. The first face color depends only on the fixed \(d,e\)-bits, while the last face color depends only on the independent \(a,b\)-bits, toggled before the third window. Equality for all four exterior bits forces both colors to be constant functions of their face positions. Since every ordered triple occurs as the first window of some full order, the entire coloring is position-independent, \(c(F,(a,b,c))=h(a,b,c)\). Failure in every order now gives \(h(a,b,c)\ne h(b,c,d)\) for every sequence of four distinct coordinates. Applied around the five cyclic rotations of \((a,b,c,d,e)\), this alternates five binary labels around an odd cycle, which is impossible. \(\square\)

**Theorem 2 (sharpness without antipodal oddness).** For every \(n\ge6\) there exists a face-independent binary coloring of ordered three-faces of \(Q_n\) such that *every* antipodal geodesic has at least two color changes.

**Proof.** Partition the coordinate directions as \(V=A\sqcup B\), with \(|B|=2\), and set
\[
h(a,b,c)=
\begin{cases}
1,&b\in A\ \text{and}\ (a\in B\text{ or }c\in B),\\
0,&\text{otherwise}.
\end{cases}
\]
Color \((F,(a,b,c))\) by \(h(a,b,c)\), independently of \(F\). Fix a full direction order \((p_1,\ldots,p_n)\). For \(2\le j\le n-1\), the window centered at \(p_j\) has color \(1\) precisely when \(p_j\in A\) and at least one of its immediate neighbors belongs to \(B\). Denote the resulting word indexed by centers \(j=2,\ldots,n-1\) by \(w\).

The word \(w\) contains a \(1\). Indeed, if the first \(B\)-position is \(i\ge3\), the preceding position \(i-1\) is an eligible interior \(A\)-center adjacent to \(B\). If \(i=2\), use center \(3\), unless the other \(B\) lies at \(3\), in which case use center \(4\). If \(i=1\), use center \(2\), unless the other \(B\) lies at \(2\), in which case use center \(3\). These positions exist and lie between \(2\) and \(n-1\) since \(n\ge6\).

We claim that if \(w\) begins with \(1\), it contains a later \(0\) and a still later \(1\). The position \(2\) is then an \(A\)-center, so one \(B\) occurs at position \(1\) or \(3\). If position \(3\) belongs to \(B\), its color is zero; center \(4\) has color one unless the other \(B\) is at position \(4\), in which case center \(5\) has color one. If position \(3\) belongs to \(A\), the \(B\)-positions are \(1\) and \(k\ge4\). For \(k=4\), the colors at centers \(3,4,5\) are \(1,0,1\). For \(k\ge5\), center \(3\) has color zero and center \(k-1\) has color one. This proves the claim. Reversing the direction order gives its mirror: if \(w\) ends with \(1\), it also has at least two changes. If \(w\) begins and ends with zero, its previously established occurrence of \(1\) produces at least two changes. Thus every order has at least two changes, independently of the starting vertex. \(\square\)

The construction in Theorem 2 satisfies \(h(c,b,a)=h(a,b,c)\), so it is **reversal-even**. It fails NORI's antipodal-reversal oddness, which for a position-independent coloring requires \(h(c,b,a)=1-h(a,b,c)\). Thus dimension five is the largest dimension in which the unrestricted one-change statement holds, while the NORI conjecture remains a distinct problem in dimension six and above.

## Further structural consequences

The unconditional dimension-five theorem combines an odd five-cycle of direction orders with independence of exterior root bits. Recent sharp counting arguments distinguish the unrestricted Q5 root-density guarantee from the stronger guarantee available under antipodal-reversal oddness.

Statement:
Let V=A⊔B and let c be a binary coloring of ordered three-faces of Q_V. Suppose changing the fixed bit of any a∈A complements c whenever a is outside the free triple. Then for any prescribed ordering σ of A, ordering τ of B, and initial bits on B, there is a choice of initial bits on A such that, along the full geodesic with coordinate order στ, every color change occurs between two consecutive triple windows lying entirely in B; their change sequence agrees exactly with that of the induced ordered-three-face coloring on Q_B at the prescribed B-start vertex. Consequently if |B|≤5, c admits an antipodal geodesic with at most one color change; if |B|≤3, it admits a monochromatic one. These conclusions hold without any antipodal symmetry hypothesis.

Proof:
Let T be the free triple of F. Repeatedly flipping fixed A coordinates gives c(F,π)=[⊕_{a∈A\T}x_a]⊕g(π,x_{B\T}), where g is independent of fixed A bits; each individual fixed A bit occurs with coefficient 1. Write |A|=r, order its coordinates first as a_1,…,a_r and then order B as b_1,…,b_m, and let w_t (1≤t≤n−2) be the color of the t-th consecutive triple window. Denote the initial a_i bit by z_i. Put G_t=g evaluated on the t-th window, a value independent of all z_i (since its fixed B bits are completely determined by the chosen B-start vertex and the B-coordinate order). The parity terms give, for 1≤t≤n−3, w_{t+1}⊕w_t=G_{t+1}⊕G_t⊕1_{t≤r}(z_t⊕1)⊕1_{t+3≤r}z_{t+3}. Fix arbitrarily every z_i with i>min(r,n−3). For t=min(r,n−3), min(r,n−3)−1,…,1 choose z_t to make the displayed difference zero. This is always possible since z_t occurs with coefficient 1 and z_{t+3}, if present, has already been fixed. Thus all differences with t≤r vanish. For t>r both windows are contained in the terminal B order, all A coordinates have already been traversed, and their parity contribution is the same constant. Hence w_{t+1}⊕w_t=G_{t+1}⊕G_t, exactly the adjacent color difference on the induced B-dimensional face coloring. This proves the exact reduction. For m≤3 there are no two consecutive B-only triple windows, so no differences remain. For m=4 there is at most one remaining difference. For m=5, every binary ordered-three-face coloring on Q_5 has a five-direction geodesic with at most one change: otherwise every order and start has word 010 or 101. For any order (a,b,c,d,e), its first and third window colors are equal. They vary independently with the two fixed exterior bits (d,e), respectively (a,b), forcing both functions to be constant. The coloring therefore depends only on the ordered triple, say h(a,b,c), and every order forces h(a,b,c)≠h(b,c,d). Applying these inequalities to the five cyclic rotations of (a,b,c,d,e) forces a binary label to alternate around an odd 5-cycle, impossible. Choose the resulting B-start bits and order and apply the exact reduction.



*The exact scoped proof is preserved in research note* note_q5_seven_flipper_and_root_density_extensions.
