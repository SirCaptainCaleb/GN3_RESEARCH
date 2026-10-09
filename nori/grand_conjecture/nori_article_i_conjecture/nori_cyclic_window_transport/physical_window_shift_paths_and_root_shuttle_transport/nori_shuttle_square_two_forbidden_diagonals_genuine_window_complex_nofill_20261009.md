# Exact root-shuttle square: four genuine shift edges, two impossible physical window diagonals

# Root-bit shuttle squares are literal induced 4-cycles with two forbidden diagonals

Fix n>=5 and four distinct directions a,i,b,k. For an actual physical cube vertex z, use the notation W_z(p,q,r) for the actual ordered three-face through z with ordered free directions (p,q,r). Put
  A  = W_z(a,i,b),
  B  = W_z(i,b,k),
  A' = W_(z xor e_k)(a,i,b),
  C  = W_z(k,a,i) = W_(z xor e_k)(k,a,i).
The equality in C holds because k is a free direction. A and A' are DIFFERENT actual physical ordered-face windows: k is fixed outside their common free triple and its bit is opposite.

**THEOREM (exact shuttle-square incidence, coloring-independent).** The four actual physical windows A,B,A',C are distinct and form an INDUCED FOUR-CYCLE in the full physical window-shift graph H_i:
 A--B--A'--C--A.
All four edges remain edges of W_good(c), the simplicial complex of jointly realizable <=1-switch geodesic windows, for EVERY binary physical ordered-three-face coloring c, because any consecutive two-window four-edge geodesic has at most one switch. However BOTH diagonals
 A--A' and B--C
are ABSENT even from the full color-free actual cooccurrence relation on direction-distinct geodesics. In particular the induced W_good complex on these four windows is exactly a C4 with NO 2-simplex. Neither local triangular subdivision of this square on its four vertices is valid.

**Proof of the four edges.** A and B are the two consecutive actual windows of an ordered four-edge path with direction word (a,i,b,k) centered through z. Because B is FREE in k, it is the SAME ordered physical three-face when represented by z xor k, so B and A' are also consecutive actual windows of another path with the same four-direction order (a,i,b,k). Likewise C and A are consecutive windows with word (k,a,i,b), and C and A' are consecutive windows with that same order represented by z xor k. Every comparison has i in the shared middle pair. Thus these are four literal sector H_i shift edges.

**Proof of the forbidden diagonals.** A and A' have identical ordered free-direction triples (a,i,b) but are distinct physical faces. Along any direction-distinct geodesic, the unordered free triples of windows at different positions are distinct: equality would repeat at least one direction. Thus no genuine path contains BOTH A,A'. For B and C, the ordered free triples are respectively (i,b,k) and (k,a,i); they share exactly the two free directions {i,k}. If two windows with a two-direction free overlap occur along a direction-distinct geodesic, their window positions must differ by exactly one, and their ordered triples must have a literal two-letter de Bruijn overlap, either the final two directions of B equaling the initial two of C or vice versa. Here (b,k)!=(k,a) and (a,i)!=(i,b). Hence no such path contains BOTH B,C. The induced 4-vertex complex has exactly the four claimed edges and no diagonals or triangles. QED.

**Alternating obstruction is ACTUALLY REALIZABLE in active NORI.** Assign c(A)=c(A')=0 and c(B)=c(C)=1. These are valid independent face assignments: none of the four displayed ordered physical faces is the antipodal reversed mate of another (the potential pair A/A' has different ordered orientation under reversal since a!=b; B/C have different free triples). Therefore extend to a legal GLOBAL active coloring by assigning complementary colors to all physical antipodal-reversal mates and choosing any colors on remaining orbits. In this coloring the shuttle 4-cycle has NO monochromatic window-shift edge at all (all four compare unequal colors), although its four literal good-window-complex edges remain available as at-most-one-switch four-geodesics. In particular an arbitrary centered shuttle square need not yield a single good connector, nor can its two transport orders be merged into a good-window triangle using only these four windows.

**Global interpretation.** The optimal-length antipodal root transport theorem (Item nori_exact_optimal_antipodal_window_shift_transport_length_and_density_20261009) constructs sector routes as sequences of genuine shifts. Its binary endpoint-parity forces an ODD number of monochromatic edges on the complete antipodal path, but this local 4-cycle shows why the elementary root-bit-shuttle relation cannot be filled automatically in W_good. A prospective beta*w pentagon annulus must recruit ADDITIONAL physical ordered windows and actual common <=1-switch geodesic certificates. The present no-go is local and sharp: it rules out the naive four-vertex triangular filler, not arbitrary longer annuli or the full NORI conjecture.
