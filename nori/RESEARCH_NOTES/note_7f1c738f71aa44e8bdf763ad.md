# Lazy paired-sweep trace rigidity

- Stable ID: note_7f1c738f71aa44e8bdf763ad
- Author: unspecified; session provenance retained
- Primary home: subsection:paired_direction_involutions_and_geodesic_endpoint_matchings
- Labels: NORI1, trace, balanced
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r10003_3
- Updated session: session_nori_r10003_3
- Disposition: none
- Successor: none

## Related references

- None

## Research note

Let c be an undirected binary edge coloring of Q_n and L(c) its paired lift to Q_(2n). Denote by K the sum of original zero-edge full-sweep permutation matrices. Let H(t) sum all lazy lifted full sweeps with adjacent original/dummy direction pairs, each update being tI+(1-t)U_i. Then tr(Ptilde H(t)^2)=2^(3n)(1-t)^(2n) tr(PK^2) for 0<=t<=1, and tr(Ptilde H(t))=0. Proof: in each paired position precisely one zero-edge swap changes its bit. Thus the product of the two lazy factors equals tI+(1-t)U_i U_(n+i). Under (x,y)->(x,x xor y), the active paired factor acts by U_i on x and flips the corresponding second-block bit. The lifted antipode complements x and fixes the second block. Across two sweeps, each pair must be active twice: zero activations leave x_i unchanged and one activation changes the second-block bit. Thus every contributing term activates all n pairs in both sweeps and has weight (1-t)^(2n). The deterministic trace transfer gives the factor 2^(3n). QED. For c_i(x)=x_((i+1) mod 3), direct enumeration gives original trace 18, lifted t=0 trace 9216 and lifted t=1/2 trace 144.
