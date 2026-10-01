# Small-order Hamiltonicity and structure

## Statement

Comparison representation; non-Hamiltonian four- and five-vertex structure; matching-block classification; fifth-vertex extension of the cyclic K4; four-of-six; and the exact count of bad four-subsets of a five-set.

## Body

# Small-order Hamiltonicity and edge-order representation

Throughout this file, `H` denotes an arbitrary boundary tournament unless another boundary tournament is explicitly named.

Let `K_V` denote the ordinary complete graph on a vertex set `V`. Its edge set consists of the two-element subsets of `V`. The **line graph** `L(K_V)` is the graph with vertex set `E(K_V)` in which two vertices are adjacent exactly when the corresponding ordinary edges meet.

For a boundary tournament `G` on `V`, define the **comparison digraph** `Gamma(G)` as the orientation of `L(K_V)` in which, for distinct `u,v,w`,

`{u,v} -> {v,w}`

if and only if `(u,v,w)` is tight.

An **edge order** on `K_V` is a strict total order `<` on `E(K_V)`. An **edge-ordered complete graph** is a complete graph together with such an edge order. A vertex-simple sequence `(v_0,...,v_k)` is an **increasing path** if

`{v_0,v_1} < {v_1,v_2} < ... < {v_{k-1},v_k}`.

## 1. Comparison representation

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

## 2. Three common-endpoint triples force a Hamilton five-path

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

## 3. Non-Hamiltonian five-sets are edge-orderable

Let `G` be a boundary tournament on exactly five vertices. If `G` has no Hamilton tight path, then `Gamma(G)` is acyclic. Equivalently, there is a strict total order `<` on `E(K_5)` such that, for all distinct `u,v,w`,

`(u,v,w) is tight  iff  {u,v}<{v,w}`.

**Proof.** Suppose `G` is non-Hamiltonian and `Gamma(G)` contains a directed cycle. Choose a shortest one. By Section 1 it is a star triangle, an ordinary triangle, or a vertex-simple ordinary cycle. A comparison cycle of length five itself gives a Hamilton tight path, so an ordinary cycle can only have length four.

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

If `M(c)` and `M(d)` shared a coordinate, that coordinate, together with `c,d`, would be the three middle vertices of three tight triples with the same first and third vertices; Section 2 would give a Hamilton five-path. Hence `M(c)` and `M(d)` are disjoint.

Up to cyclic permutation of `o,a,b` and exchange of `c,d`, the disjoint pair is one of

`(∅,∅)`, `(∅,{o})`, `(∅,{o,a})`, `(∅,{o,a,b})`, `({o},{a})`, `({o},{a,b})`.

The match-set definition fixes all mixed triples involving one exterior vertex and two vertices of the fixed three-set used in the following exhaustive table:

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

The extra branches in the table are reversal pairs, so the table is exhaustive. Thus no shortest directed comparison cycle exists. Hence `Gamma(G)` is acyclic, and Section 1 gives the required edge order. ∎

## 4. Edge-ordered four-set structure

### 4.1 Matching-block classification

An edge-ordered `K_4` has no increasing Hamilton path if and only if its three opposite-edge perfect matchings occur as three strict consecutive blocks in the edge order.

**Proof.** Let the six edges be
`e_1<e_2<...<e_6`.
If there is no increasing Hamilton path and `e_1,e_2` meet, say `e_1=ab`, `e_2=bc`, then for the fourth vertex `d` the edge `cd` occurs after `e_2`, so `a,b,c,d` is increasing, a contradiction. Hence `e_1,e_2` are disjoint. Dually `e_5,e_6` are disjoint. Therefore `{e_1,e_2}`, `{e_3,e_4}`, `{e_5,e_6}` are exactly the three opposite perfect matchings.

Conversely, in any Hamilton four-vertex word the first and third ordinary edges are disjoint, hence belong to the same opposite-edge matching. If each matching is a strict block, the middle edge lies wholly before or wholly after that block, so it cannot lie strictly between the first and third edges. Thus no Hamilton word is increasing. ∎

### 4.2 Two non-Hamiltonian four-sets force a Hamilton five-set

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

## 5. Extending a fixed three-vertex path

Let `P` be a tight path of `H` on three vertices and let `x,y,z` be distinct vertices of `V(H)-V(P)`. At least one of

`V(P)∪{x,y}`, `V(P)∪{x,z}`, `V(P)∪{y,z}`

has a Hamilton tight path.

**Proof.** Write `P` on vertices `{a,b,c}`. Assume, for contradiction, that all three five-sets obtained by adding two of `x,y,z` are non-Hamiltonian. Section 3 shows that each is represented by an edge order. Their restrictions to the common triangle `{a,b,c}` realize the same comparison orientation, so after relabelling the three vertices we may assume

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

If two exterior vertices `u,v` shared a coordinate of their match sets, Section 2 would apply. Indeed, a shared coordinate `a` gives the triples `(b,a,c),(b,u,c),(b,v,c)`; a shared coordinate `b` gives `(a,b,c),(a,u,c),(a,v,c)`; and a shared coordinate `c` gives `(a,c,b),(a,u,b),(a,v,b)`. In every case `P∪{u,v}` would have a Hamilton five-path, a contradiction. Hence `M(x),M(y),M(z)` are pairwise disjoint.

Two match sets cannot both be `∅`. If `M(u)=M(v)=∅`, then in the edge order on `P∪{u,v}`,

`uc<ub<ua`, `vc<vb<va`.

If `ub<vb`, the word `c,u,b,v,a` is increasing; if `vb<ub`, the word `c,v,b,u,a` is increasing. Either contradicts non-Hamiltonicity.

Therefore exactly one match set is `∅`. The other two are disjoint nonempty members of

`{a}`, `{c}`, `{a,b}`, `{b,c}`, `{a,b,c}`.

Three nonempty pairwise disjoint match sets would have to be `{a},{b},{c}`, but `{b}` is not in the list. After naming the vertex `x` with empty match set and ordering `y,z`, only the following three cases remain:

`I. M(x)=∅, M(y)={a}, M(z)={c};`

`II. M(x)=∅, M(y)={a}, M(z)={b,c};`

`III. M(x)=∅, M(y)={a,b}, M(z)={c}.`

Assume throughout that the relevant five-set is non-Hamiltonian. We use the same forcing rule: if a five-vertex word has two known tight triples, the reverse of its third triple is forced. The initial mixed triples involving one exterior vertex and two vertices of the fixed three-set are

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

## 6. Four Hamiltonian five-subsets of every six-set

For every six-element set `E⊆V(H)`, at least four of the five-element subsets of `E` induce Hamiltonian boundary tournaments.

**Proof.** Let `E` be a six-set and let

`M={e in E : H[E-{e}] has a Hamilton path}`.

Choose any three-set `T⊆E`. The complementary three-set `P=E-T` can be ordered as a tight path: choose any middle vertex, and boundary antisymmetry chooses one of the two orders of the other two vertices. Section 5 applied to this path and the three vertices of `T` shows that `M∩T` is nonempty. If `|E-M|>=3`, choose `T⊆E-M` of order three, a contradiction. Thus `|M|>=4`. ∎

## 7. Non-Hamiltonian four-subsets of a five-set

Let `S⊆V(H)` have order five. If `H[S]` is Hamiltonian, at most three four-element subsets of `S` are non-Hamiltonian. If `H[S]` is non-Hamiltonian, at most one four-element subset of `S` is non-Hamiltonian.

**Proof.** Let `S` be a five-set. If `H[S]` is Hamiltonian, choose a Hamilton order `(v_0,...,v_4)`. Deleting `v_0` or deleting `v_4` leaves a Hamilton tight four-vertex path, so at most three of the five four-subsets are non-Hamiltonian.

Suppose instead that `H[S]` is non-Hamiltonian. By Section 3 it is represented by an edge order. If two distinct four-subsets were both non-Hamiltonian, they would have the form `T∪{x}` and `T∪{y}` for their three-vertex intersection `T`. Their induced edge orders have no increasing Hamilton path, so Section 4.2 gives an increasing Hamilton path on all five vertices. By the representation, this is a tight Hamilton path of `H[S]`, a contradiction. Thus in the non-Hamiltonian case at most one four-subset is non-Hamiltonian. ∎


# Further four- and five-vertex structure

## 1. Two common-first-pair tight triples force one of two edge-orderable four-vertex forms

Let `H` be a boundary tournament, and let `a,b,c,d` be distinct vertices of `H`. Suppose

`(a,b,c)`, `(a,b,d)`

are tight and `H[{a,b,c,d}]` has no Hamilton tight path. Then the following six additional triples are tight:

`(b,a,c)`, `(b,a,d)`,

`(c,d,a)`, `(d,c,a)`,

`(c,d,b)`, `(d,c,b)`.

Moreover exactly two completions of the boundary relation are possible. Put

`M_0={ab,cd}`, `M_1={ac,bd}`, `M_2={ad,bc}`.

The induced boundary tournament is represented by an edge order in which the three opposite-edge matchings occur as strict blocks, with either

`M_0 < M_1 < M_2`

or

`M_0 < M_2 < M_1`.

**Proof.** Since `(a,b,c)` is tight, the path `(a,b,c,d)` can fail only at `(b,c,d)`; hence `(d,c,b)` is tight. Similarly `(a,b,d,c)` forces `(c,d,b)`.

Now `(a,c,d,b)` has `(c,d,b)` tight, so non-Hamiltonicity forces `(d,c,a)`; and `(a,d,c,b)` similarly forces `(c,d,a)`. Finally `(c,a,b,d)` and `(d,a,b,c)` force `(b,a,c)` and `(b,a,d)`.

The only remaining freedom can be taken to be the reversal pair `(a,c,b)` versus `(b,c,a)`.

Suppose first that `(a,c,b)` is tight. If `(c,b,d)` were tight, then `(a,c,b,d)` would be Hamiltonian; hence `(d,b,c)` is tight. If `(a,d,b)` were tight, then `(a,d,b,c)` would be Hamiltonian because `(d,b,c)` is tight; hence `(b,d,a)` is tight. If `(d,a,c)` were tight, then `(d,a,c,b)` would be Hamiltonian because `(a,c,b)` is tight; hence `(c,a,d)` is tight. These three choices, together with the eight triples already forced, determine every reversal pair and give the block order `M_0<M_1<M_2`.

Suppose instead that `(b,c,a)` is tight. If `(c,a,d)` were tight, then `(b,c,a,d)` would be Hamiltonian; hence `(d,a,c)` is tight. If `(b,d,a)` were tight, then `(b,d,a,c)` would be Hamiltonian because `(d,a,c)` is tight; hence `(a,d,b)` is tight. If `(d,b,c)` were tight, then `(d,b,c,a)` would be Hamiltonian because `(b,c,a)` is tight; hence `(c,b,d)` is tight. These three choices determine every reversal pair and give the block order `M_0<M_2<M_1`.

Both block orders have no increasing Hamilton four-vertex path by the matching-block classification in `the earlier small-set results` the matching-block classification above, so both completions occur and there are no others. ∎

## 2. The cyclic non-Hamiltonian four-vertex configuration is extended by every fifth vertex

Let `H` be a boundary tournament and let `X={a,b,c,z} subseteq V(H)`. Suppose the tight triples of `H[X]`, one from each reversal pair, are

`abc, bca, cab, zba, azb, baz, acz, cza, zac, zcb, bzc, cbz`.

Then for every `d in V(H)-X`, the five-set `X union {d}` has a Hamilton tight path in which `d` is one position from an endpoint.

**Proof.** Write `uvw` for the assertion that `(u,v,w)` is tight. Assume for contradiction that no Hamilton tight path on `X union {d}` places `d` one position from an endpoint.

Exactly one of `dab` and `bad` is tight. We treat the two cases separately. In each row below, two consecutive triples of the displayed five-vertex order are tight. Since the order is not Hamiltonian, its third consecutive triple is non-tight, and boundary antisymmetry gives the triple in the last column.

If `dab` is tight, the following implications hold successively:

| tight triples | five-vertex order | forced tight triple |
| --- | --- | --- |
| `dab, abc` | `z d a b c` | `adz` |
| `adz, zcb` | `a d z c b` | `czd` |
| `acz, czd` | `a c z d b` | `bdz` |
| `cab, bdz` | `c a b d z` | `dba` |
| `dba, baz` | `c d b a z` | `bdc` |
| `azb, bdc` | `a z b d c` | `dbz` |
| `dbz, bzc` | `a d b z c` | `bda` |
| `bda, acz` | `b d a c z` | `cad` |

Now `bca`, `cad`, and `adz` are all tight, so

`(b,c,a,d,z)`

is a Hamilton tight path, a contradiction.

If `bad` is tight, the analogous explicit chain is

| tight triples | five-vertex order | forced tight triple |
| --- | --- | --- |
| `zba, bad` | `z b a d c` | `cda` |
| `bzc, cda` | `b z c d a` | `dcz` |
| `dcz, cza` | `b d c z a` | `cdb` |
| `cdb, baz` | `c d b a z` | `abd` |
| `cab, abd` | `c a b d z` | `zdb` |
| `zdb, bca` | `z d b c a` | `cbd` |
| `zcb, cbd` | `z c b d a` | `adb` |
| `cza, adb` | `c z a d b` | `daz` |

Now `cda`, `daz`, and `azb` are all tight, so

`(c,d,a,z,b)`

is a Hamilton tight path, again a contradiction.

Every five-vertex order displayed in the two tables, as well as the final path in each case, places `d` in position `1` or `3` when positions are numbered `0,...,4`. ∎

## 3. A non-Hamiltonian five-set over a non-Hamiltonian edge-ordered four-set

Let `H` be a boundary tournament and let `X subseteq V(H)` have four vertices. Suppose an edge order on the complete graph `K_X` represents `H[X]`, in the sense that for all distinct `u,v,w in X`,

`(u,v,w)` is tight in `H` if and only if `uv<vw`.

Assume `K_X` has no increasing Hamilton path. By `the earlier small-set results` the matching-block classification above, its three opposite-edge perfect matchings occur in strict blocks. Write

`M_low < M_mid < M_high`

when every edge of `M_low` precedes every edge of `M_mid`, and every edge of `M_mid` precedes every edge of `M_high`.

Let `d in V(H)-X`. For an edge `{u,v}` of `X`, call `{u,v}`

- **outgoing from `d`** if `(d,u,v)` and `(d,v,u)` are both tight;
- **incoming to `d`** if `(u,v,d)` and `(v,u,d)` are both tight.

Assume `H[X union {d}]` has no Hamilton tight path.

### 3.1 Extreme matching edges

At least one edge of `M_high` is outgoing from `d`, and at least one edge of `M_low` is incoming to `d`.

No edge of `M_high` is incoming to `d`, and no edge of `M_low` is outgoing from `d`.

**Proof.** Normalize

`M_low={{t,r},{l,s}}`,
`M_mid={{t,s},{l,r}}`,
`M_high={{t,l},{r,s}}`.

Suppose neither edge of `M_high` is outgoing from `d`. For `{t,l}`, at least one of `ltd,tld` is tight; for `{r,s}`, at least one of `srd,rsd` is tight. The four possibilities give contradictions as follows:

| tight triples | if this were tight | Hamilton path | forced reverse | Hamilton path |
| --- | --- | --- | --- | --- |
| `ltd, srd` | `rdt` | `l s r d t` | `tdr` | `s l t d r` |
| `ltd, rsd` | `sdt` | `l r s d t` | `tds` | `r l t d s` |
| `tld, srd` | `rdl` | `t s r d l` | `ldr` | `s t l d r` |
| `tld, rsd` | `sdl` | `t r s d l` | `lds` | `r t l d s` |

In each row the first displayed Hamilton path uses the two assumed mixed triples and one tight triple inside `X`. Since that path cannot exist, the middle mixed triple is non-tight and its reverse in the fourth column is tight; the last displayed order is then Hamiltonian. Thus some edge of `M_high` is outgoing.

Now suppose neither edge of `M_low` is incoming to `d`. For `{t,r}`, at least one of `drt,dtr` is tight; for `{l,s}`, at least one of `dsl,dls` is tight. Again the four possibilities are exhaustive:

| tight triples | if this were tight | Hamilton path | forced reverse | Hamilton path |
| --- | --- | --- | --- | --- |
| `drt, dsl` | `rds` | `r d s l t` | `sdr` | `s d r t l` |
| `drt, dls` | `ldr` | `l d r t s` | `rdl` | `r d l s t` |
| `dtr, dsl` | `tds` | `t d s l r` | `sdt` | `s d t r l` |
| `dtr, dls` | `tdl` | `t d l s r` | `ldt` | `l d t r s` |

Thus some edge of `M_low` is incoming.

For the forbidden directions, normalize instead

`M_low={ab,cz}`, `M_mid={ac,bz}`, `M_high={bc,az}`.

Suppose first that the high edge `bc` is incoming to `d`, so `bcd,cbd` are tight. The following five non-Hamiltonian candidate orders force the displayed reverses in sequence:

| tight triples | five-vertex order | forced tight triple |
| --- | --- | --- |
| `abc, bcd` | `a b c d z` | `zdc` |
| `abz, zdc` | `a b z d c` | `dzb` |
| `dzb, zbc` | `a d z b c` | `zda` |
| `zcb, cbd` | `z c b d a` | `adb` |
| `zca, adb` | `z c a d b` | `dac` |

Then `zda,dac,acb` are tight, so `(z,d,a,c,b)` is Hamiltonian, a contradiction. The permutation exchanging `a` with `c` and `b` with `z` preserves all three matching blocks and exchanges the two edges of `M_high`, so neither high edge can be incoming.

Suppose next that the low edge `ab` is outgoing from `d`, so `dab,dba` are tight. The corresponding forcing chain is

| tight triples | five-vertex order | forced tight triple |
| --- | --- | --- |
| `dba, baz` | `c d b a z` | `bdc` |
| `bdc, caz` | `b d c a z` | `acd` |
| `bac, acd` | `b a c d z` | `zdc` |
| `abz, zdc` | `a b z d c` | `dzb` |
| `dzb, zbc` | `a d z b c` | `zda` |

Then `zda,dab,abc` are tight, so `(z,d,a,b,c)` is Hamiltonian. The same permutation `(a c)(b z)` exchanges the two edges of `M_low`, so no low edge is outgoing. ∎

### 3.2 The middle matching alternates

Continue with

`M_low={{t,r},{l,s}}`,
`M_mid={{t,s},{l,r}}`,
`M_high={{t,l},{r,s}}`.

Suppose the high edge `{t,l}` is outgoing from `d` and the low edge `{t,r}` is incoming to `d`. Let `s` be the fourth vertex. Then exactly one of the two middle edges `{t,s}`, `{l,r}` is outgoing from `d`, and the other is incoming to `d`.

**Proof.** Put

`A=[(d,t,s) is tight]`, `B=[(d,s,t) is tight]`,
`C=[(d,r,l) is tight]`, `D=[(d,l,r) is tight]`.

The block order gives the tight triples

`rts, trl, lrs, lst, tsr, rlt, slr, stl`.

We prove the four implications explicitly.

**`A=>B`.** Suppose `A` holds and `B` fails. Then `tsd` is tight. If `sdl` were tight, `(r,t,s,d,l)` would be Hamiltonian, so `lds` is tight. If `rld` were tight, `(t,r,l,d,s)` would be Hamiltonian, so `D=dlr` is tight. If `tdl` were tight, `(t,d,l,r,s)` would be Hamiltonian, so `ldt` is tight. But now `(l,d,t,s,r)` is Hamiltonian, using `ldt`, `A=dts`, and `tsr`. Thus `A=>B`.

**`B=>A`.** Suppose `B` holds and `A` fails. Then `std` is tight. If `tdr` were tight, `(l,s,t,d,r)` would be Hamiltonian, so `rdt` is tight. If `lrd` were tight, `(s,l,r,d,t)` would be Hamiltonian, so `C=drl` is tight. If `sdr` were tight, `(s,d,r,l,t)` would be Hamiltonian, so `rds` is tight. But then `(r,d,s,t,l)` is Hamiltonian, using `rds`, `B=dst`, and `stl`. Thus `B=>A`.

**`C=>D`.** Suppose `C` holds and `D` fails. Then `rld` is tight. If `sdr` were tight, `(s,d,r,l,t)` would be Hamiltonian, so `rds` is tight. If `dst` were tight, `(r,d,s,t,l)` would be Hamiltonian, so `tsd` is tight. If `sdl` were tight, `(r,t,s,d,l)` would be Hamiltonian, so `lds` is tight. But then `(t,r,l,d,s)` is Hamiltonian, using `trl`, `rld`, and `lds`. Thus `C=>D`.

**`D=>C`.** Suppose `D` holds and `C` fails. Then `lrd` is tight. If `tdl` were tight, `(t,d,l,r,s)` would be Hamiltonian, so `ldt` is tight. If `dts` were tight, `(l,d,t,s,r)` would be Hamiltonian, so `std` is tight. If `tdr` were tight, `(l,s,t,d,r)` would be Hamiltonian, so `rdt` is tight. But then `(s,l,r,d,t)` is Hamiltonian, using `slr`, `lrd`, and `rdt`. Thus `D=>C`.

Therefore `A=B` and `C=D`. If both common values were `0`, then `std` and `lrd` would be tight. Non-Hamiltonicity of `(l,s,t,d,r)` forces `tdr` to be non-tight, hence `rdt` is tight; then `(s,l,r,d,t)` is Hamiltonian. If both common values were `1`, then `B=D=1`; non-Hamiltonicity of `(r,d,s,t,l)` forces `rds` to be non-tight, hence `sdr` is tight; then `(s,d,r,l,t)` is Hamiltonian.

Thus the two common values differ. If `A=B=1`, the middle edge `{t,s}` is outgoing from `d`; if `A=B=0`, boundary antisymmetry makes both `tsd,std` tight, so `{t,s}` is incoming. The same statement holds for `{l,r}` using `C=D`, and the two directions are opposite. ∎

### 3.3 An ordered exterior edge extending in both directions forces a Hamilton P5 or P6

Normalize the matching blocks as

`M_low={ab,cz}`, `M_mid={ac,bz}`, `M_high={bc,az}`.

Let `u,v` be distinct vertices of `V(H)-X`. Suppose that for every `x in X`, both

`(x,u,v)` and `(u,v,x)`

are tight. Then either `H[X union {u}]` has a Hamilton tight path or `H[X union {u,v}]` has a Hamilton tight path.

**Proof.** The block order gives the tight triples

`(b,a,c)`, `(c,z,b)`, `(c,a,z)`, `(b,z,a)`.

Assume for contradiction that neither a Hamilton P5 on `X union {u}` nor a Hamilton P6 on `X union {u,v}` exists.

Since `(c,u,v)` and `(u,v,z)` are tight, the path

`(b,a,c,u,v,z)`

forces `(a,c,u)` to be non-tight, so `(u,c,a)` is tight. Similarly, from `(b,u,v)` and `(u,v,a)`, failure of

`(c,z,b,u,v,a)`

forces `(u,b,z)` tight.

Now in `X union {u}`, failure of `(b,u,c,a,z)` forces `(c,u,b)` tight. But then

`(c,u,b,z,a)`

is a Hamilton P5, contradiction. ∎

## 4. Three of the five four-subsets of an edge-ordered K5 are Hamiltonian

Every edge-ordered `K_5` has at least three vertex deletions whose remaining four vertices admit an increasing Hamilton path. Equivalently, at most two of its five induced `K_4`s are non-Hamiltonian.

Consequently, if `h_4(r)` is the number of four-subsets of an edge-ordered `K_r`, `r>=5`, that admit an increasing Hamilton path, then

`h_4(r) >= (3/5) binom(r,4)`.

**Proof.** In a non-Hamiltonian edge-ordered `K_4`, `the earlier small-set results` the matching-block classification above says the three opposite-edge perfect matchings occur in strict blocks. Hence for adjacent edges `e,f`, comparison is preserved on passing to their opposite edges `e*,f*`:

`e<f` if and only if `e*<f*`.

Suppose an edge-ordered `K_5` on `{a,b,c,d,e}` had three non-Hamiltonian vertex-deleted `K_4`s. Relabel so the bad four-sets are obtained by deleting `a,b,c`.

In `{b,c,d,e}`,

`bd<be` iff `ce<cd`.

In `{a,c,d,e}`,

`ce<cd` iff `ad<ae`.

In `{a,b,d,e}`,

`ad<ae` iff `be<bd`.

Chaining gives `bd<be` if and only if `be<bd`, impossible. Thus at most two four-subsets are non-Hamiltonian.

For the density statement, count pairs `(X,Y)` where `X` is a Hamiltonian four-set and `Y` is a five-set containing it. Every five-set contributes at least three such pairs, while every four-set lies in exactly `r-4` five-sets. Hence

`(r-4)h_4(r) >= 3 binom(r,5)`,

which simplifies to the displayed bound. ∎


