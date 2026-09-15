# S9023 — Fixed-Trimer Extension and Triangle-Free Bad Graph

## Theorem A — three exterior vertices force a good pair
Let P be a three-vertex support carrying a tight trimer in a Strong Level-(1) boundary tournament, and let x,y,z be three distinct vertices outside P. Then at least one of

    P∪{x,y}, P∪{x,z}, P∪{y,z}

supports a tight Hamilton P5.

### Proof
Assume for contradiction that all three five-sets are nonHamiltonian. By the human five-vertex integrability theorem S9017, each is edge-orderable. Their restrictions to the common core P induce the same comparison orientation on the three ordinary core edges. Relabel the core as a,b,c so that

    ab < ac < bc.

Thus

    bac, abc, acb

are tight.

For an exterior vertex w define

    a in M(w) iff bwc is tight,
    b in M(w) iff awc is tight,
    c in M(w) iff awb is tight.

In any edge-order representation containing P and w, the relative order of wa,wb,wc gives exactly six possible signatures:

| spoke order | M(w) |
| --- | --- |
| wa<wb<wc | {a,b,c} |
| wa<wc<wb | {b,c} |
| wb<wa<wc | {a,b} |
| wb<wc<wa | {a} |
| wc<wa<wb | {c} |
| wc<wb<wa | empty |

If two exterior vertices u,v shared a coordinate of their match sets, then the corresponding core vertex together with u,v would give three parallel tight turns on common ordered endpoints. S9022 would then give a Hamilton P5 on P∪{u,v}, contradiction. Hence M(x),M(y),M(z) are pairwise disjoint.

Two match sets cannot both be empty. If M(u)=M(v)=empty, then in the edge order on P∪{u,v}

    uc<ub<ua,   vc<vb<va.

If ub<vb, the word c,u,b,v,a has strictly increasing edge labels; if vb<ub, the word c,v,b,u,a does. Either is a Hamilton P5, contradiction.

Therefore exactly one of the three match sets is empty. The other two are disjoint nonempty members of

    {a}, {c}, {a,b}, {b,c}, {a,b,c}.

Three nonempty pairwise disjoint signatures would have to be {a},{b},{c}, but {b} is not an allowed signature. Thus the other two nonempty signatures form exactly one of the three unordered pairs

    { {a}, {c} },
    { {a}, {b,c} },
    { {a,b}, {c} }.

After naming the empty-signature vertex x and ordering y,z appropriately, only three configurations remain:

    I.   M(x)=empty, M(y)={a},   M(z)={c};
    II.  M(x)=empty, M(y)={a},   M(z)={b,c};
    III. M(x)=empty, M(y)={a,b}, M(z)={c}.

Use the following forcing rule. In a five-set assumed nonHamiltonian, if two consecutive turns of a five-vertex word are tight, then the third must be bad and its complete reversal is tight. Write

    W => rst

when this rule applied to W forces rst. Each row below is read from left to right.

| case | successive forced turns | contradiction |
| --- | --- | --- |
| I | bycxa=>xcy; xcyab=>bay; cxbay=>abx; czbxa=>xbz; acxbz=>xca; xcazb=>zac; yzacb=>azy; cxbya=>ybx; ybxac=>cax; bycax=>acy; bacyz=>zyc; bazyc=>zab; czabx=>xba | abx and xba |
| II | cxbya=>ybx; ybxac=>cax; bycax=>acy; bacyz=>zyc; czbxa=>xbz; acxbz=>xca; xcazb=>zac; zacbx=>xbc; xbcya=>ycb; azycb=>yza; yzacb=>bca | acb and bca |
| III | cxbya=>ybx; ybxac=>cax; bycax=>acy; xbacy=>abx; czbxa=>xbz; acxbz=>xca; xcazb=>zac; yzacb=>azy; bacyz=>zyc; bazyc=>zab; czabx=>xba | abx and xba |

The initial exterior-core turns in the three cases are

    I:   cxb,cxa,bxa;  byc,cya,bya;  czb,cza,azb.
    II:  cxb,cxa,bxa;  byc,cya,bya;  czb,azc,azb.
    III: cxb,cxa,bxa;  byc,ayc,bya;  czb,cza,azb.

Every case contradicts boundary antisymmetry. Hence some exterior pair extends P to a Hamilton P5. QED.

## Theorem B — bad extension pairs form a triangle-free graph
Let P be a tight trimer and let X be any set of m>=3 vertices disjoint from P. Form a graph G_bad on X by joining x,y when P∪{x,y} does not support a tight P5. Then G_bad is triangle-free. Consequently

    |E(G_bad)| <= floor(m^2/4),

so at least

    binom(m,2)-floor(m^2/4)

pairs extend P to a Hamilton five-support. Equality in the bad-pair bound forces the Mantel extremal structure: G_bad is a complete bipartite graph with part sizes floor(m/2),ceil(m/2).

### Proof
For any three distinct x,y,z in X, Theorem A says at least one of P∪{x,y}, P∪{x,z}, P∪{y,z} is Hamiltonian. Thus xy,xz,yz cannot all be edges of G_bad, so G_bad is triangle-free. Mantel's theorem gives the displayed bound and its equality characterization. QED.

## Why this is reusable
The package converts Hamilton extension around one fixed trimer into ordinary graph theory. The local six-vertex theorem is now fully human, and its failure graph is triangle-free, making Mantel's theorem and its equality case immediately available.

## Scope and nonclaims
The theorem gives existence and density of good exterior pairs. It does not identify a preferred good pair and supplies no endpoint prescription for the resulting P5.

## Provenance
Human repair and promotion of archived R146 and R328. The former DPLL certificate has been completely removed. The proof now rests only on the human Spare Parts S9017 and S9022 plus explicit forcing rows.