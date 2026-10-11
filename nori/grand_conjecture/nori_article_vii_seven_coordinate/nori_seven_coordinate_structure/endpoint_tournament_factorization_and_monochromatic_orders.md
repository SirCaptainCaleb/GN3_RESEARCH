# Endpoint-tournament factorization and monochromatic orders

# Endpoint-tournament factorization and monochromatic orders

## Arbitrary middle-sign twists: a spanning theorem from oriented Hamilton paths

Let \(V\) be a set of \(n\) coordinate directions, \(T\) an arbitrary tournament on \(V\), and \(s:V\to\{0,1\}\) *any* binary function. Set
\[
t(a,c)=\begin{cases}0&a\to c\text{ in }T,\\1&c\to a\text{ in }T,\end{cases}
\qquad
b(a,v,c)=t(a,c)\oplus s(v)
\]
for pairwise distinct \(a,v,c\). Thus the local comparison tournament at a middle vertex \(v\) is either \(T[V\setminus\{v\}]\) or its complete reversal, with the choice allowed to vary at *every* middle vertex.

**Theorem (arbitrary middle-sign spanning tight path).** For every \(n\ge3\), every such \(b\) has a vertex-simple **spanning positive tight path**. Its direction-only realization \(c(F,(a,v,c))=b(a,v,c)\) on the *physical ordered three-faces* of \(Q_n\) obeys both same-face reversal oddness and antipodal invariance, and admits a **monochromatic full antipodal cube geodesic from every starting root**.

**Proof.** We have \(t(c,a)=1\oplus t(a,c)\), hence \(b(c,v,a)=1\oplus b(a,v,c)\). Direction-only physical-face coloring therefore has \(c(F,\operatorname{rev}\pi)=1\oplus c(F,\pi)\) and \(c(\bar F,\pi)=c(F,\pi)\), giving the legal combined NORI antipodal-reversal law.

Put \(m=\lceil n/2\rceil\ge2\) and \(k=\lfloor n/2\rfloor\). By pigeonhole, some bit \(\varepsilon\) occurs at least \(m\) times among the values \(s(v)\). We choose an \(m\)-element set \(O\subseteq s^{-1}(\varepsilon)\), and put \(E=V\setminus O\), so \(|E|=k\). For \(m\notin\{3,5,7\}\), any \(O\) will work. If \(m\in\{3,5,7\}\) and \(|s^{-1}(\varepsilon)|\ge m+1\), choose \(O\) so that \(T[O]\) is **not regular**. Such a set exists by the following elementary observation.

**Nonregular-subtournament observation.** In a tournament on at least \(m+1\) vertices, with \(m\ge3\) odd, some induced subtournament of order \(m\) is nonregular. Indeed, otherwise fix any set \(U\) of \(m+1\) vertices. Every \(U\setminus\{u\}\) would be regular of degree \((m-1)/2\). Fix \(v\in U\). Comparing its degrees in \(U\setminus\{u\}\) for the various \(u\ne v\) shows that the indicators \(\mathbf1_{\{v\to u\}}\) are equal for every \(u\ne v\), so \(v\) either dominates or loses to every other vertex of \(U\). Its degree in \(U\setminus\{u\}\) would then be \(m-1\) or zero, contradicting regularity since \(0<(m-1)/2<m-1\). This proves the observation.

Finally, if \(m\in\{3,5,7\}\) and the majority sign class has size exactly \(m\), take that entire class for \(O\). Then all members of \(E\) have the opposite sign \(1\oplus\varepsilon\).

Every tournament has a directed Hamilton path. Choose an order \(e_1,\ldots,e_k\) on \(E\) such that
\[
t(e_j,e_{j+1})=\varepsilon\quad(1\le j<k).
\]
For \(\varepsilon=0\), use an ordinary directed Hamilton path in \(T[E]\); for \(\varepsilon=1\), reverse one.

Now prescribe an orientation of the *abstract* path on \(m\) consecutively numbered vertices: its \(j\)-th edge points forward precisely when \(s(e_j)=0\), and backward precisely when \(s(e_j)=1\), for \(1\le j<m\). These \(m-1\) bits are defined because \(k\ge m-1\) in both parities. Havet and Thomassé's exact theorem states that every tournament contains every orientation of a Hamilton path of the same order **except** for an antidirected path in one of three regular tournaments: the directed \(3\)-cycle, the regular \(5\)-vertex tournament, and the Paley \(7\)-vertex tournament. If \(m\notin\{3,5,7\}\), there is no exception (this includes \(m=2\)). If \(m\in\{3,5,7\}\) and the majority class has size at least \(m+1\), our nonregular choice of \(T[O]\) avoids all exceptions. In the remaining case, \(E\) has constant sign \(1\oplus\varepsilon\), so the prescribed abstract path is uniformly directed (or uniformly reversed), and the elementary tournament Hamilton-path theorem applies even if \(T[O]\) is exceptional. Thus in **every dimension \(n\ge3\)** we can realize the prescribed orientation inside \(T[O]\). We obtain an ordering \(o_1,\ldots,o_m\) of all \(O\), with
\[
t(o_j,o_{j+1})=s(e_j)\quad(1\le j<m).
\]

Interleave the two orders, beginning with the \(O\)-order:
\[
p=(o_1,e_1,o_2,e_2,\ldots,o_k,e_k)
\]
when \(n=2k\), and
\[
p=(o_1,e_1,o_2,e_2,\ldots,o_k,e_k,o_{k+1})
\]
when \(n=2k+1\). All \(n\) entries of \(p\) are distinct.

The consecutive triples starting at odd positions have the form \((o_j,e_j,o_{j+1})\); their color is
\[
b(o_j,e_j,o_{j+1})
=t(o_j,o_{j+1})\oplus s(e_j)=0.
\]
Those starting at even positions have the form \((e_j,o_{j+1},e_{j+1})\); their color is
\[
b(e_j,o_{j+1},e_{j+1})
=t(e_j,e_{j+1})\oplus s(o_{j+1})
=\varepsilon\oplus\varepsilon=0.
\]
Thus \(p\) is a spanning positive tight path. The physical cube path traversing the coordinates in the order \(p\) uses each coordinate once and is therefore a full antipodal geodesic. Its consecutive physical ordered-three-face windows all have color zero because the coloring depends only on the ordered coordinate triple, so **every starting cube vertex works**. \(\square\)

**Corollary (large induced factorized chart).** Let \(b\) be an arbitrary ordinary boundary 3-tournament on \(V\). If some \(X\subseteq V\), \(|X|\ge3\), has an induced triple coloring of the above factorized form, then \(b\) has a positive vertex-simple tight path on all \(|X|\) vertices of \(X\), hence a genuine monochromatic cube geodesic of \(|X|\) moves. More generally, the same conclusion holds for physical ordered-three-face colorings on a fixed cube fiber whenever every triple on \(X\) is insensitive to changing the coordinates of \(X\) outside its free set and, on that common fiber, agrees with the factorized rule. This fiber hypothesis ensures that all windows share the *same* direction-only chart.

**Interpretation and exact limitation.** The earlier all-dimensional theorem below permits one exceptional value of \(s\) and uses elementary tournament Hamilton paths. The new theorem permits **arbitrary sign patterns at all \(n\) middle directions**, replacing the required second parity-path orientation by the universal oriented-Hamilton-path theorem; the three exceptional oriented-Hamilton-path instances of orders \(3,5,7\) are avoided by choosing a nonregular majority subtournament or, when the majority class has exactly the required size, by observing that the prescribed orientation pattern is constant. Thus the theorem holds in every dimension \(n\ge3\). This does not assert the same result for a general boundary 3-tournament: there the local middle tournaments \(T_v\) can vary independently, rather than being restrictions of one tournament or its reverse. Handling a chronologically *prescribed sequence of different tournaments* on one parity class is the missing transfer. The familiar theorem on transversal Hamilton paths through a family of tournaments does not automatically supply this ordered requirement. The arbitrary exterior-dependent physical NORI3 case and the separate unrestricted NORI1 full-geodesic conjecture also remain unresolved.

**External theorem used.** F. Havet and S. Thomassé, *Oriented Hamiltonian Paths in Tournaments: A Proof of Rosenfeld's Conjecture*, Journal of Combinatorial Theory, Series B **78** (2000), 243–273, DOI 10.1006/jctb.1999.1945. The published theorem has three small antidirected-path exceptions on 3, 5, and 7 vertices; there are no exceptions on at least eight vertices.

## Two arbitrary middle-local tournament types: a linear guarantee

The preceding theorem assumes all middle-vertex comparison tournaments are a single tournament or its reverse. A different parity argument retains *two completely unrelated* comparison tournaments.

**Theorem (two-type boundary tournaments).** Let \(b\) be an ordinary boundary 3-tournament on \(n\ge3\) vertices. Suppose there are arbitrary tournaments \(T_0,T_1\) on \(V\) and an assignment \(s:V\to\{0,1\}\) such that
\[
b(a,v,c)=t_{s(v)}(a,c),\qquad
t_j(a,c)=\begin{cases}0&a\to c\text{ in }T_j,\\1&c\to a\text{ in }T_j.\end{cases}
\]
Then \(b\) contains a vertex-simple positive tight path of order at least
\[
\boxed{\lceil 2n/3\rceil}.
\]
If the two middle-vertex classes \(A=s^{-1}(0)\) and \(B=s^{-1}(1)\) differ in cardinality by at most one, \(b\) contains a **spanning positive tight path**. Both conclusions give monochromatic genuine coordinate-distinct cube geodesics of the same move lengths for the corresponding direction-only physical face coloring.

**Proof.** For any vertex set \(X\) all of whose middle vertices have the same type \(j\), its induced triple coloring is \(b(a,v,c)=t_j(a,c)\). Split \(X\) into two parity classes with cardinalities differing by at most one. Choose a directed Hamilton path in \(T_j\) restricted to each parity class, and interleave their vertices. Every consecutive ordered triple has its outer vertices consecutive within one of those directed paths and hence has color zero. Thus \(X\) admits a spanning positive tight path.

Write \(a=\max(|A|,|B|)\), \(b_0=\min(|A|,|B|)\), so \(a+b_0=n\). The preceding observation gives a positive tight path of order \(a\) inside a largest type class. Also select \(b_0\) vertices from each class, obtaining sets \(A'\subseteq A\) and \(B'\subseteq B\) of equal order \(b_0\). Choose a directed Hamilton path through \(A'\) in the tournament corresponding to the **middle type of \(B'\)**, and a directed Hamilton path through \(B'\) in the tournament corresponding to the **middle type of \(A'\)**. Interleave these two Hamilton paths. Windows centered at \(B'\) compare consecutive vertices of the \(A'\)-path, and windows centered at \(A'\) compare consecutive vertices of the \(B'\)-path. Every window has color zero, yielding a positive tight path of order \(2b_0\).

Consequently the longest positive path has order at least \(\max(a,2b_0)\). As \(a+b_0=n\),
\[
\max(a,2b_0)\ge 2n/3,
\]
so integer path order is at least \(\lceil2n/3\rceil\).

If \(a=b_0\), the equal-size interleaving already spans \(V\). If \(a=b_0+1\), instead choose a directed Hamilton path of order \(a\) in the tournament of the other class, a directed Hamilton path of order \(b_0\) in the tournament of the first class, and interleave beginning and ending with a vertex from the larger class. Every window is again positive, and all \(n\) vertices occur. The physical realization is exact because the direction-only colors depend exclusively on these ordered triples and all directions are distinct. \(\square\)

**Scope.** The balanced conclusion permits independent and arbitrarily cyclic local tournaments \(T_0,T_1\), with no common global edge order and no reversal relationship between them. The \(\lceil 2n/3\rceil\) result is a genuinely linear guarantee even for unbalanced classes; the arbitrary-middle-sign theorem above strengthens it to full spanning when \(T_1\) is the reverse of \(T_0\) and \(n\ge3\). For a general boundary 3-tournament, the number of distinct local tournament types can grow with \(n\), so neither result asserts a universal linear bound. A promising precise next obstacle is a **chronologically prescribed** Hamilton path through two or more varying tournaments, rather than an unordered transversal that can assign its colors to positions after the path is chosen.

---

## Elementary all-dimensional theorem with one exceptional middle sign

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

## Chronologically prescribed transitive tournaments: a rank-potential theorem and the coupled-parity obstruction

A tempting strengthening of the two-parity factorization method is to replace one fixed comparison tournament by a tournament that varies with the *position* in a path. The correct transitive case has a simple exact solution. It still does not synchronize the two interleaved parity paths.

**Theorem (chronological transitive Hamilton paths).** Let \(X\) be a set of \(m\ge 2\) vertices, and for each \(1\le i<m\) let \(T_i\) be a transitive tournament on \(X\). There is an ordering \(x_1,\ldots,x_m\) of all of \(X\) such that
\[
 x_i\longrightarrow x_{i+1}\quad\text{in }T_i
 \qquad(1\le i<m).
\]
More generally, for arbitrary injective real rank functions \(\rho_i:X\to\mathbb R\), one can require \(\rho_i(x_i)<\rho_i(x_{i+1})\) simultaneously.

**Proof.** Give \(T_i\) its unique increasing rank order \(\rho_i\). For every permutation \(p=(p_1,\ldots,p_m)\), define the scalar potential
\[
 \Phi(p)=\sum_{j=1}^m\ \sum_{i=j}^{m-1}\rho_i(p_j).
\]
Choose a permutation minimizing \(\Phi\). If \(p_j=a,p_{j+1}=b\) and \(\rho_j(a)>\rho_j(b)\), swapping those adjacent entries changes the potential by
\[
 \Phi(p\circ(j\ j+1))-\Phi(p)=\rho_j(b)-\rho_j(a)<0,
\]
contradicting minimality. Thus every prescribed comparison is positive. The proof is constructive through a finite linear assignment minimization followed, equivalently, by descent along improving adjacent swaps. \(\square\)

**Boundary-tournament half-window consequence.** Let \(A=\{a_1,\ldots,a_m\}\) and \(B=\{b_1,\ldots,b_{m-1}\}\) be disjoint vertex sets of an ordinary boundary 3-tournament, with the sequence \(b_1,\ldots,b_{m-1}\) already fixed. Suppose that for each \(i\) the middle-local tournament \(T_{b_i}[A]\), defined by \(u\to v\) iff \(h(u,b_i,v)=1\), is transitive. The theorem orders \(A\) so that
\[
 h(a_i,b_i,a_{i+1})=1\qquad (1\le i<m).
\]
Consequently the vertex-simple interleaving
\[
 a_1,b_1,a_2,b_2,\ldots,b_{m-1},a_m
\]
has **every triple centered in \(B\)** positive. Its remaining windows, centered in \(A\), are not prescribed by this argument. In a boundary tournament with all middle-local tournaments transitive, one may choose either parity's center order arbitrarily and satisfy all windows of that parity by reordering the other class.



*Exact scoped proof in note* note_chronological_local_center_parity_and_rank_potential_limitations.
