# Terminal barrier roots have canonical central cuts in the centered Boolean cube

## Metadata

- ID: terminal_barrier_roots_have_canonical_central_cuts_in_the_centered_boolean_cube
- Parent Section: protected_root_certificates_and_cellular_extraction
- Position: 74
- Row version: 1
- Development version: 1
- Composition version: 1
- Composition stale: False

## Composition

Every terminal ternary four-coordinate barrier has a canonical central prefix cut between its middle coordinates. Its physical root is exactly the difference of that cut and its same-rank Johnson successor. Complement sends the central cut to its complement and the root to its negative, so terminal barriers live equivariantly in the graded cut space embedded in the centered Boolean cube.

## Development

A terminal ternary threshold-band root has a canonical cut-crossing provenance even when it does not cross the original normalized phase cut.

Let a full coordinate order contain a terminal barrier transition on four consecutive coordinates
(a,b,c,d)
at positions j,j+1,j+2,j+3, with normalized physical root
rho=e_a-e_d.
Define the central prefix cut
C={coordinates in positions 1,...,j+1},
that is, cut the order between b and c. Then a lies in C and d lies outside C. Put
C'=(C-{a}) union {d}.
Immediately
1_C-1_C'=e_a-e_d=rho.
Thus the barrier occurrence determines a legitimate adjacent exchange in the Johnson layer J(n,|C|). No choice among the three rank cuts crossed by the slide is needed: the central cut is distinguished by the two-plus-two split of the four-coordinate transition packet.

This central choice is reversal-equivariant. Reverse the full order. The barrier packet becomes (d,c,b,a), its normalized root becomes -rho, and its central prefix cut is exactly V minus C. Therefore
C -> C^c,
C' -> (C')^c,
rho -> -rho.

Consequently all terminal barrier cuts of varying ranks admit one common antipodal embedding. For every cut C subset V define
u_C=1_C-(1/2)1 in R^n.
These are the vertices of the centered Boolean n-cube. Complement is exact antipodality:
u_{C^c}=-u_C.
Moreover
u_C-u_C'=1_C-1_C'=rho.
Hence every terminal threshold-band root is an oriented same-rank chord between two centered-cube vertices, and reversal sends the entire oriented cut-root state to its negative.

For a fixed rank k this reduces to the centered hypersimplex/Johnson picture after removing the all-ones component. But the cube embedding permits roots from different barrier ranks to coexist without falsely identifying them with the original minimum-phase cut.

This repairs the local-to-global provenance gap identified in root 69. The correct global state for terminal barrier roots is not one fixed hypersimplex. It is the graded cut space
union_{k=1}^{n-1} Delta(n,k),
equivariantly embedded in the centered Boolean cube, with complement pairing rank k to rank n-k.

The original threshold information is still relevant: the central barrier rank records how far the obstruction has propagated from the target cut, and the left/right band side records on which side it lies. But legitimate cut-crossing provenance is now automatic for every terminal barrier occurrence.

A next carrier theorem should use the centered cube rather than force all barriers onto one Johnson layer. Positive physical root dependences become mass-preserving sums of same-rank cube chords. Fixed-point or Borsuk-Ulam arguments can then retain the actual local barrier cut while complement-reversal acts by the standard antipodal map on the cube.
