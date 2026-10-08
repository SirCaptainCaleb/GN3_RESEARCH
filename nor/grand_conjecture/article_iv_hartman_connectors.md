# Article IV — Hartman connectors and least-unreachable repair topology

# Ternary colorings and monochromatic connectors

## The ordering problem

Let V be a finite set with at least three elements, and let α be a binary coloring of ordered triples of distinct elements of V satisfying

    α(c,b,a)=1−α(a,b,c).

For a linear order π=(v₁,…,vₙ), let w_α(π) be the word whose ith letter is α(v_i,v_(i+1),v_(i+2)). An order is *good* if this word has at most one color change. The ternary coordinate form of NOR asks whether every such reversal-odd α has a good order. Each order determines a geodesic in the Boolean cube 2^V from ∅ to V by adding the coordinates in that order. This is a translation-invariant, pole-to-pole formulation; a coloring that depends on the initial cube vertex requires separate treatment.

A reversal-odd coloring need not come from a tournament. We therefore identify the extra conditions before using tournament language.

## The tournament subclass

A tournament T directs each pair of distinct vertices in exactly one direction. Write ε(a,b)=0 when a→b and ε(a,b)=1 otherwise, and set

    α_T(a,b,c)=ε(a,b)+ε(b,c)+ε(a,c) (mod 2).

Changing two places of a triple changes α_T by one, so α_T is alternating under all odd permutations, not merely reversal-odd. It also satisfies the four-vertex identity

    α_T(a,b,c)+α_T(a,b,d)+α_T(a,c,d)+α_T(b,c,d)=0 (mod 2).  (1)

Every orientation bit occurs twice in this sum. Conversely, any alternating ternary coloring satisfying (1) is induced by a tournament. To see this, choose t∈V, direct t→a for every a≠t, and define ε(a,b)=α(t,a,b) for a,b≠t. Alternation makes these orientation bits antisymmetric. Equation (1) then identifies α(a,b,c) with ε(a,b)+ε(a,c)+ε(b,c) whenever t is absent; triples containing t agree by construction.

The stronger hypotheses of alternation and (1) are indispensable to that representation. Neither follows from reversal-oddness alone. Hence the arguments below concern a tournament-representable subclass unless a separate reduction to that subclass is proved.

## A conditional minimum-shore configuration

Suppose the tournament T admits a switching normalization with distinct vertices x,z and nonempty sets A,B partitioning the remaining vertices, with all cross-block edges directed in the pattern

    B→z→A→x,  and B→A.

Switching across a set reverses each edge between that set and its complement. Let d(u)=α_T(x,z,u). Assume that d is zero on A and one on B in this normalized representation.

The original minimum-shore analysis additionally supposes that x,z lack a certain *protected shortcut* and minimizes |A| among admissible such obstructions. Its claims concerning protected adjacency and the existence of this normalization depend on the precise carrier, contraction, and admissibility hypotheses. Those hypotheses are not established merely by the tournament representation. In particular, we do not infer that every counterexample to unrestricted ternary NOR possesses this split.

The relevant structural conclusion of the minimum-shore work is that T[A] contains a directed triangle u→v→w→u. Once the asserted stronger condition that every vertex of T[A] has an in-neighbor and an out-neighbor is available, this follows: an acyclic tournament has a source and sink. Deriving that stronger condition from minimum-shore minimality remains part of the assumed reduction, rather than an independent theorem of this Article.

## A concrete connector seed

Assume a directed triangle u→v→w→u in A and the special-coordinate color relations

    α_T(u,x,z)=α_T(x,z,u)=0,
    α_T(x,z,a)=0  for a∈A,
    α_T(z,a,b)=0  whenever a→b in A.

The order (u,x,z,v,w) then has three consecutive triples of color zero. Its exposed ordered pairs u→x and v→w are forward in T. Call an order a *compatible zero connector* if all its consecutive triples have color zero and its first and last directed pairs are forward. The displayed order is thus a compatible connector on five vertices, and reversal gives the complementary monochromatic word.

This seed does not itself extend to all of A. Separate legal insertions of two different shore vertices might require incompatible internal orders or endpoint pairs. The desired object is one compatible connector on A∪{x,z}, with the entirety of A present simultaneously.

## Sufficient spanning constructions

The established insertion calculation is a conditional closure principle: if a compatible zero connector spans A∪{x,z}, the complementary shore admits the required good order, and the two crossing-junction identities hold, insertion of the connector or its reversal yields a good spanning order. Its boundary calculation depends on two junction colors rather than the size of the inserted block. The requisite boundary word and junction conditions must be checked; reversal-oddness alone does not guarantee them.

A *fully ported zero path* in A is a linear order with zero on every consecutive triple and forward exposed directed pairs, whenever those pairs exist. If two disjoint such paths P,Q partition A, then (P,x,z,Q) is a spanning compatible connector provided the special-coordinate junction identities hold. Conversely, a connector of precisely this form splits into these paths. A general connector may have x and z separated; restricting to adjacent-special connectors without justification would lose possible solutions.

An especially useful sufficient condition is a fully ported zero Hamiltonian path P on A\{a} for some a∈A. Under the same junction identities, (P,x,z,a) is a spanning compatible connector: its internal triples vanish by the path condition, and the remaining crossing triples vanish by the endpoint port and special-coordinate relations. Therefore a genuine unresolved shore cannot possess such a one-path deletion certificate when the insertion theorem's outer conditions apply.

There is also a coherent-deletion construction. Let U=A∪{x,z}. For each d in a set D⊆A, suppose C_d is a compatible zero order on U\{d}. Call the orders *coherent* if they agree on relative order for every pair present in both. If |D|≥4, their comparisons determine a total order on U, because every triple survives in at least one deletion domain and hence satisfies transitivity. Every consecutive triple in that order is also consecutive in C_d for some d outside it, so its color vanishes. Choosing a deletion label outside the first or last pair likewise verifies the exposed ports. Thus four coherent deletion connectors supply a spanning compatible connector.

For fewer deletion witnesses, gluing requires extra care. Two omitted vertices inserted in adjacent distinct gaps may create one previously unchecked ternary triple; a cyclic triple of omitted labels may obstruct direct three-deletion reconstruction. These are obstructions to the specified gluing procedures, not impossibility results for unrestricted connector orders.

## Reversible repairs and the remaining problem

A repair state consists of an actual zero-colored order containing x,z and some shore vertices. A repair move is legal only if *all* affected consecutive triples, including those crossing the modified interval, retain color zero. The support of a state is its set of shore vertices. Intermediate orders may lack compatible exposed pairs, provided the terminal state has them.

A Hartman-style least-unreachable argument may be considered on the graph of legal reversible repairs. But the presence in one connected component of separate states containing each a∈A does not imply a state containing every a simultaneously. To obtain such a state one needs a proved support-combination theorem or an actual terminating exchange, followed by a boundary argument that extracts compatible final ports. A formal topological zero without these realization and extraction properties cannot establish the conjecture.

We have therefore proved direct local connector statements and identified several sufficient certificates for spanning closure. What is not proved is that the minimum-shore hypotheses force one certificate: a single full compatible connector, a suitable fully ported deletion path, an adequate coherent family, or a terminating collective absorption. Nor has the unrestricted reversal-odd ternary problem been reduced to the tournament subclass. Both qualifications remain necessary. A solution of the original conjecture must justify its scope and establish a spanning good order without depending on an unproved reduction or connector-existence assertion.
