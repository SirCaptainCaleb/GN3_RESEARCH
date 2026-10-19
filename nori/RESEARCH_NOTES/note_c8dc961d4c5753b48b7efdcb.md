# Prescribed-geodesic orbit-disjoint packing: Q4 failure and Q5–Q6 SAT evidence

- Stable ID: note_c8dc961d4c5753b48b7efdcb
- Author: unspecified; session provenance retained
- Primary home: subsection:edge_conditioned_turn_census_and_critical_flip_forcing
- Labels: NORI1, critical-flip, orbit-disjoint, witness-packing, Q4, Q5, Q6, SAT
- Lifecycle: active
- Epistemic status: tested
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11512_1
- Updated session: session_nori_r11512_1
- Disposition: none
- Successor: none

## Related references

- subsection:cartesian_factorization_of_paired_roots_and_interaction_prime_reduction

## Research note

For a legal antipodally odd edge coloring c of Q_n and a monochromatic full antipodal geodesic P, let supp(P) be its set of n antipodal edge orbits. Define property W(n): for every (c,P), some monochromatic full geodesic Q satisfies supp(P) intersect supp(Q)=empty. This property is stronger than every-orbit avoidance and implies preservation of monochromatic geodesic existence under arbitrary single-orbit recolorings: among P,Q at least one avoids any prescribed orbit.

FINITE COMPUTATION. W(4) is false. Number antipodal edge orbits for Q4 is 16; enumerate them by direction i ascending and, within direction, by the smaller exterior vertex integer from x with bit i erased, comparing with its antipodal mate. The legal coloring whose 16 orbit bits form the integer 0x1610 has a red P rooted at 0000 in order (0,1,2,3), but no monochromatic full geodesic Q is orbit-disjoint from P. The witness-independent SAT clauses are satisfied by this assignment; the source verifier checks them. This does NOT rule out two disjoint witnesses elsewhere: only the prescribed P is constrained.

For n=5 and n=6, SAT reports W(n) true, by automorphism normalization of P to red, root 0, direction order 0,1,...,n-1. Fix its n orbit bits to make P red. For every rooted full geodesic Q with supp(Q) disjoint from supp(P), add both clauses excluding all-red and all-blue color profiles. These are clauses in the antipodal orbit bits; the clause count after deduplication is 1010 for Q5 and 16152 for Q6. The corresponding bit counts are 40 and 96. With these constraints and the normalization, system libz3.so.4 returns UNSAT for n=5 and n=6 (and SAT for n=4). Therefore the finite SAT searches find no counterexample to W(5) or W(6). No independently checked SAT proof log is available; these are verified generator-and-solver computations, not proof certificates independent of Z3.

REPRODUCTION. Python generator using the Z3 C API is stored at https://github.com/SirCaptainCaleb/GN3_RESEARCH/blob/859f413f9ca76cef0313ea525e6ce78d6406ea57/nori/certificates/nori_prescribed_witness_packing.py. The generator fixes the red witness, enumerates every forbidden-orbit-avoiding rooted permutation, computes each edge orbit plus its antipodal phase, and writes the clauses to Z3. The Q4 satisfying example is checked by direct evaluation. All paths and variables are normalized using cube automorphisms, not extra assumptions about c.

RESEARCH INTERPRETATION. The possible dimension-uniform conjecture W(n) for n>=5 would immediately close NORI1 via the first-bad-orbit-flip argument, and is stronger than the archived n<=6 absence of a critical single orbit. A red-geodesic P is a geometric boundary condition that may allow a direct path-packing/topological proof. The new positive information is the finite n=5 and n=6 prescribed-witness tests; passing them does not establish W(n) for arbitrary n, and the current archive supplies no induction preserving this property. This is an active forcing candidate, not an unrestricted proof.
