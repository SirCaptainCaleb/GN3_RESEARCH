# Codimension-four Hamiltonian-side reduction

Let `H` be a boundary tournament with
[
V(H)=Ssqcup X,qquad |S|=4,
]
such that `H[X]` is Hamiltonian and `pc(H)>2`. This section records the consequences needed from the existence of the Hamiltonian set `X`.

## 1. Minimal Hamiltonian side

### Proposition 1.1

There is a nonempty set `Ysubseteq X` such that, with
[
K=H[Scup Y],
]
the following hold.

1. `H[Y]` is Hamiltonian and `pc(K)>2`.
2. If `Zsubsetneq Y` is nonempty and `H[Z]` is Hamiltonian, then
   [
   pc(H[Scup Z])le 2.
   ]
3. If `Dsubset Y`, `1le |D|le 2`, and `H[Y-D]` is Hamiltonian, then
   [
   pc(K-D)=2,
   ]
   and every exact two-path cover of `K-D` has both components of order at least two.

In particular, the third conclusion applies to deleting the first vertex, last vertex, first two vertices, last two vertices, or both endpoints of any Hamilton ordering of `Y`.

**Proof.**
Among all nonempty `Ysubseteq X` for which `H[Y]` is Hamiltonian and `pc(H[Scup Y])>2`, choose one of minimum cardinality. The family is nonempty because `X` itself belongs to it. The second assertion follows immediately from minimality.

Every boundary tournament on at most three vertices is Hamiltonian, so every boundary tournament on at most six vertices has a path cover with at most two components. Therefore `|V(K)|ge 7` and `|Y|ge 3`.

Now let `Dsubset Y` satisfy the hypotheses of the third assertion. Since `Y-D` is a nonempty proper Hamiltonian subset of `Y`, minimality gives `pc(K-D)le2`. If `K-D` were Hamiltonian, a Hamilton path of `K-D` together with the path on the one- or two-vertex set `D` would give a spanning two-path cover of `K`, a contradiction. Hence `pc(K-D)=2`.

Suppose an exact two-path cover of `K-D` had a singleton component `(w)`. The set `Dcup{w}` has order at most three and is therefore Hamiltonian. Replacing the singleton by a Hamilton path on `Dcup{w}` would again give a spanning two-path cover of `K`, a contradiction. Thus both components of every exact two-path cover of `K-D` have order at least two. ∎

For the remainder of this section fix such a minimal set `Y`, write
[
m=|Y|,
]
and let
[
Y=(x_0,x_1,ldots,x_{m-1})
]
be any Hamilton ordering. Put
[
L=x_0,qquad R=x_{m-1}.
]

## 2. The four-vertex complement

### Proposition 2.1

No tight path of `K` has more than `m` vertices. The induced boundary tournament `K[S]` is non-Hamiltonian.

Moreover, for every Hamilton ordering of `Y` with endpoints `L,R`:

1. `K[Scup{L}]`, `K[Scup{R}]`, and `K[Scup{L,R}]` are non-Hamiltonian;
2. for every `sin S`, each of
   [
   K[(S-{s})cup{L}],qquad
   K[(S-{s})cup{R}],qquad
   K[(S-{s})cup{L,R}]
   ]
   is Hamiltonian;
3. `K[S]` has an edge-order representation in which the three opposite-edge perfect matchings occur as intrinsic strict blocks
   [
   M_{mathrm{low}}<M_{mathrm{mid}}<M_{mathrm{high}}.
   ]

**Proof.**
Suppose `P` is a tight path of `K` on more than `m=|V(K)|-4` vertices. If `P` spans `K`, then `pc(K)=1`, impossible. Otherwise its complement has order one, two, or three and is Hamiltonian, so a Hamilton path of the complement together with `P` gives a spanning two-path cover of `K`, again impossible. Thus no tight path has more than `m` vertices.

The set `S` is non-Hamiltonian, because otherwise Hamilton paths on `Y` and `S` would two-cover `K`.

If `Scup{L}` were Hamiltonian, its Hamilton path together with the tight path obtained from the chosen ordering of `Y` by deleting `L` would two-cover `K`. Hence `Scup{L}` is non-Hamiltonian, and the same argument applies to `Scup{R}`. If `Scup{L,R}` were Hamiltonian, its Hamilton path together with the nonempty interior subpath obtained by deleting `L,R` from `Y` would two-cover `K`; hence it too is non-Hamiltonian.

Fix `sin S`. By Lemma 2.3 of the proof spine, the non-Hamiltonian five-set `Scup{L}` has an edge-order representation. If `(S-{s})cup{L}` were also non-Hamiltonian, then in this edge-ordered complete graph the two four-sets `S` and `(S-{s})cup{L}` would both have no increasing Hamilton path and would meet in the three-set `S-{s}`. Lemma 2.4 of the proof spine would then give an increasing Hamilton path on all five vertices, a contradiction. Thus `(S-{s})cup{L}` is Hamiltonian. The same argument applies with `R`.

Apply `TOOLKIT/LOCAL_HAMILTON_EXTENSIONS.md` Section 2 to the six-set `Scup{L,R}`. At least four of its five-subsets are Hamiltonian. The two obtained by deleting `L` or `R` are `Scup{R}` and `Scup{L}`, which are non-Hamiltonian. Therefore all four sets `(S-{s})cup{L,R}` are Hamiltonian.

Finally, an edge-order representation of `Scup{L}` restricts to one of `K[S]`. Since `K[S]` is non-Hamiltonian, Lemma 2.4 places the six ordinary edges on `S` into three strict opposite-edge perfect-matching blocks. Any two edges from different perfect matchings meet, so their comparison is fixed by the boundary relation on `S`; hence the order of the three blocks is intrinsic. ∎

### Proposition 2.2

Assume `mge2`, and put `u=x_1`, `v=x_{m-2}`. Then for every `sin S`,
[
(u,L,s)quad	ext{and}quad(s,R,v)
]
are tight.

**Proof.**
If `(s,L,u)` were tight, then prepending `s` to the Hamilton ordering of `Y` would give a Hamilton path on `Ycup{s}`. The complementary three-set `S-{s}` is Hamiltonian, so `K` would have a spanning two-path cover. Therefore `(s,L,u)` is not tight, and boundary antisymmetry gives `(u,L,s)`. The terminal assertion is identical. ∎

## 3. Pair-deletion covers and a Hamilton five-subset

Let `D` be the first two or last two vertices of a Hamilton ordering of `Y`, and let `T` be any exact two-path cover of `K-D`, whose existence and nontriviality follow from Proposition 1.1.

For `sin S`, put
[
C_s=S-{s},qquad Y_s=(Y-D)cup{s}.
]
Let `	au_s` be the number of ordinary edges of `T` with one endpoint in `C_s` and the other in `Y_s`, and let `b_s` be the number of nonempty components of the ordinary forest `T[C_s]`.

### Proposition 3.1

There is a vertex `sin S` such that

1. `K[Dcup C_s]` is Hamiltonian;
2. `	au_sge2`;
3. `b_sge2`.

**Proof.**
It is enough to treat the case in which `D={u_0,u_1}` is the initial pair of a Hamilton ordering
[
(u_0,u_1,a_2,ldots,a_{m-1})
]
of `Y`; the terminal case uses the corresponding prefix argument. Put
[
G_D={sin S:K[Dcup C_s]	ext{ is Hamiltonian}}.
]

The six-set `E=Scup D` is non-Hamiltonian, since otherwise a Hamilton path on `E` together with `(a_2,ldots,a_{m-1})` would two-cover `K`. Also `Scup{u_0}` is non-Hamiltonian, since otherwise a Hamilton path there together with `(u_1,a_2,ldots,a_{m-1})` would two-cover `K`. By `TOOLKIT/LOCAL_HAMILTON_EXTENSIONS.md` Section 2, at least four five-subsets of `E` are Hamiltonian. Hence at least three of the four sets `Dcup C_s` are Hamiltonian, so `|G_D|ge3`.

For every `sin G_D`, `TOOLKIT/PATH_COVER_SURGERY.md` Section 1, applied with deleted set `D` and side `C_s`, gives `	au_sge1`.

Let `delta` be the number of ordinary edges of `T` crossing `S|(Y-D)`, and let `d_S(s)`, `d_Y(s)` be the numbers of neighbors of `s` in `S` and `Y-D`, respectively, in the ordinary path forest of `T`. Since `K[S]` is non-Hamiltonian while `Y-D` is a tight path, `deltage1`. Moving `s` across the partition gives
[
	au_s=delta-d_Y(s)+d_S(s).
]

At most two vertices of `S` satisfy `	au_s=1`. If `delta=1`, cutting the unique crossing edge leaves three blocks; at least two lie in `S`, so `T[S]` has exactly two blocks. A vertex not incident with the crossing edge and satisfying `	au_s=1` must have `d_S(s)=0`, hence is an isolated `S`-block, and there is at most one such vertex besides the crossing endpoint. If `delta=2`, the equality `	au_s=1` forces `(d_Y(s),d_S(s))=(1,0)`, so at most two vertices qualify. If `delta=3`, it forces `(2,0)`, so at most one qualifies. If `deltage4`, then `	au_sgedelta-2ge2` because every vertex has ordinary degree at most two.

At most one vertex satisfies `b_s=1`. Let `e` be the number of ordinary edges of `T[S]`. Since `K[S]` is non-Hamiltonian and `T[S]` is a path forest on four vertices, `ele2`. If `b_s=1`, the three vertices of `C_s` form one path and therefore contribute two edges of `T[S]`; hence `e=2` and both edges avoid `s`. Two distinct vertices cannot both be avoided by two edges on the remaining two vertices.

Suppose no vertex of `G_D` satisfies both `	au_sge2` and `b_sge2`. Every vertex of `G_D` with `b_sge2` then has `	au_s=1`, and every other vertex of `G_D` has `b_s=1`. The two bounds and `|G_D|ge3` force `|G_D|=3`: exactly two vertices have `	au_s=1`, while the third, say `s_*`, has `b_{s_*}=1` and `	au_{s_*}ge2`.

Because `b_{s_*}=1`, the three vertices of `C_{s_*}` form an ordinary path `x-y-z` in `T`. Since `K[S]` is non-Hamiltonian, `T[S]` has at most two edges; they are therefore exactly `xy,yz`, and `s_*` is isolated in `T[S]`. The middle vertex `y` already has ordinary degree two, while each of `x,z` has room for at most one further edge. Hence `	au_{s_*}le2`, so `	au_{s_*}=2`, with one edge from each of `x,z` to `Y-D`.

Let `delta'` be the number of ordinary edges of `T` crossing `S|(Y-D)`. Then `delta'ge2`. For either endpoint, say `x`, we have `d_S(x)=d_{Y-D}(x)=1`, so
[
	au_x=delta'-d_{Y-D}(x)+d_S(x)=delta'ge2.
]
The same holds for `z`. Since `G_D` consists of `s_*` and two of `x,y,z`, at least one of `x,z` lies in `G_D`. For that vertex `s`, deleting `s` from `x-y-z` leaves one edge together with the isolated vertex `s_*`, so `b_s=2`, a contradiction. ∎

## 4. A five-vertex endpoint construction

Assume now that `mge4`.

### Proposition 4.1

There are `sin S` and a Hamilton ordering
[
M=(m_0,ldots,m_4)
]
of
[
{L,R}cup(S-{s})
]
such that one of the following holds.

1. `L=m_p` for some `pin{0,3,4}), and the two vertex sequences
   [
   M[0,p](x_1,ldots,x_{m-2}),qquad (s)M[p+1,4],
   ]
   with empty pieces omitted, partition `V(K)` and have exactly one non-tight consecutive triple.
2. `R=m_q` for some `qin{0,1,4}), and the two vertex sequences
   [
   M[0,q-1](s),qquad (x_1,ldots,x_{m-2})M[q,4],
   ]
   with empty pieces omitted, partition `V(K)` and have exactly one non-tight consecutive triple.

**Proof.**
Write the intrinsic matching blocks of `S` as
[
M_{mathrm{low}}<M_{mathrm{mid}}<M_{mathrm{high}}.
]
By `TOOLKIT/FOUR_VERTEX_STRUCTURE.md` Section 3, relative to each of `L,R`, one edge of `M_{mathrm{mid}}` is incoming and the other is outgoing.

Relabel
[
S={a,b,c,z}
]
so that
[
M_{mathrm{low}}={ab,cz},qquad
M_{mathrm{mid}}={ac,bz},qquad
M_{mathrm{high}}={az,bc},
]
and so that `bz` is outgoing from `L` while `ac` is incoming to `L`. Thus
[
(L,b,z),(L,z,b),(a,c,L),(c,a,L)
]
are tight. The matching-block order also gives
[
(z,b,c),(c,a,z),(z,c,a),(a,c,b),(b,a,c),(b,a,z)
]
tight.

Call a Hamilton ordering of `{L,R}cup(S-{s})` favorable if `L` occurs in position `0,3,4` or `R` occurs in position `0,1,4`. Suppose no favorable ordering exists.

There are two possibilities for the edge of `M_{mathrm{mid}}` incoming to `R`.

If `ac` is incoming to `R`, then
[
(a,c,R),(c,a,R),(R,b,z),(R,z,b)
]
are tight. Successively testing the Hamilton orders
[
(L,R,z,b,c),qquad (R,z,c,a,L),qquad (c,z,R,L,a)
]
forces
[
(z,R,L),qquad(c,z,R),qquad(a,L,R)
]
respectively. Then
[
(z,c,a,L,R)
]
is a favorable Hamilton ordering, a contradiction.

If `bz` is incoming to `R`, then
[
(b,z,R),(z,b,R),(R,a,c),(R,c,a)
]
are tight. Successively testing
[
egin{aligned}
&(L,b,z,R,c), (c,L,b,z,R), (L,R,c,a,z), (z,c,a,L,R),\
&(L,R,a,c,b), (b,a,c,L,R), (c,R,L,a,z), (c,R,z,a,L),\
&(L,b,a,z,R), (R,a,b,L,c)
end{aligned}
]
forces
[
(c,R,z),(b,L,c),(c,R,L),(R,L,a),(a,R,L),(R,L,c),(z,a,L),(a,z,R),(a,b,L),(b,a,R).
]
Then
[
(b,a,R,L,c)
]
is a favorable Hamilton ordering, again a contradiction.

Hence a favorable ordering exists. In the first alternative of the statement, the only consecutive triple not inherited from `M` or the Hamilton ordering of `Y` is, according as `p=0,3,4`,
[
(s,m_1,m_2),qquad(m_2,L,x_1),qquad(m_3,L,x_1).
]
In the second alternative, the only such triple is, according as `q=0,1,4`,
[
(x_{m-2},R,m_1),qquad(x_{m-2},R,m_2),qquad(m_2,m_3,s).
]
If this single new triple were tight, the two displayed sequences would form a spanning two-path cover of `K`, contrary to `pc(K)>2`. Therefore it is non-tight. ∎

## 5. Exact covers on the eight endpoint/complement vertices

Assume now that `mge6`, and put
[
u=x_1,qquad v=x_{m-2},qquad
N=(x_2,ldots,x_{m-3}).
]
The path `N` is nonempty.

Let the two edges of `M_{mathrm{mid}}` be denoted `I,O`, where `I` is incoming and `O` is outgoing at `L`.

### Proposition 5.1

At `R` exactly one of the following occurs.

1. `I` is incoming and `O` outgoing. Writing
   [
   O={o_0,o_1},qquad I={i_0,i_1},
   ]
   every choice of orientations gives an exact two-path cover
   [
   (u,L,o_0,o_1)mid(i_0,i_1,R,v)
   ]
   of the induced boundary tournament on
   [
   Scup{L,u,v,R}.
   ]
2. `O` is incoming and `I` outgoing. Every orientation `(o_0,o_1)` of `O`, together with either orientation of the two-vertex path on `I`, gives an exact two-path cover
   [
   (u,L,o_0,o_1,R,v)mid I.
   ]

In either case the induced boundary tournament on `Scup{L,u,v,R}` has path-cover number two.

**Proof.**
By Proposition 2.1, both `Scup{L}` and `Scup{R}` are non-Hamiltonian. Applying `TOOLKIT/FOUR_VERTEX_STRUCTURE.md` Section 3 at each endpoint shows that exactly one edge of `M_{mathrm{mid}}` is incoming and the other outgoing there. Relative to the fixed names `I,O` at `L`, the assignment at `R` is therefore exactly one of the two cases in the statement.

In the first case, for either orientation `(o_0,o_1)` of `O`, the triple `(L,o_0,o_1)` is tight; Proposition 2.2 gives `(u,L,o_0)`, so `(u,L,o_0,o_1)` is a tight four-vertex path. Similarly, for either orientation `(i_0,i_1)` of `I`, the triple `(i_0,i_1,R)` is tight and Proposition 2.2 gives `(i_1,R,v)`, so `(i_0,i_1,R,v)` is a tight four-vertex path. Their supports partition the eight vertices.

In the second case, `O` is outgoing at `L` and incoming at `R`. Hence for either orientation `(o_0,o_1)`, both `(L,o_0,o_1)` and `(o_0,o_1,R)` are tight. Together with Proposition 2.2 this makes
[
(u,L,o_0,o_1,R,v)
]
a tight six-vertex path. The remaining two vertices are exactly `I`, which form a two-vertex path in either orientation.

Thus the induced boundary tournament on `Scup{L,u,v,R}` has path-cover number at most two. If it were Hamiltonian, a Hamilton path on those eight vertices together with the disjoint nonempty tight path `N` would two-cover `K`, impossible. Hence its path-cover number is exactly two. ∎

### Proposition 5.2

Suppose the second case of Proposition 5.1 holds. Write
[
O={b,z},qquad W=V(K)-I.
]
Then `K[W]` has the four exact two-path covers
[
(u,L,b,z)mid Y[2,m-1],
]
[
(u,L,z,b)mid Y[2,m-1],
]
[
Y[0,m-3]mid(z,b,R,v),
]
and
[
Y[0,m-3]mid(b,z,R,v).
]

**Proof.**
Proposition 2.2 gives `(u,L,s)` and `(s,R,v)` tight for every `sin S`. Since `O={b,z}` is outgoing at `L`, both `(L,b,z)` and `(L,z,b)` are tight, giving the two left four-vertex paths. Since `O` is incoming at `R`, both `(z,b,R)` and `(b,z,R)` are tight, giving the two right four-vertex paths. The complementary long pieces are contiguous subpaths of `Y`, so all four displayed pairs are literal two-path covers of `W`.

If `K[W]` were Hamiltonian, a Hamilton path on `W` together with the two-vertex path on `I` would give a spanning two-path cover of `K`, impossible. Therefore `pc(K[W])=2`, and all four displayed covers are exact. ∎
