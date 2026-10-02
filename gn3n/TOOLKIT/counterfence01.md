# Reusable counterexamples to tempting universal principles

## Statement

Exact constructions rule out tempting universal shortcuts in defect compression, exchange, endpoint extension, common-middle synchronization, and bounded-refinement arguments. In particular, even a common-middle square with two simultaneous four-endpoint barrier vertices is locally consistent, so closure needs additional global path-cover information.

## Body

# Reusable counterexamples and failed universal principles

There exists a boundary tournament on vertex set

`{0,1,2,3,4,5,6}`

whose maximum tight-path order is exactly five.

In particular, **all seven six-vertex induced subtournaments are non-Hamiltonian**.

## Exact encoding

Order the independent reversal-pair variables lexicographically by triples

`(m,u,w)`

with

`0<=m<=6`,
`0<=u<w<=6`,
`u,w != m`.

For such a variable, bit `1` means

`(u,m,w)`

is tight, while bit `0` means its reverse

`(w,m,u)`

is tight.

There are 105 variables. Pad the bit word on the left by three zero bits to a multiple of four. The resulting 27-digit hexadecimal encoding is

`0008400fc0343bf45faff90ddb8`.

## Exact verification

Direct exhaustive verification checks every vertex order on every six-subset.

There are seven six-subsets and

`6!=720`

orders per six-subset, hence

`7*720=5040`

candidate Hamilton six-paths.

None is tight.

The five-vertex sequence

`(3,2,4,0,1)`

is a tight path, so the maximum tight-path order is exactly five.

A seven-vertex Hamilton path is also impossible, since any six consecutive vertices of such a path would form a Hamilton path on their six-set. Thus the full seven-set is non-Hamiltonian as well. ∎

## Consequence

There is no universal local theorem asserting that every seven-vertex boundary tournament contains a Hamiltonian six-subset.

Hence the tempting order-eleven density shortcut fails: one cannot rule out a longest-path bound of five merely by applying a putative `7 -> 6` Hamiltonian-subset theorem.

This does not challenge the grand conjecture. It only fences off a local-density route; global no-trapping arguments must continue to use complementary support structure or global reconfiguration.

---

Consider the edge-ordered complete graph on
`z,a,b,x,d,e,f`
with edges increasing in the order

`de < ef < df < xf < xe < xd < bf < be < bd < bx < af < ae < ad < ax < zf < zx < za < ab < ze < zd < zb`.

Let the associated boundary tournament declare `(r,s,t)` tight exactly when
`rs < st`.

Then the displayed permutation
`(z,a,b,x,d,e,f)`
has defect centers exactly at `b,x,d`, hence defect span three:

- `(z,a,b)` is tight;
- `(a,b,x)` is non-tight;
- `(b,x,d)` is non-tight;
- `(x,d,e)` is non-tight;
- `(d,e,f)` is tight.

Now keep `z` first and `f` last, and arbitrarily permute the entire five-vertex join window
`{a,b,x,d,e}`.
For every one of the `5!=120` permutations `sigma`, the seven-vertex order
`(z,sigma,f)`
has defect span at least three.

The distribution is:

- 2 orders have span exactly 3;
- 14 orders have span 4;
- 104 orders have span 5.

Thus even arbitrary reordering of the full five-vertex defect neighborhood, while retaining only the two exterior vertices, does not universally compress a canonical span-three state.

Nevertheless the same edge-ordered tournament is Hamiltonian. For example
`(x,f,b,d,a,z,e)`
is increasing. Hence the obstruction is specifically local: a successful repair may require moving vertices outside the immediate five-window.

## Exact bounded verification

For each of the 120 orders `(z,sigma,f)`, inspect its five consecutive triples and compute the span from the first non-tight center to the last. Direct evaluation in the displayed edge order gives the distribution above.

The edge order itself is an independently checkable certificate; no solver certificate is needed to verify the claim. ∎

This rules out a natural local version of the defect-compression defect-compression program. Any universal proof must permit defect transport or repartition involving vertices beyond the immediate five-vertex join window.

---

There exists a boundary tournament on vertices

{0,1,2,3,4,5,6}

such that

A=(0,1,2,3,4,5)

is a tight Hamilton path, but for every a in V(A), the six-set

(V(A)-{a}) union {6}

is non-Hamiltonian.

## Exact encoding

Order the independent reversal-pair variables lexicographically by triples

(m,u,w),

where

0<=m<=6,
0<=u<w<=6,
u,w != m.

For the variable (m,u,w), bit 1 means that

(u,m,w)

is tight, while bit 0 means its reverse

(w,m,u)

is tight.

There are 105 such variables. Padding the bit word on the left to a whole number of hexadecimal digits, the tournament is encoded by

0bb1ffe23ff98061f812c002204

with the first bit most significant.

Direct exhaustive verification gives:

1. (0,1,2,3,4,5) is tight.
2. For every a in {0,1,2,3,4,5}, the induced tournament on
   ({0,1,2,3,4,5}-{a}) union {6}
   has no Hamilton tight path.

Each non-Hamiltonicity assertion requires checking only 6!=720 orders.

## Consequence

Thus there is no universal positive lower bound of even one on the number of Hamiltonian one-vertex replacements

(A-{a}) union {y}

when A is a Hamiltonian set of order six and y is outside A.

In particular, the exchange-matrix proof of the order-ten exchange theorem in the extremal module cannot scale to arbitrary support size by proving that every column contains a positive, let alone linear, number of X-good one-vertex replacements. Its order-ten success genuinely uses the special five/six-vertex density furnished by four-of-six.

This does not challenge equitable two-coverability or the grand two-cover conjecture. It is a fence on one attempted proof mechanism: beyond the five-set regime, a successful support-exchange argument must use larger exchange shells, complementary structure, or global path information rather than a universal one-replacement density bound. ∎

---

Let
`T={a,b,c}`
and let `q_0,q_1,q_2,q_3` be four further vertices.

There is an edge order on the complete graph on these seven vertices for which:
- `(q_0,q_1,q_2,q_3)` is an increasing path;
- `T union {q_0,q_2}` has an increasing Hamilton path;
- `T union {q_1,q_3}` has an increasing Hamilton path;
- the full seven-vertex edge-ordered graph has no increasing Hamilton path.

One such edge order, from least to greatest, is

`q_0q_1 < cq_2 < cq_0 < q_0q_2 < cq_3 < q_1q_3 < bq_2 < bc < cq_1 < bq_0 < aq_3 < bq_3 < bq_1 < aq_2 < q_1q_2 < aq_0 < q_0q_3 < q_2q_3 < ab < aq_1 < ac`.

The two required Hamilton paths are
`(c,q_2,q_0,b,a)`
on `T union {q_0,q_2}` and
`(q_3,q_1,b,a,c)`
on `T union {q_1,q_3}`.

## Proof

The displayed orders are visibly increasing in the listed edge order:
- `q_0q_1 < q_1q_2 < q_2q_3`;
- `cq_2 < q_2q_0 < q_0b < ba`;
- `q_3q_1 < q_1b < ba < ac`.

For completeness, non-Hamiltonicity of the seven-set is the following bounded exhaustive check over `7!=5040` vertex orders.

```python
from itertools import permutations

V = ("a","b","c","q0","q1","q2","q3")
E = [
    ("q0","q1"), ("c","q2"), ("c","q0"), ("q0","q2"),
    ("c","q3"), ("q1","q3"), ("b","q2"), ("b","c"),
    ("c","q1"), ("b","q0"), ("a","q3"), ("b","q3"),
    ("b","q1"), ("a","q2"), ("q1","q2"), ("a","q0"),
    ("q0","q3"), ("q2","q3"), ("a","b"), ("a","q1"),
    ("a","c"),
]
rank = {frozenset(e): i for i,e in enumerate(E)}

def increasing(p):
    e = [frozenset((p[i],p[i+1])) for i in range(len(p)-1)]
    return all(rank[e[i]] < rank[e[i+1]] for i in range(len(e)-1))

assert increasing(("q0","q1","q2","q3"))
assert increasing(("c","q2","q0","b","a"))
assert increasing(("q3","q1","b","a","c"))
assert sum(increasing(p) for p in permutations(V)) == 0
```

By the comparison representation, this edge order defines a boundary tournament with the same tight-path conclusions.
∎

Thus the common-exterior-set conclusion supplied by the seven-set density theorem cannot by itself be closed merely by proving Hamiltonicity of the two alternating five-sets. Any successful shifted-cut argument must use additional strict-alternation information, such as the full extremal pattern of the overlapping six-sets, the distinguished fixed non-Hamiltonian four-set, or the endpoint extension data.

---

Let the vertices be
`b_0,b_1,b_2,b_3,x,y`.
Order the fifteen edges of the complete graph from least to greatest as

`b_0b_3 < b_2x < b_2y < b_3x < b_0b_1 < b_1b_2 < b_3y < xy < b_0x < b_1b_3 < b_0b_2 < b_0y < b_2b_3 < b_1x < b_1y`.

Then:
- `B=(b_0,b_1,b_2,b_3)` is an increasing path;
- the five-set `V(B) union {x}` has no increasing Hamilton path;
- the five-set `V(B) union {y}` has no increasing Hamilton path;
- the full six-set `V(B) union {x,y}` has no increasing Hamilton path.

Thus a non-Hamiltonian union of two disjoint paths need not become Hamiltonian after adjoining either endpoint of the second path to the first, even when the first path has order four and the second path has order two.

## Verification

The prescribed path is increasing because
`b_0b_1 < b_1b_2 < b_2b_3`
in the displayed edge order.

The three non-Hamiltonicity assertions are the following bounded exhaustive checks over `5!=120`, `5!=120`, and `6!=720` vertex orders respectively:

```python
from itertools import permutations

V = ('b0','b1','b2','b3','x','y')
E = [
    ('b0','b3'), ('b2','x'), ('b2','y'), ('b3','x'),
    ('b0','b1'), ('b1','b2'), ('b3','y'), ('x','y'),
    ('b0','x'), ('b1','b3'), ('b0','b2'), ('b0','y'),
    ('b2','b3'), ('b1','x'), ('b1','y'),
]
rank = {frozenset(e): i for i,e in enumerate(E)}

def increasing(p):
    e = [frozenset((p[i],p[i+1])) for i in range(len(p)-1)]
    return all(rank[e[i]] < rank[e[i+1]] for i in range(len(e)-1))

assert increasing(('b0','b1','b2','b3'))
assert not any(increasing(p) for p in permutations(('b0','b1','b2','b3','x')))
assert not any(increasing(p) for p in permutations(('b0','b1','b2','b3','y')))
assert not any(increasing(p) for p in permutations(V))
```

By the comparison representation this edge order defines a boundary tournament with the same tight-path conclusions. ∎

This rules out the simplest attempted closure of the non-singleton branch arising from `the non-singleton endpoint-extension branch`: endpoint Hamiltonization of the larger path does not follow from the induced two-path geometry alone. Any successful proof must use additional information from the ambient extremal three-cover or from interaction with the third path.

---

There is an edge-ordered complete graph on vertices `0,1,2,3,4,5,6` with edge order

`46 < 01 < 26 < 15 < 03 < 04 < 06 < 35 < 13 < 05 < 56 < 12 < 23 < 34 < 14 < 02 < 16 < 24 < 36 < 25 < 45`.

Let `P=(0,1,2,3,4,5)` and let `gamma=6`. Since
`01 < 12 < 23 < 34 < 45`,
`P` is an increasing Hamilton path on `{0,1,2,3,4,5}`.

For the boundary tournament represented by this edge order:

- the full seven-vertex set has no increasing Hamilton path;
- for every `z in {0,1,2,3,4,5}`, the six-set
  `({0,1,2,3,4,5}-{z}) union {6}`
  has no increasing Hamilton path.

Thus the universal one-vertex replacement-failure conclusion in the non-fallback branch of `the strict-alternation replacement-failure branch`, considered without the simultaneous fixed-four-set hypotheses, is consistent at the minimum order allowed by `the minimum-order bound for the non-fallback strict-alternation branch`.

## Exact finite verification

The displayed edge order determines every comparison. Exhaustive verification checks the `7!=5040` vertex orders of the full set and, for each of the six deletions `z`, the `6!=720` vertex orders of the corresponding six-set: `9360` candidate Hamilton orders in total. None is increasing.

The maximum increasing-path orders are:

| support | maximum increasing-path order |
| --- | ---: |
| all seven vertices | 6 |
| delete `0` | 5 |
| delete `1` | 5 |
| delete `2` | 5 |
| delete `3` | 5 |
| delete `4` | 5 |
| delete `5` | 5 |

In particular this witness does not challenge the full strict-alternation hypothesis; it isolates which the full strict-alternation hypothesis data are essential. Any contradiction in the strict-alternation residue must also use the common five-set structure, for example that one fixed non-Hamiltonian four-set `A` has `A union {z}` Hamiltonian for every `z in V(P)`, or the distance-two complementary supports from `the repeated-middle-defect complementary-support theorem`.

---

The statement `the three-sandwich-vertices claim` is false.

Let the seven vertices be
`a,b,c,d,p,q,r`.
Give the complete graph the strict edge order

`ap < bd < qr < ab < cr < ac < dr < pq < ad < pr < bp < aq < cp < ar < dp < cq < bq < bc < dq < cd < br`.

Let `H` be the boundary tournament represented by this edge order: `(u,v,w)` is tight exactly when `uv<vw`.

Then `(a,b,c,d)` is a tight path, and for every `x in {p,q,r}` both `(a,x,b)` and `(c,x,d)` are tight, but `H` has no Hamilton tight path.

## Verification of the hypotheses

`ab < bc < cd`, so `(a,b,c,d)` is tight.

For `p`, `ap < bp` and `cp < dp`; for `q`, `aq < bq` and `cq < dq`; for `r`, `ar < br` and `cr < dr`. Hence every `x in {p,q,r}` satisfies `(a,x,b)` and `(c,x,d)`.

## Verification of non-Hamiltonicity

Every increasing six-vertex path is listed below. For each path, `(j,k)` gives the rank `j` of its final ordinary edge and the rank `k` of the edge from its final vertex to the omitted seventh vertex:

`abpcqd : (19,7)`
`apbqdc : (20,5)`
`apcqbr : (21,7)`
`apqbcd : (20,7)`
`apqcbr : (21,7)`
`bacpdq : (19,3)`
`bdrpcq : (16,12)`
`crdaqb : (17,11)`
`crpbqd : (19,9)`
`daqcbr : (21,10)`
`drpcqb : (17,4)`
`pabqdc : (20,5)`
`pacqbr : (21,7)`
`paqbcd : (20,7)`
`paqcbr : (21,7)`
`qrcadp : (15,11)`
`qrpbcd : (20,9)`
`rdaqbc : (18,13)`
`rdaqcb : (18,11)`
`rpbqdc : (20,6)`
`rqpbcd : (20,9)`.

In every row the edge to the omitted vertex has smaller rank than the final edge. Therefore no increasing six-vertex path extends at its right end to an increasing Hamilton path. Every increasing Hamilton path would have an increasing initial six-vertex segment, so none exists. ∎

## Consequences for current live research

The proof of `the three-sandwich-vertices claim` repeatedly treats cyclic permutations of a tight ordered triple as tight. This is invalid: `(a,x,b)` means `ax<xb`, whereas its cyclic permutation `(x,b,a)` means `xb<ba`.

The pending results `a dependent sandwich argument` and `a dependent endpoint-deletion argument` use the same invalid inference. In particular, non-tightness of `(x,a,b)` gives only the reverse `(b,a,x)`, not `(a,x,b)`. Their displayed proofs therefore do not establish their statements.

---

There exists a non-Hamiltonian edge-ordered complete graph on
`F={0,1,2,3,4}`
with two vertices `ell=2`, `r=3` such that both `F-{ell}` and `F-{r}` have increasing Hamilton paths, but the following synchronization fails:

- for every increasing Hamilton path `A_ell` on `F-{ell}` for which deleting `r` leaves an increasing path on `F-{ell,r}`,
- and every increasing Hamilton path `A_r` on `F-{r}` for which deleting `ell` leaves an increasing path on `F-{ell,r}`,

the two surviving three-vertex paths have no common directed consecutive edge.

Thus even for two Hamiltonian-good deletions of a non-Hamiltonian edge-ordered `K_5`, prescribed removability on both sides does not force the residual three-paths to share an order or even a directed edge.

## Proof

Order the ten edges by
`12 < 01 < 34 < 23 < 04 < 03 < 13 < 24 < 02 < 14`.

First verify that this edge-ordered `K_5` is non-Hamiltonian. Its increasing four-vertex paths are exactly

`(1,2,3,0)`, `(2,1,0,3)`,
`(1,0,4,2)`, `(2,1,0,4)`,
`(0,3,1,4)`, `(4,0,3,1)`,
`(3,4,0,2)`, `(3,4,2,0)`,
`(4,3,0,2)`, `(4,3,2,0)`,
`(2,3,1,4)`, `(3,2,4,1)`.

For these paths, respectively, the rank of the final edge and the rank of the edge from the final vertex to the omitted fifth vertex are

`(6,5)`, `(6,3)`,
`(8,4)`, `(5,3)`,
`(10,8)`, `(7,1)`,
`(9,1)`, `(9,2)`,
`(9,1)`, `(9,2)`,
`(10,5)`, `(10,2)`.

In every case the edge to the omitted vertex has smaller rank than the final edge, so no increasing four-path can be extended at its right end. Every increasing Hamilton path would have an increasing initial four-vertex segment, so no increasing Hamilton path exists.

Now delete `ell=2`. The increasing Hamilton paths on `{0,1,3,4}` are exactly
`(0,3,1,4)` and `(4,0,3,1)`.
Deleting `r=3` from the first leaves `(0,1,4)`, which is increasing because `01<14`. Deleting `3` from the second leaves `(4,0,1)`, which is not increasing because `04>01`. Hence the only removable residual three-path on the left is
`(0,1,4)`.

Delete instead `r=3`. The increasing Hamilton paths on `{0,1,2,4}` are exactly
`(1,0,4,2)` and `(2,1,0,4)`.
Deleting `ell=2` leaves `(1,0,4)` in either case, and this is increasing because `01<04`. Hence the only removable residual three-path on the right is
`(1,0,4)`.

The directed consecutive edges of `(0,1,4)` are
`0->1`, `1->4`,
whereas those of `(1,0,4)` are
`1->0`, `0->4`.
They have no directed consecutive edge in common. ∎

---

Take vertices `0,1,2,3,4,5`, put `M=(0,1,2,3)`, `u=4`, `v=5`, and order the fifteen ordinary edges strictly as

`03 < 24 < 45 < 01 < 02 < 34 < 14 < 04 < 25 < 15 < 12 < 35 < 05 < 13 < 23`.

The displayed path `M` is increasing because `01 < 12 < 23`.

For each of `x=4,5`, direct inspection of the five possible insertion positions in `(0,1,2,3)` shows that the resulting five-vertex order is not increasing. Hence both exterior vertices are noninsertable into the displayed Hamilton path `M`.

An exhaustive check of the `6! = 720` vertex orders shows that none is increasing, so the full six-set is non-Hamiltonian. The check is finite and exact: for each vertex order one compares its five consecutive ordinary edges against the displayed strict edge order.

Therefore the abstract implication `two distinct vertices noninsertable into the same Hamilton path => their joint enlargement is Hamiltonian` is false even in the edge-orderable subclass of boundary tournaments. ∎

The successful-exchange attack must use the additional five-set deletion/side-extension/cross-support information carried by the two exterior vertices, not merely their common-middle noninsertability.

---

Consider the edge-ordered complete graph on vertices `0,1,2,3,4,5,6,7,8` with strict edge order

`37 < 15 < 28 < 03 < 01 < 46 < 14 < 26 < 18 < 35 < 34 < 08 < 67 < 04 < 58 < 16 < 13 < 12 < 57 < 48 < 06 < 02 < 38 < 47 < 17 < 36 < 56 < 23 < 68 < 27 < 78 < 24 < 05 < 45 < 25 < 07`.

Let `Y={0,1,2,3}`, `F={4,5,6,7,8}`, and `Q=(0,1,2,3)`.

The order `Q` is increasing because `01 < 12 < 23`. The induced edge order on `F` is non-Hamiltonian; exhaustive inspection of its `5!` vertex orders finds no increasing Hamilton path.

The endpoint-deletion subtournaments are non-Hamiltonian, and they have the inherited-order exact two-covers
`(4,1,2,3) | (5,6,8,7)`
and
`(0,1,2,4) | (5,6,8,7)`.
The displayed paths are increasing since respectively `14 < 12 < 23`, `56 < 68 < 78`, and `01 < 12 < 24`.

Now keep `Q` as one indivisible ordered block and treat the five vertices of `F` as singleton blocks. A complete subset dynamic program over these six blocks, with state consisting of the used block set and the final two vertices of the current path, finds no partition of the six blocks into at most two increasing concatenations. Thus no zero-cut block certificate exists.

After cutting the first edge `01`, however, the two inherited-order `Y`-blocks are `(0)` and `(1,2,3)`, and
`(4,6,5,0,7) | (8,1,2,3)`
is an increasing spanning two-cover. Indeed `46 < 56 < 05 < 07` and `18 < 12 < 23`.

Hence at least one internal cut of the displayed Hamilton order can be genuinely necessary under the relaxed inherited-order hypotheses used by the the inherited-order block-concatenation program moonshot. This example does not test or assume `pc(K)>2`, and therefore does not bear against the five-complement theorem itself. ∎

Computational note: the zero-cut nonexistence check is finite over six fixed blocks and uses no solver; each state records only the used block subset and the last two vertices, which exactly determine whether another fixed block may be appended.

---

## 1. Exact terminal data for concatenating fixed paths

Let H be a finite boundary tournament. Let B_1,...,B_b be pairwise vertex-disjoint nonempty tight paths whose supports partition V(H). Their internal orders are fixed. For each B_i retain its first two and last two vertices, taking their union when they overlap, and record min(|B_i|,4). Retain the truth value of every tight ordered triple on the retained vertices.

Then these data determine exactly which ordered concatenations of the whole blocks, using each block once in total, form a path cover of H with at most two components. No reversal, splitting, or interleaving of a block is allowed in this assertion.

In particular, let V(K)=Y disjoint-union F with |F|=5, let a,b be distinct vertices of Y, and let T be an exact two-path cover of K-{a,b}. Cut every ordinary edge of T between Y and F, and add singleton blocks (a),(b). There are at most fourteen blocks, and at most thirty-five vertices suffice for the terminal data: at most seven Y-blocks contribute four vertices each, F contributes at most five, and a,b contribute two. This is an exact finite test of the specified block concatenations, not a reduction of K to an induced boundary tournament on thirty-five vertices.

## Proof

A consecutive triple in a concatenation is either internal to one block, intersects two consecutive blocks, or meets three consecutive blocks. Internal triples are tight by hypothesis. In the two-block case its vertices lie in the last two positions of the first block and the first two positions of the second. In the three-block case the middle block is a singleton and the triple consists of the last vertex of the first block, that singleton, and the first vertex of the third. Every such triple is therefore present in the retained table. The truncated length records distinguish singleton, doubleton, tripleton, and longer blocks and determine which tests are required. Checking precisely these triples is both necessary and sufficient.

For the quantitative assertion, the F-blocks are disjoint nonempty subsets of F, so their number is at most five. In each component of T, the monochromatic blocks alternate; hence the number of Y-blocks is at most the number of F-blocks plus two, and is at most seven. Thus T has at most twelve blocks. Adding a,b yields at most fourteen, and retaining terminal vertices uses at most 4*7+5+2=35 vertices. Shortening a long block in an induced subgraph could create unverified internal triples; the finite test instead treats that block's already-tight internal order as fixed. ∎

## 2. No bounded common refinement from bounded monochromatic block counts

For every integer r>=3 there exists a boundary tournament H on {1,...,2r} with tight Hamilton paths
Q=(1,2,...,2r)
and
R=(2,4,...,2r,1,3,...,2r-1)
such that Q and R have no common ordinary edge. Consequently every common refinement into ordered path segments (even allowing reversal) has 2r singleton parts. The only sets contiguous in both orders are singletons and the whole vertex set; hence every proper partition into common contiguous supports also has 2r singleton parts. Both paths nevertheless consist of one monochromatic block relative to the partition with all these vertices on the same side.

## Proof

Declare every consecutive ordered triple of Q and every consecutive ordered triple of R tight. These prescriptions are consistent: a consecutive triple of Q has all its vertices in an interval of three consecutive integers. A triple of R lying within one parity subsequence has span four; a triple crossing the join 2r,1 has span at least five when r>=3. Thus no triple prescribed by R has the same underlying three-set as a triple prescribed by Q. Within either path, different consecutive triples have different underlying sets. No reversal pair receives conflicting prescriptions. Orient every remaining reversal pair arbitrarily to obtain H.

Every ordinary edge of Q joins integers differing by one. Every ordinary edge of R joins integers differing by two, except {2r,1}, whose difference is 2r-1>=5. The ordinary edge sets are disjoint.

Observe that an interval of consecutive integers which occurs contiguously in R either lies in one parity subsequence and hence is a singleton, or crosses the parity join. In the latter case it contains 1 and 2r, so if it is an interval in Q it must be the entire vertex set. Thus the only common interval supports are singletons and the whole set. In particular a proper common interval partition has only singletons. Moreover a common ordered path segment, even allowing its reversal, must be a singleton since the edge sets are disjoint. This proves both assertions about refinements. ∎

## Strategic scope

The fixed-block test is genuinely bounded. It does not prove that a successful concatenation exists, or that cutting at the original Y-F transitions is enough. Comparison with another Hamilton order can require arbitrarily many cuts. An order-disagreement witness is therefore not, by itself, a bounded augmentation certificate. Any finite classification must explicitly state which blocks stay intact, which new cuts are allowed, and how a successful certificate lifts to the original paths.

---

# Common-middle barriers are locally consistent

There exists a boundary tournament `J` on `V(J)={m_1,m_2,a,ell,c,r,x,y,z}`. Put `M=(m_1,m_2)`, `Lset={a,ell}`, `Rset={c,r}`, `T={x,y,z}`. It can satisfy simultaneously:
- every `(L,M,R)`, `L in Lset`, `R in Rset`, is tight;
- every complementary five-set is non-Hamiltonian;
- the same two vertices `y,z` are Hamiltonian-good deletions in all four complementary five-sets, while `x` is a non-Hamiltonian deletion in all four;
- for each `s in {y,z}`, `(m_1,a,s)`, `(m_1,ell,s)`, `(s,c,m_2)`, `(s,r,m_2)` are all tight.

## Proof

For each `L in Lset`, `R in Rset`, prescribe on `{L,R,x,y,z}` the edge order
`LR < yz < Lz < xy < Rx < Lx < Ry < Ly < Rz < xz`.
The four orders are compatible on overlaps: for fixed `L` the common restriction is `yz < Lz < xy < Lx < Ly < xz`; for fixed `R` it is `yz < xy < Rx < Ry < Rz < xz`; on `{x,y,z}` it is `yz < xy < xz`. Thus they define consistent reversal-pair orientations; assign uncovered reversal pairs arbitrarily.

For this generic five-set the increasing four-vertex paths are exactly
`(L,R,x,z)`, `(L,R,z,x)`, `(R,L,x,z)`, `(R,L,z,x)`, `(R,x,L,y)`, `(x,R,y,L)`, `(x,y,R,z)`, `(y,R,z,x)`, `(y,x,R,z)`, `(y,z,L,x)`, `(z,y,x,L)`, `(z,y,x,R)`.
For these paths, the pair `(rank of final edge, rank of edge to the omitted vertex)` is respectively
`(10,2)`, `(10,4)`, `(10,2)`, `(10,4)`, `(8,2)`, `(8,3)`, `(9,3)`, `(10,6)`, `(9,3)`, `(6,5)`, `(6,1)`, `(5,1)`.
So none extends to an increasing Hamilton path, and the five-set is non-Hamiltonian.

Deleting `x` leaves `LR < yz < Lz < Ry < Ly < Rz`, whose opposite-edge perfect matchings are the strict blocks `{LR,yz} < {Lz,Ry} < {Ly,Rz}`; hence that four-set is non-Hamiltonian. Deleting `y` leaves the increasing Hamilton path `(L,R,x,z)` because `LR < Rx < xz`. Deleting `z` leaves `(R,x,L,y)` because `Rx < Lx < Ly`. Thus `y,z` are good and `x` is bad for all four five-sets.

Adjoin `m_1,m_2`. Declare `(L,m_1,m_2)` tight for both `L`, and `(m_1,m_2,R)` tight for both `R`, giving all four common-middle paths. For `s in {y,z}`, declare `(m_1,L,s)` tight for both `L` and `(s,R,m_2)` tight for both `R`. These are new reversal pairs, so no conflict occurs. Assign all remaining reversal pairs arbitrarily. The resulting boundary tournament has every asserted property. ∎

## Research consequence

This does not assert `pc(J)>2`. It shows that even maximal local deletion multiplicity together with two simultaneous four-endpoint barrier vertices does not itself contradict the boundary-tournament axioms. Any codimension-five closure must use an additional global consequence of `pc(K)>2` or a repartition genuinely mixing the long and short supports.

## Metadata

- ID: counterfence01
- Kind: toolkit
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
