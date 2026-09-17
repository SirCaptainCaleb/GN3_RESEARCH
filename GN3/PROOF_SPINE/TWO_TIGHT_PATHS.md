# Two tight paths in a boundary tournament

## 1. Definitions and the minimal-counterexample reduction

Throughout, vertex sets are finite.

For an integer `r>=2` and a set `V`, let `V^{\underline r}` denote the set of ordered `r`-tuples of pairwise distinct vertices of `V`. An **r-uniform directed hypergraph**, or **r-digraph**, is a pair `G=(V,E)` with `E⊆V^{\underline r}`. The set `V` is the vertex set, written `V(G)`, and the members of `E` are the directed `r`-edges. In this document `r=3` unless explicitly stated otherwise.

For an ordered triple `(x,y,z)` of distinct vertices, its **reverse** is `(z,y,x)`. A **3-uniform boundary tournament**, hereafter simply a **boundary tournament**, is a 3-digraph `H=(V,E)` such that for every three distinct vertices `x,y,z`, exactly one of

`(x,y,z)`, `(z,y,x)`

belongs to `E`. An ordered triple is **tight** if it belongs to `E`. Thus boundary antisymmetry is the assertion that exactly one member of every reversal pair is tight.

For `S⊆V(H)`, write `H[S]` for the induced boundary tournament with vertex set `S`, and write `H-S` for `H[V(H)-S]`. For a vertex `v`, `H-v` abbreviates `H-{v}`.

A **tight path** is an ordered list

`P=(v_0,...,v_k)`

of distinct vertices such that `(v_{i-1},v_i,v_{i+1})` is tight for every `1<=i<=k-1`. Its vertex set is `V(P)={v_0,...,v_k}` and its order is `|P|=k+1`. Paths of order one or two satisfy the condition vacuously. The **ordinary edges** of `P` are the unordered pairs `{v_{i-1},v_i}`. The endpoints are `v_0,v_k`; when `k>=2`, the other vertices are internal. A path is **nontrivial** if it has order at least two.

A **path cover** of an induced boundary tournament `G` is a partition of `V(G)` into vertex sets of tight paths, together with one chosen tight ordering on each part. Write `pc(G)` for the minimum number of paths in such a cover. An **exact k-path cover** is a path cover with exactly `k` nonempty path components. We write `P|Q|R` for a path cover with the displayed components. The **ordinary path forest** of a path cover is the ordinary graph on the same vertex set whose edges are the ordinary edges of its path components. A tight path on all vertices of `G` is a **Hamilton path** of `G`, and `G` is **Hamiltonian** if it has such a path. A path is **proper in G** if its vertex set is a proper subset of `V(G)`.

A **tight cycle** is a cyclic ordering of at least three distinct vertices in which every cyclically consecutive ordered triple is tight. It is **proper in H** if its vertex set is a proper subset of `V(H)`. Opening a tight cycle at any one of its ordinary cycle edges gives a tight path on the same vertex set.

The conjecture is

> Every boundary tournament has path-cover number at most two.

Assume the conjecture is false. Choose a counterexample `H` with minimum order, and write

`n=|V(H)|`.

Every proper induced subgraph of `H` has path-cover number at most two. Unless another ambient boundary tournament is explicitly named, every path, cycle, and induced subgraph is taken in `H`. Choosing any vertex `v`, a two-path cover of `H-v` together with `(v)` gives a three-path cover of `H`; hence

`pc(H)=3`.

Also `n>=4`: a boundary tournament on at most three vertices is covered by at most two tight paths.

### Lemma 1.1. Complements of paths

Let `S` be a nonempty proper subset of `V(H)`. If `H[S]` has a Hamilton tight path, then

`pc(H-S)=2`.

Consequently every proper tight path of `H` extends, by adding a two-path cover of its complement, to a spanning three-path cover of `H`.

**Proof.** Minimality gives `pc(H-S)<=2`. If `H-S` were Hamiltonian, its Hamilton path together with a Hamilton path on `S` would be a spanning two-path cover of `H`, contradicting `pc(H)=3`. Therefore `pc(H-S)=2`.

More generally, let `P|Q` be any exact two-path cover of `H-S`. Neither `H[S∪V(P)]` nor `H[S∪V(Q)]` is Hamiltonian: a Hamilton path on either union, together with the untouched other component, would two-cover `H`. ∎

Every tight path of `H` has order at most `n-4`. Indeed, `H` has no Hamilton path, so every tight path `P` is proper. Minimality gives `pc(H-V(P))<=2`; if `H-V(P)` were Hamiltonian, its Hamilton path together with `P` would two-cover `H`. Thus `pc(H-V(P))=2`, while every boundary tournament on at most three vertices is Hamiltonian. Hence `|V(H)-V(P)|>=4`. Opening a tight cycle gives a tight path on the same vertex set, so every tight cycle also has order at most `n-4`.

### Lemma 1.2. Deleting one or two vertices

For every vertex `v`,

`pc(H-v)=2`,

and every exact two-path cover of `H-v` has both paths nontrivial. For distinct vertices `a,c`,

`pc(H-{a,c})=2`,

and every exact two-path cover of `H-{a,c}` has both paths nontrivial.

**Proof.** Apply Lemma 1.1 first to the singleton `(v)` and then to the two-vertex path `(a,c)`. If an exact two-path cover of `H-v` had singleton component `(s)`, then the two-vertex path `(v,s)` together with the other component would two-cover `H`. If an exact two-path cover of `H-{a,c}` had singleton component `(s)`, boundary antisymmetry makes exactly one of `(a,s,c)` and `(c,s,a)` tight; that tight three-vertex path together with the other component would two-cover `H`. ∎

A spanning three-path cover has `n-3` ordinary edges. No spanning forest whose components are tight paths can have more ordinary edges, because a path forest on `n` vertices with more than `n-3` edges has at most two components and would give a two-path cover.

## 2. Small-order lemmas

Let `K_V` denote the ordinary complete graph on a vertex set `V`. Its edge set consists of the two-element subsets of `V`. The **line graph** `L(K_V)` is the graph with vertex set `E(K_V)` in which two vertices are adjacent exactly when the corresponding ordinary edges meet.

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

Let `G` be a boundary tournament on exactly five vertices. If `G` has no Hamilton tight path, then `Gamma(G)` is acyclic. Equivalently, there is a strict total order `<` on `E(K_5)` such that, for all distinct `u,v,w`,

`(u,v,w) is tight  iff  {u,v}<{v,w}`.

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

Assume throughout that the relevant five-set is non-Hamiltonian. We use the same forcing rule: if a five-vertex word has two known tight triples, the reverse of its third triple is forced. The initial exterior-core triples are

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

### Lemma 2.7. Non-Hamiltonian four-subsets of a five-set

Let `S⊆V(H)` have order five. If `H[S]` is Hamiltonian, at most three four-element subsets of `S` are non-Hamiltonian. If `H[S]` is non-Hamiltonian, at most one four-element subset of `S` is non-Hamiltonian.

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

The complement of every member of `F_5` belongs to `B_4`, since two complementary Hamilton paths would form a two-path cover of `H`. Hence

`|B_4|>=|F_5|`.

Now count incidences between five-sets and members of `B_4`. Each member of `B_4` lies in five five-sets. By Lemma 2.7, a Hamiltonian five-set contains at most three members of `B_4`, whereas a non-Hamiltonian five-set contains at most one. Since there are `binom(9,5)=126` five-sets,

`5|B_4| <= 3|F_5| + (126-|F_5|) = 126+2|F_5|`.

Using `|B_4|>=|F_5|` gives

`5|F_5| <= 126+2|F_5|`,

so `|F_5|<=42`, contradicting `|F_5|>=84`.

Suppose `n=10`, and let `F` be the family of Hamiltonian five-subsets. It is nonempty by Corollary 2.6 and contains no complementary pair. Fix `A∈F`, put `E=V(H)-A`, and fix `a∈A`. For each `z∈E`, define

`B_z=(E-{z})∪{a}`.

At most one `B_z` is non-Hamiltonian. Indeed, if distinct `x,y in E` made both `B_x,B_y` non-Hamiltonian, order the three-set `E-{x,y}` as a tight path and apply Lemma 2.5 with outside vertices `x,y,a`. One of `E,B_x,B_y` would be Hamiltonian. But `E` is the complement of the Hamiltonian set `A`, so `E` is non-Hamiltonian, and `B_x,B_y` were assumed non-Hamiltonian, a contradiction.

Thus for each `a∈A`, at least four of the five sets `B_z` lie in `F`. As `a` ranges over `A`, these give twenty distinct members of `F`. Their complements

`(A-{a})∪{z}`

belong to `bar(F)` and are Johnson neighbors of `A`. Therefore every `A∈F` has at least twenty neighbors in `bar(F)`, so

`e(F,bar(F)) >= 20|F|`,

contradicting Lemma 2.8. Hence `n!=10`, and therefore `n>10`. ∎

## 3. Longest paths and endpoint transfers

Let `A|B|C` be a spanning three-path cover, let `A=(v_0,...,v_{ell-1})` be one component, and let `X` be another. An **endpoint transfer from `X` to `A`** is the operation of removing one endpoint `x` of `X` and appending or prepending `x` to the ordered path `A`, provided the resulting sequence is a tight path. If `X=(x)` is a singleton, the donor component disappears, so a successful transfer gives a spanning two-path cover.

If `ell=1`, either order of the two distinct vertices `V(A)∪{x}` is a tight two-vertex path, so a transfer is always possible. If `ell>=2` and `X=(x_0,...,x_m)`, appending `x_0` to the right end of `A` is possible exactly when

`(v_{ell-2},v_{ell-1},x_0)`

is tight, and prepending `x_m` to the left end is possible exactly when

`(x_m,v_0,v_1)`

is tight. If `X` is nontrivial, deleting the transferred endpoint leaves the remaining order of `X` unchanged and tight.

### Proposition 3.1. Endpoint improvement

Start from a spanning three-path cover and choose a longest component `A`. Repeatedly transfer an endpoint of another component into `A` whenever possible. Every transfer that does not already produce a two-path cover increases `|A|` by one, and `A` remains a longest component. Because every tight path has order at most `n-4`, after at most `n-4-|A|` transfers that do not produce a two-path cover the procedure ends with a spanning three-path cover in which no endpoint of either other component can be transferred into `A`.

For any integer `M`, the procedure may instead be stopped as soon as `A` has order at least `M+1`.

**Proof.** A transfer that does not produce a two-path cover increases the recipient `A` by one vertex and decreases only the donor by one vertex. Since `A` was at least as long as the donor before the transfer, it remains at least as long afterward. Every tight path has order at most `n-4`, so `|A|<=n-4` at every stage. Hence at most `n-4-|A|` such transfers can occur before no further transfer into `A` is possible. ∎


### Proposition 3.2. The ends of a longest component admitting no endpoint transfer

Let `A|B|C` be a spanning three-path cover. Suppose `A=(v_0,...,v_{ell-1})` has maximum order among the three components and no endpoint of `B` or `C` can be transferred into either end of `A`. Then

`ceil(n/3)<=ell<=n-4`,

so `|B|+|C|>=4`; in particular at least one of `B,C` is nontrivial. For every endpoint `x` of `B` or `C`,

`(x,v_{ell-1},v_{ell-2})`, `(v_1,v_0,x)`


are tight.

**Proof.** The longest of three spanning components has order at least `ceil(n/3)`, while the consequence of Lemma 1.1 gives `ell<=n-4`. Hence `|B|+|C|=n-ell>=4`, which in particular rules out both being singletons. Since `n>10`, `ell>=4`.

Fix an endpoint `x` of `B` or `C`. If `(v_{ell-2},v_{ell-1},x)` were tight, `x` could be transferred to the right end of `A`. Therefore it is not tight, and boundary antisymmetry gives `(x,v_{ell-1},v_{ell-2})`. If `(x,v_0,v_1)` were tight, `x` could be transferred to the left end of `A`. Therefore it is not tight, and boundary antisymmetry gives `(v_1,v_0,x)`. ∎

The ordered end pairs

`(v_{ell-1},v_{ell-2})`, `(v_1,v_0)`

are disjoint because `ell>=4`. These two triples give a specified left extension of the first pair and a specified right extension of the second pair for every endpoint `x` of `B` or `C`.

### Proposition 3.3. A globally longest component

A **globally longest tight path** of `H` is a tight path whose order is maximum among all tight paths of `H`. Let `A` be globally longest and put `L=|A|`. Then every exact two-path cover

`H-V(A)=B|C`

satisfies

`4<=|B|+|C|=n-L<=2L`.

Consequently

`ceil(n/3)<=L<=n-4`.

Moreover, `n=3L` if and only if some exact complementary two-cover has `|B|=|C|=L`; in that equality case every exact complementary two-cover has both components of order `L`. In particular there is a spanning three-path cover `A|B|C` with `A` globally longest. In every such cover, no endpoint of `B` or `C` can be transferred into either end of `A`; at least one of `B,C` is nontrivial; and every endpoint `x` of `B` or `C` satisfies

`(x,v_{L-1},v_{L-2})`, `(v_1,v_0,x)`

when `A=(v_0,...,v_{L-1})`.

**Proof.** The path `A` is proper because `H` has no Hamilton path. Lemma 1.1 gives `pc(H-V(A))=2`, so exact complementary two-covers exist. Every tight path leaves at least four vertices outside it, so `|V(H)-V(A)|>=4`. Since `A` is globally longest, each complementary path has order at most `L`, so

`|B|+|C|=n-L<=2L`.

This yields the displayed bounds on `L`. If `n=3L`, then every exact complementary two-cover has total order `2L`, while each component has order at most `L`; hence both have order exactly `L`. Conversely, one complementary cover with two components of order `L` gives `n=L+L+L=3L`.

Finally, any exact complementary two-cover gives a spanning three-path cover with component `A`. No endpoint transfer into `A` is possible, because that would create a tight path longer than `A`; hence Proposition 3.2 applies. ∎

## 4. A fixed pair: restrictions and continuation sequences

Fix distinct vertices `a,c`. Partition the remaining vertices as

`X={s in V(H)-{a,c} : (a,s,c) is tight}`,

`Y={s in V(H)-{a,c} : (c,s,a) is tight}`.

Boundary antisymmetry gives

`V(H)-{a,c}=X⊔Y`.

For `s∈X`, define

`L_s=(a,s)`, `R_s=(s,c)`.

For `s∈Y`, define

`L_s=(c,s)`, `R_s=(s,a)`.

The **source paths at `s`** are the two paths `L_s` and `R_s`.

If `P=(v_0,...,v_k)` and `w∉V(P)`, write `(w,P)` for `(w,v_0,...,v_k)` and `(P,w)` for `(v_0,...,v_k,w)`. A **left-extended path** is a pair `(w;P)` for which `(w,P)` is tight. A **right-extended path** is a pair `(P;w)` for which `(P,w)` is tight. The vertex `w` is the **extension vertex**.

Thus for `s∈X`, `L_s` is right-extended by `c` and `R_s` is left-extended by `a`; for `s∈Y`, `L_s` is right-extended by `a` and `R_s` is left-extended by `c`.

### Lemma 4.1. Restricting an extended path

Let `(w;P)` be a left-extended path, where

`P=(v_0,...,v_k)`.

Let `Q` be a tight path meeting `P` but not containing `v_0`, and let

`i=min{j : v_j∈V(Q)}`.

Then

`P'=(v_0,...,v_{i-1})`

is a nonempty tight path disjoint from `Q`, and `(w;P')` is left-extended by the same vertex `w`.

If `(P;w)` is right-extended and `Q` meets `P` but avoids `v_k`, let

`j=max{h : v_h∈V(Q)}`.

Then

`P''=(v_{j+1},...,v_k)`

is a nonempty tight path disjoint from `Q`, and `(P'';w)` is right-extended by the same vertex `w`.

**Proof.** Since `Q` avoids `v_0`, the first intersection index satisfies `i>=1`. The sequence `(w,v_0,...,v_{i-1})` is an initial segment of the tight path `(w,P)`, so it is tight. The definition of `i` gives disjointness from `Q`.

For the right-extended case, `Q` avoids `v_k`, so `j<=k-1`. The sequence `(v_{j+1},...,v_k,w)` is a terminal segment of the tight path `(P,w)`, so it is tight. The definition of `j` gives disjointness from `Q`. ∎

### Theorem 4.2. Fixed-pair restrictions

For every `s∈V(H)-{a,c}`, the following two fixed-pair restrictions hold.

| orientation of `s` | extended path before restriction | intersecting path `Q` | surviving subpath `P'` | inherited extension |
| --- | --- | --- | --- | --- |
| `s∈X` | `L_s=(a,s)` with `(L_s,c)=(a,s,c)` tight | `(a)` | `(s)` | right by `c` |
| `s∈X` | `R_s=(s,c)` with `(a,R_s)=(a,s,c)` tight | `(c)` | `(s)` | left by `a` |
| `s∈Y` | `L_s=(c,s)` with `(L_s,a)=(c,s,a)` tight | `(c)` | `(s)` | right by `a` |
| `s∈Y` | `R_s=(s,a)` with `(c,R_s)=(c,s,a)` tight | `(a)` | `(s)` | left by `c` |

In each row, the indicated extension belongs to the restricted path; the surviving singleton by itself does not determine that extension.

**Proof.** Consider `s∈X`. The tight triple `(a,s,c)` says that `L_s=(a,s)` is right-extended by `c`. Apply the right-extension part of Lemma 4.1 with `Q=(a)`. The surviving suffix is `(s)`, with the same right extension by `c`.

The same tight triple says that `R_s=(s,c)` is left-extended by `a`. Apply the left-extension part of Lemma 4.1 with `Q=(c)`. The surviving prefix is `(s)`, with the same left extension by `a`.

For `s∈Y`, interchange `a,c`. ∎

### Lemma 4.3. End-interval inheritance

Let `P=(v_0,...,v_k)` be a tight path.

If `(w,P)` is tight and some but not all vertices of `P` are deleted, let

`I=(v_i,...,v_j)`

be the first nonempty interval that remains in the order of `P`. Then `I` is left-extended by `w` when `i=0`, and by the deleted predecessor `v_{i-1}` when `i>0`.

If `(P,w)` is tight and `J=(v_i,...,v_j)` is the last nonempty interval that remains, then `J` is right-extended by `w` when `j=k`, and by the deleted successor `v_{j+1}` when `j<k`.

**Proof.** If `i=0`, `(w,I)` is an initial segment of `(w,P)`. If `i>0`, `(v_{i-1},I)` is a contiguous subpath of `P`.

If `j=k`, `(J,w)` is a terminal segment of `(P,w)`. If `j<k`, `(J,v_{j+1})` is a contiguous subpath of `P`. ∎

### Oppositely extended pairs and continuation sequences

An **oppositely extended pair** is a quadruple

`Pi=(alpha;P,Q;beta)`

where `P,Q` are vertex-disjoint nonempty tight paths, `alpha∉V(P)`, `beta∉V(Q)`, and

`(alpha,P)` and `(Q,beta)`

are tight. The paths `P,Q` are respectively the first and second supports of `Pi`; `alpha` is the left extension vertex of `P`, and `beta` is the right extension vertex of `Q`. When the extension vertices are already specified, we abbreviate the quadruple by `(P,Q)`.

Let

`Pi=(alpha;P,Q;beta)`, `Pi'=(alpha';P',Q';beta')`

be oppositely extended pairs.

Suppose `P=(d_0,d_1)`. A **first-support endpoint reduction** from `Pi` to `Pi'` is a quadruple

`(z,d,x,y)`

where `z∈{d_0,d_1}` is the surviving endpoint, `d` is the other endpoint, and `x,y` are distinct vertices outside

`V(P) union V(Q) union {alpha,beta}`,

such that one of

`(d,x,y)`, `(y,x,d)`

is tight, together with the requirements

`P'=(z)`, `Q'=Q`, `beta'=beta`,

and

`alpha'=alpha` if `z=d_0`, while `alpha'=d_0` if `z=d_1`.

Suppose instead that `Q=(d_0,d_1)`. A **second-support endpoint reduction** from `Pi` to `Pi'` is a quadruple

`(z,d,x,y)`

where `z∈{d_0,d_1}` is the surviving endpoint, `d` is the other endpoint, and `x,y` are distinct vertices outside

`V(P) union V(Q) union {alpha,beta}`,

such that one of

`(d,x,y)`, `(y,x,d)`

is tight, together with the requirements

`P'=P`, `Q'=(z)`, `alpha'=alpha`,

and

`beta'=beta` if `z=d_1`, while `beta'=d_1` if `z=d_0`.

An **endpoint reduction** from `Pi` to `Pi'` is either a first-support endpoint reduction from `Pi` to `Pi'` or a second-support endpoint reduction from `Pi` to `Pi'`.

Suppose

`P=(p)`, `Q=(t_0,...,t_{r-1})`, `r>=2`,

and put

`O=V(H)-({p} union V(Q))`.

A **second-support one-vertex shortening** from `Pi` to `Pi'` is a pair `(F_O,U)` where `F_O` is a path cover of `H[O]` with at most two components and `U` is a distinguished nontrivial component

`U=(u_0,u_1,...)`

of `F_O`, such that one of

`(t_0,u_0,u_1)`, `(u_1,u_0,t_0)`

is tight, and

`P'=P`, `Q'=(t_1,...,t_{r-1})`, `alpha'=alpha`, `beta'=beta`.

Suppose instead that

`P=(t_0,...,t_{r-1})`, `Q=(p)`, `r>=2`,

and put

`O=V(H)-(V(P) union {p})`.

A **first-support one-vertex shortening** from `Pi` to `Pi'` is a pair `(F_O,U)` where `F_O` is a path cover of `H[O]` with at most two components and `U` is a distinguished nontrivial component

`U=(u_0,u_1,...)`

of `F_O`, such that one of

`(t_{r-1},u_0,u_1)`, `(u_1,u_0,t_{r-1})`

is tight, and

`P'=(t_0,...,t_{r-2})`, `Q'=Q`, `alpha'=alpha`, `beta'=beta`.

A **one-vertex shortening** from `Pi` to `Pi'` is either a first-support one-vertex shortening from `Pi` to `Pi'` or a second-support one-vertex shortening from `Pi` to `Pi'`.

Suppose the supports are singletons

`P=(p)`, `Q=(t)`,

and let `y∉{p,t}`. A **second-singleton replacement by `y`** from `Pi` to `Pi'` is a quintuple

`(U,V,d,v_0,v_1)`

such that `U|V` is an exact two-path cover of `H-{p,t}` with both components nontrivial, `y∈V(U)`, `d` is a neighbor of `y` along `U`, `(v_0,v_1)` is an ordered edge of `V`, and one of the following two alternatives holds:

1. `(d,y,t)` is tight, `r=d`, `gamma=t`;
2. `(t,y,d)` is tight, `r=t`, `gamma=d`;

and, in either alternative, one of

`(r,v_0,v_1)`, `(v_1,v_0,r)`

is tight, while

`Pi'=(t;(p),(y);gamma)`.

Under the same singleton hypotheses, a **first-singleton replacement by `y`** from `Pi` to `Pi'` is a quintuple

`(U,V,d,v_0,v_1)`

such that `U|V` is an exact two-path cover of `H-{p,t}` with both components nontrivial, `y∈V(U)`, `d` is a neighbor of `y` along `U`, `(v_0,v_1)` is an ordered edge of `V`, and one of the following two alternatives holds:

1. `(d,y,p)` is tight, `r=p`, `gamma=d`;
2. `(p,y,d)` is tight, `r=d`, `gamma=p`;

and, in either alternative, one of

`(r,v_0,v_1)`, `(v_1,v_0,r)`

is tight, while

`Pi'=(gamma;(y),(t);p)`.

A **prescribed singleton replacement** from `Pi` to `Pi'` is either a first-singleton replacement by some `y` from `Pi` to `Pi'` or a second-singleton replacement by some `y` from `Pi` to `Pi'`.

Define `->` to be the binary relation on oppositely extended pairs given by

`Pi -> Pi'`

if and only if there is an endpoint reduction, a one-vertex shortening, or a prescribed singleton replacement from `Pi` to `Pi'`.

A **continuation sequence** is a finite sequence

`Sigma=(Pi_0,...,Pi_m)`

of oppositely extended pairs such that `Pi_i -> Pi_{i+1}` for every `0<=i<m`. An **extension of `Sigma`** is a continuation sequence

`Sigma'=(Pi_0,...,Pi_m,...,Pi_k)`

having `Sigma` as its initial segment.

Let `P∈{L_s,R_s}`. A **continuation reduction of `P` to `(s)`** is a continuation sequence `Sigma=(Pi_0,...,Pi_m)` with `m>=1` such that `P` is one support of `Pi_0`, the first relation `Pi_0 -> Pi_1` is an endpoint reduction on that support with surviving endpoint `s`, and the corresponding support of `Pi_1` is `(s)`.

A proper subpath of a support is not thereby a later support in a continuation sequence; consecutive pairs must satisfy one of the three relations defining `->`.

### Lemma 4.4. Endpoint reduction using a tight three-vertex path

Let

`Pi=(alpha;P,Q;beta)`

be an oppositely extended pair. Suppose one support is

`D=(d_0,d_1)`

and there are two distinct vertices outside

`V(P) union V(Q) union {alpha,beta}`.

For either prescribed endpoint `z∈{d_0,d_1}`, there is an endpoint reduction on the support `D` whose surviving support is `(z)` and whose other support is unchanged.

**Proof.** Let `d` be the endpoint of `D` different from `z`, and choose distinct

`x,y∉V(P) union V(Q) union {alpha,beta}`.

Boundary antisymmetry makes exactly one of `(d,x,y)` and `(y,x,d)` tight.

First suppose `D=P`. If `z=d_0`, put `alpha'=alpha`; if `z=d_1`, put `alpha'=d_0`. Then

`Pi'=(alpha';(z),Q;beta)`

is an oppositely extended pair, and `(z,d,x,y)` is a first-support endpoint reduction from `Pi` to `Pi'`.

Now suppose `D=Q`. If `z=d_1`, put `beta'=beta`; if `z=d_0`, put `beta'=d_1`. Then

`Pi'=(alpha;P,(z);beta')`

is an oppositely extended pair, and `(z,d,x,y)` is a second-support endpoint reduction from `Pi` to `Pi'`. ∎


### Lemma 4.5. Fixed-singleton descent

Let

`T=(t_0,...,t_{r-1})`

be a nonempty tight path.

1. If
   
   `Pi_0=(alpha;(p),T;beta)`
   
   is an oppositely extended pair, then there is a continuation sequence
   
   `Pi_0 -> Pi_1 -> ... -> Pi_{r-1}`
   
   whose last pair has supports `((p),(t_{r-1}))`. If `r>1`, each relation is a second-support one-vertex shortening, so the sequence has exactly `r-1` such shortenings.
2. If
   
   `Pi_0=(alpha;T,(p);beta)`
   
   is an oppositely extended pair, then there is a continuation sequence
   
   `Pi_0 -> Pi_1 -> ... -> Pi_{r-1}`
   
   whose last pair has supports `((t_0),(p))`. If `r>1`, each relation is a first-support one-vertex shortening, so the sequence has exactly `r-1` such shortenings.

**Proof.** For the first assertion, if `r=1`, take the one-term sequence. Assume `r>=2`, and put

`O=V(H)-({p} union V(T))`.

Every tight path of `H` leaves at least four vertices outside it. Since `p∉V(T)`, the set `O` has order at least three. The induced boundary tournament `H[O]` is proper, so minimality gives a path cover of `H[O]` by at most two tight paths. Some component is nontrivial; write it

`U=(u_0,u_1,...)`.

Boundary antisymmetry on `{t_0,u_0,u_1}` makes exactly one of

`(t_0,u_0,u_1)`, `(u_1,u_0,t_0)`

tight. Put

`T'=(t_1,...,t_{r-1})`.

The path `T'` remains right-extended by `beta`, so

`Pi_1=(alpha;(p),T';beta)`

is an oppositely extended pair. The chosen path cover, the component `U`, and the displayed tight triple give a second-support one-vertex shortening. Repeating the same construction removes one first vertex at each stage and reaches `(t_{r-1})` after exactly `r-1` shortenings.

For the second assertion, again take the one-term sequence when `r=1`. Assume `r>=2`, and put

`O=V(H)-(V(T) union {p})`.

As above, `|O|>=3`, and `H[O]` has a path cover by at most two tight paths with a nontrivial component

`U=(u_0,u_1,...)`.

Boundary antisymmetry on `{t_{r-1},u_0,u_1}` makes exactly one of

`(t_{r-1},u_0,u_1)`, `(u_1,u_0,t_{r-1})`

tight. Put

`T'=(t_0,...,t_{r-2})`.

The path `T'` remains left-extended by `alpha`, so

`Pi_1=(alpha;T',(p);beta)`

is an oppositely extended pair. The chosen path cover, the component `U`, and the displayed tight triple give a first-support one-vertex shortening. Repeating the same construction removes one last vertex at each stage and reaches `(t_0)` after exactly `r-1` shortenings. ∎


### Lemma 4.6. Prescribed singleton replacement

Let

`Pi=(alpha;(p),(t);beta)`

be an oppositely extended singleton pair, and let `y∉{p,t}`.

Then there are prescribed singleton replacements

`Pi -> Pi_R`, `Pi -> Pi_L`

such that `Pi_R` has supports `((p),(y))` and `Pi_L` has supports `((y),(t))`.

**Proof.** By Lemma 1.2 choose an exact two-path cover

`H-{p,t}=U|V`

with both paths nontrivial. Relabel if necessary so that `y∈V(U)`, and choose a neighbor `d` of `y` along `U`. Choose an ordered edge `(v_0,v_1)` of `V`.

For the replacement of the second support, exactly one of

`(d,y,t)`, `(t,y,d)`

is tight. In the first case put `r=d` and `gamma=t`; in the second put `r=t` and `gamma=d`. Boundary antisymmetry makes exactly one of

`(r,v_0,v_1)`, `(v_1,v_0,r)`

tight. Therefore

`Pi_R=(t;(p),(y);gamma)`

is an oppositely extended pair, and the displayed objects give a second-singleton replacement by `y`.

For the replacement of the first support, exactly one of

`(d,y,p)`, `(p,y,d)`

is tight. If `(d,y,p)` is tight, put `r=p` and `gamma=d`; then

`(d;(y,p),(t);p)`

is an oppositely extended pair. If `(p,y,d)` is tight, put `r=d` and `gamma=p`; then

`(p;(y,d),(t);p)`

is an oppositely extended pair. In either case the first support is `(y,r)` and its left extension is `gamma`.

Boundary antisymmetry makes exactly one of

`(r,v_0,v_1)`, `(v_1,v_0,r)`

tight. Thus the ordered edge `(v_0,v_1)` of `V` supplies the tight three-vertex path required for a first-support endpoint reduction preserving `y`. The resulting pair is

`Pi_L=(gamma;(y),(t);p)`,

so the displayed objects give a first-singleton replacement by `y`. ∎


### Theorem 4.7. Prescribed common singleton for both fixed-pair source reductions

Let

`s∈V(H)-{a,c}`

and let

`v∈V(H)-{a,c,s}`

be prescribed. Then the two source paths `L_s,R_s` admit separate continuation sequences with the following last pairs:

- the sequence starting from `R_s` has last pair `((s),(v))`;
- the sequence starting from `L_s` has last pair `((v),(s))`.

In particular, both source paths have continuation reductions to `(s)`, and both reductions can be made to end on the same unordered singleton pair `{s,v}`. The two sequences are alternative constructions and are not asserted to coexist.

**Proof.** Choose distinct vertices

`u,w∈V(H)-{a,c,s,v}`.

Boundary antisymmetry makes exactly one of `(u,v,w)` and `(w,v,u)` tight. Interchange `u,w` if necessary so that

`(u,v,w)`

is tight. Then `(u,v)` is right-extended by `w`, while `(v,w)` is left-extended by `u`.

The source path `R_s` is left-extended: by `a` when `s∈X`, and by `c` when `s∈Y`. Hence

`(R_s,(u,v))`

is an oppositely extended pair whose two supports both have order two. Its two supports together with their two displayed extension vertices use at most six vertices. Since `n>10`, at least five other vertices remain. By Lemma 4.4 there is an endpoint reduction of the first support with surviving endpoint `s`, giving

`((s),(u,v))`.

By Lemma 4.5, one one-vertex shortening then gives

`((s),(v))`.

Similarly, `L_s` is right-extended: by `c` when `s∈X`, and by `a` when `s∈Y`. Hence

`((v,w),L_s)`

is an oppositely extended pair whose two supports both have order two. Applying Lemma 4.4 to the second support gives an endpoint reduction with surviving endpoint `s`, giving

`((v,w),(s))`,

and Lemma 4.5(2) gives one first-support one-vertex shortening ending at

`((v),(s))`.

Every removed source-support vertex is therefore met by an explicitly displayed tight three-vertex path when it is removed. No step uses bare endpoint deletion. The two constructions are separate, so their auxiliary tight paths need not be compatible with one another. ∎

### Proposition 4.8. Comparison with a new edge through `s`

Let `s∈X` and `u∉{a,s,c}`.

1. If `Q=(s,u)`, exactly one of `(a,s,u)` and `(u,s,a)` is tight. If `(a,s,u)` is tight, it is a tight path properly containing both `L_s=(a,s)` and `Q`; if `(u,s,a)` is tight, that triple traverses the ordinary edges of `Q` and `L_s` in the opposite order.
2. If `Q=(u,s)`, exactly one of `(u,s,c)` and `(c,s,u)` is tight. If `(u,s,c)` is tight, it is a tight path properly containing both `Q` and `R_s=(s,c)`; if `(c,s,u)` is tight, that triple traverses the ordinary edges of `R_s` and `Q` in the opposite order.

The same statements hold for `s∈Y` after interchanging `a,c`.

**Proof.** Each item is one reversal pair, so boundary antisymmetry proves the assertion. ∎

### Theorem 4.9. A new endpoint and return within one continuation sequence

Let `s∈V(H)-{a,c}`.

If a two-vertex tight path through `s` has the form

`Q=(s,u)` or `Q=(u,s)`

with `u∉{a,s,c}`, then either `Q` and one source path through `s` lie in a tight three-vertex path containing both, or there is a tight triple containing `u` that traverses an ordered edge of `Q` and an ordered edge of that source path in the opposite order.

Now let `P` be one of the source paths `L_s,R_s`, let `Sigma=(Pi_0,...,Pi_m)` be a continuation reduction of `P` to `(s)`, and let

`Sigma'=(Pi_0,...,Pi_m,...,Pi_k)`

be an extension of `Sigma`. If some `Pi_j` with `j>1` has a two-vertex support whose vertex set is `V(P)`, then that support occurs after the reduction of `P` to `(s)`.

The conclusion concerns only members of the same continuation sequence; it gives no ordering between supports belonging to unrelated continuation sequences.

**Proof.** If `s∈X`, the two possible orientations of the triples on `{a,s,u}` and `{u,s,c}` give the first assertion exactly as in the two cases displayed in Proposition 4.8; if `s∈Y`, interchange `a,c`. For the second assertion, the definition of a continuation reduction gives `P` as a support of `Pi_0` and `(s)` as the corresponding support of `Pi_1`. Thus any later `Pi_j` with a support on the vertex set `V(P)` occurs after the singleton stage. ∎

### Lemma 4.10. Four vertices of one orientation

Let `S⊆V(H)-{a,c}` have order at least four, and suppose `(a,s,c)` is tight for every `s∈S`. Then there are distinct `x,y,z∈S` such that

`(x,a,y,c,z)`

is a tight path.

**Proof.** It is enough to prove the result for a four-element subset of `S`, so assume `|S|=4`. Define tournaments on `S` by

`x->_a y` iff `(x,a,y)` is tight,

`x->_c y` iff `(x,c,y)` is tight.

Suppose no distinct `x,y,z` satisfy `x->_a y->_c z`. If a vertex has indegree at least two in `->_a`, then it has outdegree zero in `->_c`; otherwise two of its `->_a` predecessors together with one `->_c` successor would give such a mixed chain.

The sum of indegrees in the four-vertex tournament `->_a` is six, so some vertex `y` has indegree at least two. Hence `y` has outdegree zero in `->_c`, so `y` is the unique `->_c` sink. Every other vertex has positive `->_c` outdegree and therefore `->_a` indegree at most one. The indegree sum then forces `y` to have `->_a` indegree three and each other vertex to have `->_a` indegree one. Thus `y` is also the `->_a` sink.

Choose `v!=y`. Since `y` is the `->_c` sink, `v->_c y`. The unique `->_a` predecessor `x` of `v` cannot be `y`, because `y` is the `->_a` sink. Hence `x->_a v->_c y`, a mixed chain on three distinct vertices, contradiction. Therefore such a mixed chain exists. Renaming its middle and last vertices as `y,z`, the triples `(x,a,y)`, `(a,y,c)`, `(y,c,z)` are tight, so `(x,a,y,c,z)` is tight. ∎

### Corollary 4.11. A five-vertex path through vertices with both source reductions

Every subset `S⊆X` of order at least four contains distinct `x,y,z` for which

`(x,a,y,c,z)`

is a tight path, and every subset `S⊆Y` of order at least four contains distinct `x,y,z` for which

`(x,c,y,a,z)`

is a tight path. For each of the three vertices, both fixed-pair source paths admit continuation reductions to the corresponding singleton. In particular, since one of `X,Y` has order at least `ceil((n-2)/2)>=5`, such a five-vertex path always exists.

**Proof.** Apply Lemma 4.10 to the chosen subset, interchanging `a,c` for `Y`. Theorem 4.7 supplies both source reductions for every vertex outside `{a,c}`. ∎


## 5. Deletion and comparison of path covers

If `F` is an ordinary graph and `S⊆V(F)`, write `F-S` for the induced subgraph on `V(F)-S`, `deg_F(v)` for the ordinary degree of `v`, `e_F(S)` for the number of ordinary edges of `F` with both endpoints in `S`, and `comp(F)` for the number of connected components of `F`, counting isolated vertices.

### Lemma 5.1. Counting components after deletion

Let `F` be an ordinary path forest with `k` components and let `S⊆V(F)`. Then

`comp(F-S)=k+sum_{v in S}(deg_F(v)-1)-e_F(S)`.


If `F` is the ordinary path forest of a tight-path cover, every nonempty component of `F-S` inherits from its path component before deletion a tight vertex order.

**Proof.** Let `N=|V(F)|`. Since `F` is a path forest with `k` components, it has `N-k` edges. Deleting `S` removes

`sum_{v in S} deg_F(v)-e_F(S)`

edges: the degree sum counts an edge internal to `S` twice, so one copy must be subtracted. The remaining graph has

`N-|S|`

vertices and

`N-k-sum_{v in S}deg_F(v)+e_F(S)`

edges. A forest has number of components equal to vertices minus edges, which gives the displayed formula. Tightness of inherited path orders follows because every surviving component is a contiguous subpath of an original tight path. ∎

### Proposition 5.2. One internal deletion produces a crossing

Fix distinct vertices `a,c`, let `U|V` be an exact two-path cover of `H-{a,c}`, and let `s` be internal in one of `U,V`. Let `T` be any exact two-path cover of `H-{a,c,s}`; such a cover exists.

Deleting `s` from `U|V` leaves three nonempty ordered paths. Some ordinary edge `xy` of `T` has its endpoints in two different paths among those three. Moreover the edge may be named so that there is a vertex `h∉{x,y}` for which `{h,x}` is an ordinary edge of the cover `U|V`. Boundary antisymmetry then gives exactly one tight triple from the reversal pair

`(h,x,y)`, `(y,x,h)`.


If the path containing `x` after deletion of `s` is nontrivial, `h` may be chosen in that path. If both paths crossed by `xy` are singletons, one may take `h=s`.

**Proof.** The three-set `{a,s,c}` has a Hamilton tight path, so Lemma 1.1 gives `pc(H-{a,c,s})=2`; hence an exact cover `T` exists.

Deleting the internal vertex `s` splits one of `U,V` into two nonempty subpaths and leaves the other path unchanged. Thus three nonempty path vertex sets remain. If every ordinary edge of both components of `T` had both endpoints inside one of these three sets, then each connected component of the ordinary path forest of `T` would lie inside one of the three sets. Two connected components could not cover all three nonempty sets. Therefore an ordinary edge `xy` of `T` crosses two of the three sets.

If one crossed set contains at least two vertices, name the endpoint in that set `x` and choose `h` adjacent to `x` along its inherited subpath. Then `{h,x}` is an ordinary edge of `U|V`, and `h` is distinct from `x,y`.

Otherwise both crossed sets are singleton subpaths. The unchanged component of `U|V` is nontrivial by Lemma 1.2, so the two singleton subpaths are the two pieces created by deleting the internal vertex `s`. Each singleton vertex was adjacent to `s` in the original path. Name either one `x` and take `h=s`. Boundary antisymmetry gives the displayed reversal pair. ∎

Thus the two compared covers determine ordinary edges `{h,x}`, `{x,y}` and the reversal pair `(h,x,y)`, `(y,x,h)`, exactly one member of which is tight.

For the remainder of this section, fix distinct vertices `a,c` and an exact two-path cover

`U|V`

of `H-{a,c}`.

### Proposition 5.3. Internal vertices of one orientation

Exactly `n-6` vertices are internal in `U|V`. Consequently one of the two orientation classes contains at least

`ceil((n-6)/2)`

internal vertices. In particular, since `n>10`, there are three internal vertices `p,q,r` for which either

`(a,p,c)`, `(a,q,c)`, `(a,r,c)`

are all tight, or

`(c,p,a)`, `(c,q,a)`, `(c,r,a)`

are all tight.

**Proof.** By Lemma 1.2 both paths are nontrivial, so together they have exactly four endpoints among the `n-2` vertices of `H-{a,c}`. The remaining `n-6` vertices are exactly the internal vertices. The partition `V(H)-{a,c}=X⊔Y` partitions them into two classes, so one class contains at least `ceil((n-6)/2)` internal vertices. Since `n>10`, this number is at least three. ∎

After interchanging `a,c` if necessary, we shall write the selected vertices so that

`(a,p,c)`, `(a,q,c)`, `(a,r,c)`


are tight.

### Proposition 5.4. The eight induced subgraphs

Let `p,q,r` be distinct vertices such that `(a,p,c)`, `(a,q,c)`, `(a,r,c)` are tight, and put

`P={p,q,r}`, `K={a,c,p,q,r}`, `W=V(H)-K`.

For every `J⊆P`, define

`G_J=H[W∪J]`.

Then `H[K-J]` has a Hamilton tight path and

`pc(G_J)=2`.

Consequently every exact two-path cover of `G_J`, together with any Hamilton tight path on `K-J`, is a spanning three-path cover of `H`.

**Proof.** If `J=∅`, Lemma 2.2 applied to the three common-endpoint triples `(a,p,c)`, `(a,q,c)`, `(a,r,c)` gives a Hamilton path on `K`.

If `|P-J|=2`, write `P-J={s,t}`. Exactly one of `(s,c,t)` and `(t,c,s)` is tight, so either `(a,s,c,t)` or `(a,t,c,s)` is a Hamilton path on `K-J`. If `|P-J|=1`, say `P-J={s}`, the path `(a,s,c)` is Hamilton on `K-J`. If `P-J=∅`, `(a,c)` is Hamilton on `K-J`.

Thus `H[K-J]` is Hamiltonian for every `J`. Since `W` has order `n-5>=6`, every `G_J` is a proper nonempty induced subgraph of `H`, so minimality gives `pc(G_J)<=2`. If `G_J` were Hamiltonian, a Hamilton path in `G_J` together with the Hamilton path on `K-J` would two-cover `H`. Therefore `pc(G_J)=2`. Since

`V(H)=(W∪J)⊔(K-J)`,

every exact two-path cover of `G_J` together with a Hamilton tight path on `K-J` is a spanning three-path cover of `H`. ∎

For each `s in P`, let `U|V` be the fixed exact cover of `G_P=H-{a,c}` and let `U'|V'` be any exact cover of `G_{P-{s}}`. Then deleting `s` from the ordinary path forest of `U|V` and comparing the resulting subpaths with `U'|V'` yields vertices `h,x,y` for which `{h,x}` is an ordinary edge inherited from `U|V`, `{x,y}` is an ordinary edge of `U'|V'`, and exactly one of `(h,x,y)`, `(y,x,h)` is tight.

## 6. A lexicographically maximal three-path cover

For a spanning three-path cover `F`, let

`lambda(F)=(ell_1,ell_2,ell_3)`, `ell_1>=ell_2>=ell_3`,

be its three component orders in decreasing order. For two distinct triples `x=(x_1,x_2,x_3)` and `y=(y_1,y_2,y_3)`, define `x` to be **lexicographically larger** than `y` if, for the least index `i` with `x_i!=y_i`, one has `x_i>y_i`. Since each `ell_i` is a positive integer and `ell_1+ell_2+ell_3=n`, only finitely many such triples occur. Choose a spanning three-path cover

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

### Proposition 6.2. Fixed-pair restrictions and reductions at the ends of the longest component

Write

`A=(v_0,...,v_{ell-1})`.

Choose a nontrivial component

`X_0=(x_0,...,x_m)`

from `{B,C}` and put

`a=x_0`, `c=x_m`.

Then

`(a,v_{ell-1},v_{ell-2})`, `(v_1,v_0,c)`

are tight. Each of the four vertices

`v_{ell-1}`, `v_{ell-2}`, `v_1`, `v_0`

lies outside `{a,c}`. Hence each has both fixed-pair restrictions, and each of its two source paths admits a continuation reduction to the corresponding singleton.

Because `n>10`, one may choose a vertex

`z∉{a,c,v_{ell-1},v_{ell-2},v_1,v_0}`.

For each of the four displayed end vertices `s`, both source reductions can be chosen to end on the same unordered singleton pair `{s,z}`; the two reductions for a fixed `s`, and the reductions for different `s`, remain separate continuation sequences.

For any one of these four vertices `s`, a two-vertex path through `s` with a new endpoint outside `{a,c}` either joins one source path through `s` inside a tight three-vertex path or forms, with that source path, a reversed ordered-edge pair in a tight triple. If one of the continuation sequences just described is an initial segment of a longer continuation sequence, then any later occurrence of the same source support occurs after its singleton stage.

No assertion is made that the several continuation sequences coexist or that one is an initial segment of another.

**Proof.** Proposition 6.1 shows that no endpoint of `B` or `C` can be transferred into `A`. Proposition 3.2 applied to the endpoints `a,c` of `X_0` gives the two displayed tight triples. Since the three components of `A|B|C` are disjoint, the four displayed vertices of `A` lie outside `{a,c}`, so Theorem 4.2 gives both fixed-pair restrictions for all four. The choice of `z` is possible because at most six vertices are excluded and `n>10`; Theorem 4.7 then gives both continuation reductions for each end vertex with the same prescribed second singleton `z`. Proposition 4.8 gives the extension-or-reversal alternative for a new two-vertex path through `s`. If a chosen reduction sequence is an initial segment of a longer continuation sequence, Theorem 4.9 places every later occurrence of the same source support after its singleton stage. ∎

Lexicographic maximality rules out every spanning three-path cover whose component-order triple is lexicographically larger than `lambda(F)`. For every vertex outside a fixed pair, each source path admits a continuation reduction to its singleton. A later occurrence of a source support is ordered after that singleton stage only when both occurrences lie in one continuation sequence.

It remains to establish the following augmentation statement:

> Let `F` be a spanning three-path cover of a smallest counterexample such that no endpoint can be transferred from one component into another component of at least equal order. Then either a spanning two-path cover exists or there is a spanning three-path cover `F'` with `lambda(F')` lexicographically larger than `lambda(F)`.

The statement is not proved here.

## Appendix A. Intersections of ordered paths

For a tight path `P=(p_0,...,p_k)`, an **ordered edge of `P`** is an ordered pair `(p_i,p_{i+1})` for some `0<=i<k`. A tight triple `(x,y,z)` **reverses an ordered edge of P** if `(z,y)` or `(y,x)` is an ordered edge of `P`; equivalently, one of its consecutive ordered pairs is the reverse of an ordered edge of `P`.

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

### Lemma A.2. Intersection at an extended end

Let `(w;P)` be a left-extended path with

`P=(v_0,...,v_k)`,

and let `Q` be a tight path containing `v_0`. Then at least one of the following exists:

1. a tight path properly containing `P` as an ordered subpath;
2. a tight path properly containing `Q` as an ordered subpath;
3. a vertex-simple tight cycle;
4. a tight triple that reverses an ordered edge of `P` or `Q`.

All vertices in the conclusion lie in `V(P)∪V(Q)∪{w}`.

The same four alternatives hold if `(P;w)` is right-extended and `Q` contains `v_k`; again all vertices in the conclusion lie in `V(P)∪V(Q)∪{w}`.

**Proof.** First suppose `(w;P)` is left-extended. If `k=0`, then either `Q=(v_0)`, in which case `(w,v_0)` is a tight path properly containing both `P` and `Q`, or `Q` properly contains `P`. Hence assume `k>=1`.

If the common vertices of `P,Q` occur in different relative orders, apply Lemma A.1. Outcomes 2 and 3 there already suffice. If outcome 1 there gives a reversed common edge, choose a consecutive tight triple of `(w,P)` containing that edge. Such a triple exists because `(w,P)` has order at least three. This gives outcome 4 here.

Now assume the common vertices occur in the same order. Since `Q` contains `v_0`, the vertex `v_0` is the first common vertex along `Q`.

If `Q` has a predecessor `u` immediately before `v_0`, test `(u,v_0,v_1)`. If it is tight, the initial segment of `Q` ending at `v_0` followed by `P` is a tight path properly containing `P`; the initial segment has no other vertex of `P`. If it is not tight, `(v_1,v_0,u)` is tight and gives outcome 4.

It remains that `Q` starts at `v_0`. If `Q=(v_0)`, then `(w,v_0)` properly contains `Q`. Otherwise write the next vertex of `Q` as `q_1`. If `w∉V(Q)`, test `(w,v_0,q_1)`. If it is tight, `(w,Q)` properly contains `Q`; otherwise `(q_1,v_0,w)` is tight and gives outcome 4.

Finally suppose `w∈V(Q)`. The paths `(w,P)` and `Q` contain the common vertices `w,v_0` in opposite orders. Apply Lemma A.1 to these two paths. Its tight-triple outcome gives outcome 4 here, its cycle outcome gives outcome 3, and its reversed-edge outcome can be placed in a consecutive tight triple of `(w,P)`, giving outcome 4.

Now suppose `(P;w)` is right-extended. If `k=0`, then either `Q=(v_0)`, in which case `(v_0,w)` is a tight path properly containing both `P` and `Q`, or `Q` properly contains `P`. Hence assume `k>=1`.

If the common vertices of `P,Q` occur in different relative orders, apply Lemma A.1. Outcomes 2 and 3 there already suffice. If outcome 1 there gives a reversed common edge, choose a consecutive tight triple of `(P,w)` containing that edge. Such a triple exists because `(P,w)` has order at least three. This gives outcome 4 here.

Now assume the common vertices occur in the same order. Since `Q` contains `v_k`, the vertex `v_k` is the last common vertex along `Q`.

If `Q` has a successor `u` immediately after `v_k`, test `(v_{k-1},v_k,u)`. If it is tight, `P` followed by the terminal segment of `Q` beginning at `v_k` is a tight path properly containing `P`; that terminal segment has no other vertex of `P`. If it is not tight, `(u,v_k,v_{k-1})` is tight and gives outcome 4.

It remains that `Q` ends at `v_k`. If `Q=(v_k)`, then `(v_k,w)` properly contains `Q`. Otherwise write the preceding vertex of `Q` as `q`. If `w∉V(Q)`, test `(q,v_k,w)`. If it is tight, `(Q,w)` properly contains `Q`; otherwise `(w,v_k,q)` is tight and gives outcome 4.

Finally suppose `w∈V(Q)`. The paths `(P,w)` and `Q` contain the common vertices `v_k,w` in opposite orders. Apply Lemma A.1 to these two paths. Its tight-triple outcome gives outcome 4 here, its cycle outcome gives outcome 3, and its reversed-edge outcome can be placed in a consecutive tight triple of `(P,w)`, giving outcome 4. ∎

Every tight cycle has order at most `n-4`, because opening it gives a tight path on the same vertex set.
