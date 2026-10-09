# Article III — Monochromatic reachability and antipodal splicing

# Complementary reachability and antipodal extraction

Let c be a reversal-odd coloring of ordered physical three-faces of Q_n. A geodesic of length k has k-2 consecutive ordered-window colors. It is monochromatic when this word is constant, and good when the word changes at most once. The central question is to extract a full good path from two genuinely monochromatic branches whose coordinate supports are complementary.

## Reversed-two-tail criterion

Fix an ordered terminal pair J=(a,b) and D=[n] without {a,b}. For a cube root x, define R_J(x) as the family of supports U subset D for which some monochromatic direction-distinct path starts at x, uses precisely U and then the final ordered directions (a,b). The monochromatic color is existential. The exact reversed-tail extraction theorem states that a complementary pair U in R_(a,b)(x) and D without U in R_(b,a)(x), from the same root, yields a full antipodal geodesic with at most one change.

The physical terminal order matters. Ordinary concatenation of arbitrary monochromatic three-window paths creates two new ordered windows at the seam, and the colors of those windows are not determined by the two interior monochromatic colors. In the reversed-two-tail construction, the actual common root, complementary supports, and reversed terminal pairs provide the special face identifications that make extraction valid. Thus a topological coincidence of support labels is useful precisely when it retains these data.

## Accessibility and state carriers

For an undirected edge coloring, let E_q(x,S) assert existence of a q-monochromatic geodesic from x with direction support S. For nonempty S, deleting its first direction proves

E_q(x,S) iff there exists a in S such that c({x,x xor e_a})=q and E_q(x xor e_a,S without {a}).

The converse prepends the edge. The union E_0 union E_1 is accessible under deletion of at least one direction, but need not be a Boolean downset. Its collision with the same-root complementary-support transform is equivalent to a one-switch antipodal edge geodesic. Under antipodal oddness, the standard rotation converts such an existential one-switch edge witness into a monochromatic antipodal witness.

Root-endpoint states (x,y), ranked by the number of differing coordinates, admit covers by extending either endpoint in an unused direction. Every monochromatic cover-chain from a diagonal state is an actual monochromatic geodesic. Coordinatewise the order complex is a circle, so the full state complex triangulates an n-torus, with restricted equivariant index. Barycentric reachability carriers also encode exact targets: the center of the support face D lies in the simplex complex genuinely witnessed by q-paths from x exactly when x can reach x xor D monochromatically. Nestedness forces the carrier simplex to contain both empty and D supports.

## Signed profile topology

For NORI use label pairs (J,U), and let the involution send (J,U) to (rev J,D without U). At each root x retain only labels of actual monochromatic witnesses. Their signed nerve has two complete shores because every three-edge path is automatically monochromatic. Mixed shore intersections at distinct roots can form equivariant four-cycles even under failure of the grand conjecture. The missing same-root diagonals are exactly the desired complementary-terminal coincidences.

A reduced two-ended path memory records the two endpoints, first and last direction pairs, and switch-state information. At rank six distinct histories can share one such memory state, so a quotient-level intersection must be lifted using actual seams and roots. This identifies the exact gap: a topological theorem must force a diagonal signed-root intersection with complementary reversed terminal memory, rather than a generic equivariant label coincidence.
