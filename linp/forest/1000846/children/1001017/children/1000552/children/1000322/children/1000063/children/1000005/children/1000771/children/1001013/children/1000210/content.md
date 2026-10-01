# Three affine endpoint paths do not survive arbitrary matching deletions

## Statement

The three affine-stabilizer spanning paths used to prove specialness of A_0={0,1,4} in the full cyclic STS(13) are not robust enough by themselves to prove specialness under matching deletions: the disjoint blocks A_6 and A_11 hit all three.

## Body

Write A_i={i,i+1,i+4} modulo 13. The base spanning path ending at A_0 has nonterminal edge set
S_0={A_1,A_2,A_6,A_7,A_8}.
The affine stabilizer f(x)=3x+1 sends A_i to A_{3i}. Applying f and f^2 gives the other two spanning paths ending at A_0, with nonterminal edge sets
S_1={A_3,A_5,A_6,A_8,A_11},
S_2={A_2,A_5,A_7,A_9,A_11}.

Now
A_6={6,7,10}
and
A_11={11,12,2}
are disjoint, so {A_6,A_11} is a matching. But A_6 meets S_0 and S_1, while A_11 meets S_1 and S_2. Thus deleting this two-block matching destroys all three symmetry-generated A_0-ending spanning paths at once.

This does not refute robust specialness: other spanning paths may survive, and the computational evidence says they do. It only shows that the full-design three-path affine-stabilizer proof cannot be transferred verbatim to arbitrary matching deletions. Any human proof of 09b3a90c50a9 needs a larger endpoint-path family or a different structural argument.