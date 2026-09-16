# Two tight paths in a boundary tournament

## 1. Definitions and the minimal-counterexample reduction

Throughout, vertex sets are finite.

For an integer `r>=2` and a set `V`, let `V^{\underline r}` denote the set of ordered `r`-tuples of pairwise distinct vertices of `V`. An **r-uniform directed hypergraph**, or **r-digraph**, is a pair `G=(V,E)` with `E⊆V^{\underline r}`. The set `V` is the vertex set, written `V(G)`, and the members of `E` are the directed `r`-edges. In this document `r=3` unless explicitly stated otherwise.

For an ordered triple `(x,y,z)` of distinct vertices, its **reverse** is `(z,y,x)`. A **3-uniform boundary tournament**, hereafter simply a **boundary tournament**, is a 3-digraph `H=(V,E)` such that for every three distinct vertices `x,y,z`, exactly one of

`(x,y,z)`, `(z,y,x)`

belongs to `E`. An ordered triple belonging to `E` is called **tight**. Thus boundary antisymmetry is the assertion that exactly one member of every reversal pair is tight.

For `S⊆V(H)`, write `H[S]` for the induced boundary tournament with vertex set `S`, and write `H-S` for `H[V(H)-S]`. For a vertex `v`, `H-v` abbreviates `H-{v}`.

A **tight path** is an ordered list

`P=(v_0,...,v_k)`

of distinct vertices such that `(v_{i-1},v_i,v_{i+1})` is tight for every `1<=i<=k-1`. Its vertex set is `V(P)={v_0,...,v_k}` and its order is `|P|=k+1`. Paths of order one or two satisfy the condition vacuously. The **ordinary edges** of `P` are the unordered pairs `{v_{i-1},v_i}`. The endpoints are `v_0,v_k`; when `k>=2`, the other vertices are internal. A path is **nontrivial** if it has order at least two.

A **path cover** of an induced boundary tournament `G` is a partition of `V(G)` into vertex sets of tight paths, together with one chosen tight ordering on each part. Write `pc(G)` for the minimum number of paths in such a cover. An **exact k-path cover** has exactly `k` nonempty path components. We write `P|Q|R` for a path cover with the displayed components. The **ordinary path forest** of a path cover is the ordinary graph on the same vertex set whose edges are the ordinary edges of its path components. A tight path on all vertices of `G` is a **Hamilton path** of `G`, and `G` is **Hamiltonian** if it has such a path. A path is **proper in G** if its vertex set is a proper subset of `V(G)`.

A **tight cycle** is a cyclic ordering of at least three distinct vertices in which every cyclically consecutive ordered triple is tight. It is **proper in H** if its vertex set is a proper subset of `V(H)`. Opening a tight cycle at any one of its ordinary cycle edges gives a tight path on the same vertex set.

The conjecture is

> Every boundary tournament has path-cover number at most two.

**Status.** The conjecture remains open. The established proof spine below ends before the augmentation step needed to contradict the extremal three-path cover constructed in Section 6. The missing augmentation statement and research directions are recorded in `GN3/MIGRATION/EVIDENCE/AUGMENTATION_FRONTIER.md`.

Assume the conjecture is false. Choose a counterexample `H` with minimum order, and write

`n=|V(H)|`.

Every proper induced subgraph of `H` has path-cover number at most two. Unless another ambient boundary tournament is explicitly named, every path, cycle, and induced subgraph below is a path, cycle, or induced subgraph of `H`. Choosing any vertex `v`, a two-path cover of `H-v` together with `(v)` gives a three-path cover of `H`; hence

`pc(H)=3`.

Also `n>=4`: a boundary tournament on at most three vertices is covered by at most two tight paths.

### Lemma 1.1. Complements of paths

Let `S` be a nonempty proper subset of `V(H)`. If `H[S]` has a Hamilton tight path, then

`pc(H-S)=2`.

Consequently every proper tight path of `H` extends, by adding a two-path cover of its complement, to a spanning three-path cover of `H`.

**Proof.** Minimality gives `pc(H-S)<=2`. If `H-S` were Hamiltonian, its Hamilton path together with a Hamilton path on `S` would be a spanning two-path cover of `H`, contradicting `pc(H)=3`. Therefore `pc(H-S)=2`. ∎

### Lemma 1.2. Deleting two vertices

For distinct vertices `a,c`, every minimum path cover of `H-{a,c}` is an exact two-path cover, and both paths are nontrivial.

**Proof.** Apply Lemma 1.1 to the two-vertex path `(a,c)`. Thus `pc(H-{a,c})=2`. If an exact two-path cover had singleton component `(s)`, boundary antisymmetry makes exactly one of `(a,s,c)` and `(c,s,a)` tight. That tight three-vertex path together with the other component would two-cover `H`, a contradiction. ∎

A spanning three-path cover has `n-3` ordinary edges. No spanning forest whose components are tight paths can have more ordinary edges, because a path forest on `n` vertices with more than `n-3` edges has at most two components and would give a two-path cover.

## 2. Small-order lemmas

Let `K_V` denote the ordinary complete graph on a vertex set `V`. Its edge set consists of the two-element subsets of `V`. The **line graph** `L(K_V)` has vertex set `E(K_V)`, with two vertices adjacent exactly when the corresponding ordinary edges meet.

For a boundary tournament `G` on `V`, define the **comparison digraph** `Gamma(G)` as the orientation of `L(K_V)` in which, for distinct `u,v,w`,

`{u,v} -> {v,w}`

if and only if `(u,v,w)` is tight.

An **edge order** on `K_V` is a strict total order `<` on `E(K_V)`. An **edge-ordered complete graph** is a complete graph together with such an edge order. A vertex-simple sequence `(v_0,...,v_k)` is an **increasing path** if

`{v_0,v_1} < {v_1,v_2} < ... < {v_{k-1},v_k}`.

### Lemma 2.1. Comparison representation

For every boundary tournament `G`:

1. `Gamma(G)` is a well-defined orientation of `L(K_V)`.
2. A vertex-simple sequence is a tight path in `G` if and only if its consecutive ordinary edges form a directed chain in `Gamma(G)`.
3. There exists an edge order `<` satisfying
   
   `(u,v,w) is tight  iff  {u,v}<{v,w}`
   
   for all distinct `u,v,w` if and only if `Gamma(G)` is acyclic.
4. If `Gamma(G)` is cyclic and `C` is a shortest directed cycle, then `C` is chordless in `L(K_V)`. Its underlying ordinary edges are either a three-edge star, the three edges of an ordinary triangle, or the edges of a vertex-simple ordinary cycle of length at least four.

**Proof.** If `{u,v}` and `{v,w}` are incident ordinary edges, the two possible comparison directions correspond to the reversal pair `(u,v,w)` and `(w,v,u)`. Boundary antisymmetry chooses exactly one, proving the first assertion.

For a vertex-simple sequence `P=(v_0,...,v_k)`, put `e_i={v_{i-1},v_i}`. By definition, `e_i->e_{i+1}` is equivalent to tightness of `(v_{i-1},v_i,v_{i+1})`. This proves the second assertion.

If an edge order realizes all tight triples, every comparison arc points from a smaller edge to a larger edge, so `Gamma(G)` is acyclic. Conversely, if `Gamma(G)` is acyclic, it has a vertex of indegree zero: otherwise, following incoming arcs indefinitely would repeat a vertex and create a directed cycle. Repeatedly remove such a vertex to obtain a topological ordering of all vertices. In that total order, each adjacent pair of vertices of `Gamma(G)` appears in the direction of its comparison arc, so the order realizes every tight triple. This proves the third assertion.

Now let

`e_0 -> e_1 -> ... -> e_{m-1} -> e_0`

be a shortest directed cycle. A chord between nonconsecutive cycle vertices, in either direction, combines with one of the two directed segments of the cycle to give a shorter directed cycle. Hence the cycle is chordless.

For `m=3`, three pairwise incident ordinary edges are either the three edges of one triangle or three edges through one common vertex. For `m>=4`, chordlessness implies that nonconsecutive ordinary edges are disjoint and consecutive ones meet. Writing `v_i=e_{i-1}∩e_i` cyclically, the vertices `v_i` are distinct and `e_i={v_i,v_{i+1}}`. Thus the ordinary edges form a vertex-simple cycle. ∎

An **ordinary tournament** on a set `S` is an orientation of the complete graph on `S`. It is **transitive** if its vertices can be linearly ordered so that every arc points forward.

### Lemma 2.2. Three common-endpoint triples force a Hamilton five-path

Let `a,c,p,q,r` be distinct vertices of `H`. If

`(a,p,c)`, `(a,q,c)`, `(a,r,c)`

are tight, then `H[{a,c,p,q,r}]` has a Hamilton tight path.

**Proof.** For distinct `x,y∈{p,q,r}`, define tournaments

`x ->_a y` iff `(x,a,y)` is tight,

`x ->_c y` iff `(x,c,y)` is tight.

If distinct `x,y,z` satisfy `x->_a y->_c z`, then `(x,a,y,c,z)` is a Hamilton tight path. Assume no such mixed chain exists.

The tournament `->_a` cannot be transitive. Otherwise relabel so `x->_a y->_a z` and `x->_a z`. Excluding `(x,a,y,c,z)` forces `z->_c y`, while excluding `(x,a,z,c,y)` forces `y->_c z`, impossible. Hence, after relabelling,

`p->_a q->_a r->_a p`.

Excluding the three mixed chains forces

`r->_c q`, `p->_c r`, `q->_c p`.

Assume still that no Hamilton five-path exists. In each of the following six words the first two consecutive triples are tight, so the third must be non-tight and its reverse must be tight:

| word | forced tight triple |
| --- | --- |
| `a p c r q` | `(q,r,c)` |
| `a q c p r` | `(r,p,c)` |
| `a r c q p` | `(p,q,c)` |
| `p q a r c` | `(a,q,p)` |
| `q r a p c` | `(a,r,q)` |
| `r p a q c` | `(a,p,r)` |

Using these six triples and the same argument gives:

| word | forced tight triple |
| --- | --- |
| `a p r c q` | `(c,r,p)` |
| `a q p c r` | `(c,p,q)` |
| `a r q c p` | `(c,q,r)` |
| `p a q r c` | `(r,q,a)` |
| `q a r p c` | `(p,r,a)` |
| `r a p q c` | `(q,p,a)` |

Set

`u=1` iff `(q,p,r)` is tight,
`v=1` iff `(p,q,r)` is tight,
`w=1` iff `(p,r,q)` is tight.

For each of the eight values of `(u,v,w)`, every consecutive triple of each candidate below is already determined except the displayed reversal pair:

| `(u,v,w)` | first candidate | second candidate | remaining reversal pair |
| --- | --- | --- | --- |
| `000` | `a c q r p` | `r p q c a` | `(a,c,q)` / `(q,c,a)` |
| `100` | `c a r q p` | `q p r a c` | `(c,a,r)` / `(r,a,c)` |
| `010` | `a c p q r` | `q r p c a` | `(a,c,p)` / `(p,c,a)` |
| `110` | `a c p q r` | `q r p c a` | `(a,c,p)` / `(p,c,a)` |
| `001` | `c a p r q` | `r q p a c` | `(c,a,p)` / `(p,a,c)` |
| `101` | `c a p r q` | `r q p a c` | `(c,a,p)` / `(p,a,c)` |
| `011` | `a c r p q` | `p q r c a` | `(a,c,r)` / `(r,c,a)` |
| `111` | `c a q p r` | `p r q a c` | `(c,a,q)` / `(q,a,c)` |

Boundary antisymmetry makes exactly one member of the remaining reversal pair tight. Hence one candidate in each row is a Hamilton tight path, a contradiction. ∎

### Lemma 2.3. Non-Hamiltonian five-sets are edge-orderable

Let `G` be a boundary tournament on exactly five vertices. If `G` has no Hamilton tight path, then `Gamma(G)` is acyclic. Equivalently, `G` is realized by an edge order on `K_5` in the sense of Lemma 2.1.

**Proof.** Suppose `G` is non-Hamiltonian and `Gamma(G)` contains a directed cycle. Choose a shortest one. By Lemma 2.1 it is a star triangle, an ordinary triangle, or a vertex-simple ordinary cycle. A comparison cycle of length five itself gives a Hamilton tight path, so an ordinary cycle can only have length four.

In the case tables below, a three-letter string such as `xyz` abbreviates the assertion that `(x,y,z)` is tight. We repeatedly use the following forcing rule. Let `W=v_0v_1v_2v_3v_4` be a word on all five vertices. If two of its three consecutive triples are known to be tight, then the third cannot also be tight, because otherwise `W` is a Hamilton path. Hence the reverse of the third triple is tight. We write `W => xyz` when this rule forces the triple `(x,y,z)`.

**Ordinary four-cycle.** Normalize the comparison cycle as

`oa -> ab -> bc -> co -> oa`,

so `(o,a,b),(a,b,c),(b,c,o),(c,o,a)` are tight, and let `d` be the fifth vertex. The following complementary branches are exhaustive; each row is read from left to right.

| branch | successive forced triples | contradiction |
| --- | --- | --- |
| `acd, oac` | `bcoad=>dao; boacd=>aob; daobc=>cbo; cdaob=>adc; adcbo=>bcd; oabcd=>bao` | `oab` and `bao` |
| `acd, cao` | `dbcoa=>cbd; doabc=>aod; caodb=>bdo; acbdo=>bca; bcaod=>doa; doabc=>bao` | `oab` and `bao` |
| `dca, bac` | `coabd=>dba; odbac=>bdo; abcod=>doc; bdoca=>aco; dbaco=>abd; coabd=>bao` | `oab` and `bao` |
| `dca, cab` | `dcabo=>oba; dabco=>bad; obadc=>cda; cobad=>boc; bocda=>dco; dcoab=>bao` | `oab` and `bao` |

Thus a shortest comparison cycle is not an ordinary four-cycle.

**Star triangle.** Normalize the star triangle at `o` so that

`(a,o,b)`, `(b,o,c)`, `(c,o,a)`

are tight. For the fifth vertex `d`, set

`S(d)={u in {a,b,c} : (u,o,d) is tight}`.

Cyclic permutation of `a,b,c` preserves the normalized star triangle. Also define the reverse boundary tournament `G^rev` by declaring `(x,y,z)` tight in `G^rev` exactly when `(z,y,x)` is tight in `G`. Reversing the vertex order of a tight path in `G` gives a tight path in `G^rev`. Passing to `G^rev` and then exchanging the labels `b,c` restores the normalized star triangle and sends `|S(d)|` to `3-|S(d)|`. Hence it is enough to treat `|S(d)|=0` and `|S(d)|=1`.

If `|S(d)|=0`, then `(d,o,a),(d,o,b),(d,o,c)` are tight. The following branches are exhaustive:

| branch | successive forced triples | contradiction |
| --- | --- | --- |
| `obc` | `dobca=>acb; doacb=>cao; dcaob=>acd; aobcd=>dcb; daobc=>oad; oadcb=>cda; bocda=>dco; bdcoa=>cdb; acdbo=>obd; caobd=>oac` | `oac` and `cao` |
| `cbo, oda, oba, bdc` | `bdcoa=>ocd; bocda=>adc; obadc=>dab; odabc=>cba; docba=>bco; dbcoa=>cbd; aobdc=>dbo; adboc=>bda; cbdao=>oad; bcoad=>dao` | `oda` and `dao` |
| `cbo, oda, oba, cdb` | `dobac=>cab; cdoba=>odc; odcab=>acd; acdbo=>obd; caobd=>oac; oacdb=>cao` | `oac` and `cao` |
| `cbo, oda, abo, oac` | `abocd=>dco; daboc=>bad; badco=>cda; cdaob=>oad; coadb=>bda; bcoad=>ocb; ocbda=>dbc; doacb=>bca; odbca=>bdo; bdoac=>cao` | `oac` and `cao` |
| `cbo, oda, abo, cao` | `dcaob=>acd; abocd=>dco; bdcoa=>cdb; acdbo=>obd; caobd=>oac` | `oac` and `cao` |
| `cbo, ado, obd` | `caobd=>oac; badoc=>dab; daboc=>oba; dobac=>cab; cdoba=>odc; odcab=>acd; aobdc=>cdb; oacdb=>cao` | `oac` and `cao` |
| `cbo, ado, dbo` | `adboc=>bda; cadob=>dac; bdaco=>oca; dboca=>obd` | `obd` and `dbo` |

If `|S(d)|=1`, cyclically relabel so `S(d)={c}`. Thus `(d,o,a),(d,o,b),(c,o,d)` are tight. The exhaustive branches are:

| branch | successive forced triples | contradiction |
| --- | --- | --- |
| `odb, adc` | `codba=>abd; acodb=>oca; ocabd=>bac; dobac=>abo; abocd=>dco; badco=>dab; daboc=>oba` | `oba` and `abo` |
| `odb, cda` | `cdaob=>oad; acodb=>oca; bocad=>dac; dboca=>obd; obdac=>adb; coadb=>dao` | `oad` and `dao` |
| `bdo, bdc` | `bdcoa=>ocd; abocd=>oba; aobdc=>dbo; dboca=>aco; adboc=>bda; bdaco=>cad; cadob=>oda; codab=>bad; bocda=>adc; obadc=>abo` | `oba` and `abo` |
| `bdo, cdb` | `bdoac=>cao; dcaob=>acd; acdbo=>obd; caobd=>oac` | `oac` and `cao` |

The symmetry already described handles `|S(d)|=2,3`. Thus a shortest comparison cycle is not a star triangle.

**Ordinary triangle.** Normalize the comparison triangle as

`oa -> ab -> bo -> oa`,

so `(o,a,b),(a,b,o),(b,o,a)` are tight, and let `c,d` be the other vertices. For `w∈{c,d}` define

`o in M(w)` iff `(b,w,a)` is tight,

`a in M(w)` iff `(o,w,b)` is tight,

`b in M(w)` iff `(a,w,o)` is tight.

If `M(c)` and `M(d)` shared a coordinate, that coordinate, together with `c,d`, would be the three middle vertices of three tight triples with the same first and third vertices; Lemma 2.2 would give a Hamilton five-path. Hence `M(c)` and `M(d)` are disjoint.

Up to cyclic permutation of `o,a,b` and exchange of `c,d`, the disjoint pair is one of

`(∅,∅)`, `(∅,{o})`, `(∅,{o,a})`, `(∅,{o,a,b})`, `({o},{a})`, `({o},{a,b})`.

The match-set definition fixes all exterior-core triples used in the following exhaustive table:

| `M(c),M(d)` | extra branch | successive forced triples | contradiction |
| --- | --- | --- | --- |
| `∅,∅` | none | `bcoda=>doc; bdoca=>aco` | `oca` and `aco` |
| `∅,{o}` | none | `bcoda=>doc; bdoca=>aco` | `oca` and `aco` |
| `∅,{o,a}` | none | `bcoda=>doc; docab=>bac; odbac=>abd; odacb=>cad; bocad=>cob; cobda=>dbo; cdboa=>bdc; oabdc=>bao` | `oab` and `bao` |
| `∅,{o,a,b}` | `abc` | `abcod=>doc; badoc=>dab; dabco=>ocb` | `ocb` and `bco` |
| `∅,{o,a,b}` | `cba` | `cbado=>dab; cdabo=>adc; boadc=>dao; cbdao=>dbc; dbcoa=>aoc; bdaoc=>oad` | `oad` and `dao` |
| `({o},{a})` | `ocd` | `bcoda=>doc; docab=>bac; odbac=>abd; oabdc=>cdb; aocdb=>coa; coabd=>bao` | `oab` and `bao` |
| `({o},{a})` | `dco` | `ocadb=>dac; bodac=>dob; dobca=>cbo; dcboa=>bcd; cboad=>dao; bcdao=>adc; badco=>dab; daboc=>cob; adcob=>cda; bcdao=>oad` | `oad` and `dao` |
| `({o},{a,b})` | `cod` | `codba=>abd; abcod=>cba; cbado=>dab; daboc=>cob; cdabo=>adc; adcob=>ocd; oabdc=>cdb; aocdb=>coa; coabd=>bao` | `oab` and `bao` |
| `({o},{a,b})` | `doc` | `docab=>bac; odbac=>abd; badoc=>dab; daboc=>cob; cdabo=>adc; adcob=>ocd; oabdc=>cdb; aocdb=>coa; coabd=>bao` | `oab` and `bao` |

The extra branches in the table are reversal pairs, so the table is exhaustive. Thus no shortest directed comparison cycle exists. Hence `Gamma(G)` is acyclic, and Lemma 2.1 gives the required edge order. ∎

### Lemma 2.4. Two non-Hamiltonian edge-ordered four-sets

Let `K` be an edge-ordered complete graph, let `T={u_0,u_1,u_2}`, and let `x,y` be distinct vertices outside `T`. If neither `K[T∪{x}]` nor `K[T∪{y}]` has an increasing Hamilton path, then `K[T∪{x,y}]` has an increasing Hamilton path.

**Proof.** First classify a non-Hamiltonian edge-ordered `K_4`. Let its six ordinary edges be

`e_1<e_2<...<e_6`.

If `e_1,e_2` met, say `e_1=ab` and `e_2=bc`, then for the fourth vertex `d` the edge `cd` occurs after `e_2`, so `a,b,c,d` is an increasing Hamilton path. Thus `e_1,e_2` are disjoint. Dually `e_5,e_6` are disjoint. Hence the pairs `{e_1,e_2}`, `{e_3,e_4}`, `{e_5,e_6}` are the three opposite perfect matchings of `K_4`, ordered in three strict blocks.

Relabel `T` so

`u_1u_2 < u_0u_2 < u_0u_1`.

For `r∈{x,y}`, the matching-block classification in `T∪{r}` forces

`ru_0 < ru_1 < ru_2`.

If `xu_1<yu_1`, then

`u_0,x,u_1,y,u_2`

is increasing. If `yu_1<xu_1`, then

`u_0,y,u_1,x,u_2`

is increasing. ∎

### Lemma 2.5. Extending a fixed three-vertex path

Let `P` be a tight path of `H` on three vertices and let `x,y,z` be distinct vertices of `V(H)-V(P)`. At least one of

`V(P)∪{x,y}`, `V(P)∪{x,z}`, `V(P)∪{y,z}`

has a Hamilton tight path.

**Proof.** Write `P` on vertices `{a,b,c}`. Assume, for contradiction, that all three five-sets obtained by adding two of `x,y,z` are non-Hamiltonian. By Lemma 2.3 each is represented by an edge order. Their restrictions to the common triangle `{a,b,c}` realize the same comparison orientation, so after relabelling the three vertices we may assume

`ab<ac<bc`.

Thus `(b,a,c)`, `(a,b,c)`, `(a,c,b)` are tight.

For an exterior vertex `w`, define

`a in M(w)` iff `(b,w,c)` is tight,

`b in M(w)` iff `(a,w,c)` is tight,

`c in M(w)` iff `(a,w,b)` is tight.

In an edge order on a five-set containing `{a,b,c,w}`, the relative order of `wa,wb,wc` gives exactly the following six possibilities:

| order of `wa,wb,wc` | `M(w)` |
| --- | --- |
| `wa<wb<wc` | `{a,b,c}` |
| `wa<wc<wb` | `{b,c}` |
| `wb<wa<wc` | `{a,b}` |
| `wb<wc<wa` | `{a}` |
| `wc<wa<wb` | `{c}` |
| `wc<wb<wa` | `∅` |

If two exterior vertices `u,v` shared a coordinate of their match sets, Lemma 2.2 would apply. Indeed, a shared coordinate `a` gives the triples `(b,a,c),(b,u,c),(b,v,c)`; a shared coordinate `b` gives `(a,b,c),(a,u,c),(a,v,c)`; and a shared coordinate `c` gives `(a,c,b),(a,u,b),(a,v,b)`. In every case `P∪{u,v}` would have a Hamilton five-path, a contradiction. Hence `M(x),M(y),M(z)` are pairwise disjoint.

Two match sets cannot both be `∅`. If `M(u)=M(v)=∅`, then in the edge order on `P∪{u,v}`,

`uc<ub<ua`, `vc<vb<va`.

If `ub<vb`, the word `c,u,b,v,a` is increasing; if `vb<ub`, the word `c,v,b,u,a` is increasing. Either contradicts non-Hamiltonicity.

Therefore exactly one match set is `∅`. The other two are disjoint nonempty members of

`{a}`, `{c}`, `{a,b}`, `{b,c}`, `{a,b,c}`.

Three nonempty pairwise disjoint signatures would have to be `{a},{b},{c}`, but `{b}` is not in the list. After naming the `∅`-signature vertex `x` and ordering `y,z`, only the following three cases remain:

`I. M(x)=∅, M(y)={a}, M(z)={c};`

`II. M(x)=∅, M(y)={a}, M(z)={b,c};`

`III. M(x)=∅, M(y)={a,b}, M(z)={c}.`

Assume throughout that the relevant five-set is non-Hamiltonian. We again use the forcing rule from Lemma 2.3: if a five-vertex word has two known tight triples, the reverse of its third triple is forced. The initial exterior-core triples are

`I: cxb,cxa,bxa; byc,cya,bya; czb,cza,azb.`

`II: cxb,cxa,bxa; byc,cya,bya; czb,azc,azb.`

`III: cxb,cxa,bxa; byc,ayc,bya; czb,cza,azb.`

The following table completes the three cases:

| case | successive forced triples | contradiction |
| --- | --- | --- |
| I | `bycxa=>xcy; xcyab=>bay; cxbay=>abx; czbxa=>xbz; acxbz=>xca; xcazb=>zac; yzacb=>azy; cxbya=>ybx; ybxac=>cax; bycax=>acy; bacyz=>zyc; bazyc=>zab; czabx=>xba` | `abx` and `xba` |
| II | `cxbya=>ybx; ybxac=>cax; bycax=>acy; bacyz=>zyc; czbxa=>xbz; acxbz=>xca; xcazb=>zac; zacbx=>xbc; xbcya=>ycb; azycb=>yza; yzacb=>bca` | `acb` and `bca` |
| III | `cxbya=>ybx; ybxac=>cax; bycax=>acy; xbacy=>abx; czbxa=>xbz; acxbz=>xca; xcazb=>zac; yzacb=>azy; bacyz=>zyc; bazyc=>zab; czabx=>xba` | `abx` and `xba` |

Each case violates boundary antisymmetry. ∎

### Corollary 2.6. Four Hamiltonian five-subsets of every six-set

For every six-element set `E⊆V(H)`, at least four of the five-element subsets of `E` induce Hamiltonian boundary tournaments.

**Proof.** Let `E` be a six-set and let

`M={e in E : H[E-{e}] has a Hamilton path}`.

Choose any three-set `T⊆E`. The complementary three-set `P=E-T` can be ordered as a tight path: choose any middle vertex, and boundary antisymmetry chooses one of the two orders of the other two vertices. Lemma 2.5 applied to this path and the three vertices of `T` shows that `M∩T` is nonempty. If `|E-M|>=3`, choose `T⊆E-M` of order three, a contradiction. Thus `|M|>=4`. ∎

### Lemma 2.7. At most three non-Hamiltonian four-subsets

For every five-element set `S⊆V(H)`, at most three four-element subsets of `S` induce non-Hamiltonian boundary tournaments.

**Proof.** Let `S` be a five-set. If `H[S]` is Hamiltonian, choose a Hamilton order `(v_0,...,v_4)`. Deleting `v_0` or deleting `v_4` leaves a Hamilton tight four-vertex path, so at most three of the five four-subsets are non-Hamiltonian.

Suppose instead that `H[S]` is non-Hamiltonian. By Lemma 2.3 it is represented by an edge order. If two distinct four-subsets were both non-Hamiltonian, they would have the form `T∪{x}` and `T∪{y}` for their three-vertex intersection `T`. Their induced edge orders have no increasing Hamilton path, so Lemma 2.4 gives an increasing Hamilton path on all five vertices. By the representation, this is a tight Hamilton path of `H[S]`, a contradiction. Thus in the non-Hamiltonian case at most one four-subset is non-Hamiltonian. ∎

### Lemma 2.8. The Johnson cut bound

Let `Omega` be a ten-element set and let `F⊆binom(Omega,5)` contain no complementary pair. Put

`bar(F)={Omega-A : A in F}`.

In the Johnson graph `J(10,5)`, whose vertices are the five-subsets of `Omega` and whose adjacent vertices meet in four elements, let `e(F,bar(F))` denote the number of Johnson edges with one endpoint in `F` and one endpoint in `bar(F)`. Then

`e(F,bar(F)) <= 15|F|`.

**Proof.** For every four-set `C⊆Omega`, let

`K_C={C∪{v} : v in Omega-C}`.

This is a clique of order six in `J(10,5)`, and every Johnson edge belongs to exactly one such clique, namely the clique indexed by the intersection of its endpoints. Put

`r_C=|F∩K_C|`, `s_C=|bar(F)∩K_C|`.

Since `F` contains no complementary pair, `F` and `bar(F)` are disjoint. Hence `r_C+s_C<=6`, and therefore

`r_C s_C <= (r_C+s_C)^2/4 <= (3/2)(r_C+s_C)`.

Summing over all four-sets counts every edge from `F` to `bar(F)` exactly once. Each five-set contains exactly five four-subsets, so

`sum_C r_C=5|F|`, `sum_C s_C=5|bar(F)|=5|F|`.

Consequently

`e(F,bar(F)) <= (3/2)(10|F|)=15|F|`. ∎

### Theorem 2.9. Order of a smallest counterexample

`n>10`.

**Proof.** Every set of at most three vertices has a Hamilton tight path. Hence every boundary tournament of order at most six has a two-path cover. For orders seven and eight, choose any six vertices. Corollary 2.6 supplies a Hamilton path on five of them, and the complement has order at most three and is Hamiltonian. Thus `n>=9`.

Suppose `n=9`. Let `F_5` be the Hamiltonian five-subsets and let `B_4` be the non-Hamiltonian four-subsets. Counting incidences between six-sets and Hamiltonian five-subsets gives

`4|F_5| >= 4 binom(9,6)`,

because every six-set contains at least four Hamiltonian five-subsets and every five-set lies in four six-sets. Hence `|F_5|>=84`.

Counting incidences between five-sets and members of `B_4`, Lemma 2.7 gives

`5|B_4| <= 3 binom(9,5)`,

so `|B_4|<=75`. The complement of every member of `F_5` belongs to `B_4`, since two complementary Hamilton paths would form a two-path cover of `H`. Hence `|B_4|>=|F_5|`, a contradiction.

Suppose `n=10`, and let `F` be the family of Hamiltonian five-subsets. It is nonempty by Corollary 2.6 and contains no complementary pair. Fix `A∈F`, put `E=V(H)-A`, and fix `a∈A`. For each `z∈E`, define

`B_z=(E-{z})∪{a}`.

At most one `B_z` is non-Hamiltonian. Indeed, if distinct `x,y in E` made both `B_x,B_y` non-Hamiltonian, order the three-set `E-{x,y}` as a tight path and apply Lemma 2.5 with outside vertices `x,y,a`. One of `E,B_x,B_y` would be Hamiltonian. But `E` is the complement of the Hamiltonian set `A`, so `E` is non-Hamiltonian, and `B_x,B_y` were assumed non-Hamiltonian, a contradiction.

Thus for each `a∈A`, at least four of the five sets `B_z` lie in `F`. As `a` ranges over `A`, these give twenty distinct members of `F`. Their complements

`(A-{a})∪{z}`

belong to `bar(F)` and are Johnson neighbors of `A`. Therefore every `A∈F` has at least twenty neighbors in `bar(F)`, so

`e(F,bar(F)) >= 20|F|`,

contradicting Lemma 2.8. Hence `n!=10`, and therefore `n>10`. ∎

## 3. Longest paths and endpoint transfers

Let `A|B|C` be a spanning three-path cover, let `A=(v_0,...,v_{ell-1})` be one component, and let `X` be another. An **endpoint transfer from `X` to `A`** removes one endpoint `x` of `X` and appends or prepends `x` to the ordered path `A`, provided the resulting sequence is a tight path. If `X=(x)` is a singleton, the donor component disappears, so a successful transfer gives a spanning two-path cover.

If `ell=1`, either order of the two distinct vertices `V(A)∪{x}` is a tight two-vertex path, so a transfer is always possible. If `ell>=2` and `X=(x_0,...,x_m)`, appending `x_0` to the right end of `A` is possible exactly when

`(v_{ell-2},v_{ell-1},x_0)`

is tight, and prepending `x_m` to the left end is possible exactly when

`(x_m,v_0,v_1)`

is tight. If `X` is nontrivial, deleting the transferred endpoint leaves the remaining order of `X` unchanged and tight.

### Proposition 3.1. Endpoint improvement

Start from a spanning three-path cover and choose a longest component `A`. Repeatedly transfer an endpoint of another component into `A` whenever possible. Every transfer that does not already produce a two-path cover increases `|A|` by one, and `A` remains a longest component. Hence the procedure ends either with a spanning two-path cover or with a spanning three-path cover in which no endpoint of either other component can be transferred into `A`.

For any integer `M`, the procedure may instead be stopped as soon as some component has order at least `M+1`.

**Proof.** A nonclosing transfer increases the recipient `A` by one vertex and decreases only the donor by one vertex. Since `A` was at least as long as the donor before the transfer, it remains at least as long afterward. Also `|A|<=n`, so at most `n-|A|` nonclosing transfers can occur. ∎


### Proposition 3.2. The ends of a terminal longest component

Let `A|B|C` be a spanning three-path cover. Suppose `A=(v_0,...,v_{ell-1})` has maximum order among the three components and no endpoint of `B` or `C` can be transferred into either end of `A`. Then `ell>=4`, at least one of `B,C` is nontrivial, and for every endpoint `x` of `B` or `C`,

`(x,v_{ell-1},v_{ell-2})`, `(v_1,v_0,x)`


are tight.

**Proof.** Since `n>10`, the longest of three spanning components has order at least `ceil(n/3)>=4`. If `B,C` were both singletons, their two vertices would themselves form a tight two-vertex path, and that path together with `A` would two-cover `H`.

Fix an endpoint `x` of `B` or `C`. If `(v_{ell-2},v_{ell-1},x)` were tight, `x` could be transferred to the right end of `A`. Therefore it is not tight, and boundary antisymmetry gives `(x,v_{ell-1},v_{ell-2})`. The left-end statement is identical. ∎

The ordered end pairs

`(v_{ell-1},v_{ell-2})`, `(v_1,v_0)`

are disjoint because `ell>=4`. These two triples give a specified left extension of the first pair and a specified right extension of the second pair for every endpoint `x` of `B` or `C`.

### Proposition 3.3. A globally longest component

A **globally longest tight path** of `H` is a tight path whose order is maximum among all tight paths of `H`. There is a spanning three-path cover `A|B|C` in which `A` is a globally longest tight path of `H`. Every such cover satisfies Proposition 3.2.

**Proof.** A globally longest tight path cannot be Hamiltonian, since `pc(H)=3`. Hence it is proper, and Lemma 1.1 completes it to a spanning three-path cover. No endpoint transfer into `A` is possible, because such a transfer would produce a longer tight path. Proposition 3.2 applies. ∎

## 4. A fixed pair: static restrictions and descendant chains

Fix distinct vertices `a,c`. Partition the remaining vertices as

`X={s in V(H)-{a,c} : (a,s,c) is tight}`,

`Y={s in V(H)-{a,c} : (c,s,a) is tight}`.

Boundary antisymmetry gives

`V(H)-{a,c}=X⊔Y`.

For `s∈X`, define

`L_s=(a,s)`, `R_s=(s,c)`.

For `s∈Y`, define

`L_s=(c,s)`, `R_s=(s,a)`.

If `P=(v_0,...,v_k)` and `w∉V(P)`, write `(w,P)` for `(w,v_0,...,v_k)` and `(P,w)` for `(v_0,...,v_k,w)`. A **left-extended path** is a pair `(w;P)` for which `(w,P)` is tight. A **right-extended path** is a pair `(P;w)` for which `(P,w)` is tight. The vertex `w` is the extension vertex. The protected end of a left-extended path is the first vertex of `P`; the protected end of a right-extended path is the last vertex of `P`.

Thus for `s∈X`, `L_s` is right-extended by `c` and `R_s` is left-extended by `a`; for `s∈Y`, `L_s` is right-extended by `a` and `R_s` is left-extended by `c`.

### Lemma 4.1. Restricting an extended path

Let `(w;P)` be a left-extended path, where

`P=(v_0,...,v_k)`.

Let `Q` be a tight path meeting `P` but not containing `v_0`, and let

`i=min{j : v_j∈V(Q)}`.

Then

`P'=(v_0,...,v_{i-1})`

is a nonempty tight path disjoint from `Q`, and `(w;P')` is left-extended by the same vertex `w`.

Dually, if `(P;w)` is right-extended and `Q` meets `P` but avoids `v_k`, then the suffix of `P` strictly after the last vertex of `P` lying in `Q` is nonempty, disjoint from `Q`, and right-extended by `w`.

**Proof.** Since `Q` avoids `v_0`, the first intersection index satisfies `i>=1`. The sequence `(w,v_0,...,v_{i-1})` is an initial segment of the tight path `(w,P)`, so it is tight. The definition of `i` gives disjointness from `Q`. The right-extension statement is the same argument read from the other end. ∎

### Theorem 4.2. Static fixed-pair restrictions

For every `s∈V(H)-{a,c}`, the following two applications of Lemma 4.1 hold.

| orientation of `s` | original extended path | intersecting path `Q` | surviving subpath `P'` | inherited extension |
| --- | --- | --- | --- | --- |
| `s∈X` | `L_s=(a,s)` with `(L_s,c)=(a,s,c)` tight | `(a)` | `(s)` | right by `c` |
| `s∈X` | `R_s=(s,c)` with `(a,R_s)=(a,s,c)` tight | `(c)` | `(s)` | left by `a` |
| `s∈Y` | `L_s=(c,s)` with `(L_s,a)=(c,s,a)` tight | `(c)` | `(s)` | right by `a` |
| `s∈Y` | `R_s=(s,a)` with `(c,R_s)=(c,s,a)` tight | `(a)` | `(s)` | left by `c` |

Each row is a static graph-theoretic fact. It includes the displayed original three-vertex tight extension; the surviving singleton alone is not a substitute for that orientation data.

**Proof.** Consider `s∈X`. The tight triple `(a,s,c)` says that `L_s=(a,s)` is right-extended by `c`. Apply the right-extension part of Lemma 4.1 with `Q=(a)`. The surviving suffix is `(s)`, with the same right extension by `c`.

The same tight triple says that `R_s=(s,c)` is left-extended by `a`. Apply the left-extension part of Lemma 4.1 with `Q=(c)`. The surviving prefix is `(s)`, with the same left extension by `a`.

For `s∈Y`, interchange `a,c`. ∎

### Lemma 4.3. End-interval inheritance

Let `P=(v_0,...,v_k)` be a tight path.

If `(w,P)` is tight and some but not all vertices of `P` are deleted, let

`I=(v_i,...,v_j)`

be the first nonempty interval that remains in the order of `P`. Then `I` is left-extended by `w` when `i=0`, and by the deleted predecessor `v_{i-1}` when `i>0`.

Dually, if `(P,w)` is tight and `J=(v_i,...,v_j)` is the last nonempty interval that remains, then `J` is right-extended by `w` when `j=k`, and by the deleted successor `v_{j+1}` when `j<k`.

**Proof.** If `i=0`, `(w,I)` is an initial segment of `(w,P)`. If `i>0`, `(v_{i-1},I)` is a contiguous subpath of `P`. The right-extension statement is the reverse argument. ∎

### Oppositely extended pairs and descendant chains

An **oppositely extended pair** is an ordered pair `(P,Q)` of vertex-disjoint nonempty tight paths together with vertices `alpha∉V(P)` and `beta∉V(Q)` such that

`(alpha,P)` and `(Q,beta)`

are tight. Thus the first path is left-extended and the second is right-extended. The paths, extension sides, and extension vertices are all part of the data. Reversing both path orders gives the equivalent dual orientation.

We use three kinds of descendant step between oppositely extended pairs.

An **endpoint-restriction step** starts from an oppositely extended pair `(D,T)` whose first path `D=(d_0,d_1)` has order two. One prescribed endpoint `x∈{d_0,d_1}` survives and the other is deleted. Lemma 4.3 supplies the left extension of `(x)`: the old extension vertex when `x=d_0`, and the deleted neighbor `d_0` when `x=d_1`. The second path `T` is unchanged. The step records the old pair, the prescribed endpoint, the deleted endpoint, and the resulting extension vertex.

A **support-shortening step** starts from an oppositely extended pair `((p),T)` with

`T=(t_0,...,t_m)`

nontrivial and right-extended. It also contains a tight three-vertex path `C`, disjoint from `(p)`, whose intersection with `T` is either `{t_0}` or `{t_0,t_1}`. The step removes exactly that initial segment of `T`. The remaining nonempty suffix `T'` is right-extended by the same extension vertex as `T`, so `((p),T')` is the next oppositely extended pair. The left/right dual is defined by reversing both members.

A **singleton-replacement step** starts from an oppositely extended singleton pair `((p),(t))`. It contains an exact two-path cover

`H-{p,t}=U|V`,

a prescribed vertex `y∈V(U)`, a neighbor `d` of `y` along `U`, and the orientation selected by boundary antisymmetry on `{d,y,t}`. If `(d,y,t)` is tight, put `S=(d,y)` and use `t` as its right-extension vertex. If `(t,y,d)` is tight, put `S=(t,y)` and use `d` as its right-extension vertex. In either case `(p)` is kept as the first path and may use `t` as a left-extension vertex. Thus the step produces the next oppositely extended pair `((p),S)`. The preceding pair remains an earlier member of the descendant chain, with its extension witnesses unchanged; the new pair need not use the same witness on `(p)`.

A **descendant chain** is a finite sequence of oppositely extended pairs

`Pi_0,Pi_1,...,Pi_m`

such that every consecutive pair is joined by an endpoint-restriction step, a support-shortening step, or a singleton-replacement step. The descendant chain includes every transition datum and every earlier oppositely extended pair. Thus a later pair is a literal descendant of the earlier pair through specified path restrictions or a specified replacement; it is not an independently reconstructed pair.

For the fixed pair `a,c`, all paths `L_s,R_s` are named when the descendant chain is begun. If `Pi_i` contains a singleton path that meets one of these named extended paths away from its protected end, a **source restriction at index `i`** is the exact application of Lemma 4.1 to that named path and singleton. It records the named source path, the singleton member of `Pi_i`, the surviving singleton subpath, and its inherited extension vertex and side. This gives a strict descendant relation from the named source path to the surviving singleton, even though that singleton need not be a member of `Pi_i`. Source restrictions are attached data of the descendant chain and remain attached when the chain is extended.

### Lemma 4.4. Fixed-singleton descent

Let a descendant chain end at an oppositely extended pair `((p),T)`, where `(p)` is the left member and `T` is the right member. There is an extension of that same descendant chain ending either with a spanning two-path cover of `H` or with an oppositely extended pair of two singleton paths `((p),(q))`. The path `(p)` is unchanged throughout the extension. Every nonclosing transition after the initial stage is a support-shortening step and strictly shortens the second member.

**Proof.** Write

`T=(t_0,...,t_m)`.

If `m=0`, there is nothing to prove. Assume `m>=1` and put

`O=V(H)-({p}∪V(T))`.

If `O=∅`, then `(p)|T` is a spanning two-path cover.

Suppose `|O|>=2`. The proper induced tournament `H[O]` has a path cover with at most two components. If `|O|>=3`, one component is nontrivial; choose consecutive vertices `u_0,u_1` on it. If `|O|=2`, use the two vertices in either order. Boundary antisymmetry makes exactly one of

`(t_0,u_0,u_1)`, `(u_1,u_0,t_0)`

tight. Let `C` be that tight three-vertex path. It is disjoint from `(p)` and meets `T` exactly in `t_0`. Hence it gives a support-shortening step from `((p),T)` to

`((p),(t_1,...,t_m))`.

Now suppose `O={u}`. Since `n>10`, we have `|T|=n-2>=9`, so `t_2` exists. If `(p,u,t_0)` is not tight, then `(t_0,u,p)` is tight, and the two disjoint tight paths

`(t_0,u,p)`, `(t_1,...,t_m)`

span `H`, giving a two-path cover. Hence in the nonclosing case `(p,u,t_0)` is tight. The spanning word

`(p,u,t_0,t_1,...,t_m)`

cannot be a Hamilton tight path, so `(u,t_0,t_1)` is not tight. Therefore `(t_1,t_0,u)` is tight. This three-vertex path is disjoint from `(p)` and meets `T` exactly in `t_0,t_1`, giving a support-shortening step from `((p),T)` to

`((p),(t_2,...,t_m))`.

Every nonclosing step leaves `(p)` unchanged and strictly decreases the order of the second member. Repetition therefore reaches a singleton after finitely many steps. All transitions extend the same descendant chain. ∎

### Lemma 4.5. Endpoint selection within one descendant chain

Let a descendant chain end at an oppositely extended pair `(D,T)` whose first member `D` has order two. For either prescribed vertex `x∈V(D)`, there is an extension of that descendant chain ending either with a spanning two-path cover of `H` or with an oppositely extended singleton pair `((x),(q))` for some vertex `q`.

The descendant chain retains the incoming oppositely extended pair, the original extension of `D`, the chosen endpoint `x`, the endpoint-restriction step, and every later support-shortening step. The second singleton is not prescribed.

**Proof.** Write `D=(d_0,d_1)` and apply the endpoint-restriction step selecting `x`. This gives a descendant oppositely extended pair `((x),T)`; Lemma 4.3 supplies the left-extension vertex of `(x)` exactly as stated in the definition. Apply Lemma 4.4. ∎

The right-member version is the exact dual.

### Lemma 4.6. Prescribed singleton replacement within one descendant chain

Let a descendant chain end at an oppositely extended singleton pair `((p),(t))`, and let `y∉{p,t}`. There is an extension of that same descendant chain ending either with a spanning two-path cover of `H` or with the oppositely extended singleton pair `((p),(y))`.

The vertex `p` remains the first singleton throughout the extension. Every earlier pair and transition remains part of the descendant chain. The replacement records an exact pair-deletion cover, the selected adjacency through `y`, the oriented tight triple that creates the intermediate path, its extension vertex, an outside edge, and the final shortening to `(y)`.

**Proof.** By Lemma 1.2 choose an exact two-path cover

`H-{p,t}=U|V`

with both paths nontrivial. Relabel so `y∈V(U)`, and choose a neighbor `d` of `y` along `U`.

Exactly one of

`(d,y,t)`, `(t,y,d)`

is tight. In the first case put `S=(d,y)`; then `S` is right-extended by `t`. In the second case put `S=(t,y)`; then `S` is right-extended by `d`. The singleton `(p)` is left-extended by `t` because `(t,p)` is a tight two-vertex path. Hence these data form a singleton-replacement step from `((p),(t))` to `((p),S)`.

Write `S=(r,y)`. The path `V` is disjoint from `{p}∪V(S)` and is nontrivial. Choose consecutive vertices `v_0,v_1` on `V`. Exactly one of

`(r,v_0,v_1)`, `(v_1,v_0,r)`

is tight. Let `C` be that tight path. It is disjoint from `(p)` and meets `S` exactly in `r`, so it gives a support-shortening step from `((p),S)` to `((p),(y))`.

Both transitions extend the incoming descendant chain, and `(p)` is the first member at every stage. ∎

The dual statement preserves the second singleton and replaces the first.

### Theorem 4.7. Simultaneous fixed-pair descendant reductions

For every fixed pair of distinct vertices `a,c`, either `H` has a spanning two-path cover or there is one descendant chain `Sigma` ending at the oppositely extended singleton pair `((c),(a))` such that, for every

`s∈V(H)-{a,c}`,

both fixed-pair source restrictions from Theorem 4.2 occur as source restrictions along `Sigma`.

Equivalently, every vertex outside `{a,c}` has both descendant source reductions in one descendant chain; there is no exceptional vertex.

**Proof.** Since `|X|+|Y|=n-2>=9`, one of `X,Y` contains two distinct vertices. Interchange `a,c` if necessary and choose distinct `s,t∈X`.

The paths

`R_t=(t,c)`, `L_s=(a,s)`

are vertex-disjoint. The first is left-extended by `a`, and the second is right-extended by `c`, so they form an oppositely extended pair. Take this pair as `Pi_0`, and name every source path `L_v,R_v` at the root.

Apply Lemma 4.5 to the first member `R_t`, prescribing the endpoint `c`. Unless a spanning two-path cover occurs, the descendant chain reaches an oppositely extended singleton pair `((c),(q))` for some `q`. If `q=a`, keep this pair. Otherwise apply Lemma 4.6, preserving `(c)` and prescribing `a`. The same descendant chain then reaches `((c),(a))`.

Fix any `v∈V(H)-{a,c}`. If `v∈X`, use the singleton `(a)` at the terminal stage to apply Lemma 4.1 to the named right-extended path `L_v=(a,v)`, producing `(v)` right-extended by `c`; use the singleton `(c)` to apply Lemma 4.1 to the named left-extended path `R_v=(v,c)`, producing `(v)` left-extended by `a`. These are the two source restrictions at `v`.

If `v∈Y`, interchange `a,c` in the preceding sentence. The oppositely extended pair remains `((c),(a))`, so these source restrictions for different vertices are all attached at the same terminal pair. Thus every outside vertex has both descendant source reductions in the one descendant chain `Sigma`. ∎

### Proposition 4.8. Static contact away from the fixed pair

Let `s∈X` and `u∉{a,s,c}`.

1. If `Q=(s,u)`, exactly one of `(a,s,u)` and `(u,s,a)` is tight. If `(a,s,u)` is tight, it is a tight path properly containing both `L_s=(a,s)` and `Q`; if `(u,s,a)` is tight, that triple traverses the ordinary edges of `Q` and `L_s` in the opposite order.
2. If `Q=(u,s)`, exactly one of `(u,s,c)` and `(c,s,u)` is tight. If `(u,s,c)` is tight, it is a tight path properly containing both `Q` and `R_s=(s,c)`; if `(c,s,u)` is tight, that triple traverses the ordinary edges of `R_s` and `Q` in the opposite order.

The same statements hold for `s∈Y` after interchanging `a,c`.

**Proof.** Each item is one reversal pair, so boundary antisymmetry proves the assertion. ∎

### Theorem 4.9. Localization of later recurrence

Let `Sigma` be a nonclosing descendant chain from Theorem 4.7, and extend it by further certified descendant transitions. Let `s∈V(H)-{a,c}`. Suppose a later oppositely extended pair has a two-vertex member

`Q=(s,u)` or `Q=(u,s)`

with `u∉{a,s,c}`. Then the named source paths through `s` and the path `Q` give at least one of the following:

1. a tight path properly containing `Q` and one named source path through `s`;
2. a vertex-simple proper tight cycle;
3. an explicit tight triple containing `u` that traverses an ordered edge of `Q` and an ordered edge of a named source path in the opposite order.

Proposition 4.8 already gives outcome 1 or outcome 3 in this two-vertex case. The descendant source restrictions are not needed to prove the new-endpoint conclusion. Their role is different: Theorem 4.7 places, inside this same descendant chain, two strict descendant relations from the old source paths through `s` to the singleton `(s)`. Therefore a later member of an oppositely extended pair with vertex set `{a,s}` or `{s,c}` is an exact return to an earlier source support after the strict descendant `(s)` of that source path has already occurred in the same descendant chain.

Thus the only two-vertex supports through `s` not covered by the new-endpoint conclusion are

`{a,s}`, `{s,c}`.

The theorem does not assert that either exact return is impossible. Those two supports are precisely the unresolved recurrence residue.

**Proof.** The two source restrictions at `s` are attached to `Sigma` by Theorem 4.7 and remain part of every extension of that descendant chain. Apply Proposition 4.8 to `Q`; this gives outcome 1 or 3. The statement about exact return follows from the two strict source restrictions recorded at the terminal singleton pair of Theorem 4.7. ∎

### Lemma 4.10. Four vertices of one orientation

Let `S` be a four-element subset of `V(H)-{a,c}` such that `(a,s,c)` is tight for every `s∈S`. Then there are distinct `x,y,z∈S` such that

`(x,a,y,c,z)`

is a tight path.

**Proof.** Define tournaments on `S` by

`x->_a y` iff `(x,a,y)` is tight,

`x->_c y` iff `(x,c,y)` is tight.

Suppose no distinct `x,y,z` satisfy `x->_a y->_c z`. If a vertex has indegree at least two in `->_a`, then it has outdegree zero in `->_c`; otherwise two of its `->_a` predecessors together with one `->_c` successor would give such a mixed chain.

The sum of indegrees in the four-vertex tournament `->_a` is six, so some vertex `y` has indegree at least two. Hence `y` has outdegree zero in `->_c`, so `y` is the unique `->_c` sink. Every other vertex has positive `->_c` outdegree and therefore `->_a` indegree at most one. The indegree sum then forces `y` to have `->_a` indegree three and each other vertex to have `->_a` indegree one. Thus `y` is also the `->_a` sink.

Choose `v!=y`. Since `y` is the `->_c` sink, `v->_c y`. The unique `->_a` predecessor `x` of `v` cannot be `y`, because `y` is the `->_a` sink. Hence `x->_a v->_c y`, a mixed chain on three distinct vertices, contradiction. Therefore such a mixed chain exists. Renaming its middle and last vertices as `y,z`, the triples `(x,a,y)`, `(a,y,c)`, `(y,c,z)` are tight, so `(x,a,y,c,z)` is tight. ∎

### Corollary 4.11. A five-vertex path through descendant-reduced vertices

Let `Sigma` be a nonclosing descendant chain from Theorem 4.7. Then there are distinct vertices `x,y,z`, each having both descendant source reductions in `Sigma`, such that either

`(x,a,y,c,z)`

or

`(x,c,y,a,z)`

is a tight path.

**Proof.** One of `X,Y` has order at least five. Choose any four vertices from that class and apply Lemma 4.10, interchanging `a,c` if necessary. Theorem 4.7 supplies both descendant source reductions for every outside vertex, in particular for the resulting `x,y,z`. ∎


## 5. Deletion and comparison of path covers

If `F` is an ordinary graph and `S⊆V(F)`, write `F-S` for the induced subgraph on `V(F)-S`, `deg_F(v)` for the ordinary degree of `v`, `e_F(S)` for the number of ordinary edges of `F` with both endpoints in `S`, and `comp(F)` for the number of connected components of `F`, counting isolated vertices.

### Lemma 5.1. Counting components after deletion

Let `F` be an ordinary path forest with `k` components and let `S⊆V(F)`. Then

`comp(F-S)=k+sum_{v in S}(deg_F(v)-1)-e_F(S)`.


If `F` is the ordinary path forest of a tight-path cover, every nonempty component of `F-S` inherits from its original path a tight vertex order.

**Proof.** Let `N=|V(F)|`. Since `F` is a path forest with `k` components, it has `N-k` edges. Deleting `S` removes

`sum_{v in S} deg_F(v)-e_F(S)`

edges: the degree sum counts an edge internal to `S` twice, so one copy must be subtracted. The remaining graph has

`N-|S|`

vertices and

`N-k-sum_{v in S}deg_F(v)+e_F(S)`

edges. A forest has number of components equal to vertices minus edges, which gives the displayed formula. Tightness of inherited path orders follows because every surviving component is a contiguous subpath of an original tight path. ∎

### Proposition 5.2. One internal deletion produces a crossing

Fix distinct vertices `a,c`, let `U|V` be an exact two-path cover of `H-{a,c}`, and let `s` be internal in one of `U,V`. Let `T` be any exact two-path cover of `H-{a,c,s}`; such a cover exists.

Deleting `s` from `U|V` leaves three nonempty ordered paths. Some ordinary edge `xy` of `T` has its endpoints in two different paths among those three. Moreover the edge may be named so that there is a vertex `h∉{x,y}` for which `{h,x}` is an ordinary edge of the original cover `U|V`. Boundary antisymmetry then gives exactly one tight triple from the reversal pair

`(h,x,y)`, `(y,x,h)`.


If the path containing `x` after deletion of `s` is nontrivial, `h` may be chosen in that path. If both paths crossed by `xy` are singletons, one may take `h=s`.

**Proof.** The three-set `{a,s,c}` has a Hamilton tight path, so Lemma 1.1 gives `pc(H-{a,c,s})=2`; hence an exact cover `T` exists.

Deleting the internal vertex `s` splits one of `U,V` into two nonempty subpaths and leaves the other path unchanged. Thus three nonempty path vertex sets remain. If every ordinary edge of both components of `T` had both endpoints inside one of these three sets, then each connected component of the ordinary path forest of `T` would lie inside one of the three sets. Two connected components could not cover all three nonempty sets. Therefore an ordinary edge `xy` of `T` crosses two of the three sets.

If one crossed set contains at least two vertices, name the endpoint in that set `x` and choose `h` adjacent to `x` along its inherited subpath. Then `{h,x}` is an ordinary edge of `U|V`, and `h` is distinct from `x,y`.

Otherwise both crossed sets are singleton subpaths. The unchanged component of `U|V` is nontrivial by Lemma 1.2, so the two singleton subpaths are the two pieces created by deleting the internal vertex `s`. Each singleton vertex was adjacent to `s` in the original path. Name either one `x` and take `h=s`. Boundary antisymmetry gives the displayed reversal pair. ∎

Thus Proposition 5.2 produces an explicit tight three-vertex path on `{h,x,y}` together with the exact ordinary edges from the two compared covers that determine it.

### Proposition 5.3. Three internal vertices of one orientation

Fix distinct vertices `a,c` and an exact two-path cover `U|V` of `H-{a,c}`. At least five vertices are internal in `U|V`. Consequently there are three internal vertices `p,q,r` for which either

`(a,p,c)`, `(a,q,c)`, `(a,r,c)`

are all tight, or

`(c,p,a)`, `(c,q,a)`, `(c,r,a)`

are all tight.

**Proof.** By Lemma 1.2 both paths are nontrivial, so together they have exactly four endpoints. Since `n-2>=9`, at least `n-6>=5` vertices are internal. The partition `V(H)-{a,c}=X⊔Y` from Section 4 partitions these internal vertices into two classes. One class contains at least three of them. ∎

After interchanging `a,c` if necessary, we shall write the selected vertices so that

`(a,p,c)`, `(a,q,c)`, `(a,r,c)`


are tight.

### Proposition 5.4. The eight induced subgraphs

Assume the first orientation alternative of Proposition 5.3, so `(a,p,c)`, `(a,q,c)`, `(a,r,c)` are tight, and put

`P={p,q,r}`, `K={a,c,p,q,r}`, `W=V(H)-K`.

For every `J⊆P`, define

`G_J=H[W∪J]`.

Then `H[K-J]` has a Hamilton tight path and

`pc(G_J)=2`.

Consequently every exact two-path cover of `G_J`, together with any Hamilton tight path on `K-J`, is a spanning three-path cover of `H`.

**Proof.** If `J=∅`, Lemma 2.2 applied to the three common-endpoint triples `(a,p,c)`, `(a,q,c)`, `(a,r,c)` gives a Hamilton path on `K`.

If `|P-J|=2`, write `P-J={s,t}`. Exactly one of `(s,c,t)` and `(t,c,s)` is tight, so either `(a,s,c,t)` or `(a,t,c,s)` is a Hamilton path on `K-J`. If `|P-J|=1`, say `P-J={s}`, the path `(a,s,c)` is Hamilton on `K-J`. If `P-J=∅`, `(a,c)` is Hamilton on `K-J`.

Thus `H[K-J]` is Hamiltonian for every `J`. Since `W` has order `n-5>=6`, every `G_J` is a proper nonempty induced subgraph of `H`, so minimality gives `pc(G_J)<=2`. If `G_J` were Hamiltonian, a Hamilton path in `G_J` together with the Hamilton path on `K-J` would two-cover `H`. Therefore `pc(G_J)=2`. The final assertion is immediate from the disjoint partition

`V(H)=(W∪J)⊔(K-J)`. ∎

For each `s in P`, Proposition 5.2 compares the original exact cover of `G_P=H-{a,c}` with any exact cover of `G_{P-{s}}` and produces an explicit crossing triple. The order-sensitive path-intersection statements needed for other comparisons are collected in Appendix A.

## 6. A lexicographically maximal three-path cover

For a spanning three-path cover `F`, let

`lambda(F)=(ell_1,ell_2,ell_3)`, `ell_1>=ell_2>=ell_3`,

be its three component orders in decreasing order. For two such triples, the **lexicographic order** compares the first coordinate at which they differ. Since each `ell_i` is a positive integer and `ell_1+ell_2+ell_3=n`, only finitely many such triples occur. Choose a spanning three-path cover

`F=A|B|C`

for which `lambda(F)` is lexicographically maximal, and order the component names so that

`|A|>=|B|>=|C|`.

### Proposition 6.1. Properties of the extremal cover

For the lexicographically maximal cover `A|B|C`:

1. `A` is a globally longest tight path of `H`;
2. no endpoint can be transferred from one component into another component whose order is at least as large as the donor's order;
3. `|B|>=3`.

**Proof.** Let `Q` be any globally longest tight path of `H`. It is proper because `pc(H)=3`, so Lemma 1.1 completes it to a spanning three-path cover. Hence the first coordinate of the lexicographically maximal `lambda(F)` is at least `|Q|`; by definition it cannot exceed `|Q|`. Thus `|A|=|Q|` and `A` is globally longest.

Suppose an endpoint can be transferred from a donor `D` to a recipient `R` with `|R|>=|D|`. If `D` is a singleton, the transfer produces a spanning two-path cover, impossible. Otherwise the transfer changes the multiset of component orders by replacing `|R|,|D|` with `|R|+1,|D|-1`. Because `|R|>=|D|`, sorting the three orders gives a lexicographically larger triple, contradicting maximality. This proves the second assertion.

To prove the third, suppose `|B|<=2`. If `|C|=1`, then `|B∪C|<=3`; that induced subgraph has a Hamilton tight path, which together with `A` gives a spanning two-path cover. Therefore the only remaining possibility is `|B|=|C|=2`. Write

`B=(b_0,b_1)`, `C=(c_0,c_1)`.

The transfer of `c_0` to the right end of `B` is forbidden, so `(b_0,b_1,c_0)` is not tight and `(c_0,b_1,b_0)` is tight. The transfer of `c_1` to the left end of `B` is forbidden, so `(c_1,b_0,b_1)` is not tight and `(b_1,b_0,c_1)` is tight. Hence

`(c_0,b_1,b_0,c_1)`

is a tight path, and together with `A` it gives a spanning two-path cover, again impossible. Thus `|B|>=3`. ∎

### Proposition 6.2. Fixed-pair data and recurrence control at the ends of the longest component

Write

`A=(v_0,...,v_{ell-1})`.

Choose a nontrivial component

`X_0=(x_0,...,x_m)`

from `{B,C}`; such a component exists by Proposition 3.2. Put

`a=x_0`, `c=x_m`.

Then

`(a,v_{ell-1},v_{ell-2})`, `(v_1,v_0,c)`

are tight. Each of the four vertices

`v_{ell-1}`, `v_{ell-2}`, `v_1`, `v_0`

lies outside `{a,c}` and therefore has both static fixed-pair restrictions from Theorem 4.2.

For this same pair `a,c`, let `Sigma` be the descendant chain of Theorem 4.7. Since `H` is a counterexample, the spanning-two-path-cover outcome does not occur. Hence all four displayed end vertices have both descendant source reductions attached to `Sigma`. This descendant chain is auxiliary to the extremal cover `A|B|C`; none of its oppositely extended pairs is asserted to be a pair of components of that cover. What is shared with the extremal cover is the physical vertex pair `a,c` and the named source paths attached to that pair.

For each of the four end vertices `s`, Theorem 4.9 applies after any further certified descendant transitions: if a later oppositely extended pair has a two-vertex member through `s` whose other endpoint lies outside `{a,c}`, contact with the named source paths gives a larger tight path, a proper tight cycle, or an explicit reversed/crossing tight triple. The only unresolved two-vertex recurrence supports through `s` are `{a,s}` and `{s,c}`.

**Proof.** Proposition 6.1 makes the cover terminal for transfers into `A`. Proposition 3.2 applied to the endpoints `a,c` of `X_0` gives the two displayed tight triples. Since the three components of `A|B|C` are disjoint, the four displayed vertices of `A` lie outside `{a,c}`, so Theorem 4.2 applies to all four.

Apply Theorem 4.7 to the same pair `a,c`. In the nonclosing outcome, that theorem supplies both descendant source reductions for every vertex outside `{a,c}`, in particular for all four end vertices of `A`. The final assertion is Theorem 4.9. ∎

The roles of the two ingredients are now distinct. Lexicographic maximality supplies the global descent/equality framework: any literal spanning three-path cover with lexicographically larger component orders is impossible. The fixed-pair descendant chain supplies descendant control when a later descendant returns through a vertex that has already undergone both source reductions; Theorem 4.9 localizes the unresolved equality residue to exact return on one of the two old supports.

This does not yet complete the proof. The missing augmentation statement is:

> Let `F` be a spanning three-path cover of a smallest counterexample such that no endpoint can be transferred from one component into another component of at least equal order. Then either a spanning two-path cover exists or there is a spanning three-path cover `F'` with `lambda(F')` lexicographically larger than `lambda(F)`.

No result above yet constructs `F'` in all cases. The analysis of that missing step is recorded in `GN3/MIGRATION/EVIDENCE/AUGMENTATION_FRONTIER.md`.

## Appendix A. Intersections of ordered paths

For a tight path `P=(p_0,...,p_k)`, an **ordered edge of P** means one of the ordered pairs `(p_i,p_{i+1})`. A tight triple `(x,y,z)` **reverses an ordered edge of P** if `(z,y)` or `(y,x)` is an ordered edge of `P`; equivalently, one of its consecutive ordered pairs is the reverse of an ordered edge of `P`.

### Lemma A.1. Reversed order of common vertices

Let `P=(v_0,...,v_k)` and `Q` be tight paths. Suppose the common vertices of `P,Q` do not occur in the same relative order. Then at least one of the following exists:

1. an ordered edge of `Q` that is the reverse of an ordered edge of `P`;
2. a tight triple on `V(P)∪V(Q)` that reverses an ordered edge of one of the two paths at an intersection with the other;
3. a vertex-simple tight cycle on `V(P)∪V(Q)`.

In particular the lemma applies to two different Hamilton orders on the same vertex set.

**Proof.** Read the common vertices in their order along `Q`. Since the relative orders disagree, there are two consecutive common vertices along `Q`, say `v_i,v_j`, with `i>j`. Let `E` be the subpath of `Q` from `v_i` to `v_j`. By choice, the interior of `E` contains no vertex of `P`.

If `E` is the single ordinary edge from `v_i` to `v_j` and `i=j+1`, outcome 1 holds. Otherwise let `x` be the successor of `v_i` on `E` and `y` the predecessor of `v_j` on `E`. Since `i>j`, we have `i>=1` and `j<=k-1`, so the triples

`(v_{i-1},v_i,x)`, `(y,v_j,v_{j+1})`

are defined. If either is not tight, boundary antisymmetry gives its tight reverse, which gives outcome 2. If both are tight, traverse `E` from `v_i` to `v_j`, then traverse `P` from `v_j` to `v_{i-1}`, and close to `v_i`. The two displayed tight triples supply the joins. The interior of `E` is disjoint from `P`, so the resulting tight cycle is vertex-simple. ∎

### Lemma A.2. Contact at an extended end

Let `(w;P)` be a left-extended path with

`P=(v_0,...,v_k)`,

and let `Q` be a tight path containing `v_0`. Then either `P=Q=(v_0)` or at least one of the following exists:

1. a tight path properly containing `P` as an ordered subpath;
2. a tight path properly containing `Q` as an ordered subpath;
3. a vertex-simple tight cycle;
4. a tight triple that reverses an ordered edge of `P` or `Q`.

All vertices in the conclusion lie in `V(P)∪V(Q)∪{w}`. The corresponding statement for a right-extended path is obtained by reversing all path orders.

**Proof.** If `k=0`, either `Q=(v_0)` or `Q` properly contains `P`. Assume `k>=1`.

If the common vertices of `P,Q` occur in different relative orders, apply Lemma A.1. Outcomes 2 and 3 there already suffice. If outcome 1 there gives a reversed common edge, choose a consecutive tight triple of `(w,P)` containing that edge. Such a triple exists because `(w,P)` has order at least three. This gives outcome 4 here.

Now assume the common vertices occur in the same order. Since `Q` contains `v_0`, the vertex `v_0` is the first common vertex along `Q`.

If `Q` has a predecessor `u` immediately before `v_0`, test `(u,v_0,v_1)`. If it is tight, the initial segment of `Q` ending at `v_0` followed by `P` is a tight path properly containing `P`; the initial segment has no other vertex of `P`. If it is not tight, `(v_1,v_0,u)` is tight and gives outcome 4.

It remains that `Q` starts at `v_0`. If `Q=(v_0)`, then `(w,v_0)` properly contains `Q`. Otherwise write the next vertex of `Q` as `q_1`. If `w∉V(Q)`, test `(w,v_0,q_1)`. If it is tight, `(w,Q)` properly contains `Q`; otherwise `(q_1,v_0,w)` is tight and gives outcome 4.

Finally suppose `w∈V(Q)`. The paths `(w,P)` and `Q` contain the common vertices `w,v_0` in opposite orders. Apply Lemma A.1 to these two paths. Its tight-triple outcome gives outcome 4 here, its cycle outcome gives outcome 3, and its reversed-edge outcome can again be placed in a consecutive tight triple of `(w,P)`, giving outcome 4. ∎

Any tight cycle produced in Appendix A is proper in `H`: if it used every vertex of `H`, opening it would give a Hamilton tight path, contradicting `pc(H)=3`.