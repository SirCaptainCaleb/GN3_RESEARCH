# Q6 closure survives eight antipodal-law defects, or any number on one direction triple

# Robust Q6 closure under eight antipodal-reversal-law defects

Let d be an arbitrary binary coloring of the 960 physical ordered three-face windows (F,pi) of Q_6. Write tau(F,pi)=(bar F,reverse(pi)), a free involution with 480 two-element orbits. An oddness defect is an orbit {u,tau u} with d(u)=d(tau u); let t count such defects. A good full rooted six-geodesic has at most one switch among its four consecutive ordered-face colors.

THEOREM A (eight-defect robustness). If t<=8, d admits a good full rooted six-geodesic. Quantitatively, it has at least

  461 - 2t(t-1) - 20 floor(t^2/4)

distinct good rooted directed full six-geodesics for t<=8. At t=8 this guarantees at least 29 good geodesics.

Proof. Correct each defective tau-orbit by changing the color of precisely one of its two faces, obtaining an antipodal-reversal-odd coloring c. Thus d and c differ at exactly t individual oriented physical faces f_1,...,f_t, one from each defective orbit.

Let X be the 64*720 rooted directed full six-geodesics. Reversing the entire direction order while retaining the root defines a fixed-point-free involution R on X. Because for legal c the four-window word of R(P) is the complemented reversal of the word of P, the c-good geodesics form a union of R-pairs. The quantitative physical theorem [Item nori_q6_922_good_geodesics_pentagon_certificate_20261009] gives at least 461 good R-pairs.

Define A_i={P in X: the ordered physical face f_i is a window of P}, and A=union_i A_i. Any c-good path outside A remains good for d. A good R-pair can lose both good members only if each member intersects A; equivalently it contributes both elements to A intersect R(A).

First compute physical window co-occurrence. For two distinct oriented three-face windows f and g, the number of full rooted six-geodesics containing both is at most 24. Let S,T be their three-direction supports. If |S intersect T|=3, a full direction permutation cannot contain them in two different sliding windows, so the count is zero. If |S intersect T|=2, the windows must be adjacent, and their ordered direction triples must overlap in exactly their common consecutive pair; there are three possible adjacent position pairs, 2! arrangements of the two unused directions, and at most 2^2 root assignments (their common two directions remain free), so at most 24. If |S intersect T|=1, the windows are separated by two positions, giving at most 2*2=4 rooted paths. If S and T are disjoint, they occupy the first and fourth windows and can occur in either temporal order, giving at most 2 rooted paths. These counts use the literal physical fixed-exterior-bit requirements of both ordered faces, and are upper bounds even if the face assignments are incompatible.

We sharpen the 24 bound by controlling which fault pairs can attain it. Write pi_i=(a,b,c) for the ordered direction triple of f_i. Form a simple graph H on the t defects, connecting i,j only if f_i and tau(f_j) can occur as adjacent consecutive three-windows in a full directed six-geodesic (equivalently, their directions have a consistent two-coordinate suffix-prefix overlap, ignoring exterior-bit compatibility). Because the reverse of pi_j is the ordered direction triple of tau(f_j), the neighbors of an ordered triple (a,b,c) in this graph have one of the two forms

  (d,c,b) or (b,a,d),  where d lies outside {a,b,c}.

This graph is TRIANGLE-FREE. Two distinct neighbors of the first form share their final ordered pair (c,b) in the same orientation, and therefore cannot be neighbors of each other: adjacency requires reversal of an ordered consecutive common pair. The same holds for two distinct neighbors of the second form. A neighbor (d,c,b) of the first form and (b,a,e) of the second form share only b unless d=e; when d=e their common directions {b,d} occupy the two nonconsecutive ends of both triples, again excluding adjacency. Hence no triangle is possible.

Let m be the number of edges of H. The elementary triangle-free bound is m<=floor(t^2/4): for any edge uv the neighborhoods of u and v are disjoint, so deg(u)+deg(v)<=t; summing over edges and applying Cauchy gives (2m)^2/t<=sum_v deg(v)^2<=tm.

Now R(A_j) consists exactly of paths containing tau(f_j). For i=j, A_i intersect R(A_i) is empty because f_i and tau(f_i) have the same three-support. For i!=j, if ij is an edge of H the intersection size is at most 24; otherwise its size is at most 4 (at most 4 for overlap one, 2 for disjoint, and zero for incompatible overlap two or identical supports). Hence the union bound yields

  |A intersect R(A)| <= 2*(24m + 4*(C(t,2)-m))
                    = 4t(t-1)+40m
                    <= 4t(t-1)+40 floor(t^2/4).

This intersection is R-invariant; at most half its size counts R-pairs in which both paths are altered. Therefore among the >=461 c-good R-pairs, at least

  461 - 2t(t-1) - 20 floor(t^2/4)

have an unchanged good member. Select one such member per pair. For t<=8 this bound is positive, decreasing to 461-112-320=29 at t=8. Every selected geodesic is good for d. QED.

THEOREM B (single-support robustness, arbitrarily many defects). If every oddness-defect orbit of d has the same underlying unordered three-direction support S, then d has a good full rooted six-geodesic, irrespective of the number of defect orbits.

Proof. Repair the defects by flipping one member of each bad tau-orbit, only on S, obtaining a legal c. Choose a c-good full path P; R(P) is also c-good. Any six-direction order contains at most one consecutive triple with unordered support S. If P avoids all flipped faces, it remains good. Otherwise its unique S-window is a flipped face f, whereas the unique S-window of R(P) is tau(f), the unflipped member of its orbit. All remaining windows have supports different from S and remain unchanged. Hence R(P) stays good for d. QED.

CONDITIONAL HIGHER-DIMENSIONAL CONSEQUENCE. If a six-coordinate subcube of any Q_n coloring has at most eight intrinsic reversal-law defect orbits, Theorem A supplies a good six-direction path inside it. Appending all n-6 remaining directions yields a full n-geodesic with at most n-5 switches (at most two in Q_7). For a globally NORI-odd coloring on Q_7, the intrinsic defects of either facet perpendicular to g correspond to its g-sensitive ordered physical three-faces, grouped in internal antipodal-reversal pairs. This is an exterior-sensitivity criterion for a two-switch path, not a proof of one-switch closure for n>=7.

EXACT FINITE CHECK. Direct enumeration of 46080 rooted directed six-geodesics and 960 oriented physical three-face windows gives individual incidence 192 and maximum co-occurrences 24 (two-support overlap), 4 (one-support overlap), 2 (disjoint supports); the abstract order-adjacency graph on 120 distinct ordered direction triples is 6-regular and triangle-free. The argument above proves the requisite combinatorial bounds independently of enumeration.
