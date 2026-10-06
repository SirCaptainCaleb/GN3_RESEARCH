# Relative-index filtration proves terminalization

## Metadata

- ID: relative_index_filtration_and_the_mixed_face_outward_push_lemma
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 2
- Row version: 2
- Development version: 2
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Relative-index filtration proves terminalization

Order the fixed witness-path edges from the center outward as
[
e_1,e_2,ldots,e_d,
]
where the witness-edge space has dimension
[
d=m-2,qquad m=n-2.
]
For a bad spanning-order chamber (pi), let (ho(pi)in{1,ldots,d}) be the depth of its selected witness edge, and let its orientation on (e_{ho(pi)}) be (+) or (-). Reversal preserves depth and reverses orientation.

The finite terminal theorem supplies the following local dichotomy in the form needed here:

> **Mixed-face escape dichotomy.** Fix (r). If a proper permutahedron face contains chambers of both orientations (+e_r) and (-e_r), then either it contains a chamber whose selected witness has depth (>r), or its determining windows are one of the classified terminal finite configurations. In the latter case the local two-cover supplied by the finite terminal theorem splices with the protected exterior and yields a spanning two-cover.

Thus, under the standing assumption that (H) is a counterexample, every face containing both orientations of (e_r) contains a chamber of strictly greater witness depth.

### The depth-filtered face posets

For (r=1,ldots,d+1), let (mathcal P_r) be the poset of nonempty proper faces (F) of the permutahedron for which (F) contains at least one chamber (pi) with
[
ho(pi)ge r.
]
For (r=d+1), interpret (ho(pi)ge d+1) as saying that (pi) has no forbidden local witness. By the forbidden-pattern theorem, such a chamber already gives a spanning two-cover.

Let
[
Y_r=Delta(mathcal P_r)
]
be the order complex. The antipodal involution acts freely on every (Y_r). If (H) is a counterexample then every chamber has a witness, hence
[
Y_1=operatorname{sd}(partial P)cong S^m.
]

### Canonical separator at one witness depth

Fix (rle d). For (Finmathcal P_r), define
[
s_r(F)in{-1,0,+1}
]
as follows:
- (s_r(F)=+1) if (F) contains a (+e_r) chamber and no (-e_r) chamber;
- (s_r(F)=-1) if (F) contains a (-e_r) chamber and no (+e_r) chamber;
- (s_r(F)=0) otherwise.

Thus (s_r(F)=0) exactly when either (F) contains no depth-(r) chamber, or it contains both orientations.

The labeling is odd:
[
s_r(-F)=-s_r(F).
]

It is also monotone enough along chains to forbid a direct sign conflict. If
[
Fsubseteq G
]
and (s_r(F)=+1), then (G) still contains the (+e_r) chamber already present in (F), so (s_r(G)
e-1). Symmetrically a negative face cannot be contained in a positive face. Consequently no simplex of (Y_r) contains both a (+1) and a (-1) vertex.

Extend (s_r) affinely over (Y_r). Its zero set is therefore exactly the full subcomplex
[
Sigma_r:=Delta{Finmathcal P_r:s_r(F)=0}.
]
The complement (Y_r-Sigma_r) has two exchanged sign regions and admits an equivariant map to (S^0).

### Every separator face is already one level farther out

Let (F) be a vertex of (Sigma_r).

If (F) contains no depth-(r) chamber, then because (Finmathcal P_r) it contains some chamber of depth (>r). Hence
[
Finmathcal P_{r+1}.
]

If (F) contains both orientations of (e_r), the mixed-face escape dichotomy applies. In a counterexample the terminal branch is impossible, so again (F) contains a chamber of depth (>r), and therefore
[
Finmathcal P_{r+1}.
]

Hence
[
oxed{Sigma_rsubseteq Y_{r+1}.}
]

This is the crucial point. No coherent choice of an (e_r)-free chamber or subface is needed: the separator consists of permutahedron faces themselves, and each separator face simply survives as a vertex of the next depth-filtered face poset.

### The index-drop inequality

Use the (mathbb Z_2)-genus
[
gamma(X)=min{k:	ext{there is an equivariant map }X	o S^{k-1}}.
]
We claim
[
oxed{gamma(Y_{r+1})gegamma(Y_r)-1.}
]

Indeed, let (gamma(Sigma_r)=k). Choose an equivariant map
[
f:Sigma_r	o S^{k-1}subsetmathbb R^k.
]
Because (Y_r) is a finite free (mathbb Z_2)-complex, extend (f) equivariantly to a continuous map
[
widetilde f:Y_r	omathbb R^k.
]
The pair
[
xlongmapstoigl(widetilde f(x),,s_r(x)igr)inmathbb R^{k+1}
]
never vanishes: on (s_r^{-1}(0)=Sigma_r), the first coordinate has norm one, while off (Sigma_r) the last coordinate is nonzero. After normalization this is an equivariant map
[
Y_r	o S^k.
]
Therefore
[
gamma(Y_r)le k+1=gamma(Sigma_r)+1.
]
Since (Sigma_rsubseteq Y_{r+1}), monotonicity of genus gives
[
gamma(Y_{r+1})
gegamma(Sigma_r)
gegamma(Y_r)-1.
]

### Iteration

Because
[
Y_1cong S^m,
qquad
gamma(Y_1)=m+1,
]
iteration yields
[
gamma(Y_r)ge m-r+2.
]
In particular, with (d=m-2),
[
gamma(Y_{d+1})
ge
m-(d+1)+2
=
3.
]
Hence (Y_{d+1}) is nonempty.

But a vertex of (Y_{d+1}) is a proper permutahedron face containing a chamber with no local forbidden witness. By the exact forbidden-pattern theorem, that chamber satisfies the two-cover criterion. This contradicts the assumption that (H) is a counterexample.

Therefore the terminalization recursion closes:

[
oxed{
	ext{finite terminal theorem}
+
	ext{relative-index depth filtration}
Longrightarrow
operatorname{pc}(H)le2.
}
]

### Balanced-carrier form of the recursion

The same argument recovers the requested outward balanced carrier at each stage.

For (Finmathcal P_r), let
[
A_r(F)={piinmathcal V(F):ho(pi)ge r}.
]
At the barycentric vertex corresponding to (F), average the oriented witness vectors over (A_r(F)), and extend affinely over (Y_r). This is an odd map into the span of
[
e_r,ldots,e_d.
]
The genus bound above is larger than the dimension of that target, so the map has a zero. In the smallest simplex carrying a zero, the top face contributes a strictly positive coefficient to every chamber in (A_r(F)). Hence one obtains a positive balanced carrier supported entirely on witness depths at least (r).

Applying the index-drop step gives (Y_{r+1}) with the same surplus of genus over the remaining witness-space dimension, and the corresponding relative averaging map gives a new positive balanced carrier supported entirely on depths at least (r+1). Thus from a carrier with innermost witness edge (e_r), the global separator mechanism yields either the finite terminal/two-cover branch or a new balanced carrier strictly farther outward.

The important conceptual simplification is that the new carrier need not be extracted by reweighting the old non-antipodal face. It is regenerated from the invariant depth-filtered face poset, where the separator carries one less witness depth but loses at most one unit of (mathbb Z_2)-index.

## Frontier

- Development version when composed: None
- Development version now: 2
