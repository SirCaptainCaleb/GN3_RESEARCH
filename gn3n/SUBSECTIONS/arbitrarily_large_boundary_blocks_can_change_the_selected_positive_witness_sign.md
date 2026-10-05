# Arbitrarily large boundary blocks can change the selected positive witness sign

## Metadata

- ID: arbitrarily_large_boundary_blocks_can_change_the_selected_positive_witness_sign
- Parent Section: terminalization_reachability_and_the_exact_frontier
- Position: 54
- Row version: 1
- Development version: 1
- Composition version: None
- Composition stale: False

## Cold composition

(none yet)

## Development

The protected corridor intersection bound does not make boundary blocks sign-neutral.

For any N>=4 and d>=6 set a=N-3, b=a+d, n=a+b+3=2N+d-3, and m=n-2. Let F have one freely permutable block B of N vertices in the first N positions, followed by singleton vertices z_1,...,z_{n-N}. The protected corridor C=[a+1,b+3] meets B in exactly its last three positions.

Choose an arbitrary boundary tournament on B. For distinct u,v in B prescribe h(u,v,z_1)=1; prescribe h(u,z_1,z_2)=0 for every u in B. On the fixed singleton sequence, set every displayed consecutive status to zero except the status at global start b+2, which is one. Complete all other boundary-reversal pairs arbitrarily. These prescriptions are compatible: their middle vertices and exterior vertex placements distinguish the prescribed families, and none is the boundary reversal of another prescribed triple.

In every chamber of F, write the last four block vertices as (u,v,w,t), occupying positions a,...,a+3=N. The statuses from a onward begin
h(u,v,w), h(v,w,t), 1, 0, 0,...
and thereafter remain zero through b+1, with the fixed one at b+2 and zeros beyond. The right determining word at b is therefore always 001. The left word at a is positive (001 or 011) exactly when h(u,v,w)=0.

Every strictly inward positive span-two word is absent. At a+1 the three bits are h(v,w,t),1,0, giving 010 or 110; at a+2 they are 100; all later triples before b are zero triples. Likewise no strictly inward alternating 0101 occurs: the beginning is h(v,w,t),1,0,0, and the remaining inward interval is a zero string terminating in the one at b+2. At a itself an alternating word ends in zero, and cannot be 0101. Any positive word wholly in earlier block positions is farther outward than the selected span-two edge. Hence F is protected and its selected unsigned witness depth is the same in every chamber.

Use the central-pair tie gauge, and choose its fixed comparison to give the left intrinsic sign. The central pair consists of singleton vertices because d>=6. Its gauge is consequently constant throughout F. If h(u,v,w)=0 both reflected occurrences are present and the tie receives the left sign; if h(u,v,w)=1 only the right occurrence remains and the intrinsic sign is the opposite. Both values occur: for any ordered triple of distinct block vertices, its boundary reversal has the complementary h-value, and each can be placed in positions a,a+1,a+2 with a fourth distinct vertex following.

Thus F has chambers labelled +e_r and -e_r, no inward witness in any chamber, and a fixed central gauge. It contains a label-zero point under affine/barycentric extension. Its only nontrivial Coxeter component is the full block B, of rank N-1, and some edge of that component changes the actual sign because the permutation graph is connected. The rank is unbounded.

This does not contradict a bound on the block coupling both determining windows: B meets only the left one. It shows that a large one-sided boundary block can be essential through intrinsic/tie transitions, even though its intersection with the protected corridor has order only three. Therefore 'all blocks other than the two-window coupling block are harmless product factors' requires an additional repair/transport argument; it is false if interpreted as sign-neutrality of the actual central-gauge label.

The example is a local protected balanced face, not a boundary tournament known to violate the grand two-cover conjecture. It also does not rule out collapsing B into a protected target carrier or choosing smaller zero carriers. Such choices need their own equivariance and compatibility proofs.
