# The ordered-tuple one-change conjecture — preserved pre-item development


## Grand conjecture: tuple arity is the index

Let (Q_V) be the Boolean cube on coordinate set (V), and fix (kge 1).

A **colored (k)-tuple** is an ordered tuple
[
(X_0,ldots,X_{k-1})
]
of (k) consecutive vertices on a cube geodesic. Thus it contains (k-1) cube steps. The project index (k) is always the arity of this colored tuple.

A binary (N_k) coloring assigns
[
chi(X_0,ldots,X_{k-1})in{0,1}
]
to every permitted ordered geodesic (k)-tuple, subject to the active antipodal rule
[
chi(ar X_{k-1},ldots,ar X_0)=1-chi(X_0,ldots,X_{k-1}).
]

For an antipodal geodesic
[
G=(X_0,ldots,X_n),qquad X_n=ar X_0,
]
its (N_k) word is the sliding (k)-tuple word
[
chi(X_0,ldots,X_{k-1}),
chi(X_1,ldots,X_k),
ldots,
chi(X_{n-k+1},ldots,X_n).
]

### Grand Conjecture (N_k)

Every admissible (N_k) coloring has an antipodal geodesic whose sliding (k)-tuple word changes value at most once, equivalently is of the form
[
0^*1^*qquad	ext{or}qquad1^*0^*.
]

### Indexing examples

- (N_1) colors cube vertices.
- (N_2) colors consecutive vertex pairs, i.e. cube edges.
- (N_3) colors consecutive vertex triples, i.e. two-step windows.
- (N_4) colors consecutive vertex quadruples, i.e. three-step windows; the GN3 coordinate-triple model lives here.

### Translation-invariant coordinate form

A (k)-tuple window has (r=k-1) successive flipped coordinates
[
v_1,ldots,v_r.
]
If its color is invariant under global symmetric-difference translation, then it has a coordinate representation
[
chi(X_0,ldots,X_r)=h(v_1,ldots,v_r).
]
Thus an (r)-ary coordinate label (h) belongs to the translation-invariant sector of (N_{r+1}), not (N_r).

Under antipodal reversal this coordinate label satisfies
[
h(v_r,ldots,v_1)=1-h(v_1,ldots,v_r).
]

This (r=k-1) distinction is mandatory throughout NOR: (k) indexes the arity of the colored cube-vertex tuple; (r) may be used for the number of steps or the arity of a reduced coordinate label.


## Provenance: from edge-ordered graphs to directed Norine
Recorded from Caleb's explanation on 2026-10-06.

### The original motivation
The starting question concerns long monotone paths in edge-ordered complete graphs. Represent increasing paths as tight paths in a directed system of ordered triples. A cover by two such paths would force one large monotone path. The rooted variant was tried earlier; Caleb reports that it fails. It is not an assumption of this research route.

The next question is whether coloring directed triples by edge membership versus nonmembership always admits a spanning order with at most one color change. This would yield a two-path cover. Caleb reports that neither this one-change possibility nor the unrooted two-cover possibility had been refuted in the development leading to NOR.

The resemblance to Norine is structural: there are two colors, reversal exchanges them, and the desired spanning object has at most one change. The cube formulation realizes this resemblance rather than merely using it as an analogy.

### Ordered triples encode monotone paths
Let K_V have a strict total ordering lambda of its ordinary edges. Define a directed triple system H by
(a,b,c) in H if and only if lambda(ab)<lambda(bc),
for distinct a,b,c. Its reversal (c,b,a) is in H if and only if lambda(bc)<lambda(ab). Precisely one of each reversal pair is an edge.

A vertex sequence is H-tight precisely when its ordinary edge labels are strictly increasing. A sequence consisting entirely of nonedges of H is strictly decreasing; reversing it gives an increasing path.

Use the binary label h(a,b,c)=0 for edges of H and h(a,b,c)=1 for nonedges. Then h(c,b,a)=1-h(a,b,c).

### Why a spanning one-change order gives a two-cover
Let pi=(v_1,...,v_n) have triple word 0^p1^q, where p+q=n-2. Then
(v_1,...,v_{p+2})
is increasing, and
(v_{p+1},...,v_n)
is decreasing. Reverse the latter to obtain another increasing path. These two paths cover V and overlap in the switching edge v_{p+1}v_{p+2}. The case 1^p0^q exchanges increasing and decreasing.

If a vertex-disjoint two-cover is required, retain the prefix path and remove its two shared vertices from the other path; the remaining suffix is still monotone. Empty or singleton pieces are allowed. Thus the implication also gives a partition into at most two monotone paths.

The overlapping cover has path vertex counts p+2 and q+2, whose sum is n+2. Consequently it supplies a monotone path with at least ceil((n+2)/2) vertices, equivalently at least ceil(n/2) ordinary edges. A disjoint two-cover alone gives at least ceil(n/2) vertices in one path. These conventions should be distinguished when discussing the bound.

Caleb identifies the asymptotic n/2 upper-bound benchmark from the edge-ordered-graph literature as the reason this target is especially attractive: the proposed cover would give the corresponding lower bound. This is recorded as the supplied historical motivation, without a new literature search.

### The cube realization lies at N_4
For four consecutive cube vertices (X_0,X_1,X_2,X_3), let a,b,c be their three successive flipped dimensions. Set
chi(X_0,X_1,X_2,X_3)=h(a,b,c).
This coloring is translation-invariant. Complementing the vertices and reversing their order reverses the dimension list, so
chi(bar(X_3),bar(X_2),bar(X_1),bar(X_0))
=h(c,b,a)
=1-h(a,b,c).

An antipodal cube geodesic flips every dimension once and hence lists a permutation of V. Its sliding four-vertex colors are exactly the edge/nonedge statuses of the corresponding sliding directed triples. An antipodal geodesic with at most one color change therefore yields the two-cover described above.

The implication chain is:
directed N_4 one-change conclusion
=> one-change spanning order in the ordered-triple model
=> two monotone paths covering the edge-ordered complete graph
=> a monotone path with at least ceil(n/2) ordinary edges.

The edge-order model is a subclass of the directed ternary coordinate model: its local comparisons arise from one global ordering of ordinary edges. NOR deliberately permits more general reversal-antisymmetric triple colorings. The purpose of that generalization is to retain the antipodal structure while pursuing a common mechanism for the original monotone-path target and the broader directed path-cover problem.
