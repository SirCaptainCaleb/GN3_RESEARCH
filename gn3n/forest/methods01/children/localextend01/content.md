# Local Hamilton-extension and match-set calculus

## Statement

Bad extension pairs around a tight three-path are triangle-free; match-set and parallel-middle structure force local Hamilton paths; bad four-extensions and double-extenders give controlled five-vertex forcing; and bad five-sets admit strong opposite-deletion and repeated-defect cross-exterior Hamiltonicity conclusions.

## Body

# Local Hamilton-extension and match-set calculus

# Local Hamilton extension lemmas

Throughout this file, `H` is an arbitrary boundary tournament.

## 1. Bad extension pairs around a tight three-vertex path form a triangle-free graph

Let `P` be a tight path on three vertices, and let `X` be a set of `m>=3` vertices disjoint from `V(P)`. Define a graph `B_P(X)` on vertex set `X` by joining distinct `x,y` exactly when

`H[V(P) union {x,y}]`

has no Hamilton tight path.

Then `B_P(X)` is triangle-free. Consequently

`|E(B_P(X))| <= floor(m^2/4)`,

so at least

`binom(m,2)-floor(m^2/4)`

pairs `{x,y}` extend `P` to a Hamilton five-vertex induced subgraph. Equality in the upper bound occurs exactly when `B_P(X)` is a complete bipartite graph with part sizes `floor(m/2)` and `ceil(m/2)`.

**Proof.** For any three distinct `x,y,z in X`, `the small-order structure module` Section 5 says that at least one of

`V(P) union {x,y}`, `V(P) union {x,z}`, `V(P) union {y,z}`

has a Hamilton tight path. Hence `xy,xz,yz` cannot all be edges of `B_P(X)`, so the graph is triangle-free. Mantel's theorem gives the bound and its equality case. ∎



## 3. Two parallel middle vertices force a Hamilton four-path

Let `a,c,x,y` be four distinct vertices of a boundary tournament. If

`(a,x,c)` and `(a,y,c)`

are tight, then at least one of

`(a,x,c,y)`, `(a,y,c,x)`

is a tight Hamilton path on `{a,c,x,y}`.

**Proof.** Exactly one of `(x,c,y)` and `(y,c,x)` is tight. In the first case `(a,x,c,y)` is tight; in the second `(a,y,c,x)` is tight. ∎


# Match sets and parallel-middle forcing

## 1. Match sets relative to a fixed three-set

Fix a three-vertex set

`C={a,b,c}`

in a boundary tournament `H`, and let `E` be a set of vertices disjoint from `C`.

For `x in E` and `d in C`, write `C-{d}={u,v}` and choose the order `(u,v)` for which `(u,d,v)` is tight. Define

`d in M_C(x)`

if and only if `(u,x,v)` is tight.

This is well-defined: reversing `u,v` reverses both tested triples, so boundary antisymmetry preserves whether their tightness agrees.

Define a graph `Gamma_C` on `E` by joining distinct `x,y` when `H[C union {x,y}]` has a Hamilton tight path.

Then:

1. for every `d in C`, the set

   `E_d={x in E:d in M_C(x)}`

   is a clique of `Gamma_C`;
2. if `U subseteq E` is independent in `Gamma_C`, then the sets `M_C(x)`, `x in U`, are pairwise disjoint, and therefore

   `sum_{x in U}|M_C(x)|<=3`;
3. if `U={x,y,z}` is independent, then, after relabelling the vertices of `C` and the three exterior vertices, the triple of match sets is exactly one of

   `(emptyset,emptyset,emptyset)`,

   `({a},emptyset,emptyset)`,

   `({a,b},emptyset,emptyset)`,

   `({a},{b},emptyset)`,

   `({a,b,c},emptyset,emptyset)`,

   `({a,b},{c},emptyset)`,

   `({a},{b},{c})`.

**Proof.** Fix `d in C` and suppose `x,y in E_d`. With `u,v` ordered so that `(u,d,v)` is tight, the triples

`(u,d,v)`, `(u,x,v)`, `(u,y,v)`

are all tight. `the small-order structure module` Section 2 gives a Hamilton tight path on

`{u,v,d,x,y}=C union {x,y}`.

Thus `xy` is an edge of `Gamma_C`, proving that `E_d` is a clique.

Hence two vertices of an independent set cannot share a coordinate `d`, so their match sets are pairwise disjoint subsets of the three-element set `C`. This gives the sum bound.

For three exterior vertices, the possible multisets of sizes of three pairwise disjoint subsets of a three-element set are

`(0,0,0)`, `(1,0,0)`, `(2,0,0)`, `(1,1,0)`, `(3,0,0)`, `(2,1,0)`, `(1,1,1)`.

Relabelling the exterior vertices orders the three sizes, and relabelling `a,b,c` gives exactly the seven displayed representatives. ∎

## 2. Three parallel middle vertices admit a Hamilton five-path with an exterior endpoint

Let `H` be a boundary tournament, let `a,c,p,q,r` be distinct vertices, and suppose

`(a,p,c)`, `(a,q,c)`, `(a,r,c)`

are tight. Then `H[{a,c,p,q,r}]` has a Hamilton tight path with at least one endpoint in `{p,q,r}`.

In general one cannot prescribe in advance which of `p,q,r` is an endpoint.

**Proof.** `the small-order structure module` Section 2 gives some Hamilton tight path on the five vertices. If one endpoint lies in `{p,q,r}`, there is nothing to prove. Suppose instead that the endpoints are `a,c`. After relabelling `p,q,r` as `x,y,z`, the path is one of

`(a,x,y,z,c)`, `(c,x,y,z,a)`.

### Case 1: `(a,x,y,z,c)` is tight

Set

`alpha=[(a,y,z) is tight]`,
`beta=[(z,c,x) is tight]`,
`gamma=[(z,c,y) is tight]`,
`delta=[(c,y,x) is tight]`,
`epsilon=[(x,a,y) is tight]`,
`eta=[(x,a,z) is tight]`.

Consider the seven candidate paths

`a,y,z,c,x`,
`a,z,c,y,x`,
`x,a,y,c,z`,
`x,a,z,c,y`,
`y,a,x,c,z`,
`z,a,x,y,c`,
`z,y,a,x,c`.

Using the three hypotheses and the triples already supplied by `(a,x,y,z,c)`, these candidates are tight respectively under the conditions

`alpha and beta`,
`gamma and delta`,
`epsilon and not gamma`,
`eta and gamma`,
`not epsilon and not beta`,
`not eta and not delta`,
`not alpha and not epsilon`.

Assume all seven fail. Failure of the last condition gives `alpha or epsilon`. If `alpha` is false then `epsilon` is true. If `alpha` is true, failure of the first condition gives `beta` false, and failure of the fifth again gives `epsilon` true. Thus `epsilon` is true. Failure of the third condition gives `gamma` true; failure of the second gives `delta` false; failure of the sixth gives `eta` true. The fourth candidate is then tight, a contradiction.

### Case 2: `(c,x,y,z,a)` is tight

Use

`beta=[(z,c,x) is tight]`,
`gamma=[(z,c,y) is tight]`,
`epsilon=[(x,a,y) is tight]`,
`eta=[(x,a,z) is tight]`.

The five candidates

`a,z,c,x,y`,
`x,a,z,c,y`,
`y,z,a,x,c`,
`x,a,y,c,z`,
`y,a,x,c,z`

are tight respectively under the conditions

`beta`,
`eta and gamma`,
`not eta`,
`epsilon and not gamma`,
`not epsilon and not beta`.

If all fail, then successively `beta` is false, `eta` is true, `gamma` is false, and `epsilon` is false; the fifth candidate is then tight, a contradiction.

Thus some Hamilton five-path has an endpoint in `{p,q,r}`. ∎

### Non-prescribability

Take five vertices `a,c,p,q,r` and order the ten ordinary edges by

`pq < ar < ac < qr < ap < cp < pr < aq < cr < cq`.

Let tight triples be those whose two consecutive ordinary edges increase in this order. Then

`ap<cp`, `aq<cq`, `ar<cr`,

so `(a,p,c),(a,q,c),(a,r,c)` are tight. The Hamilton increasing paths are exactly

`(a,p,r,c,q)` and `(r,a,p,c,q)`.

Thus `p` is never an endpoint of a Hamilton tight path in this example. Relabelling `p,q,r` shows that no fixed middle vertex can be prescribed universally.

## 3. Four parallel middle vertices force a five-path

Let `H` be a boundary tournament, let `a,c` be distinct vertices, and let `S⊆V(H)-{a,c}` have order at least four. Suppose

`(a,s,c)`

is tight for every `s∈S`. Then there are distinct `x,y,z∈S` such that

`(x,a,y,c,z)`

is a tight path.

**Proof.** It is enough to prove the result for a four-element subset of `S`, so assume `|S|=4`. Define tournaments on `S` by

`x->_a y` iff `(x,a,y)` is tight,

`x->_c y` iff `(x,c,y)` is tight.

Suppose no distinct `x,y,z` satisfy `x->_a y->_c z`. If a vertex has indegree at least two in `->_a`, then it has outdegree zero in `->_c`; otherwise two of its `->_a` predecessors together with one `->_c` successor would give such a mixed chain.

The sum of indegrees in the four-vertex tournament `->_a` is six, so some vertex `y` has indegree at least two. Hence `y` has outdegree zero in `->_c`, so `y` is the unique `->_c` sink. Every other vertex has positive `->_c` outdegree and therefore `->_a` indegree at most one. The indegree sum then forces `y` to have `->_a` indegree three and each other vertex to have `->_a` indegree one. Thus `y` is also the `->_a` sink.

Choose `v!=y`. Since `y` is the `->_c` sink, `v->_c y`. The unique `->_a` predecessor `x` of `v` cannot be `y`, because `y` is the `->_a` sink. Hence `x->_a v->_c y`, a mixed chain on three distinct vertices, contradiction. Therefore such a mixed chain exists. Renaming its middle and last vertices as `y,z`, the triples `(x,a,y)`, `(a,y,c)`, `(y,c,z)` are tight, so `(x,a,y,c,z)` is tight. ∎


# Local five-vertex forcing

## 1. Two exterior vertices across adjacent positions of a tight path

### Proposition 1.1

Let \`H\` be a boundary tournament, let \`X=(x_0,\ldots,x_{m-1})\` be a tight path in \`H\`, let \`0\le i\le m-3\`, and let \`s,t\` be distinct vertices of \`V(H)-V(X)\`. Suppose
\`(x_{i+1},s,x_i)\`,
\`(x_{i+1},t,x_i)\`,
\`(x_{i+2},s,x_{i+1})\`,
and
\`(x_{i+2},t,x_{i+1})\`
are all tight.

Then exactly one of
\`(x_{i+2},s,x_{i+1},t,x_i)\`
and
\`(x_{i+2},t,x_{i+1},s,x_i)\`
is a tight five-vertex path.

**Proof.**
Exactly one of \`(s,x_{i+1},t)\` and \`(t,x_{i+1},s)\` is tight.

If \`(s,x_{i+1},t)\` is tight, then
\`(x_{i+2},s,x_{i+1},t,x_i)\`
is tight, using the hypotheses \`(x_{i+2},s,x_{i+1})\` and \`(x_{i+1},t,x_i)\`.

If \`(t,x_{i+1},s)\` is tight, then
\`(x_{i+2},t,x_{i+1},s,x_i)\`
is tight, using the other two hypotheses. The two cases are exclusive by boundary antisymmetry. ∎

## 2. A five-vertex consequence of ordered matching blocks

### Proposition 2.1

Let \`H\` be a boundary tournament, and let \`b,c,r,s,u\` be distinct vertices of \`H\`. Suppose \`H[\{b,c,r,s\}]\` is represented by an edge order whose opposite-edge perfect matchings satisfy
\`\{bc,rs\}<\{br,cs\}<\{bs,cr\}\`.
Assume \`H[\{b,c,r,s,u\}]\` is non-Hamiltonian and \`(b,c,u)\` is tight.

Then exactly one of \`(r,u,s)\` and \`(u,s,c)\` is tight.

**Proof.**
The matching-block order gives, among others, the tight triples
\`(b,c,s)\`,
\`(s,c,r)\`,
\`(r,b,s)\`,
\`(c,s,b)\`,
\`(r,s,c)\`,
\`(b,r,c)\`,
and
\`(s,r,b)\`.

Let \`A\` denote the assertion that \`(r,u,s)\` is tight and \`B\` the assertion that \`(u,s,c)\` is tight.

If both are false, boundary antisymmetry gives \`(s,u,r)\` and \`(c,s,u)\` tight. Hence
\`(b,c,s,u,r)\`
is a Hamilton tight path, a contradiction.

Suppose both are true. Since the five-set is non-Hamiltonian, whenever two consecutive triples of a displayed five-vertex order are tight, the reverse of its third consecutive triple is forced. Applying this successively gives
\`b\,u\,s\,c\,r \Rightarrow (s,u,b)\`,
\`b\,r\,u\,s\,c \Rightarrow (u,r,b)\`,
\`c\,u\,r\,b\,s \Rightarrow (r,u,c)\`,
\`r\,u\,c\,s\,b \Rightarrow (s,c,u)\`,
\`r\,s\,c\,u\,b \Rightarrow (b,u,c)\`,
and
\`s\,u\,b\,r\,c \Rightarrow (r,b,u)\`.

Now \`(s,r,b)\`, \`(r,b,u)\`, and \`(b,u,c)\` are tight, so
\`(s,r,b,u,c)\`
is a Hamilton tight path, again a contradiction. Therefore the two assertions cannot agree, and exactly one of the two displayed triples is tight. ∎


# Two bad four-extensions force a controlled five-path

## Lemma

Let H be a boundary tournament, let
T={u_0,u_1,u_2},
and let x,y be two distinct vertices outside T.

Assume both four-sets
T union {x}
and
T union {y}
are non-Hamiltonian.

Then the five-set
T union {x,y}
has a Hamilton tight path whose two endpoints both lie in T.

More precisely, after relabelling the three vertices of T, one of

(u_0,x,u_1,y,u_2)

or

(u_0,y,u_1,x,u_2)

is a Hamilton tight path.

## Proof

There are two cases.

### Case 1: both bad four-sets are edge-orderable

The two representing edge orders induce the same comparison orientation on the three ordinary edges of T. Relabel u_0,u_1,u_2 so that this common order is

u_1u_2 < u_0u_2 < u_0u_1.

By the matching-block classification of a non-Hamiltonian edge-ordered K_4, for each r in {x,y} the three r-edges are forced into the order

ru_0 < ru_1 < ru_2.

Hence, for each r in {x,y},

(u_0,r,u_1)
and
(u_1,r,u_2)

are tight.

Exactly one of

(x,u_1,y), (y,u_1,x)

is tight by boundary antisymmetry. In the first case

(u_0,x,u_1,y,u_2)

is tight; in the second case

(u_0,y,u_1,x,u_2)

is tight.

### Case 2: one bad four-set is not edge-orderable

We first record the four-vertex fact needed here.

**Subclaim.** Every non-Hamiltonian four-vertex boundary tournament whose comparison digraph is cyclic is the exceptional cyclic K_4, up to relabelling. In particular every one of its three-vertex subsets has cyclic comparison orientation.

To prove the subclaim, take a shortest directed cycle in the comparison digraph. A four-cycle of ordinary edges would itself contain three successive comparison arcs and hence give a Hamilton tight four-path, so the shortest cycle has length three.

If it is an ordinary-triangle cycle, relabel the triangle a,b,c so that

(a,b,c), (b,c,a), (c,a,b)

are tight, and call the fourth vertex z. Non-Hamiltonicity immediately forces

(b,a,z), (c,b,z), (a,c,z)

because otherwise respectively zabc, z b c a, or z c a b (after the corresponding cyclic relabelling) is Hamiltonian; likewise it forces

(z,b,a), (z,c,b), (z,a,c)

by considering c a b z, a b c z, and b c a z. Finally, if for example (b,z,a) were tight, then the already forced (c,b,z) would make (c,b,z,a) Hamiltonian, so (a,z,b) is tight. Cyclically the other two middle-z triples are

(b,z,c), (c,z,a).

Thus the twelve tight representatives are exactly

abc, bca, cab,
zba, azb, baz,
acz, cza, zac,
zcb, bzc, cbz.

If instead the shortest comparison triangle is a star, relabel it as

(a,o,b), (b,o,c), (c,o,a).

Successively avoiding the Hamilton words

a o b c,
c a o b,
a b o c,
b o c a,
b c o a,
c o a b,
a c b o,
o b a c,
o c b a

forces respectively

(c,b,o),
(o,a,c),
(o,b,a),
(a,c,o),
(o,c,b),
(b,a,o),
(b,c,a),
(c,a,b),
(a,b,c).

These twelve triples are the same exceptional cyclic K_4 after relabelling. This proves the subclaim.

Now suppose, without loss of generality, that H[T union {x}] is not edge-orderable. By the subclaim it is the exceptional cyclic K_4, so the comparison orientation already induced on the shared triangle T is cyclic. Therefore H[T union {y}] cannot be edge-orderable either: an edge order would make every induced comparison digraph acyclic. Since it is also non-Hamiltonian, the subclaim makes it the same exceptional cyclic K_4 relative to T.

Relabel T as {a,b,c} so that for each z in {x,y},

(a,z,b)
and
(b,z,c)

are tight. Exactly one of

(x,b,y), (y,b,x)

is tight. In the first case

(a,x,b,y,c)

is a Hamilton tight path; in the second case

(a,y,b,x,c)

is one.

Thus in all cases T union {x,y} has the asserted Hamilton five-path with both endpoints in T. ∎

## Reconfiguration interpretation

Suppose an eight-vertex boundary tournament is displayed as a Hamilton 5-path

P=(x,a,b,c,y)

together with a tight 3-path on vertex set T.

If neither T union {x} nor T union {y} is Hamiltonian, the lemma replaces the old 5|3 state by another 5|3 state whose five-side is

T union {x,y}

and whose endpoints lie in T, while the new three-side is the old internal triple {a,b,c}.

Thus failure of both direct endpoint transfers does not merely produce some new Hamiltonian five-set: it performs a controlled support rotation exchanging the old five-path interior with the old three-side.

This is a local rotation primitive for global no-trapping arguments. ∎

# Three double-extenders force a Hamiltonian five-set

Let `H` be a boundary tournament. Let `u,v,a,b,c` be five distinct vertices. Assume that for every
`s in {a,b,c}`,
both
`(s,u,v)`
and
`(u,v,s)`
are tight.

Then
`H[{u,v,a,b,c}]`
is Hamiltonian.

## Proof

Suppose for contradiction that the five-set
`X={u,v,a,b,c}`
is non-Hamiltonian. By the non-Hamiltonian-five-set theorem, `H[X]` has an edge-order representation. Write its strict edge order as `<`.

The two tight triples for each shell vertex `s in {a,b,c}` give
`su < uv < vs`.

We now inspect the three shell edges.

If there are distinct shell vertices `r,s` with
`vr < rs`,
let `t` be the third shell vertex. Then
`tu < uv < vr < rs`,
so
`(t,u,v,r,s)`
is an increasing Hamilton path, contradiction.

Hence we may assume that for every distinct shell pair `r,s`,
`rs < vr`.
Interchanging the names `r,s` shows also
`rs < vs`.

Next, if there are distinct shell vertices `r,s` with
`rs < su`,
and `t` is the third shell vertex, then
`rs < su < uv < vt`,
so
`(r,s,u,v,t)`
is an increasing Hamilton path, contradiction.

Hence we may also assume that for every distinct shell pair `r,s`,
`su < rs`.
Again interchanging `r,s` gives
`ru < rs`.

Therefore every shell edge `rs` satisfies
`ru,su < rs < vr,vs`.

Among the three shell edges, choose two in increasing order. Since the shell is a triangle, they share a vertex, so after relabelling the shell vertices we have
`ab < bc`.
The preceding inequalities give
`ua < ab < bc < cv`.
Thus
`(u,a,b,c,v)`
is an increasing Hamilton path on `X`, contradiction.

Therefore `H[X]` is Hamiltonian. ∎

This lemma converts a symmetric endpoint-extension pattern into an actual Hamilton path. It is particularly suited to direct vertex-addition arguments where repeated omission swaps or order-disagreement witnesses create several vertices extending the same ordered edge at both ends.

# Asymmetric double-extenders

# An asymmetric double-extender Hamiltonizes a five-set

## Lemma

Let H be a boundary tournament and let a,u,v,b,c be five distinct vertices. Assume

(a,u,v), (u,v,b), (c,u,v), (u,v,c)

are all tight.

Then H[{a,u,v,b,c}] is Hamiltonian.

## Proof

Suppose for contradiction that X={a,u,v,b,c} is non-Hamiltonian. By the non-Hamiltonian-five-set theorem, H[X] has an edge-order representation. Write its strict edge order as <.

The four displayed tight triples give

au<uv<vb

and

cu<uv<vc.

We force four additional comparisons by avoiding explicit increasing Hamilton paths.

If ab<au, then

ab<au<uv<vc,

so (b,a,u,v,c) is an increasing Hamilton path. Hence

au<ab.

If vb<ab, then

cu<uv<vb<ab,

so (c,u,v,b,a) is an increasing Hamilton path. Hence

ab<vb.

Thus

au<ab<vb.

If vb<vc, then

au<ab<vb<vc,

so (u,a,b,v,c) is an increasing Hamilton path. Hence

vc<vb.

If cu<au, then

cu<au<ab<vb,

so (c,u,a,b,v) is an increasing Hamilton path. Hence

au<cu.

Combining the inequalities now gives

au<cu<uv<vc<vb.

In particular

au<cu<vc<vb,

so

(a,u,c,v,b)

is an increasing Hamilton path on X, contradiction. Therefore X is Hamiltonian. ∎



# Repeated bad deletion forces cross-exterior Hamiltonicity

Let `H` be a boundary tournament. Let `A` be a four-vertex set with a Hamilton tight path
`(a,b,c,d)`.
Let `z,z'` be distinct vertices outside `A`.

Assume both five-sets
`A union {z}` and `A union {z'}`
are non-Hamiltonian.

Then both five-sets
`{a,b,c,z,z'}`
and
`{b,c,d,z,z'}`
are Hamiltonian.

## Proof

Apply the fixed-three-path extension theorem to the tight path `(a,b,c)` and the three exterior vertices `d,z,z'`. At least one of

`{a,b,c,d,z}=A union {z}`,
`{a,b,c,d,z'}=A union {z'}`,
`{a,b,c,z,z'}`

is Hamiltonian. The first two are non-Hamiltonian by hypothesis, so the third is Hamiltonian.

Apply the same theorem to the tight path `(b,c,d)` and exterior vertices `a,z,z'`. Again the first two resulting five-sets are `A union {z}` and `A union {z'}`, so the remaining set
`{b,c,d,z,z'}`
is Hamiltonian. ∎

## Five-set defect form

Let `S` be a non-Hamiltonian five-set, let `u in S` have `S-u` Hamiltonian, and let `z,z'` lie outside `S`. If both
`(S-u) union {z}` and `(S-u) union {z'}`
are non-Hamiltonian, choose any Hamilton path `(a,b,c,d)` on `S-u`. Then the two cross-exterior five-sets displayed above are Hamiltonian.

This gives a concrete certificate whenever the same exceptional deletion label recurs for two exterior vertices in the extension-amplification framework.

# Oppositely oriented Hamiltonian deletions in a bad five-set

Let `H` be a boundary tournament and let `S={a,c,p,q,r}` be a five-vertex set such that `H[S]` is non-Hamiltonian. Put `T=S-{a,c}`.

Partition `T` as `X={t in T:(a,t,c) is tight}` and `Z={t in T:(c,t,a) is tight}`.

Then there exist `x in X` and `z in Z` such that both `H[S-{x}]` and `H[S-{z}]` are Hamiltonian.

## Proof

Boundary antisymmetry gives `T=X sqcup Z`. Neither class is empty. If all three vertices of `T` belonged to `X`, the three common-endpoint triples `(a,t,c)` would force `H[S]` to be Hamiltonian. If all three belonged to `Z`, the same lemma after interchanging `a,c` gives the same contradiction. Thus the class sizes are `2` and `1`.

Suppose without loss of generality that `X={p,q}` and `Z={r}`. The two parallel-middle triples `(a,p,c)` and `(a,q,c)` force a Hamilton tight path on `{a,c,p,q}=S-{r}`. Hence `H[S-{r}]` is Hamiltonian.

A non-Hamiltonian five-vertex boundary tournament has at most one non-Hamiltonian four-vertex induced subtournament. Therefore at least one of `H[S-{p}]` and `H[S-{q}]` is Hamiltonian. Taking that deleted vertex as `x` and taking `z=r` proves the claim. The case `|Z|=2` is symmetric. ∎

# Cross-compatible opposite deletions

Let `H` be a boundary tournament, let `S` be a non-Hamiltonian five-vertex set, fix distinct `a,c in S`, and put `T=S-{a,c}`.

Then there are distinct `s,t in T` and Hamilton tight paths `A_s,A_t` on `S-{s}` and `S-{t}`, respectively, such that:

1. the endpoint orientations through `a,c` are opposite; after interchanging `s,t` if necessary, `(a,s,c)` and `(c,t,a)` are tight;
2. deleting `t` from the vertex sequence `A_s` leaves a tight path on `S-{s,t}`;
3. deleting `s` from the vertex sequence `A_t` leaves a tight path on the same three-vertex set `S-{s,t}`.

The two surviving three-vertex orders need not be the same.

## Proof

By the oppositely oriented Hamiltonian-deletions result, choose `s,t in T` in opposite orientation classes through `a,c` such that both `H[S-{s}]` and `H[S-{t}]` are Hamiltonian.

Because `H[S]` is a non-Hamiltonian boundary tournament on five vertices, it has an edge-order representation. Restrict that edge order to each of the Hamiltonian four-sets `S-{s}` and `S-{t}`.

Apply the prescribed-removable-vertex theorem from the edge-ordered comparison module to the edge-ordered `K_4` on `S-{s}`, prescribing `t`. It gives an increasing Hamilton path `A_s` whose deletion of `t` is still an increasing three-vertex path. Apply the same lemma to `S-{t}`, prescribing `s`, to obtain `A_t`.

Increasing paths in the representing edge order are exactly tight paths of the induced boundary tournament, so the conclusions translate directly. ∎
