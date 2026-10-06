# Explicit proofs for finite terminal compression

## Metadata

- ID: explicit_proofs_for_finite_terminal_compression
- Parent Section: local_witness_topology_and_the_finite_terminal_theorem
- Position: 3
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Explicit proof package for the finite terminal compression

This addendum supplies the proof material identified as missing by [[independent_audit_finite_terminal_compression_proof_obligations]]. The arguments below are reconstructed from the archived migration proofs, with the failed archived shortcut for the span-two block omitted.

### Five protected positions cannot lie in one face block

Write (h(u,v,w)=1) when ((u,v,w)) is tight. Suppose five consecutive protected vertex positions belong to one face block. Those five vertices may then be placed in every order.

Protection forbids an earlier status (0) together with a later status (1) at distance at least two. Hence every ordering ((a,b,c,d,e)) satisfies
[
h(c,d,e)=1Longrightarrow h(a,b,c)=1.
]

Label the five block vertices (0,1,2,3,4). Using boundary antisymmetry after each implication, the seven admissible reorderings
[
20134, 02431, 13024, 03142, 14203, 14302, 20143
]
give
[
h(102)=1Rightarrow h(134)=0Rightarrow h(024)=1Rightarrow
h(031)=0Rightarrow h(142)=0Rightarrow h(203)=0Rightarrow
h(143)=1Rightarrow h(102)=0.
]
Thus (h(102)=0).

The seven reorderings
[
10234, 01432, 23014, 03241, 24103, 10342, 10243
]
give the reverse implication chain
[
h(102)=0Rightarrow h(234)=0Rightarrow h(014)=1Rightarrow
h(032)=0Rightarrow h(142)=1Rightarrow h(103)=0Rightarrow
h(243)=1Rightarrow h(102)=1,
]
a contradiction. Therefore no face block contains five consecutive protected positions.

### The terminal bridging-block bound

Consider a terminal single-sided configuration with disjoint left and right determining windows. Let (B) be the unique face block coupling the two windows, contributing (alpha) positions to the left window and (eta) positions to the right.

The left witness state depends on an ordered (alpha)-tuple of distinct vertices of (B); the right state depends on an ordered (eta)-tuple. Compatible left/right tuples are disjoint.

If
[
|B|ge alpha+eta+1,
]
the bipartite disjointness graph on ordered (alpha)-tuples and ordered (eta)-tuples is connected: one may replace tuple entries one at a time using the spare vertex while keeping the opposite tuple disjoint. Terminality says that on every compatible pair exactly one of the two witness states occurs. Along a connected bipartite graph this forces each of the two state functions to be constant, contradicting that both reflected orientations occur somewhere in the carrier. Hence
[
|B|le alpha+eta.
]

Conversely, one chamber simultaneously occupies the (alpha+eta) window positions with distinct vertices of (B), so
[
|B|gealpha+eta.
]
Therefore
[
|B|=alpha+eta.
]

Fix the exterior orders and a partition of (B) into the (alpha) vertices used on the left and the (eta) vertices used on the right. Their internal orders vary independently. Since exactly one reflected witness occurs for every such pair of orders, the left witness indicator is constant over all orders of the left support and the right indicator is constant over all orders of the right support.

Suppose a left-witness support had (alphage3). The (alpha) block positions form the inward suffix of the left determining window, so its final three positions form one consecutive triple whose status is prescribed by the forbidden word. Swapping the first and third vertices of that triple preserves the face and the support partition but, by boundary antisymmetry, flips that status. The same left witness therefore cannot remain present, contradiction. Thus (alphale2). Symmetrically (etale2). Hence
[
|B|=alpha+etale4.
]

### The disjoint alternating branch is impossible

Take the nearest alternating type (0101); the complemented type (1010) is symmetric. By the preceding bound,
[
alpha,etale2.
]
In the left four-status witness write the statuses as (s_1,s_2,s_3,s_4). Protection from the closer span-two witness forces
[
s_2=s_4.
]
The first two statuses lie outside (B), so whenever the left (0101) witness occurs, (s_1=0) and (s_2=s_4=1) are fixed on the face.

If (alpha=1), then (s_3) is outside (B) as well, and the left witness is either present in every chamber or absent in every chamber, contrary to the occurrence of both reflected orientations. Hence (alpha=2). The left witness then depends only on the first of the two (B)-vertices in the left suffix. Symmetrically (eta=2), and the right witness depends only on the last (B)-vertex in the right prefix. Therefore (|B|=4).

For a block order ((x,y,z,w)), write (L(x)) and (R(w)) for the left and right witness indicators. Terminality gives
[
L(x)+R(w)=1
]
for every distinct (x,win B). Given (w_1,w_2), choose (x) distinct from both; then
[
R(w_1)=1-L(x)=R(w_2).
]
So (R) is constant, and then (L) is constant, contradicting that both orientations occur. Thus no disjoint alternating terminal branch survives.

### The disjoint span-two branch has block order two

Now take a disjoint terminal span-two branch. The previous result gives
[
|B|in{2,3,4}.
]
The four status positions between the two reflected determining windows avoid all six nearer dual-polarity witnesses, hence are monochromatic in every chamber. Call their common bit (C).

If (|B|=3), then up to symmetry (alpha=1,eta=2). Write a block order as ((x,y,z)). The terminal state depends only on the singleton left support, say (C(x)). The central triples give
[
h(x,y,z)=C(x),qquad h(x,z,y)=C(x).
]
Boundary antisymmetry gives
[
h(y,z,x)=1-C(x).
]
But in the chamber with block order ((y,z,x)), the same central triple equals (C(y)). Hence
[
C(y)=1-C(x)
]
for every distinct (x,y), impossible on three vertices.

If (|B|=4), then (alpha=eta=2). The terminal state depends only on the unordered left support pair, write (C({x,y})). From block orders ((x,y,z,w)) and ((z,y,x,w)), boundary antisymmetry gives
[
C({y,z})=1-C({x,y})
]
for every three distinct (x,y,z). Thus every two edges of (K_4) sharing a vertex must receive opposite (C)-colors. Three edges incident with one vertex make this impossible.

Therefore
[
|B|=2,qquad alpha=eta=1.
]

### The final two-vertex disjoint span-two branch is impossible

In the two-vertex case the four central protected statuses are monochromatic in every chamber, and both colors occur somewhere because both reflected orientations occur. The chamber graph of the face is connected, so along some adjacent Coxeter edge the common central bit changes from (C) to (1-C).

An adjacent transposition changes only the local status coordinates meeting the swapped pair. To change all four central statuses simultaneously, the swap must be the unique central swap of the two bridge vertices. Let (a) be the status immediately to the left of the four central statuses. That bridge swap does not change (a).

In the first endpoint chamber the closer three-bit window is
[
(a,C,C).
]
Avoidance of the dual-polarity span-two witnesses (001,011,110,100) forces (a=C): if (C=0), (a=1) would give (100); if (C=1), (a=0) would give (011).

In the swapped chamber the same closer window is
[
(a,1-C,1-C),
]
and the same argument forces (a=1-C). Contradiction.

Thus no disjoint single-sided span-two terminal branch survives.

### Consequence

Every terminal configuration in the nearest dual-polarity reduction is therefore centered or consists of overlapping/reflected-double determining windows.

For span-two witnesses, the two five-vertex determining windows have reflected start separation at most three, so their union has at most eight vertices. For alternating witnesses, the two six-vertex determining windows have start separation at most four, so their union has at most ten vertices.

Hence every terminal support has order at most ten. The established eight-vertex and ten-vertex two-cover theorems then give path-cover number at most two on every terminal support.

This repairs the proof-material gap in the finite-terminal compression itself. It does **not** by itself settle the separate protected-carrier iteration problem for centered/overlapping terminal faces.

## Frontier

- Development version when composed: None
- Development version now: 1
