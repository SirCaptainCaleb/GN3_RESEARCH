# Endpoint-tournament factorization and monochromatic orders

# Endpoint-tournament factorization yields monochromatic antipodal geodesics

Let \(V\) be a set of \(n\ge3\) coordinate directions, \(T\) an arbitrary tournament on \(V\), and \(s:V\to\mathbb F_2\) a function constant on \(V\setminus\{v\}\) for some \(v\in V\). Let \(t(a,c)\in\mathbb F_2\) be 0 when \(a\to c\) in \(T\) and 1 when \(c\to a\). Define the position-independent ordered-face coloring
\[
c(F,(a,b,c'))=t(a,c')\oplus s(b).
\]
(Here \(c'\) names the third direction, to distinguish it from the coloring \(c\).)

**Theorem (monochromatic tournament-factorized NORI).** This coloring satisfies antipodal-reversal oddness and admits a monochromatic full antipodal geodesic, for every \(n\ge3\).

**Balanced two-path lemma.** For every tournament \(T\) on \(n\ge3\) vertices and any distinguished vertex \(v\), there is an ordering \(p=(p_1,\dots,p_n)\) such that \(p_i\to p_{i+2}\) for all \(1\le i\le n-2\) and \(v\in\{p_1,p_n\}\).

**Proof of the lemma.** Every tournament has a directed Hamilton path: inductively insert a new vertex immediately before the first existing path vertex it dominates, or append it if it dominates none. Choose such a path \(q=(q_1,\ldots,q_n)\), with \(v=q_j\).

If \(n=2k\), at least one of the numbers \(j-1,n-j\) is at least \(k-1\). If \(n-j\ge k-1\), take the consecutive directed path \(q_j,\ldots,q_{j+k-1}\) as the odd-position subsequence \(p_1,p_3,\ldots,p_{2k-1}\). Then \(p_1=v\). If \(j-1\ge k-1\), take \(q_{j-k+1},\ldots,q_j\) as the even-position subsequence \(p_2,p_4,\ldots,p_{2k}\). Then \(p_n=v\). In either case, order the other \(k\) vertices by any directed Hamilton path in their induced tournament and place them in the vacant parity positions.

If \(n=2k+1\), at least one of \(j-1,n-j\) is at least \(k\). Take a directed consecutive \(q\)-segment of \(k+1\) vertices beginning or ending at \(v\), and place it in the odd positions \(p_1,p_3,\ldots,p_{2k+1}\); place a directed Hamilton path on the other \(k\) vertices in the even positions. Then \(v=p_1\) or \(v=p_n\), respectively.

In every case, each parity subsequence is a directed path, hence \(p_i\to p_{i+2}\) for all \(i\). \(\square\)

**Proof of the theorem.** Reversing an ordered triple swaps its outer directions; since \(t(c',a)=1\oplus t(a,c')\), we have
\[
c(\bar F,(c',b,a))=t(c',a)\oplus s(b)=1\oplus c(F,(a,b,c')).
\]
Apply the balanced two-path lemma to \(T\) with distinguished vertex \(v\). Along the resulting full coordinate order \(p\), the window at index \(i\) has color
\[
t(p_i,p_{i+2})\oplus s(p_{i+1})=s(p_{i+1}).
\]
All middle positions \(p_2,\ldots,p_{n-1}\) avoid \(v\), so this value is constant. Since the face coloring ignores exterior fixed bits, the starting cube vertex is arbitrary; every such starting vertex yields a monochromatic antipodal geodesic. \(\square\)

**Scope.** This solves a nontrivial all-dimensional subclass of coordinate-only, reversal-odd ternary colorings, including every endpoint-tournament labeling \(t(a,c)\) and every perturbation by a single exceptional middle direction. It does not treat general triangle-dependent ternary colorings or exterior-face-dependent NORI. The proof exhibits the potential usefulness of balanced two-path covers with prescribed extreme vertices as a replacement for one-switch endpoint repairs.

# Facet monochromatic lifting and a face-dependent tournament-factorized class

**Lemma (monochromatic facet lifting).** Let \(n\ge4\), \(g\in[n]\), and let \(c\) be any binary coloring of ordered three-faces of \(Q_n\), without a symmetry assumption. If one facet \(H=\{x:x_g=\varepsilon\}\cong Q_{n-1}\) contains a full \((n-1)\)-direction geodesic all of whose ordered-three-face windows have the same color, then the full \(Q_n\) has an antipodal geodesic with at most one color change.

**Proof.** Let \(p=(p_1,\ldots,p_{n-1})\) be the direction order of the monochromatic geodesic in \(H\), starting from \(y\in H\). In \(Q_n\), start at the vertex whose \(g\)-bit is \(1-\varepsilon\) and whose other coordinates agree with \(y\), and traverse directions \((g,p_1,\ldots,p_{n-1})\). Its first ordered-three-face window contains \(g\) and has arbitrary color \(b\); after the first move the path is in \(H\), and its remaining \(n-3\) windows agree exactly with those of the given monochromatic path in \(H\), so each has color \(q\). The full word is \(b,q,\ldots,q\), with at most one change. \(\square\)

**Corollary (one-facet tournament factorization).** Fix \(g\) and one facet \(x_g=\varepsilon\). Suppose that on all ordered three-faces lying entirely within this single facet, the coloring is position-independent and is of the form
\[
c(F,(a,b,d))=t(a,d)\oplus s(b),
\]
where \(t(a,d)=0\) for \(a\to d\) in some tournament on \([n]\setminus\{g\}\), \(t(d,a)=1\oplus t(a,d)\), and \(s\) is constant except possibly at one direction. Then \(Q_n\) admits a one-change antipodal geodesic. The coloring of every face containing \(g\), and every face in the opposite facet, is arbitrary; antipodal-reversal oddness is unnecessary.

**Proof.** The balanced two-path tournament lemma proved above supplies a monochromatic full geodesic in the specified \((n-1)\)-facet. Apply the lemma above. \(\square\)

**Research role.** A single suitably structured facet suffices for full one-change closure. In particular, face-dependent behavior outside that facet and across the entering ordered-three-face window cannot spoil the construction. This is a route for extending monochromatic coordinate-only theorems to genuine face-dependent NORI families.

## Recent consequences and compatibility conditions

**Theorem.** There is a coordinate-only reversal-odd ordered-three-face coloring of Q_7 with no monochromatic six-direction geodesic in any coordinate facet. It nevertheless admits a full one-change geodesic. Thus the six-direction monochromatic-five-facet theorem cannot be extended by requiring a monochromatic (n-1)-facet in every dimension.

**Exact construction.** Let V={0,1,2,3,4,5,6}. List the ordered triples (a,b,c) with a<c in lexicographic order, starting at index 0. There are 105 such triples. Let
M=0x1ace4c51f1eca17f4237e025d13.
For a<c, define h(a,b,c) to be bit i of M, where i is that triple's index. For a>c, put h(a,b,c)=1-h(c,b,a). Color each ordered face by h of its direction order, independently of its exterior bits. Reversal oddness follows immediately from the definition.

**Verification certificate.** The following complete finite enumeration reproduces the color-change counts. Its indexing convention fully specifies the example.

    from itertools import permutations
    from collections import Counter
    V = range(7)
    reps = [t for t in permutations(V,3) if t[0] < t[2]]
    index = {t:i for i,t in enumerate(reps)}
    M = int("1ace4c51f1eca17f4237e025d13",16)
    def h(t):
        if t[0] < t[2]:
            return (M >> index[t]) & 1
        return 1 - ((M >> index[t[::-1]]) & 1)
    for k in (5,6,7):
        counts = Counter()
        for p in permutations(V,k):
            w = [h(p[i:i+3]) for i in range(k-2)]
            counts[sum(x != y for x,y in zip(w,w[1:]))] += 1
        print(k, dict(sorted(counts.items())))

The exact output is:

| directions traversed | zero changes | one change | two changes | three changes | four changes |
|---|---:|---:|---:|---:|---:|
| 5 | 100 | 1168 | 1252 | 0 | 0 |
| 6 | 0 | 792 | 2520 | 1728 | 0 |
| 7 | 0 | 144 | 1332 | 2376 | 1188 |

Because colors ignore exterior bits, the zero in the six-direction row excludes every monochromatic six-direction path at every starting cube vertex. The example is a finite exact counterexample to the monochromatic-facet strengthening; the full one-change statement holds.

**Compatibility mechanism.** The cyclic direction order
(0,1,2,5,3,4,6)
has circular triple word 1101001. Three of its six-direction facet deletions are good:
(3,4,6,0,1,2), with word 0011;
(4,6,0,1,2,5), with word 0111;
(6,0,1,2,5,3), with word 1110.
The three-cyclic-facet theorem (Item nori_three_cyclic_facet_witnesses_dimension_independent_20261008) therefore applies. Explicitly, the full rotation
(3,4,6,0,1,2,5)
has word 00111.

**Research implication.** Retain one-change facet witnesses as the induction state. Their compatibility on a common cyclic direction order can force full closure even when every monochromatic facet is absent. This example supports the cyclic-witness target and identifies a strict limitation of demanding monochromatic facet transfer at every stage.

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
