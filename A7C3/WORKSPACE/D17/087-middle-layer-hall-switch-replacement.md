# Port maps, missing-chord escapes, and rooted Hall replacement

**Workspace:** D17
**State:** working
**Key:** `middle-layer-hall-switch-replacement`

**Summary:** Port maps split Hall obstructions before order transport; the section develops the aligned-cycle splice, off-circuit endpoint switches, missing-chord escape fans, exact rooted replacement ledger, fresh-core compression, and switch-free common-core graph normal form.

### 12. Port maps split the full Hall obstruction before any order transport

Retain the minimal all-endpoint Hall witness F|N. For an incidence S-R with S=R+{x}, choose an actual Hamilton path on S exposing the completion x. Its other physical endpoint is some p in R. Call p a PORT of R realized by this endpoint incidence. Let Pi(R) be the set of all such ports over every incident support and every actual endpoint-realizing Hamilton order.

There are three exact structural possibilities.

(PORT-SWITCH.) Some core R has at least two distinct ports p,q. Then the same Hall core is used by actual endpoint completions whose Hamilton paths terminate at different physical vertices of R. This is a physical endpoint-role switch, stronger data than merely saying two induced Hamilton orders differ.

(PAIR-SWITCH.) Every core has a unique port, but some support S has two different endpoint pairs. Under unique ports those two endpoint pairs must be disjoint. Indeed if actual Hamilton paths on S had endpoint pairs {u,v} and {u,w} with v!=w, then at the common endpoint-deletion core S-{u}, completion u would be paired once with port v and once with port w, contradicting uniqueness of its port. Thus a support-level pair-switch is literally two disjoint endpoint pairs on one fixed k-support.

(RIGID GRAPH.) Every core has one port and every support has exactly one endpoint pair. Then the Hall incidence graph becomes an ordinary simple graph G on vertex set N: a support S whose unique endpoints are u,v joins the two endpoint-deletion cores R_u=S-{u} and R_v=S-{v}. At R_u the completion u is paired with port v, so p(R_u)=v; at R_v, p(R_v)=u. Hence

  R_u-{p(R_u)} = S-{u,v} = R_v-{p(R_v)}.

Because the original Hall incidence graph B[F,N] is connected and every support now has exactly the two incidences supplied by its unique endpoint pair, G is connected. Therefore the displayed (k-2)-set is constant throughout G; call it M. Every right core and every left support have the exact forms

  R_p = M union {p},
  S_pq = M union {p,q},

and every Hamilton path witnessing the unique endpoint pair of S_pq has physical endpoints p,q.

In this rigid branch each support has degree exactly two in the Hall incidence graph. Consequently Hall minimality translates literally to graph sparsity:

  |E(G)|=|F|=|N|+1=|V(G)|+1,

while every proper edge family E' satisfies |E'|<=|V(E')|. Also every vertex has degree at least two, since every Hall core has at least two support neighbors. Thus G is a connected minimal bicycle: deleting any nonempty proper collection down to its incident-vertex subgraph leaves cyclomatic excess at most one, while G itself has cyclomatic number two. Equivalently its suppressed topology is a theta, a figure-eight, or two cycles joined by a path.

This trichotomy is purely endpoint-pair geometry. It does not assume that Hamilton orders at a core synchronize, and it does not use R435. The next order-valued work may therefore be concentrated separately on a core port-switch, a disjoint support pair-switch, or the common-M rigid bicycle.

### 13. At k=5 an order-aligned Hall cycle is impossible by a direct six-vertex splice

Specialize to the first live uniform order k=5, so |H|=11 and an aligned cycle from sections 9-10 has |M|=3. Write

  M=(a,c,b).

Every aligned cycle has length at least four, so its alternating normal form supplies distinct x,y in X and distinct z,w in Z. Section 10 gives the saturation identities

  (a,x,t), (a,y,t) tight for every t outside M union the named X-vertex,

and

  (t,z,b), (t,w,b) tight for every t outside M union the named Z-vertex.

In particular

  (a,y,z), (a,y,w), (y,z,b), (y,w,b)

are tight, and the x/y-dual statements also hold.

Boundary antisymmetry on the physical triple {x,a,y} says exactly one of

  (x,a,y), (y,a,x)

is tight. Suppose first that (x,a,y) is tight. If (z,b,w) were tight, then

  (x,a,y,z,b,w)

would be a tight P6: its four turns are (x,a,y), (a,y,z), (y,z,b), (z,b,w). Since the uniform branch has no P6, (z,b,w) is bad, and R3 therefore gives

  (w,b,z) tight.

But then

  (x,a,y,w,b,z)

is a tight P6, using the turns (x,a,y), (a,y,w), (y,w,b), (w,b,z), again a contradiction. The case (y,a,x) tight is identical after exchanging x and y.

Therefore NO fully order-aligned matching cycle can occur when k=5. In particular, every near-perfect-matching functional cycle at order eleven contains a genuine closed-cycle order mismatch unless growth has already occurred.

This is a finite-base theorem internal to the Hall development, not a general large-k rectangle theorem. Exact feasibility checks show that the analogous bare 2x2 aligned rectangle can survive locally for k=6 even when the two same-side k-supports are Hamiltonian, so the six-vertex splice above should not be extrapolated without additional Hall structure.

Status: sections 12-13 are complete internal arguments and working/expository only. They refine the Closed Hall Obstruction Growth target but do not yet eliminate port-switch, pair-switch, or the rigid-bicycle order-switch branches.


### 14. Minimum Hall circuits force off-circuit endpoint switches

Strengthen the extremal choice of the Hall witness: among ALL Hall-deficient left families choose F with minimum cardinality. It is automatically inclusion-minimal, so sections 7-12 apply. Suppose its port-map branch is RIGID. Thus there is a fixed (k-2)-set M and a connected simple graph G on a label set U such that

  R_p=M union {p}  (p in U),
  S_pq=M union {p,q}  (pq in E(G)),

every Hamilton path on S_pq has physical endpoint set exactly {p,q}, and G is a bicircular circuit: |E(G)|=|U|+1 while every proper edge family E' has at most as many edges as incident vertices.

The following graph lemma is the useful new extremal input.

**Chord lemma for a bicircular circuit.** Let G be a simple bicircular circuit and let e=pq be a missing edge between two vertices of G. If G+e contains no bicircular circuit with fewer edges than G, then G is K4 minus one edge and e is its missing sixth edge.

Proof. A bicircular circuit has minimum degree at least two: if v had degree one, deleting its incident edge would also delete v from the incident-vertex set and would leave a proper edge family with one more edge than incident vertices, contradicting circuit minimality. Fix f in E(G). Since G-f is a proper subset of a circuit it is bicircular-independent. But H_f=G-f+e has |V(G)|+1 edges on |V(G)| vertices, hence is dependent, and every circuit contained in H_f must use e. If no smaller circuit exists, H_f itself must therefore be a circuit for every f. Now let v be any degree-two vertex of G not equal to p or q and choose f incident with v. In H_f the vertex v has degree one, impossible for a circuit. Hence every degree-two vertex of G lies in {p,q}. Since

  sum_v (deg_G(v)-2)=2|E(G)|-2|V(G)|=2

and all degrees are at least two, either one vertex has degree four and all others degree two, or two vertices have degree three and all others degree two. In the first case all but one vertices have degree two, so |V(G)|<=3, impossible for a simple graph with |E|=|V|+1. In the second case |V(G)|<=4. Simplicity again excludes |V|<=3, and on four vertices the degree sequence is (3,3,2,2), uniquely K4 minus one edge. Conversely that graph has no smaller simple bicircular circuit, so the exception is sharp.

Now take any missing pair pq of U. Uniform k-set Hamiltonicity makes T=M union {p,q} Hamiltonian. If EVERY Hamilton path on T had endpoint set exactly {p,q}, then T would behave as the rigid chord e. Unless G=K4-e, the chord lemma gives a strictly smaller bicircular circuit C contained in G+pq. The supports indexed by C have exactly their two graph-endpoint cores as Hall neighbors, so they form a Hall-deficient family smaller than F, contradicting the minimum-cardinality choice.

Therefore, outside the exceptional K4-e case, EVERY missing chord pq forces nonrigid endpoint geometry on T=M union {p,q}: some Hamilton path on T has endpoint pair different from {p,q}. This output is physically localized. If the new endpoint pair contains exactly one of p,q, its other endpoint lies in M and gives a genuine PORT-SWITCH at the existing core R_q or R_p. If both endpoints lie in M, deleting either endpoint gives an endpoint core outside the rigid neighborhood {M union {u}:u in U}. Thus minimum Hall extremality converts every missing rigid chord into either an existing-core port switch or a genuinely new off-circuit endpoint core.

This is a global augmentation pressure arising from the second Hall cycle. It is not available from one selected matching cycle. The only rigid graph not eliminated by the chord lemma is K4-e.

### 15. At k=5 the exceptional rigid K4-e is impossible

For k=5 the common core M has three vertices. The K4-e exception contains a triangle of three rigid supports around M. The following exact seven-vertex finite theorem eliminates such a triangle in any no-P6 ambient system with even one additional vertex.

**Rigid-triangle seven-vertex theorem.** Let M={0,1,2}, let x=3,y=4,z=5, and let w=6. Suppose each of the three five-sets M+{x,y}, M+{x,z}, M+{y,z} supports a Hamilton P5 and EVERY Hamilton P5 on each such support has endpoint set equal to its displayed exterior pair. Then the seven vertices support a tight P6.

Exact finite certificate. Encode boundary antisymmetry by 105 Boolean variables, one for each complete-reversal pair of ordered triples on seven vertices. Canonical representatives are ordered lexicographically; a true variable means the canonical orientation is tight. For every ordered six-tuple, forbid simultaneous tightness of its four consecutive turns, giving 7P6=5040 no-P6 clauses. For each rigid five-support there are 120 vertex orders. Exactly 12 orders have the prescribed exterior endpoint set, so the other 108 are forbidden by three-literal no-P5 clauses; over the three supports this gives 324 clauses. Introduce one witness variable for each of the 36 allowed endpoint-preserving orders. Each witness implies its three consecutive tight turns, giving 108 implication clauses, and one 12-literal existence clause is imposed for each of the three supports. Thus the CNF has

  105+36=141 variables,
  5040+324+108+3=5475 clauses.

A complete deterministic DPLL verification is UNSAT. After unit propagation, choose a variable of maximum occurrence among the currently shortest unresolved clauses, breaking ties by smallest variable index; branch False before True. Number the 105 turn variables by lexicographic canonical reversal representative, then the witness variables support-by-support in the order {3,4},{3,5},{4,5}, with allowed Hamilton orders lexicographic. This search closes all branches after 1599 DPLL nodes, maximum branch depth 21. Independently, translating every clause to its equivalent binary linear inequality gives an infeasible 141-variable binary MILP under SciPy/HiGHS. Hence the rigid triangle plus a seventh vertex cannot avoid P6.

Return to the order-eleven uniform residue. A rigid Hall graph has |U|>=4. If |U|=4 then |E|=5, so G=K4-e and contains a rigid triangle; H has vertices outside the six-set M plus that triangle packet, so the rigid-triangle theorem yields P6, contradiction. If |U|>=5, G has a missing chord and section 14 forces off-circuit nonrigid endpoint geometry. Thus at k=5 the RIGID branch is completely reduced to a physical port switch or a new endpoint core; there is no surviving purely rigid Hall bicycle.

For general k the symbolic chord lemma remains valid, but the K4-e exceptional rigid nucleus is not yet eliminated. Also, the port-switch/new-core outputs are progress interfaces, not yet a proof of P_{k+1}. The remaining parent theorem must consume these switches using the near-perfect matching and alternating-reachability structure.


### 16. Missing-chord escapes are injective, but a counting threshold forces an adjacent repeated internal endpoint

Continue in the minimum-cardinality rigid-bicycle setting of section 14, with common core M, exterior label set U=V(G), and r=|U|. Assume G is not the exceptional K4-e nucleus, so every missing chord pq has a Hamilton support

  T_pq=M union {p,q}

with some endpoint pair different from {p,q}. If such a path has exactly one endpoint in {p,q}, section 14 already gives a PORT-SWITCH at an existing rigid core. Thus, in the branch where no such port switch occurs, every missing chord admits an actual Hamilton path whose two endpoints both lie in M. For each missing chord pq choose one such endpoint pair A_pq subset M, |A_pq|=2.

There is an important one-step limitation. If m in A_pq and we delete endpoint m from the chosen Hamilton path on T_pq, the resulting Hamilton (k-1)-core is

  W(m,pq)=(M-{m}) union {p,q}.

These escape cores do not collide accidentally: relative to fixed M, W(m,pq) uniquely determines m as the unique missing vertex of M and determines {p,q}=W(m,pq)-M. Hence

  W(m,pq)=W(m',p'q')  implies  m=m' and {p,q}={p',q'}.

So raw counting of fresh right cores cannot by itself contradict Hall deficiency.

Nevertheless, the endpoint labels on the missing chords cannot always remain completely dispersed. Let

  h = C(r,2)-|E(G)| = C(r,2)-r-1

be the number of missing chords. For each m in M form a graph J_m on U whose edges are those missing chords pq for which m belongs to the chosen pair A_pq. Every missing chord appears in exactly two of the J_m, so

  sum_{m in M} |E(J_m)| = 2h.

If no J_m contains two adjacent edges, then every J_m is a matching and therefore

  2h <= |M| floor(r/2) = (k-2) floor(r/2).

Consequently, whenever

  2[C(r,2)-r-1] > (k-2) floor(r/2),                         (16.1)

there exist distinct missing chords pq and pr sharing an exterior label p and an internal vertex m in M such that the selected Hamilton paths on both T_pq and T_pr use m as an endpoint.

At k=5, |M|=3 and (16.1) holds for every r>=5: its left side is r^2-3r-2, while the right side is 3 floor(r/2), and the inequality already reads 8>6 at r=5 and only widens thereafter. Therefore, after the k=5 K4-e exception is removed, any no-port-switch rigid exit with r>=5 contains a coherent two-chord escape fan

  pq, pr, m.

This is stronger than merely having many fresh cores. The two chord supports share the physical exterior label p and one physical internal endpoint m.

### 17. The coherent two-chord fan feeds a second-generation Hamilton support

Retain missing chords pq and pr and shared m from section 16. Choose actual Hamilton paths on

  T_q=M union {p,q},
  T_r=M union {p,r}

with endpoint pairs {m,a_q} and {m,a_r}, where a_q,a_r belong to M-{m}. Deleting m gives the two first-generation Hamilton cores

  W_q=(M-{m}) union {p,q},
  W_r=(M-{m}) union {p,r}.

Their inherited ports are respectively a_q and a_r: in T_q the completion m is paired with a_q at W_q, and similarly for T_r.

Now use the full uniform middle layer on the k-set

  K=(M-{m}) union {p,q,r}.

It has an actual Hamilton path. Its endpoint pair is strongly constrained if no PORT-SWITCH is allowed.

* The pair {q,r} is impossible. Deleting r would realize port q at W_q, different from its inherited internal port a_q; symmetrically deleting q changes the port of W_r.

* If r is an endpoint, then the other endpoint must be exactly a_q. Indeed deleting r leaves W_q, so any other partner would be a second port of W_q. Thus the only no-switch endpoint pair involving r is {r,a_q}. Dually, the only no-switch endpoint pair involving q is {q,a_r}.

* If neither q nor r is an endpoint, then both endpoints lie in (M-{m}) union {p}. Deleting either produces an endpoint core that omits m but contains both q and r, hence lies outside the original rigid neighborhood {M union {u}:u in U}.

Therefore every Hamilton realization of K gives one of the following verified outcomes:

  (i) a PORT-SWITCH at W_q or W_r;
  (ii) endpoint pair {r,a_q};
  (iii) endpoint pair {q,a_r};
  (iv) two second-generation endpoint cores outside the original rigid neighborhood.

In cases (ii) and (iii) one endpoint deletion is the named first-generation core W_q or W_r and the other endpoint deletion is itself a new second-generation core. Thus even the completely port-quiet branch cannot terminate at two isolated fresh cores: uniformity forces a literal transport step from a first-generation escape core to another off-circuit core through one actual k-support K.

For k=5 this reduction occurs on the six physical vertices M union {p,q,r}. Local six-vertex PORT-SWITCH and PAIR-SWITCH fences show that this transport step alone need not force P6. The remaining theorem must use its attachment back to the minimum Hall bicycle and/or a further uniform completion. In particular, no generic R435 output is claimed here.

Status: sections 16-17 are complete internal symbolic arguments conditional only on the working section-14 missing-chord conclusion. They do not assert closure of Uniform Middle-Layer Growth.


### 18. Exact rooted Hall-replacement ledger

Retain a minimum-cardinality Hall-deficient family F in the all-endpoint incidence graph, with N=N(F) and |N|=|F|-1. Let D be a set of original supports to delete and let A be a family of off-circuit Hamilton supports to insert. All endpoint incidences of the inserted supports are counted; no selected endpoint pair is substituted for the full neighborhood.

Define

  X(A)=N(A)-N,

(the genuinely fresh endpoint cores of the inserted supports), and

  L(D)=N-N(F-D),

(the old cores whose every original incident support lies in D). After insertion, an old core is truly lost only when it lies in L(D)-N(A). For

  F'=(F-D) union A

we therefore have the exact neighborhood identity

  |N(F')|=|N|-|L(D)-N(A)|+|X(A)|.

Since |F|=|N|+1,

  |F'|-|N(F')|
    = 1+|A|-|D|+|L(D)-N(A)|-|X(A)|.              (18.1)

Consequently F' is Hall-deficient exactly when

  |X(A)| <= |A|-|D|+|L(D)-N(A)|.                 (18.2)

This is the rooted replacement ledger. It distinguishes three different phenomena which selected-edge bookkeeping can conflate: fresh cores created by inserted supports, old cores actually lost after removals, and old cores restored by the inserted supports. A switch or new endpoint core is not a Hall improvement unless it satisfies this complete incidence ledger or yields a direct path absorber.

### 19. Proper rigid replacements require fresh-core compression

Now suppose F is in the R928 rigid-bicycle branch, so F is the edge set of a connected simple minimal bicycle G and N is its vertex set. Let D be a nonempty proper set of edges of G. Then

  |L(D)| <= |D|-1.                                (19.1)

Indeed every lost vertex has all its incident G-edges in D and has G-degree at least two, so 2|L(D)|<=2|D|. Equality |L(D)|=|D| would force every D-edge to have both endpoints lost and every lost vertex to have degree exactly two. Since lost vertices have no G-edge outside D, they would form a union of connected components of G. Connectedness and D proper rule this out, proving (19.1).

Combining (18.2) with |L(D)-N(A)|<=|L(D)| gives the necessary condition

  |X(A)| <= |A|-1                                (19.2)

for ANY Hall-deficient replacement which removes a nonempty proper part of the original rigid circuit. Thus an inserted family must achieve genuine FRESH-CORE COMPRESSION: it must create strictly fewer new endpoint cores than supports inserted.

This immediately fences the shallow coherent two-chord transport of sections 16-17. In the no-original-port-switch branch, each missing-chord support has two endpoints in M and hence at least two fresh endpoint cores. Escape-core injectivity makes the fresh-core sets of two distinct missing chords disjoint. Therefore the two chord supports already contribute at least four fresh cores. Adding the one second-generation support K can reuse some of them but cannot remove them. For

  A={T_q,T_r,K}

we have |A|=3 and |X(A)|>=4, whereas (19.2) would require |X(A)|<=2. Hence two first-generation chords plus one second-generation transport support can never, by themselves, form a proper Hall-deficient rooted replacement. More escape generations without a compression mechanism are not progress toward circuit replacement.

### 20. Switch-free endpoint components are rigid common-core graphs

The rigid common-core conclusion does not require Hall minimality. Consider any connected component of the COMPLETE all-endpoint incidence graph and assume throughout that every incident right core has one physical port and every Hamilton k-support has one endpoint pair. For a support S with endpoint pair {u,v}, its two incident endpoint cores are R_u=S-{u} and R_v=S-{v}. Unique ports give

  R_u-{p(R_u)} = S-{u,v} = R_v-{p(R_v)}.

Connectedness propagates one fixed (k-2)-set C through the component. Hence its cores and supports have the exact forms

  R_x=C union {x},
  S_xy=C union {x,y},

and every Hamilton path on S_xy has endpoint pair {x,y}. The component is therefore the ordinary incidence graph of a simple graph G_C on at most

  |V(H)-C| = k+3

core labels.

This gives the correct interpretation of off-circuit escape under global absence of PORT-SWITCH and PAIR-SWITCH. It does not form an amorphous sequence of generations. It enters another rigid common-core graph component. A tree component has one fewer support than core, a unicyclic component has equal numbers, and fresh-core compression |X|<|A| first becomes possible only when the inserted support graph contains two independent cycles, equivalently a bicircular Hall circuit. Thus the rooted return objects are exactly:

  a genuine PORT-SWITCH or PAIR-SWITCH,
  a fresh rigid bicycle/Hall circuit,
  or a direct path absorber.

In particular, the second-generation fan of section 17 is merely the beginning of another rigid component when all switches are suppressed.



## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    }
]
```
