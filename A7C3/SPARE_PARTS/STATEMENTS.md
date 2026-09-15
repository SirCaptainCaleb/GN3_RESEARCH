# A7C3 Spare-Part Statement Catalog

Fast initialization catalog for `A7C3/SPARE_PARTS/`. This file contains the mathematical statement of every current spare part, with proofs, provenance, scope notes, and discussion removed. Bundled spare parts retain each named theorem statement. Two older files also contribute a useful secondary formal statement: the S9001 same-support corollary and the S9018 parallel-trimer lemma.

**Researcher use:** skim this file during ordinary initialization to know which reusable tools already exist. Open the linked `S####_*.md` source file before relying on a result when its proof, scope, exact conventions, or provenance matters.

## S9001 — Reverse-Ear Lemma

Let

`P=(v_0,...,v_k)`

and `K` be vertex-simple tight paths in a finite Strong Level-(1) boundary tournament. Let `E` be a `K`-subpath from `v_i` to `v_j` such that `v_i,v_j` are consecutive contacts of `K` with `P`, so every internal vertex of `E` lies outside `P`, and suppose `i>j`.

Then one of the following occurs:

1. `E` is the single state `v_i v_j` with `i=j+1`, so `K` contains the exact reversal of the old `P`-state `v_j v_i`;
2. one of the two `P/E` seams yields a tight reverse trimer; or
3. `E` together with the old `P`-segment from `v_j` through `v_{i-1}` forms a vertex-simple proper tight cycle.

Consequently, outside these explicit outputs, the vertices of `P` encountered along any tight path `K` occur in increasing `P`-order.

**Same-support corollary.** Let `P` and `Q` be vertex-simple tight Hamilton paths on the same vertex set. If their literal orders differ, then either `Q` contains the exact reversal of an adjacent state of `P`, there is a tight reverse trimer at a comparison seam, or there is a vertex-simple proper tight cycle.

## S9002 — Punctured Component-Drop Pair Theorem

Let `H` be a finite Strong Level-(1) boundary tournament, and let `W` be a proper subset of `V(H)`. Suppose `H[W]` has two literal path covers

`R = R_1 | ... | R_c`

and

`T = T_1 | ... | T_r`

with `r<c`. Then `H` contains a graph-intrinsic balanced opposite-sign pair.

Equivalently: whenever the same proper induced subsystem is represented once with `c` path components and once with fewer than `c` path components, the component drop itself forces an opposite-sign pair certificate in the ambient tournament.

No smallest-counterexample hypothesis, endpoint hypothesis, extremality condition, or deleted-marker structure is required.

## S9003 — Absorbable-Deletion Crossing Lemma

Let `H` be a finite boundary tournament with path-cover number `pc(H)>2`. Let `D` be a nonempty proper vertex set, put

`W = V(H) \ D`,

and let `S` be a nonempty proper subset of `W`. Suppose there is a vertex-simple tight path `Q` whose vertex set is exactly

`D ∪ S`.

Then every literal spanning two-path cover

`T = T_1 | T_2`

of `H-D` selects an adjacent directed state with one endpoint in `S` and the other in `W\S`.

Equivalently, if the deleted vertices together with one remainder block `S` can already be absorbed into a certified tight path, then no two-cover of the deletion can keep `S` completely separated from the complementary remainder.

No Strong Level-(1) antisymmetry, smallest-counterexample minimality, endpoint hypothesis, or extremality assumption is needed once the displayed objects exist.

## S9004 — Wrap Selection-or-Reversal Lemma

Let

`P=(p_0,p_1,...,p_r)`, `r>=1`,

be a literal tight path in a Strong Level-(1) boundary tournament, and consider the wrap state `p_rp_0`.

If `r=1`, the reversed dimer `(p_1,p_0)` is automatically a tight path.

Assume `r>=2`. Define the two wrap seams

`alpha=(p_r,p_0,p_1)`,

`beta=(p_{r-1},p_r,p_0)`,

and the two cyclic rotations

`P_H=(p_r,p_0,p_1,...,p_{r-1})`,

`P_T=(p_1,...,p_r,p_0)`.

Exactly one of the following four branches holds.

### Double wrap

Both `alpha` and `beta` are tight. Equivalently, both cyclic rotations are tight. In this case

`(p_0,p_1,...,p_r,p_0)`

is a tight Hamilton cycle on `V(P)`.

### Single wrap at the head rotation

`alpha` is tight and `beta` is bad. Then `P_H` is a tight Hamilton path, `P_T` is not, and boundary antisymmetry gives

`(p_0,p_r,p_{r-1})`

tight.

### Single wrap at the tail rotation

`beta` is tight and `alpha` is bad. Then `P_T` is a tight Hamilton path, `P_H` is not, and boundary antisymmetry gives

`(p_1,p_0,p_r)`

tight.

### Double fail

Both `alpha` and `beta` are bad. Then neither rotation is tight, and boundary antisymmetry gives both

`(p_1,p_0,p_r)`

and

`(p_0,p_r,p_{r-1})`

tight. If `r>=3`, these concatenate to the vertex-simple tight reverse `P4`

`(p_1,p_0,p_r,p_{r-1})`.

In particular, a single successful rotation is merely a cyclically shifted Hamilton path. A Hamilton cycle on the displayed support occurs exactly in the double-wrap branch.

## S9005 — Boundary-Reversed Hamilton Dimer Absorber

Let `X` be a finite induced vertex set in a Strong Level-(1) boundary tournament. Suppose there are distinct vertices `u,v in X` and two Hamilton tight paths of `X` with the following boundary states:

- one Hamilton path begins with the ordered dimer `(u,v)`;
- one Hamilton path ends with the reverse ordered dimer `(v,u)`.

Then every exterior vertex `d notin X` Hamilton-extends `X`.

More precisely, boundary antisymmetry makes exactly one of

`(d,u,v)` and `(v,u,d)`

tight. In the first case, prepend `d` to the Hamilton path beginning with `(u,v)`. In the second case, append `d` to the Hamilton path ending with `(v,u)`. Either way `X∪{d}` has a Hamilton tight path.

Thus a Hamilton support carrying opposite orientations of one boundary dimer at its two available ends is a universal one-vertex absorber.

## S9006 — Cycle-Opening Gain Identity

Let a spanning path cover on a fixed `n`-vertex set initially have `q` path components. Suppose a compatible selected-state exchange adds and removes states with **raw gain**

`g = (# inserted states) - (# removed states)`,

and suppose the resulting selected-state system has only vertex-simple path components and physical tight-cycle components. If exactly `c` cycle components occur, then opening one selected state on each cycle yields a genuine spanning path cover with

`q' = q - g + c`

components.

Equivalently,

`q - q' = g - c`.

Thus actual path-cover improvement is raw exchange gain minus cycle debt. A physical tight cycle is constructive bookkeeping debt, not a contradiction: each cycle costs exactly one selected state to open.

## S9007 — Both-Singleton Sign Degeneracy Guardrail

Let `p` and `t` be distinct vertices of a Level-(1) boundary tournament. Under the standard signed-support convention, the disjoint singleton supports `(p)` and `(t)` always admit a formal balanced opposite-sign labelling.

Indeed, the two-vertex path `(t,p)` is automatically tight because it has no internal turn. Hence `(p)` may be viewed as head-signed by witness `t`, while `(t)` may be viewed as tail-signed by witness `p`.

Consequently, a bare balanced pair whose two supports are both singletons carries no three-vertex turn information by itself. Any theorem that treats such a mass-two floor as productive must use additional retained ancestry, witness structure, payment history, capture data, or another genuine geometric certificate.

## S9008 — Three-Cover Six-Clause Splice Fan

Let `H` be a finite Strong Level-(1) boundary tournament with `pc(H)>2`, and suppose

`H = A | B | C`

is a literal spanning three-path cover in which all three component paths are nontrivial.

For every ordered pair of distinct components, say

`A=(a_0,...,a_p)` and `B=(b_0,...,b_q)` with `p,q>=1`,

consider the spanning two-path proposal obtained by concatenating `A` to `B` and leaving `C` unchanged:

`(a_0,...,a_p,b_0,...,b_q) | C`.

Its complete uncertified-turn set consists exactly of the two seam turns

`h_1=(a_{p-1},a_p,b_0)`

and

`h_2=(a_p,b_0,b_1)`.

At least one of these two turns is bad. Consequently boundary antisymmetry forces the physical mate clause

`(b_0,a_p,a_{p-1})` tight

or

`(b_1,b_0,a_p)` tight.

Applying this construction to all six ordered pairs among `A,B,C` yields six explicit two-hole mate clauses attached to the same literal spanning three-cover.

## S9009 — Two-Ended Hamilton Absorber Splice Lemma

Let `H` be a finite exact-reversal tight-turn system. Let `X,Y` partition `V(H)`, and suppose `Y` has a literal two-path cover

`U | V`

with both rails nonempty. Choose an endpoint `x` of `U` and an endpoint `y` of `V` in opposite splice roles. In one orientation write

`U=(x,u_1,...,u_r)`,

`V=(v_0,...,v_{s-1},y)`,

and suppose `X∪{x,y}` has a Hamilton tight path

`Q=(y,q_1,...,q_t,x)`.

Form the vertex-simple spanning word

`K=(v_0,...,v_{s-1},y,q_1,...,q_t,x,u_1,...,u_r)`,

omitting an empty residual piece when necessary.

Its complete uncertified-turn set consists of at most the two attachment turns

`alpha=(v_{s-1},y,q_1)`

when the left residual seam exists, and

`beta=(q_t,x,u_1)`

when the right residual seam exists.

If `pc(H)>1`, at least one existing attachment turn is bad, so exact reversal gives `reverse(alpha)` tight or `reverse(beta)` tight, with nonexistent holes omitted.

If `pc(H)>2`, then both residual seams exist and both `alpha` and `beta` are bad. Consequently both reversed attachment turns are tight simultaneously.

The other endpoint-role choices are obtained by the corresponding role-correct concatenation, without reversing any certified tight path.

## S9010 — Signed-Path Contact and Historical Anchor Protection

Let `(w;P)` be a graph-intrinsic head-signed tight path in a Strong Level-(1) boundary tournament, with

`P=(v_0,...,v_k)`

and signed anchor `v_0`. Let `Q` be any proper tight path meeting `P`.

If `Q` avoids `v_0`, let

`i = min{j : v_j in V(Q)}`.

Then `i>=1`, and the prefix

`P^-=(v_0,...,v_{i-1})`

is a nonempty, strictly shorter head-signed support disjoint from `Q`, with the same anchor `v_0`.

If `Q` contains `v_0`, then, apart from the vacuous exact replay of the same singleton support with no new certificate data, at least one of the following occurs:

1. strict tight-path growth of the old support `P`;
2. strict tight-path growth of `Q`;
3. a vertex-simple proper tight cycle;
4. explicit reverse-contact geometry of the Reverse-Ear type.

The tail-signed dual is exact.

Consequently, outside these explicit events, a genuinely later signed support or marker cannot silently contain the signed anchor of an older historical support. Quiet contact away from the anchor can only shorten the old support on its signed side while preserving that anchor.

## S9011 — Line-Graph Comparison Representation Theorem

Let `H` be a finite Strong Level-(1) boundary tournament on vertex set `V`. Define a directed graph `Gamma(H)` whose vertices are the ordinary edges of the complete graph `K_V`.

Whenever

`e={u,v}` and `f={v,w}`

are distinct incident ordinary edges, orient the corresponding line-graph edge

`e -> f`

exactly when the ordered turn `(u,v,w)` is tight.

Then:

1. `Gamma(H)` is a well-defined orientation of the full line graph `L(K_V)`.
2. A vertex-simple sequence `P=(v_0,...,v_k)` is a tight path in `H` if and only if its consecutive ordinary edges

   `e_i={v_{i-1},v_i}`

   form a directed chain

   `e_1 -> e_2 -> ... -> e_k`

   in `Gamma(H)`.
3. `H` is realizable by a global total order `<` on `E(K_V)` satisfying

   `(u,v,w)` tight iff `{u,v} < {v,w}`

   if and only if `Gamma(H)` is acyclic. In the acyclic case, any topological ordering of `Gamma(H)` gives such an edge order.
4. If `Gamma(H)` is cyclic and `C` is a shortest directed cycle, then `C` is chordless in `L(K_V)`. Its underlying ordinary edges have one of the following forms:
   - a three-edge star about one vertex, giving a directed triangle in the local middle-vertex tournament;
   - the three edges of an ordinary triangle, with all three cyclic turns tight;
   - for length `r>=4`, the edges of a simple ordinary `r`-cycle, with every cyclic consecutive turn tight.

Thus failure of global edge-orderability always has a minimal holonomy certificate of star-triangle or vertex-simple cyclic-turn type.

## S9012 — Two-Ended Endpoint Replacement Lemma

Let

`Q=(q_0,q_1,...,q_r)`, `r>=2`,

be a vertex-simple Hamilton tight path on a support `X` in a finite Strong Level-(1) boundary tournament, and let `y` be a vertex outside `X`.

Assume `X∪{y}` is non-Hamiltonian. Suppose nevertheless that there is

- a Hamilton tight path `L` on `(X-{q_0})∪{y}`, and
- a Hamilton tight path `R` on `(X-{q_r})∪{y}`.

Then at least one of the three path comparisons

`(Q,L)`, `(Q,R)`, `(L,R)`

has an explicit Reverse-Ear output: an exact reversed old adjacent state, a tight reverse trimer at a seam, or a vertex-simple proper tight cycle.

Equivalently, outside explicit reverse-order geometry, one exterior vertex cannot Hamilton-replace both endpoints of a Hamilton path while the full one-vertex extension remains non-Hamiltonian.

More precisely, if `(Q,L)` is Reverse-Ear-quiet, then

`L=(y,q_1,q_2,...,q_r)`

or

`L=(q_1,y,q_2,...,q_r)`.

If `(Q,R)` is Reverse-Ear-quiet, then

`R=(q_0,...,q_{r-1},y)`

or

`R=(q_0,...,q_{r-2},y,q_{r-1})`.

If `(L,R)` is quiet as well, only the boundary-overlap cases `r=2` or `r=3` survive, and each directly concatenates to a Hamilton path on `X∪{y}`, contradiction.

## S9013 — Partition-Cover Deficit Identity

Fix a partition

`Pi={X_1,...,X_m}`

of a finite vertex set into nonempty physical classes. Let `T` be a literal exact path cover of the whole vertex set with `q` path components.

Let `t_Pi(T)` be the number of selected adjacent states of `T` whose endpoints lie in different partition classes. For each class `X_i`, let

`pc(X_i)`

be the intrinsic minimum number of tight paths needed to cover the induced subsystem on `X_i`.

Then there is a nonnegative integer `sigma_Pi(T)` such that

`t_Pi(T) = sum_i pc(X_i) - q + sigma_Pi(T)`.

More concretely, if `b_i(T)` is the number of monochromatic path blocks obtained by restricting the displayed cover `T` to class `X_i`, then

`sigma_Pi(T)=sum_i (b_i(T)-pc(X_i)) >= 0`.

Hence

`t_Pi(T) >= sum_i pc(X_i)-q`,

with equality if and only if every class restriction of `T` realizes the intrinsic path-cover minimum of that class.

## S9014 — Signed-Interval Rebirth and Tight-Path Cut Memory

Let

`P=(v_0,...,v_k)`

be a graph-intrinsic tight path, and let `S` be any vertex set such that `P-S` is nonempty.

Call a **surviving interval** a maximal nonempty contiguous block of vertices of `P` that remains after deleting `S`. Every surviving interval

`I=(v_i,...,v_j)`

in the old path order remembers its immediate cut neighbors:

- if `i>0`, then `v_{i-1}` is deleted and `(v_{i-1},I)` is a tight path;
- if `j<k`, then `v_{j+1}` is deleted and `(I,v_{j+1})` is a tight path.

In particular, signed intervals regenerate canonically.

### Head-signed form

Suppose `P` is head-signed by a witness `w`, meaning

`(w,v_0,...,v_k)`

is tight. Let `I=(v_i,...,v_j)` be the first surviving interval of `P-S`.

- If `i=0`, then `I` remains head-signed by `w`.
- If `i>0`, then `I` is head-signed by the immediately preceding deleted vertex `v_{i-1}`.

### Tail-signed form

Dually, suppose

`(v_0,...,v_k,z)`

is tight, and let `J=(v_i,...,v_j)` be the last surviving interval of `P-S`.

- If `j=k`, then `J` remains tail-signed by `z`.
- If `j<k`, then `J` is tail-signed by the immediately following deleted vertex `v_{j+1}`.

Thus deletion of arbitrary vertices from a tight path does not erase boundary information: every surviving interval retains exact cut-side witness data, and the first or last surviving interval of a signed support is automatically reborn as a signed descendant.

## S9015 — Three-Component Broad-Interval Augmentation

Let `G` be an edge-ordered complete graph and let `F` be a spanning cover of `G` by `c>=3` vertex-disjoint increasing paths, each oriented in its increasing direction.

For a vertex `v` on one of the paths, let `L(v)` denote the label of its incoming path edge when that edge exists and put `L(v)=-infinity` at a path source. Likewise let `U(v)` denote the label of its outgoing path edge when it exists and put `U(v)=+infinity` at a path terminal.

Suppose `p->v` is a selected edge of one component `C`. Let `t` be the terminal vertex of a second component `A`, and let `s` be the source vertex of a third component `B`, with `A,B,C` pairwise distinct. If

`L(t) < lambda(tv) < U(v)`

and

`L(p) < lambda(ps) < U(s)`,

then deleting the selected edge `p->v` and adding `t->v` and `p->s` produces a spanning cover by `c-1` vertex-disjoint increasing paths.

The conclusion remains valid when `A` or `B` is a singleton under the endpoint conventions above.

## S9016 — Two-Slot Insertion Theorem for Reversal-Symmetric Ternary Systems

Let V be a finite set and E a relation on ordered triples of distinct vertices. Assume (PA) for every distinct u,v,w, at least one of (u,v,w) and (w,u,v) lies in E, and (RS) reversal symmetry: (u,v,w) is in E if and only if (w,v,u) is in E. Call a vertex sequence tight when every consecutive ordered triple lies in E. Then for every tight path P=(v_0,...,v_{k-1}) and every x outside P, at least two of the k+1 literal insertion positions of x in P produce a tight path. Consequently every n-vertex system satisfying (PA)+(RS) has at least 2^(n-1) spanning tight paths. This bound is sharp: fix a total order on V and declare (a,b,c) tight exactly when b is not the maximum of {a,b,c}; then the spanning tight paths are exactly the permutations decreasing to the minimum and then increasing, hence there are exactly 2^(n-1).

## S9017 — Five-Vertex Non-Hamiltonian Boundary Tournaments Are Edge-Orderable

Let H be a boundary 3-tournament on exactly five vertices. If H has no directed tight Hamilton path, its line-graph comparison orientation Gamma(H) is acyclic. Equivalently there is a total order on E(K_5) realizing every tight turn as an increasing consecutive-edge comparison. In contrapositive form, any nonintegrable five-vertex boundary tournament is Hamiltonian. Consequently, in any boundary tournament with pc(H)>2, the five-vertex complement of any proper tight path is edge-orderable.

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

## S9019 — Edge-Ordered Complete Graphs Through Order Ten Have Two Increasing Paths

Let `G` be a complete graph on `n<=10` vertices with a strict total order on its ordinary edges. Then `V(G)` can be partitioned into at most two vertex-disjoint increasing paths. Equivalently,

`pc_inc(G) <= 2`

for every edge-ordered `K_n` with `n<=10`.

## S9020 — Non-Hamiltonian K4 Structure and Overlap Amplification

### Theorem A — minimum-edge mate

Let X={x,y,a,b} induce an edge-ordered K4 with no increasing Hamilton path. If xy is the smallest of the six edges of X, then the opposite edge ab is smaller than each of xa,xb,ya,yb. Hence xy and ab are the two locally smallest edges of X. In the standard transitive matching-height boundary orientation induced by the edge order, the opposite pair {xy,ab} is the top matching level M_R (because a turn is tight when its first edge is earlier).

### Theorem B — shared-triangle amplification

Let G be an edge-ordered complete graph and let T={u0,u1,u2} be a three-vertex set. Let x,y be distinct vertices outside T. If both induced edge orders on T∪{x} and T∪{y} have no increasing Hamilton path, then G[T∪{x,y}] has an increasing Hamilton path.

## S9021 — Canonical Barrier Gaps for Noninsertable Vertices in an Edge-Ordered Path

Let G be an edge-ordered graph and let Q=(q_0,...,q_m), m>=1, be an increasing path. Let x be a vertex outside Q adjacent to every q_i. For 0<=i<=m-1, call the gap i right-feasible if either i=m-1 or the edge xq_{i+1} precedes q_{i+1}q_{i+2}; call it left-feasible if either i=0 or q_{i-1}q_i precedes q_i x. Assume that inserting x between q_i and q_{i+1} never gives an increasing path, for any i. Then some gap is simultaneously left- and right-feasible, and at every such gap the middle spoke pair is reversed: xq_{i+1} precedes xq_i. In particular, if beta(x) is the least right-feasible gap, then beta(x) is also left-feasible and xq_{beta(x)+1}<xq_{beta(x)}. Moreover, for two such noninsertable vertices x,y, if beta(x)<beta(y), then at the rail vertex q_{beta(x)+1} one has xq_{beta(x)+1}<q_{beta(x)+1}q_{beta(x)+2}<yq_{beta(x)+1}; consequently the ordered turn (x,q_{beta(x)+1},y) is tight in the boundary tournament induced by the edge order. Thus any family of noninsertable exterior vertices carries a canonical barrier preorder, with strict barrier separation witnessed by a graph-intrinsic cross turn.

## S9022 — Parallel Source Turns Force an Endpoint-Controlled Hamilton P5

### Theorem A — Hamilton P5 existence

Let `a,c,p,q,r` be five distinct vertices in a Strong Level-(1) boundary tournament. If

    (a,p,c), (a,q,c), (a,r,c)

are tight, then the induced subsystem on `{a,c,p,q,r}` has a tight Hamilton path of order five.

### Theorem B — a source spoke can be an endpoint

Let `A,C,p,q,r` be distinct vertices of a Strong Level-(1) boundary tournament and suppose

`(A,s,C)`

is tight for every `s∈{p,q,r}`. Then the induced five-set `{A,C,p,q,r}` has a tight Hamilton `P5` with at least one endpoint in `{p,q,r}`.

The source-spoke endpoint cannot in general be prescribed in advance: for each designated source label there are examples satisfying the three source turns in which that label is not an endpoint of any tight Hamilton `P5`.

## S9023 — Fixed-Trimer Extension and Triangle-Free Bad Graph

### Theorem A — three exterior vertices force a good pair

Let P be a three-vertex support carrying a tight trimer in a Strong Level-(1) boundary tournament, and let x,y,z be three distinct vertices outside P. Then at least one of the three five-sets P∪{x,y}, P∪{x,z}, P∪{y,z} supports a tight five-vertex path.

### Theorem B — bad extension pairs form a triangle-free graph

Let P be a tight trimer in a Strong Level-(1) boundary tournament and let X be any set of m>=3 vertices disjoint from P. Form a graph G_bad on X by joining x,y when the five-set V(P) union {x,y} does not support a tight P5. Then G_bad is triangle-free. Consequently |E(G_bad)|<=floor(m^2/4), so at least binom(m,2)-floor(m^2/4) pairs {x,y} extend P to a Hamiltonian five-support. Equality in the bad-pair bound forces the Mantel extremal structure: G_bad is a complete bipartite graph with part sizes floor(m/2),ceil(m/2). Equivalently, in the equality case the outside vertices split into two nearly equal classes and every within-class pair extends P to a tight P5.

## S9024 — Two-Cut Singleton Cross-Swap Augmentation

Let an edge-ordered complete graph have a spanning three-path cover A sqcup B sqcup {z}, with A and B nontrivial increasing paths. Orient A,B increasingly. Choose selected edges q->w of A and p->v of B. Let L(x) denote the incoming selected-edge label, with L(source)=-infinity, and U(x) the outgoing selected-edge label, with U(terminal)=+infinity. If L(q)<lambda(qz)<lambda(zv)<U(v) and L(p)<lambda(pw)<U(w), then deleting q->w and p->v and adding q->z, z->v, and p->w yields a spanning cover by two vertex-disjoint increasing paths. Explicitly the new paths are A_prefix_through_q followed by z followed by B_suffix_from_v, and B_prefix_through_p followed by A_suffix_from_w.

## S9025 — Singleton Endpoint Transfer Forces an Extreme Carrier-Triangle Edge

Let G be a finite edge-ordered complete graph with pc_inc(G)>2. A SOURCE TRANSFER for singleton pair {x,y} at carrier neighbor v means there are literal spanning three-covers A | (y,v,b_2,...,b_m) | {x} and A | (x,v,b_2,...,b_m) | {y}, with the obvious order-two interpretation when no b_2 exists. Then lambda(vx)<lambda(xy) and lambda(vy)<lambda(xy), so xy is the unique maximum edge of triangle {x,y,v}. Dually, a TERMINAL TRANSFER at carrier neighbor w means there are literal spanning three-covers A | (...,w,y) | {x} and A | (...,w,x) | {y}; then lambda(xy)<lambda(wx) and lambda(xy)<lambda(wy), so xy is the unique minimum edge of {x,y,w}. If the same unordered singleton pair {x,y} occurs in both a source transfer with carrier v and a terminal transfer with carrier w, where v,w are distinct from x,y, then lambda(vx),lambda(vy) < lambda(xy) < lambda(wx),lambda(wy). Consequently both (v,x,y,w) and (v,y,x,w) are increasing Hamilton P4 orders.

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

## S9029 — Hamilton-Five Density Hierarchy

### Theorem A — four of six deletions are Hamilton-five

Every six-vertex subset E of a Strong Level-(1) boundary tournament has at least four vertices e such that E\\{e} supports a tight five-vertex path.

### Theorem B — fixed-subset density hierarchy

Let W be an r-vertex subset, r>=6, of a Strong Level-(1) boundary tournament, and let S subset W have size s in {0,1,2,3}. Let h_5(W;S) be the number of five-subsets F of W containing S that support a tight P5. Then h_5(W;S) >= ((4-s)/(6-s)) * binom(r-s,5-s). Explicitly: at least two-thirds of all five-subsets of W are Hamilton-five supports; every fixed vertex lies in at least three-fifths of its possible five-set supersets that are P5 supports; every fixed pair lies in at least one-half; and every fixed triple lies in at least one-third. In particular every physical triple in any six-or-larger vertex set has many Hamilton-five extensions.

## S9030 — Johnson Local-Clique Density Principles

### Theorem A — dual-clique density bound

Let r>=k+1, let B be a family of k-subsets of an r-element ground set, write b=|B|, M=binom(r,k), and p=b/M. Assume every (k+1)-subset contains at most t members of B. Then (r-k+1)p^2-p <= t(t-1)(r-k)/(k(k+1)), hence p <= [1+sqrt(1+4t(t-1)(r-k)(r-k+1)/(k(k+1)))]/[2(r-k+1)]. For t>=2, equality can occur only if every (k+1)-set contains exactly t members of B and every (k-1)-set lies in the same number kb/binom(r,k-1) of members of B. The case `k=5,t=2` is the structural form used in Hamilton-five density applications.

### Theorem B — degree-local density bound

Let B be a family of k-subsets of an r-element ground set, r>=k+1, and suppose every (k+1)-set contains at most t members of B. Write p=|B|/binom(r,k). Then

p <= [k+(t-1)(r-k)]/[k(r-k+1)].

More precisely, the induced subgraph J(r,k)[B] has maximum degree at most (t-1)(r-k), while the intersection-clique decomposition forces average degree at least k(r-k+1)p-k. Comparing them gives the stated ceiling. Equality requires both mechanisms to be tight: every member F of B must lie in exactly t members of B inside every (k+1)-superset U of F, and the (k-1)-core occupancies x_S=|{F in B:S subset F}| must all be equal. For k=2,t=2 the bound becomes p<=r/[2(r-1)], the usual Mantel density scale. For k=5,t=2 it gives p<=r/[5(r-4)].

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

## S9032 — Tested-Dimer Two-Witness Interaction

Let D=(a,b) be a fixed tested oriented physical dimer in a Strong Level-(1) boundary tournament, and let x,y be distinct witnesses outside {a,b}. A head certificate on D with witness w means the exact ordered turn (w,a,b) is tight; a tail certificate on D with witness w means the exact ordered turn (a,b,w) is tight. Then two witness-indexed certificates on this same tested orientation have the following exhaustive interaction. (HH) If (x,a,b) and (y,a,b) are tight, they are exactly the same-support two-head extension collision packet on D with distinct witnesses x,y. (TT) If (a,b,x) and (a,b,y) are tight, they are exactly the same-support two-tail extension collision packet on D. (HT) If (x,a,b) and (a,b,y) are tight, then (x,a,b,y) is a literal vertex-simple tight P4. (TH) If (y,a,b) and (a,b,x) are tight, then (y,a,b,x) is a literal vertex-simple tight P4. Thus opposite-polarity certificates on one tested oriented dimer have an explicit strict two-ended realization, while same-polarity certificates are the literal two-extension collision packet. Tested order is part of the datum: a certificate tested on (a,b) and one tested on the reverse dimer (b,a) are not licensed as a same-oriented-support interaction merely because they share the unordered physical support {a,b}. To compare reverse-tested certificates, first treat (b,a) as its own tested oriented dimer and apply this theorem there. No cyclic permutation or witness-order rearrangement of a certified turn is licensed.

## S9033 — Deletion Block Count and Unique-Transition Witness Fan

### Theorem A — deletion block-count inequality

Let H be any finite directed tight-path system. Let V(H)=D disjoint-union S disjoint-union C, with S,C nonempty. Suppose A=A_1 sqcup ... sqcup A_a is a literal tight-path cover of H[D union S], and T=T_1 sqcup ... sqcup T_k is a literal tight-path cover of H-D=H[S union C]. Split every T-rail at each selected S|C transition and let b_C(T) be the total number of nonempty maximal contiguous C-blocks. Then pc(H) <= a+b_C(T). Equivalently b_C(T) >= pc(H)-a. In particular, if A is one tight path and pc(H)>k, then every k-rail cover T of H-D has b_C(T)>=k. If such a T has exactly one selected S|C transition, then it has the following canonical normal form: exactly one rail is mixed and consists of one S-block and one C-block, in either order; every other one of the k-1 rails lies wholly in C; hence all vertices of S occur in the unique S-block and there is no S-only rail. For `k=2` this gives the familiar two-rail crossing/block-count normal form, without Strong Level-(1) or any small-order hypothesis.

### Theorem B — unique transition inherits Hamilton boundary multiplicity

Let H be a finite exact-reversal tight-turn system with pc(H)>k. Partition V(H)=D disjoint-union S disjoint-union C with S,C nonempty, and suppose X=H[D union S] is Hamiltonian. Let T be a literal k-path cover of H-D having exactly one selected S|C transition. By Theorem A, T has one mixed rail and k-1 pure C-rails. (SC orientation.) Suppose the unique transition is the selected state x y with x in S and y in C. For every vertex p in (D union S)-{x} for which X has a Hamilton tight path ending with the ordered state (p,x), the turn (y,x,p) is tight. Hence the tested crossing dimer (y,x) is tail-signed by every such Hamilton predecessor p. In particular, two distinct Hamilton predecessors p_1,p_2 force a same-oriented two-tail witness collision on the actual selected crossing dimer (y,x). (CS orientation.) Dually, if the unique transition is y x with y in C and x in S, then for every p for which X has a Hamilton tight path starting with (x,p), the turn (p,x,y) is tight; thus the tested crossing dimer (x,y) is head-signed by every such Hamilton successor p, and two distinct successors force a same-oriented two-head witness collision. Therefore a unique recompletion transition converts Hamilton boundary multiplicity of the absorber into a role-sensitive witness fan on the literal selected crossing.

## S9034 — Complementary Absorbers Force Dual Non-Hamiltonicity

Let H be a finite boundary tournament with pc(H)>2. Let T be a vertex set, let c,d be distinct vertices outside T, and suppose there are tight paths L_c and L_d such that V(L_c)=V(H)\\(T union {d}) and V(L_d)=V(H)\\(T union {c}). Then neither H[T union {c}] nor H[T union {d}] has a Hamilton tight path.

## S9035 — Global-Longest Path Endpoint Shield

Let K=(k_1,...,k_m) be a globally longest tight path in a Strong Level-(1) boundary tournament. For every vertex w outside K, the direct endpoint attachment turns (w,k_1,k_2) and (k_{m-1},k_m,w) are bad. Hence by boundary antisymmetry the reverse endpoint turns (k_2,k_1,w) and (w,k_m,k_{m-1}) are tight. Thus every exterior vertex simultaneously witnesses both terminal reverse systems of K as graph-intrinsic facts.

## S9036 — Complete Mate-Box Collapse

Let H satisfy pc(H)>k. For j=1,...,r let A_j={alpha_{j,i}: i in I_j} be finite families of ordered turns. Assume that for every tuple (i_1,...,i_r) there is a literal spanning k-component path proposal C(i_1,...,i_r) whose only possibly bad turns are holes h_{j,i_j} with complete reversals alpha_{j,i_j}. Then at least one family A_j is entirely tight.

## S9037 — Extreme Dimers Turn Failed Cooperative Splices into Barrier Corridors

Let G be a finite edge-ordered complete graph with pc_inc(G)>2. MINIMUM-DIMER CORRIDOR: suppose G has a spanning increasing three-cover D|A|B where D is the dimer on vertices x,y and xy is the globally minimum edge. Orient A,B increasingly. Let p->v be any selected edge of A and let s be the source of B. If L_A(p)<lambda(ps)<U_B(s), then lambda(xv)>=U_A(v) and lambda(yv)>=U_A(v). MAXIMUM-DIMER CORRIDOR: suppose instead D is the dimer on vertices X,Y and XY is the globally maximum edge. Let p->v be any selected edge of A and t the terminal of B. If L_B(t)<lambda(tv)<U_A(v), then lambda(pX)<=L_A(p) and lambda(pY)<=L_A(p). Thus failure of all `S9015` cooperative splices with an extreme dimer produces simultaneous two-end successor barriers in the minimum case and simultaneous two-end predecessor barriers in the maximum case.

## S9038 — Reverse-Middle Two-Witness P4 Ear

Let A,C,x,y be four distinct vertices in a Strong Level-(1) boundary tournament. If (A,x,C) and (A,y,C) are tight, then at least one of (A,x,C,y) and (A,y,C,x) is a tight Hamilton P4. More precisely, if (x,C,y) is tight the first path is tight; if it is bad, boundary antisymmetry makes `(y,C,x)` tight and the second path is tight.

## S9039 — Three-of-Five Hamilton K4 Deletions

Every edge-ordered `K5` has at least three vertex deletions whose remaining four vertices support an increasing Hamilton `P4`. Equivalently, at most two of its five induced `K4`s are non-Hamiltonian.

Consequently, if `h_4(r)` denotes the number of four-subsets of an edge-ordered `K_r`, `r>=5`, that support an increasing Hamilton `P4`, then

`h_4(r) >= (3/5) C(r,4)`.

## S9040 — Complement-Free Johnson 5-of-10 Bounds

### Theorem A — four-core Johnson cut ceiling

Let `Omega` be a 10-element set and let `F` be a family of 5-subsets of `Omega` containing no complementary pair. Put `barF={Omega\A:A in F}`. In the Johnson graph `J(10,5)`, where two 5-sets are adjacent when they meet in four vertices,

`e_J(F,barF) <= 15|F|`.

Equivalently, the average number of four-overlap neighbors in `barF` seen from a member of `F` is at most `15`.

### Theorem B — spectral intersection-one ceiling

Let `G` be the graph on the 252 five-subsets of a 10-element set `Omega`, joining distinct `S,T` exactly when `|S intersect T|=1`. If `H` is a complement-free family of `m` five-subsets, then the average degree of the induced graph `G[H]` is at most

`7 + 18m/252`.

In particular, since complement-freeness implies `m<=126`, the average degree of `G[H]` is at most `16`.