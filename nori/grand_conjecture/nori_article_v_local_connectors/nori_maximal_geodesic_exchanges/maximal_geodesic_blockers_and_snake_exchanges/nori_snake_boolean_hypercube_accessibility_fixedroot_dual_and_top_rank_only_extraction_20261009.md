# Complete Boolean snake-root cube, accessible dual monochromatic fans, and top-rank-only NORI extraction

# FULL Boolean snake-fan cube: exact root anchor, accessibility, antipodal duality, and top-rank-only closure

Sources: active NORI physical ordered-3-face coloring, original Devine–Milans snake digraph inspiration supplied by user; extends proved NORI snake maximal-path dual terminal fan, Johnson hypersimplex rank-two fan, and exact same-root reversed-two-tail criterion. Web/literature search NOT performed.

Let n>=5, q∈{0,1}, P be a GLOBAL LONGEST q-monochromatic cube geodesic of k>=3 edges, k<n, starting at x, ending y, with direction word (u_1,...,u_(k−2),a,b). Put U={u_i}, S=U sqcup {a,b}, T=[n]\S, m=|T|=n−k>=1. Since P is q-terminal maximal, for each d∈T, the true physical cap window (a,b,d) has color 1−q and its antipodal-reversal partner (d,b,a) on F_bar_y({a,b,d}) has color q.

Let
   h=bar y xor a xor b
     = x xor T xor a xor b.
For EACH subset A⊆T define the LITERAL CUBE VERTEX
   r_A=h xor A
       = x xor a xor b xor (T\A).
Thus A↦r_A identifies the whole abstract Boolean lattice 2^T with the vertices of the actual m-dimensional coordinate subcube spanned by T, with all exterior S bits fixed. In particular r_empty=h, r_{d}=h xor d are the m single-snake roots, rank-two r_{d,e} are the JOHNSON J(m,2) roots, and the unique TOP root is
   r_T=x xor a xor b =:s.
The antipodal points IN THAT T-subcube are r_A and r_(T\A), but this relative complement is NOT the full Q_n antipode on physical faces; antipodal NORI coloring oddness applies to the FULL Q_n involution only.

**Definition (honest incoming q snake fan).** Set F_q(P) to comprise nonempty A⊆T such that there exists some ordering d_1,...,d_t of A for which the actual full direction-distinct geodesic
    (d_1,...,d_t,b,a)
from root r_A to fixed endpoint bar y has ALL ordered-three-face window colors q. For formal poset convenience include empty support by declaring the two-edge tail (b,a) from h to bar y vacuously q-monochromatic; it has NO three-face windows and does not itself certify a color.

**THEOREM 1 (accessibility and forced rank-one skeleton).** Every singleton {d}⊆T lies in F_q(P) (the q opposite-corner 3-edge fan). If |A|>=2 belongs to F_q(P), some d∈A exists such that A\{d} also belongs, witnessed by DELETING THE FIRST DIRECTION of the same ordered path. More strongly, a witness for A produces a CHAIN of accessible supports A ⊃ A\{d_1} ⊃ ... ⊃ {d_t} ⊃ empty, all as literal suffixes of a SINGLE monochromatic q-geodesic ending at bar y. This is an accessible set system, not necessarily a downset, antimatroid, greedoid, or simplicial complex. The literal root of each witness's support is r_A, so the chart has no abstract lift ambiguity.

**THEOREM 2 (fixed-root dual outgoing fan).** For every nonempty A∈F_q(P) with witness word (d_1,...,d_t,b,a), global antipodal reversal produces a REAL (1−q)-monochromatic geodesic beginning at the SAME fixed root y, with direction word
    (a,b,d_t,...,d_1).
Conversely every (1−q)-monochromatic geodesic from y beginning (a,b) and then traversing any A⊆T gives, via global antipodal reversal, a q incoming fan path to bar y, rooted at r_A. Thus F_q(P) is EXACTLY the support family of the (1−q)-monochromatic forward (a,b)-prefixed geodesic fan at y restricted to the unused alphabet T.

**THEOREM 3 (GLOBAL MAXIMUM RANK RESTRICTION).** Since P is chosen to be a GLOBAL maximum-length q-monochromatic geodesic, every nonempty A∈F_q(P) has |A|+2<=k; hence F_q(P) is contained in ranks <=min(m,k−2). In particular if k<(n+2)/2, the TOP support T is impossible for purely maximum-length reasons. This is a genuine upper bound on accessible snake rank, not a proof of a long new path.

**THEOREM 4 (TOP-ONLY EXACT GRAND EXTRACTION).** Suppose the FULL unused set T∈F_q(P). Then its q incoming path B from THE SINGLE ROOT s=r_T=x xor {a,b} to bar y has ordered word (permutation(T),b,a). Let P_s denote the ORIGINAL direction word (permutation(U),a,b), run instead from the SAME root s. If P_s is MONOCHROMATIC of EITHER color, the exact NORI same-root reversed-two-tail splice applies, giving a FULL antipodal at-most-one-switch geodesic in Q_n. Its windows are exactly the two certified monochromatic blocks; no seam guesswork. Under hypothetical grand failure, therefore, for EVERY globally longest q path P with T∈F_q(P), P_s MUST BE NONMONOCHROMATIC. This is the precise two-bit root-slide defect at the TOP rank, now valid for ANY m.

**CRITICAL WRONG SHORTCUT (THE TOP RANK MATTERS).** For PROPER A⊊T, the root r_A and the P-word translated there do NOT satisfy the global antipodal splice geometry. Specifically, P from r_A reaches r_A xor U = y xor (T\A), while global antipodal reversal of the q incoming A-branch starts at bar(bar y)=y. The two points differ by precisely the omitted T\A coordinates. Therefore NO partial one-switch or longer monochromatic path follows by concatenating these two witnesses, and no maximum-length contradiction may be claimed for proper A. Any suggested partial fusion requires a separate real connector across the untraversed coordinates, which is EXACTLY the unresolved topological problem.

**Next research strategy.** The Boolean cube / Johnson layers are not themselves witness-rich: blocked first caps force all rank-one vertices, whereas rank-two edges can be chosen independently by NORI-legal face colors. Seek a genuinely equivariant TOP-RANK extension/Hex theorem for the family of F_q(P) attached to ALL globally maximal mono paths P, not a one-fan claim. Any topological nerve has to encode actual suffix-order memory AND the full-Q_n antipodal face involution; relative complement A↔T\A is insufficient.
