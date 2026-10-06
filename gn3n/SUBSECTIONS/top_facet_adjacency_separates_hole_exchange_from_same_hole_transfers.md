# Top-facet adjacency separates hole exchange from same-hole transfers

## Metadata

- ID: top_facet_adjacency_separates_hole_exchange_from_same_hole_transfers
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 257
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

## Top-facet adjacency separates hole exchange from same-hole transfer

Assume H has no spanning two-cover, on n vertices. Let E(H) be the signed downward-closure complex of disjoint nonempty Hamiltonian support pairs, as in subsection 243. Let E_top be the union of its simplices of total support n-1 and all their faces; in a minimum counterexample these simplices are exactly the oriented deletion-cover support pairs.

We do NOT assume that a face of E_top has Hamiltonian components. Hamiltonicity is not hereditary. This distinction matters at codimension one.

### Correct coface indicators for every signed face

Let F=A^+ union B^- have total support n-2, with missing labels x,y. Its four possible top cofaces have indicators
f_x^A=[H[A+x] Hamiltonian AND H[B] Hamiltonian],
f_x^B=[H[A] Hamiltonian AND H[B+x] Hamiltonian],
f_y^A=[H[A+y] Hamiltonian AND H[B] Hamiltonian],
f_y^B=[H[A] Hamiltonian AND H[B+y] Hamiltonian].

Under no spanning two-cover,
f_x^A f_y^B = f_y^A f_x^B = 0.
Either crossed pair would itself supply two complementary Hamiltonian supports on V(H).

Consequently every codimension-one face has at most two top cofaces. Its degree is zero, one, or two; odd degree is exactly unique degree. This strengthens the incidence statement in subsection 255 from Hamiltonian two-hole states to ALL signed codimension-one faces, including faces whose restrictions have lost Hamiltonicity.

The mod-two sum of all top simplices therefore has boundary consisting exactly of ALL degree-one signed faces. Subsection 255's formulation using only Hamiltonian two-hole states does not by itself justify this chain identity for the downward-closure complex: non-Hamiltonian restrictions also have to be included. Its local indicator argument remains valid on the stated Hamiltonian states.

### The two possible adjacencies

The four allowed degree-two patterns divide into two types.

I. Hole exchange: f_x^A=f_y^A=1, or f_x^B=f_y^B=1.
The deletion covers omit different labels and keep one entire Hamiltonian support fixed. For example (A+x)|B and (A+y)|B omit y and x respectively. These are support-agreement edges, even if H[A] is non-Hamiltonian.

II. Same-hole transfer: f_x^A=f_x^B=1, or f_y^A=f_y^B=1.
Both deletion covers omit the SAME label. For example (A+x)|B and A|(B+x) both omit y. The vertex x moves between the two supports. These are NOT edges of the support-agreement graph of covers at distinct holes.

No other two-coface pattern is possible without an actual spanning two-cover.

Thus the top-simplex adjacency graph contains a previously explicit but structurally separate class of moves: same-hole support transfers. Connectivity in a support complex cannot be identified with agreement connectivity while these moves are being suppressed.

### Minimum-imbalance selection sharply limits the additional moves

Restrict the top simplices to covers minimizing quadratic potential among deletion covers at their own hole. Put a=|A| and b=|B| for a same-hole transfer above. Its endpoint potentials are
(a+1)^2+b^2 and a^2+(b+1)^2.
Their difference is 2(a-b).

If both endpoint covers are minima for that hole, their potentials must be equal. Hence a=b, n-2=2a, and n is even. The two covers then have side sizes a+1,a in opposite roles.

Therefore:
- at odd n, no same-hole transfer joins two minimum-imbalance deletion covers;
- at even n, such adjacency between minima is necessarily neutral and has near-balanced profile (a+1,a);
- a hole-exchange agreement edge always preserves the unordered support-size profile.

It follows that every connected component of the minimum-cover top-adjacency graph has a fixed unordered size profile. In odd order its unoriented graph is exactly the full support-agreement graph on all minimum deletion-cover support partitions. A path through smaller supports in the full poset does not establish a path in this graph.

This is a scale-independent structural obstruction to the proposed implication from low homotopy connectivity to agreement connectivity. It is not a numerical order cutoff.

## Reconstruction without selecting one cover per hole

Here is a genuine extension of subsection 210.

For each hole x, let S_x be any nonempty family of deletion-cover support partitions. Define a graph D whose vertices are states s=(x,F), F in S_x. Edges join states at different holes whose partitions agree after restricting to the common domain.

Theorem. Suppose n>=4. If, for every distinct u,v in V(H), the induced graph on states with hole outside {u,v} is connected, then H has a spanning two-cover.

Proof. For vertices u,v of H, the predicate that u,v belong to the same support is constant along every edge between states whose hole is outside {u,v}. Connectivity makes this predicate independent of all such states; call the resulting relation u~v. For any three distinct labels u,v,w, choose a state whose hole lies outside this triple. Such a state exists because every hole is represented and n>=4. All three relations are computed in one two-part partition, proving transitivity. The same argument shows there are at most two equivalence classes.

For every state at hole x, its support partition is the restriction of this global partition: each surviving pair has precisely the reconstructed same-class relation. If the two global classes A,B are nonempty, choose a state with hole in B to witness H[A] Hamiltonian, and one with hole in A to witness H[B] Hamiltonian. If there is only one class, every deletion cover has a single nonempty support, so H-x is Hamiltonian and together with {x} gives a two-cover. QED.

Thus the reconstruction theorem can use ALL deletion covers at a hole. No consistent choice of one representative per hole is needed. In a minimum counterexample, any such all-hole state family must fail the two-hole-removal connectivity test.

The stronger condition is useful only if the required state-graph connectivity can be proved. Universal existence of deletion covers or low-dimensional support-poset fillings does not prove it.

## Relation to the earlier support graph and antipodal loops

In a counterexample a deletion-cover component cannot be a singleton or a pair: adding the hole gives a Hamiltonian support of size at most three and hence a spanning two-cover with the other component.

The Article I argument that agreement preserves one entire support therefore applies to arbitrary states, not only to a selected transversal of holes. Define J on Hamiltonian supports occurring in the family, with an edge A-B for each deletion state A|B of V-x. A fixed support and fixed hole determine its partner uniquely. States at the same hole cannot share a support unless they coincide. Agreement at different holes is equivalent to sharing a support, because placing the restored labels in different sides would give complementary Hamiltonian supports spanning H.

Consequently D=L(J). This is the all-state form of the existing Article I line-graph identification; it is not claimed as a new selected-family theorem.

The signed identification of sides along agreement edges is a two-sheeted cover of D. In the signed complex, an agreement edge is represented by a path between aligned top-facet barycenters through their common signed face. Projecting modulo side swap gives a map from D to the quotient of E(H), with that two-sheeted cover as its pullback. A negative agreement cycle lifts to a path ending at the antipode of its starting point.

Thus simple connectivity of the covering support space does not force every agreement cycle to be positive. Even a simply connected free antipodal space has a quotient whose fundamental group contains this side-swap class. Filling a loop upstairs and orienting a loop downstairs are different obligations.

## Strategic conclusion

The bridge is now explicit. To invoke reconstruction, one needs connectivity of actual deletion-cover states after removing any two hole fibers, not connectivity obtained by dropping most support vertices. At top rank the only additional adjacency is same-hole vertex transfer, and minimum imbalance either excludes it (odd order) or restricts it to neutral near-balanced transfers (even order).

The boundary-tournament conditions must supply a lifting from partial-support fillings to these top-rank states, or supply a proved sequence of support transfers which controls the same-class predicates. No such lifting, spanning two-cover, or terminating improvement has been proved here. The grand theorem remains open.
