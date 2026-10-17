# Six-cube absence of critical profile orbits and universal direction-profile attainment

- Stable ID: note_nori_q6_profile_critical_sat_extension_r11435
- Author: unspecified; session provenance retained
- Primary home: subsection:full_geodesic_color_profiles_span_the_entire_binary_space
- Labels: NORI1, Q6, computational, critical-orbit, full-geodesic-profiles, SAT, red-critical, direction-indexed, dimension-six
- Lifecycle: active
- Epistemic status: tested
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11435_4
- Updated session: session_nori_r11435_4
- Disposition: none
- Successor: none

## Related references

- note:note_6f6b320f698318cecb8efd89
- note:note_nori_q4_ten_path_critical_surgery_r11435

## Research note

# SAT exclusion of critical profile orbits in Q6

A legal antipodally odd coloring of Q6 assigns one Boolean color bit to each of the 96 antipodal edge-pair orbits. A full-geodesic *direction-indexed* profile w records the color of the edge used in each direction i, independently of traversal order. An orbit O is w-critical when w is attained and every path attaining w meets O.

**Finite SAT result.** No legal Q6 coloring has an attainable direction-indexed profile with a critical orbit. The reproducible generator and Z3 wrapper are `/mnt/data/nori_research/orbit_critical_z3.py`, with mathematical and computational audit in `/mnt/data/nori_research/q6_profile_critical_sat_audit.md`.

**Reduction.** Complement the direction-i rule whenever w_i=1, making all paths with profile w all-red and preserving antipodal oddness. Translate and permute directions to place a prescribed red witness at root 0 with order (0,1,2,3,4,5). Select its orbit in step k. Six distinct orbit bits are fixed red by this witness. Each of the 43200 rooted full geodesics avoiding O gives a Boolean clause requiring at least one blue edge, excluding another avoiding red path. The six positions k=0,1,2,3,4,5 give respectively 18790,18723,18712,18712,18723,18790 distinct effective clauses, each over the 90 free bits. All six instances return UNSAT with the installed libz3.so.4 engine. The Q3 endpoint-critical control returns SAT, its interior control returns UNSAT, and Q4/Q5 reproduce the archived exclusions.

Orbit encoding: for an edge in direction i starting at x, set a=x with bit i removed, b=(63 XOR x) with bit i removed, orbit key (i,min(a,b)), and sign 1 iff a>b. Its color is z_orbit XOR sign. Each normalized red witness edge sets z_orbit=sign. Every avoided red path is excluded by OR over its edge-blue literals.

**Full direction-profile attainment in dimension six.** With no critical orbit for any attained w, every attained w survives every single-orbit recoloring. Legal colorings are connected by such flips. The cyclic-reader coloring c_i(x)=x_(i+1 mod 6) realizes every w in {0,1}^6 under the fixed order (0,1,2,3,4,5) by selecting its starting vertex. Consequently EVERY legal Q6 coloring realizes all 64 direction-indexed profiles.

**Epistemic scope.** This extends the earlier Q4/Q5 SAT exclusions to Q6. It is a finite computer-assisted result; no independently checked unsatisfiability proof log is supplied. The claim concerns direction-indexed profiles, not arbitrary prescribed temporal color words. It gives no dimension-uniform forcing mechanism, and direct Q7 runs remain computationally unresolved.

## Dimension-uniform fractional feasibility: why first-order blocking inequalities cannot close the critical-orbit contradiction

**Theorem.** Fix n>=2, a rooted full antipodal geodesic P in Q_n, and any orbit O of one of its edges. Prescribe all P edges red, and relax every remaining antipodal edge-orbit Boolean variable z_J to the interval [0,1]. Each edge e retains the affine blue indicator b(e)=z_J or 1-z_J determined by its orientation within J. For every full geodesic Q avoiding O impose the linear blocker inequality sum_{e in Q} b(e)>=1. This entire linear system has a feasible point, in every dimension: set each of the n orbit variables met by P to make P red, and all other orbit variables to 1/2.

**Proof.** At this point, each edge of Q is either one of P's red edges (blue indicator 0), an antipodal mate of a P edge (blue indicator 1), or an edge belonging to an unprescribed orbit (blue indicator 1/2). If Q contains a forced-blue mate, the blocker inequality holds. Otherwise suppose Q contains at most one unprescribed edge. Since Q traverses n distinct direction labels, it then contains at least n-1 of P's red edges. Because Q avoids O, these shared edges must be precisely the n-1 edges of P other than the edge e in O; the last direction of Q is dir(e).

Delete e from P. If e is internal, the remaining edges comprise two vertex-disjoint subpaths in opposite dir(e)-facets. Their only pair of vertices joined by a dir(e)-edge is the two original endpoints of e: before e the other flipped directions form subsets of the prefix set A, while after e they form supersets of A with additional suffix directions. Equality of their other direction bits forces both sets to equal A. Thus the only completion is e itself, contrary to Q avoiding O.

If e is an endpoint edge, the other n-1 edges form one chain. The only dir(e)-edges that can extend it to a full direction-simple path are e at the original end and its antipodal mate at the other end. The former belongs to O and the latter is a forced-blue edge. Either contradicts the case under consideration. Therefore Q has at least two unprescribed edges, contributing 1/2+1/2=1 to its fractional blue count. This proves simultaneous feasibility of every blocker inequality. QED.

**Interpretation.** The finite Boolean UNSAT result is invisible to the first-order linear relaxation in every dimension. A Farkas certificate formed only from these pathwise expected-blue inequalities and the orbit bounds cannot establish the red-critical contradiction. A successful proof must exploit integrality or constraints involving correlated orbit assignments. This is an unrestricted structural diagnosis of the critical-orbit system, not a reduction of the conjecture.
