# Persistent-label successful-exchange transport

## Statement

Persistent-label successful-exchange transport: exterior-extension amplification, two dual-good vertices, a fixed pair covering every middle position with at most six label/failure types, strict-alternation normalization, and exact shifted two-cut complement structure when one non-Hamiltonian four-deletion repeats.

## Body

# Persistent-label transport in successful-exchange states

Let `H` be a boundary tournament, let `S` be a non-Hamiltonian five-vertex set, and let `z` be a vertex outside `S`.

Define
`D={u in S : H[S-{u}] is Hamiltonian}`
and
`E_z={u in D : H[(S-{u}) union {z}] is Hamiltonian}`.

Then
`|D-E_z|<=1`.

In particular, since every non-Hamiltonian five-set has at least four Hamiltonian four-deletions,
`|E_z|>=3`.

## Proof

Take any two distinct vertices `u,v in D` and put `C=S-{u,v}`. Then `C` has three vertices, so choose any tight Hamilton path `P_C` on `C`.

Apply the fixed-three-path extension theorem in the local Hamilton-extension module to `P_C` and the exterior vertices `u,v,z`. At least one of
`C union {u,v}=S`,
`C union {u,z}=(S-{v}) union {z}`,
`C union {v,z}=(S-{u}) union {z}`
is Hamiltonian.

The first is non-Hamiltonian by hypothesis. Therefore at least one of the latter two is Hamiltonian, meaning at least one of `u,v` lies in `E_z`.

Thus no two distinct elements of `D` can both lie outside `E_z`, so `|D-E_z|<=1`.

The five-vertex deletion theorem gives `|D|>=4`, hence `|E_z|>=|D|-1>=3`. ∎

## Consequences

This is the parent mechanism behind the successful-exchange side-extension amplification: taking `z=ell` and `z=r` gives two extension families, each missing at most one good deletion, so their intersection has order at least two. The statement is independent of any codimension-five decomposition.

# Two dual-good exterior vertices

Let `K` be a boundary tournament with `pc(K)>2`. Suppose
`Q=(y_0,M,y_k)`
and
`P=(ell,M,r)`
are tight paths with `|M|>=2`, all four displayed endpoint vertices distinct and outside `M`. Let `T` be a three-vertex set disjoint from these vertices and from `M`, assume
`V(K)=V(M) disjoint-union {y_0,y_k,ell,r} disjoint-union T`,
and put
`S=T union {y_0,y_k}`.
Assume `K[S]` is non-Hamiltonian.

Define
`D={u in S : K[S-{u}] is Hamiltonian}`.
Then `|D|>=4`.

For `u in D`, put
`u in L`
iff `K[(S-{u}) union {ell}]` is Hamiltonian, and
`u in R`
iff `K[(S-{u}) union {r}]` is Hamiltonian.

Then
`|D-L|<=1`,
`|D-R|<=1`,
and hence
`|L intersection R|>=|D|-2>=2`.
Moreover
`L intersection R subseteq T`.

Consequently there are distinct `u,v in T` such that, for each `x in {u,v}`,
both
`K[(S-{x}) union {ell}]`
and
`K[(S-{x}) union {r}]`
are Hamiltonian, while both
`K[M union {ell,x}]`
and
`K[M union {r,x}]`
are non-Hamiltonian.

Thus each of `u,v` cannot be inserted into any position of either tight Hamilton path `(ell,M)` or `(M,r)`, and the local insertion-obstruction theorem gives a bounded obstruction on each side for each vertex.

## Proof

Because `S` is a non-Hamiltonian five-vertex boundary tournament, at most one of its five four-vertex deletions is non-Hamiltonian. Thus `|D|>=4`.

Take distinct `u,v in D` and put `C=S-{u,v}`. Choose a tight Hamilton path on the three-set `C`. Apply the fixed-three-path extension theorem to this path and the exterior vertices `u,v,ell`. At least one of
`S=C union {u,v}`,
`(S-{v}) union {ell}=C union {u,ell}`,
and
`(S-{u}) union {ell}=C union {v,ell}`
is Hamiltonian. Since `S` is not, at least one of `u,v` lies in `L`.

Thus no two vertices of `D` can both lie outside `L`, proving `|D-L|<=1`. The identical argument with `r` gives `|D-R|<=1`. Hence
`|L intersection R| >= |L|+|R|-|D| >= |D|-2 >=2`.

Fix `x in L intersection R`. Since `(S-{x}) union {ell}` is Hamiltonian, its complementary vertex set in `K` is
`M union {r,x}`.
If that complement were Hamiltonian, the two complementary Hamilton paths would form a spanning two-path cover of `K`; hence it is non-Hamiltonian. Similarly Hamiltonicity of `(S-{x}) union {r}` forces
`K[M union {ell,x}]`
non-Hamiltonian.

It remains to exclude `x=y_0,y_k`. The two tight paths `Q=(y_0,M,y_k)` and `P=(ell,M,r)` imply that both
`(y_0,M,r)`
and
`(ell,M,y_k)`
are tight: all internal triples lie in `M`, and the two endpoint triples are inherited one from each of `Q,P`.

If `x=y_0`, the set `M union {r,x}` is Hamiltonian via `(y_0,M,r)`, contradicting the preceding non-Hamiltonicity. If `x=y_k`, the set `M union {ell,x}` is Hamiltonian via `(ell,M,y_k)`, again a contradiction. Therefore every vertex of `L intersection R` lies in `T`.

So at least two distinct vertices `u,v in T` have both side extensions Hamiltonian and both complementary long-side enlargements non-Hamiltonian. Since `(ell,M)` and `(M,r)` are Hamiltonian paths, non-Hamiltonicity after adjoining `x` means insertion of `x` fails in every position of each displayed path. The local insertion-obstruction theorem then supplies the stated bounded obstruction on each side. ∎

# Two persistent noninsertable labels on the common middle

Let `K` be a boundary tournament with `pc(K)>2`. Suppose
`Q=(y_0,M,y_k)`
and
`P=(ell,M,r)`
are tight paths with the same middle `M`, and let `T` be a disjoint three-vertex set such that
`V(K)=V(M) disjoint-union {y_0,y_k,ell,r} disjoint-union T`.
Put
`S=T union {y_0,y_k}`
and assume `K[S]` is non-Hamiltonian.

Then there exist distinct `u,v in T` such that each of `u,v` cannot be inserted into any position of the displayed tight path `M). Consequently the local insertion-obstruction theorem gives two bounded comparison-digraph obstruction patterns on the same path `M`, one for `u` and one for `v`.

## Proof

By the two-sided obstruction theorem for this configuration, there are distinct `u,v in T` such that for each `x in {u,v}`, both
`K[M union {ell,x}]`
and
`K[M union {r,x}]`
are non-Hamiltonian.

The small-order theorem implies that every boundary tournament with path-cover number greater than two has more than ten vertices. Since the five vertices outside
`V(Q)={y_0} union V(M) union {y_k}`
are `F={ell,r} union T`, it follows that `|V(Q)|>=6). Therefore `M` has order at least four.

Fix `x in {u,v}` and suppose that inserting `x` at some position of
`M=(m_1,...,m_h)`
produces a tight Hamilton path `R` on `M union {x}`, where `h>=4`. Number insertion positions by `j=0,...,h`, where `j` is the number of old vertices of `M` preceding `x`.

If `j>=2`, the first two vertices of `R` remain `m_1,m_2`. Since `(ell,m_1,m_2)` is tight as the first triple of `P`, prepending `ell` to `R` gives a Hamilton tight path on
`M union {ell,x}`,
contradicting its non-Hamiltonicity.

If `j<=h-2`, the last two vertices of `R` remain `m_{h-1},m_h`. Since `(m_{h-1},m_h,r)` is tight as the last triple of `P`, appending `r` to `R` gives a Hamilton tight path on
`M union {r,x}`,
again a contradiction.

Because `h>=4`, every insertion position `j` satisfies at least one of
`j>=2`
or
`j<=h-2`.
Hence no insertion position succeeds. Thus `x` is noninsertable into `M`.

This holds for both distinct vertices `u,v`. Applying the local insertion-obstruction theorem separately to `(M,u)` and `(M,v)` gives the asserted bounded obstruction patterns. ∎

# Adjacent common deletion or strict alternation

Let `K` be a boundary tournament with `pc(K)>2`. Suppose
`Q=(y_0,p_1,...,p_h,y_k)`
and
`P=(ell,p_1,...,p_h,r)`
are tight paths with common middle
`M=(p_1,...,p_h)`,
where `h>=2`. Let `T` be a disjoint three-vertex set completing the vertex partition, put
`S=T union {y_0,y_k}`,
and assume `K[S]` is non-Hamiltonian.

Let
`D={d in S:K[S-{d}] is Hamiltonian}`.
For any vertex `z notin S`, put
`E(z)={d in D:K[(S-{d}) union {z}] is Hamiltonian}`.
Set
`L=E(ell)`,
`R=E(r)`,
and
`C=L intersection R`.

Then:

1. `|D-E(z)|<=1` for every `z notin S`;
2. `|D|>=4`, `|L|>=|D|-1`, `|R|>=|D|-1`, and hence `|C|>=|D|-2>=2`;
3. for every set of middle indices `I`,
   `|C intersection intersection_{i in I} E(p_i)| >= |C|-|I|`.

In particular, if `|C|>=3`, then every adjacent pair
`p_i,p_{i+1}`
has some
`d in C`
such that all four five-sets
`(S-{d}) union {ell}`,
`(S-{d}) union {r}`,
`(S-{d}) union {p_i}`,
and
`(S-{d}) union {p_{i+1}}`
are Hamiltonian.

Suppose instead that no adjacent pair of middle vertices has such a common deletion. Then necessarily:

- `|D|=4`;
- `|L|=|R|=3`;
- the unique elements
  `alpha in D-L`
  and
  `beta in D-R`
  are distinct;
- `C=D-{alpha,beta}={u,v}` for distinct `u,v`;
- for every `i`, the set `E(p_i) intersection C` is a singleton;
- these singletons alternate strictly along the middle.

More explicitly, after possibly interchanging `u,v`,
`E(p_i)=D-{v}`
for odd `i`, and
`E(p_i)=D-{u}`
for even `i`.

Thus the failure of an adjacent common deletion forces a unique four-deletion normal form whose bad deletion alternates between two fixed vertices along the entire middle path.

## Proof

The exterior-extension theorem for a non-Hamiltonian five-set gives
`|D-E(z)|<=1`
for every exterior vertex `z`. The small-order theorem gives
`|D|>=4`.

Applying the extension theorem to `ell` and `r` gives
`|L|,|R|>=|D|-1`, so
`|C|=|L intersection R|>=|L|+|R|-|D|>=|D|-2>=2`.

For a set of indices `I`, each complement
`C-E(p_i)`
has order at most one. Therefore
`C-(intersection_{i in I}E(p_i))`
is contained in the union of `|I|` sets of order at most one. Hence
`|C intersection intersection_{i in I}E(p_i)|>=|C|-|I|`.
Taking `I={i,i+1}` proves the adjacent-pair assertion whenever `|C|>=3`.

Now assume no adjacent pair has a common deletion in `C`. Since `|C|>=2`, the preceding paragraph forces `|C|=2`. Because `|C|>=|D|-2` and `|D|>=4`, we obtain `|D|=4`.

Also `|L|,|R|>=3`. If either had order four, then its intersection with the other would have order at least three, contrary to `|C|=2`. Thus `|L|=|R|=3`. Their omitted elements `alpha,beta` must be distinct, otherwise `L=R` and `|C|=3`. Therefore
`C=D-{alpha,beta}`.

Write `C={u,v}`. For each `i`, the extension theorem says that at most one element of `D`, hence at most one element of `C`, can fail to lie in `E(p_i)`. Thus `E(p_i) intersection C` is nonempty. It cannot equal all of `C`, because then it would intersect the corresponding set for either neighbor, contradicting the assumed absence of an adjacent common deletion. Hence every `E(p_i) intersection C` is a singleton.

Two consecutive nonempty singleton subsets of `{u,v}` must be different, again because their intersection is empty. Hence the singleton labels alternate.

Finally, if `E(p_i) intersection C={u}`, then `v notin E(p_i)`. Since `D-E(p_i)` has order at most one, every other element of `D` lies in `E(p_i)`, so `E(p_i)=D-{v}`. The case with `u,v` interchanged is identical. ∎

# Fixed pair covers every successful-exchange middle position

Use the notation in the statement.

## Proof

By the two-dual-good-vertices theorem above, there exist distinct `u,v in T` such that both `u` and `v` lie in the Hamiltonian-deletion set
`D={x in S : K[S-{x}] is Hamiltonian}`,
and, for each `x in {u,v}`, both side extensions
`K[(S-{x}) union {ell}]` and `K[(S-{x}) union {r}]`
are Hamiltonian.

Fix a middle position `p_i`. Apply the exterior-extension amplification theorem `the exterior-extension theorem above` to the non-Hamiltonian five-set `S` and exterior vertex `p_i`. Among the vertices of `D`, at most one fails to satisfy that
`K[(S-{x}) union {p_i}]`
is Hamiltonian. Since `u` and `v` are two distinct members of `D`, at least one of them, call it `x_i`, has this Hamiltonian `p_i`-extension.

For this same `x_i`, the two side extensions by `ell` and `r` are Hamiltonian by the fixed choice of `u,v`. Thus all three five-sets
`(S-{x_i}) union {ell}`,
`(S-{x_i}) union {r}`,
`(S-{x_i}) union {p_i}`
are Hamiltonian.

Now consider
`R_i=(V(P)-{p_i}) union {x_i}`.
The complement of `R_i` in `V(K)` is exactly `(S-{x_i}) union {p_i}`, which is Hamiltonian. If `K[R_i]` were Hamiltonian, these two complementary Hamilton paths would form a spanning two-path cover of `K`, contradicting `pc(K)>2`. Hence `K[R_i]` is non-Hamiltonian.

The displayed replacement sequence
`(ell,p_1,...,p_{i-1},x_i,p_{i+1},...,p_h,r)`
spans `R_i`. Every consecutive triple not meeting `x_i` is inherited from the tight path `P`, so at least one of the at most three consecutive triples meeting `x_i` is non-tight. By reversal antisymmetry, the corresponding reverse triple is tight.

Thus every middle position can be labeled using one fixed pair `{u,v}` and one of the three possible local replacement failures. There are therefore at most six label/failure types. ∎

This sharpens the corresponding variable-label formulation. The useful point is not merely the smaller count: the same two exterior vertices now persist across the entire middle, so adjacent or repeated local obstruction patterns can be compared without changing the exterior labels.

# Shifted two-cut complements from a non-Hamiltonian four-set

## Endpoint lemma

Let `S=A union {gamma}` be a five-vertex set in a boundary tournament, with `|A|=4`. Assume both `K[S]` and `K[A]` are non-Hamiltonian. If `d in A` and `K[S-{d}]` is Hamiltonian, then `K[S-{d}]` has a Hamilton tight path with `gamma` at an endpoint.

## Proof

Because `K[S]` is a non-Hamiltonian five-set, it has an edge-order representation. Because `K[A]` is non-Hamiltonian, the three opposite-edge perfect matchings of `A` occur as three strict blocks.

Write
`A-{d}={x,y,z}`
and relabel these three vertices so that
`xy<yz<xz`.
The three displayed edges belong to the three different matching blocks. Their opposite edges in `A` are respectively
`dz,dx,dy`.
Hence the block order gives
`dz<yz<dy`.

Suppose, for contradiction, that no Hamilton path of `S-{d}` has `gamma` at an endpoint. The three-vertex orders
`(x,y,z)`, `(y,x,z)`, and `(y,z,x)`
are increasing on their two consecutive edges. Failure to attach `gamma` at their available ends gives
`xy<xgamma<xz`,
`zgamma<yz<ygamma`.

Since `S-{d}` is Hamiltonian, it has an increasing Hamilton path, and by assumption `gamma` is internal in every such path. Checking the two possible internal positions against these four inequalities leaves only two possible comparison patterns:
`xgamma<gammaz<yz`
or
`yz<ygamma<gammax`.

In the first case,
`(x,gamma,z,y,d)`
is increasing, because
`xgamma<gammaz<zy<yd`
and `zy=yz<dy=yd`.

In the second case,
`(d,z,y,gamma,x)`
is increasing, because
`dz<zy<ygamma<gammax`
and `dz<yz=zy`.

Either way `K[S]` has a Hamilton path, contradicting its non-Hamiltonicity. Therefore some Hamilton path of `S-{d}` has `gamma` at an endpoint. ∎

## Strict-alternation consequence

Now work in the strict-alternation successful-exchange configuration. Thus
`S={u,v,gamma,y_0,y_k}`,
`A=S-{gamma}` is the unique non-Hamiltonian four-deletion of `S`, and
`P=(ell,p_1,...,p_h,r)`.
For odd middle indices the unique failed deletion is `v`, and for even middle indices it is `u`.

Let `p_i,p_j` have the same parity, and let `d=v` for odd parity and `d=u` for even parity. Then
`K[(S-{d}) union {p_i}]`
and
`K[(S-{d}) union {p_j}]`
are non-Hamiltonian, while `K[S-{d}]` is Hamiltonian.

By the endpoint lemma choose a Hamilton path
`(a,b,c,e)`
of `S-{d}` with `gamma` equal to `a` or `e`. Apply `the repeated-middle-defect complementary-support theorem` to the repeated failed deletion `d`.

If `gamma=e`, the first Hamiltonian five-set from `the repeated-middle-defect complementary-support theorem` is
`(S-{d,gamma}) union {p_i,p_j}`,
and its complementary support is
`{d,gamma} union (V(P)-{p_i,p_j})`.

If `gamma=a`, the second Hamiltonian five-set and its complement are exactly the same two vertex sets.

Therefore
`K[(S-{d,gamma}) union {p_i,p_j}]`
is Hamiltonian, while
`K[{d,gamma} union (V(P)-{p_i,p_j})]`
is non-Hamiltonian.

In particular every distance-two pair has the exact alternating partition:
- for odd `i`, `K[{u,y_0,y_k,p_i,p_{i+2}}]` is Hamiltonian and `K[{v,gamma} union (V(P)-{p_i,p_{i+2}})]` is non-Hamiltonian;
- for even `i`, `K[{v,y_0,y_k,p_i,p_{i+2}}]` is Hamiltonian and `K[{u,gamma} union (V(P)-{p_i,p_{i+2}})]` is non-Hamiltonian.

Thus both the unspecified endpoint and the unspecified Hamiltonian five-set in `the repeated-middle-defect complementary-support theorem` disappear completely in the strict-alternation strict-alternation residue. ∎