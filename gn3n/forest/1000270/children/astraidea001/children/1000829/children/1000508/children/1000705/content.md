# Neutral support corridors alternate compatibility with forced distance-two support switches

## Statement

Let H be in the sharp half-order shell and let S_0-S_1-S_2-S_3 be a simple three-edge path in a selected deletion-support transversal, with distinct edge labels x_0,x_1,x_2. Let F_i=S_i|S_{i+1} be the selected deletion cover of H-x_i. If the two length-two walks S_0-S_1-S_2 and S_1-S_2-S_3 both take the rigid same-end alternative of astra004twowalk, then F_0 is compatible with F_1 and F_1 is compatible with F_2, whereas F_0 and F_2 are support-incompatible on H-{x_0,x_2}. More precisely, the surviving middle label x_1 lies in opposite support classes in F_0 and F_2, while every other surviving vertex retains the natural parity class.

## Body

The rigid alternative of astra004twowalk applied to S_0-S_1-S_2 gives compatibility of F_0 and F_1 on H-{x_0,x_1}; applying it to S_1-S_2-S_3 gives compatibility of F_1 and F_2 on H-{x_1,x_2}.

For the nonconsecutive pair, odd-graph complementation along the first two edges gives
S_2=(S_0-{x_1}) union {x_0}.
Along the next edge, since x_2 is its omitted label and x_1 is the label acquired on the preceding step,
S_3=(S_1-{x_2}) union {x_1}.

Now restrict F_0=S_0|S_1 to H-{x_0,x_2}. Because x_2 lies in S_1, its two support classes are
S_0
and
S_1-{x_2}.
The vertex x_1 lies in S_0.

Restrict F_2=S_2|S_3 to H-{x_0,x_2}. Because x_0 lies in S_2, its classes are
S_2-{x_0}=S_0-{x_1}
and
S_3=(S_1-{x_2}) union {x_1}.
Thus x_1 lies in the class corresponding to S_1-{x_2}, opposite to its class in F_0, while the remaining vertices of S_0-{x_1} and S_1-{x_2} retain their respective classes.

Hence the two restricted unordered support partitions differ, so F_0 and F_2 are support-incompatible. ∎
