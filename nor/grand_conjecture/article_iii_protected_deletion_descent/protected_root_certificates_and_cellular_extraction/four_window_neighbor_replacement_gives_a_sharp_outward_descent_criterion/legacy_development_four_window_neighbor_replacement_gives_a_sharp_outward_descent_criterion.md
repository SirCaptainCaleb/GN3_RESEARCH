# Four-window neighbor replacement gives a sharp outward descent criterion — preserved pre-item development

## Four-window neighbor replacement and the corrected descent criterion

### Scope and notation
Work with an alternating ternary label alpha and a fixed switch cut k. The target is eta at window ranks i<=k and 1-eta at ranks i>k. Let D_i be the threshold defect indicator, E=sum D_i, d_k(i)=k-i on the pre side and i-k-1 on the post side, and Q_k=sum D_i d_k(i)^2.

Consider the interior adjacent swap
(...,y,z,w,a,b,c,...) -> (...,y,z,a,w,b,c,...).
Let (w,a,b) have window rank t. Assume the tracked b-centered window at rank t+1 changes from defective to satisfied. The four changed window ranks are t-2,t-1,t,t+1. No others change. Write
A=D_(t-2), B=D_(t-1), C=D_t, and N=D'_(t-2).
Alternation complements the colors of (z,w,a) and (w,a,b). Each remains at its own rank, so their defect indicators become 1-B and 1-C, regardless of the cut. The tracked indicator becomes zero. Consequently
E'-E=N-A+1-2(B+C).

This identity repairs the missing outer-window calculation in root §81, arbitrary_complementary_tucker_cells_still_contain_a_controlled_local_repair_event, and root §92, quadratic_switch_distance_also_terminates_neighbor_replacement_equality_transport.

### Sharp outward descent theorem
Assume t+1<=k, so all four ranks are pre-switch, and B+C>=1. Then the left-neighbor replacement strictly decreases the lexicographic potential (E,-Q_k).

Proof. If B+C=2, the displayed identity gives E'-E<=-2. If B+C=1, it gives E'-E<=0. Equality requires A=0 and N=1. Put d=k-t>=1.
If B=0,C=1, the old defects in the packet occupy t,t+1 and the new ones t-2,t-1; hence
Q'_k-Q_k=(d+2)^2+(d+1)^2-d^2-(d-1)^2=8d+4>0.
If B=1,C=0, they occupy t-1,t+1 before and t-2,t after; hence
Q'_k-Q_k=(d+2)^2+d^2-(d+1)^2-(d-1)^2=4d+2>0.
Unchanged ranks cancel. This proves the theorem. The reflected post-switch right-neighbor move has the same conclusion.

This is a theorem about the full four-window packet, not the two-window truncation used previously.

### The excluded case is a real obstruction to the old potential
If B=C=0, then E'-E=N-A+1 lies in {0,1,2}. Equality holds precisely when A=1,N=0. Then the defect ranks change from {t-2,t+1} to {t-1,t}, and
Q'_k-Q_k=(d+1)^2+d^2-(d+2)^2-(d-1)^2=-4.
Thus equality is inward transport and makes (E,-Q_k) worse. In the other two cases E increases.

In particular, a fixed-cut minimizer of (E,-Q_k) cannot admit an outward tracked-disappearance swap with B+C>=1. Such a disappearing tracked defect at a minimizer must instead have both intervening windows satisfied. This yields a proved local restriction on extremal states, but not a terminating global path rule.

### Flat alternating examples showing sharpness
Use seven coordinates ordered y<z<w<a<b<c<d. Define directed pair bits f(u,v), with f(v,u)=1-f(u,v), and
alpha(u,v,w)=f(u,v) xor f(u,w) xor f(v,w).
This label is alternating, cyclically invariant, and coboundary-flat: the four face values on every ordered quadruple have XOR zero, because each directed pair occurs twice.

Set every increasing pair bit to zero except
f(y,a)=f(w,c)=f(b,c)=1.
The order (y,z,w,a,b,c,d) has word 00011. The swapped order (y,z,a,w,b,c,d) has word 11101. At cut k=4 and eta=0 the target is 00001, so E increases from 1 to 3. The original unique violating window is (a,b,c), centered at b and cut-adjacent; after the swap its replacement (w,b,c) is satisfied. Thus the example also meets nearest-violation selection at the starting state.

For an equality example, instead use increasing pair bits
f(y,w)=f(w,c)=f(b,c)=1,
with all others zero. The old word is 10011 and the new word is 01101. Against target 00001, both have E=2, but Q_4 drops from 9 to 5. Again the original nearest defect is the b-centered rank-4 window and it disappears.

These are local counterexamples to a proposed repair law, not counterexamples to NOR and not a small-order closure search.

### Consequences for the Article III frontier
The unrestricted assertion that neighbor-replacement disappearance is always strict defect improvement or outward equality transport is false, even in the flat alternating sector. The fixed-cut neighbor potential is valid under the additional intervening-defect condition B+C>=1 in the outward direction. Inward directions need a separate argument.

The later assertion in a_complementary_tucker_edge_seeds_a_terminating_central_threshold_band that arbitrary complementary-cell paths have already acquired a terminating fixed-cut neighbor handoff therefore does not follow from §92. Its genuine switch-crossing central seed and conditional outward flat-band repairs are not refuted here.

The dimension-saturation/vertical-edge argument may still produce available complementary-middle states. To claim a terminating extraction from them, supply a path rule ensuring every neighbor-disappearance step satisfies the corrected outward criterion, or prove another legal improvement for the B=C=0 branch. Merely tracking first disappearance along an arbitrary chamber path does not supply that condition.
