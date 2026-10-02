# Route 4 — Incidence rank / induced-path clique-cover

## Statement

Comprehensive synthesis of the algebraic upper-bound route through the incidence matrix, induced-path-free intersection graph, exact clique-cover realizability, and weighted/nullity rank inequalities.

## Body

# Route 4. Incidence rank and the induced-path clique-cover model

## Goal and setup

Let H be an n-vertex linear 3-uniform hypergraph with m edges, and let N be its n×m vertex-edge incidence matrix over the reals. Let F be the intersection graph of H: the vertices of F are the hyperedges of H, and two vertices of F are adjacent exactly when the corresponding hyperedges intersect.

This route seeks the one-third upper bound by proving that P_ℓ-freeness forces

ℓ·rank(N) ≥ 3m.      (1)

Since rank(N)≤n, equation (1) would immediately give

m≤(ℓ/3)n.      (2)

The algebraic problem is therefore exact: show that a P_ℓ-free linear triple system cannot have too many incidence columns relative to their real rank.

## 1. Exact translation to an induced-path problem

Linearity makes the intersection graph unusually faithful. A sequence of distinct hyperedges

e_1,e_2,…,e_k

is a linear hypergraph path if and only if the corresponding vertices form an induced path in F.

Indeed, consecutive hyperedges in a linear path meet, whereas nonconsecutive ones are disjoint, so the intersection graph induced by them is exactly a graph path. Conversely, an induced graph path forces consecutive intersections and forbids all nonconsecutive intersections, which is precisely the linear-path condition.

Hence

H is P_ℓ-free  ⇔  F is induced-P_ℓ-free.      (3)

But not every induced-P_ℓ-free graph is relevant. The graph F carries the exact incidence realization of a linear triple system.

For each ground vertex x∈V(H), let C_x be the clique of all hyperedges containing x. Then:

1. every vertex of F lies in exactly three cliques C_x, because every hyperedge has three vertices;
2. every edge of F lies in exactly one clique C_x, because two hyperedges of a linear system meet in at most one vertex.

Conversely, any graph equipped with an indexed clique family satisfying these two conditions is the intersection graph of a linear 3-uniform hypergraph.

Thus the route is not a generic theorem about induced-path-free graphs. It is a rank theorem inside this exact three-clique realizability class.

## 2. The spectral identity

Because H is 3-uniform and linear,

N^T N = 3I_m + A(F),      (4)

where A(F) is the adjacency matrix of the intersection graph.

Therefore

rank(N)=rank(3I_m+A(F))
       =m−mult_F(−3),      (5)

where mult_F(−3) is the multiplicity of eigenvalue −3 of A(F).

The desired inequality (1) is equivalently

mult_F(−3) ≤ m(1−3/ℓ).      (6)

So the obstruction to one-third is a large −3 eigenspace, or equivalently a large space of linear dependencies among incidence columns.

The three-clique realization is essential here. Generic positive-semidefinite arguments applied only to 3I+A(F) discard exactly the structure that distinguishes realizable intersection graphs from arbitrary graphs.

## 3. The low-degree regime is already closed

There is a sharp rank theorem whenever the hypergraph maximum degree is below the forbidden path length.

If Δ(H)≤ℓ−2, then

ℓ·rank(N) ≥ 3m.      (7)

Thus any counterexample to (1) must satisfy

Δ(H)≥ℓ−1.      (8)

This cleanly removes the sparse regime. The remaining problem is intrinsically high-degree.

A useful way to see the low-degree theorem is through a more general weighted inequality. Give each hyperedge e a weight 0≤w_e≤1, let

W=Σ_e w_e,

and suppose every ground vertex has weighted degree at most D:

Σ_{e∋v} w_e ≤ D.

Then

rank(N) ≥ 3W/(D+2).      (9)

Taking all w_e=1 and D=Δ gives the low-degree estimate.

Equation (9) also suggests a possible high-degree strategy: rather than control the whole edge set, extract a large weighted fraction whose vertex loads are small enough.

## 4. Fractional-rank branch

Suppose one can choose weights with

W ≥ ρm−O(n)
and
D ≤ cℓ+O(1).

Then (9) gives

rank(N) ≥ (3ρ/(cℓ+O(1)))m.

To reach the exact one-third target, one would need parameters equivalent to 3W/(D+2)≥3m/ℓ. For a strict leading improvement over weaker existing coefficients, any fixed favorable ratio ρ/c already has value.

This branch reduces the theorem to a packing problem: find a large subdistribution of hyperedges whose weighted incidence at every ground vertex is low. The exact clique realization should constrain how high-degree concentration can coexist with induced-P_ℓ-freeness.

No theorem presently produces a sufficiently large weighted subfamily in the high-degree regime.

## 5. Nullity and cycle complexity

A second route to rank is to control the nullity directly.

Let s be the number of special hyperedges. If for fixed C,D one proves

nullity(N) ≤ C s + Dn,      (10)

then the snake inequality and rank(N)=m−nullity(N) combine to give

m ≤ [C(2ℓ−3)+D+1]/(2C+1) · n.      (11)

Thus any absolute bound of the form (10) yields a strict leading improvement.

The terminal-pair graph from the rotation route gives a more structural estimate. Let T be the terminal-pair graph of nonspecial edges, β(T) its cycle rank, and h the number of distinct entrance vertices used by nonspecial edges. Then

nullity(N_ns) ≤ β(T)+h,      (12)

and for the full incidence matrix,

nullity(N) ≤ β(T)+h+s.      (13)

So a theorem controlling β(T)+h in terms of special-edge mass and O(n) would immediately become a rank theorem here.

This explains the precise interface with the rotation route: terminal cycles and entrance reuse are not merely combinatorial nuisances; they are upper bounds for the dimension of the incidence dependency space.

## 6. Anatomy of a possible counterexample

Several certified structural theorems sharply limit what a counterexample to (1) could look like.

First, bounded matching number is insufficient as a rank surrogate; that line cannot reach the one-third scale.

Second, any P_ℓ-free construction whose density exceeds ℓ/3 must be genuinely large and high-degree. It must have average degree above ℓ, maximum degree at least ℓ+1, large matching and transversal numbers, and a dense induced minimum-degree core. In particular, a counterexample to the rank conjecture cannot hide in a small sparse exceptional configuration.

Third, if the intersection graph F is chordal, then

m≤3n/2.

More quantitatively, excess above 3n/2 forces linearly many edge-disjoint linear cycles in H. Hence a dense counterexample necessarily has abundant cycle structure. That cycle abundance is exactly what the nullity/cycle branch would like to exploit.

Together these facts place the unresolved problem in a narrow regime: high degree, large matching complexity, many cycles, and an exact three-clique incidence realization, yet still no long induced path.

## 7. Known obstructions

The simplest nullity conjectures are false.

There are linear 3-graphs with no special edges whose incidence matrix nevertheless has positive nullity; the basic obstruction is the same K_{3,3}-type terminal geometry seen in the rotation route. Hence

nullity(N)≤s

is false, and nonspecial incidence columns need not be independent.

Likewise, a dependence circuit need not contain a special edge. Therefore the rank deficit cannot be charged locally to specialness alone.

Generic graph-theoretic spectral bounds are also too weak because they ignore the indexed three-clique realization. Conversely, the low-degree regime Δ≤ℓ−2 is already solved and should not be reopened.

The remaining theorem must use realizability in a genuinely high-degree way.

## 8. First unsupported implication

The proof stops at the following high-degree statement.

**High-degree realizable rank target.** Let F be an induced-P_ℓ-free graph equipped with an indexed clique family in which every graph vertex lies in exactly three cliques and every graph edge lies in exactly one. Let N be the corresponding incidence matrix. Prove

rank(N) ≥ 3m/ℓ.      (14)

Equivalently, prove the same statement for every P_ℓ-free linear 3-uniform hypergraph with Δ≥ℓ−1.

There are two concrete weaker targets that would also advance the theorem:

1. extract weights of total mass W large enough and weighted degree D small enough for (9) to beat the current coefficient;
2. prove a bound on nullity(N), or on β(T)+h, strong enough to feed (11).

The exact graph translation, spectral identity, low-degree theorem, weighted rank bound, and nullity bridges are all certified. What is unsupported is the high-degree realizability theorem itself.

## Research handoff

Work only in the high-degree regime and keep the indexed three-clique realization explicit. The most promising formulations are either a realizability-aware −3 multiplicity theorem, a fractional low-load extraction, or a cycle/entrance nullity bound imported from the rotation route.

Do not retry generic PSD arguments on arbitrary induced-path-free graphs, bounded-matching certificates, nullity≤special-edges, nonspecial-column independence, or the already-solved low-degree case.

The route's virtue is its clean stopping point: once (14) is proved, the one-third upper bound follows immediately from rank(N)≤n.