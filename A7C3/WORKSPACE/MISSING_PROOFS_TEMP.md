# Missing proofs (temporary)

Current disposition of the original proof-gap worklist:

- R3 → P1120 (foundational axiom certificate; pending independent review)
- R893 → P1122 (definition/consequence proof; pending independent review)
- R685 → P1121 was constructed, but independent audit found a scoped failure. The exact 43 labelled edge-set configurations and distribution A:6, B:4, C:12, D:3, E:12, F:6 remain correct. The later assertion that a labelled configuration plus the two X-dimer orientations completely determines the ordered rail pair is false. A nonsingleton component containing at most one Q-block has an additional direction choice. The audited orientation count is 22 configurations with one admissible component orientation and 21 with two, giving 4*(22+2*21)=256 directed candidates rather than <=172. R685 and P1121 are therefore marked needs-more-work / invalid as written.

The remaining proofless entries below are explicitly conjectural in Supabase and therefore are not proof obligations.

## R888

Conjecture. Every finite Strong Level-(1) boundary tournament whose comparison orientation Gamma(H) is acyclic has pc(H)<=2. Equivalently, for every total ordering of E(K_n), the vertex set of K_n can be partitioned into at most two vertex-disjoint increasing paths. A potentially useful strengthening is endpoint-flexibility: for every prescribed vertex v, such a two-path partition can be chosen with v exposed as an endpoint of one path.

## R892

Every finite 3-uniform boundary tournament has a spanning cover by at most two directed tight paths.
