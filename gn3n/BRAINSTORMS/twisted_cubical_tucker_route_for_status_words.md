# Twisted cubical Tucker route for status words

The full 0/1 status word of a spanning order has dimension n-2, exactly the dimension of the centered permutahedron boundary. Investigate whether the strong local consistency of these status labels upgrades the existing root-balance/Borsuk-Ulam argument to a cubical Tucker/Kuhn theorem that forces a two-cover.

# Twisted cubical Tucker route for status words

Let (m=n-2). For a spanning order (pi), define the sign status vector
[
lambda(pi)_i=2epsilon_i(pi)-1in{-1,+1}.
]
The centered permutahedron boundary has the same dimension (m).

## Adjacent-transposition locality

If (pi') is obtained from (pi) by swapping positions (k,k+1), then only the status windows beginning at (k-2,k-1,k,k+1) can change. Thus the raw status vector has a strong four-coordinate locality that the extreme coordinates (p,q) do not preserve.

## Twisted antipodality and the odd mirrored projection

Reversal gives
[
lambda(pi^{m rev})=-Jlambda(pi),
]
where (J) reverses coordinates. The full status cube is therefore twisted rather than ordinarily antipodal.

Pair mirrored coordinates:
[
s_i(pi)=lambda_i(pi)+lambda_{m+1-i}(pi).
]
Then (s(pi^{m rev})=-s(pi)). The resulting odd map has target dimension (lceil m/2ceil), so Bourgin--Yang forces a zero locus of dimension at least (lfloor m/2floor). For far mirrored positions, one adjacent transposition cannot change (s_i) directly from (-2) to (+2).

## Face-poset Tucker output

Label a permutahedron face (F) by the first mirrored coordinate that is uniformly (+2) or uniformly (-2) on every chamber of (F). Inclusion of faces preserves a uniform sign, while reversal negates it. Tucker on the barycentric subdivision therefore forces a face with no uniformly signed mirrored coordinate. This avoids artificial triangulation diagonals.

## Face-average localization

For
[
F=B_1|cdots|B_k,
]
the average full status vector over all chamber permutations is supported only at the two positions adjacent to each block boundary. Every window lying in a single block cancels by swapping its first and third positions. This is [[permutahedron_face_status_localization]].

## Boolean cubes inside faces

The cancellation is actually joint. For any collection of pairwise disjoint three-position windows lying inside blocks, the endpoint swaps commute and independently flip the selected statuses. Hence every (0/1) assignment to those selected coordinates occurs equally often among the chambers. This is [[disjoint_status_windows_form_boolean_cubes]].

Thus large permutahedron faces contain honest cubical status geometry, not merely averaged zeros.

## Auxiliary-centered violations

In the auxiliary extension (H^+), put (r) in position (t). The construction forces
[
epsilon_{t-2}=1,qquad epsilon_t=0.
]
A left violation is a zero before this forced transition; a right violation is a one after it. Index by distance (d) from (r) and set
[
v_d=
1_{	ext{left violation at }d}
-
1_{	ext{right violation at }d}.
]
Then
[
v(pi^{m rev})=-v(pi).
]
No violations is precisely a directed one-change certificate. A zero violation vector instead means a perfectly mirrored violation pattern around (r), giving a rigid structural alternate output.

## Singleton faces and an ordinary tournament cut

Fix a partition (L|R) of the original vertices and consider
[
F_L=L|{r}|R.
]
By face-average localization, the average status vector vanishes everywhere except the three windows touching (r). The outer coordinates are forced (+1) and (-1). The middle coordinate is
[
rac1{|L||R|}sum_{uin L,win R}chi(u,r,w),
]
the normalized directed-cut imbalance of (L|R) in the ordinary local tournament (T_r).

Equivalently, if
[
b(u)=d^+_{T_r}(u)-d^-_{T_r}(u),
]
then the numerator is
[
sum_{uin L}b(u).
]

For odd (n=|V(H)|), every (n)-vertex tournament has a nonempty proper subset with zero imbalance sum. This follows from the standard length bound for minimal zero-sum integer sequences after dividing the even tournament imbalances by (2). Hence for odd (n) there exists (L) for which the entire singleton-face average is
[
0,ldots,0,+1,0,-1,0,ldots,0.
]
This is recorded as [[auxiliary_singleton_face_cut_imbalance]].

The limitation is important: the face factors as
[
operatorname{Perm}(L)	imesoperatorname{Perm}(R).
]
The averaged one-change pattern does not by itself imply a chamber with a one-change word; upgrading it requires coupling the two side permutations.

## Good words form a cubical ribbon

The exact criterion (qle p+1) says the good status words are precisely
[
1^a0^b
quad	ext{or}quad
1^a010^b.
]
These form the monotone cube geodesic together with the adjacent square vertices: a thin cubical ribbon. A counterexample labels every permutation vertex outside this ribbon.

## Discrete fixed-point route

The Iimura--Murota--Tamura fixed-point theorem applies to direction-preserving maps on finite integrally convex lattice sets. The integer points of a standard permutahedron form an M-convex, hence integrally convex, set. The GN3 field is currently defined only at permutation vertices, so the missing bridge is a canonical extension to all lattice points that preserves direction-preservation and makes fixed points correspond to no violations.

## Oriented transition-system formulation

For each vertex (v), define the ordinary tournament
[
u	o_{T_v}wiff (u,v,w)	ext{ is tight}.
]
Then a tight path is exactly a path in (K_n) whose transition at each internal vertex follows the local tournament orientation. This is [[boundary_tournaments_as_oriented_transition_systems]].

The comparison digraph is not generally locally semicomplete: two out-neighbors of one edge can leave through its two different endpoints and be disjoint. So standard locally-semicomplete Hamiltonicity does not apply.

Likewise the ordinary Gallai--Milgram theorem does not directly extend merely from the fact that every three-set contains a tight path. The missing axiom is precisely the two-step memory: merging two tight paths depends on terminal pairs, not one endpoint adjacency.

## Current global targets

1. Use the embedded Boolean cubes and face localization to strengthen the face-poset Tucker output from "mixed on every mirrored coordinate" to an actual chamber in the good cubical ribbon.
2. Exploit the auxiliary singleton faces: the interface reduces to one ordinary tournament cut, so the only unresolved part is simultaneous Hamiltonicity/one-change behavior on the two sides.
3. Extend the auxiliary violation direction field from permutation vertices to the integer permutahedron and test the Iimura--Murota--Tamura theorem directly.
4. Study minimal convex/positive dependencies among mirrored violation vectors; a zero supported only on bad chambers should correspond to a highly structured symmetric ladder.
5. Keep the line global and structural; no minimum-counterexample or disturbance analysis is needed.

## Minimum-deficiency face rigidity

Let \(k=\kappa_2(H)>0\), \(m=n-2\), and \(K=m-k\). For a spanning order write \(p,q,c\) for the exact inversion coordinates, so
\[
\delta=q-p-1=m-(p+c)\ge k.
\]

If \(\delta=k\), then
\[
p+c=K,\qquad q=p+k+1.
\]
Thus the minimum-deficiency exact-root graph is a disjoint union of complementary two-cycles
\[
p\leftrightarrow K-p
\]
and, when \(K\) is even, the possible diagonal loop \(K/2\to K/2\). Any odd exact-root cycle of length greater than one therefore contains a chamber of deficiency strictly greater than \(k\).

More strongly, assume \(k\ge2\). If adjacent chamber permutations \(\pi,\pi'\) both have deficiency \(k\), then they have the same exact root. Indeed, an adjacent transposition changes statuses only in four consecutive positions. If \(p\) moved while deficiency stayed \(k\), then \(q=p+k+1\) would have to move by the same amount. The old/new extreme positions that must both change are at least \(k+2\ge4\) apart, too far to lie in one affected four-position interval.

Hence on any connected permutahedral face all of whose chambers have deficiency \(k\), the exact root is constant. If such a face is a positive-balance carrier face of the exact-root map, that constant root must be zero. Therefore every chamber has
\[
p=c=K/2,\qquad q=p+k+1,
\]
so every chamber has the same balanced canonical size profile.

In this all-minimum zero-root branch, every status coordinate outside
\[
p+1,\ldots,q-1
\]
is fixed across the whole face: \(i<p\) is tight, \(i=p\) non-tight, \(i=q\) tight, and \(i>q\) non-tight. Face-average localization then implies that any block of size at least three must be contained in the positional corridor
\[
[p+1,q+1],
\]
of length \(k+2\). This corridor is exactly the \(k\)-vertex canonical hole plus one exposed terminal vertex from each canonical path.

The exact-root Bourgin--Yang theorem gives
\[
\dim\Psi^{-1}(0)\ge k+2.
\]
For the piecewise-linear zero set, some zero has a carrier face of dimension at least \(k+2\). On an all-minimum zero-root carrier, the \(k+2\)-position core can contribute at most \(k+1\) face dimensions. Hence at least one further dimension comes from a two-vertex block wholly outside the hole-plus-terminals core.

So for \(k\ge2\), some high-dimensional exact-zero carrier satisfies the structural dichotomy
\[
\boxed{
\text{it contains a chamber with }\delta>k
\quad\vee\quad
\text{it has an independent adjacent exchange inside one canonical path away from the hole core}.}
\]

This is the concrete form of the earlier "three extra zero-set dimensions" observation. Two extra dimensions beyond the obvious \(k-1\) hole-permutation face can be absorbed by the two exposed terminal vertices; at least one more must move outside that core unless the carrier already leaves the minimum-deficiency stratum.

### Current structural target

Exploit the exterior two-block in the all-minimum zero branch using face symmetry rather than disturbance analysis. The desired outcomes are: a support exchange among minimum \(k\)-holes, a forced higher-deficiency chamber within the same zero geometry, or a direct reduction to a \((k-1)\)-hole.


## Gauge-forced blocks from the exact-root dimension budget

Let
\[
k=\kappa_2(H)>0,\qquad m=n-2.
\]
The exact-root map of [[convex_root_balance_and_bourgin_yang]] takes values in a linear space of dimension at most
\[
m-k-2=n-k-4.
\]

For distinct actual vertices \(a,b\), define the relative-order gauge
\[
g_{ab}(\pi)=
\begin{cases}
+1,&a\text{ occurs before }b\text{ in }\pi,\\
-1,&b\text{ occurs before }a\text{ in }\pi.
\end{cases}
\]
Then
\[
g_{ab}(\pi^{\mathrm{rev}})=-g_{ab}(\pi).
\]

Let \(G\) be any forest on actual vertices with \(d\) edges, where
\[
d\le k+2.
\]
Append the \(d\) gauges \(g_e\), \(e\in E(G)\), to the exact-root map. Averaging at face barycenters and extending over the barycentric subdivision gives an odd continuous map
\[
\Theta_G:S^{n-2}\to W\oplus\mathbb R^d
\]
with
\[
\dim(W\oplus\mathbb R^d)\le n-k-4+d\le n-2.
\]
Hence Bourgin--Yang gives a zero; indeed
\[
\dim\Theta_G^{-1}(0)\ge k+2-d.
\]

Let \(F\) be the carrier face of such a zero. The carrier expansion has strictly positive weights on every chamber of \(F\). For each gauge edge \(ab\in E(G)\),
\[
\sum_{\pi\in\mathcal V(F)}\lambda_\pi g_{ab}(\pi)=0.
\]
Since every gauge value is \(\pm1\), both signs occur among the chambers of \(F\). In one ordered-partition face the relative order of \(a,b\) can vary iff they belong to the same face block. Therefore the endpoints of every edge of \(G\) lie in one common block. By connectivity, every connected component of \(G\) lies in a single face block.

Thus:

**Gauge-forced block theorem.** For every forest \(G\) with at most \(k+2\) edges, there exists a positive exact-root carrier face in which each connected component of \(G\) is contained in one block.

This is a direct topological control on actual vertices, not just switch coordinates.

### Consequence: k>=4 forces an exact diagonal chamber

Assume first \(k\ge5\). Take a tree on \(k+3\) prescribed vertices. It has \(k+2\) edges, so the gauge-forced carrier contains a block of order at least
\[
k+3\ge8.
\]
If the carrier had no zero exact root, the bounded-central-block theorem in [[topological_recurrence_to_local_gn3_structure]] would make every block have order at most seven, contradiction. Hence the carrier contains a chamber with
\[
p=c.
\]

For \(k=4\), use a forest with two connected components of orders \(5\) and \(3\), on eight distinct vertices. It has
\[
4+2=6=k+2
\]
edges. In a diagonal-free positive exact-root carrier every block except the unique central block has order at most two. Both forced components therefore lie in that same central block, which would then have order at least eight, again contradicting the seven-vertex bound.

Hence
\[
\boxed{k=\kappa_2(H)\ge4\Longrightarrow
\text{some spanning order has }p=c.}
\]

Equivalently, every counterexample at deletion distance at least four admits a canonical partial two-cover with equal left and right path orders.

This improves the previous threshold \(k\ge7\) obtained from the ungauged central-block theorem.

### The k=3 equality branch

Let \(k=3\). Use all five available gauges on a forest with connected components of orders \(4\) and \(3\). A diagonal-free carrier must place both components in the unique central block, so that block has order at least seven. The central-block theorem gives order at most seven, hence
\[
|B|=7.
\]
The mixed placement cases have \(b\le5\), so only the symmetric cases remain:
\[
(\ell,r)=(s,s)\quad\text{or}\quad(s+1,s+1).
\]
In either case \(n=\ell+7+r\) is odd.

Therefore
\[
\boxed{k=3,\ n\text{ even}\Longrightarrow\text{some chamber has }p=c.}
\]

If \(k=3\), \(n\) is odd, and no diagonal exists in the gauge-forced carrier, then the carrier is forced into a centered seven-block equality configuration, with every exterior block of order at most two. This is a genuine finite structural residue obtained without a minimum-counterexample hypothesis.

### Next target

Use the local forbidden-pattern path topology on the centered seven-block equality branch. Because all exact-root variability is already confined to the central seven-block and its immediate boundary data, the paired \(001/011/0101\) witness orientations should reduce the remaining \(k=3\) diagonal-free case to a finite rank-two compatibility problem rather than an arbitrary small-order search.


## The k=3 diagonal-free residue is impossible

The preceding gauge argument leaves, for \(k=3\), only a centered seven-block \(B\) in a hypothetical diagonal-free carrier. There are two symmetric placement cases. Both are impossible by a Kneser-graph covering argument.

### Case 1: ell=r=s, alpha=beta=2, L=5

Here
\[
m=2s+5.
\]
Write
\[
p=s+x,\qquad c=s+y.
\]
Since every chamber has deficiency at least \(k=3\),
\[
x+y\le2.
\]
No zero root is allowed, so every chamber has
\[
p=s\quad\text{or}\quad c=s.
\]

Choose one left outside-block order occurring in a chamber with \(p=s\), and independently one right outside-block order occurring in a chamber with \(c=s\). Fix these outside orders.

For a two-set \(E\subseteq B\), call \(E\) **left-full** if both orders of \(E\) in the first two positions of \(B\) force \(p=s\). Define **right-full** analogously for the final two positions read inward and the event \(c=s\).

Let \(E,F\) be disjoint two-sets.

- If \(E\) is not left-full and \(F\) is not right-full, choose avoiding orientations and place them at the two ends of \(B\). Then \(p,c\ge s+1\). The inequality \(x+y\le2\) forces \(p=c=s+1\), a zero root, contradiction.
- If \(E\) is left-full and \(F\) is right-full, place them at the two ends. Then \(p=c=s\), again a zero root.

Hence for every disjoint pair \(E,F\), exactly one of
\[
E\text{ left-full},\qquad F\text{ right-full}
\]
holds.

Any two two-sets \(E_1,E_2\subseteq B\) have a common disjoint two-set \(F\), since \(|B|=7\). Therefore
\[
E_1\text{ left-full}\iff F\text{ not right-full}\iff E_2\text{ left-full}.
\]
So all two-sets have the same left-full status.

If all are left-full, take any actual right witness for \(c=s\) and choose a disjoint two-set at the left end; this produces \(p=c=s\). If none are left-full, the exact-one rule makes every two-set right-full; combine one with an actual left witness. Both alternatives contradict the no-zero hypothesis.

Thus the \(L=5\) seven-block case is impossible.

### Case 2: ell=r=s+1, alpha=beta=1, L=7

The bounded-central-block proof gives a unique vertex \(z\in B\) such that every \(p=s\) witness starts \(B\) with \(z\), and every \(c=s\) witness ends \(B\) with \(z\) in the inward order.

Place \(z\) away from the first two and last two positions of \(B\). Then
\[
p,c\ge s+1.
\]
Now
\[
m=2s+7,\qquad \delta\ge3
\]
gives
\[
(p-s)+(c-s)\le4.
\]
If both \(p,c\ge s+2\), equality forces
\[
p=c=s+2,
\]
a zero root. Hence every chamber with \(z\) away from the two ends satisfies
\[
p=s+1\quad\text{or}\quad c=s+1.
\]

Such a chamber exists, so one of the coordinates \(s+1\) occurs. Exact-root coordinate recurrence implies that \(s+1\) occurs on the opposite side as well. Fix left and right outside orders from witnesses for \(p=s+1\) and \(c=s+1\).

Put
\[
U=B-\{z\},\qquad |U|=6.
\]
For a two-set \(E\subseteq U\), call it left-full if both orders in the first two \(B\)-positions force \(p=s+1\) under the fixed left outside order. Define right-full similarly on \(U\).

For disjoint \(E,F\subseteq U\), place \(E,F\) at the two ends and \(z\) in the middle.

- If neither is full, choose avoiding orientations. Then \(p,c\ge s+2\), forcing the zero root \(p=c=s+2\).
- If both are full, then \(p=c=s+1\), also a zero root.

Thus exactly one fullness condition holds on every disjoint pair. Any two two-sets of the six-element set \(U\) have a common disjoint two-set, so all two-sets again have the same left-full status.

If all are left-full, combine a disjoint left-full pair with any actual \(c=s+1\) witness; the witness pair may contain \(z\), but a disjoint pair in \(U\) still exists. This gives \(p=c=s+1\). If none are left-full, every two-set of \(U\) is right-full and the symmetric argument with an actual \(p=s+1\) witness gives the same contradiction.

Therefore the \(L=7\) seven-block case is also impossible.

Combining the two cases with the gauge-forced block reduction yields the global theorem
\[
\boxed{
\kappa_2(H)\ge3
\Longrightarrow
\text{there exists a spanning order with exact root }p=c.
}
\]

Equivalently, every boundary tournament whose minimum deletion distance to a two-cover is at least three admits a canonical partial two-cover with equal path orders. This is a global structural consequence of exact-root topology, gauge forcing, and Kneser connectivity; it uses no minimum-counterexample hypothesis.


## Updated consequence using the sharpened four-vertex central-block theorem

The concurrent Article VII sharpening in [[topological_recurrence_to_local_gn3_structure]] improves the diagonal-free positive exact-root carrier substantially: the unique central block has order at most four, every exterior block has order at most two, at most ten actual vertices determine the varying roots, and every simple directed root cycle has length two or three.

Combining this with the gauge-forced block theorem above immediately strengthens the global diagonal conclusion.

**Theorem.** If
\[
k=\kappa_2(H)\ge2,
\]
then some spanning order of \(H\) has exact root zero:
\[
p(\pi)=c(\pi).
\]

**Proof.** Since \(k+2\ge4\), choose four relative-order gauges whose forest consists of two disjoint three-vertex trees. By the gauge-forced block theorem, there is a positive exact-root carrier face \(F\) in which each of those two prescribed triples lies in one face block.

Suppose \(F\) contains no zero exact root. The sharpened central-block theorem then says that every exterior block has order at most two, so neither prescribed triple can lie in an exterior block. Both triples must therefore lie in the unique central block. They are disjoint, forcing that block to contain at least six actual vertices, contradicting the bound
\[
|B|\le4.
\]
Thus \(F\) contains a chamber with \(p=c\). \(\square\)

Hence
\[
\boxed{\kappa_2(H)\ge2\Longrightarrow\exists\pi\text{ with }p(\pi)=c(\pi).}
\]

The only deletion-distance layer not forced onto the exact diagonal by this global gauge argument is
\[
\kappa_2(H)=1.
\]

This subsumes the preceding \(k\ge3\) Kneser analysis. The latter remains useful as an independent proof under the earlier seven-block bound, but it is no longer the sharp frontier.

### Relation to the recovered omission-vector frontier

The rooted omission-vector argument in [[article_vii_synthesis_and_exact_frontier]] is complementary. It proves that strictly positive constant-vector omission balance yields a zero-omission chamber on every proper face except the two extreme auxiliary facets
\[
\{r\}\mid V,\qquad V\mid\{r\}.
\]
The matching-block four-vertex example shows those exceptional facets can genuinely carry projected topological zeros with no zero-omission chamber.

Thus the current global structural frontier is now:

1. exact-root topology plus gauges forces every counterexample with \(\kappa_2\ge2\) onto an exact diagonal \(p=c\);
2. nonzero exact-root recurrent faces reduce to central blocks of order at most four and root cycles of length two or three;
3. rooted omission balance would solve the conjecture away from two explicit exceptional facets;
4. the unresolved conversion is to use the extra diagonal/root structure to force an omission zero outside those facets, or to extract a two-cover directly from an exceptional-facet balance.

No minimum-counterexample or disturbance argument is used in any of these four statements.


## Mixed-direction omission quotients and almost-total r-block localization

Let \(H^+\) be the auxiliary extension with rooted omission vectors
\[
D(\pi)=\mathbf 1_{A(\pi)}-\mathbf 1_{B(\pi)}
\in\mathbb R^{V(H)}.
\]
For distinct actual vertices \(a,b\), put
\[
w_{ab}=e_a-e_b.
\]
Project \(D\) to
\[
\mathbb R^{V(H)}/\langle w_{ab}\rangle.
\]
The target has dimension \(n-1\), equal to the dimension of the permutahedron boundary of \(H^+\). Averaging on face barycenters and extending over the barycentric subdivision gives an odd continuous map, so Borsuk--Ulam gives a zero.

Let \(F\) be the carrier face. Then there are strictly positive chamber weights with
\[
\sum_{\pi\in\mathcal V(F)}\lambda_\pi D(\pi)
=
c(e_a-e_b).
\]
Therefore every vertex
\[
v\in Z:=V(H)-\{a,b\}
\]
has average omission coordinate zero.

Let \(B_r\) denote the face block containing the auxiliary vertex \(r\).

**Localization lemma.** If some \(z\in Z\) lies outside \(B_r\), then
\[
\kappa_2(H)\le2.
\]

**Proof.**
Because \(z\) lies strictly to one side of the \(r\)-block, its side of \(r\) is fixed throughout the face. Hence its omission coordinate is always in \(\{0,1\}\) or always in \(\{0,-1\}\). Its strictly positive weighted average is zero, so
\[
D(\pi)_z=0
\]
for every chamber.

Now let \(u\in Z\) be arbitrary. If \(u\) lies in a face block distinct from the block of \(z\), the threshold form of the omission vectors gives a fixed coordinate inequality between \(D_z\) and \(D_u\) in every chamber. Their averages are both zero, so positivity forces equality chamberwise. Hence \(D_u=0\). If all of \(Z\) lies in the same block as \(z\), that block is still strictly to one side of \(r\), so every \(Z\)-coordinate has one fixed sign and zero average and is again identically zero.

Thus every chamber omits only vertices from \(\{a,b\}\). Removing \(r\) from its two rooted paths gives a two-path cover of
\[
H-\{a,b\},
\]
so
\[
\kappa_2(H)\le2.
\]
\(\square\)

Consequently, under the structural hypothesis
\[
\kappa_2(H)\ge3,
\]
every mixed-direction zero carrier satisfies
\[
(V(H)-\{a,b\})\cup\{r\}\subseteq B_r.
\]
That is, all but at most two original vertices lie in the same face block as the auxiliary vertex.

This quotient automatically bypasses the two exceptional facets of the constant-vector omission projection: on \(\{r\}|V\) all omission coordinates are nonpositive, and on \(V|\{r\}\) they are nonnegative, so a nonzero multiple of \(e_a-e_b\) cannot occur there.

If the scalar \(c\) is zero, then the full average omission vector is zero. On every proper nonexceptional face the localization proposition in [[article_vii_synthesis_and_exact_frontier]] then forces an actual zero-omission chamber. Hence a counterexample in the \(\kappa_2\ge3\) branch must have
\[
c\ne0
\]
and an almost-total \(r\)-block.

### Parameterized quotient target

Replace \(e_a-e_b\) by
\[
w_t=e_a-t e_b,\qquad t>0.
\]
For every \(t\), the quotient remains dimension-tight. Under \(\kappa_2(H)\ge3\), every projected zero is trapped in the same almost-total \(r\)-block geometry.

As \(t\to0\) and \(t\to\infty\), the quotient directions approach the one-coordinate directions \(e_a\) and \(-e_b\). This suggests a parameterized Borsuk--Ulam / mod-two continuation argument: the zero set of the family
\[
(x,t)\longmapsto \operatorname{proj}_{w_t^\perp}D(x)
\]
should form a one-dimensional cobordism between the two endpoint facet regimes. Any transition that escapes the almost-total \(r\)-block family would give either \(\kappa_2(H)\le2\) by the localization lemma or a full omission zero.

The remaining task is therefore a two-anchor continuation problem on faces with one giant \(r\)-block, not the original unrestricted omission-balance problem.


## Exact nearest-violation map and singleton-center closure

The auxiliary violation vector can be compressed further while keeping exact chamber zeros.

Fix an original vertex \(a\). For a chamber \(\pi\) of the auxiliary extension \(H^+\), let
\[
d(\pi)=\min\{d:x_d(\pi)=1\text{ or }y_d(\pi)=1\},
\]
with \(d(\pi)=\infty\) when there are no violations. Let
\[
g_a(\pi)=
\begin{cases}
+1,&a\text{ occurs before }r,\\
-1,&a\text{ occurs after }r.
\end{cases}
\]
Reversal interchanges left and right violations and reverses the relative order of \(a,r\), so \(g_a(\pi^{\rm rev})=-g_a(\pi)\).

Let \(D=n-2\) be the number of possible positive violation radii and let
\[
e_1,\ldots,e_D,e_*
\]
be the standard basis of \(\mathbb R^{D+1}=\mathbb R^{n-1}\). Define the **nearest-violation label**
\[
N_a(\pi)=
\begin{cases}
0,&d(\pi)=\infty,\\
+e_d,&d(\pi)=d,\ (x_d,y_d)=(1,0),\\
-e_d,&d(\pi)=d,\ (x_d,y_d)=(0,1),\\
g_a(\pi)e_*,&d(\pi)=d,\ (x_d,y_d)=(1,1).
\end{cases}
\]
Then
\[
N_a(\pi^{\rm rev})=-N_a(\pi),
\]
and
\[
N_a(\pi)=0
\iff
\pi\text{ has no violations}
\iff
\pi\text{ is a directed one-change order}.
\]

Average \(N_a\) over each proper face of the auxiliary permutahedron and extend affinely over the barycentric subdivision. Since the boundary is \(S^{n-1}\) and the target is \(\mathbb R^{n-1}\), Borsuk--Ulam gives a zero. As usual, its carrier face \(C\) has strictly positive chamber weights
\[
\lambda_\pi>0,\qquad
\sum_{\pi\in\mathcal V(C)}\lambda_\pi N_a(\pi)=0.
\]

The basis-coordinate structure makes this balance completely transparent:

- for every used radius \(d\), the total positive weight of nearest left-only labels \(+e_d\) equals the total positive weight of nearest right-only labels \(-e_d\);
- the total weight of nearest-double chambers with \(g_a=+1\) equals the total weight of nearest-double chambers with \(g_a=-1\).

### Theorem: every singleton-r carrier closes

Assume \(r\) is a singleton block of the carrier face \(C\). Then \(g_a\) is constant throughout \(C\), because the block containing \(a\) lies strictly on one fixed side of the singleton block \(\{r\}\).

If \(H\) had no two-cover, no chamber of \(C\) could have \(N_a=0\). The \(e_*\)-balance would then force there to be no nearest-double chamber at all: every double label has the same sign \(g_a e_*\), and all carrier weights are positive.

Hence every chamber label is a single signed basis vector \(\pm e_d\). For every radius \(d\) that occurs, both orientations occur.

Let \(d_{\max}\) be the largest nearest-violation radius occurring among chambers of \(C\). Choose
\[
\pi_L,\pi_R\in\mathcal V(C)
\]
with nearest labels
\[
N_a(\pi_L)=+e_{d_{\max}},
\qquad
N_a(\pi_R)=-e_{d_{\max}}.
\]
Thus both chambers have no violation at any smaller radius; \(\pi_L\) has a left-only violation at \(d_{\max}\), while \(\pi_R\) has a right-only violation there.

Because \(r\) is a singleton block, every left violation condition depends only on the orders of face blocks strictly left of \(r\), and every right violation condition depends only on the orders of blocks strictly right of \(r\). Form a new chamber \(\sigma\in\mathcal V(C)\) by taking all left-side block orders from \(\pi_R\) and all right-side block orders from \(\pi_L\). Then \(\sigma\) has no left or right violation at any radius at most \(d_{\max}\).

If \(\sigma\) had any farther violation, its nearest-violation radius would be greater than \(d_{\max}\), contradicting maximality of \(d_{\max}\) over all chambers of \(C\). Therefore \(\sigma\) has no violations at all:
\[
N_a(\sigma)=0.
\]
This is a directed one-change order, hence a spanning two-cover of \(H\).

Therefore
\[
\boxed{
\text{every positive zero carrier of the nearest-violation map with }r\text{ singleton contains an actual two-cover certificate.}
}
\]

Equivalently, under the counterexample hypothesis every zero carrier of this exact dimension-tight map must place the auxiliary vertex \(r\) in a non-singleton face block.

This strengthens [[fixed_center_violation_intermediate_value]]: no iterative path argument is needed once nearest violations are separated into independent basis coordinates. The left/right product structure across a singleton \(r\) allows the two opposite maximal-radius witnesses to be spliced directly.

### Consequence for the current frontier

Together with the recovered omission-vector analysis, the remaining topological obstruction is now sharply localized:

1. projected omission zeros can be trapped only by the two exceptional extreme facets;
2. the exact violation map escapes those facets;
3. the nearest-violation refinement closes every carrier in which \(r\) is singleton;
4. hence a hypothetical counterexample must realize an exact nearest-violation zero on a proper face whose \(r\)-block contains at least one original vertex.

The next target is therefore not a generic facewise conversion theorem. It is the much narrower problem of controlling one non-singleton block containing \(r\).
