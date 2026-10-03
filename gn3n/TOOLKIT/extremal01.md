# Extremal Hamiltonicity and Johnson-density toolkit

**Summary:** Hamiltonian five-sets satisfy complementary finite-range and Johnson-degree density bounds, together with reusable equality, overlap, reconfiguration, and terminal-pair counting structure.

## Statement

Extremal Hamiltonicity toolkit: complementary finite-range and Johnson-degree density bounds for Hamiltonian five-sets, equality/regularity information, complement-free ten-set spectral bounds, fixed-pair extension structure, bad-six-set order/K4 overlap structure, reconfigurable 5|5 structure at order ten, and terminal-pair rank counting.

## Body

# Extremal and density tools for Hamiltonian small sets

Let `J(r,k)` be the Johnson graph whose vertices are the `k`-subsets of an `r`-element set, with two vertices adjacent exactly when their intersection has order `k-1`.

## 1. A quadratic density bound from local `(k+1)`-set occupancy

Let `B` be a family of `k`-subsets of an `r`-element set, where `r>=k+1`. Write

`b=|B|`, `M=binom(r,k)`, `p=b/M`.

Suppose every `(k+1)`-subset contains at most `t` members of `B`. Then

`(r-k+1)p^2-p <= t(t-1)(r-k)/(k(k+1))`,

and therefore

`p <= [1+sqrt(1+4t(t-1)(r-k)(r-k+1)/(k(k+1)))]/[2(r-k+1)]`.

If `t>=2` and equality holds throughout, then every `(k+1)`-subset contains exactly `t` members of `B`, and every `(k-1)`-subset is contained in the same number of members of `B`.

**Proof.** For each `(k+1)`-set `U`, put

`y_U=|B intersect binom(U,k)|`.

Every edge of `J(r,k)[B]` has a unique union of order `k+1`, so

`e(B)=sum_U binom(y_U,2) <= binom(r,k+1) binom(t,2)`.

For each `(k-1)`-set `S`, put

`x_S=|{F in B:S subset F}|`.

Every Johnson edge has a unique intersection of order `k-1`, hence

`e(B)=sum_S binom(x_S,2)=(sum_S x_S^2-kb)/2`,

because `sum_S x_S=kb`. By Cauchy-Schwarz,

`sum_S x_S^2 >= k^2b^2/binom(r,k-1)`.

Combining the lower and upper bounds for `e(B)` and using

`binom(r,k-1)=binom(r,k)k/(r-k+1)`,

`binom(r,k+1)=binom(r,k)(r-k)/(k+1)`,

and `b=p binom(r,k)` gives the displayed quadratic inequality. Solving it for the positive root gives the density bound.

If equality holds and `t>=2`, then equality is required both in the pointwise estimate `binom(y_U,2)<=binom(t,2)` and in Cauchy-Schwarz. Thus every `y_U=t` and all `x_S` are equal. ∎

## 2. A degree bound from the same local occupancy hypothesis

Under the same hypotheses,

`p <= [k+(t-1)(r-k)]/[k(r-k+1)]`.

More precisely, every vertex of `J(r,k)[B]` has degree at most

`(t-1)(r-k)`,

while the average degree of `J(r,k)[B]` is at least

`k(r-k+1)p-k`.

If equality holds, then every member `F of B` has exactly `t-1` neighbors of `B` inside each `(k+1)`-set containing `F`, and every `(k-1)`-subset lies in the same number of members of `B`.

**Proof.** Fix `F in B`. Every Johnson neighbor `G of F` has a unique union `U=F union G` of order `k+1`. There are `r-k` such supersets `U` of `F`, and each contains at most `t-1` further members of `B`. Hence

`deg_B(F)<= (t-1)(r-k)`.

Thus

`2e(B)<=b(t-1)(r-k)`.

Using the intersection counts `x_S` from the previous proof,

`2e(B)=sum_S x_S(x_S-1)=sum_S x_S^2-kb`.

Cauchy-Schwarz gives

`2e(B)>=k^2b^2/binom(r,k-1)-kb`.

Comparing the two inequalities and substituting

`binom(r,k-1)=binom(r,k)k/(r-k+1)`, `b=p binom(r,k)`

yields

`k(r-k+1)p-k <= (t-1)(r-k)`,

which is equivalent to the claimed bound. Equality forces equality in every pointwise degree bound and in Cauchy-Schwarz, giving the stated regularity conditions. ∎

For `k=2,t=2` the second bound gives `p<=r/[2(r-1)]`. For `k=5,t=2` it gives `p<=r/[5(r-4)]`.

## 3. Complement-pair cut bound in `J(10,5)`

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

## 4. Hamilton-five density hierarchy in boundary tournaments

Let `H` be a boundary tournament, let `W⊆V(H)` have order `r>=6`, and fix `S⊆W` of order `s∈{0,1,2,3}`. Let `h_5(W;S)` be the number of five-subsets `F` such that

`S⊆F⊆W`

and `H[F]` is Hamiltonian. Then the fraction of five-subsets containing `S` that are non-Hamiltonian is at most

`(r-s)/[(5-s)(r-4)]`.

Equivalently,

`h_5(W;S) >= [1-(r-s)/((5-s)(r-4))] binom(r-s,5-s)`.

For `s=0`, this gives Hamilton-five density at least

`4(r-5)/[5(r-4)]`.

For fixed vertex, pair, and triple, the corresponding asymptotic guaranteed densities tend respectively to `3/4`, `2/3`, and `1/2`. For every `r>10`, these bounds strictly improve the elementary fixed-subset density bounds obtained by direct double counting from the four-of-six theorem.

**Proof.** Let `B_S` be the family of sets

`F-S`

where `S⊆F⊆W`, `|F|=5`, and `H[F]` is non-Hamiltonian. Then `B_S` is `k=(5-s)`-uniform on the `N=r-s` vertices of `W-S`.

Every `(k+1)=(6-s)`-subset `U⊆W-S` corresponds to the six-set `S∪U`. By `the small-set structure module` Section 6, at least four of the six five-subsets of `S∪U` are Hamiltonian. Hence at most two members of `B_S` lie inside `U`.

Apply Section 2 with `t=2`. The bad-set density satisfies

`p_bad <= [k+(N-k)]/[k(N-k+1)] = N/[k(N-k+1)]`.

Substituting `N=r-s`, `k=5-s`, and `N-k+1=r-4` gives

`p_bad <= (r-s)/[(5-s)(r-4)]`.

Complementing inside the family of all five-subsets containing `S` gives the displayed Hamiltonian density. ∎



# Complement-free ten-set spectral bound

## Theorem. Spectral bound for intersection-one pairs

Let `Omega` be a ten-element set. Let `G` be the graph whose vertices are the `252` five-subsets of `Omega`, with two distinct five-sets adjacent exactly when they meet in one element.

Let `F` be a complement-free family of `m` five-subsets, meaning that `A in F` implies `Omega-A notin F`. Then the average degree of the induced graph `G[F]` is at most

`7 + 18m/252`.

In particular, `m<=126`, so the average degree is at most `16`.

**Proof.** Let `J` be the adjacency matrix of the ordinary Johnson graph `J(10,5)`, where two five-sets are adjacent when they meet in four elements. For `0<=j<=5`, let `U_j` denote the usual `j`th Johnson eigenspace. The eigenvalues of `J` on

`U_0,U_1,U_2,U_3,U_4,U_5`

are respectively

`25,15,7,1,-3,-5`.

The distance-four adjacency matrix of `J(10,5)` is exactly the adjacency matrix `A` of `G`, since Johnson distance four means intersection size one. The standard Johnson one-swap recurrence gives

`A = p_4(J)`

with

`p_4(t)=(t^4-32t^3+166t^2+864t-1575)/576`.

Evaluating this polynomial at the six Johnson eigenvalues gives the eigenvalues of `A`:

`25,-15,7,-1,-3,5`.

Thus `G` is `25`-regular, and every eigenvalue on the orthogonal complement of the constant vectors is at most `7`.

Let `chi` be the characteristic vector of `F` and write

`chi=(m/252)1+v`,

where `v` is orthogonal to `1`. Then

`||v||^2=m-m^2/252`.

By the Rayleigh bound,

`2e(G[F]) = chi^T A chi`

`<=25m^2/252 + 7(m-m^2/252)`.

Dividing by `m` gives average degree at most

`7+18m/252`.

Finally, the `252` five-subsets split into `126` complementary pairs, and a complement-free family contains at most one member of each pair. Hence `m<=126`, giving the bound `16`. ∎


# Fixed-pair bad-extension structure

Let H be an arbitrary boundary tournament. Fix two distinct vertices r,s, and let X be a set of m vertices disjoint from {r,s}.

Partition X into

X_+={v in X : (r,v,s) is tight}

and

X_-={v in X : (s,v,r) is tight}.

Boundary antisymmetry gives

X=X_+ disjoint-union X_-.

Define the bad-pair graph B_{r,s}(X) on vertex set X by joining distinct x,y exactly when

H[{r,s,x,y}]

is non-Hamiltonian.

## Theorem

B_{r,s}(X) is bipartite with bipartition X_+|X_-.

Consequently

|E(B_{r,s}(X))| <= |X_+||X_-| <= floor(m^2/4).

Equivalently, at least

binom(m,2)-floor(m^2/4)

pairs {x,y} make the four-set {r,s,x,y} Hamiltonian.

If equality holds in the numerical upper bound, then m is split as evenly as possible between X_+,X_- and every cross pair is bad.

## Proof

Take distinct x,y in X_+.

Then

(r,x,s)

and

(r,y,s)

are both tight.

By the parallel-middle lemma in the local Hamilton-extension module, at least one of

(r,x,s,y),
(r,y,s,x)

is a Hamilton tight path on {r,s,x,y}.

Therefore xy is not an edge of B_{r,s}(X).

The same argument with r and s interchanged applies to two vertices x,y in X_-. Hence B_{r,s}(X) has no edge inside either orientation class, so every bad edge crosses X_+|X_-.

Thus B_{r,s}(X) is bipartite and

|E(B_{r,s}(X))| <= |X_+||X_-|.

For fixed sum |X_+|+|X_-|=m, the product is at most floor(m^2/4), with equality exactly for the most balanced split. Numerical equality also requires every possible cross edge to occur, since B is a subgraph of the complete bipartite graph X_+ x X_-.

This proves all claims. ∎

## Exchange interpretation

For a fixed two-vertex support {r,s}, non-Hamiltonian four-vertex extensions are controlled by a single binary orientation class. In particular a complete family of failed exchanges between two vertex sets A,B can occur only when all relevant vertices of A lie in one class and all relevant vertices of B lie in the other.

This explains the complete-bipartite exceptional pattern that can arise when attempting to rebalance a 5|5|2 cover by deleting one vertex from each five-side and adjoining the deleted pair to {r,s}. ∎

# Rooted seven-set set expansion

Let H be a boundary tournament. Let

W=A disjoint-union {y}

with |A|=6.

Define an ordinary graph G_y on vertex set A by declaring distinct a,b in A adjacent when

H[{y} union (A-{a,b})]

is Hamiltonian.

## Theorem

The graph G_y has minimum degree at least three. Consequently:

1. G_y has at least nine edges;
2. G_y has a Hamilton cycle;
3. in particular, G_y has a perfect matching.

Equivalently, among the fifteen five-subsets of W that contain the distinguished vertex y, at least nine are Hamiltonian, and six of those Hamiltonian five-sets can be indexed cyclically by the six consecutive omitted pairs of a cyclic ordering of A.

## Proof

Fix a in A. Apply the four-of-six theorem to the six-set

W-{a}=(A-{a}) union {y}.

At least four of its six five-subsets are Hamiltonian.

Exactly one of those six subsets omits y, namely A-{a}. The other five are

{y} union (A-{a,b})

as b ranges over A-{a}.

Therefore at least three of these five sets are Hamiltonian. By definition, a has at least three neighbors in G_y.

Since a was arbitrary,

delta(G_y)>=3.

The edge bound follows immediately from the handshake lemma:

2|E(G_y)| >= 6*3,

so

|E(G_y)|>=9.

For completeness we prove Hamiltonicity without importing an external graph theorem. Let

v_1,...,v_k

be a longest path of G_y.

Both endpoints have all their neighbors on this path. Put

I={i in {1,...,k-1}: v_1 v_{i+1} is an edge}

and

J={i in {1,...,k-1}: v_i v_k is an edge}.

Since both endpoint degrees are at least three,

|I|,|J|>=3.

Because k<=6, there are at most five possible indices i. Hence I and J intersect. Choose i in I intersect J. Then

v_1,v_2,...,v_i,v_k,v_{k-1},...,v_{i+1},v_1

is a cycle through all k vertices of the longest path.

If k<6, then G_y is connected: every connected component has at least four vertices because every vertex has degree at least three, so two components would require at least eight vertices. Thus some vertex outside the k-cycle has an edge into it. Breaking the cycle at that neighbor and starting from the outside vertex gives a path longer than k, contradiction.

Therefore k=6 and the displayed cycle is Hamiltonian.

Taking alternate edges of a six-cycle gives a perfect matching. ∎

## set-expansion interpretation

This is a genuine set-expansion statement. Even when every one-vertex replacement of a six-vertex support by y is non-Hamiltonian—as is possible by the known one-vertex-replacement counterexample—the next lower-order set cannot remain sparse: the two-deletion five-set around y contains at least nine Hamiltonian supports arranged around a Hamilton cycle.

Thus complete failure of the first replacement set forces structured abundance one layer deeper. This does not itself provide the complementary Hamiltonian support needed for a two-cover, but it supplies a concrete model for an augmenting-set proof rather than a bounded-distance conjecture. ∎

# 5|5 structure at order ten

Let `H` be a boundary tournament on ten vertices. Suppose
`V(H)=A disjoint-union F`,
with
`|A|=|F|=5`,
and `H[A]` Hamiltonian.

Then there is a partition
`V(H)=X disjoint-union Y`
into two Hamiltonian five-sets such that the split `X|Y` has exchange distance at most two from `A|F`.

Consequently the two-support-exchange conjecture of `the radius-two support-exchange proposal` holds for the even equitable addition step
`5|4 + x -> 5|5`
at total order ten.

## Proof

If `H[F]` is Hamiltonian, take
`X=A`,
`Y=F`;
the exchange distance is zero.

Assume therefore that `F` is non-Hamiltonian.

For each
`a in A`,
`y in F`,
define
`X_{a,y}=(A-{a}) union {y}`
and
`Y_{a,y}=(F-{y}) union {a}`.
These two five-sets are complementary.

Construct a `5 x 5` matrix indexed by `A x F`.
Call a cell `(a,y)`

- **X-good** if `X_{a,y}` is Hamiltonian;
- **Y-good** if `Y_{a,y}` is Hamiltonian.

Fix a column `y in F`. Apply the four-of-six theorem to the six-set
`A union {y}`.
At least four of its six five-subsets are Hamiltonian.
One of them is `A` itself, obtained by deleting `y`.
Therefore at least three of the remaining five subsets
`X_{a,y}`, `a in A`,
are Hamiltonian.

Hence every column contains at least three X-good cells, so there are at least
`5*3=15`
X-good cells.

Now fix a row `a in A`. Apply four-of-six to
`F union {a}`.
At least four of its six five-subsets are Hamiltonian.
The subset obtained by deleting `a` is `F`, which is non-Hamiltonian.
Therefore at least four of the five remaining subsets
`Y_{a,y}`, `y in F`,
are Hamiltonian.

Hence every row contains at least four Y-good cells, so there are at least
`5*4=20`
Y-good cells.

The matrix has only 25 cells. Therefore the sets of X-good and Y-good cells intersect in at least
`15+20-25=10`
cells.

Choose one common-good cell `(a,y)`.
Then
`X_{a,y}|Y_{a,y}`
is an equitable spanning two-cover of `H`.

For the vertex-addition interpretation, write
`F=B union {x}`,
where the old cover has orders
`|A|=5`,
`|B|=4`.

If `y=x`, then
`X_{a,x}=(A-{a}) union {x}`,
`Y_{a,x}=B union {a}`,
which is the distance-one replace-and-transfer pattern of `the radius-two exchange formulation`.

If `y in B`, then
`X_{a,y}=(A-{a}) union {y}`,
`Y_{a,y}=(B-{y}) union {a,x}`,
which is the distance-two one-for-one swap pattern.

Thus every common-good cell gives exchange distance at most two. ∎

## Exchange-matrix principle

The proof isolates the scalable mechanism.

Let `A,F` be disjoint equal-size sets of order `m`. For each cell `(a,y) in A x F`, define complementary replacement sets
`X_{a,y}=(A-a)+y`,
`Y_{a,y}=(F-y)+a`.

If every column has at least `r` X-good cells and every row at least `s` Y-good cells, with
`r+s>m`,
then some cell is good on both sides, because
`mr+ms>m^2`.

At `m=5`, four-of-six gives
`r>=3`
when `A` is Hamiltonian and
`s>=4`
when `F` is non-Hamiltonian, so
`r+s>=7>5`.

A general proof of the two-support-exchange conjecture could therefore follow from sufficiently strong Hamiltonian-deletion density in larger one-vertex extensions. ∎

Every boundary tournament on ten vertices admits a partition into two Hamiltonian five-sets.

Consequently, if `H` is a minimum-order counterexample of order eleven, then for **every** vertex `x in V(H)` the deletion `H-x` has an equitable `5|5` two-cover. Equivalently, every vertex of `H` occurs as the singleton of a spanning `5|5|1` three-cover.

## Proof

Let `K` be an arbitrary boundary tournament on ten vertices.

Choose any six-vertex subset `U subseteq V(K)`.

By the four-of-six theorem `the small-set structure module`, at least four of the six five-subsets of `U` are Hamiltonian. In particular there exists a Hamiltonian five-set

`A subseteq U`.

Let

`F=V(K)-A`.

Then `|F|=5`, so

`V(K)=A disjoint-union F`

is a partition into two five-sets with `A` Hamiltonian.

Apply the order-ten exchange theorem `the order-ten exchange theorem immediately above`. Its hypotheses are exactly that `K` has ten vertices, `|A|=|F|=5`, and `A` is Hamiltonian. Therefore it produces a partition

`V(K)=X disjoint-union Y`

such that both `X` and `Y` are Hamiltonian five-sets.

Hence `X|Y` is an equitable `5|5` two-cover of `K`. ∎

Now let `H` be a minimum counterexample of order eleven and fix any vertex `x`.

The proper induced subtournament `H-x` has order ten, so the theorem above gives an `5|5` cover of `H-x`.

Since `x` was arbitrary, every vertex deletion is equitable `5|5`. Adding the singleton `(x)` yields a spanning `5|5|1` three-cover of `H` for every choice of singleton label. ∎

## Order-eleven consequence

In the order-eleven collision, there are **no exceptional singleton labels**.

Thus the weaker order-eleven reachability statement `the earlier weaker nine-of-eleven reachability theorem` is superseded: the equitable omission-reconfiguration surface contains all eleven vertices, not merely at least nine.

The remaining obstruction is therefore entirely in the failure to absorb the omitted singleton into either side of an equitable `5|5` deletion cover, despite the fact that every possible omitted vertex admits such a balanced state.

# Terminal-pair rank lower bound

Source: the user's research scrapbook, section Antisymmetric Tournaments.

The numerical lower bound is not close to the two-cover conjecture. The relevant feature is the proof mechanism: local extension failure is encoded as a rank on terminal pairs, and boundary antisymmetry turns each equal-rank in-neighborhood into an ordinary tournament whose outneighbors must already be occupied by one extremal path.

## Theorem

Every n-vertex 3-uniform boundary tournament H contains a tight path on at least 1+sqrt((n-1)/2) vertices.

More precisely, one can orient every unordered pair {u,v} and attach an integer rank so that for every vertex v and every rank r, at most 2r-3 arcs of rank r enter v.

## Proof

For distinct u,v, let L(u,v) be the maximum order of a tight path ending with the ordered pair (u,v). Orient {u,v} as u->v when L(u,v)>=L(v,u), breaking equality arbitrarily, and label this arc by L(u,v).

Fix v and rank r. Let X be the set of vertices u for which u->v has label r. Define a tournament T_X on X by orienting u->w exactly when (u,v,w) is tight. Boundary antisymmetry makes this an ordinary tournament.

Choose u in X with outdegree at least (|X|-1)/2 in T_X, and let P be a tight path of order r ending with (u,v).

Every outneighbor w of u in T_X must already lie on P. Otherwise (u,v,w) is tight and appending w gives a tight path of order r+1 ending with (v,w). But w->v was chosen as an incoming arc to v of label r, so L(w,v)>=L(v,w), whereas L(w,v)=r and L(v,w)>=r+1, a contradiction.

Thus P contains u,v and every outneighbor of u, giving r>=2+(|X|-1)/2 and hence |X|<=2r-3.

Choose v of indegree at least (n-1)/2 in the auxiliary tournament. If t is the maximum order of a tight path in H, partition incoming arcs at v by labels r=2,...,t. Then

(n-1)/2 <= sum_{r=2}^t (2r-3) = (t-1)^2,

so t>=1+sqrt((n-1)/2). ∎

## Relevance to GN3

The theorem itself is only a single-path lower bound. The reusable idea is the terminal-pair rank: orient a local state by whichever direction supports the longer completion, then use antisymmetry plus extremality to force all possible extensions into the already occupied path.

This is a candidate template for a genuine decreasing/ranking invariant on span-three states. No such lift to defect-span states is asserted here.

# Reciprocal swaps of Hamiltonian 5|5 covers

Let `G` be a boundary tournament on ten vertices with a Hamiltonian `5|5` cover
`P|Q`,
where `P,Q` denote both the chosen paths and their five-vertex supports.

For `p in P`, `q in Q`, call the cell `(p,q)`

- **P-good** if `(P-{p}) union {q}` is Hamiltonian;
- **Q-good** if `(Q-{q}) union {p}` is Hamiltonian;
- **double-good** if it is both P-good and Q-good.

A double-good cell is exactly a reciprocal support swap
`p <-> q`
that preserves a Hamiltonian `5|5` partition.

## Theorem

1. There are at least five double-good cells.
2. There are two double-good cells
   `(p_1,q_1)` and `(p_2,q_2)`
   with
   `p_1 != p_2` and `q_1 != q_2`.

Thus every Hamiltonian `5|5` cover of a ten-vertex boundary tournament has at least five one-for-one reciprocal swaps preserving Hamiltonicity on both sides, including two vertex-disjoint swaps.

## Proof

Fix `q in Q`.
Apply the four-of-six theorem to the six-set
`P union {q}`.
Deleting `q` leaves the Hamiltonian five-set `P`, so among the five other vertex deletions at least three are Hamiltonian.
Equivalently, the column indexed by `q` contains at least three P-good cells.

Summing over the five columns gives at least
`5*3=15`
P-good cells.

Symmetrically, for every fixed `p in P`, four-of-six on
`Q union {p}`
shows that the row indexed by `p` contains at least three Q-good cells.
Hence there are at least
`5*3=15`
Q-good cells.

The matrix has 25 cells. Inclusion-exclusion therefore gives at least
`15+15-25=5`
double-good cells.

It remains to prove that two can be chosen in distinct rows and columns.
Suppose not.
Then the bipartite graph of double-good cells has matching number one, so all of its edges share one common endpoint.
Thus either all double-good cells lie in one row or all lie in one column.

Assume first that they all lie in one row `p_*`.
For each of the other four rows `p != p_*`, at least three cells are Q-good.
None of those Q-good cells can be P-good, because every double-good cell lies in row `p_*`.
Hence among those four rows there are at least
`4*3=12`
P-bad cells.

But every column has at least three P-good cells, so every column has at most two P-bad cells.
Across all five columns there are therefore at most
`5*2=10`
P-bad cells, contradiction.

The case in which all double-good cells lie in one column is symmetric: the four other columns contribute at least 12 Q-bad cells, while every row has at most two Q-bad cells, giving at most 10 in total.

Therefore the double-good graph has matching number at least two. ∎

## Order-eleven consequence

Let `H` be a hypothetical order-eleven minimum counterexample and let
`H-x=P|Q`
be any equitable deletion cover.
Then, without changing the omitted vertex `x`, there are at least five neighboring Hamiltonian `5|5` support partitions of `H-x` obtained by one reciprocal swap, and two such swaps can be chosen on disjoint pairs of old vertices.

This supplies genuine within-deletion mobility complementary to the singleton-swap cliques of `the support-compatible deletion cliques in the order-eleven testbed`.

# Order disagreement in bad six-sets

Let `R` be a six-vertex induced boundary tournament that is non-Hamiltonian.

Let

`G={d in R : R-{d} is Hamiltonian}`.

By the four-of-six theorem `the small-set structure module`,

`|G|>=4`.

For each `d in G`, choose an arbitrary Hamilton tight path `P_d` on `R-{d}`.

Then there exist distinct `d,e in G` such that `P_d` and `P_e` order some two common vertices differently.

Consequently the ordered-path intersection theorem `the path restriction and intersection calculus` yields, inside `R`, at least one of:

- a reversed common ordered edge;
- a tight triple reversing an ordered edge at an intersection;
- a vertex-simple tight cycle.

## Proof

Assume for contradiction that every pair

`P_d,P_e`, `d,e in G`,

orders all common vertices in the same relative order.

We glue these local orders to a global order on `R`.

Fix distinct vertices `u,v in R`.

Because `|G|>=4`, there exists

`d in G-{u,v}`.

Then both `u,v` lie on `P_d`. Define

`u<v`

according to their relative order on `P_d`.

This is well-defined: if `e in G-{u,v}` is another choice, then `P_d,P_e` contain both `u,v`, and our compatibility assumption gives the same relative order.

Now take any three distinct vertices `u,v,w in R`.

Again `|G|>=4` guarantees some

`d in G-{u,v,w}`.

The global pairwise relation on this triple agrees with the restriction of the linear order `P_d`. Hence the global relation is transitive on every three-set. It is therefore a total linear order on all six vertices.

Write it as

`r_0<r_1<r_2<r_3<r_4<r_5`.

Fix any consecutive triple

`r_i,r_{i+1},r_{i+2}`.

Since `|G|>=4`, choose

`d in G-{r_i,r_{i+1},r_{i+2}}`.

The path `P_d` contains this triple, and its vertex order is the restriction of the global order. Because the three vertices are consecutive globally and `d` lies outside the triple, they remain consecutive in `P_d`.

Therefore

`(r_i,r_{i+1},r_{i+2})`

is tight.

This holds for every `i=0,1,2,3`, so

`(r_0,r_1,r_2,r_3,r_4,r_5)`

is a Hamilton tight path of `R`, contradicting the assumed non-Hamiltonicity of `R`.

Thus some two deletion paths disagree in relative order. The final alternatives follow from `the path restriction and intersection calculus`. ∎

## Order-eleven order-eleven consequence

Let

`P|Q|(x)`

be any equitable `5|5|1` state in a hypothetical order-eleven minimum counterexample.

Both six-sets

`V(P) union {x}`
and
`V(Q) union {x}`

are non-Hamiltonian, or else `H` would have a spanning `6|5` two-cover.

By `the omission-graph theorem in the order-eleven testbed`, each six-set contributes a clique of at least four omission states obtained from its Hamiltonian five-deletions while keeping the opposite five-support fixed.

The theorem above says that each such clique necessarily contains a pair of adjacent omission states whose Hamilton paths disagree in relative order on common vertices.

Hence every balanced order-eleven omission state lies in two one-swap cliques, one on each side, each carrying a reversed-edge / reversing-triple / tight-cycle witness.

This localizes order complexity throughout the universal balanced reconfiguration graph, not merely in the special three-side endpoint shells. ∎

# Prescribed Hamiltonian K4 overlap in a bad six-set

Let `R` be a non-Hamiltonian six-vertex boundary tournament and put

`G={d in R : R-{d} is Hamiltonian}`.

By the four-of-six theorem, `|G|>=4`.

Then for **every prescribed** `d in G`, there exists `e in G-{d}` such that

`R-{d,e}`

is Hamiltonian.

## Proof

Fix `d in G`. Assume for contradiction that `R-{d,e}` is non-Hamiltonian for every `e in G-{d}`.

The five-set `F=R-{d}` is Hamiltonian. For each `e in G-{d}`, the four-set `F-{e}=R-{d,e}` is non-Hamiltonian.

The small-order theorem `the small-set structure module`, Section 7, says that a Hamiltonian five-set has at most three non-Hamiltonian four-subsets. Hence `|G|-1<=3`.

Since four-of-six gives `|G|>=4`, necessarily `|G|=4`.

Write `G={d,e_1,e_2,e_3}` and let the remaining two vertices of `R` be `a,b`.

For `i=1,2,3`,
`R-{d,e_i}={a,b} union ({e_1,e_2,e_3}-{e_i})`
is non-Hamiltonian.

Thus for the fixed pair `{a,b}`, each of the three pairs
`{e_1,e_2}`, `{e_1,e_3}`, `{e_2,e_3}`
is a bad four-extension.

Equivalently, the bad-pair graph of `the fixed-pair bad-extension theorem earlier in this module` on the three exterior vertices `e_1,e_2,e_3` contains the triangle `K_3`.

But `the fixed-pair bad-extension theorem earlier in this module` says every such fixed-pair bad-extension graph is bipartite. Contradiction.

Therefore some `e in G-{d}` has `R-{d,e}` Hamiltonian. ∎

## Order-eleven consequence

Let `H` be a hypothetical minimum counterexample of order eleven and let

`H-x=P|Q`

be an equitable `5|5` cover.

Put
`R_P=V(P) union {x}`,
`R_Q=V(Q) union {x}`.

Both six-sets are non-Hamiltonian.

In `R_P`, the prescribed deletion `d=x` is good because `R_P-{x}=V(P)` is Hamiltonian. The theorem therefore gives a vertex `p in V(P)` such that both

`V(P)-{p}`

and

`(V(P)-{p}) union {x}`

are Hamiltonian.

Likewise there is `q in V(Q)` such that both

`V(Q)-{q}`

and

`(V(Q)-{q}) union {x}`

are Hamiltonian.

Set
`C=V(P)-{p}`,
`D=V(Q)-{q}`.

Then `C,D` are disjoint Hamiltonian four-sets, while the remaining three vertices are exactly `{p,q,x}`.

Every three-vertex boundary tournament is Hamiltonian. Hence `H` has a spanning three-cover of component orders

`4|4|3`

whose three-vertex component contains the originally omitted vertex `x`.

Moreover the same construction simultaneously gives the reversible omission states

`(C union {x})|Q|(p)`

and

`P|(D union {x})|(q)`.

Thus every equitable order-eleven omission state admits a Hamiltonian-core swap on each side and canonically refines to a spanning `4|4|3` cover. ∎

# Finite-range fixed-subset Hamilton-five density

## 2. Density of Hamilton five-sets through a fixed small subset

Let `W` be an `r`-vertex subset of a boundary tournament, where `r>=6`, and let `S subseteq W` have order `s in {0,1,2,3}`. Let `h_5(W;S)` be the number of five-element sets `F` satisfying

`S subseteq F subseteq W`

for which `H[F]` has a Hamilton tight path. Then

`h_5(W;S) >= ((4-s)/(6-s)) binom(r-s,5-s)`.

Thus at least two-thirds of all five-subsets of `W` are Hamiltonian; among the five-subsets containing a prescribed vertex, pair, or triple, the corresponding proportions are at least `3/5`, `1/2`, and `1/3`.

**Proof.** Count pairs `(U,F)` such that

`S subseteq F subset U subseteq W`, `|F|=5`, `|U|=6`,

and `H[F]` is Hamiltonian.

There are `binom(r-s,6-s)` possible six-sets `U`. By `the small-order structure module` Section 6, each `U` has at least four Hamiltonian five-subsets. At most `s` of those can fail to contain all of `S`, because a five-subset of `U` is obtained by deleting one vertex. Hence each `U` contributes at least `4-s` admissible pairs.

On the other hand, each Hamiltonian five-set `F` containing `S` lies in exactly `r-5` six-subsets of `W`. Therefore

`(r-5) h_5(W;S) >= (4-s) binom(r-s,6-s)`.

Using

`binom(r-s,6-s)/(r-5)=binom(r-s,5-s)/(6-s)`

gives the claimed bound. ∎

For the stronger Johnson-degree density hierarchy, which improves these fixed-subset bounds for every `r>10`, see `the Johnson-density hierarchy earlier in this module` Section 4.



## Metadata

- ID: extremal01
- Kind: toolkit
- Version: 3
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
- Toolkit status: Limbo
