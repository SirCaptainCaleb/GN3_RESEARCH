# Infinite unimodular shift countermodels with odd skew Pfaffian

- Stable ID: note_nori_shift_odd_pfaffian_countermodels_20261016_r10917
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: NORI1, Pfaffian, counterexample, noncubical, Fourier
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10917_3
- Updated session: session_nori_r10917_3
- Disposition: none
- Successor: none

## Related references

- note:note_nori_arc_digraph_eulerian_high_chromatic_no_alt_cycles_20261016
- note:note_nori_cubelike_pfaffian_matching_duality_20261016_r10917

## Research note

INFINITE PFaffian COUNTERMODEL FAMILY. For each q>=7 not divisible by 3, the shift-matching digraph D_q in note_nori_arc_digraph_eulerian_high_chromatic_no_alt_cycles_20261016 has a nonsingular skew adjacency K_q=D_q-D_q^T over the real numbers, and det K_q is odd. Nevertheless it contains no alternating odd closed walk with one transit vertex. Proof: its Fourier directed-adjacency symbol, in ordered layer/s type, is F(z)=[[z,z,z,0],[z^2,z^2,0,0],[0,0,z,z],[0,z^2,z^2,z^2]]. The binary undirected adjacency symbol is F(z)+F(z^(-1))^T. Its determinant over F2 is z^(-6)(z^2+z+1)^6. This Laurent polynomial is coprime to z^q-1 precisely when 3 does not divide q. Hence the undirected adjacency is invertible over F2 for all those q. The integer skew adjacency reduces to that matrix mod2, so its determinant is odd. Being skew of even order, it has an odd integer Pfaffian. The existing transition-port labels a(t,u,s)=u+s and b(t,u,s)=u exclude all one-transit alternating walks. The models remain near-balanced, strongly connected, 5-regular, odd-girth five, codegree two, with unimodular directed adjacency. A separate symplectic Gram-Schmidt check gives Arf invariant zero for q=7 and q=11, matching the split type of the folded G5. LIMITATION: the countermodel does not have cubelike identity A^2=I modulo two, or complete square coherence. Thus this refutes only proof mechanisms based on skew Pfaffian oddness or split quadratic type, not those using the full involution identity.
