# Physical window shifts and root-shuttle transport

# Physical window shifts, antipodal transport, and connector obstructions

Fix n>=5. An actual ordered three-face window is denoted W_z(a,b,c), with three distinct free coordinate directions a,b,c and all other coordinates fixed as in z. As z ranges over its face the same ordered physical window is represented; this independence is essential when gluing successive four-edge windows. The active NORI involution is tau W_z(a,b,c)=W_(bar z)(c,b,a), and its color is complementary.

## Transport in the distinguished-middle-direction graph

Fix i. The window-shift graph H_i has actual ordered windows containing i, with an edge when the two windows are consecutive triples along a genuine four-edge direction-distinct path and i belongs to the two common middle directions. For pairwise distinct a,b,d,i,k, a two-step shuttle connects W_z(a,i,b) to W_(z xor k)(d,i,b) through W_z(i,b,k). Both constituent edges are actual four-edge shifts. The intermediate face has free set {i,b,k}, so changing the k-bit of its representative leaves this physical face unchanged. This allows an exterior bit to be toggled while exchanging an outer free direction. Two-step shuttles can likewise preserve the exterior bit.

The shuttles provide explicit paths from any v to tau(v), by successively bringing exterior coordinates into a free slot, changing their fixed bits, and returning the desired free directions. A proved construction gives even-length paths linear in n; the strengthened exact transport theorem establishes the shortest length

L(n)=max(6, 2 ceil((n-1)/2))

for every actual window and all n>=5. In particular each exterior coordinate must enter a free slot to complement its fixed bit, and the original outer directions must undergo an exchange to reverse the ordered window. These necessities account for the lower bound, with the even parity of H_i paths and the minimal outer exchange supplying the remaining restriction. The companion constructive shuttles attain the bound.

## Guaranteed monochromatic shifts

An H_i path of even length from v to tau(v) has endpoints of opposite colors. Therefore at least one consecutive edge along it joins windows of equal color: if all L consecutive colors differed and L were even, the endpoint colors would coincide. Such an equal-color shift corresponds to an actual monochromatic four-edge geodesic connector.

Let E_0=2^(n-2)(n-1)(n-2)(n-3) be the number of edges in each of the two middle-slot orientation orbits. Translate roots and permute directions fixing i to average a chosen optimal antipodal path over the full orbit. If N_i is the total number of distinct equal-color connector edges in both middle-slot orbits, the averaging argument and antipodal reversal give

N_i >= 2 ceil(E_0/L(n)).

The lower bound is quantitative and applies to arbitrary exterior-dependent physical ordered-three-face colorings. It forces many real local monochromatic connectors, with the two middle-slot types equally represented. Their respective roots and unused supports may vary.

## Physical gluing constraints

A root shuttle also exhibits an induced four-cycle on four actual windows, with both diagonals forbidden by direction-distinct four-edge incidence. Thus the shuttle square is a genuine 1-dimensional loop in the physical incidence graph; filling it by triangles on the same four vertices would introduce nonexistent cube paths. Any topological filling argument must use further actual windows with verifiable ordered-face incidence.

There is a separate obstruction to orienting a simple zero-seam-side label continuously under adjacent exchanges. Two full Q_7 geodesics differing by one adjacent transposition can both have opposite endpoint colors and three switches while the position of their unique equal adjacent pair moves across the midpoint. The prescribed windows extend to a legal reversal-odd coloring since their physical-face orbits impose consistent color constraints. Accordingly the transport graph requires richer path-memory data than the location of a single equality seam.

## Extraction frontier

The transport theorem yields genuine antipodal paths in window space, a nontrivial quotient-cover class, and exponentially many monochromatic four-edge connectors. Full NORI requires a single n-edge geodesic with at most one change. The missing theorem is a certificate-preserving global compatibility rule that selects connectors with matching physical roots, ordered terminal pairs, and complementary remaining coordinate supports. The local existence and density results above establish the carrier geometry for that global problem.

## Research-note boundary after independent audit

The alternating shuttle-square counterexample and duplicate refinement are now in a linked note; the genuine shuttle-distance and induced-square proofs remain published.
