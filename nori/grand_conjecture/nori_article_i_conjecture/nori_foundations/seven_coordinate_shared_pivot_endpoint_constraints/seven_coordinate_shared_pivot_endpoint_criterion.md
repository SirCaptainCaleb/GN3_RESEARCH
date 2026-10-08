# Independent and shared endpoint pivots for ordered k-face windows

## Development

Central-pivot structure for consecutive ordered k-face windows.

Statement.
Let k≥2, let c assign binary colors to ordered k-dimensional cube faces, independently of the traversal corner, and let p_1,…,p_m be distinct successive directions of a cube geodesic segment, with all initial bits outside the specified pivots fixed.

(a) If m=2k, write its k+1 consecutive window colors as w_1,…,w_{k+1}. Varying x_{p_{k+1}}=u and x_{p_k}=v leaves w_2,…,w_k invariant and independently gives a word (A(u),M_1,…,M_{k−1},E(v)).

(b) If m=2k+1, varying the single bit x_{p_{k+1}}=t leaves the k interior windows invariant and gives a word (A(t),M_1,…,M_k,E(t)).

In either case, let q count color changes within M_1,…,M_s. A choice of pivots yields at most one change exactly when q+[A≠M_1]+[E≠M_s]≤1. For the shared-pivot case (b), if q=0 and both t choices fail, then A(0)=A(1)=E(0)=E(1)=1−M_1. If q=1 and both endpoints toggle with t, both choices fail exactly when A(0)⊕E(0)≠M_1⊕M_s.

For k=3, (a) is the six-move independent endpoint square and (b) is the seven-move shared-pivot criterion. No antipodal oddness is required.

Proof.
A window beginning at position i has free directions p_i,…,p_{i+k−1}; flipping the starting bit of any free direction leaves the underlying ordered k-face unchanged.

For m=2k, the intersection of the free-direction sets of all interior windows i=2,…,k is {p_k,p_{k+1}}. The first window has p_k free and p_{k+1} fixed, whereas the last window has p_{k+1} free and p_k fixed. Thus varying x_{p_{k+1}} can affect only the first color, varying x_{p_k} can affect only the last, and the two variations are independent. This proves (a).

For m=2k+1, the intersection of the free-direction sets of the interior windows i=2,…,k+1 is exactly {p_{k+1}}. This direction is fixed outside both endpoint windows, proving (b).

Every change belongs either to the interior word or to one of its two boundary edges. Hence the displayed change-count equality and the exact criterion. If q=0 and no shared-pivot value succeeds, both boundary mismatches must hold for each t. If q=1 and each endpoint is sensitive, flipping t complements both endpoint colors; the two candidate endpoint pairs are therefore complements and share the same XOR. A target pair (M_1,M_s) is among them precisely if its XOR agrees.

Dimension-seven consequence. For k=3 and m=7, the three-window middle block always has a shared control direction (the fourth move). A hypothetical counterexample must satisfy the stated endpoint rigidity after every choice of seven directions and all other starting bits, whenever that interior block is monochromatic or has one change. This gives exact necessary local conditions, while global closure still requires compatibility between overlapping move orders and starting vertices.
