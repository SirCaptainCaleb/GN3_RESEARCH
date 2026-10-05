# Path-cover surgery and comparison

**Summary:** A reusable toolkit supplies path-cover surgery, cut interaction, block-count, four-set, component-drop, symmetric-difference, and component-augmentation lemmas.

## Statement

Reusable path-cover surgery, cut interaction and block-count lemmas; two-cover four-set structure; component-drop and Cartesian-clause comparison; weighted matching symmetric difference; and generic boundary-tournament component-augmentation constraints.

## Body

# Path-cover surgery and comparison

## 1. cut interaction forced by an absorbable deletion

Let `H` be a boundary tournament with `pc(H)>2`. Let `D` be a nonempty proper subset of `V(H)`, put `W=V(H)-D`, and let `S` be a nonempty proper subset of `W`. Suppose `H[D union S]` has a Hamilton tight path.

Then every two-path cover of `H-D` contains an ordinary path edge with one endpoint in `S` and the other in `W-S`.

**Proof.** Let `T_1|T_2` be a two-path cover of `H-D` and suppose no ordinary edge of either path crosses the cut `S | (W-S)`. Then each connected path component lies wholly in one side of the cut. Since both sides are nonempty and the two paths cover `W`, after exchanging their names we have

`V(T_1)=S`, `V(T_2)=W-S`.

A Hamilton tight path on `D union S`, together with `T_2`, is then a spanning two-path cover of `H`, contradicting `pc(H)>2`. ∎

## 2. Cyclic rotations of a tight path

Let `P=(p_0,p_1,...,p_r)` be a tight path in a boundary tournament, with `r>=2`. Put

`alpha=(p_r,p_0,p_1)`, `beta=(p_{r-1},p_r,p_0)`.

Then the cyclic rotation

`(p_r,p_0,p_1,...,p_{r-1})`

is tight exactly when `alpha` is tight, and

`(p_1,...,p_r,p_0)`

is tight exactly when `beta` is tight. Consequently exactly one of the following four possibilities occurs:

1. both rotations are tight, in which case `(p_0,p_1,...,p_r,p_0)` is a tight cycle;
2. only the first rotation is tight, and `(p_0,p_r,p_{r-1})` is tight;
3. only the second rotation is tight, and `(p_1,p_0,p_r)` is tight;
4. neither rotation is tight, and both `(p_1,p_0,p_r)` and `(p_0,p_r,p_{r-1})` are tight. If `r>=3`, then `(p_1,p_0,p_r,p_{r-1})` is a tight four-vertex path.

**Proof.** Each rotation preserves every old consecutive triple of `P` except its one displayed wrap triple. Thus the two equivalences are immediate. Boundary antisymmetry gives the reverse of each failed wrap triple, and when both fail and `r>=3` the two reversed triples concatenate. ∎

## 3. Opposite orientations of one end edge absorb every exterior vertex

Let `X` be a vertex set in a boundary tournament, and let `u,v` be distinct vertices of `X`. Suppose `H[X]` has a Hamilton tight path beginning with `(u,v)` and also a Hamilton tight path ending with `(v,u)`.

Then for every `d outside X`, the induced tournament `H[X union {d}]` is Hamiltonian.

**Proof.** Exactly one of `(d,u,v)` and `(v,u,d)` is tight. In the first case prepend `d` to the Hamilton path beginning with `(u,v)`; in the second append `d` to the Hamilton path ending with `(v,u)`. ∎

## 4. Component count after a path-cover edge exchange

Let a spanning tight-path cover on `n` vertices have `q` components, so its ordinary path forest has `n-q` edges. Delete `a` ordinary edges and insert `b` ordinary edges. Suppose the resulting spanning ordinary graph has only path components and cycle components, and that every component carries the corresponding tight path or tight cycle order. Let `c` be the number of cycle components.

Opening each cycle by deleting one of its ordinary cycle edges gives a spanning tight-path cover with

`q' = q-(b-a)+c`

components.

**Proof.** After the exchange there are `n-q-a+b` ordinary edges. Opening the `c` cycles leaves `n-q-a+b-c` edges. A spanning path forest with `q'` components has `n-q'` edges, so

`n-q'=n-q-a+b-c`,

which rearranges to the formula. ∎

## 5. Joining two path-cover components through a Hamilton path

Let `X,Y` partition `V(H)`, and suppose `Y` has a two-path cover

`U=(x,u_1,...,u_r)`, `V=(v_0,...,v_{s-1},y)`

with `r,s>=0`. Suppose `X` is nonempty and `H[X union {x,y}]` has a Hamilton tight path

`Q=(y,q_1,...,q_t,x)`.

Form the spanning vertex order

`K=(v_0,...,v_{s-1},y,q_1,...,q_t,x,u_1,...,u_r)`,

omitting an empty residual prefix or suffix. Every consecutive triple of `K` is tight except possibly

`alpha=(v_{s-1},y,q_1)` when `s>=1`,

and

`beta=(q_t,x,u_1)` when `r>=1`.

If `pc(H)>1`, at least one existing one of `alpha,beta` is not tight. If `pc(H)>2`, then `r,s>=1` and neither `alpha` nor `beta` is tight. Hence in the latter case both

`(q_1,y,v_{s-1})`, `(u_1,x,q_t)`

are tight.

**Proof.** All triples wholly inside the residual part of `V`, inside `Q`, or inside the residual part of `U` are already tight, so the displayed triples are the only possible failures.

If all existing attachment triples were tight, `K` would be a Hamilton tight path, contradicting `pc(H)>1`.

Now suppose `pc(H)>2`. If `K` had at most one non-tight consecutive triple, then cutting `K` at one of the two ordinary edges inside that triple would split `K` into two nonempty tight paths covering all vertices. Thus `H` would have a spanning two-path cover. Therefore `K` has at least two non-tight consecutive triples. Since only `alpha,beta` can fail, both must exist and both must fail. Boundary antisymmetry gives their reverses. ∎

## 6. Transitions across a vertex partition

Let `Pi={X_1,...,X_m}` be a partition of `V(H)` into nonempty sets, and let `T` be a spanning `q`-path cover. Let `t_Pi(T)` be the number of ordinary edges of the paths of `T` whose endpoints lie in different classes of `Pi`.

For each `i`, delete all such cross-class edges and let `b_i(T)` be the number of resulting nonempty path blocks contained in `X_i`. Then

`t_Pi(T)=sum_i b_i(T)-q`

and hence

`t_Pi(T) >= sum_i pc(H[X_i])-q`.

Equality holds exactly when the blocks inside every `X_i` form a minimum path cover of `H[X_i]`.

**Proof.** Deleting one cross-class edge from a path forest increases the number of components by one. Thus all deletions produce exactly `q+t_Pi(T)` blocks, which is `sum_i b_i(T)`. Since the blocks in `X_i` form a path cover of `H[X_i]`, we have `b_i(T)>=pc(H[X_i])`. The inequality and equality condition follow. ∎

## 7. Deletion block count and a unique cut interaction

Let

`V(H)=D disjoint-union S disjoint-union C`,

where `S,C` are nonempty. Suppose `H[D union S]` has a path cover with `a` components. Let `T` be a `k`-path cover of `H-D`. For each component of `T`, cut every ordinary edge with one endpoint in `S` and the other in `C`, and let `b_C(T)` be the total number of nonempty resulting blocks contained in `C`.

Then

`pc(H) <= a+b_C(T)`.

In particular, if `H[D union S]` is Hamiltonian and `pc(H)>k`, then `b_C(T)>=k`.

Under these latter hypotheses, if `T` has exactly one ordinary edge joining `S` to `C`, then exactly one component of `T` meets both sets. That component consists of one nonempty `S`-block followed by one nonempty `C`-block, or vice versa; every other component of `T` lies wholly in `C`.

Assume now that `H` is a boundary tournament and keep these latter hypotheses. If the unique cut interaction edge occurs in the order `x,y` with `x in S` and `y in C`, then for every Hamilton tight path of `H[D union S]` ending with the ordered pair `(p,x)`, the triple

`(y,x,p)`

is tight. Dually, if the unique cut interaction occurs in the order `y,x`, then for every Hamilton tight path of `H[D union S]` beginning with `(x,p)`, the triple

`(p,x,y)`

is tight.

**Proof.** After cutting all `S-C` edges of `T`, the `C`-blocks are disjoint tight paths covering `C`. Together with the given `a`-path cover of `D union S`, they form a spanning path cover of `H`, proving `pc(H)<=a+b_C(T)`.

If `a=1` and `pc(H)>k`, then `pc(H)>=k+1`, so `b_C(T)>=k`. If there is exactly one `S-C` edge in `T`, cutting it produces exactly `k+1` monochromatic blocks. There is at least one `S`-block and at least `k` `C`-blocks, so there is exactly one `S`-block and exactly `k` `C`-blocks. The asserted form of `T` follows.

Suppose the unique cut interaction is `x,y` with `x in S`, `y in C`, and let `Q` be a Hamilton path of `H[D union S]` ending with `(p,x)`. Replace the unique `S`-block of the mixed component of `T` by `Q`, leaving the adjacent `C`-block and every other component unchanged. If `(p,x,y)` were tight, these `k` paths would cover `H`, contradicting `pc(H)>k`. Hence `(p,x,y)` is not tight, so boundary antisymmetry gives `(y,x,p)`. The other orientation is identical after reversing the order of the replacement. ∎

## 8. Two crossings forced by a three-part one-vertex-deletion cover

Let `K` be a boundary tournament with `pc(K)>2`, let `d in V(K)`, and suppose `K-d` has a spanning three-path cover

`C | A | B`

by nonempty tight paths. Put `S=V(A) union V(B)`, and assume:

- `|S|=4` and `K[S]` is non-Hamiltonian;
- `min{|A|,|B|}<=2`; and
- whenever one of `A,B` has order three, its displayed tight ordering can be extended by `d` at one end to a tight four-vertex path.

Then every two-path cover `F` of `K-d` contains at least two ordinary edges whose endpoints lie in different members of the partition

`V(C) | V(A) | V(B)`.

**Proof.** Let `k` be the number of ordinary edges of `F` joining different members of this partition. Since `F` has two components while the partition has three nonempty classes, `k>=1`.

Suppose `k=1`. Cutting the unique cut interaction edge produces exactly three nonempty path blocks. Hence each of `V(C),V(A),V(B)` induces one connected block of `F`, and one of the three classes is an entire component of `F`.

The isolated class cannot be `V(C)`: otherwise the other component of `F` is a tight Hamilton path on `S`, contradicting non-Hamiltonicity of `K[S]`.

Thus one of `A,B` is an entire component of `F`. Every component of a two-path cover of `K-d` has order at least three. Indeed, if a component had order one or two, then adjoining `d` gives a set of order at most three, which is Hamiltonian; replacing that component by a Hamilton path on the enlarged set would give a spanning two-path cover of `K`.

Because `|A|+|B|=4` and `min{|A|,|B|}<=2`, the isolated component therefore has order three and the other of `A,B` has order one. By hypothesis, the displayed three-vertex path extends with `d` to a tight four-vertex path. Replacing that entire component of `F` by the extended path leaves the other component unchanged and yields a spanning two-path cover of `K`, again a contradiction.

Hence `k>=2`. ∎



# Further comparison lemmas



If `P=(p_0,\ldots,p_r)` and `Q=(q_0,\ldots,q_s)` are vertex-disjoint ordered paths, write `PQ` for the concatenated vertex sequence `(p_0,\ldots,p_r,q_0,\ldots,q_s)`. For `0<=i<=j<=r`, write `P[i,j]=(p_i,\ldots,p_j)`.

## 1. Exterior constraints at Hamilton path ends

### Proposition 1.1

Let \`H\` be a boundary tournament, let \`X\subsetneq V(H)\` induce a Hamiltonian boundary tournament, and let \`D\subseteq V(H)-X\` be nonempty. Assume \`H[X\cup\{d\}]\` is non-Hamiltonian for every \`d\in D\`.

If some Hamilton path of \`H[X]\` begins with \`(u,v)\`, then \`(v,u,d)\` is tight for every \`d\in D\`.

If some Hamilton path of \`H[X]\` ends with \`(u,v)\`, then \`(d,v,u)\` is tight for every \`d\in D\`.

Consequently no ordered pair \`(u,v)\` can begin a Hamilton path of \`H[X]\` while \`(v,u)\` ends a Hamilton path of \`H[X]\`.

**Proof.**
Let \`P\` be a Hamilton path of \`H[X]\` beginning with \`(u,v)\`, and fix \`d\in D\`. If \`(d,u,v)\` were tight, prepending \`d\` to \`P\` would give a Hamilton path of \`H[X\cup\{d\}]\`, contrary to hypothesis. Boundary antisymmetry therefore gives \`(v,u,d)\` tight.

Dually, if \`Q\` is a Hamilton path of \`H[X]\` ending with \`(u,v)\` and \`(u,v,d)\` were tight, appending \`d\` would give a Hamilton path of \`H[X\cup\{d\}]\`. Hence \`(d,v,u)\` is tight.

If \`(u,v)\` begins one Hamilton path and \`(v,u)\` ends another, the first conclusion gives \`(v,u,d)\` while the second, applied to the terminal pair \`(v,u)\`, gives \`(d,u,v)\`; these are reverses, a contradiction. ∎

## 2. Cutting one path and adjoining the other two components

### Proposition 2.1

Let \`H\` satisfy \`pc(H)>2\`, and let
\`M=(m_0,\ldots,m_t)\mid A=(a_0,\ldots,a_r)\mid B=(b_0,\ldots,b_s)\`
be a spanning three-path cover by nonempty tight paths.

For every \`0\le i<t\`, consider the two spanning vertex sequences
\`M[0,i]A\` and \`BM[i+1,t]\`.
Every consecutive triple in these sequences is inherited from \`M,A,B\` except possibly the following present triples:
\`(m_{i-1},m_i,a_0)\` when \`i\ge1\`,
\`(m_i,a_0,a_1)\` when \`r\ge1\`,
\`(b_{s-1},b_s,m_{i+1})\` when \`s\ge1\`,
and \`(b_s,m_{i+1},m_{i+2})\` when \`i+2\le t\`.
At least one present triple is non-tight.

The same statement holds after interchanging \`A\` and \`B\`.

**Proof.**
The two displayed vertex sequences are disjoint and span \`V(H)\`. Every consecutive triple lying wholly inside \`M\`, \`A\`, or \`B\` is inherited and tight. At the join from \`M[0,i]\` to \`A\`, the only possible new triples are \`(m_{i-1},m_i,a_0)\` and \`(m_i,a_0,a_1)\` when they exist. At the join from \`B\` to \`M[i+1,t]\`, the only possible new triples are \`(b_{s-1},b_s,m_{i+1})\` and \`(b_s,m_{i+1},m_{i+2})\` when they exist.

If all present new triples were tight, both spanning sequences would be tight paths and would form a spanning two-path cover of \`H\`, contrary to \`pc(H)>2\`. Interchanging \`A,B\` gives the symmetric statement. ∎

## 3. Two-sided concatenation obstruction

### Proposition 3.1

Let \`H\` be a boundary tournament with \`pc(H)>2\` and let
\`V(H)=V(A)\sqcup W\sqcup V(B)\`,
where \`A,B\` are nonempty tight paths and \`W\` has a cover \`P\mid Q\` by two nontrivial tight paths.

Then either neither \`AP\` nor \`AQ\` is tight, or neither \`PB\` nor \`QB\` is tight.

**Proof.**
Suppose \`A\` concatenates with one of \`P,Q\`, say \`P\`. If \`B\` concatenates after \`Q\`, then \`AP\mid QB\` is a spanning two-path cover of \`H\`. If \`B\` concatenates after \`P\`, then \`APB\mid Q\` is a spanning two-path cover: because \`P\` has at least two vertices, every consecutive triple of \`APB\` already occurs in either \`AP\` or \`PB\`. Both are impossible. Therefore, once one left concatenation exists, no right concatenation exists with either middle path. The same argument with left and right interchanged proves the dichotomy. ∎

## 4. Comparing nested deletion covers

### Proposition 4.1

Let \`K\` be a boundary tournament with \`pc(K)>2\`, let \`a,b\` be distinct vertices, let \`F=P\mid Q\` be a two-path cover of \`K-a\` in which the component containing \`b\` is nontrivial, and let \`T=R\mid S\` be a two-path cover of \`K-\{a,b\}\`.

If \`b\` is an endpoint of its component in \`F\`, let \`c\` be its path neighbor. If that component begins \`(b,c,\ldots)\`, then \`(c,b,a)\` is tight. If it ends \`(\ldots,c,b)\`, then \`(a,b,c)\` is tight.

If \`b\` is internal in its component in \`F\`, then deleting \`b\` from \`F\` gives a three-path cover of \`K-\{a,b\}\`, and some ordinary edge of \`T\` has endpoints in two different components of \`F-b\`.

**Proof.**
Suppose first that \`b\` is an endpoint of its component in \`F\`. Because the component is nontrivial, it has a path neighbor \`c\`.

If the component begins \`(b,c,\ldots)\` and \`(a,b,c)\` were tight, prepending \`a\` would enlarge that component to a tight path and, together with the other component of \`F\`, would give a spanning two-path cover of \`K\`. Hence \`(a,b,c)\` is non-tight and \`(c,b,a)\` is tight.

If the component ends \`(\ldots,c,b)\`, the same argument shows that \`(c,b,a)\` cannot be tight, since appending \`a\` would two-cover \`K\`; hence \`(a,b,c)\` is tight.

Now suppose \`b\` is internal in its component of \`F\`. Deleting \`b\` splits that component into two nonempty tight subpaths, while the other component of \`F\` remains nonempty. Thus \`F-b\` is a three-path cover of \`K-\{a,b\}\`. By \`this module\` Section 1, some ordinary edge of the two-path cover \`T\` has endpoints in two distinct components of \`F-b\`. ∎

## 5. Endpoint alternatives after deleting two vertices

### Proposition 5.1

Let \`K\` be a boundary tournament with \`pc(K)>2\`, let \`a,b\` be distinct vertices, and let \`T=P\mid Q\` be a two-path cover of \`K-\{a,b\}\`. If \`P=(p_0,\ldots,p_r)\` with \`r\ge1\`, then each of the following disjunctions holds:

1. \`(p_0,b,a)\` or \`(p_1,p_0,b)\` is tight;
2. \`(p_0,a,b)\` or \`(p_1,p_0,a)\` is tight;
3. \`(a,p_r,p_{r-1})\` or \`(b,a,p_r)\` is tight;
4. \`(b,p_r,p_{r-1})\` or \`(a,b,p_r)\` is tight.

**Proof.**
Prepend \`(a,b)\` to \`P\`. The only new consecutive triples are \`(a,b,p_0)\` and \`(b,p_0,p_1)\`. They cannot both be tight, since otherwise the enlarged path together with \`Q\` would two-cover \`K\`. Reversing a non-tight triple gives \`(p_0,b,a)\` or \`(p_1,p_0,b)\`. Prepending \`(b,a)\` gives the second disjunction.

Appending \`(a,b)\` to \`P\` creates exactly the two possible new triples \`(p_{r-1},p_r,a)\` and \`(p_r,a,b)\`; reversing a non-tight one gives \`(a,p_r,p_{r-1})\` or \`(b,a,p_r)\`. Appending \`(b,a)\` gives the fourth disjunction. ∎


# Four-vertex structure inside two-covers

## 1. Degree and block counts

### Proposition 1.1

Let \`G\` be a boundary tournament with \`V(G)=S\sqcup Q\`, where \`|S|=4\` and \`G[S]\` is non-Hamiltonian. Let \`T\` be a two-path cover of \`G\` in which every vertex of \`S\` has ordinary degree two.

Put
\`e=|E(T[S])|\`,
let \`\delta\` be the number of ordinary edges of \`T\` joining \`S\` to \`Q\`,
and let \`b_Q\` be the number of nonempty components of \`T[Q]\`.

Then
\`e\in\{0,1,2\}\`,
\`\delta=8-2e\`,
and
\`b_Q=6-e\`.
Equivalently, \`(e,\delta,b_Q)\` is one of
\`(2,4,4)\`, \`(1,6,5)\`, \`(0,8,6)\`.

**Proof.**
Since \`G[S]\` is non-Hamiltonian, the path forest \`T[S]\` has at most two ordinary edges, so \`e\in\{0,1,2\}\`.

The sum of ordinary degrees over the four vertices of \`S\` is eight. Each edge of \`T[S]\` contributes two to this sum, while each edge joining \`S\` to \`Q\` contributes one. Hence
\`8=2e+\delta\`,
so \`\delta=8-2e\`.

Cut all \`\delta\` edges joining \`S\` to \`Q\`. The two-path forest becomes \`\delta+2\` maximal blocks lying entirely in one side. Since \`T[S]\` is a forest on four vertices with \`e\` edges, it has \`4-e\` components. Therefore
\`b_Q=(\delta+2)-(4-e)=6-e\`.
The three displayed cases follow. ∎

## 2. Alternation of the resulting blocks

### Proposition 2.1

Under the hypotheses of Proposition 1.1, contract every nonempty component of \`T[S]\` and every nonempty component of \`T[Q]\`. Every contracted component coming from \`S\` has degree two, and each of the two resulting path components alternates between components from \`Q\` and components from \`S\`, beginning and ending with a component from \`Q\`.

**Proof.**
Let \`B\` be one component of \`T[S]\`. Since \`G[S]\` is non-Hamiltonian, \`B\` has order at most three. If \`B\` is a singleton, its unique vertex has total ordinary degree two in \`T\`, so exactly two edges leave \`B\`. If \`B\` has order two, its one internal edge uses one incident edge at each endpoint, leaving exactly one outside edge at each endpoint. If \`B\` has order three, its two internal path edges leave one outside edge at each path endpoint and none at the middle vertex. Thus every contracted component coming from \`S\` has degree two.

After contracting all maximal same-side components, the two path components of the ordinary forest of \`T\` remain paths. Their vertices alternate between the two sides by maximality of the blocks. Since no contracted \`S\`-vertex has degree one, no path endpoint lies in \`S\`. Hence every contracted path begins and ends with a component from \`Q\`. ∎


# Cover-comparison and matching principles

## 1. A component drop forces a cut interaction edge

Let `H` be a boundary tournament and let `W subseteq V(H)`. Suppose `H[W]` has path covers

`R=R_1|...|R_c`

and

`T=T_1|...|T_r`

with `r<c`. Then some ordinary edge `xy` of a component of `T` has its endpoints in two different components of `R`.

If the `R`-component containing `x` is nontrivial and `p` is a neighbor of `x` along that component, then exactly one of

`(y,x,p)`, `(p,x,y)`

is tight.

**Proof.** Suppose every ordinary edge of every component of `T` had both endpoints in one component of `R`. Since each `T_i` is connected, every `T_i` would then lie in a single `R_j`. Because the `T_i` cover `W`, every one of the `c` nonempty components of `R` would contain at least one component of `T`. Distinct components of `R` are disjoint, so these components of `T` would be distinct. Hence `r>=c`, a contradiction.

Thus some edge `xy` of `T` crosses two components of `R`. If the component containing `x` is nontrivial, choose a path neighbor `p` of `x` in that component. The vertices `p,x,y` are distinct, and boundary antisymmetry gives exactly one tight member of the displayed reversal pair. ∎

Each singleton component contains no ordered triple, and every two-vertex ordering is a tight path vacuously. Thus the orders of two singleton components alone impose no tightness condition on any ordered triple of distinct vertices.

## 2. A Cartesian clause lemma

Let `I_1,...,I_m` be nonempty finite sets. For each `j` and each `i in I_j`, let `P_{j,i}` be a Boolean statement. Suppose that for every tuple

`(i_1,...,i_m) in I_1 x ... x I_m`

at least one of

`P_{1,i_1},...,P_{m,i_m}`

is true. Then for some `j`, every statement `P_{j,i}` with `i in I_j` is true.

**Proof.** If no coordinate family were entirely true, choose for every `j` an index `i_j` for which `P_{j,i_j}` is false. The resulting tuple would make all `m` statements false, contradicting the hypothesis. ∎

### Boundary-tournament form

Let `H` be a boundary tournament, and let `k>=1` be an integer with `pc(H)>k`. For `j=1,...,m`, let `{alpha_{j,i}:i in I_j}` be finite families of ordered triples of distinct vertices of `H`, and for each `alpha_{j,i}` let `h_{j,i}` be its reverse.

Assume that for every tuple `(i_1,...,i_m)` there exist `k` pairwise vertex-disjoint vertex-simple sequences whose vertex sets partition `V(H)` and such that:

- every consecutive ordered triple of every sequence, other than the listed triples

  `h_{1,i_1},...,h_{m,i_m}`,

  is tight; and
- each listed triple `h_{j,i_j}` occurs as a consecutive ordered triple of one of the `k` sequences.

Then for some `j`, every triple `alpha_{j,i}`, `i in I_j`, is tight.

**Proof.** Fix a tuple `(i_1,...,i_m)` and the corresponding `k` sequences. If every listed triple `h_{j,i_j}` were tight, then every consecutive triple in every vertex-simple sequence would be tight. The sequences would therefore be `k` tight paths forming a spanning `k`-path cover of `H`, contrary to `pc(H)>k`.

Hence at least one listed triple `h_{j,i_j}` is non-tight. Boundary antisymmetry makes its reverse `alpha_{j,i_j}` tight. Thus for every tuple at least one of the Boolean statements

`P_{j,i_j} := [alpha_{j,i_j} is tight]`

is true. The Cartesian clause lemma gives an index `j` for which every `alpha_{j,i}` is tight. ∎

## 3. A weighted symmetric-difference lemma for two matchings

Let `G=(V,E)` be a finite graph, and let `F` and `J` be matchings in `G`, with

`|F|=|J|+1`.

Let `w:E -> R_{>=0}` be a nonnegative edge weight such that every edge of `J` has weight zero, and suppose

`W=sum_{e in F} w(e)>0`.

Decompose `F triangle J` into its alternating connected components. For such a component `C`, put

`delta(C)=|F intersect C|-|J intersect C|`

and

`omega(C)=sum_{e in F intersect C} w(e)`.

Then exactly one of the following holds:

1. some union `S` of alternating components satisfies

   `sum_{C in S} delta(C)=1`

   and

   `sum_{C in S} omega(C)<W`;

2. there is a unique alternating path `C_*` with `delta(C_*)=1`; it satisfies `omega(C_*)=W`, there is no component with `delta=-1`, and every other alternating component has `delta=0` and weight zero.

**Proof.** Every alternating component of two matchings has `delta in {-1,0,1}`. Moreover

`sum_C delta(C)=|F|-|J|=1`

and

`sum_C omega(C)=W`.

Assume the first conclusion fails. In particular, every component with `delta=1` must have weight at least `W`, because that component alone would otherwise satisfy conclusion 1. Since all component weights are nonnegative, their total is `W`, and `W>0`, there can be at most one component with `delta=1`. The total excess is one, so such a component exists; call it `C_*`. Necessarily `omega(C_*)=W`, and every other component has weight zero.

If some component had `delta=-1`, then with only one component of excess `+1` the sum of all `delta` values could not equal `1`. Thus no such component exists, and every remaining component is balanced. A symmetric-difference component with one more `F`-edge than `J`-edge is an alternating path, so `C_*` is the unique `F`-heavy alternating path. ∎

The positivity hypothesis `W>0` is essential for this formulation: with zero total weight, several zero-weight `F`-heavy components can coexist with `J`-heavy components.

A useful specialization takes `w` to be the indicator of edges cut interaction a fixed vertex partition. If `J` uses no cut interaction edge, the second alternative says that one alternating path contains every cut interaction edge of `F`.


# Boundary-tournament cover augmentation

# Cover augmentation lemmas

## 1. Concatenating two components forces a reversed joining triple

Let `H` be a boundary tournament with `pc(H)>2`, and let

`A|B|C`

be a spanning three-path cover of `H` in which all three components are nontrivial. Write

`A=(a_0,...,a_p)`, `B=(b_0,...,b_q)`

with `p,q>=1`.

If `A` is followed by `B`, the only new consecutive triples are

`(a_{p-1},a_p,b_0)`

and

`(a_p,b_0,b_1)`.

They cannot both be tight. Hence at least one of

`(b_0,a_p,a_{p-1})`, `(b_1,b_0,a_p)`

is tight.

The same conclusion holds for each of the six ordered pairs of distinct components among `A,B,C`.

**Proof.** Every consecutive triple wholly inside `A` or `B` is tight. If both new consecutive triples were tight, the concatenation of `A` and `B` would be a tight path and, together with the untouched third component, would give a spanning two-path cover. Boundary antisymmetry gives the reverse of each non-tight joining triple. ∎



## 6. Cutting a component around a three-vertex component

Let `H` be a boundary tournament with `pc(H)>2`. Suppose

`(a,s,c)|R|Q`

is a spanning three-path cover, where

`R=(u_0,...,u_k)`, `k>=1`.

Then at least one of the following holds:

1. `(s,c,u_0)` is not tight;
2. `(u_k,a,s)` is not tight;
3. `k>=2` and both `(c,u_0,u_1)` and `(u_{k-1},u_k,a)` are not tight.

**Proof.** Delete an edge `u_i u_{i+1}` of `R` and consider the vertex sequence

`(u_{i+1},...,u_k,a,s,c,u_0,...,u_i)`.

Together with `Q`, this would be a spanning two-path cover if every new consecutive triple were tight.

When `k=1`, deleting the sole edge leaves only the two new triples `(u_k,a,s)` and `(s,c,u_0)`, so at least one is non-tight.

Assume `k>=2` and both of those triples are tight. Deleting the first edge of `R` leaves only one additional new triple, `(u_{k-1},u_k,a)`, so it must be non-tight. Deleting the last edge leaves only `(c,u_0,u_1)`, which must also be non-tight. ∎

Boundary antisymmetry supplies the corresponding reversed tight triple whenever one of the displayed joining triples is non-tight.

## 7. Joining two components relative to a fixed two-cover

Let `G` be a boundary tournament. Let

`J=P|Q|R`

be a spanning three-path cover and let `F` be a spanning two-path cover of the same vertex set.

Choose an ordered pair of distinct components, say

`P=(p_0,...,p_k)`, `Q=(q_0,...,q_l)`,

and concatenate them using the ordinary edge `p_k q_0`. The only new consecutive triples that can occur are

`(p_{k-1},p_k,q_0)` when `k>=1`,

and

`(p_k,q_0,q_1)` when `l>=1`.

Hence either one of the displayed triples is non-tight, in which case its reverse is a tight triple on three distinct vertices, or the concatenation gives a spanning two-path cover.

Moreover, among distinct ordinary edges joining endpoints of two components of `J` and used to concatenate those components, at most one can produce the same ordinary path forest as `F`. Consequently there is a concatenation for which either a new consecutive triple is non-tight and supplies its tight reverse, or the resulting two-cover has ordinary path forest different from that of `F`.

**Proof.** Every consecutive triple wholly inside `P,Q,R` is inherited. If both existing new triples are tight, the concatenation of `P` and `Q`, together with `R`, is a two-cover.

Every successful concatenation adds exactly one ordinary edge to the ordinary path forest of `J`. If such a concatenation has the same ordinary forest as `F`, then the forest of `J` is contained in that of `F` and the added joining edge is the unique edge of `F` not already in `J`. Thus at most one distinct joining edge can reconstruct the forest of `F`.

The three unordered pairs of components of `J` supply three distinct ordinary endpoint-joining edges, since the components are pairwise vertex-disjoint. Choose one different from the possible unique edge that reconstructs `F`, orient the corresponding pair of components in either concatenation order, and apply the first assertion. ∎


## Metadata

- ID: coversurg01
- Kind: toolkit
- Version: 5
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
