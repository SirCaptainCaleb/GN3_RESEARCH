# Route 7 — Transversal/Latin/blow-up/product lower constructions

## Statement

Comprehensive synthesis of the lower-bound route through transversal designs, properly colored lifts, fixed-template Latin blow-ups, shared-color constructions, and products.

## Body

# Route 7. Transversal, Latin, blow-up, and product constructions

## Goal

This route asks whether a good finite P_ℓ-free component can be amplified by replacing vertices or edges with large transversal-design gadgets, Latin squares, shared-color lifts, or graph products.

The basic hope is attractive: a fixed template may have unusually high edge density relative to its longest path, and a q-fold lift multiplies the edge count by roughly q² while multiplying the vertex count only by q. If the longest path grew only linearly with a sufficiently small constant, the normalized lower bound could improve.

The developed mathematics shows that most natural lifts fail for exactly the opposite reason: the same quasigroup or color structure that creates many edges also creates many compatible routes, and those routes concatenate into long linear paths.

This rehearsal therefore functions as a proof of a sequence of no-go theorems, followed by the narrow class of constructions that remain genuinely open.

## 1. Transversal designs as properly colored bipartite graphs

A transversal design TD(3,q) has three vertex classes A,B,C of size q and q² triples, with every pair from distinct classes lying in exactly one triple.

Equivalently, choose a proper q-edge-coloring of K_{q,q} on A∪B by colors C. The colored edge ab with color c represents the triple {a,b,c}.

A rainbow graph path in K_{q,q} lifts to a linear hypergraph path, because distinct graph edges give distinct triples, proper coloring prevents adjacent triples from sharing a second vertex, and the rainbow condition prevents nonconsecutive triples from meeting in a color vertex.

Thus the path problem in TD(3,q) is at least as strong as the rainbow-path problem in its properly colored bipartite representation.

## 2. Full transversal designs have a one-third ceiling

Every TD(3,q) contains a linear path of length

q−o(q).      (1)

Since TD(3,q) has 3q vertices and q² edges, taking the first forbidden length near q gives normalized edge density at most

1/3+o(1).      (2)

Therefore a full Latin square or full transversal design cannot yield an asymptotic lower coefficient larger than one third.

This closes the most direct amplification idea. The obstruction is not peculiar to a special Latin square: it holds for every full TD(3,q).

## 3. Arbitrary Latin blow-ups of a fixed template

Let T be a fixed linear 3-uniform template with v vertices and m edges. Replace each template vertex by a cluster of q vertices. For every template hyperedge, place an arbitrary TD(3,q) across the corresponding three clusters.

The resulting blow-up has

qv vertices
and
q²m hyperedges.      (3)

Suppose the template contains a linear cycle of length s. Follow that cycle through its s clusters. Each traversal around the cycle imposes a sequence of Latin constraints from one joint cluster to the next.

The key route-packing theorem states that, regardless of the chosen Latin fillings, one can find

q−o(q)

internally resource-disjoint lifted traversals of the base cycle and concatenate them. Therefore the blow-up contains a linear path of length

sq−o(q).      (4)

At the first forbidden length allowed by (4), its normalized edge density is at most

m/(vs)+o(1).      (5)

This is the decisive fixed-template theorem.

Consequently, an arbitrary independent Latin blow-up can beat the one-third barrier only if the base template has a cycle of maximum length s satisfying

s < 3m/v.      (6)

Equivalently, the template must have edge density unusually large relative to its circumference.

The original hope that a good small example could simply be “Latin-amplified” is therefore false unless it already carries this exceptional circumference-density ratio.

## 4. Why the cycle lifts are unavoidable

The proof mechanism behind (4) is worth recording because it describes what any surviving construction must defeat.

Fix a base linear cycle. A lifted lap chooses one vertex in each visited cluster, subject to the Latin relation on each base edge. For a prescribed starting point, the Latin operation determines or heavily constrains the succeeding choices. Different starts generate a large family of candidate laps.

One then forms an auxiliary matching problem whose resources are the cluster vertices and local transition choices. Since each individual route consumes only O(s) resources and the full TD supplies q choices in every cluster, a matching argument selects q−o(q) essentially disjoint laps. Their endpoints can be ordered so that consecutive laps share exactly the joint needed for concatenation.

Thus the long path is not an artifact of one algebraic filling. It is a consequence of the abundance and regularity of independent Latin routes.

A successful lift must therefore break this route-packing mechanism, not merely choose a more complicated Latin square.

## 5. Shared-color and one-factorization lifts

A second amplification idea begins with a properly edge-colored graph G. Create many copies of its vertex set while reusing one common color set, and convert colored graph edges into triples.

This also fails asymptotically. For repeated arbitrary proper-color lifts, P_ℓ-freeness forces the underlying graph density to satisfy a bound corresponding to an asymptotic hypergraph coefficient at most

1/4.      (7)

Thus repeated shared-color lifting is actually weaker than the one-third benchmark.

The natural one-factorization lift of K_N is even more explicit: for large N it contains a linear path of length N−2. Hence the exceptional small 11-vertex P_5 construction cannot be scaled by this one-factorization mechanism.

These results subsume earlier small-order and special-factorization obstructions. The shared-color route is closed in its regular repeated form.

## 6. Cartesian products

Suppose H and K contain linear paths of lengths a and b. Their Cartesian-style product contains a linear path of length

(a+1)(b+1)−1.      (8)

The proof concatenates a copy of the b-edge path in one factor across successive vertices of the a-edge path in the other, with the product coordinates keeping nonconsecutive edges disjoint.

Iterating a fixed seed therefore multiplies available path length approximately exponentially in the number of factors, while the normalized edge density grows only additively. Consequently repeated Cartesian powering has normalized coefficient tending to zero.

Thus products do not amplify a finite exceptional component into an asymptotically stronger lower bound.

## 7. The surviving low-circumference template problem

The fixed-template theorem leaves one precise loophole.

Suppose a finite linear 3-graph T has v vertices, m edges, and circumference s, where s is the maximum length of a linear cycle. If

s < 3m/v,      (9)

then the universal cycle-lift bound (5) does not by itself rule out a coefficient above one third.

Such a template would still need a filling in which no other lifted structure creates paths substantially longer than sq. The arbitrary-Latin theorem says that every base cycle already costs sq−o(q), but it does not prove that every template satisfies s≥3m/v.

Therefore one live construction problem is:

**Low-circumference template target.** Find a finite linear triple-system template with s<3m/v and a family of fillings whose longest paths remain controlled at the scale sq.

A theorem proving

s≥3m/v

for every relevant template would instead close the entire fixed-template arbitrary-Latin branch negatively.

## 8. Partial and nonregular transversal systems

The full TD theorem uses the completeness and regularity of the Latin structure. This suggests a second loophole: abandon full transversal designs.

A partial Latin system may sacrifice some q² local edges in order to destroy the route-matching abundance. Likewise, one may correlate the fillings on different base edges so that local route choices are not independent.

For such a construction to improve the lower coefficient, it must satisfy two competing requirements:

1. retain enough triples that the density loss is o(q²) at each large gadget;
2. destroy enough compatible routes that the longest lifted path grows with a constant strictly smaller than the density gain.

No current theorem constructs such a system, and no general no-go theorem rules it out. This is therefore the genuinely open portion of the transversal route.

## 9. Known dead ends

The following mechanisms are already fenced:

- full TD(3,q) or full Latin-square components;
- arbitrary independent Latin blow-ups of a fixed template unless the template has exceptional circumference-density ratio;
- repeated shared-color or one-factorization lifts;
- Cartesian powers of a fixed seed;
- extrapolation from small q path suppression without a mechanism stable as q grows.

Earlier provisional affine-Latin and special-factorization analyses are no longer frontier results; their asymptotic conclusions are subsumed by the stronger certified theorems above.

## 10. First unsupported implication

The route now stops at one of two genuinely new construction tasks.

**Template target.** Produce a finite template with circumference s<3m/v and prove that an appropriate filling has longest path only sq+o(q).

**Nonregular target.** Construct a partial, nonregular, or globally correlated transversal system of near-quadratic local density whose route structure avoids the full-TD and fixed-template matching arguments.

No present theorem supplies either object.

The obstruction is conceptually clear: regular Latin structure makes edges cheaply, but it also makes compatible routes cheaply. A successful construction must retain the former while destroying the latter.

## Research handoff

Search only outside the fenced regular mechanisms. The most concrete finite problem is the low-circumference inequality s<3m/v; the most conceptually distinct infinite problem is a nonregular or globally correlated Latin filling in which the route choices cannot be packed independently.

Do not revisit full transversal designs, arbitrary independent Latin blow-ups of ordinary templates, repeated shared-color lifts, one-factorizations, or Cartesian powering without a new mechanism that invalidates the corresponding certified long-path theorem.

Status note: the full-TD path theorem, fixed-template arbitrary-Latin cycle lift, shared-color ceiling, one-factorization fence, and Cartesian-product path theorem are certified. The low-circumference and nonregular construction targets remain open.