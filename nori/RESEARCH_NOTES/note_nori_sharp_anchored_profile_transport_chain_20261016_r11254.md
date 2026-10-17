# Sharp half-dimensional root-transport obstruction and balanced linear-distance lift

- Stable ID: note_nori_sharp_anchored_profile_transport_chain_20261016_r11254
- Author: session_nori_r11254_2
- Primary home: subsection:full_geodesic_color_profiles_span_the_entire_binary_space
- Labels: NORI1, root-transport, sharp-bound, all-dimensions, balanced, counterexample
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11254_2
- Updated session: session_nori_r11254_2
- Disposition: none
- Successor: none

## Related references

- note:note_nori_anchored_profile_transport_radius_two_20261016_r11254
- note:note_nori_profile_root_incidence_disconnected_20261016_r10917

## Research note

# Sharp anchored transport obstruction across all dimensions

For every n>=2, put r=floor(n/2), a_j=2j and b_j=2j+1 for j=0,...,r-1. Define S_w(c) as the supporting roots for complete direction-indexed profile w.

**Theorem.** Some legal antipodally odd coloring c of Q_n has a full red geodesic from zero, while
S_(e_1)(c)={x: x_(a_j)+x_(b_j)=1 for every 0<=j<r}.
In odd dimensions the final bit is unrestricted. Hence the nearest root supporting the one-bit-modified target is at Hamming distance r. This is universally optimal because reversal preserves the profile and replaces its starting root with its antipode, so every nonempty root-support set is antipodally invariant and contains a root within floor(n/2) of every specified vertex.

**Coloring.** Over F_2 put c_(a_0)(x)=x_(b_0), c_(b_0)(x)=1+x_(a_0), and c_(b_j)(x)=1+x_(a_j) for j>=1. Let
L(A,B,t)=1+AB+(A+B)t,
H(A,B,t)=A+B+AB+(A+B)t.
For r>=2 put c_(a_1)=L(x_(a_0),x_(b_0),x_(b_1)), and for j>=2 put c_(a_j)=H(x_(a_(j-1)),x_(b_(j-1)),x_(b_j)). If n is odd, add c_(2r)=x_0. Each rule ignores its direction bit. L and H toggle under simultaneous complementation of all three inputs (verify AB becomes AB+A+B+1 and (A+B)t becomes (A+B)t+A+B). Each unary rule also toggles under complementation, so the coloring is legal.

**Source witness.** At root 0, traverse anchor (a_0,b_0) first, then the other pairs in descending index order (a_(r-1),b_(r-1)),...,(a_1,b_1), inserting the odd extra direction first when present. Both anchor colors vanish. For j>=2 the predecessor pair is still (0,0) when a_j is used, so H=0. For a_1 the anchor has reached (1,1), so L=0. Each b_j follows a_j, so c_(b_j)=1+1=0. The odd extra edge is red. This yields the zero profile.

**Necessity.** Consider a path realizing e_1. The anchor colors (w_(a_0),w_(b_0))=(0,1) force P_0=x_(a_0)+x_(b_0)=1. Its two bits then evolve either (1,0)->(0,0)->(0,1) or (0,1)->(0,0)->(1,0). In particular AB=0 throughout. For each j>=1, w_(b_j)=0 and c_(b_j)=1+x_(a_j) force a_j before b_j if its initial a_j bit is zero, and b_j before a_j otherwise. Thus when a_j is used, its current reader bit b_j equals P_j=x_(a_j)+x_(b_j). At a_1, its zero color gives 0=L(A,B,P_1)=1+(A+B)P_1, hence P_1=1. If P_(j-1)=1, pair j-1 evolves (0,1)->(1,1)->(1,0) or its reflected ordering; always A OR B=1. The zero color of a_j therefore gives 0=H(A,B,P_j)=1+(A+B)P_j and forces P_j=1. By induction all P_j are one.

**Sufficiency.** Assume every P_j=1. Traverse pairs in descending index order. For each j>=1 use (a_j,b_j) if x_(a_j)=0 and (b_j,a_j) otherwise. Then b_j has color zero; when a_j is used, its predecessor pair has initial parity one and has not yet been traversed, and its current b_j reader bit equals one, so L or H gives zero. Finish with anchor (a_0,b_0) when x_(a_0)=1 and (b_0,a_0) otherwise, obtaining anchor colors (0,1). For odd n put the last direction before the others if x_0=0 and after the others otherwise, obtaining its target color zero. Thus every root satisfying the parity conditions witnesses e_1.

**Balanced corollary.** Every even N>=4 admits a vertex-balanced legal coloring with a zero-root witness of u and a one-bit-modified target u+e_i whose nearest supporting root has distance floor(N/4). Write r=floor(N/4). Use the Q_(2r) coloring above on old directions. Append 2r new directions with complementary rules d_j(x)=1+c_j(x). For N=4r+2 add two more rules x_0 and 1+x_0. All these new rules depend only on old bits. Each old direction is paired at every vertex with a new direction of complementary color, and the final pair is similarly complementary, proving balance. For each old rooted full geodesic and each prescribed pattern on new directions, place each new direction before all old steps or after all old steps to obtain its requested color. This does not change the old profile. Hence the target-support equations on the old bits persist and are sufficient. Their minimum Hamming displacement is r.

The theorem does not refute NORI1: the displayed source geodesic is monochromatic. It rules out all dimension-independent or sublinear bounds for transport of a prescribed rooted witness under a single changed profile bit. A separate subset-dynamic-programming enumeration confirmed the support equations for n=2,...,11; the proof is dimension-uniform.
