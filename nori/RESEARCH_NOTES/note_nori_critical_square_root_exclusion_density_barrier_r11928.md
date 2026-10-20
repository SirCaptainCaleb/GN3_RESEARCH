# Critical square root exclusion and seven-eighths density obstruction

- Stable ID: note_nori_critical_square_root_exclusion_density_barrier_r11928
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: NORI1, paired-flat, critical-square, root-support, dimension-uniform, method-obstruction
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11928_1
- Updated session: session_nori_r11928_1
- Disposition: none
- Successor: none

## Related references

- None

## Research note

# Root exclusion at a critical paired square and a density barrier

Let G be any legal antipodally odd paired-flat coloring of Q_(2m), m>=2, and let S=F union bar(F) be an antipodal pair of alternating squares in one prescribed direction pair. Assume a legal switch on S takes G from red-successful to red-unsuccessful.

THEOREM. No vertex of S is a root of a red full antipodal geodesic in G. Equivalently, if G has a rooted red full antipodal geodesic from any one of the eight vertices in S, then the switched coloring still has a red full antipodal geodesic.

PROOF. The established two-hit transport theorem requires every red full geodesic of G to hit S in one strictly internal edge. A dimension-simple path starting at a vertex of F cannot visit F after leaving it. Its red steps within F cannot be consecutive: the red matching on the prescribed direction pair is an involution. Thus it can hit F only in its first edge. To reach bar(F), the path must first traverse all 2m-2 directions outside the pair; any red edge in bar(F) must therefore be the last edge. The same argument interchanges F and bar(F). A rooted red geodesic from S would have no hit or only an endpoint hit, contradicting the critical switch assumption. This uses arbitrary nonlinear gates and direction simplicity. Reversal and antipodal oddness imply that red-root success is closed under complementation and is equivalent to blue-root success.

COROLLARY. If at most six vertices fail to start a red full antipodal geodesic in G, then every legal paired-square switch preserves red success. More generally, a critical good coloring has at least eight failed roots, forming the two squares of the proposed switch orbit.

SHARPNESS OF ROOT SUPPORT ALONE. On Q6 with prescribed pairs (0,1),(2,3),(4,5), let the red selector f_i(z) for outside four-bit index z be ((M_i >> min(z,15-z)) & 1) + [z>=8] mod2. Take masks (M0,M1,M2)=(0x53,0xea,0x80). These are legal antipodally odd paired-flat gates. Let S be the two faces in pair 2 whose outside indices are 6 and 9. Exhaustively enumerate every root and all 6! direction-simple full words: precisely 56 of 64 roots support red full geodesics; the eight failed roots are the eight vertices of S. There are 244 rooted red full geodesics, 190 avoiding S and 54 meeting S once internally. Therefore G is robust at S despite the maximal failure of root anchoring at that orbit. The eight-root necessary condition cannot be strengthened solely by root-count arguments in Q6.

DIMENSION-UNIFORM DENSITY OBSTRUCTION. For m>3, retain the Q6 gates independently of added direction pairs, and give every new pair the gate f_j=x_0, the first old vertex bit. Every red full path projects to one in the core, so any root with a failed core projection remains failed. Conversely, any red full core path from any specified root traverses direction 0 once; insert one red step of each new pair before that move and its complementary red step after it. The new gates change value across direction 0, giving a red full path from every extended root whose core projection was successful. Thus 7/8 of all roots support red full paths in each Q_(2m), and an antipodally paired square orbit with eight vertices remains disjoint from that root-support set. Root density of 7/8 does not produce a red root on every paired-square orbit.

Independent verifier: nori_root_orbit_avoidance_verifier.py tests the full Q6 path census and rooted full-path dynamic programming in Q6,Q8,Q10. The construction does not supply a good-to-bad critical boundary or close NORI1. This is a root-anchoring obstruction and a limited forcing consequence, not an unrestricted closure theorem.
