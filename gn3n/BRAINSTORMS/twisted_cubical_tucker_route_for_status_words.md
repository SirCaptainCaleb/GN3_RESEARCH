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
