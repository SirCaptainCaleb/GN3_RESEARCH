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
