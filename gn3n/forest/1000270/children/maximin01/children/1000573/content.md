# Clean deletion augmentations are sparse, forcing recurrent central path destruction

## Statement

Let H be a minimum counterexample and let A|B|C be a lexicographically maximal spanning three-path cover with decreasing component orders a>=b>=c>=2. Put g=a-(b+c)>=1. First, in any spanning three-cover with |B|,|C|>=2, internal deletion positions of A admitting clean inherited-order split augmentations form an independent set. In the central interval g<=i<=a-g-1, every block-faithful deletion cover must cross-pair the A-prefix/A-suffix with B,C; adjacent block-faithful positions use opposite pairings, and three consecutive such positions force the two outer component orders. Consequently six consecutive central block-faithful positions would contain two adjacent clean positions, impossible. Hence every six consecutive central positions contain an index at which every exact deletion cover splits or reorders an inherited path.

## Body

# Clean deletion augmentations are sparse, forcing recurrent central path destruction

Let
A=(a_0,...,a_{a-1}) | B | C
be a spanning three-path cover. For an internal position i, write
L_i=A[0,i-1],  R_i=A[i+1,a-1].

Call i clean when H-a_i has an exact two-cover preserving the displayed orders of L_i,R_i,B,C and pairing them as two concatenations, one A-interval with B and the other with C.

Two adjacent internal positions cannot both be clean. If i and i+1 use the same pairing, one component from the H-a_{i+1} cover and the opposite component from the H-a_i cover are disjoint tight paths spanning H. If they use opposite pairings, after naming the side paths P,Q suitably the sequences
L_i P A[i+2,a-1]
and
(a_i,Q,a_{i+1})
are tight: every consecutive triple is inherited from one of the two deletion covers, and |P|,|Q|>=2 prevents an unchecked jump. These two paths again span H, contradiction. Thus clean positions form an independent set.

Now assume the component-order triple (a,b,c) is lexicographically maximal, a>=b>=c>=2, and put g=a-(b+c). Maximin compression gives g>=1, every exact deletion cover has both component orders at least b+c, and U=V(B) union V(C) is non-Hamiltonian.

Fix a central index g<=i<=a-g-1. Then L_i,R_i,B,C all have order below b+c. Hence if an exact cover is block-faithful—each inherited path remains one contiguous block in its displayed order—each component must contain two blocks. The pairing {L_i,R_i}|{B,C} is impossible because it would Hamiltonize U. Therefore every block-faithful cover has one of the two cross-pairing types
{L_i,B}|{R_i,C},  {L_i,C}|{R_i,B}.

Adjacent central block-faithful positions cannot use the same pairing, since the same two-cover splice argument would span H. Hence their pairing types alternate.

If i,i+1,i+2 are block-faithful, positions i and i+2 use the same pairing. Comparing the corresponding covers at distance two, their chosen components cover H and intersect only in a_{i+1}. If that shared vertex were an endpoint of either relevant component, deleting it from that component would leave two disjoint tight paths covering H. Therefore the later left-paired component must have the A-prefix first, and the earlier right-paired component must have the A-suffix second.

Suppose six consecutive central positions j,...,j+5 were block-faithful. Alternation plus the distance-two forcing applied to j,j+2; j+1,j+3; j+2,j+4; and j+3,j+5 implies that at positions j+2 and j+3 the left component is L_t P and the right component is Q R_t, with {P,Q}={B,C}. Thus j+2 and j+3 are adjacent clean positions, contradiction.

Therefore every central block-faithful run has length at most five. Equivalently, every six consecutive central positions contain an index for which every exact cover of H-a_i genuinely splits or reorders at least one inherited path.
