# Two-hub selector obstruction and cross-hub path interleaving

### A coupled-hub obstruction to independent leaf elimination

The nonlinear star theorem supplies a paired-root hub selector in every leaf fiber. A natural attempt at an interaction-tree induction is to apply the star selector separately at two adjacent hubs and then solve the two selected hub-bit conditions. The following example shows this procedure can fail even when the complete double-star coloring is exceptionally favorable.

**Proposition 1 (incompatible isolated-star selectors but compatible complete paths).** Consider the four-dimensional cube with two adjacent hubs \(a,b\) and one leaf at each hub, called \(u,v\). Use bits \(a,b,u,v\), and color its undirected edges as follows:
\[
\boxed{
f_a=b\oplus u,\qquad
f_b=a\oplus v\oplus1,\qquad
f_u=1-a,\qquad
f_v=1-b.
}
\tag{1}
\]
Every formula is independent of the bit in its own edge direction. Its interaction graph is the path \(u-a-b-v\), a connected double-star.

Fix the leaf configuration \(u=v=0\). When the hub \(b\) is held fixed, the isolated \(a,u\) star has a unique paired root bit \(a=b\). When hub \(a\) is held fixed, the isolated \(b,v\) star has a unique paired root bit \(b=1-a\). Hence the two independently selected hub bits cannot simultaneously satisfy both conditions.

Nevertheless **every** of the four full roots \((a,b,0,0)\) is paired, and in fact each has a monochromatic complete antipodal geodesic. For roots \((a,b)=(0,0),(1,1)\), direction order \(a,b,u,v\) is monochromatic, with respective constant colors zero and one. For roots \((a,b)=(1,0),(0,1)\), direction order \(b,u,a,v\) is monochromatic, again with respective constant colors zero and one.

*Proof.* The local star selectors follow from the sharp connected-star model \(f_{\rm hub}=x_{\rm leaf}\oplus t,\ f_{\rm leaf}=1-s\), whose unique paired hub choice at a fixed leaf root is \(s=x_{\rm leaf}\oplus t\). The first isolated star has \(t=b\), the second \(t=a\oplus1\). These yield the stated inconsistent equations. For the four complete roots, substitute the displayed direction orders into (1). Each traversal uses all directions once, and its four colors are \(0000\) or \(1111\), as indicated. A monochromatic full geodesic qualifies for both orientations at its root. QED.

**Corollary 2 (obstruction to unmodified local-selector gluing).** Even for an affine coloring with a four-vertex path interaction graph, separately chosen star selectors need not have a simultaneous solution. Any tree-induction theorem must permit *interleaving the hub crossings and leaf steps*, rather than imposing an independent paired-root selector at each hub. The phenomenon persists in every dimension \(d\ge4\) after Cartesian multiplication by constant-color single-direction factors.

### Finite test of the two-hub fiber conjecture

For an interaction double-star with two central directions, two leaf groups, and arbitrary nonlinear dependence allowed by the interaction graph, the stronger conjecture is that every fixed assignment of the leaf bits has at least one paired choice of the two hub bits. This has not been proved.

We exhaustively tested two small parameter families to identify sharp local cases:
- \(Q_4\), one leaf at each hub: the permitted edge-color dependence has 12 independent binary parameters. All \(2^{12}=4096\) colorings were enumerated, and for each all four possible leaf configurations were checked. The smallest paired-root count in a four-root hub fiber was one.
- \(Q_5\), two leaves attached to the first hub and one to the second: there are 18 independent edge-color parameters. All \(2^{18}=262144\) assignments were enumerated, with the leaf root fixed to zero; flipping prescribed leaf bits permutes the parameter family, so this suffices for all leaf configurations. Again the minimum hub-fiber paired-root count was one.

Both calculations used a binary subset dynamic program for each root and orientation, in which the state is the used-direction set and whether the unique permitted monotone phase change has happened. These are **finite computational checks**, not a general two-hub theorem.

**Closure direction.** A viable two-hub induction should study the four joint hub states as a *single square-valued interface*, with monotone path certificates that permit leaf steps on either side of both hub crossings. The example (1) rules out the simpler fixed-point approach using independent star selectors. Establishing a four-state interface intersection lemma under arbitrary nonlinear hub functions would extend the all-dimensional star theorem to double-stars and could initiate an interaction-tree reduction.

## A six-dimensional obstruction to fixed-leaf hub selection

The four-type macro compression reduces unrestricted nonlinear two-hub stars to at most six dimensions, but the resulting six-dimensional root interface cannot be solved independently over each fixed leaf assignment.

Let Q_6 have hub bits \(t_0,t_1\) and four leaf bits \(x_2,x_3,x_4,x_5\). Color undirected direction-i edges by the following Boolean functions (all arithmetic in \(\mathbb F_2\)):
\[
\boxed{\begin{aligned}
f_0&=1+x_2+t_1(x_2+x_3),\\
f_1&=1+x_4+t_0(x_4+x_5),\\
f_2&=t_0,\quad f_3=1+t_0,\quad
f_4=t_1,\quad f_5=1+t_1.
\end{aligned}}
\tag{A}
\]
Each f_i is independent of its own bit and hence defines a valid undirected-edge coloring. All four leaf types of the two-hub macro-star are represented.

**Proposition (failure of fixed-leaf selector).** At each root \((t_0,t_1,0,0,0,0)\) with \(t_0,t_1\in\mathbb F_2\), there is NO full dimension-simple antipodal geodesic with word \(0^*1^*\). Nonetheless,
\[
\boxed{|A(f)|=48,\qquad|P(f)|=36}
\tag{B}
\]
among the 64 cube roots. In particular the proposed rule that every fixed leaf assignment allows some favorable, or paired, hub-bit choice is false. This does not refute the conjectured global nine-sixteenths favorable-root bound.

**Reproducible finite certificate.** Fix root z. A state R0(S) means that the dimensions in S can be traversed from z with all edge colors zero. A state R1(S) means they can be traversed with a word \(0^*1^+\). Initialize R0(empty)=true and R1(empty)=false. For unused direction i and current vertex \(v=z+\mathbf1_S\), propagate R0(S) to R0(S union {i}) if \(f_i(v)=0\), and propagate R0(S) or R1(S) to R1(S union {i}) if \(f_i(v)=1\). No other transitions are allowed. Root z is favorable if either terminal state at S=[6] is true.

For the four roots at leaf 0000, the counts of reachable states R0/R1 as subset cardinality grows from 0 to 6 are:
- hubs 00 or 11: R0 counts (1,2,3,4,2,0,0), R1 counts (0,4,14,20,14,4,0);
- hubs 01 or 10: R0 counts (1,2,1,0,0,0,0), R1 counts (0,4,12,14,8,2,0).

Thus the terminal state is unreachable for all four roots. Applying the same recurrence to all 64 roots gives 48 favorable and 36 paired, where pairing means z and its antipode are both favorable. This is a finite exhaustive verification of the six-dimensional example, not an all-dimensional theorem.

**Proof-closure consequence.** Any general two-hub theorem must permit favorable roots to move *between different leaf assignments*. Applying an isolated one-hub selector to each hub, or demanding one favorable hub choice over every fixed leaf assignment, is insufficient. The macro-reduction gives a bounded structured problem, but global compatible root placement remains its unresolved substance.

**Small benchmark.** Exhaustive search over the 256 choices for each hub Boolean color function in the Q4 double-star with one leaf per hub, at normalized leaf offsets, gives a minimum of 9 favorable roots out of 16 and 4 paired roots. The six-dimensional example above shows that its stronger fixed-leaf property does not extrapolate to four leaf types. These computations do not establish the proposed lower bound for arbitrary Q6 two-hub stars.

## Hub-color CNF and a short three-root contradiction

**Theorem (k-hub SAT reduction).** For a coloring with k hub directions, suppose every nonhub edge color is determined by the starting root and the order of the hub flips. Regard the values of all hub-edge color functions as independent Boolean variables. For a specified root z, the assertion that no full dimension-simple antipodal geodesic has color word \(0^*1^*\) is equivalent to a CNF with clause width at most k. In particular, a two-hub bad-root condition is 2-SAT.

*Proof.* Fix any dimension ordering. Its nonhub edge colors are determined, and its k hub steps read at most k hub variables. For each assignment to those hub values that makes the full color word nondecreasing, forbid that assignment with a clause stating at least one accessed variable differs. Conjoin these clauses across all full dimension orders. The root is unfavorable precisely when all forbidden patterns are avoided. QED.

For the four-leaf-type Q6 model, put \(L(x)=x_2+2x_3+4x_4+8x_5\). Let X0,...,X63 be the hub-edge table bits: hub 0 reads \(X_{16x_1+L(x)}\) and hub 1 reads \(X_{32+16x_0+L(x)}\). The leaf colors are \(x_0,1+x_0,x_1,1+x_1\). Encode an initial root as \(\sum_i2^i z_i\).

**Proposition (three-root incompatibility).** No two-hub coloring of this class makes all three initial roots \(0,3,23\) unfavorable.

*Proof.* The following eight forbidden hub assignments are forced if those three roots are all unfavorable: each row supplies a dimension ordering that would otherwise be a full nondecreasing geodesic.

| Root | Order | Forbidden hub values | Resulting path colors |
|---|---|---|---|
|0|240315|X5=0, X55=0|000000|
|3|324150|X55=1, X15=1|011111|
|23|351024|X63=0, X15=0|000000|
|0|240351|X5=0, X63=1|000011|
|3|142035|X48=0, X5=1|001111|
|23|241035|X48=1, X0=1|111111|
|0|041352|X0=0, X52=0|000001|
|3|412035|X52=1, X5=1|111111|

Negating these permitted patterns gives both implication chains
\[
X_5=0\Rightarrow X_{55}=1\Rightarrow X_{15}=0
\Rightarrow X_{63}=1\Rightarrow X_5=1,
\]
\[
X_5=1\Rightarrow X_{48}=1\Rightarrow X_0=0
\Rightarrow X_{52}=1\Rightarrow X_5=0.
\]
Either bit value for X5 forces its opposite. This contradiction proves the proposition. QED.

**Computational checks, not a general theorem.** Each root in the reduced Q6 class yields 66 distinct 2-SAT clauses. All 64 individual root constraints and all 2016 distinct pairs are jointly satisfiable. Among 41664 root triples, 5952 are inconsistent. The corresponding 3-uniform obstruction hypergraph has independence number 32, as certified by integer optimization using one root variable and one inequality per forbidden triple. Therefore triple incompatibilities alone cannot establish the conjectural nine-sixteenths favorable-root lower bound (at most 28 unfavorable roots). Four-root and higher compatibility must enter such a proof.

This gives an intrinsic implication-graph formulation for nonlinear hub interactions, without assuming independent hub selectors. The general two-hub conjecture remains open.

## Computer-assisted sharp two-hub majority and two-branch closure

**Theorem (sharp nine-sixteenths favorable-root bound; computer-assisted).** Let f be any binary edge coloring of Q_(m+2) with two hub directions 0,1, arbitrary nonlinear hub edge-color functions, and every other direction j colored by \(a_j+t_{\eta(j)}\), where eta(j) in {0,1}. Then
\[
\boxed{|A(f)|\ge\frac9{16}2^{m+2},\qquad
|P(f)|\ge\frac18 2^{m+2}.}
\tag{A}
\]
The favorable-root constant is sharp. Sharpness of the paired-root lower bound is not established here.

*All-dimensional reduction.* The established four-type compression groups leaves by their controlling hub and offset bit. Its full-branch expansion preserves full dimension-simple nondecreasing paths and antipodal paired roots. The root-density bound thus reduces to structured two-hub colorings with at most four distinct macro leaves, on at most six dimensions. Missing macro types can be added as independent sink directions with their prescribed hub-controlled colors; since no existing edge color depends on an added bit, the seam-insertion identity duplicates the favorable-root set. It therefore suffices to prove the nine-sixteenths bound on the full four-type Q6 model.

*Finite verified step.* On Q6 let the leaf-edge bits be
\[
f_2=x_0,\ f_3=1+x_0,\ f_4=x_1,\ f_5=1+x_1.
\]
Let L(x)=x_2+2x_3+4x_4+8x_5, and encode the 64 free hub-edge color bits as X0,...,X63, with f0 at x reading \(X_{16x_1+L(x)}\) and f1 at x reading \(X_{32+16x_0+L(x)}\).

For each root z create Boolean indicator b_z. Traverse all 720 dimension orders from z. Each path reads one hub-0 and one hub-1 variable; its other four edge colors are determined by the root and the order. For each pair of hub-value assignments that makes the complete color word nondecreasing, require
\[
\boxed{b_z\Rightarrow(X_u\ne a\ \vee\ X_v\ne b).}
\tag{B}
\]
This is a two-SAT clause conditioned on root un-favorability. The construction yields 66 distinct clauses per root, thus 4224 clauses. Add
\[
\boxed{\sum_{z=0}^{63}b_z\ge29.}
\tag{C}
\]
The resulting finite SMT-LIB formula was verified **UNSAT** with Z3 4.13.3. If any two-hub coloring had at least 29 unfavorable roots, choose b_z=true at 29 of them; the formula would be satisfiable. Contradiction. Hence Q6 has at least 36 favorable roots and the asserted nine-sixteenths bound follows in every dimension by compression.

The generated check input comprises 4224 implication clauses and (C). The generator and SMT-LIB files are named nori_two_hub_sat_certificate.py and nori_two_hub_29_bad_unsat.smt2; their SHA256 fingerprints are respectively 440bb657a03e0024e1035e37d58fb260a66cf23ae3ae9b91294e396ba2aeef70 and 78930da53de38a93e48c94d861d8e6d2d8f29d0313e2290ab4b72cf715074d11. The check script also independently counts roots in the following sharp witness.

*Sharpness.* Choose
\[
f_0=1+x_3,\qquad f_1=1+x_5
\]
and retain the four leaf rules above. This is the Cartesian product of two three-dimensional sharp nonlinear-star colorings, each having 6 favorable roots and 4 paired roots. Thus the six-dimensional product has precisely 36 favorable and 16 paired roots. Paired-root inclusion-exclusion in any n-dimensional coloring gives
\[
|P(f)|=|A(f)\cap\bar A(f)|\ge2|A(f)|-2^n,
\]
giving the one-eighth bound in (A). The displayed witness proves sharpness of the favorable-root bound; its paired-root density is one quarter, so it does not prove sharpness of the one-eighth paired-root bound. \(\square\)

**Corollary (closure of all two-branch dependency components).** If every strongly connected component of the directed dependency graph of an arbitrary cube-edge coloring has at most two vertices with internal indegree greater than one, then the coloring has a paired root.

*Proof.* A terminal SCC with no or one branching target is handled by the earlier directed-cycle or rooted-tree feedback theorem. With two branching targets, the unique-predecessor forest lemma compresses its nonhub trees to a two-hub star. At every fixed outside assignment the component fiber is a coloring of this class, so by (A) at least nine-sixteenths of its roots are favorable. Any two such fiber favorable sets intersect after antipodal complementation in at least
\[
\boxed{(2\cdot9/16-1)2^s=2^{s-3}}
\]
roots for a component of size s. Paired-root fiber gluing therefore removes the terminal SCC. Induct over the component condensation DAG. \(\square\)

**Remaining closure target.** If NORI1 fails, a minimal paired-root counterexample must have a terminal strongly connected dependency component with at least **three independent branching targets**. The bounded hub compression reduces k such targets to at most 3k dimensions, but for k>=3 a general density majority cannot hold, as independent star products show. A cross-fiber intersection principle stronger than majority is still needed. The result above is computer-assisted and does not yet provide an elementary six-dimensional proof or unrestricted NORI1.

## Median structure and robust cross-fiber two-hub gluing

**Theorem (median closure of prescribed unfavorable roots).** Fix a two-hub star leaf template (the controlling hub and offset of each leaf), and let U denote the set of Boolean assignments to all hub-edge table entries. For a root z, let \(\mathcal B_z\subseteq U\) be the assignments for which z has no full geodesic of word \(0^*1^*\). Then \(\mathcal B_z\) is the solution set of a 2-CNF formula. For every set R of prescribed unfavorable roots, the intersection
\[
\boxed{\mathcal B_R=\bigcap_{z\in R}\mathcal B_z}
\]
is closed under the componentwise ternary majority operation.

*Proof.* The previous hub SAT theorem expresses each \(\mathcal B_z\) as a conjunction of clauses with at most two hub-table variables. Intersections retain the 2-CNF form. If three assignments satisfy a two-variable clause, their pointwise majority cannot violate it: if both clause terms were false in the majority, each term would be false in at least two of the three assignments, and the two subsets of size at least two intersect, yielding an input assignment violating the clause. Thus the majority satisfies every clause. \(\square\)

**Corollary (implication-cycle obstruction certificates).** If no hub coloring simultaneously makes all roots in R unfavorable, the joint 2-CNF is unsatisfiable. Consequently its implication digraph contains a hub-bit variable X for which directed paths exist from \(X=0\) to \(X=1\) and back. Each implication has a two-step square-path witness in the underlying root constraints; the eight-path certificate for roots 0,3,23 is an illustrative short instance. This characterization is uniform in the leaf count and nonlinear hub functions.

**Theorem (arbitrary cross-star favorable intersection; computer-assisted via sharp bound).** Let f and g be any two two-hub star edge colorings on the *same* \(Q_d\), with arbitrarily differing nonlinear hub functions, leaf offsets, and leaf-to-hub assignments. Then
\[
\boxed{|A(f)\cap\overline{A(g)}|\ge 2^{d-3}.}
\tag{D}
\]
The two colorings need not share a dependency pattern other than each having at most two hubs and every other direction colored by an affine function of one of its hubs or a constant.

*Proof.* The sharp two-hub computer-assisted theorem gives \(|A(f)|,|A(g)|\ge(9/16)2^d\). Antipodal complement preserves cardinality. Inclusion-exclusion yields the lower bound \((2\cdot9/16-1)2^d=2^{d-3}\). Constant-colored leaves are harmless: their edge colors are independent of every other dimension and a full constant-color leaf traversal can be placed in the appropriate zero or one segment of any favorable full path, so favorable-root density does not diminish under their addition. \(\square\)

**Lemma (fiberwise disappearance of tree predecessor arrows).** Suppose a directed dependency SCC in the full coloring has precisely two branching hubs and every other direction has one predecessor, so its underlying nonhub arrows form outward trees from the two hubs. Fix any outside assignment. The induced fiber coloring can deactivate some parent arrows, leaving \(f_i=a_i+\lambda_i x_{p(i)}\) with \(\lambda_i\in\{0,1\}\). The fiber's favorable-root density remains at least nine-sixteenths, and its paired-root density at least one-eighth.

*Proof.* Remove every inactive parent arrow from the outward trees. The resulting components not attached to either hub are rooted subtrees with a constant-color top edge. Each can be traversed monochromatically in that top color from **every** starting root, by orienting the active descendant parent-child dependencies to attain the same color. The color functions of those components are independent of all directions outside the component: the removed parent arrow has coefficient zero, and the other outgoing dependencies remain inside its descendant tree, while all feedback arrows in the global graph enter the hubs and do not alter edge colors of these tree components. Thus these tree components are Cartesian factors whose favorable-root sets are the entire component cubes. Their insertion at a favorable path's zero-to-one seam (on the zero or one side, as appropriate) preserves all dimensions and color monotonicity. Removing them therefore preserves or increases favorable-root density and paired-root density.

The residual component has two hubs and active outward rooted trees. Apply the monochromatic macro-forest compression to produce a two-hub star with at most two leaf types per hub, and apply the computer-assisted nine-sixteenths theorem. Reinsert the independent monochromatic tree components; every root in them can be used, so the same density lower bound holds for the full fiber. Antipodal inclusion-exclusion yields the paired-root bound. \(\square\)

This supplies the missing fiberwise activation check in the SCC corollary of the nine-sixteenths theorem. Cross-fiber compatibility now holds even if different outside assignments suppress different predecessor arrows and change the active tree shapes. The case of three or more branching hubs remains open; its unfavorable-root constraint is generally 3-CNF or wider, and no analogous majority-closure argument follows automatically.

### Correction to the vanished parent-arrow argument

The conclusion of the inactive-parent SCC lemma remains valid, but its previous claim that detached trees form Cartesian factors of the **entire** coloring was erroneous: hub edge colors may still depend on detached tree bits.

**Correct proof via one-way fiber insertion.** Fix the external bits of a two-branch SCC. Delete inactive parent arrows in the outward predecessor forest. Let A consist of the resulting subtrees detached from both hubs; let B consist of the remaining hub-rooted active forest. Every A-direction edge color is independent of B-bits, because A-direction color functions depend only on active parent bits within their detached subtree, or are constant at the detached top vertex. Hub-direction colors may nevertheless depend arbitrarily on A-bits; no two-sided independence is assumed.

Every root of the A-block is favorable: each detached tree can be traversed monochromatically, in the constant color of its top edge, by orienting its active parent-child relations. Since different A-trees have no dependencies between their edge colors, concatenate their zero-colored full paths followed by their one-colored full paths.

For each A-starting root z, choose a favorable full A-path and its zero-to-one seam y. At fixed y the induced B-fiber has an active outward forest on two hubs, and the published macro-forest compression reduces it to a two-hub star. The computer-assisted theorem gives at least nine-sixteenths favorable roots in *each* such B-fiber. Insert any favorable B-fiber path at seam y. This yields at least ((9/16)2^{|B|}) favorable combined roots above each z, hence
[
\boxed{|A(F)|\ge(9/16)2^{|A|+|B|}.}
]
The bound also holds for every earlier-parameter fiber of the SCC, so any two favorable sets have an antipodally complemented intersection of size at least (2^{|SCC|-3}) by inclusion-exclusion. The paired-root SCC deletion conclusion is therefore unchanged.

This note **supersedes the Cartesian-factor assertion** in the preceding lemma. The correct structural relation is one-way dependence, with detached trees outside and the two-hub core inside; seam insertion, not Cartesian factorization, proves the bound.

## Sharp paired-root density for two-hub stars (computer-assisted)

Let \(f\) be a binary edge coloring of \(Q_n\) with two hub directions \(h,k\). Assume that every nonhub direction \(i\) has color \(f_i(x)=a_i+x_{\eta(i)}\), where \(\eta(i)\in\{h,k\}\) and \(a_i\in\mathbb F_2\); the hub colors are arbitrary Boolean functions. Independent constant-colored directions are harmless.

**Theorem.** Every such coloring has
\[
\boxed{|P(f)|\ge2^{n-2}.}\tag{TP1}
\]
The bound is sharp in arbitrarily large dimensions.

**Reduction.** The previously established four-type compression groups nonhub directions by their hub/offset pair. In each coset of the group-toggle space it produces a coloring on \(Q_{r+2}\), \(r\le4\), whose paired roots all lift to distinct paired roots of the original coloring. Its cosets partition the full starting-root set. Missing macro-leaf types can be inserted as new sink directions reading only a hub. For either prescribed starting bit, any rising or falling macro-path accepts insertion of that direction at its phase seam, so paired roots double per added missing type. Consequently a lower bound of 16 paired roots for the full four-type \(Q_6\) model implies \(2^{n-2}\) paired roots for all two-hub stars.

**Finite model.** The \(Q_6\) canonical leaves have colors
\[
f_2=x_0,\quad f_3=1+x_0,\quad f_4=x_1,\quad f_5=1+x_1.
\]
The hub-0 and hub-1 truth tables each have 32 independent bits \(X_0,\ldots,X_{31}\) and \(X_{32},\ldots,X_{63}\). Write \(L(x)=x_2+2x_3+4x_4+8x_5\); the two hub values are indexed by \(16x_1+L(x)\) and \(32+16x_0+L(x)\).

For each starting root \(z\in Q_6\), enumerate all 720 full dimension orders. Each order reads one variable from each hub table, while its other four colors are fixed by the leaf rule. Record a witness \((u,v,a,b)\) whenever the table assignment \(X_u=a,X_v=b\) yields a nondecreasing full color word. Deduplicating yields 66 witnesses per root, or 4224 total.

Use 64 binary variables \(b_z\) for roots designated nondecreasing-unfavorable, and 32 variables \(d_r\) for antipodal pairs \(\{r,63-r\}\) containing a designated unfavorable root, \(0\le r<32\). For each witness of root \(z\) impose
\[
\boxed{b_z+[X_u=a]+[X_v=b]\le2,}\tag{TP2}
\]
where the bracket denotes the Boolean value of the equality. For each antipodal pair impose
\[
\boxed{d_r\le b_r+b_{63-r}.}\tag{TP3}
\]
Maximize \(\sum_{r=0}^{31}d_r\) over these 160 binary variables. The model has 4256 sparse constraints: 4224 from (TP2) and 32 from (TP3). A root may be declared unfavorable if and only if none of its listed monotone-path witnesses survives. Therefore the optimum equals the maximum number of antipodal root pairs without both endpoints in \(A_0(f)\), namely \(32-\min_f|P(f)|/2\).

**Verified finite optimum.** A reproducible Python 3 / SciPy 1.17.0 mixed-integer solver implementation, using HiGHS, returns optimal objective 24, with both primal and dual bounds equal to 24 and zero gap. Thus \(\min_f|P(f)|=2(32-24)=16\). The execution used 20 branch-and-bound nodes and 46901 LP iterations. This is a computer-assisted theorem, not a claimed elementary proof of the finite optimum.

**Sharpness and independent audit.** With hub truth-table integers
\[
X_{0:31}=\mathtt{0x33333333},\qquad
X_{32:63}=\mathtt{0x00ff00ce},
\]
a separate subset-state dynamic program (not using the MILP witness clauses) obtains 36 nondecreasing-favorable roots and 16 paired roots. The paired-root list, encoding root \(z=\sum_{i=0}^52^i x_i\), is
\[
\{3,7,10,14,19,23,26,30,33,37,40,44,49,53,56,60\}.
\]
Adjoining independent constant-colored directions doubles \(P\) each time, proving sharpness in unbounded dimension.

**Reproduction source.** The script \(\texttt{nori\_two\_hub\_paired\_milp.py}\) produces the witness clauses, solves the integer program, checks its primal and dual optimum, and independently enumerates all full geodesic directions to verify the sharp witness. SHA256: \(\texttt{1237b47895dfd952990f38e2fc3c5f67c0549e8c3fd8ce949f428967d125ab60}\).

**Limit.** The theorem proves the proposed feedback-vertex multiplicity bound for arbitrary nonlinear two-hub stars. It does not cover all colorings with a two-element feedback vertex set, whose nonhub edge colors may depend on several nonhub directions and hence lack the four-type compression.


**Corollary (failure of antipodal nonhub-fiber selectors).** The six-dimensional coloring (A) from the preceding fixed-leaf obstruction has no paired roots among the eight roots whose four nonhub leaf bits are either \(0000\) or \(1111\). Thus even the weaker proposed two-hub selector condition — at least one paired root over each antipodal pair of nonhub leaf assignments — is false.

*Proof.* The earlier finite certificate establishes that no root with nonhub leaf bits \(0000\) lies in \(A_0(f)\). By full-path reversal \(A_1(f)=\overline{A_0(f)}\), so no root with nonhub leaf bits \(1111\) lies in \(A_1(f)\). Neither group can contain a paired root. The coloring remains paired-root-rich globally, with \(|P(f)|=36\), so this is an obstruction to fiberwise induction, not to the global paired-root theorem. \(\square\)


## Correction: owner-local hub lifting and a four-dimensional obstruction

Let \(f,g\) be arbitrary binary colorings of the undirected edges of \(Q_N\). A full root is **rising-favorable** for \(f\) if it supports a dimension-simple antipodal geodesic with word \(0^*1^*\); it is **falling-favorable** for \(g\) if it supports one with word \(1^*0^*\). Write \(A_0(f),A_1(g)\) for their root sets and \(P(f)=A_0(f)\cap A_1(f)\).

Partition the directions into hubs \(H\) and leaves \(L\). The earlier **unconditional opposite-leaf hub lifting assertion (MH1)** and its proof, in the previous composition of this Subsection, are false. The underlying mistake is that a leaf bit can influence several arbitrary hub-edge functions, while inserting that leaf before or after its designated reader hub controls its value at only that hub. The discrepancy invalidates the claimed comparison with hub colorings evaluated at all-zero and all-one leaf vectors.

**Proposition (four-dimensional counterexample to MH1).** On \(Q_4\), put \(H=\{0,1,2\}\), \(L=\{3\}\), and define, over \(\mathbb F_2\),
\[
f_0(x)=x_3,\quad f_3(x)=x_0,\quad
f_1(x)=1+x_2(x_0\lor x_3),\quad
f_2(x)=1+x_1(x_0\lor x_3).
\tag{MH-C1}
\]
All edge-color functions ignore their own direction bit. Let \(u\) and \(v\) be the induced hub colorings with \(x_3=0\) and \(x_3=1\), respectively. Encoding roots by \(r=\sum_{i=0}^3 2^ix_i\), complete full-geodesic enumeration gives
\[
\begin{aligned}
A_0(f)&=\{2,3,4,5,6,7,10,12,14\},\\
P(f)&=\{3,5,10,12\},\\
A_0(u)&=\{1,2,3,4,5,6,7\},\\
A_0(v)&=\{2,3,4,5,6,7\}.
\end{aligned}
\]
Since \(A_1(v)=\overline{A_0(v)}\), with complementation in three hub bits,
\[
\boxed{A_0(u)\cap A_1(v)=\{1,2,3,4,5\},\qquad
|P(f)|=4<5.}\tag{MH-C2}
\]
In particular hub root \(1\) is in the right-hand intersection, yet neither full root above it is paired. These claims follow by a subset-state dynamic program for the rising and falling phase; an independent implementation additionally enumerates all direction permutations. A reproducible checker is \(\texttt{nori\_mh1\_counterexample\_check.py}\), SHA256
\(\texttt{1ebe9179e6287ef11b12e2e19bfd3dc72baf7d3317af3cc7488e1434d4622c71}\). \(\square\)

The counterexample refutes the old inequality as well as its claimed lifting of each hub root. It does **not** disprove any of the earlier numerical bounds for paired roots of unrestricted three- or four-hub stars; those bounds need independent proofs. In particular the unrestricted claims previously labeled MH2--MH5 and the SCC consequences CH2 based solely on MH1 are not established by their published arguments. The sharpened two-hub paired-root theorem elsewhere in this Subsection is logically separate from MH1.

**Theorem (valid owner-local cross-hub lifting).** Suppose \(f\) and \(g\) have the same unary leaf-edge functions
\[
f_i(x)=g_i(x)=a_i+\lambda_i x_{p(i)}
\quad (i\in L),\qquad p(i)\in H,\quad
a_i,\lambda_i\in\mathbb F_2,
\tag{MH-C3}
\]
and for each leaf \(i\), every hub \(h\ne p(i)\) has both hub-edge functions \(f_h,g_h\) independent of \(x_i\). The hub functions may otherwise be nonlinear and may read their own leaves and other hub bits. Let \(u\) be the hub coloring of \(f\) with all leaf bits set to zero, and \(v\) the hub coloring of \(g\) with all leaf bits set to one. Then each \(z\in A_0(u)\cap A_1(v)\) extends to a root in \(A_0(f)\cap A_1(g)\), and
\[
\boxed{|A_0(f)\cap A_1(g)|\ge |A_0(u)\cap A_1(v)|.}\tag{MH-C4}
\]

*Proof.* Fix hub-root \(z\) in the intersection, a rising full hub order under \(u\), and a falling full hub order under \(v\). Denote the corresponding hub-step colors by \(U_h,V_h\), respectively. For a leaf \(i\) with parent \(h=p(i)\), set \(a=f_i(z_h)=g_i(z_h)\) and \(b=f_i(1-z_h)=g_i(1-z_h)\). At least one of
\[
(a\le U_h\ \land\ b\le V_h)
\quad\text{or}\quad
(U_h\le b\ \land\ V_h\le a)
\tag{MH-C5}
\]
holds for binary \(a,b,U_h,V_h\). Indeed for \((U_h,V_h)=(0,0)\) the second holds automatically; for \((1,1)\) the first holds; for \((0,1)\) use the first if \(a=0\) and otherwise the second; for \((1,0)\) use the first if \(b=0\) and otherwise the second.

In the first alternative give \(i\) initial bit one, traverse \(i\) before \(h\) in the rising order and after \(h\) in the falling order. The leaf colors are \(a\) and \(b\), and the parent sees bit zero in the rising order and one in the falling order. The inequalities permit \(i\)'s insertion without introducing a prohibited color change. In the second alternative give \(i\) initial bit zero, traverse \(i\) after \(h\) in the rising order and before \(h\) in the falling order. The same parent-bit observations hold, while the leaf colors are \(b\) and \(a\), compatible with the other inequalities.

Choose independently for all leaves. By the owner-local assumption a leaf has no effect on another hub, so every hub step retains its prescribed color under \(u\) or \(v\). Each prescribed full hub order, together with the pendant-leaf precedence relations, defines an acyclic precedence relation. Every such relation respects the corresponding color-phase order, so a linear extension gives a rising \(f\)-geodesic and a falling \(g\)-geodesic from one common full root. Distinct \(z\) produce distinct full starting roots, proving (MH-C4). \(\square\)

**Conditional hub consequences.** Under (MH-C3) and the owner-local hypothesis, arbitrary hub rules with \(|H|=3\) have at least four cross-orientation roots, since every ordinary coloring of \(Q_3\) has at least six rising-favorable roots and \(6+6-8=4\). For \(|H|=4\), the recorded finite \(Q_4\) favorable-root minimum of nine gives at least \(9+9-16=2\). Taking \(f=g\) gives corresponding paired-root bounds. Componentwise seam lifting remains available when each strongly connected component has these owner-local rules, unchanged under conditioning on earlier components. No unrestricted three- or four-hub conclusion follows from this corrected argument.

## Sharp cross-favorability obstruction with differing leaf rules

The earlier two-hub cross-root bound
\[
|A_0(f)\cap A_1(g)|\ge 2^{n-3}
\tag{XC1}
\]
for two arbitrary two-hub stars on \(Q_n\), obtained from the nine-sixteenths individual favorable-root theorem by inclusion-exclusion, is sharp even if \(f,g\) have the same hub set. In particular, a proposed strengthening of (XC1) to \(2^{n-2}\) when their leaf rules may differ is false.

**Proposition (affine six-dimensional sharpness).** Take common hubs \(0,1\) and define
\[
\begin{aligned}
f_0&=1+x_2,& f_1&=1+x_3,& f_2&=1+x_0,&
f_3&=1+x_1,& f_4&=x_0,& f_5&=x_1,\\
g_0&=1+x_3,& g_1&=1+x_2,& g_2&=1+x_1,&
g_3&=1+x_0,& g_4&=x_0,& g_5&=x_1.
\end{aligned}\tag{XC2}
\]
Then
\[
\boxed{|A_0(f)|=|A_0(g)|=36,\quad |P(f)|=|P(g)|=16,\quad
|A_0(f)\cap A_1(g)|=8.}\tag{XC3}
\]
The common roots, encoded by \(r=\sum_{i=0}^5 2^ix_i\), are
\(\{3,12,19,28,35,44,51,60\}\).

*Proof.* Consider the three-direction star with bits \(h,b,a\) and colors \(q_h=1+x_b,\ q_b=1+x_h,\ q_a=x_h\). Its rising-favorable roots are all roots except those with \(x_h=x_b=0\): at \(00\), the first of the two \(h,b\) steps has color one and the second color zero; at \(01,10,11\), respectively, the orders \(h,b,a\), \(b,h,a\), and \(h,a,b\) have nondecreasing color words. Its falling-favorable roots consequently exclude only \(x_h=x_b=1\). The independent \(a\)-bit does not affect either restriction.

Coloring \(f\) is the Cartesian product of the two stars with hub-critical pairs \((0,2),(1,3)\), and \(g\) uses pairs \((0,3),(1,2)\). Their common cross-root condition forbids \((x_0,x_2)=(0,0)\), \((x_1,x_3)=(0,0)\), \((x_0,x_3)=(1,1)\), and \((x_1,x_2)=(1,1)\). Only \((x_0,x_1,x_2,x_3)=(0,0,1,1)\) and \((1,1,0,0)\) remain. The two auxiliary bits are free, giving eight common roots. Each star has six rising roots and four paired roots, giving the other counts by Cartesian products. \(\square\)

**Theorem (cyclic obstruction in every number of hubs).** For \(k\ge1\), take \(3k\) directions partitioned as hubs \(h_i\), critical leaves \(b_i\), and auxiliary leaves \(a_i\), with \(i\in\mathbb Z/k\mathbb Z\). Define
\[
\begin{array}{lll}
f_{h_i}=1+x_{b_i}, & f_{b_i}=1+x_{h_i}, & f_{a_i}=x_{h_i},\\
g_{h_i}=1+x_{b_{i+1}}, & g_{b_{i+1}}=1+x_{h_i}, & g_{a_i}=x_{h_i}.
\end{array}\tag{XC4}
\]
Then
\[
\boxed{|A_0(f)|=|A_0(g)|=6^k,\quad
|P(f)|=|P(g)|=4^k,\quad
|A_0(f)\cap A_1(g)|=2^{k+1}.}\tag{XC5}
\]

*Proof.* Each coloring is a Cartesian product of \(k\) copies of the preceding three-direction star, proving its two individual counts. Rising favorability for \(f\) excludes the pair \(h_i=b_i=0\) for every \(i\). Falling favorability for \(g\) excludes \(h_i=b_{i+1}=1\) for every \(i\). An index \(i\) with \(h_{i-1}=1,h_i=0\) would force both \(b_i=0\) and \(b_i=1\). Thus no cyclic transition \(1\to0\) is possible, forcing every hub bit to be constant. When all hubs are zero, all critical leaves must be one; when all hubs are one, all critical leaves must be zero. The \(k\) auxiliary leaf bits are arbitrary, giving \(2\cdot2^k\) common roots. \(\square\)

The cross-root density \(2^{k+1-3k}=2^{1-2k}\) decays exponentially, although \(|P(f)|=|P(g)|=4^k\). Each coloring attains the feedback-vertex multiplicity count for a graph of \(k\) disjoint two-cycles with pendant leaves. Therefore individual paired-root multiplicity alone cannot control the overlap of two unrelated favorable-root sets. These examples change the parent assignments of some critical leaves; they do not refute the owner-local shared-leaf theorem above.

**Independent audits.** Complete subset-state geodesic enumeration verified (XC3) and (XC5) for \(k=1,2,3\). The checker \(\texttt{nori\_cross\_star\_cycle\_check.py}\) has SHA256 \(\texttt{f4caa3e78071a032556597dbf65cb067e318000377c378e938b4751f58997e9b}\). The proofs above establish the mathematical statements in all claimed dimensions.


## Twin-leaf contraction and finite cross-root obstruction kernels

Fix k hub directions H. Let f,g be arbitrary ordinary binary edge colorings with every nonhub direction i having local rules f_i=F_i(x_H), g_i=G_i(x_H). All hub-direction edge rules may depend arbitrarily on all other bits.

**Lemma.** If two nonhub directions i,j have identical ordered local rules (F_i,G_i)=(F_j,G_j), delete j and, in every hub rule of both colorings, substitute x_j=x_i. Denote the smaller pair by f',g'. Then
\[
\boxed{|A_0(f)\cap A_1(g)|\ge |A_0(f')\cap A_1(g')|.}\tag{KL1}
\]

*Proof.* For each cross-favorable root of f',g', duplicate its initial i-bit into j. In both monotone dimension orders, replace step i by consecutive steps i,j. They have the same color because their local functions are identical and no hub bit changes between these consecutive steps. All hub steps encounter equal i- and j-bits, since both steps occur consecutively, so their nonlinear color rules equal the restricted functions in f',g'. Other nonhub edge colors depend only on hub bits and also remain unchanged. Thus the rising and falling color words are obtained by duplicating an entry, preserving monotonicity. Both resulting paths are full geodesics from the same lifted root; different small roots give different large roots. \(\square\)

**Theorem (dimension-uniform finite kernel).** If cross-favorability fails for a pair in this k-hub class, it fails for a pair of dimension at most
\[
\boxed{k+2^{\,2^{k+1}}.}\tag{KL2}
\]
For the one-color paired-root property the corresponding bound is \(k+2^{2^k}\). If nonhub functions are restricted to constants or signed one-bit hub readers, these bounds improve to
\[
\boxed{k+(2+2k)^2,\qquad k+2+2k.}\tag{KL3}
\]
Thus for three hubs, all-dimensional two-color cross-favorability with independently varying unary leaf rules reduces to a finite problem on cubes of order at most 67.

*Proof.* There are \(2^{2^k}\) Boolean functions on k bits; consequently at most \(2^{2^{k+1}}\) ordered pairs of such functions. Contract repeated joint leaf types by the lemma. Failure persists through the contractions. For one coloring, use only one function per type. With unary readers the available functions are the two constants and the two signed readers for each hub, yielding \(2+2k\) types. \(\square\)

This reduces the all-dimensional varying-leaf SCC gluing problem to a finite verification for fixed k, without assuming affinity or restricting nonlinear hub rules. The 67-direction verification for k=3 remains open; this is not unrestricted NORI1 closure. A randomized independent audit checked the root lift in 800 nonlinear instances with three hubs and two duplicate leaves.


## Cyclically changing three-hub readers: all-dimensional cross-favorability

The twin-leaf kernel permits a nontrivial finite certificate to close an unbounded-dimensional cross-root branch with **different** leaf reader directions in the two colorings.

**Theorem (three-hub cyclic-reader cross theorem, computer-assisted finite base).** Let H={h_0,h_1,h_2} be three hubs and partition all nonhub directions into arbitrary groups L_0,L_1,L_2, possibly empty. Fix bits a_i,b_i for i in {0,1,2}. Suppose two ordinary binary edge colorings f,g obey, for every leaf w in L_i,
\[
\boxed{ f_w(x)=x_{h_i}+a_i,\qquad
g_w(x)=x_{h_{i-1}}+b_i \pmod2,}
\tag{CY1}
\]
with hub subscripts modulo three. The six hub functions f_{h_i},g_{h_i} are arbitrary Boolean functions of all other direction bits. Then
\[
\boxed{A_0(f)\cap A_1(g)\ne\varnothing.}\tag{CY2}
\]
The conclusion holds in every dimension, with unbounded leaf multiplicities and unrestricted nonlinear hub feedback.

*Reduction to six dimensions.* By the twin-leaf contraction lemma, repeated leaves of one group and type can be identified without destroying a cross-root-free counterexample. Thus a hypothetical failure yields a failure with at most one leaf in each group. If a group is absent, adjoin a new leaf with its stipulated rules, and make all hub functions independent of that new bit. Any cross-favorable paths in the enlarged pair project, after deleting the new direction, to cross-favorable full paths in the original pair. It is therefore sufficient to treat three hubs and one leaf in each of the three groups.

Translate the starting hub bits simultaneously in f and g to absorb the three a_i offsets. The remaining offsets are \(\delta_i=b_i+a_{i-1}\). Cyclically permuting the three hub/leaf labels rotates \(\delta\), so its eight possible words reduce to four representatives
\[
\boxed{000,\quad100,\quad110,\quad111.}\tag{CY3}
\]
It remains to establish the asserted cross-intersection for these four pairs of colorings on Q_6.

**Finite unsatisfiability certificate.** Label the hub directions 0,1,2, leaves 3,4,5. In the normalized model, f_{3+i}=x_i and g_{3+i}=x_{i-1}+\delta_i. Each of the three hub-direction functions has 32 independent edge colors, yielding 96 Boolean variables for f and 96 for g.

For each of 64 roots z and each of 720 direction orders, read the three hub-edge variables and the three prescribed leaf colors. Enumerate the eight assignments to the three hub values, retaining those that make the entire six-edge word nondecreasing. Deduplication gives 24,000 root/path-pattern witnesses for each coloring. Introduce flags u_z,v_z asserting that z is rising-unfavorable in f,g respectively. For every rising path pattern with three hub assignments \(X_{j_t}=\epsilon_t\), impose
\[
u_z\ \Longrightarrow\ \bigvee_{t=1}^3(X_{j_t}\ne\epsilon_t),
\tag{CY4}
\]
and analogously for v_z and the g variables. Add the 64 clauses
\[
\boxed{u_z\vee v_{\bar z}.}\tag{CY5}
\]
Because \(A_1(g)=\overline{A_0(g)}\), the conjunction of (CY4)--(CY5) is satisfiable if and only if some choice of nonlinear hub functions makes (CY2) fail.

For each offset representative (CY3), the full 48,064-clause formula is **UNSAT**, checked with Z3 4.13.3. The four deterministic SMT-LIB SHA-256 digests, in (CY3) order, are:

- 80a596085d12c4a230eaeee4d5aa2f1fa372bd4349ef10e2b5f0b064e104b64e
- 102079cc84306e8abecce42f73943e326fb025434d574566e4cdcb02305f5a5b
- 82202f5131e0025274b4f120ccc44e3efd7316c8060682d65b61559feb823383
- c691cda93d534ce49af46f8e4e70c6ab5f0702d62fe4e7b6096a7801fb2c5aef

The standalone Python/libz3 generator and checker is named nori_cyclic_reader_cross_verify.py (SHA-256 6cabdac8c33bdf70ea6f395b4d49c03c5a85b35e29f765a3bf6611a8ca54d153). Its full-path witness semantics were separately audited against subset-state geodesic reachability for 100 random nonlinear hub assignments in each of the two principal reader templates, with no discrepancies. The reduction preceding the finite check is analytic and valid in every dimension. \(\square\)

**Scope.** This proves a dimension-uniform two-color compatibility theorem despite a cyclic change of nonhub readers. It is not universal three-hub cross-favorability: within each group the two color offsets are fixed, and only the particular cyclic reader change (CY1) is certified. Arbitrarily varying leaf offsets within a group or nonlinear multi-hub leaf rules require further arguments.


## Full three-hub permutation-reader cross theorem

The earlier unconditional hub lifting (MH1) was refuted by a separate owner-local audit. The theorem below does **not** invoke MH1, its three-hub corollary, or an unproved independent-leaf polarization. It uses the rigorously established twin-leaf contraction (KL1) and a complete six-dimensional SAT certificate.

**Theorem (arbitrary permutations of three reader hubs, computer-assisted finite core).** Fix hubs H={h_0,h_1,h_2} and partition all nonhub directions into three groups L_0,L_1,L_2 of arbitrary sizes, including zero. Suppose f,g are two binary undirected-edge colorings such that, for every leaf w in group L_i,
\[
\boxed{
f_w(x)=x_{h_{\sigma(i)}}+a_i,\qquad
g_w(x)=x_{h_{\tau(i)}}+b_i \pmod2,
}\tag{PRH1}
\]
where \(\sigma,\tau\in S_3\) are any permutations and \(a_i,b_i\in\mathbb F_2\). All six hub-direction functions are unrestricted nonlinear Boolean functions of the other hub and nonhub bits. Then
\[
\boxed{A_0(f)\cap A_1(g)\ne\varnothing.}\tag{PRH2}
\]

*Proof.* First contract every repeated leaf within each group using (KL1); a missing group can be supplied with a dummy leaf, with both hub colorings independent of its bit. If cross-favorability holds after adding such a dummy leaf, deleting its step from both monotone paths proves cross-favorability before addition. It is therefore sufficient to prove (PRH2) on Q_6 with one leaf in each group.

Rename the hubs and groups to make \(\sigma=\mathrm{id}\), and translate hub starting bits to absorb all \(a_i\). The remaining reader permutation \(\tau\) is defined up to conjugation in \(S_3\), and the residual three offsets are permuted by the centralizer of \(\tau\). The finite cases consist of:
\[
\begin{array}{c|c|l}
\tau&\text{type}&\text{offset representatives}\\
(0,1,2)&\mathrm{id}&000,100,110,111\\
(1,0,2)&\text{transposition}&000,001,100,101,110,111\\
(2,0,1)&\text{three-cycle}&000,100,110,111 .
\end{array}\tag{PRH3}
\]
These 14 representatives exhaust the possible six-dimensional reader arrangements and color offsets up to the stated cube symmetries.

For each normalized pair, allow **all** \(2^{96}\) independent three-hub edge tables in f and all \(2^{96}\) in g. At every cube root enumerate 720 dimension orders. For each order enumerate the eight assignments of the three encountered hub-edge bits and record those yielding a nondecreasing six-bit path word. After deduplication there are 24,000 favorable-root witness patterns in each coloring. Encode a Boolean variable \(u_z\) saying the first coloring has no nondecreasing full geodesic from root z, and \(v_z\) analogously for the second coloring. For each witness pattern with hub bits \(X_{j_s}=\epsilon_s\), impose the clause
\[
u_z\ \Longrightarrow\ \bigvee_{s=1}^{3}(X_{j_s}\ne\epsilon_s),
\tag{PRH4}
\]
and analogously for g. Finally impose \(u_z\lor v_{\bar z}\) for each root z. The last condition forces failure of (PRH2), since \(A_1(g)=\overline{A_0(g)}\).

Each resulting SMT-LIB formula has 192 hub variables, 128 unfavorable-root flags, 48,000 three-hub witness clauses, and 64 root-cover clauses. **All 14 formulas are unsatisfiable**, checked with Z3 4.13.3 through its C API. A deterministic standalone generator/verifier, nori_three_hub_permuted_reader_verify.py, has SHA-256
\[
\texttt{26fe75175182b75960434fb596368cac57ce8ac3e2d367178206fd495c0604fb}.
\]
The SHA-256 of its 14 concatenated SMT-LIB certificates, in the displayed class/offset order, is
\[
\texttt{de43c49fea89fd9c5e3472c15117a7646bb2e49dba465e102cc191222741b326}.
\]
An independent subset-state evaluator agreed with the root-favorability witness clauses on 112 randomized nonlinear hub assignments distributed across all 14 normalized templates. Thus (PRH2) holds in the six-dimensional core, and the initial contraction and dummy-leaf steps establish it for arbitrary group multiplicities. \(\square\)

**Significance and limits.** This is a positive all-dimensional two-color cross-root theorem allowing the three leaf reader assignments, offsets, and hub truth tables to differ completely between the two colorings, subject only to the requirement that each coloring's group-to-hub assignment is a permutation with one signed reader rule shared within each group. No owner-local restriction is imposed; a hub can read every leaf in every group. More general leaf maps with repeated readers, different offsets *within* the same group, and multi-hub nonlinear leaf rules are not covered. The unrestricted NORI1 conjecture remains open.


## One-bijective-reader nonlinear three-hub cross theorem

**Theorem (computer-assisted finite core, all-dimensional conclusion).** Fix three hubs h_0,h_1,h_2 and three fixed disjoint leaf groups L_0,L_1,L_2 of arbitrary multiplicities. Let f,g be arbitrary binary edge colorings such that
\[
f_w(x)=x_{h_{\sigma(i)}}+a_i,\quad
g_w(x)=x_{h_{\tau(i)}}+b_i\pmod2
\quad(w\in L_i),\tag{OM1}
\]
with \(\sigma\) a permutation of the three hubs, \(\tau\) **any** map from three groups to three hubs, and offsets a_i,b_i fixed within each group. All hub edge-color functions may be unrestricted nonlinear Boolean functions of every other bit. Then
\[
\boxed{A_0(f)\cap A_1(g)\ne\varnothing.}\tag{OM2}
\]
The conclusion is symmetric when g has the bijective reader map, by complementing starting roots and interchanging the colorings.

*Proof.* Contract all duplicate joint leaf types by the twin-leaf lemma (KL1). Add a dummy leaf to any absent group, with all hub functions independent of its bit; a common pair of monotone paths in the enlarged cube projects to one in the original. Thus a counterexample would produce one on Q_6 with three hubs and three distinct leaves. Normalize \(\sigma\) to the identity by relabeling the hubs, and normalize the f offsets by translating hub bits. Simultaneous relabeling of the hubs and their indexed leaf groups now acts by conjugation on \(\tau\), and its stabilizer permutes the residual binary offsets.

There are seven conjugacy classes of three-element maps, represented in image-word notation by
\[
000,\ 001,\ 002,\ 012,\ 021,\ 100,\ 120.
\]
Their numbers of offset orbits are respectively \(6,8,8,4,6,8,4\), totaling **44** reduced Q_6 cases.

In each case, introduce 96 independent hub-edge bits in each coloring and Boolean flags declaring which of the 64 roots are rising-unfavorable. Enumerate all 720 full dimension orders from each root and all eight assignments to their three encountered hub bits. Every assignment yielding a nondecreasing word contributes a clause forbidding it when that root is flagged unfavorable. There are 24,000 deduplicated clauses per coloring. Add 64 clauses insisting that, for each root z, either f is rising-unfavorable at z or g is rising-unfavorable at bar z. Since \(A_1(g)=\overline{A_0(g)}\), the 48,064-clause formula is satisfiable if and only if (OM2) can fail.

All **44** formulas are UNSAT, verified using Z3 4.13.3. The standalone deterministic generator/checker nori_three_hub_one_permutation_verify.py has SHA-256
\[
\texttt{62194bf57b8281f250ee3a178c1e66ed4a8ce489d6f8cf2a2d08fe81e3934acc}.
\]
The two 22-case batches have combined SMT-LIB SHA-256 hashes
\[
\texttt{6e95fb63582a68c9cce568d227e039407b7b489f6e057eb79fc93ac8aa616fb3}
\]
and
\[
\texttt{eac287dae0ed7b7a3f49bffb39cffd69c2654b4a8fa8d1a18d84af9d3db99c33}.
\]
The witness-generation semantics were also checked against independent subset-state reachability on random nonlinear instances. The finite result and the initial contraction prove the theorem in every dimension. \(\square\)

**Scope.** This proves cross-root compatibility even if the second conditional coloring assigns several leaf groups to one hub. It does not establish compatibility when **both** reader maps may be nonbijective, or when signs vary within one fixed group. It does not rely on the earlier withdrawn unrestricted hub-polarization claim.


## All three-hub signed-reader maps: sharp finite majority and global cross closure

**Lemma (computer-assisted nonlinear Q6 majority).** Label directions 0,1,2 as hubs and 3,4,5 as leaves. Let each leaf i=3+j have color \(f_i(x)=x_{\rho(j)}+\epsilon_j\pmod2\), with \(\rho:\{0,1,2\}\to\{0,1,2\}\) nonbijective and arbitrary signs. The three hub functions may depend arbitrarily on all other bits. Then
\[
\boxed{|A_0(f)|=|A_1(f)|\ge36.}\tag{NM1}
\]
All nonbijective reader/sign types attain 36.

*Proof.* Independently relabeling hubs and leaves, and translating individual hub bits, reduces all possibilities to the following four cases (reader image word, signs):
\[
\boxed{(000,000),\ (000,010),\ (001,000),\ (001,010).}\tag{NM2}
\]
They represent respectively three equal readers with equal signs or one opposite sign, and two equal readers with equal or opposite signs, plus a singleton reader.

For each case, assign independent Boolean variables to all 96 hub-direction edge colors. Enumerate all 64 roots, 720 direction permutations and eight choices of values on the three encountered hub edges. Retain each choice yielding a nondecreasing six-edge word, and deduplicate the resulting triple conditions at each root. Introduce a flag \(U_z\) for every root, and require \(U_z\) to exclude every favorable triple condition at z. Finally require
\[
\sum_{z\in Q_6}\mathbf1_{U_z}\ge29. \tag{NM3}
\]
This formula is satisfiable if and only if some assignment of the unrestricted nonlinear hub tables has fewer than 36 favorable roots. Z3 4.13.3 reports **UNSAT** for all four cases (NM2). Changing 29 to 28 produces **SAT** for all four, proving the optimality of 36.

A standalone Python 3/libz3 verifier, nori_three_hub_majority_verifier.py, has SHA-256
\(\texttt{3cfe28da736a1231647d5ea87254d5f2e164925f1dcdeb32f1e3d8c01d242038}\).
An independently programmed subset-state geodesic evaluator agreed with the finite witness encoding in 12,800 randomized full-root comparisons. The bound is computer-assisted; the combinatorial symmetry reduction is analytic. \(\square\)

**Theorem (all reader maps, dimension-uniform three-hub cross-root closure).** Let f,g be two ordinary binary colorings of a cube with three hubs \(h_0,h_1,h_2\) and three fixed nonhub groups \(L_0,L_1,L_2\) of arbitrary multiplicity. Their hub-edge color functions may be arbitrary nonlinear functions of all other bits. Suppose each leaf w in group L_i satisfies
\[
\boxed{f_w=x_{h_{\rho(i)}}+a_i,\qquad
g_w=x_{h_{\tau(i)}}+b_i\pmod2,}\tag{NM4}
\]
where both reader assignments \(\rho,\tau\) are arbitrary three-element maps and a_i,b_i are arbitrary binary offsets, uniform within each group. Then
\[
\boxed{A_0(f)\cap A_1(g)\ne\varnothing.}\tag{NM5}
\]

*Proof.* Clone-contract repeated leaves within each group using the twin-leaf lemma, and supply a harmless dummy leaf for any absent group. A common favorable root in the resulting six-dimensional pair lifts to all cloned leaves, and deleting dummy steps preserves monotonicity. It is enough to treat Q6 with one leaf per group. If at least one of the two reader maps is bijective, apply the proved 44-case one-bijective-reader cross theorem (OM2), using root complementation and exchanging the two colorings if necessary. Otherwise both maps are nonbijective. The preceding lemma gives
\[
|A_0(f)|\ge36,\qquad |A_1(g)|=|A_0(g)|\ge36,
\]
so inclusion-exclusion on 64 roots yields
\[
\boxed{|A_0(f)\cap A_1(g)|\ge8.}\tag{NM6}
\]
Thus a common root exists and survives the inverse clone expansion and dummy deletion. \(\square\)

**Scope.** The theorem covers *every* pair of three-group reader maps, including reader collisions on both sides and arbitrary nonlinear hub feedback, in every dimension. It does not cover leaf groups with different signed readers within the same group, nonlinear leaf functions, or the unrestricted paired-root conjecture.
