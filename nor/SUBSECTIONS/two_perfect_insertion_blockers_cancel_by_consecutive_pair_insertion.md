# Two perfect insertion blockers cancel by consecutive pair insertion

## Metadata

- ID: two_perfect_insertion_blockers_cancel_by_consecutive_pair_insertion
- Parent Section: directed_nor_union_closed_bridge
- Position: 103
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Composition

(none yet)

## Development

Pure-orientation two-blocker cancellation. Let O=(v_1,...,v_m) have alpha-word 0^p 1^q with p,q>=1. For an exterior vertex x write s_i^x=alpha(x,v_i,v_{i+1}), 1<=i<=m-1. The one-vertex insertion calculus shows that the unique scan which blocks prepend, append, and every interior insertion into O is B=1^(p+1)0^q (with the evident truncation at the ends). Suppose two exterior vertices x,y both have this blocking scan.

Define c_i=alpha(x,y,v_i). In any tournament representative of the switching class normalized so O is a directed Hamilton path, write q_i^x=t(x,v_i), q_i^y=t(y,v_i). Then s_i^x=q_i^x xor q_{i+1}^x and similarly for y, while c_i differs from q_i^x xor q_i^y by a constant depending only on the oriented edge xy. Consequently
c_i xor c_{i+1}=s_i^x xor s_i^y.
Since the two scans are identical, c_i is constant in i. Reversing the order of x,y complements every c_i, so choose their order so this constant is 1.

Insert the consecutive pair x,y in the gap between v_p and v_{p+1}. For p>=2 the four new local statuses are
s_{p-1}^x, c_p, c_{p+1}, s_{p+1}^y = 1,1,1,1.
All untouched statuses before this packet are 0 and all untouched statuses after it are 1. Hence the enlarged order has at most one change. For p=1 the left packet is truncated and the new initial statuses are c_1,c_2,s_2^y=1,1,1, followed by the old 1-run, so it is monochromatic. Thus two vertices cannot simultaneously be perfect insertion blockers for the same one-change carrier.

This is a genuine pair-extension mechanism absent from the one-vertex induction. Adversarially, any minimum counterexample must ensure that no one-change order on a codimension-two deletion has both omitted vertices in the unique blocking state. Equivalently, for every such carrier at least one omitted vertex has some individually admissible insertion, although inserting it may still leave the other vertex globally blocked. The next target is to exploit this asymmetry by choosing the codimension-two carrier or insertion position extremally.

## Frontier

- Development version when composed: None
- Development version now: 1
