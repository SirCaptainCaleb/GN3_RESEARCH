# Every compatibility run of length at least three is two-deep inside its anchor path

## Statement

Fix an anchor deletion cover F_d=P|Q in a minimum counterexample and the chosen deletion-cover compatibility graph. Let p_i,...,p_j be one consecutive compatibility-run component on P, indexed in the full displayed anchor order P=(p_0,...,p_m), and suppose j-i+1>=3. Then i>=2 and j<=m-2. More precisely, for every adjacent pair p_t,p_{t+1} in the run that has a run neighbor on at least one side, the compatible triangle F_d,F_{p_t},F_{p_{t+1}} has transitive precedence; hence its common insertion gap is two-deep on both sides of the surviving anchor order.

## Body

By 689b439cc429, a compatibility component inside the anchor neighborhood is exactly a consecutive run in the displayed anchor order. Thus for every t with i<=t<j, the covers
F_d, F_{p_t}, F_{p_{t+1}}
are pairwise compatible and form a compatible triangle.

Fix such a pair that has a run neighbor on at least one side. If p_{t+2} belongs to the run, then F_{p_{t+2}} is compatible with F_d and F_{p_{t+1}}, so it is an outside cover compatible with two states of the triangle. If instead p_{t-1} belongs to the run, then F_{p_{t-1}} is compatible with F_d and F_{p_t}, again giving an outside cover compatible with two triangle states.

The fourth-cover localization theorem in gapgeom01 says that a compatible triangle with cyclic precedence is compatibility-isolated: every outside deletion cover is compatible with at most one of its three states. Therefore our triangle cannot have cyclic precedence. Its precedence tournament is transitive.

For the labels {d,p_t,p_{t+1}}, delete the three labels from the anchor path P. The common insertion gap is exactly between p_{t-1} and p_{t+2}, with the evident endpoint interpretation. Hence the surviving common order has exactly t vertices on the left of the gap, namely p_0,...,p_{t-1}, and m-t-1 vertices on the right, namely p_{t+2},...,p_m.

The certified two-deep theorem for a transitive compatible triangle in gapgeom01 therefore gives
t>=2
and
m-t-1>=2.

Now apply this to the first adjacent pair p_i,p_{i+1}. Because the run has length at least three, p_{i+2} is a run neighbor, so i>=2.

Apply it to the last adjacent pair p_{j-1},p_j. Because p_{j-2} is a run neighbor, the same argument with t=j-1 gives
m-(j-1)-1 = m-j >=2,
so j<=m-2.

Thus every compatibility run of length at least three is separated from both anchor endpoints by at least two anchor positions. In particular any run containing p_1 or p_{m-1} has length at most two.

This is an arbitrary-order geometric restriction: the ambient paths may be arbitrarily long, and the conclusion comes from compatibility-gap structure rather than finite-size analysis.
