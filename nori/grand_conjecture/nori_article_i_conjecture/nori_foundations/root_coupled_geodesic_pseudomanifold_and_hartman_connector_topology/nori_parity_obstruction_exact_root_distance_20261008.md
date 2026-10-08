# A legal odd face coloring can require half the root bits to change

EXACT HAMMING DISTANCE TO A GOOD ROOT FOR THE FACE-LOCAL PARITY OBSTRUCTION.

Fix even n>=6 and a reference vertex a in Q_n. Let c_a(F,pi) be the parity of the number of exterior coordinates where the fixed face bit disagrees with a. This is an antipodal-reversal-odd ordered-three-face coloring because n-3 is odd.

THEOREM. Let D_n be the minimum Hamming distance d_H(a,y) over all starting vertices y for which SOME full antipodal geodesic beginning at y has at most one change under c_a. Then
 D_n = n/2-1, if n=0 (mod 6),
 D_n = n/2-2, if n=2 or 4 (mod 6).
For any fixed direction order p, the minimum over starting vertices y is this same D_n. In particular any uniformly guaranteed repair from the root a must leave its Hamming ball of radius D_n-1 before it can find a good full geodesic.

PROOF. Write d_i=y_(p_i) XOR a_(p_i). At window i the color is the parity of J_i, where J_i counts exterior disagreements with a. Consecutive changes satisfy
 w_i XOR w_(i+1) = 1 XOR d_i XOR d_(i+3).
Thus the number of color changes equals the number of seam edges i->i+3 on which d_(i+3)=d_i. The graph of all such edges on position set {1,...,n} is the disjoint union of three paths of lengths (numbers of vertices) l1,l2,l3, the residue classes modulo3. Along a path of l vertices, zero violated edges forces the bits to alternate; the minimal number of 1-bits is floor(l/2).

With at most one violated edge globally, choose either all chains alternating, or one chain having exactly one equal-adjacent-bit edge. On one chain with l vertices, splitting at this equal edge produces two alternating blocks of sizes u and l-u. Their minimum possible number of 1-bits is at least floor(u/2)+floor((l-u)/2), which is floor(l/2)-1 exactly when l is even and u is odd, and floor(l/2) otherwise. This lower bound is achievable: choose both alternating blocks with the minimum number of 1-bits; for two odd blocks their first and last bits are zero, so the join is 00 and is a violated edge. If one or both blocks are even, the lower bound floor(l/2) is attained by suitable choice of phases compatible with an equal join; alternatively use an alternating unbroken chain, which is never worse than floor(l/2).

Hence the total minimum is
 D_n = sum_(r=1)^3 floor(l_r/2) - 1_{there exists an even chain of length >=2}.
The three chain lengths are independent of the direction labels and determined by n. For n=6q they are (2q,2q,2q), giving 3q-1=n/2-1. For n=6q+2 they are (2q+1,2q+1,2q), giving 3q-1=n/2-2; here n>=8 implies q>=1. For n=6q+4 they are (2q+2,2q+1,2q+1), giving 3q=n/2-2. The indicated alternating/equal-edge assignments construct an appropriate root y for any fixed direction permutation p, attaining the bound. QED.

IMPLICATION. The obstruction c_a is a legitimate NORI coloring with abundant monochromatic geodesics elsewhere, but a one-change witness can require changing roughly n/2 starting-coordinate bits from a. This rules out any proof claiming a bounded-radius root-repair guarantee around EVERY starting root. It strengthens the exact fixed-root obstruction and explains why a genuinely root-coupled global complex, rather than a single Freudenthal root chamber or bounded local correction, is mathematically necessary.
