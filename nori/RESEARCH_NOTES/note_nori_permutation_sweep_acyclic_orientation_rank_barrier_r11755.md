# Acyclic-orientation ceiling for nonlinear half-sweep permutation ranks

- Stable ID: note_nori_permutation_sweep_acyclic_orientation_rank_barrier_r11755
- Author: session_nori_r11755_4
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: NORI1, paired-flat, nonlinear-gates, rank-barrier, acyclic-orientations, critical-square, dimension-uniform, dependency-graph, half-sweep
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11755_4
- Updated session: session_nori_r11755_4
- Disposition: none
- Successor: none

## Related references

- subsection:obstruction_compatibility_and_a_programme_for_nori1_closure

## Research note

# Acyclic-orientation ceiling for half-sweep permutation ranks

Session session_nori_r11755_4. This theorem applies to the unrestricted nonlinear paired-flat model, and limits the permutation-rank certificate AR2 in the current gauge/critical-switch manuscript.

Let a legal paired-flat coloring on Q_(2m) have pair gates f_i(p,q), independent of their own bits p_i,q_i, and odd under simultaneous complement of q. For i≠j put ij in the undirected interaction graph H when f_i depends on p_j or q_j, or f_j depends on p_i or q_i. Define T_i(p,q)=(p+e_i,q+(1+f_i(p,q))e_i), the involution following the red edge in pair i. For a starting pair-parity p and a permutation pi of [m], let F_pi^p be the bijection of the q-fiber induced by T_(pi_m)...T_(pi_1), and P_pi its permutation matrix.

**Theorem (acyclic-orientation factorization).** The map pi -> F_pi^p factors through the acyclic orientations of H. Consequently, if a(H) denotes the number of acyclic orientations of H, then for every family C of half-sweep pair orders and every pi0 in C,
  |{F_pi^p:pi in C}| <= a(H),
  dim_R span{P_pi-P_pi0:pi in C} <= a(H)-1.             (AO1)

**Proof.** If ij is absent from H, the gate f_i ignores both bits of j and f_j ignores both bits of i. Therefore T_i and T_j commute as functions of (p,q), including parity changes: each reads the same inputs and changes its own pair only. Swapping two consecutive nonadjacent labels of H in an update word preserves its full transformation, hence its endpoint map on every starting parity fiber. Associate an acyclic orientation of H to an order by directing each H-edge from its earlier to its later endpoint. Two linear orders yield the same orientation if and only if they are topological orderings of the same directed acyclic graph. Any two topological orderings are connected by adjacent swaps of incomparable vertices; such vertices cannot be adjacent in H. Therefore both orders induce the same endpoint map. There are a(H) possible orientation classes, proving the cardinality bound, and the dimension bound follows by taking differences from one representative. QED.

**Corollary (rank forcing requires sufficiently many acyclic orientations).** Put N=2^m and D=(N-1)(N-2)/2. The rank-forcing criterion AR2 can certify a red antipodal full geodesic from a given family of half-sweep maps only if
  a(H)>= D+2.                                           (AO2)
As a coarse sufficient condition for *failure of the rank certificate*, if m>=3 and |E(H)|<=2m-2, then a(H)<=2^|E(H)|<=2^(2m-2)<=D; consequently every family of half-sweep maps, including a critical-square-safe family, has difference rank <D+1. This conclusion concerns the **certificate**, not the existence of monochromatic geodesics.

**Strongly connected example.** For m>=3 set f_i(p,q)=q_(i-1 mod m), with all p-dependence absent. Each gate is legal, its directed q-dependency graph is the strong directed m-cycle, and H=C_m for m>=4 (H=K3 when m=3). An orientation of a cycle is acyclic unless every edge is oriented consistently around it, so a(C_m)=2^m-2. Hence
  dim span{P_pi-P_pi0} <=2^m-3
in every p-fiber, as opposed to the forcing threshold (2^m-1)(2^m-2)/2. Thus arbitrary large strongly connected components alone cannot make the permutation-rank certificate decisive. This instance belongs to established successful classes, so the calculation is a method obstruction only.

**Dimension-eight-pair near-complete graph calculation.** At m=8, N=256, D=32385. For H=K8, a(H)=8!=40320. If one edge is absent, a(H)=8!-7!=35280. If two edges are absent and disjoint, chromatic-polynomial deletion gives a(H)=8!-2*7!+6!=30960; if the two missing edges meet, a(H)=8!-2*7!=30240. Because deleting further graph edges cannot increase a(H), every H missing at least two edges has a(H)<=30960 and hence difference rank at most 30959, strictly below D. Therefore the AR2 criterion is incapable of forcing success in dimension Q16 using any half-sweep family whenever the interaction graph has two absent edges. One absent edge leaves sufficient orientation classes for a rank certificate to be logically possible, with no claim that the rank threshold is attained.

**Proof of the orientation counts.** Stanley's identity gives a(H)=(-1)^m chi_H(-1), where chi_H is the chromatic polynomial. For K_m with two disjoint missing edges, a proper coloring either uses all distinct colors, identifies one of the two admissible nonadjacent pairs, or identifies both. Thus chi=(t)_m+2(t)_(m-1)+(t)_(m-2). When the two omitted edges share an endpoint, identifying both is forbidden, so chi=(t)_m+2(t)_(m-1). Evaluation at -1 gives the stated values. These formulas can alternatively be derived by classifying update-order permutations under adjacent commutations.

**Transfer obligation.** The upper bound explains why counting safe orders or establishing large strongly connected dependency blocks is insufficient for the rank program. A closure argument through AR2 must (i) establish a(H)>=D+2 in the same hypothetical critical coloring, (ii) produce a lower bound on the dimension of distinct endpoint maps, or (iii) force a geodesic by another mechanism in interaction graphs where the orientation ceiling makes AR2 inert. No unrestricted NORI1 or boundary-tournament conclusion follows from (AO1).

**Strengthening (fully nonlinear strong-feedback obstruction).** Let m=2k with k>=3 and H=C_k square K_2, the connected cubic prism graph. Assign to each pair label i the gate
  f_i(p,q)=q_a q_b+q_a q_c+q_b q_c,
where a,b,c are its three neighbors in H and multiplication is in F2. This is Boolean majority of the three neighboring q bits. It is independent of its own pair bits and is antipodally odd, since complementing three arguments interchanges majority 0 and majority 1. Every gate has algebraic degree two in q and depends essentially on all three neighbors. Hence its directed dependency graph has BOTH arcs for every H edge, is strongly connected, and has directed feedback vertex number equal to the minimum vertex-cover number tau(H). Indeed every edge is a directed two-cycle, requiring a feedback set to meet every undirected edge; conversely the complement of a vertex cover is independent and supports no directed cycle. As H is cubic with 3m/2 edges, tau(H)>=|E(H)|/3=m/2.

Nevertheless |E(H)|=3m/2<=2m-2, so the orientation ceiling of the preceding theorem implies rank deficiency for EVERY half-sweep family, including all square-safe families. Thus simultaneously imposing full q-nonlinearity at every gate, arbitrarily large strongly connected dependency components, and directed feedback vertex number Omega(m) does not establish the rank hypothesis required by AR2. This is an obstruction to that method only; no counterexample to NORI1 is asserted.

The independent standard-library verifier nori_cubic_rank_barrier_verify.py checks every gate's oddness and three essential reader bits, every directed feedback vertex-cover subset, and every orientation of H for k=3,4,5. The resulting tuples (m, feedback vertex number, acyclic orientations, AR2 forcing threshold) are (6,4,204,1953), (8,4,1862,32385), and (10,6,14700,522753). The formula above proves the conclusion for every k>=3 without relying on finite enumeration.
