# Defect-stability route to the two-thirds Turan upper bound

## Statement

For a globally longest L-edge path P ending in a maximum-rank nonspecial edge e={x,y,z}, terminal blocker defects measure exactly the deviation from the saturated punctured-Steiner regime: for each terminal v in {y,z},
U_v-S_v=2(L-d_H(v)),
where S_v is the number of single blockers and U_v the number of precursor vertices unused by the v-star. Consequently, in a minimum-degree-delta graph,
U_v-S_v<=2(L-delta).
This suggests a general 2/3 strategy: a nonspecial edge above the threshold 3delta>2L+2 must lie either in a rotation-rich regime with many open blocker defects, or in a near-saturated regime close to the punctured-Steiner one/two-chain topology.

## Body

The identity is immediate from the certified local terminal-defect formula of 437f531f4ad8:
2d_H(v)=2L+S_v-U_v.
Rearranging gives
U_v-S_v=2(L-d_H(v)).
Thus minimum degree delta gives
U_v-S_v<=2(L-delta)
at both terminals.

This is the exact quantitative generalization of the punctured-Steiner equality U_v=S_v, which occurs when d_H(v)=L.

The significance for the Turan problem is structural rather than merely numerical.

Let p be the number of open alternating components in the union of the two terminal double-blocker matchings. The same certified accounting gives
S_y+S_z+U_y+U_z=2p.
Hence open components are exactly the terminal defect budget.

There are then two natural regimes.

ROTATION-RICH REGIME.
If p or the single-blocker count is large, there are many open-chain endpoints/single-blocker handles. Certified single-blocker and opposite-terminal splice lemmas turn such defects into length-preserving rotations unless they satisfy highly constrained joint/triangle patterns. Iterating these rotations should expose many opposite endpoints. The appropriate global target is the fixed-edge rotation-closure statement 9125faa547ae: some endpoint in the closure should have degree at most floor(2(L+1)/3). Such a witness immediately yields
3delta<=2L+2.

NEAR-SATURATED REGIME.
If p is small, the double-blocker union is mostly alternating cycles. The punctured-Steiner analysis shows the extreme p=1,2 case: exact regular saturation compresses the obstruction to one open chain, or two open chains plus a terminal triangle. The deficiency-s decomposition 04196fff30ca shows that near pair-saturation is measured by the uncovered-pair graph, while the strong-rainbow shadow formulation ea7f4204e4b1 converts residual path avoidance into a near-Hamilton strongly-rainbow path problem in an almost-complete graph. Thus the small-p regime should admit a stability theorem: a dense nonspecial obstruction with few rotation defects must be close to a punctured-Steiner/low-deficiency configuration, where the structural uncrossing argument can take over.

Therefore a plausible proof architecture for the sharp 2/3 Turan coefficient is:

1. Peel to a core of minimum degree delta>2ell/3.
2. Assume a nonspecial edge and propagate, if necessary, to a maximum-rank nonspecial state or an equivalent fixed-edge rotation state.
3. Build the two-terminal alternating blocker system on a longest path.
4. If the defect count is large, use rotation expansion to force a low-degree endpoint or a longer path.
5. If the defect count is small, use deficiency/shadow stability to reduce to the punctured-Steiner-like saturated topology and eliminate it structurally.
6. Hence the core is all-special; the certified peeling theorem then gives ex_L(n,P_ell^(3))<=floor(2ell/3)n.

The finite n<=12 proof should therefore be viewed as the zero-/one-deficiency endpoint of a general stability argument, not as an isolated exact computation.
