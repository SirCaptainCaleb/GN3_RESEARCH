# A7C3 Specialized Toolkit — Statement Catalog

This proof-free catalog contains the statements of Spare Parts whose use is comparatively specialized: narrow normal forms, exceptional guardrails, parameter-specific finite tools, or mechanisms whose hypotheses make them less likely to belong in an ordinary research startup. The statements below are copied from the former flat `A7C3/SPARE_PARTS/STATEMENTS.md` catalog.

## S9007 — Both-Singleton Sign Degeneracy Guardrail

Let `p` and `t` be distinct vertices of a Level-(1) boundary tournament. Under the standard signed-support convention, the disjoint singleton supports `(p)` and `(t)` always admit a formal balanced opposite-sign labelling.

Indeed, the two-vertex path `(t,p)` is automatically tight because it has no internal turn. Hence `(p)` may be viewed as head-signed by witness `t`, while `(t)` may be viewed as tail-signed by witness `p`.

Consequently, a bare balanced pair whose two supports are both singletons carries no three-vertex turn information by itself. Any theorem that treats such a mass-two floor as productive must use additional retained ancestry, witness structure, payment history, capture data, or another genuine geometric certificate.

## S9016 — Two-Slot Insertion Theorem for Reversal-Symmetric Ternary Systems

Let V be a finite set and E a relation on ordered triples of distinct vertices. Assume (PA) for every distinct u,v,w, at least one of (u,v,w) and (w,u,v) lies in E, and (RS) reversal symmetry: (u,v,w) is in E if and only if (w,v,u) is in E. Call a vertex sequence tight when every consecutive ordered triple lies in E. Then for every tight path P=(v_0,...,v_{k-1}) and every x outside P, at least two of the k+1 literal insertion positions of x in P produce a tight path. Consequently every n-vertex system satisfying (PA)+(RS) has at least 2^(n-1) spanning tight paths. This bound is sharp: fix a total order on V and declare (a,b,c) tight exactly when b is not the maximum of {a,b,c}; then the spanning tight paths are exactly the permutations decreasing to the minimum and then increasing, hence there are exactly 2^(n-1).

## S9018 — Core-Polarity Signature Compression

Let `H` be a finite Strong Level-(1) boundary tournament. Fix a three-vertex core

`C={a,b,c}`

and an exterior set `E` disjoint from `C`.

For `x in E` and `d in C`, write `C-{d}={u,v}`. Define the **core-polarity match-set**

`M_C(x) subseteq C`

by declaring

`d in M_C(x)` iff `(u,d,v)` and `(u,x,v)` have the same polarity,

that is,

`[(u,d,v) is tight] = [(u,x,v) is tight]`.

This is independent of the ordering chosen for `u,v`: swapping `u,v` replaces each tested turn by its complete reversal, so boundary antisymmetry complements both Boolean values and preserves their equality. Equivalently, one may orient `u,v` uniquely so that `(u,d,v)` is tight; then `d in M_C(x)` exactly when `(u,x,v)` is tight.

Let `Gamma_C` be the graph on `E` in which distinct exterior vertices `x,y` are adjacent exactly when the induced five-set `C union {x,y}` has a tight Hamilton path of order five.

Then:

1. For each `d in C`, the coordinate class

   `E_d={x in E : d in M_C(x)}`

   is a clique of `Gamma_C`.

2. Consequently, if `U subseteq E` is independent in `Gamma_C`, then the match-sets `M_C(x)`, `x in U`, are pairwise disjoint. In particular,

   `sum_{x in U} |M_C(x)| <= 3`.

3. If `U={x,y,z}` has three exterior vertices and all three pair-extensions

   `C union {x,y}`, `C union {x,z}`, `C union {y,z}`

   are Hamilton-P5-free, then, up to independent relabelling of the core coordinates and of `x,y,z`, the signature triple

   `(M_C(x),M_C(y),M_C(z))`

   is exactly one of

   `(emptyset,emptyset,emptyset)`,

   `({a},emptyset,emptyset)`,

   `({a,b},emptyset,emptyset)`,

   `({a},{b},emptyset)`,

   `({a,b,c},emptyset,emptyset)`,

   `({a,b},{c},emptyset)`,

   `({a},{b},{c})`.

Thus a nine-bit three-exterior polarity table collapses to seven normal forms whenever the three exterior pairs are all Hamilton-P5-free.

**Parallel-trimer lemma.** Let `a,c,p,q,r` be five distinct vertices. If `(a,p,c)`, `(a,q,c)`, `(a,r,c)` are tight, then the induced subsystem on `{a,c,p,q,r}` has a tight Hamilton path of order five.

## S9026 — Two-Witness P4-Free Star Renormalization

Let A,B,c,d be four distinct vertices in a Strong Level-(1) boundary tournament. Suppose ABc and ABd are tight. If the four-set Z={A,B,c,d} has no tight Hamilton P4, then BAc and BAd are also tight, and cdA,dcA,cdB,dcB are all tight. Moreover there are exactly two possible no-P4 completions of the twelve reversal pairs on Z. In both completions Z is a transitive matching-height four-cell whose top opposite-edge matching is M_R={{A,B},{c,d}}; the remaining two cross matchings M_1={{A,c},{B,d}} and M_2={{A,d},{B,c}} occur in one of the two strict orders M_R>M_1>M_2 or M_R>M_2>M_1. Thus a same-oriented two-witness star ABc,ABd that does not already amplify to a P4 canonically renormalizes to a transitive no-P4 cell, with the star dimer and witness dimer forming the top matching.

## S9027 — Every Fifth Vertex Hamilton-Extends the Cyclic No-P4 Four-Cell

Let X={a,b,c,z} be the four-cell whose tight-turn representatives are listed below; after labelling, the representatives are abc,bca,cab,zba,azb,baz,acz,cza,zac,zcb,bzc,cbz. Then every fifth vertex d outside X lies in a Hamilton tight P5 on X∪{d}, and d can be placed one step from an end: its position is 1 or 3 in a five-vertex order numbered 0,...,4.

## S9028 — P5-Free Fifth-Vertex Gates over a Transitive Four-Cell

### Theorem A — Extreme gate existence

Let X={t,l,r,s} be a transitive matching-height no-P4 four-cell in a Strong Level-(1) boundary tournament, with opposite-edge perfect matchings M_R={{t,r},{l,s}}>M_S={{t,s},{l,r}}>M_L={{t,l},{r,s}}. Let d be a fifth vertex such that X union {d} has no tight Hamilton P5. Then at least one M_L edge is fully outgoing from d, and at least one M_R edge is fully incoming to d. Equivalently, for at least one uv in M_L both duv and dvu are tight, and for at least one xy in M_R both xyd and yxd are tight.

### Theorem B — Wrong-polarity extreme gates are forbidden

Let X={a,b,c,z} be a transitive matching-height no-P4 four-cell with perfect matchings M_R>M_S>M_L, normalized by M_R={ab,cz}, M_S={ac,bz}, M_L={bc,az}. Let d be a fifth vertex and suppose X∪{d} is P5-free. Then no M_L-edge can be fully incoming to d: for every uv∈M_L, the two turns (u,v,d),(v,u,d) cannot both be tight. Dually, no M_R-edge can be fully outgoing from d: for every rs∈M_R, the two turns (d,r,s),(d,s,r) cannot both be tight. Equivalently, every bottom matching edge has at least one bad incoming orientation and every top matching edge has at least one bad outgoing orientation.

### Theorem C — Middle matching gates alternate

Let X be a transitive no-P4 Strong Level-(1) four-cell. Write its three opposite-edge perfect matchings as M_R>M_S>M_L so that for distinct u,v,w in X, uvw is tight iff M(uv)>M(vw). Let d be a fifth vertex such that X union {d} has no tight Hamilton P5. Suppose an M_L-edge {t,l} is fully outgoing from d, meaning dtl and dlt are tight, and an M_R-edge {t,r} is fully incoming to d, meaning trd and rtd are tight. Let s be the fourth vertex of X. Then among the two M_S-edges {t,s} and {l,r}, exactly one is fully outgoing from d and the other is fully incoming to d. Equivalently, with A=[dts], B=[dst], C=[drl], D=[dlr], one has A=B, C=D, and A is not equal to C. In particular every P5-free fifth vertex over a transitive four-cell has a full gate in each matching class, with the middle-class gate orientation opposite on its two edges.

### Theorem D — A bidirectionally universal bridge dimer forces P5 or P6

Let X={a,b,c,z} be a transitive matching-height no-P4 four-cell normalized by M_R={ab,cz}>M_S={ac,bz}>M_L={bc,az}. Let u,v be distinct vertices outside X. Suppose (x,u,v) and (u,v,x) are tight for every x∈X. Then at least one of the following holds: X∪{u} supports a Hamilton P5, or X∪{u,v} supports a Hamilton P6. Equivalently, if X+u is P5-free and the six-set X+u+v is P6-free, a physical dimer uv cannot carry both universal polarities X→uv and uv→X.

## S9031 — First-Flip Obstruction for Failed One-Vertex Insertion

Let

    B=(b_1,...,b_m),  m>=2,

be a tight path in a Strong Level-(1) boundary tournament, let `x` be outside `B`, and write

    e_i={b_i,b_{i+1}}  (1<=i<=m-1),
    f_i={x,b_i}        (1<=i<=m).

Assume that inserting `x` into every one of the `m+1` slots of the displayed order of `B` fails to produce a tight path. Equivalently, `I_B(x)=empty`.

Then there is an index `1<=t<=m-1` with one of the following certificates in the line-graph comparison orientation `Gamma`.

### Star-triangle
For some `2<=t<=m-1`,

    f_t -> e_{t-1} -> e_t -> f_t.

### Reverse-spoke hook

    e_t -> f_t,
    f_{t+1} -> f_t,

and additionally

    e_{t-1} -> f_t          if t>1,
    f_{t+1} -> e_{t+1}      if t<m-1,

while at `t=m-1` the failed final insertion gives

    f_m -> e_{m-1}.

Thus total failure of displayed-order one-vertex insertion always has a local obstruction on `x` and at most three consecutive vertices of `B`.

## S9037 — Extreme Dimers Turn Failed Cooperative Splices into Barrier Corridors

Let G be a finite edge-ordered complete graph with pc_inc(G)>2. MINIMUM-DIMER CORRIDOR: suppose G has a spanning increasing three-cover D|A|B where D is the dimer on vertices x,y and xy is the globally minimum edge. Orient A,B increasingly. Let p->v be any selected edge of A and let s be the source of B. If L_A(p)<lambda(ps)<U_B(s), then lambda(xv)>=U_A(v) and lambda(yv)>=U_A(v). MAXIMUM-DIMER CORRIDOR: suppose instead D is the dimer on vertices X,Y and XY is the globally maximum edge. Let p->v be any selected edge of A and t the terminal of B. If L_B(t)<lambda(tv)<U_A(v), then lambda(pX)<=L_A(p) and lambda(pY)<=L_A(p). Thus failure of all `S9015` cooperative splices with an extreme dimer produces simultaneous two-end successor barriers in the minimum case and simultaneous two-end predecessor barriers in the maximum case.

## S9040 — Complement-Free Johnson 5-of-10 Bounds

### Theorem A — four-core Johnson cut ceiling

Let `Omega` be a 10-element set and let `F` be a family of 5-subsets of `Omega` containing no complementary pair. Put `barF={Omega\A:A in F}`. In the Johnson graph `J(10,5)`, where two 5-sets are adjacent when they meet in four vertices,

`e_J(F,barF) <= 15|F|`.

Equivalently, the average number of four-overlap neighbors in `barF` seen from a member of `F` is at most `15`.

### Theorem B — spectral intersection-one ceiling

Let `G` be the graph on the 252 five-subsets of a 10-element set `Omega`, joining distinct `S,T` exactly when `|S intersect T|=1`. If `H` is a complement-free family of `m` five-subsets, then the average degree of the induced graph `G[H]` is at most

`7 + 18m/252`.

In particular, since complement-freeness implies `m<=126`, the average degree of `G[H]` is at most `16`.
