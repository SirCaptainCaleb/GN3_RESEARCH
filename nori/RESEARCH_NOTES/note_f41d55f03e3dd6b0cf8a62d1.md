# Folded cube Gram-graph fragmentation

- Stable ID: note_f41d55f03e3dd6b0cf8a62d1
- Author: unspecified; session provenance retained
- Primary home: subsection:antipodal_multifacet_bridge_and_seven_coordinate_universality
- Labels: NORI1, folded-cube, gram-graph
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

For each r>=1, take d=4r+1 and split the first 4r directions into four-bit blocks (a,b,c,d). Set their color rules to (x_c,1-x_c,x_a,1-x_a), and the remaining direction q to x_a of the first block. The coloring is antipodally odd, with zero degrees 2r or 2r+1. Its folded-cube orientation is therefore near-balanced. The four-bit red factor has connected components of sizes 12 and 4; the smaller component is entirely in x_a=1. In the product of r such factors, the extra q-direction joins the two copies of a component only if its first block is the large component. Hence the red cube graph has 3*2^(r-1) components. In the folded orientation, the common-out-neighbor graph is the two-step zero-edge graph on even cube vertices, so it has the same components. Its largest component has 12^r of the 16^r quotient vertices, fraction (3/4)^r. The coloring has a full red geodesic, by concatenating factor red geodesics from integer roots 1 in direction order (3,0,2,1), then traversing q. Every near-balanced folded G_(2m+1) common-out-neighbor graph has minimum degree at least binom(m,2): each vertex has at least m out-neighbors, each has at least m in-neighbors, and two folded-cube vertices have at most two common neighbors. The construction attains equality at the even root where the a and c bits of every block are 1, the b and d bits are 0, and q=0. This provides all-dimensional counterexamples to universal connectivity and giant-component assumptions for the auxiliary Gram graph.
