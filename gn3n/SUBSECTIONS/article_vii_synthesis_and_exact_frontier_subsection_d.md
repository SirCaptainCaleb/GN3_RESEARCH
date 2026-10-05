# The remaining face-to-cover conversion

## Metadata

- ID: article_vii_synthesis_and_exact_frontier_subsection_d
- Parent Section: article_vii_synthesis_and_exact_frontier
- Position: 4
- Row version: 18
- Development version: 18
- Composition version: 1
- Composition stale: False

## Composition

### Current status of the face-to-cover conversion

The earlier descriptions in this Section of Article VII as closed, and the assertion that no further topological continuation is justified, are superseded by the following precise status. The small-support compression results do not prove a two-cover and do not prove that every obstruction to the grand conjecture has been eliminated. The exact reachability intersection remains unproved.

The bounded-central-block theorem in [[topological_recurrence_to_local_gn3_structure]] gives a uniform reduction within Article VII itself. For a positively balanced exact-root carrier whose chambers all have positive deficiency, either a zero-root chamber occurs or its nonzero-root geometry has one central block of order at most four, exterior blocks of order at most two, at most four consecutive root coordinates, and at most ten actual vertices determining the varying root labels after irrelevant exterior block orders are fixed. The proof uses ordered-partition block freedom and boundary antisymmetry, not minimum-counterexample or disturbance arguments.

This is a finite reduction of one face-geometric branch, not a reduction of the grand conjecture to order ten. Two conversion problems remain. In the diagonal branch, p=c gives equal canonical path lengths but can leave a nonempty hole. In the non-diagonal branch, bounded determining data still have to produce a spanning cover or force a useful change of face.

### Rooted omission vectors

For a spanning order (pi=(L,r,R)) of the auxiliary extension, let (P_pi) be the longest suffix of (L), followed by (r), that is a tight path. Let (Q_pi) be the corresponding rooted path on the right, obtained from the longest initial segment of (R) whose reversal followed by (r) is tight. Define
[
A(pi)=V(L)setminus V(P_pi),qquad
B(pi)=V(R)setminus V(Q_pi),
]
and
[
D(pi)=mathbf 1_{A(pi)}-mathbf 1_{B(pi)}.
]
Reversal exchanges (A) and (B), so (D(pi^{m rev})=-D(pi)). Also (D(pi)=0) exactly when the two rooted tight tails cover every original vertex, which by auxiliary exactification is exactly a spanning two-cover of (H).

Along the chamber order every (D(pi)) has signed threshold form
[
+cdots+,0cdots0, -cdots-.
]
It is never identically positive or identically negative, because an original vertex adjacent to (r) belongs to a two-vertex tight path with (r).

### A dimension-tight quotient map

Let (n=|V(H)|). The boundary of the centered permutahedron on (H^+) is (S^{n-1}). Project the omission vector to
[
mathbb R^{V(H)}/langlemathbf1angle,
]
which also has dimension (n-1). Averaging projected omission vectors on every proper face and extending affinely over the barycentric subdivision gives a continuous odd map. Borsuk--Ulam therefore gives a zero. Its carrier face (F) has strictly positive chamber weights satisfying
[
sum_{piinmathcal V(F)}lambda_pi D(pi)=c,mathbf1
]
for some scalar (c).

This yields a sharper structural frontier:

**Facewise omission-balance problem.** If a proper permutahedral face admits a strictly positive convex combination of rooted omission vectors equal to a constant vector, must it contain a chamber with (D(pi)=0)?

A positive answer proves the two-cover conjecture directly through auxiliary exactification, without minimum-counterexample or disturbance arguments. The extra structure is that each chamber label is a signed prefix/suffix threshold vector of actual omitted vertices and all chambers of (F) arise by independent permutations inside ordered face blocks. The remaining task is therefore an uncrossing or face-convexity problem for threshold omissions inside one ordered partition, not a generic convex-cancellation problem.

The sharper theorem leaves only a two- or four-vertex central block with two singleton witness families supported on the same vertex \(z\), or a three-vertex block with a singleton witness \(\{z\}\) on one side and the full star at \(z\) as the opposite pair family. Moreover, every simple directed root cycle has length two or three. The proof of these sharper bounds sometimes converts a matched pair of tight triples directly into a spanning two-cover; it is therefore stronger than a zero-root argument alone.

The remaining nonzero cases have global deletion distance at most three. This is a consequence under the no-zero-root face hypothesis, not a universal bound on \(\kappa_2(H)\).


### Localization of omission balance and the two exceptional facets

The facewise omission-balance question above has a precise exception. Let the auxiliary vertex be \(r\), let \(V=V(H)\), and use the rooted omission vectors \(D(\pi)\) just defined. In the chamber order their entries on original vertices have the form
\[
+\cdots+,\,0\cdots0,\,-\cdots-.
\]
In particular, if original vertices \(u,v\) lie in distinct ordered face blocks with the block of \(u\) earlier, then
\[
D(\pi)_u\ge D(\pi)_v
\]
for every chamber of that face.

**Proposition (localization to the two exceptional facets).** Let \(F\) be a proper face of the permutahedron on \(V\cup\{r\}\). Suppose
\[
\sum_{\pi\in\mathcal V(F)}\lambda_\pi D(\pi)=c\mathbf1,
\qquad \lambda_\pi>0,\quad \sum_\pi\lambda_\pi=1.
\]
If \(F\) is neither \(\{r\}\mid V\) nor \(V\mid\{r\}\), then \(D(\pi)=0\) for every chamber of \(F\).

**Proof.** If original vertices occur in at least two face blocks, the displayed coordinate inequality and equality of coordinate averages imply
\[
D(\pi)_u=D(\pi)_v
\]
for every chamber and every pair in different original-vertex blocks. Positivity of every coefficient is essential here. Using any vertex in a second block also equates two coordinates in the same block. Thus every chamber vector is constant on all original vertices.

At least one original vertex is adjacent to \(r\) in each chamber and belongs to a rooted tight path of order two. Its omission coordinate is zero. Therefore the constant vector is zero.

If all original vertices occur in one block, a proper face can have only that block and the singleton block \(\{r\}\), in either order. These are exactly the two excluded facets. \(\square\)

Thus, under the assumption that \(H\) has no two-cover, every zero of the projected omission map must have one of the two exceptional facets as its carrier. The Borsuk--Ulam conclusion by itself does not exclude this possibility.

**Example (the exceptional facets really can balance).** Identify four original vertices with \(\mathbb F_2^2\). Order the three nonzero differences as \(d_1<d_2<d_3\), and give the ordinary edge \(\{x,y\}\) the class of \(x+y\). Declare
\[
(x,y,z)\text{ tight}\quad\Longleftrightarrow\quad
\operatorname{class}(x+y)<\operatorname{class}(y+z).
\]
The two classes are different, so boundary reversal complements tightness. This is the matching-block boundary tournament.

It has no tight Hamilton path. Such a path would have three successive, strictly increasing edge classes, hence differences \(d_1,d_2,d_3\). Their sum is zero in \(\mathbb F_2^2\), so its final vertex would equal its initial vertex. This contradicts distinctness. It does, of course, have a two-cover by two pairs.

On the facet \(\{r\}\mid V\), the left rooted path is the singleton \(r\). The right rooted path covers either two or three original vertices; it never covers four because that would give a tight Hamilton path of \(H\). Hence no chamber of this facet has \(D=0\).

Translations of \(\mathbb F_2^2\) preserve edge classes and act transitively on original vertices. The uniform average of \(D\) over all chambers of this facet is therefore a constant vector. Exactly half the orders have a non-tight first original triple, allowing the reversed rooted prefix to cover three original vertices; the other half cover only two. Thus the average number omitted is \(3/2\), and
\[
\frac1{4!}\sum_{\pi\in\mathcal V(\{r\}\mid V)}D(\pi)
=-\frac38\mathbf1.
\]
All weights are strictly positive. Reversal gives the opposite constant on \(V\mid\{r\}\).

This refutes the universal facewise implication proposed above: strictly positive projected omission balance need not yield a zero chamber in the same face. It does not refute the grand conjecture. The viable strengthened target is to force a projected zero outside the two exceptional facets, or to extract a two-cover directly from balance on an exceptional facet. The localization proposition proves the first target sufficient; the example shows why the second cannot demand a Hamilton path.


### Facewise omission balance collapses to the two extreme auxiliary facets

Retain the rooted omission notation
\[
D(\pi)={\bf1}_{A(\pi)}-{\bf1}_{B(\pi)}
\]
on spanning orders \(\pi=(L,r,R)\) of \(H^+\). Thus \(A(\pi)\) is a prefix of \(L\), \(B(\pi)\) is a suffix of \(R\), and \(D(\pi)=0\) is exactly a two-cover certificate for \(H\).

Let
\[
F=C_1|\cdots|C_t
\]
be a nonempty proper permutahedron face, and suppose \(r\in C_j\). Assume there are strictly positive weights
\[
\lambda_\pi>0\qquad(\pi\in\mathcal V(F)),\qquad
\sum_\pi\lambda_\pi=1,
\]
such that
\[
\sum_\pi\lambda_\pi D(\pi)=c\,{\bf1}
\]
for some scalar \(c\).

**Theorem (facewise omission reduction).**
If \(F\) is not one of the two extreme facets
\[
\{r\}|V(H),
\qquad
V(H)|\{r\},
\]
then \(F\) contains a chamber \(\pi\) with
\[
D(\pi)=0.
\]
In fact, except for a terminal two-block configuration with the auxiliary block containing original vertices, the argument forces \(D=0\) in every chamber of \(F\); that remaining terminal configuration also collapses by the probability argument below.

**Proof.**

First suppose
\[
1<j<t.
\]
Every original vertex in a block before \(C_j\) is always left of \(r\), hence its \(D\)-coordinate is in \(\{0,1\}\). Every original vertex in a block after \(C_j\) has coordinate in \(\{0,-1\}\). Since all weighted coordinate averages equal \(c\), both sides force
\[
c=0.
\]
Strict positivity of all \(\lambda_\pi\) then implies that every original vertex outside \(C_j\) has \(D\)-coordinate \(0\) in every chamber.

If some chamber had \(A(\pi)\ne\varnothing\), then, because \(A(\pi)\) is a prefix of \(L\) and there is a whole face block before \(C_j\), the first original vertex of the chamber would lie in \(A(\pi)\), contradicting its identically zero coordinate. Hence \(A(\pi)=\varnothing\) for every chamber. The symmetric suffix argument gives \(B(\pi)=\varnothing\). Thus every chamber has \(D=0\).

Now suppose \(j=1\); the case \(j=t\) is symmetric. Every original vertex outside \(C_1\) has coordinate in \(\{0,-1\}\), so
\[
c\le0.
\]
If \(c=0\), strict positivity makes every outside coordinate identically zero. A nonempty suffix \(B(\pi)\) would contain the last original vertex of the chamber, which lies outside \(C_1\), a contradiction. Thus \(B(\pi)=\varnothing\) for every chamber. The remaining coordinates are then nonnegative, have average zero, and hence \(A(\pi)=\varnothing\) as well.

Assume therefore
\[
c=-W<0.
\]

If \(C_1\ne\{r\}\), choose
\[
x\in C_1-\{r\}.
\]
Let \(E\) be the event, under the positive weights \(\lambda\), that every original vertex outside \(C_1\) belongs to \(B(\pi)\), and write its total weight as \(e\).

For every outside vertex \(y\),
\[
D_y=-{\bf1}_{\{y\in B\}},
\]
so its average \(-W\) gives
\[
\Pr_\lambda(y\in B)=W.
\]
Since \(E\subseteq\{y\in B\}\),
\[
e\le W.
\]

Write
\[
a_x=\Pr_\lambda(x\in A),
\qquad
b_x=\Pr_\lambda(x\in B).
\]
If \(x\in B(\pi)\), the suffix property forces every later outside vertex into \(B(\pi)\), hence
\[
\{x\in B\}\subseteq E
\]
and therefore
\[
b_x\le e.
\]
The balance equation at coordinate \(x\) is
\[
a_x-b_x=-W,
\]
so
\[
b_x=a_x+W\ge W.
\]
Consequently
\[
W\le b_x\le e\le W.
\]
Thus
\[
a_x=0,\qquad b_x=e=W.
\]

The same argument holds for every \(x\in C_1-\{r\}\). Hence on every chamber in \(E\), all original vertices of \(C_1\) and all outside vertices belong to \(B(\pi)\): every original vertex of \(H\) is omitted on the right. This is impossible, because whenever \(R\ne\varnothing\), the first vertex of \(R\) together with \(r\) is a two-vertex tight path, so the rooted right path \(Q_\pi\) always contains at least that vertex.

Thus \(c<0\) is impossible whenever \(C_1\ne\{r\}\).

It remains only
\[
C_1=\{r\}.
\]
If \(t\ge3\), choose vertices \(u\in C_i\), \(v\in C_j\) with
\[
2\le i<j\le t.
\]
Because \(B(\pi)\) is a suffix of \(R\),
\[
{\bf1}_{\{u\in B\}}\le{\bf1}_{\{v\in B\}}
\]
in every chamber. Their weighted expectations are both \(W\), so strict positivity forces equality chamberwise. Varying \(u,v\) shows that in every chamber either every original vertex is in \(B\) or none is. The former is impossible by the immediate-neighbor observation, while the latter contradicts \(W>0\).

Therefore the only unresolved case with \(j=1\) is
\[
F=\{r\}|V(H).
\]
The symmetric argument leaves only
\[
F=V(H)|\{r\}.
\]
This proves the theorem. \(\square\)

### The reduction is sharp at the level of convex cancellation

The two exceptional facets cannot be discarded by a generic convexity argument. On the facet
\[
\{r\}|V(H),
\]
one has
\[
D(\pi)=-{\bf1}_{B(\pi)},
\]
where \(B(\pi)\) is the suffix omitted after the maximal rooted right path.

For a standard non-Hamiltonian four-vertex matching-block boundary tournament, the uniform distribution on all \(24\) permutations gives
\[
\Pr(v\in B)=\frac38
\]
for every vertex \(v\), while no permutation has \(B=\varnothing\). Thus
\[
\frac1{24}\sum_\pi D(\pi)
=
-\frac38\,{\bf1}
\]
is a genuine full-support constant balance with no zero chamber.

Accordingly, the facewise omission theorem is sharp:
\[
\boxed{
\text{all non-extreme carrier faces close;}
\quad
\text{the only genuine convex-cancellation residue is the pair of extreme facets.}
}
\]

The remaining global topological question is therefore whether an odd zero of the quotient omission map can be supported entirely by those two antipodal extreme facets when the whole tournament has no two-cover. Local averaging alone cannot answer this.

### The exceptional facets carry essential degree

The matching-block example above shows that the two exceptional facets can support projected omission balance without a zero chamber. In a hypothetical counterexample, the limitation is stronger: the projected omission map is topologically forced to have a zero in the interior of each exceptional facet.

Let
\[
F^-=\{r\}\mid V(H)
\]
be the left exceptional facet. It is canonically a copy of the centered permutahedron \(P_V\) on the original vertex set, of dimension \(n-1\). Its boundary is therefore an \((n-2)\)-sphere.

On \(F^-\), every omission vector has the form
\[
D(\pi)=-\mathbf 1_{B(\pi)},
\]
where \(B(\pi)\) is a suffix of the original-vertex order. Hence, if
\[
G=B_1|\cdots|B_t
\]
is any proper face of \(P_V\), and \(u\in B_i,\ v\in B_j\) with \(i<j\), then
\[
D(\pi)_u\ge D(\pi)_v
\]
for every chamber \(\pi\) of \(G\). The same inequalities hold for the face-average omission vector assigned to the barycenter of \(G\), and therefore throughout every barycentric simplex whose largest face is \(G\).

Write
\[
Q=\mathbb R^{V(H)}/\langle\mathbf 1\rangle
\]
and, for an ordered partition \(G\), let
\[
C_G=
\left\{
[y]\in Q:
y_u\ge y_v
\text{ whenever }
u\in B_i,\ v\in B_j,\ i<j
\right\}.
\]
Thus the projected omission map on the barycentric subdivision of \(\partial P_V\) is carried by the spherical carrier
\[
K_G=(C_G\setminus\{0\})/\mathbb R_{>0}.
\]

Assume now that \(H\) has no spanning two-cover. By the facewise omission theorem above, the projected omission map has no zero on \(\partial F^-\): any zero there would have a proper nonexceptional carrier face in the full auxiliary permutahedron and would force an actual chamber with \(D=0\).

Each \(K_G\) is contractible. Indeed \(C_G\) is a proper convex cone; after quotienting its lineality space, the pointed part has a spherically convex section, and \(K_G\) is the join of that section with the sphere of the lineality space.

Compare the normalized omission map on \(\partial P_V\) with
\[
h(x)=-\frac{x}{\|x\|}.
\]
If \(x\) lies in the permutahedron face \(G\), then the coordinates of \(x\) increase from earlier to later blocks, so the coordinates of \(-x\) decrease from earlier to later blocks. Therefore
\[
h(G)\subseteq K_G.
\]
The normalized omission map is carried by the same acyclic carrier. The acyclic carrier theorem makes the two maps homotopic.

Consequently
\[
\deg(\widehat D|_{\partial F^-})
=
\deg(h)
=
(-1)^{n-1},
\]
up to the harmless orientation convention for \(Q\). In particular the degree has absolute value one.

Every continuous extension of this boundary map over the exceptional facet \(F^-\) must therefore hit the origin. The barycentric omission map is such an extension, so \(F^-\) contains an interior projected omission zero. Reversal gives the same conclusion for
\[
F^+=V(H)\mid\{r\}.
\]

Thus in a hypothetical counterexample the two exceptional facets do not merely permit topological cancellation:
\[
\boxed{
\text{each exceptional facet carries an essential degree-one omission zero.}
}
\]

This sharpens the limitation of the rooted omission projection. The global Borsuk--Ulam zero can be absorbed by the two extreme facets for a structural degree reason. Therefore a continuation that uses only the same projected omission map and the same quotient target cannot force a useful nonexceptional zero; additional information or a genuinely different target is required.


### The exact violation map escapes the exceptional omission facets

The omission projection fails for a topologically structural reason on the two extreme auxiliary facets, but the exact auxiliary violation vector behaves differently.

Let \(n=|V(H)|\), so the auxiliary tournament \(H^+\) has \(n+1\) vertices and the boundary of its centered permutahedron is
\[
S^{n-1}.
\]
Use the odd violation vector
\[
F(\pi)=(F_d(\pi))_{1\le d\le n-2}
\]
from [[auxiliary_violation_vector_has_exact_chamber_zeros]], where
\[
F_d=x_d-y_d+g\,x_dy_d.
\]
Its chamber zeros are exactly directed one-change orders and therefore exactly two-cover certificates for \(H\).

Average \(F\) over every proper face and extend affinely on the barycentric subdivision. This gives a continuous odd map
\[
\mathcal F:S^{n-1}\longrightarrow\mathbb R^{n-2}.
\]
Bourgin--Yang therefore gives
\[
\dim \mathcal F^{-1}(0)\ge1.
\]
Every zero has the usual positive carrier-face expansion:
\[
\sum_{\pi\in\mathcal V(C)}\lambda_\pi F(\pi)=0,
\qquad
\lambda_\pi>0.
\]

Now consider the exceptional facet
\[
C^-=\{r\}\mid V(H).
\]
Here \(r\) is first in every chamber. There are no left violations, so
\[
x_d=0,\qquad F_d=-y_d\in\{0,-1\}
\]
for every chamber and every distance \(d\). If a positive convex combination of these vectors were zero, every coordinate of every chamber vector would have to vanish. Thus every chamber in the carrier would satisfy
\[
F(\pi)=0,
\]
which is already a directed one-change order and hence a two-cover of \(H\).

Therefore, under the counterexample hypothesis,
\[
\mathcal F^{-1}(0)\cap C^-=\varnothing.
\]
By reversal,
\[
\mathcal F^{-1}(0)\cap C^+=\varnothing,
\qquad
C^+=V(H)\mid\{r\}.
\]

Hence:
\[
\boxed{
\text{if }H\text{ has no two-cover, every zero carrier of the exact violation map is nonexceptional.}
}
\]

This contrasts sharply with the projected omission map, whose two exceptional facets carry essential degree-one zeros. The violation map therefore genuinely escapes Astra's exceptional-facet obstruction.

The remaining gap is different: positive balance of the violation vectors on a nonexceptional face does not yet imply that one chamber has \(F=0\). The next structural target is a facewise conversion theorem for these positional violation vectors, ideally using fixed-center intermediate value and the fact that the zero locus has positive dimension.


### A side-set gauge and exact closure on singleton-\(r\) carrier faces

The coordinatewise gauge in the exact violation vector can be replaced by one global double-violation coordinate in a way that is better adapted to faces.

Let the original vertex set be \(V\), let \(r\) be the auxiliary vertex, and for a spanning order \(\pi\) write
\[
L_r(\pi)=\{v\in V:v\text{ occurs left of }r\},
\qquad
R_r(\pi)=V\setminus L_r(\pi).
\]
Fix once and for all a total order \(\prec\) on subsets of \(V\). Define an antipodal sign \(g_{\rm set}\) by
\[
g_{\rm set}(\pi)=
\begin{cases}
+1,&|L_r(\pi)|<|R_r(\pi)|,\\
-1,&|L_r(\pi)|>|R_r(\pi)|,\\
+1,&|L_r|=|R_r|\text{ and }L_r\prec R_r,\\
-1,&|L_r|=|R_r|\text{ and }R_r\prec L_r.
\end{cases}
\]
Reversal exchanges \(L_r\) and \(R_r\), hence
\[
g_{\rm set}(\pi^{\rm rev})=-g_{\rm set}(\pi).
\]

For the left/right violation bits \(x_d,y_d\) of [[auxiliary_violation_vector_has_exact_chamber_zeros]], define
\[
A_d(\pi)=x_d(\pi)-y_d(\pi),
\]
and choose arbitrary positive weights \(w_d>0\). Put
\[
B(\pi)
=
g_{\rm set}(\pi)\sum_d w_d x_d(\pi)y_d(\pi).
\]
Then
\[
\Theta(\pi)=\bigl((A_d(\pi))_d,B(\pi)\bigr)
\]
is odd. Its target has dimension \(n-1\), equal to the dimension of the auxiliary Coxeter sphere.

Moreover
\[
\Theta(\pi)=0
\]
if and only if \(\pi\) has no violations. Indeed \(A_d=0\) gives \(x_d=y_d\) at every distance, while \(B=0\), since \(g_{\rm set}=\pm1\) and all \(w_d>0\), forces
\[
x_dy_d=0
\]
for every \(d\). Thus \(x_d=y_d=0\) for all \(d\).

Average \(\Theta\) on proper face barycenters and extend affinely. Borsuk--Ulam gives a zero and the usual strictly positive expansion over every chamber of its carrier face.

The key advantage of \(g_{\rm set}\) is the following.

**Theorem (singleton-\(r\) carrier conversion).**
Let
\[
C=C_1|\cdots|C_t
\]
be a proper permutahedron face in which
\[
C_j=\{r\}.
\]
Suppose there are strictly positive weights
\[
\lambda_\pi>0\qquad(\pi\in\mathcal V(C))
\]
with
\[
\sum_\pi\lambda_\pi\Theta(\pi)=0.
\]
Then every chamber of \(C\) is violation-free. In particular \(H\) has a spanning two-cover.

**Proof.**
Because \(r\) is a singleton block, the set of original vertices left of \(r\) and the set right of \(r\) are fixed throughout \(C\). Hence
\[
g_{\rm set}(\pi)=g_0\in\{\pm1\}
\]
is constant on all chambers of \(C\).

The last coordinate of the positive balance is therefore
\[
0
=
g_0\sum_\pi\lambda_\pi\sum_d w_dx_d(\pi)y_d(\pi).
\]
Every summand inside the last sum is nonnegative, every \(w_d\) is positive, and every \(\lambda_\pi\) is positive. Hence
\[
x_d(\pi)y_d(\pi)=0
\]
for every chamber \(\pi\) and every distance \(d\).

Now fix \(d\). Since \(r\) is a singleton block, the chamber set factors as
\[
\mathcal V(C)
=
\mathcal L\times\mathcal R,
\]
where \(\mathcal L\) consists of the independent permutations in blocks left of \(r\), and \(\mathcal R\) those right of \(r\). The bit \(x_d\) depends only on the left factor and \(y_d\) only on the right factor.

If some left factor had \(x_d=1\) and some right factor had \(y_d=1\), their product chamber would satisfy
\[
x_dy_d=1,
\]
contrary to the preceding paragraph. Therefore at least one of the two functions is identically zero on its factor.

But the \(A_d\)-coordinate of the positive balance says
\[
\sum_\pi\lambda_\pi x_d(\pi)
=
\sum_\pi\lambda_\pi y_d(\pi).
\]
If one side is identically zero, positivity forces the other side to be identically zero as well. Hence
\[
x_d(\pi)=y_d(\pi)=0
\]
for every chamber. Since \(d\) was arbitrary, every chamber of \(C\) is violation-free. \(\square\)

Thus the exact violation map has no unresolved singleton-\(r\) carrier geometry at all:
\[
\boxed{
\text{positive }\Theta\text{-balance on a face with }\{r\}\text{ as a block}
\Longrightarrow
\text{an actual two-cover certificate}.
}
\]

Consequently, under the counterexample hypothesis, every zero carrier of the \(\Theta\)-map must place \(r\) in a block containing at least one original vertex. This eliminates the central singleton case as well as the two extreme singleton facets; the only remaining face-to-cover obstruction is genuinely the geometry of a nontrivial \(r\)-block.


### Constant-gauge nontrivial \(r\)-blocks collapse to order four

The previous theorem handles faces in which \(\{r\}\) is already a block. Now let
\[
C=C_1|\cdots|C_t
\]
be a proper carrier face with
\[
r\in C_j,
\qquad
W=C_j\setminus\{r\}\ne\varnothing.
\]
Assume the side-set gauge \(g_{\rm set}\) has the same sign on every chamber of \(C\), and suppose
\[
\sum_{\pi\in\mathcal V(C)}\lambda_\pi\Theta(\pi)=0,
\qquad
\lambda_\pi>0.
\]
Assume for contradiction that \(H\) has no two-cover.

For \(S\subseteq W\), let \(\mathcal C_S\) be the chambers in which precisely the vertices of \(S\) occur before \(r\) inside the block \(C_j\). Equivalently \(\mathcal C_S\) is the chamber set of the refinement
\[
C_1|\cdots|C_{j-1}|S|\{r\}|(W\setminus S)|C_{j+1}|\cdots|C_t,
\]
with empty blocks omitted.

Because the gauge is constant on all of \(C\), the final coordinate of the positive balance forces
\[
u(\pi)v(\pi)=0
\]
for every chamber, where
\[
u(\pi)={\bf1}\{\text{some left violation occurs}\},
\qquad
v(\pi)={\bf1}\{\text{some right violation occurs}\}.
\]
Indeed one may use this stronger mixed-side term in place of
\(\sum_d w_dx_dy_d\):
\[
B_{\rm mix}(\pi)=g_{\rm set}(\pi)u(\pi)v(\pi).
\]
Together with the coordinates
\[
A_d=x_d-y_d,
\]
the chamber zero set is still exactly the directed one-change orders.

Thus, under the counterexample hypothesis, every chamber of \(C\) is of exactly one of two types:
\[
L:\quad u=1,\ v=0,
\qquad
R:\quad u=0,\ v=1.
\]

**Lemma (fiber constancy).**
For each \(S\subseteq W\), every chamber of \(\mathcal C_S\) has the same type.

**Proof.**
The chamber graph of \(\mathcal C_S\) is connected and uses only adjacent transpositions that do not move \(r\). Such a transposition occurs entirely on one side of \(r\), so it can change only left violations or only right violations. Hence an \(L\)-chamber cannot move in one step to an \(R\)-chamber: changing the left side can only keep type \(L\) or create a zero chamber, while changing the right side can only keep type \(L\) or create a mixed chamber. Both alternatives are excluded. \(\square\)

The \(A_d\)-balance and positivity imply that both fiber types occur. Indeed if all chambers were \(L\), every \(A_d\)-average would be nonnegative and at least one would be positive; similarly for \(R\).

The Boolean cube on subsets of \(W\) is connected, so there are adjacent subsets
\[
S,\qquad S'=S\cup\{z\}
\]
whose fibers have opposite types. Choose orders so that \(z\) is immediately after \(r\) in a chamber
\[
\pi\in\mathcal C_S
\]
and swap \(r,z\) to obtain
\[
\pi'\in\mathcal C_{S'}.
\]
After reversing the labels \(L,R\) if necessary, assume \(\pi\) is \(L\) and \(\pi'\) is \(R\).

Moving \(r\) one step to the right gives the exact remote-profile transport identities
\[
x_{d+1}(\pi')=x_d(\pi),
\qquad
y_d(\pi')=y_{d+1}(\pi)
\qquad(d\ge1).
\]
Since \(\pi\) has no right violations and \(\pi'\) has no left violations, the opposite orientation of the crossing edge is forced: equivalently, reading the edge from the \(L\)-fiber to the \(R\)-fiber moves \(r\) one step to the **left**. In that orientation,
\[
x_d(\pi')=x_{d+1}(\pi),
\qquad
y_{d+1}(\pi')=y_d(\pi)
\qquad(d\ge1),
\]
and the only newly exposed coordinate is \(y_1(\pi')\).

Therefore
\[
x_d(\pi)=0\quad(d\ge2),
\qquad
y_d(\pi')=0\quad(d\ge2).
\]
Because \(\pi\) is \(L\) and \(\pi'\) is \(R\),
\[
x_1(\pi)=1,
\qquad
y_1(\pi')=1.
\]
Thus an opposite-type fiber edge has the rigid profile
\[
\boxed{
\pi:\ x_1=1,\ x_{d\ge2}=0,\ y_d=0;
\qquad
\pi':\ y_1=1,\ y_{d\ge2}=0,\ x_d=0.
}
\]

Now use the fact that an entire fiber has one type. In an \(L\)-fiber, the complete right side is violation-free for every permutation allowed by the fiber. If any free block wholly to the right of \(r\) had order at least three, choose three consecutive positions inside that block and swap the first and third vertices. Boundary antisymmetry flips the corresponding right status, contradicting universal right cleanliness. Hence every right-side block in an \(L\)-fiber has order at most two.

Similarly, every left-side block in an \(R\)-fiber has order at most two.

Apply this to the adjacent fibers above. In the \(L\)-fiber the block
\[
W\setminus S
\]
lies immediately to the right of \(r\), so
\[
|W\setminus S|\le2,
\]
and every original face block after \(C_j\) has order at most two. In the \(R\)-fiber the block
\[
S'=S\cup\{z\}
\]
lies immediately to the left of \(r\), so
\[
|S|+1\le2,
\]
and every original face block before \(C_j\) has order at most two.

Consequently
\[
|S|\le1,
\qquad
|W\setminus S|\le2,
\qquad
|W|\le3.
\]
Thus
\[
\boxed{|C_j|\le4,}
\]
and every other block of \(C\) has order at most two.

So the constant-gauge branch of the exact violation map has no unbounded face geometry:
\[
\boxed{
\text{constant }g_{\rm set}
\Longrightarrow
\text{all exterior blocks have order }\le2
\text{ and the }r\text{-block has order }\le4.
}
\]
The only uncompressed branch is therefore the one in which \(g_{\rm set}\) changes sign inside the \(r\)-block, i.e. the block crosses the global side-set median.


### Map distinction

For clarity, two closely related full-dimensional exact maps are in use.

The first is
\[
\Theta_{\rm eq}(\pi)
=
\left(
(A_d(\pi))_d,\ 
g_{\rm set}(\pi)\sum_d w_dx_d(\pi)y_d(\pi)
\right),
\]
which records equal-radius double violations.

For the constant-gauge block-collapse argument, use instead
\[
\Theta_{\rm mix}(\pi)
=
\left(
(A_d(\pi))_d,\ 
g_{\rm set}(\pi)u(\pi)v(\pi)
\right),
\]
where
\[
u={\bf1}\{\exists d:x_d=1\},
\qquad
v={\bf1}\{\exists d:y_d=1\}.
\]

Both maps are odd, both take values in \(\mathbb R^{n-1}\), and both have chamber zero set exactly equal to the directed one-change orders. Borsuk--Ulam and the positive carrier expansion apply separately to each map. The singleton-\(r\) conversion is valid for either map. The nontrivial constant-gauge block-collapse theorem above is to be read for a positive carrier of
\[
\Theta_{\rm mix}.
\]


### Nearest-violation Tucker compression

There is a lower-information exact label that is particularly well adapted to Tucker-style arguments.

Assume \(H\) has no two-cover, so every spanning order of the auxiliary extension \(H^+\) has at least one violation. For a chamber \(\pi\), let
\[
d_0(\pi)
=
\min\{d\ge1:x_d(\pi)=1\text{ or }y_d(\pi)=1\}.
\]
At the nearest violating radius there are three possibilities:
\[
(1,0),\qquad(0,1),\qquad(1,1).
\]

Use the side-set antipodal gauge \(g_{\rm set}\) above, and define a signed label
\[
\ell(\pi)\in
\{\pm1,\ldots,\pm(n-2),\pm\star\}
\]
by
\[
\ell(\pi)=
\begin{cases}
+d_0,&(x_{d_0},y_{d_0})=(1,0),\\
-d_0,&(x_{d_0},y_{d_0})=(0,1),\\
g_{\rm set}(\pi)\star,&(x_{d_0},y_{d_0})=(1,1).
\end{cases}
\]
Identify the \(n-1\) unsigned labels
\[
1,\ldots,n-2,\star
\]
with the coordinate vectors of \(\mathbb R^{n-1}\), and write \(L(\pi)\) for the corresponding signed basis vector.

Reversal preserves the nearest violating radius, exchanges left and right, and negates \(g_{\rm set}\). Hence
\[
L(\pi^{\rm rev})=-L(\pi).
\]

Average \(L\) over the chambers of every nonempty proper face and extend affinely over the barycentric subdivision.

**Theorem (nearest-violation Tucker carrier).**
The resulting map
\[
\mathcal L:S^{n-1}\longrightarrow\mathbb R^{n-1}
\]
is continuous and odd. Hence it has a zero. If \(C\) is the carrier face of such a zero, then there are strictly positive coefficients
\[
\lambda_\pi>0\qquad(\pi\in\mathcal V(C))
\]
with
\[
\sum_{\pi\in\mathcal V(C)}\lambda_\pi L(\pi)=0.
\]
Consequently every signed label occurring among the chambers of \(C\) occurs with both signs. In particular:

- if \(+d\) occurs, then \(-d\) occurs;
- if \(+\star\) occurs, then \(-\star\) occurs.

**Proof.**
Oddness and Borsuk--Ulam give a zero. The positive carrier expansion is the same smallest-barycentric-simplex argument used throughout Article VII. Since the vectors \(L(\pi)\) are signed coordinate vectors and every chamber of the carrier has positive coefficient, the vanishing of each coordinate forces positive mass on both signs of every unsigned label that occurs. \(\square\)

This gives a sharp dichotomy.

**Corollary (protected-radius or median-mixed dichotomy).**
A carrier \(C\) as above satisfies one of the following.

1. **Protected-radius branch.** No \(\star\)-label occurs. Let \(d\) be the smallest ordinary label occurring in \(C\). Then every chamber of \(C\) has
   \[
   x_j=y_j=0
   \qquad(1\le j<d),
   \]
   and \(C\) contains both a chamber with
   \[
   (x_d,y_d)=(1,0)
   \]
   and a chamber with
   \[
   (x_d,y_d)=(0,1).
   \]

2. **Median-mixed branch.** A \(\star\)-label occurs. Then \(C\) contains nearest-radius double-violation chambers on both gauge signs:
   \[
   g_{\rm set}=+1
   \qquad\text{and}\qquad
   g_{\rm set}=-1.
   \]

In the first branch, minimality of \(d\) gives the protected-radius hypothesis on **every** chamber of the carrier, not merely on the two opposite witnesses. If \(r\) is a singleton block, [[fixed_center_violation_intermediate_value]] applies directly and forces either larger protected radius or a double violation at radius \(d\). Iterating therefore reaches either a violation-free chamber or the second branch.

Thus the remaining nontrivial topology can be localized to the median-mixed branch: one face contains double violations at the nearest radius on both sides of the antipodal side-set wall.


### Protected radius at least two forces a tiny \(r\)-block

Let \(C=C_1|\cdots|C_t\) be any proper face of the auxiliary permutahedron, with
\[
r\in C_j.
\]
Suppose every chamber of \(C\) has no violation at radius \(1\):
\[
x_1(\pi)=y_1(\pi)=0
\qquad(\pi\in\mathcal V(C)).
\]

**Lemma (radius-one rigidity).**
Then
\[
|C_j|\le3.
\]
Moreover, when the neighboring blocks exist,
\[
|C_{j-1}|\le2,
\qquad
|C_{j+1}|\le2.
\]

**Proof.**
Write
\[
W=C_j\setminus\{r\}.
\]
If \(|W|\ge3\), place \(r\) last in its block and choose three vertices of \(W\) in the three positions immediately before \(r\). Since \(x_1=0\), their ordered triple must be tight. Reversing those three vertices while keeping every other block order fixed gives another chamber of \(C\), but boundary antisymmetry makes the reversed triple non-tight, contradicting \(x_1=0\). Hence
\[
|W|\le2,
\]
so \(|C_j|\le3\).

If \(|C_{j-1}|\ge3\), place \(r\) first in \(C_j\). The three positions immediately before \(r\) may then be filled by any ordered triple from the end of \(C_{j-1}\). The same reversal argument contradicts \(x_1=0\). Thus \(|C_{j-1}|\le2\).

The right-hand statement is symmetric: place \(r\) last in \(C_j\). If \(|C_{j+1}|\ge3\), arbitrary reversal of the first three vertices of \(C_{j+1}\) flips the immediate right status, contradicting \(y_1=0\). \(\square\)

Apply this to a nearest-violation Tucker carrier. Let
\[
d_{\min}
=
\min_{\pi\in\mathcal V(C)}d_0(\pi).
\]

**Corollary.**
If
\[
d_{\min}\ge2,
\]
then the carrier has
\[
|C_j|\le3,
\qquad
|C_{j\pm1}|\le2
\]
for the existing neighboring blocks.

Thus every carrier with a large nontrivial \(r\)-block necessarily satisfies
\[
\boxed{d_{\min}=1.}
\]

This conclusion is independent of which signed nearest label realizes the minimum. It uses only the universal protected-radius statement
\[
x_1=y_1=0
\]
on the carrier. Hence the genuinely unbounded branch of the nearest-violation Tucker program is localized to the first uncontrolled triples immediately outside the forced auxiliary junction.


### The first active exact-violation coordinate

The same radius localization follows directly from the coordinatewise exact violation map, without the nearest-label compression.

Let
\[
F(\pi)=(F_1(\pi),\ldots,F_{n-2}(\pi))
\]
be the odd exact violation vector from [[auxiliary_violation_vector_has_exact_chamber_zeros]], and let \(C\) be the carrier face of a zero with strictly positive chamber weights:
\[
\sum_{\pi\in\mathcal V(C)}\lambda_\pi F(\pi)=0,
\qquad
\lambda_\pi>0.
\]
Assume \(H\) has no two-cover, so no chamber has \(F(\pi)=0\).

Define the **first active radius**
\[
d(C)
=
\min\{d:\exists\pi\in\mathcal V(C)\text{ with }F_d(\pi)\ne0\}.
\]

**Proposition (first-active-radius balance).**
For every chamber of \(C\),
\[
x_j(\pi)=y_j(\pi)=0
\qquad(1\le j<d(C)).
\]
At radius \(d(C)\), both signs occur:
\[
\exists\pi_+,\pi_-\in\mathcal V(C)
\quad
F_{d(C)}(\pi_+)=+1,
\qquad
F_{d(C)}(\pi_-)=-1.
\]

**Proof.**
For \(j<d(C)\), the definition gives
\[
F_j(\pi)=0
\]
for every chamber. By exactness of one coordinate,
\[
F_j(\pi)=0
\iff
x_j(\pi)=y_j(\pi)=0.
\]
At \(d=d(C)\), some chamber has nonzero \(F_d\). Since every \(\lambda_\pi\) is strictly positive and
\[
\sum_\pi\lambda_\pi F_d(\pi)=0,
\]
the nonzero values cannot all have the same sign. Thus both \(+1\) and \(-1\) occur. \(\square\)

Combining this with the radius-one rigidity lemma gives:

**Corollary (unbounded exact-violation carriers are radius-one carriers).**
If the \(r\)-block of \(C\) has order at least four, or if either adjacent face block has order at least three, then
\[
\boxed{d(C)=1.}
\]

Equivalently, every positive carrier whose first active exact-violation radius satisfies
\[
d(C)\ge2
\]
already has
\[
|C_j|\le3,
\qquad
|C_{j\pm1}|\le2.
\]

This formulation is useful because it is intrinsic to the established exact map \(F\). The only potentially unbounded facewise cancellation for that map occurs in the first violation coordinate, i.e. in the two original triples immediately outside the forced auxiliary junction.


### A double-nearest sign wall is supported at radii one and two

The median-mixed branch admits a sharp adjacent-swap localization.

Let \(\pi'\) be obtained from \(\pi\) by moving \(r\) one position to the right, swapping it with the adjacent original vertex. For the violation profiles one has the exact remote transport identities
\[
x_{d+1}(\pi')=x_d(\pi),
\qquad
y_d(\pi')=y_{d+1}(\pi)
\qquad(d\ge1).
\]
The only new left coordinate is \(x_1(\pi')\); the old right coordinate \(y_1(\pi)\) disappears into the central junction.

**Lemma (double-nearest transport).**
Suppose both \(\pi\) and \(\pi'\) have a double violation at their nearest violating radius:
\[
x_d(\pi)=y_d(\pi)=1,
\qquad
x_j(\pi)=y_j(\pi)=0\quad(j<d),
\]
and similarly with nearest radius \(d'\) for \(\pi'\). Then
\[
\boxed{d,d'\in\{1,2\}.}
\]
More precisely, if \(d\ge2\), then
\[
d=2,\qquad d'=1.
\]

**Proof.**
Assume \(d\ge2\). Since
\[
y_{d-1}(\pi')=y_d(\pi)=1,
\]
and all
\[
y_j(\pi')=y_{j+1}(\pi)=0
\qquad(j<d-1),
\]
the nearest right violation of \(\pi'\) is exactly at radius \(d-1\). If \(\pi'\) is double-nearest, its nearest left violation must also occur at radius \(d-1\).

If \(d-1\ge2\), however,
\[
x_{d-1}(\pi')=x_{d-2}(\pi)=0,
\]
a contradiction. Therefore
\[
d-1=1,
\]
so \(d=2\), and the new exposed coordinate \(x_1(\pi')\) must equal one. Hence \(d'=1\).

If \(d=1\), then
\[
x_2(\pi')=x_1(\pi)=1,
\]
so the nearest left violation of \(\pi'\) is at radius at most two. Since \(\pi'\) is double-nearest,
\[
d'\le2.
\]
This proves the claim. The left-moving version is symmetric. \(\square\)

Now return to a nearest-violation Tucker carrier \(C\) containing both
\[
+\star
\qquad\text{and}\qquad
-\star.
\]
Choose a chamber-graph path in \(C\) between such witnesses.

If some chamber on the path has an ordinary nearest label, then the carrier also contains the opposite ordinary label of the same unsigned coordinate by the Tucker balance theorem.

Otherwise every chamber on the chosen path is double-nearest. Since the side-set gauge changes sign from one endpoint to the other, some edge of the path changes the gauge sign. An adjacent transposition not involving \(r\) leaves the set \(L_r\) unchanged, so such an edge must swap \(r\) with one original vertex. The double-nearest transport lemma then shows that the two endpoint radii of this sign-wall edge belong to
\[
\{1,2\}.
\]

Hence:

**Corollary (median-mixed localization).**
Every median-mixed Tucker carrier satisfies at least one of the following.

1. It contains an ordinary nearest-violation label, and therefore an opposite ordinary pair.
2. It contains an adjacent \(r\)-swap crossing the gauge wall whose two chambers are both double-nearest and whose nearest radii are at most two.

Thus the genuinely mixed sign-wall residue is a radius-\(1/2\) local configuration around the auxiliary vertex, not an unbounded violation profile.


### Coordinatewise local gauges remove the global median artifact

The antipodal gauge in the exact violation vector need not be global and need not be the same for every radius.

Fix once and for all a total order \(\prec\) on the original vertex set \(V(H)\). For a radius \(d\) at which both violation bits are present,
\[
x_d(\pi)=y_d(\pi)=1,
\]
let
\[
\mu_d^L(\pi),\qquad \mu_d^R(\pi)
\]
be the middle original vertices of the left and right radius-\(d\) status triples, respectively. These vertices are distinct. Define
\[
g_d^{\rm loc}(\pi)
=
\begin{cases}
+1,&\mu_d^L(\pi)\prec\mu_d^R(\pi),\\
-1,&\mu_d^R(\pi)\prec\mu_d^L(\pi).
\end{cases}
\]
When \(x_dy_d=0\), the value of \(g_d^{\rm loc}\) is irrelevant.

Reversal exchanges the two radius-\(d\) windows and preserves the middle vertex of each reversed triple. Hence, whenever the double term is active,
\[
g_d^{\rm loc}(\pi^{\rm rev})
=
-g_d^{\rm loc}(\pi).
\]

Define
\[
F_d^{\rm loc}(\pi)
=
x_d(\pi)-y_d(\pi)
+
g_d^{\rm loc}(\pi)x_d(\pi)y_d(\pi).
\]
Then
\[
F_d^{\rm loc}(\pi^{\rm rev})
=
-F_d^{\rm loc}(\pi),
\]
and
\[
F_d^{\rm loc}(\pi)=0
\iff
x_d(\pi)=y_d(\pi)=0.
\]
Thus
\[
F^{\rm loc}=(F_1^{\rm loc},\ldots,F_{n-2}^{\rm loc})
\]
is another exact odd violation vector with the same chamber zero set as the original vector:
\[
F^{\rm loc}(\pi)=0
\iff
\pi\text{ is a directed one-change order}.
\]

The face-average barycentric extension therefore gives an odd map
\[
S^{n-1}\longrightarrow\mathbb R^{n-2}
\]
whose zero set has dimension at least one by Bourgin--Yang.

The advantage is locality. An adjacent transposition changes a status only in the four consecutive starting positions whose windows meet the swapped pair. The left and right radius-\(d\) status starts differ by
\[
2d+2\ge4.
\]
Hence one adjacent transposition cannot change both radius-\(d\) violation windows. It also cannot change both middle vertices used by \(g_d^{\rm loc}\).

**Lemma (one-sided sign wall).**
Let \(\pi,\pi'\) be adjacent chambers. If
\[
F_d^{\rm loc}(\pi)=+1,
\qquad
F_d^{\rm loc}(\pi')=-1,
\]
then the transposition meets exactly one of the two radius-\(d\) windows, while the opposite violation bit remains equal to \(1\) at both endpoints.

More explicitly, up to left-right symmetry, the right violation stays present,
\[
y_d(\pi)=y_d(\pi')=1,
\]
and either

1. the left bit changes
   \[
   x_d:1\longleftrightarrow0,
   \]
   with the double endpoint carrying local gauge \(+1\); or

2. both endpoints are double violations and the local gauge changes sign because the left middle vertex changes.

**Proof.**
If the transposition misses both radius-\(d\) windows, neither violation bit nor either middle vertex changes, so \(F_d^{\rm loc}\) is unchanged. It cannot meet both windows because their start positions differ by at least four.

Suppose it meets only the left window. Then \(y_d\) is fixed. If \(y_d=0\), the coordinate is simply
\[
F_d^{\rm loc}=x_d\in\{0,1\},
\]
so it cannot change from \(+1\) to \(-1\). Hence \(y_d=1\). With \(y_d=1\), the only nonzero possibilities are a right-only state \(F=-1\) and double states \(F=g_d^{\rm loc}\). The displayed alternatives follow. The right-window case is symmetric. \(\square\)

Therefore the first active coordinate of a positive carrier has no genuinely global sign wall. Opposite signs must be connected through local changes at one of the two determining windows. This removes the artificial global-median branch introduced by the side-set gauge. The unresolved conversion problem is now a local one-sided transition across a protected one-change corridor.


## Development

### Current status of the face-to-cover conversion

The earlier descriptions in this Section of Article VII as closed, and the assertion that no further topological continuation is justified, are superseded by the following precise status. The small-support compression results do not prove a two-cover and do not prove that every obstruction to the grand conjecture has been eliminated. The exact reachability intersection remains unproved.

The bounded-central-block theorem in [[topological_recurrence_to_local_gn3_structure]] gives a uniform reduction within Article VII itself. For a positively balanced exact-root carrier whose chambers all have positive deficiency, either a zero-root chamber occurs or its nonzero-root geometry has one central block of order at most four, exterior blocks of order at most two, at most four consecutive root coordinates, and at most ten actual vertices determining the varying root labels after irrelevant exterior block orders are fixed. The proof uses ordered-partition block freedom and boundary antisymmetry, not minimum-counterexample or disturbance arguments.

This is a finite reduction of one face-geometric branch, not a reduction of the grand conjecture to order ten. Two conversion problems remain. In the diagonal branch, p=c gives equal canonical path lengths but can leave a nonempty hole. In the non-diagonal branch, bounded determining data still have to produce a spanning cover or force a useful change of face.

### Rooted omission vectors

For a spanning order (pi=(L,r,R)) of the auxiliary extension, let (P_pi) be the longest suffix of (L), followed by (r), that is a tight path. Let (Q_pi) be the corresponding rooted path on the right, obtained from the longest initial segment of (R) whose reversal followed by (r) is tight. Define
[
A(pi)=V(L)setminus V(P_pi),qquad
B(pi)=V(R)setminus V(Q_pi),
]
and
[
D(pi)=mathbf 1_{A(pi)}-mathbf 1_{B(pi)}.
]
Reversal exchanges (A) and (B), so (D(pi^{m rev})=-D(pi)). Also (D(pi)=0) exactly when the two rooted tight tails cover every original vertex, which by auxiliary exactification is exactly a spanning two-cover of (H).

Along the chamber order every (D(pi)) has signed threshold form
[
+cdots+,0cdots0, -cdots-.
]
It is never identically positive or identically negative, because an original vertex adjacent to (r) belongs to a two-vertex tight path with (r).

### A dimension-tight quotient map

Let (n=|V(H)|). The boundary of the centered permutahedron on (H^+) is (S^{n-1}). Project the omission vector to
[
mathbb R^{V(H)}/langlemathbf1angle,
]
which also has dimension (n-1). Averaging projected omission vectors on every proper face and extending affinely over the barycentric subdivision gives a continuous odd map. Borsuk--Ulam therefore gives a zero. Its carrier face (F) has strictly positive chamber weights satisfying
[
sum_{piinmathcal V(F)}lambda_pi D(pi)=c,mathbf1
]
for some scalar (c).

This yields a sharper structural frontier:

**Facewise omission-balance problem.** If a proper permutahedral face admits a strictly positive convex combination of rooted omission vectors equal to a constant vector, must it contain a chamber with (D(pi)=0)?

A positive answer proves the two-cover conjecture directly through auxiliary exactification, without minimum-counterexample or disturbance arguments. The extra structure is that each chamber label is a signed prefix/suffix threshold vector of actual omitted vertices and all chambers of (F) arise by independent permutations inside ordered face blocks. The remaining task is therefore an uncrossing or face-convexity problem for threshold omissions inside one ordered partition, not a generic convex-cancellation problem.

The sharper theorem leaves only a two- or four-vertex central block with two singleton witness families supported on the same vertex \(z\), or a three-vertex block with a singleton witness \(\{z\}\) on one side and the full star at \(z\) as the opposite pair family. Moreover, every simple directed root cycle has length two or three. The proof of these sharper bounds sometimes converts a matched pair of tight triples directly into a spanning two-cover; it is therefore stronger than a zero-root argument alone.

The remaining nonzero cases have global deletion distance at most three. This is a consequence under the no-zero-root face hypothesis, not a universal bound on \(\kappa_2(H)\).


### Localization of omission balance and the two exceptional facets

The facewise omission-balance question above has a precise exception. Let the auxiliary vertex be \(r\), let \(V=V(H)\), and use the rooted omission vectors \(D(\pi)\) just defined. In the chamber order their entries on original vertices have the form
\[
+\cdots+,\,0\cdots0,\,-\cdots-.
\]
In particular, if original vertices \(u,v\) lie in distinct ordered face blocks with the block of \(u\) earlier, then
\[
D(\pi)_u\ge D(\pi)_v
\]
for every chamber of that face.

**Proposition (localization to the two exceptional facets).** Let \(F\) be a proper face of the permutahedron on \(V\cup\{r\}\). Suppose
\[
\sum_{\pi\in\mathcal V(F)}\lambda_\pi D(\pi)=c\mathbf1,
\qquad \lambda_\pi>0,\quad \sum_\pi\lambda_\pi=1.
\]
If \(F\) is neither \(\{r\}\mid V\) nor \(V\mid\{r\}\), then \(D(\pi)=0\) for every chamber of \(F\).

**Proof.** If original vertices occur in at least two face blocks, the displayed coordinate inequality and equality of coordinate averages imply
\[
D(\pi)_u=D(\pi)_v
\]
for every chamber and every pair in different original-vertex blocks. Positivity of every coefficient is essential here. Using any vertex in a second block also equates two coordinates in the same block. Thus every chamber vector is constant on all original vertices.

At least one original vertex is adjacent to \(r\) in each chamber and belongs to a rooted tight path of order two. Its omission coordinate is zero. Therefore the constant vector is zero.

If all original vertices occur in one block, a proper face can have only that block and the singleton block \(\{r\}\), in either order. These are exactly the two excluded facets. \(\square\)

Thus, under the assumption that \(H\) has no two-cover, every zero of the projected omission map must have one of the two exceptional facets as its carrier. The Borsuk--Ulam conclusion by itself does not exclude this possibility.

**Example (the exceptional facets really can balance).** Identify four original vertices with \(\mathbb F_2^2\). Order the three nonzero differences as \(d_1<d_2<d_3\), and give the ordinary edge \(\{x,y\}\) the class of \(x+y\). Declare
\[
(x,y,z)\text{ tight}\quad\Longleftrightarrow\quad
\operatorname{class}(x+y)<\operatorname{class}(y+z).
\]
The two classes are different, so boundary reversal complements tightness. This is the matching-block boundary tournament.

It has no tight Hamilton path. Such a path would have three successive, strictly increasing edge classes, hence differences \(d_1,d_2,d_3\). Their sum is zero in \(\mathbb F_2^2\), so its final vertex would equal its initial vertex. This contradicts distinctness. It does, of course, have a two-cover by two pairs.

On the facet \(\{r\}\mid V\), the left rooted path is the singleton \(r\). The right rooted path covers either two or three original vertices; it never covers four because that would give a tight Hamilton path of \(H\). Hence no chamber of this facet has \(D=0\).

Translations of \(\mathbb F_2^2\) preserve edge classes and act transitively on original vertices. The uniform average of \(D\) over all chambers of this facet is therefore a constant vector. Exactly half the orders have a non-tight first original triple, allowing the reversed rooted prefix to cover three original vertices; the other half cover only two. Thus the average number omitted is \(3/2\), and
\[
\frac1{4!}\sum_{\pi\in\mathcal V(\{r\}\mid V)}D(\pi)
=-\frac38\mathbf1.
\]
All weights are strictly positive. Reversal gives the opposite constant on \(V\mid\{r\}\).

This refutes the universal facewise implication proposed above: strictly positive projected omission balance need not yield a zero chamber in the same face. It does not refute the grand conjecture. The viable strengthened target is to force a projected zero outside the two exceptional facets, or to extract a two-cover directly from balance on an exceptional facet. The localization proposition proves the first target sufficient; the example shows why the second cannot demand a Hamilton path.


### Facewise omission balance collapses to the two extreme auxiliary facets

Retain the rooted omission notation
\[
D(\pi)={\bf1}_{A(\pi)}-{\bf1}_{B(\pi)}
\]
on spanning orders \(\pi=(L,r,R)\) of \(H^+\). Thus \(A(\pi)\) is a prefix of \(L\), \(B(\pi)\) is a suffix of \(R\), and \(D(\pi)=0\) is exactly a two-cover certificate for \(H\).

Let
\[
F=C_1|\cdots|C_t
\]
be a nonempty proper permutahedron face, and suppose \(r\in C_j\). Assume there are strictly positive weights
\[
\lambda_\pi>0\qquad(\pi\in\mathcal V(F)),\qquad
\sum_\pi\lambda_\pi=1,
\]
such that
\[
\sum_\pi\lambda_\pi D(\pi)=c\,{\bf1}
\]
for some scalar \(c\).

**Theorem (facewise omission reduction).**
If \(F\) is not one of the two extreme facets
\[
\{r\}|V(H),
\qquad
V(H)|\{r\},
\]
then \(F\) contains a chamber \(\pi\) with
\[
D(\pi)=0.
\]
In fact, except for a terminal two-block configuration with the auxiliary block containing original vertices, the argument forces \(D=0\) in every chamber of \(F\); that remaining terminal configuration also collapses by the probability argument below.

**Proof.**

First suppose
\[
1<j<t.
\]
Every original vertex in a block before \(C_j\) is always left of \(r\), hence its \(D\)-coordinate is in \(\{0,1\}\). Every original vertex in a block after \(C_j\) has coordinate in \(\{0,-1\}\). Since all weighted coordinate averages equal \(c\), both sides force
\[
c=0.
\]
Strict positivity of all \(\lambda_\pi\) then implies that every original vertex outside \(C_j\) has \(D\)-coordinate \(0\) in every chamber.

If some chamber had \(A(\pi)\ne\varnothing\), then, because \(A(\pi)\) is a prefix of \(L\) and there is a whole face block before \(C_j\), the first original vertex of the chamber would lie in \(A(\pi)\), contradicting its identically zero coordinate. Hence \(A(\pi)=\varnothing\) for every chamber. The symmetric suffix argument gives \(B(\pi)=\varnothing\). Thus every chamber has \(D=0\).

Now suppose \(j=1\); the case \(j=t\) is symmetric. Every original vertex outside \(C_1\) has coordinate in \(\{0,-1\}\), so
\[
c\le0.
\]
If \(c=0\), strict positivity makes every outside coordinate identically zero. A nonempty suffix \(B(\pi)\) would contain the last original vertex of the chamber, which lies outside \(C_1\), a contradiction. Thus \(B(\pi)=\varnothing\) for every chamber. The remaining coordinates are then nonnegative, have average zero, and hence \(A(\pi)=\varnothing\) as well.

Assume therefore
\[
c=-W<0.
\]

If \(C_1\ne\{r\}\), choose
\[
x\in C_1-\{r\}.
\]
Let \(E\) be the event, under the positive weights \(\lambda\), that every original vertex outside \(C_1\) belongs to \(B(\pi)\), and write its total weight as \(e\).

For every outside vertex \(y\),
\[
D_y=-{\bf1}_{\{y\in B\}},
\]
so its average \(-W\) gives
\[
\Pr_\lambda(y\in B)=W.
\]
Since \(E\subseteq\{y\in B\}\),
\[
e\le W.
\]

Write
\[
a_x=\Pr_\lambda(x\in A),
\qquad
b_x=\Pr_\lambda(x\in B).
\]
If \(x\in B(\pi)\), the suffix property forces every later outside vertex into \(B(\pi)\), hence
\[
\{x\in B\}\subseteq E
\]
and therefore
\[
b_x\le e.
\]
The balance equation at coordinate \(x\) is
\[
a_x-b_x=-W,
\]
so
\[
b_x=a_x+W\ge W.
\]
Consequently
\[
W\le b_x\le e\le W.
\]
Thus
\[
a_x=0,\qquad b_x=e=W.
\]

The same argument holds for every \(x\in C_1-\{r\}\). Hence on every chamber in \(E\), all original vertices of \(C_1\) and all outside vertices belong to \(B(\pi)\): every original vertex of \(H\) is omitted on the right. This is impossible, because whenever \(R\ne\varnothing\), the first vertex of \(R\) together with \(r\) is a two-vertex tight path, so the rooted right path \(Q_\pi\) always contains at least that vertex.

Thus \(c<0\) is impossible whenever \(C_1\ne\{r\}\).

It remains only
\[
C_1=\{r\}.
\]
If \(t\ge3\), choose vertices \(u\in C_i\), \(v\in C_j\) with
\[
2\le i<j\le t.
\]
Because \(B(\pi)\) is a suffix of \(R\),
\[
{\bf1}_{\{u\in B\}}\le{\bf1}_{\{v\in B\}}
\]
in every chamber. Their weighted expectations are both \(W\), so strict positivity forces equality chamberwise. Varying \(u,v\) shows that in every chamber either every original vertex is in \(B\) or none is. The former is impossible by the immediate-neighbor observation, while the latter contradicts \(W>0\).

Therefore the only unresolved case with \(j=1\) is
\[
F=\{r\}|V(H).
\]
The symmetric argument leaves only
\[
F=V(H)|\{r\}.
\]
This proves the theorem. \(\square\)

### The reduction is sharp at the level of convex cancellation

The two exceptional facets cannot be discarded by a generic convexity argument. On the facet
\[
\{r\}|V(H),
\]
one has
\[
D(\pi)=-{\bf1}_{B(\pi)},
\]
where \(B(\pi)\) is the suffix omitted after the maximal rooted right path.

For a standard non-Hamiltonian four-vertex matching-block boundary tournament, the uniform distribution on all \(24\) permutations gives
\[
\Pr(v\in B)=\frac38
\]
for every vertex \(v\), while no permutation has \(B=\varnothing\). Thus
\[
\frac1{24}\sum_\pi D(\pi)
=
-\frac38\,{\bf1}
\]
is a genuine full-support constant balance with no zero chamber.

Accordingly, the facewise omission theorem is sharp:
\[
\boxed{
\text{all non-extreme carrier faces close;}
\quad
\text{the only genuine convex-cancellation residue is the pair of extreme facets.}
}
\]

The remaining global topological question is therefore whether an odd zero of the quotient omission map can be supported entirely by those two antipodal extreme facets when the whole tournament has no two-cover. Local averaging alone cannot answer this.

### The exceptional facets carry essential degree

The matching-block example above shows that the two exceptional facets can support projected omission balance without a zero chamber. In a hypothetical counterexample, the limitation is stronger: the projected omission map is topologically forced to have a zero in the interior of each exceptional facet.

Let
\[
F^-=\{r\}\mid V(H)
\]
be the left exceptional facet. It is canonically a copy of the centered permutahedron \(P_V\) on the original vertex set, of dimension \(n-1\). Its boundary is therefore an \((n-2)\)-sphere.

On \(F^-\), every omission vector has the form
\[
D(\pi)=-\mathbf 1_{B(\pi)},
\]
where \(B(\pi)\) is a suffix of the original-vertex order. Hence, if
\[
G=B_1|\cdots|B_t
\]
is any proper face of \(P_V\), and \(u\in B_i,\ v\in B_j\) with \(i<j\), then
\[
D(\pi)_u\ge D(\pi)_v
\]
for every chamber \(\pi\) of \(G\). The same inequalities hold for the face-average omission vector assigned to the barycenter of \(G\), and therefore throughout every barycentric simplex whose largest face is \(G\).

Write
\[
Q=\mathbb R^{V(H)}/\langle\mathbf 1\rangle
\]
and, for an ordered partition \(G\), let
\[
C_G=
\left\{
[y]\in Q:
y_u\ge y_v
\text{ whenever }
u\in B_i,\ v\in B_j,\ i<j
\right\}.
\]
Thus the projected omission map on the barycentric subdivision of \(\partial P_V\) is carried by the spherical carrier
\[
K_G=(C_G\setminus\{0\})/\mathbb R_{>0}.
\]

Assume now that \(H\) has no spanning two-cover. By the facewise omission theorem above, the projected omission map has no zero on \(\partial F^-\): any zero there would have a proper nonexceptional carrier face in the full auxiliary permutahedron and would force an actual chamber with \(D=0\).

Each \(K_G\) is contractible. Indeed \(C_G\) is a proper convex cone; after quotienting its lineality space, the pointed part has a spherically convex section, and \(K_G\) is the join of that section with the sphere of the lineality space.

Compare the normalized omission map on \(\partial P_V\) with
\[
h(x)=-\frac{x}{\|x\|}.
\]
If \(x\) lies in the permutahedron face \(G\), then the coordinates of \(x\) increase from earlier to later blocks, so the coordinates of \(-x\) decrease from earlier to later blocks. Therefore
\[
h(G)\subseteq K_G.
\]
The normalized omission map is carried by the same acyclic carrier. The acyclic carrier theorem makes the two maps homotopic.

Consequently
\[
\deg(\widehat D|_{\partial F^-})
=
\deg(h)
=
(-1)^{n-1},
\]
up to the harmless orientation convention for \(Q\). In particular the degree has absolute value one.

Every continuous extension of this boundary map over the exceptional facet \(F^-\) must therefore hit the origin. The barycentric omission map is such an extension, so \(F^-\) contains an interior projected omission zero. Reversal gives the same conclusion for
\[
F^+=V(H)\mid\{r\}.
\]

Thus in a hypothetical counterexample the two exceptional facets do not merely permit topological cancellation:
\[
\boxed{
\text{each exceptional facet carries an essential degree-one omission zero.}
}
\]

This sharpens the limitation of the rooted omission projection. The global Borsuk--Ulam zero can be absorbed by the two extreme facets for a structural degree reason. Therefore a continuation that uses only the same projected omission map and the same quotient target cannot force a useful nonexceptional zero; additional information or a genuinely different target is required.


### The exact violation map escapes the exceptional omission facets

The omission projection fails for a topologically structural reason on the two extreme auxiliary facets, but the exact auxiliary violation vector behaves differently.

Let \(n=|V(H)|\), so the auxiliary tournament \(H^+\) has \(n+1\) vertices and the boundary of its centered permutahedron is
\[
S^{n-1}.
\]
Use the odd violation vector
\[
F(\pi)=(F_d(\pi))_{1\le d\le n-2}
\]
from [[auxiliary_violation_vector_has_exact_chamber_zeros]], where
\[
F_d=x_d-y_d+g\,x_dy_d.
\]
Its chamber zeros are exactly directed one-change orders and therefore exactly two-cover certificates for \(H\).

Average \(F\) over every proper face and extend affinely on the barycentric subdivision. This gives a continuous odd map
\[
\mathcal F:S^{n-1}\longrightarrow\mathbb R^{n-2}.
\]
Bourgin--Yang therefore gives
\[
\dim \mathcal F^{-1}(0)\ge1.
\]
Every zero has the usual positive carrier-face expansion:
\[
\sum_{\pi\in\mathcal V(C)}\lambda_\pi F(\pi)=0,
\qquad
\lambda_\pi>0.
\]

Now consider the exceptional facet
\[
C^-=\{r\}\mid V(H).
\]
Here \(r\) is first in every chamber. There are no left violations, so
\[
x_d=0,\qquad F_d=-y_d\in\{0,-1\}
\]
for every chamber and every distance \(d\). If a positive convex combination of these vectors were zero, every coordinate of every chamber vector would have to vanish. Thus every chamber in the carrier would satisfy
\[
F(\pi)=0,
\]
which is already a directed one-change order and hence a two-cover of \(H\).

Therefore, under the counterexample hypothesis,
\[
\mathcal F^{-1}(0)\cap C^-=\varnothing.
\]
By reversal,
\[
\mathcal F^{-1}(0)\cap C^+=\varnothing,
\qquad
C^+=V(H)\mid\{r\}.
\]

Hence:
\[
\boxed{
\text{if }H\text{ has no two-cover, every zero carrier of the exact violation map is nonexceptional.}
}
\]

This contrasts sharply with the projected omission map, whose two exceptional facets carry essential degree-one zeros. The violation map therefore genuinely escapes Astra's exceptional-facet obstruction.

The remaining gap is different: positive balance of the violation vectors on a nonexceptional face does not yet imply that one chamber has \(F=0\). The next structural target is a facewise conversion theorem for these positional violation vectors, ideally using fixed-center intermediate value and the fact that the zero locus has positive dimension.


### A side-set gauge and exact closure on singleton-\(r\) carrier faces

The coordinatewise gauge in the exact violation vector can be replaced by one global double-violation coordinate in a way that is better adapted to faces.

Let the original vertex set be \(V\), let \(r\) be the auxiliary vertex, and for a spanning order \(\pi\) write
\[
L_r(\pi)=\{v\in V:v\text{ occurs left of }r\},
\qquad
R_r(\pi)=V\setminus L_r(\pi).
\]
Fix once and for all a total order \(\prec\) on subsets of \(V\). Define an antipodal sign \(g_{\rm set}\) by
\[
g_{\rm set}(\pi)=
\begin{cases}
+1,&|L_r(\pi)|<|R_r(\pi)|,\\
-1,&|L_r(\pi)|>|R_r(\pi)|,\\
+1,&|L_r|=|R_r|\text{ and }L_r\prec R_r,\\
-1,&|L_r|=|R_r|\text{ and }R_r\prec L_r.
\end{cases}
\]
Reversal exchanges \(L_r\) and \(R_r\), hence
\[
g_{\rm set}(\pi^{\rm rev})=-g_{\rm set}(\pi).
\]

For the left/right violation bits \(x_d,y_d\) of [[auxiliary_violation_vector_has_exact_chamber_zeros]], define
\[
A_d(\pi)=x_d(\pi)-y_d(\pi),
\]
and choose arbitrary positive weights \(w_d>0\). Put
\[
B(\pi)
=
g_{\rm set}(\pi)\sum_d w_d x_d(\pi)y_d(\pi).
\]
Then
\[
\Theta(\pi)=\bigl((A_d(\pi))_d,B(\pi)\bigr)
\]
is odd. Its target has dimension \(n-1\), equal to the dimension of the auxiliary Coxeter sphere.

Moreover
\[
\Theta(\pi)=0
\]
if and only if \(\pi\) has no violations. Indeed \(A_d=0\) gives \(x_d=y_d\) at every distance, while \(B=0\), since \(g_{\rm set}=\pm1\) and all \(w_d>0\), forces
\[
x_dy_d=0
\]
for every \(d\). Thus \(x_d=y_d=0\) for all \(d\).

Average \(\Theta\) on proper face barycenters and extend affinely. Borsuk--Ulam gives a zero and the usual strictly positive expansion over every chamber of its carrier face.

The key advantage of \(g_{\rm set}\) is the following.

**Theorem (singleton-\(r\) carrier conversion).**
Let
\[
C=C_1|\cdots|C_t
\]
be a proper permutahedron face in which
\[
C_j=\{r\}.
\]
Suppose there are strictly positive weights
\[
\lambda_\pi>0\qquad(\pi\in\mathcal V(C))
\]
with
\[
\sum_\pi\lambda_\pi\Theta(\pi)=0.
\]
Then every chamber of \(C\) is violation-free. In particular \(H\) has a spanning two-cover.

**Proof.**
Because \(r\) is a singleton block, the set of original vertices left of \(r\) and the set right of \(r\) are fixed throughout \(C\). Hence
\[
g_{\rm set}(\pi)=g_0\in\{\pm1\}
\]
is constant on all chambers of \(C\).

The last coordinate of the positive balance is therefore
\[
0
=
g_0\sum_\pi\lambda_\pi\sum_d w_dx_d(\pi)y_d(\pi).
\]
Every summand inside the last sum is nonnegative, every \(w_d\) is positive, and every \(\lambda_\pi\) is positive. Hence
\[
x_d(\pi)y_d(\pi)=0
\]
for every chamber \(\pi\) and every distance \(d\).

Now fix \(d\). Since \(r\) is a singleton block, the chamber set factors as
\[
\mathcal V(C)
=
\mathcal L\times\mathcal R,
\]
where \(\mathcal L\) consists of the independent permutations in blocks left of \(r\), and \(\mathcal R\) those right of \(r\). The bit \(x_d\) depends only on the left factor and \(y_d\) only on the right factor.

If some left factor had \(x_d=1\) and some right factor had \(y_d=1\), their product chamber would satisfy
\[
x_dy_d=1,
\]
contrary to the preceding paragraph. Therefore at least one of the two functions is identically zero on its factor.

But the \(A_d\)-coordinate of the positive balance says
\[
\sum_\pi\lambda_\pi x_d(\pi)
=
\sum_\pi\lambda_\pi y_d(\pi).
\]
If one side is identically zero, positivity forces the other side to be identically zero as well. Hence
\[
x_d(\pi)=y_d(\pi)=0
\]
for every chamber. Since \(d\) was arbitrary, every chamber of \(C\) is violation-free. \(\square\)

Thus the exact violation map has no unresolved singleton-\(r\) carrier geometry at all:
\[
\boxed{
\text{positive }\Theta\text{-balance on a face with }\{r\}\text{ as a block}
\Longrightarrow
\text{an actual two-cover certificate}.
}
\]

Consequently, under the counterexample hypothesis, every zero carrier of the \(\Theta\)-map must place \(r\) in a block containing at least one original vertex. This eliminates the central singleton case as well as the two extreme singleton facets; the only remaining face-to-cover obstruction is genuinely the geometry of a nontrivial \(r\)-block.


### Constant-gauge nontrivial \(r\)-blocks collapse to order four

The previous theorem handles faces in which \(\{r\}\) is already a block. Now let
\[
C=C_1|\cdots|C_t
\]
be a proper carrier face with
\[
r\in C_j,
\qquad
W=C_j\setminus\{r\}\ne\varnothing.
\]
Assume the side-set gauge \(g_{\rm set}\) has the same sign on every chamber of \(C\), and suppose
\[
\sum_{\pi\in\mathcal V(C)}\lambda_\pi\Theta(\pi)=0,
\qquad
\lambda_\pi>0.
\]
Assume for contradiction that \(H\) has no two-cover.

For \(S\subseteq W\), let \(\mathcal C_S\) be the chambers in which precisely the vertices of \(S\) occur before \(r\) inside the block \(C_j\). Equivalently \(\mathcal C_S\) is the chamber set of the refinement
\[
C_1|\cdots|C_{j-1}|S|\{r\}|(W\setminus S)|C_{j+1}|\cdots|C_t,
\]
with empty blocks omitted.

Because the gauge is constant on all of \(C\), the final coordinate of the positive balance forces
\[
u(\pi)v(\pi)=0
\]
for every chamber, where
\[
u(\pi)={\bf1}\{\text{some left violation occurs}\},
\qquad
v(\pi)={\bf1}\{\text{some right violation occurs}\}.
\]
Indeed one may use this stronger mixed-side term in place of
\(\sum_d w_dx_dy_d\):
\[
B_{\rm mix}(\pi)=g_{\rm set}(\pi)u(\pi)v(\pi).
\]
Together with the coordinates
\[
A_d=x_d-y_d,
\]
the chamber zero set is still exactly the directed one-change orders.

Thus, under the counterexample hypothesis, every chamber of \(C\) is of exactly one of two types:
\[
L:\quad u=1,\ v=0,
\qquad
R:\quad u=0,\ v=1.
\]

**Lemma (fiber constancy).**
For each \(S\subseteq W\), every chamber of \(\mathcal C_S\) has the same type.

**Proof.**
The chamber graph of \(\mathcal C_S\) is connected and uses only adjacent transpositions that do not move \(r\). Such a transposition occurs entirely on one side of \(r\), so it can change only left violations or only right violations. Hence an \(L\)-chamber cannot move in one step to an \(R\)-chamber: changing the left side can only keep type \(L\) or create a zero chamber, while changing the right side can only keep type \(L\) or create a mixed chamber. Both alternatives are excluded. \(\square\)

The \(A_d\)-balance and positivity imply that both fiber types occur. Indeed if all chambers were \(L\), every \(A_d\)-average would be nonnegative and at least one would be positive; similarly for \(R\).

The Boolean cube on subsets of \(W\) is connected, so there are adjacent subsets
\[
S,\qquad S'=S\cup\{z\}
\]
whose fibers have opposite types. Choose orders so that \(z\) is immediately after \(r\) in a chamber
\[
\pi\in\mathcal C_S
\]
and swap \(r,z\) to obtain
\[
\pi'\in\mathcal C_{S'}.
\]
After reversing the labels \(L,R\) if necessary, assume \(\pi\) is \(L\) and \(\pi'\) is \(R\).

Moving \(r\) one step to the right gives the exact remote-profile transport identities
\[
x_{d+1}(\pi')=x_d(\pi),
\qquad
y_d(\pi')=y_{d+1}(\pi)
\qquad(d\ge1).
\]
Since \(\pi\) has no right violations and \(\pi'\) has no left violations, the opposite orientation of the crossing edge is forced: equivalently, reading the edge from the \(L\)-fiber to the \(R\)-fiber moves \(r\) one step to the **left**. In that orientation,
\[
x_d(\pi')=x_{d+1}(\pi),
\qquad
y_{d+1}(\pi')=y_d(\pi)
\qquad(d\ge1),
\]
and the only newly exposed coordinate is \(y_1(\pi')\).

Therefore
\[
x_d(\pi)=0\quad(d\ge2),
\qquad
y_d(\pi')=0\quad(d\ge2).
\]
Because \(\pi\) is \(L\) and \(\pi'\) is \(R\),
\[
x_1(\pi)=1,
\qquad
y_1(\pi')=1.
\]
Thus an opposite-type fiber edge has the rigid profile
\[
\boxed{
\pi:\ x_1=1,\ x_{d\ge2}=0,\ y_d=0;
\qquad
\pi':\ y_1=1,\ y_{d\ge2}=0,\ x_d=0.
}
\]

Now use the fact that an entire fiber has one type. In an \(L\)-fiber, the complete right side is violation-free for every permutation allowed by the fiber. If any free block wholly to the right of \(r\) had order at least three, choose three consecutive positions inside that block and swap the first and third vertices. Boundary antisymmetry flips the corresponding right status, contradicting universal right cleanliness. Hence every right-side block in an \(L\)-fiber has order at most two.

Similarly, every left-side block in an \(R\)-fiber has order at most two.

Apply this to the adjacent fibers above. In the \(L\)-fiber the block
\[
W\setminus S
\]
lies immediately to the right of \(r\), so
\[
|W\setminus S|\le2,
\]
and every original face block after \(C_j\) has order at most two. In the \(R\)-fiber the block
\[
S'=S\cup\{z\}
\]
lies immediately to the left of \(r\), so
\[
|S|+1\le2,
\]
and every original face block before \(C_j\) has order at most two.

Consequently
\[
|S|\le1,
\qquad
|W\setminus S|\le2,
\qquad
|W|\le3.
\]
Thus
\[
\boxed{|C_j|\le4,}
\]
and every other block of \(C\) has order at most two.

So the constant-gauge branch of the exact violation map has no unbounded face geometry:
\[
\boxed{
\text{constant }g_{\rm set}
\Longrightarrow
\text{all exterior blocks have order }\le2
\text{ and the }r\text{-block has order }\le4.
}
\]
The only uncompressed branch is therefore the one in which \(g_{\rm set}\) changes sign inside the \(r\)-block, i.e. the block crosses the global side-set median.


### Map distinction

For clarity, two closely related full-dimensional exact maps are in use.

The first is
\[
\Theta_{\rm eq}(\pi)
=
\left(
(A_d(\pi))_d,\ 
g_{\rm set}(\pi)\sum_d w_dx_d(\pi)y_d(\pi)
\right),
\]
which records equal-radius double violations.

For the constant-gauge block-collapse argument, use instead
\[
\Theta_{\rm mix}(\pi)
=
\left(
(A_d(\pi))_d,\ 
g_{\rm set}(\pi)u(\pi)v(\pi)
\right),
\]
where
\[
u={\bf1}\{\exists d:x_d=1\},
\qquad
v={\bf1}\{\exists d:y_d=1\}.
\]

Both maps are odd, both take values in \(\mathbb R^{n-1}\), and both have chamber zero set exactly equal to the directed one-change orders. Borsuk--Ulam and the positive carrier expansion apply separately to each map. The singleton-\(r\) conversion is valid for either map. The nontrivial constant-gauge block-collapse theorem above is to be read for a positive carrier of
\[
\Theta_{\rm mix}.
\]


### Nearest-violation Tucker compression

There is a lower-information exact label that is particularly well adapted to Tucker-style arguments.

Assume \(H\) has no two-cover, so every spanning order of the auxiliary extension \(H^+\) has at least one violation. For a chamber \(\pi\), let
\[
d_0(\pi)
=
\min\{d\ge1:x_d(\pi)=1\text{ or }y_d(\pi)=1\}.
\]
At the nearest violating radius there are three possibilities:
\[
(1,0),\qquad(0,1),\qquad(1,1).
\]

Use the side-set antipodal gauge \(g_{\rm set}\) above, and define a signed label
\[
\ell(\pi)\in
\{\pm1,\ldots,\pm(n-2),\pm\star\}
\]
by
\[
\ell(\pi)=
\begin{cases}
+d_0,&(x_{d_0},y_{d_0})=(1,0),\\
-d_0,&(x_{d_0},y_{d_0})=(0,1),\\
g_{\rm set}(\pi)\star,&(x_{d_0},y_{d_0})=(1,1).
\end{cases}
\]
Identify the \(n-1\) unsigned labels
\[
1,\ldots,n-2,\star
\]
with the coordinate vectors of \(\mathbb R^{n-1}\), and write \(L(\pi)\) for the corresponding signed basis vector.

Reversal preserves the nearest violating radius, exchanges left and right, and negates \(g_{\rm set}\). Hence
\[
L(\pi^{\rm rev})=-L(\pi).
\]

Average \(L\) over the chambers of every nonempty proper face and extend affinely over the barycentric subdivision.

**Theorem (nearest-violation Tucker carrier).**
The resulting map
\[
\mathcal L:S^{n-1}\longrightarrow\mathbb R^{n-1}
\]
is continuous and odd. Hence it has a zero. If \(C\) is the carrier face of such a zero, then there are strictly positive coefficients
\[
\lambda_\pi>0\qquad(\pi\in\mathcal V(C))
\]
with
\[
\sum_{\pi\in\mathcal V(C)}\lambda_\pi L(\pi)=0.
\]
Consequently every signed label occurring among the chambers of \(C\) occurs with both signs. In particular:

- if \(+d\) occurs, then \(-d\) occurs;
- if \(+\star\) occurs, then \(-\star\) occurs.

**Proof.**
Oddness and Borsuk--Ulam give a zero. The positive carrier expansion is the same smallest-barycentric-simplex argument used throughout Article VII. Since the vectors \(L(\pi)\) are signed coordinate vectors and every chamber of the carrier has positive coefficient, the vanishing of each coordinate forces positive mass on both signs of every unsigned label that occurs. \(\square\)

This gives a sharp dichotomy.

**Corollary (protected-radius or median-mixed dichotomy).**
A carrier \(C\) as above satisfies one of the following.

1. **Protected-radius branch.** No \(\star\)-label occurs. Let \(d\) be the smallest ordinary label occurring in \(C\). Then every chamber of \(C\) has
   \[
   x_j=y_j=0
   \qquad(1\le j<d),
   \]
   and \(C\) contains both a chamber with
   \[
   (x_d,y_d)=(1,0)
   \]
   and a chamber with
   \[
   (x_d,y_d)=(0,1).
   \]

2. **Median-mixed branch.** A \(\star\)-label occurs. Then \(C\) contains nearest-radius double-violation chambers on both gauge signs:
   \[
   g_{\rm set}=+1
   \qquad\text{and}\qquad
   g_{\rm set}=-1.
   \]

In the first branch, minimality of \(d\) gives the protected-radius hypothesis on **every** chamber of the carrier, not merely on the two opposite witnesses. If \(r\) is a singleton block, [[fixed_center_violation_intermediate_value]] applies directly and forces either larger protected radius or a double violation at radius \(d\). Iterating therefore reaches either a violation-free chamber or the second branch.

Thus the remaining nontrivial topology can be localized to the median-mixed branch: one face contains double violations at the nearest radius on both sides of the antipodal side-set wall.


### Protected radius at least two forces a tiny \(r\)-block

Let \(C=C_1|\cdots|C_t\) be any proper face of the auxiliary permutahedron, with
\[
r\in C_j.
\]
Suppose every chamber of \(C\) has no violation at radius \(1\):
\[
x_1(\pi)=y_1(\pi)=0
\qquad(\pi\in\mathcal V(C)).
\]

**Lemma (radius-one rigidity).**
Then
\[
|C_j|\le3.
\]
Moreover, when the neighboring blocks exist,
\[
|C_{j-1}|\le2,
\qquad
|C_{j+1}|\le2.
\]

**Proof.**
Write
\[
W=C_j\setminus\{r\}.
\]
If \(|W|\ge3\), place \(r\) last in its block and choose three vertices of \(W\) in the three positions immediately before \(r\). Since \(x_1=0\), their ordered triple must be tight. Reversing those three vertices while keeping every other block order fixed gives another chamber of \(C\), but boundary antisymmetry makes the reversed triple non-tight, contradicting \(x_1=0\). Hence
\[
|W|\le2,
\]
so \(|C_j|\le3\).

If \(|C_{j-1}|\ge3\), place \(r\) first in \(C_j\). The three positions immediately before \(r\) may then be filled by any ordered triple from the end of \(C_{j-1}\). The same reversal argument contradicts \(x_1=0\). Thus \(|C_{j-1}|\le2\).

The right-hand statement is symmetric: place \(r\) last in \(C_j\). If \(|C_{j+1}|\ge3\), arbitrary reversal of the first three vertices of \(C_{j+1}\) flips the immediate right status, contradicting \(y_1=0\). \(\square\)

Apply this to a nearest-violation Tucker carrier. Let
\[
d_{\min}
=
\min_{\pi\in\mathcal V(C)}d_0(\pi).
\]

**Corollary.**
If
\[
d_{\min}\ge2,
\]
then the carrier has
\[
|C_j|\le3,
\qquad
|C_{j\pm1}|\le2
\]
for the existing neighboring blocks.

Thus every carrier with a large nontrivial \(r\)-block necessarily satisfies
\[
\boxed{d_{\min}=1.}
\]

This conclusion is independent of which signed nearest label realizes the minimum. It uses only the universal protected-radius statement
\[
x_1=y_1=0
\]
on the carrier. Hence the genuinely unbounded branch of the nearest-violation Tucker program is localized to the first uncontrolled triples immediately outside the forced auxiliary junction.


### The first active exact-violation coordinate

The same radius localization follows directly from the coordinatewise exact violation map, without the nearest-label compression.

Let
\[
F(\pi)=(F_1(\pi),\ldots,F_{n-2}(\pi))
\]
be the odd exact violation vector from [[auxiliary_violation_vector_has_exact_chamber_zeros]], and let \(C\) be the carrier face of a zero with strictly positive chamber weights:
\[
\sum_{\pi\in\mathcal V(C)}\lambda_\pi F(\pi)=0,
\qquad
\lambda_\pi>0.
\]
Assume \(H\) has no two-cover, so no chamber has \(F(\pi)=0\).

Define the **first active radius**
\[
d(C)
=
\min\{d:\exists\pi\in\mathcal V(C)\text{ with }F_d(\pi)\ne0\}.
\]

**Proposition (first-active-radius balance).**
For every chamber of \(C\),
\[
x_j(\pi)=y_j(\pi)=0
\qquad(1\le j<d(C)).
\]
At radius \(d(C)\), both signs occur:
\[
\exists\pi_+,\pi_-\in\mathcal V(C)
\quad
F_{d(C)}(\pi_+)=+1,
\qquad
F_{d(C)}(\pi_-)=-1.
\]

**Proof.**
For \(j<d(C)\), the definition gives
\[
F_j(\pi)=0
\]
for every chamber. By exactness of one coordinate,
\[
F_j(\pi)=0
\iff
x_j(\pi)=y_j(\pi)=0.
\]
At \(d=d(C)\), some chamber has nonzero \(F_d\). Since every \(\lambda_\pi\) is strictly positive and
\[
\sum_\pi\lambda_\pi F_d(\pi)=0,
\]
the nonzero values cannot all have the same sign. Thus both \(+1\) and \(-1\) occur. \(\square\)

Combining this with the radius-one rigidity lemma gives:

**Corollary (unbounded exact-violation carriers are radius-one carriers).**
If the \(r\)-block of \(C\) has order at least four, or if either adjacent face block has order at least three, then
\[
\boxed{d(C)=1.}
\]

Equivalently, every positive carrier whose first active exact-violation radius satisfies
\[
d(C)\ge2
\]
already has
\[
|C_j|\le3,
\qquad
|C_{j\pm1}|\le2.
\]

This formulation is useful because it is intrinsic to the established exact map \(F\). The only potentially unbounded facewise cancellation for that map occurs in the first violation coordinate, i.e. in the two original triples immediately outside the forced auxiliary junction.


### A double-nearest sign wall is supported at radii one and two

The median-mixed branch admits a sharp adjacent-swap localization.

Let \(\pi'\) be obtained from \(\pi\) by moving \(r\) one position to the right, swapping it with the adjacent original vertex. For the violation profiles one has the exact remote transport identities
\[
x_{d+1}(\pi')=x_d(\pi),
\qquad
y_d(\pi')=y_{d+1}(\pi)
\qquad(d\ge1).
\]
The only new left coordinate is \(x_1(\pi')\); the old right coordinate \(y_1(\pi)\) disappears into the central junction.

**Lemma (double-nearest transport).**
Suppose both \(\pi\) and \(\pi'\) have a double violation at their nearest violating radius:
\[
x_d(\pi)=y_d(\pi)=1,
\qquad
x_j(\pi)=y_j(\pi)=0\quad(j<d),
\]
and similarly with nearest radius \(d'\) for \(\pi'\). Then
\[
\boxed{d,d'\in\{1,2\}.}
\]
More precisely, if \(d\ge2\), then
\[
d=2,\qquad d'=1.
\]

**Proof.**
Assume \(d\ge2\). Since
\[
y_{d-1}(\pi')=y_d(\pi)=1,
\]
and all
\[
y_j(\pi')=y_{j+1}(\pi)=0
\qquad(j<d-1),
\]
the nearest right violation of \(\pi'\) is exactly at radius \(d-1\). If \(\pi'\) is double-nearest, its nearest left violation must also occur at radius \(d-1\).

If \(d-1\ge2\), however,
\[
x_{d-1}(\pi')=x_{d-2}(\pi)=0,
\]
a contradiction. Therefore
\[
d-1=1,
\]
so \(d=2\), and the new exposed coordinate \(x_1(\pi')\) must equal one. Hence \(d'=1\).

If \(d=1\), then
\[
x_2(\pi')=x_1(\pi)=1,
\]
so the nearest left violation of \(\pi'\) is at radius at most two. Since \(\pi'\) is double-nearest,
\[
d'\le2.
\]
This proves the claim. The left-moving version is symmetric. \(\square\)

Now return to a nearest-violation Tucker carrier \(C\) containing both
\[
+\star
\qquad\text{and}\qquad
-\star.
\]
Choose a chamber-graph path in \(C\) between such witnesses.

If some chamber on the path has an ordinary nearest label, then the carrier also contains the opposite ordinary label of the same unsigned coordinate by the Tucker balance theorem.

Otherwise every chamber on the chosen path is double-nearest. Since the side-set gauge changes sign from one endpoint to the other, some edge of the path changes the gauge sign. An adjacent transposition not involving \(r\) leaves the set \(L_r\) unchanged, so such an edge must swap \(r\) with one original vertex. The double-nearest transport lemma then shows that the two endpoint radii of this sign-wall edge belong to
\[
\{1,2\}.
\]

Hence:

**Corollary (median-mixed localization).**
Every median-mixed Tucker carrier satisfies at least one of the following.

1. It contains an ordinary nearest-violation label, and therefore an opposite ordinary pair.
2. It contains an adjacent \(r\)-swap crossing the gauge wall whose two chambers are both double-nearest and whose nearest radii are at most two.

Thus the genuinely mixed sign-wall residue is a radius-\(1/2\) local configuration around the auxiliary vertex, not an unbounded violation profile.


### Coordinatewise local gauges remove the global median artifact

The antipodal gauge in the exact violation vector need not be global and need not be the same for every radius.

Fix once and for all a total order \(\prec\) on the original vertex set \(V(H)\). For a radius \(d\) at which both violation bits are present,
\[
x_d(\pi)=y_d(\pi)=1,
\]
let
\[
\mu_d^L(\pi),\qquad \mu_d^R(\pi)
\]
be the middle original vertices of the left and right radius-\(d\) status triples, respectively. These vertices are distinct. Define
\[
g_d^{\rm loc}(\pi)
=
\begin{cases}
+1,&\mu_d^L(\pi)\prec\mu_d^R(\pi),\\
-1,&\mu_d^R(\pi)\prec\mu_d^L(\pi).
\end{cases}
\]
When \(x_dy_d=0\), the value of \(g_d^{\rm loc}\) is irrelevant.

Reversal exchanges the two radius-\(d\) windows and preserves the middle vertex of each reversed triple. Hence, whenever the double term is active,
\[
g_d^{\rm loc}(\pi^{\rm rev})
=
-g_d^{\rm loc}(\pi).
\]

Define
\[
F_d^{\rm loc}(\pi)
=
x_d(\pi)-y_d(\pi)
+
g_d^{\rm loc}(\pi)x_d(\pi)y_d(\pi).
\]
Then
\[
F_d^{\rm loc}(\pi^{\rm rev})
=
-F_d^{\rm loc}(\pi),
\]
and
\[
F_d^{\rm loc}(\pi)=0
\iff
x_d(\pi)=y_d(\pi)=0.
\]
Thus
\[
F^{\rm loc}=(F_1^{\rm loc},\ldots,F_{n-2}^{\rm loc})
\]
is another exact odd violation vector with the same chamber zero set as the original vector:
\[
F^{\rm loc}(\pi)=0
\iff
\pi\text{ is a directed one-change order}.
\]

The face-average barycentric extension therefore gives an odd map
\[
S^{n-1}\longrightarrow\mathbb R^{n-2}
\]
whose zero set has dimension at least one by Bourgin--Yang.

The advantage is locality. An adjacent transposition changes a status only in the four consecutive starting positions whose windows meet the swapped pair. The left and right radius-\(d\) status starts differ by
\[
2d+2\ge4.
\]
Hence one adjacent transposition cannot change both radius-\(d\) violation windows. It also cannot change both middle vertices used by \(g_d^{\rm loc}\).

**Lemma (one-sided sign wall).**
Let \(\pi,\pi'\) be adjacent chambers. If
\[
F_d^{\rm loc}(\pi)=+1,
\qquad
F_d^{\rm loc}(\pi')=-1,
\]
then the transposition meets exactly one of the two radius-\(d\) windows, while the opposite violation bit remains equal to \(1\) at both endpoints.

More explicitly, up to left-right symmetry, the right violation stays present,
\[
y_d(\pi)=y_d(\pi')=1,
\]
and either

1. the left bit changes
   \[
   x_d:1\longleftrightarrow0,
   \]
   with the double endpoint carrying local gauge \(+1\); or

2. both endpoints are double violations and the local gauge changes sign because the left middle vertex changes.

**Proof.**
If the transposition misses both radius-\(d\) windows, neither violation bit nor either middle vertex changes, so \(F_d^{\rm loc}\) is unchanged. It cannot meet both windows because their start positions differ by at least four.

Suppose it meets only the left window. Then \(y_d\) is fixed. If \(y_d=0\), the coordinate is simply
\[
F_d^{\rm loc}=x_d\in\{0,1\},
\]
so it cannot change from \(+1\) to \(-1\). Hence \(y_d=1\). With \(y_d=1\), the only nonzero possibilities are a right-only state \(F=-1\) and double states \(F=g_d^{\rm loc}\). The displayed alternatives follow. The right-window case is symmetric. \(\square\)

Therefore the first active coordinate of a positive carrier has no genuinely global sign wall. Opposite signs must be connected through local changes at one of the two determining windows. This removes the artificial global-median branch introduced by the side-set gauge. The unresolved conversion problem is now a local one-sided transition across a protected one-change corridor.
