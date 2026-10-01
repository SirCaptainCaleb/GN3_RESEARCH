# Rank-band decomposition for the grand two-thirds conjecture

## Statement

Let H be a P_ell-free linear 3-graph with minimum degree delta>2ell/3 and global maximum path length L<=ell-1. To prove every edge special, it is enough to eliminate ascending nonspecial edges rank-by-rank. The existing machinery suggests three bands.

LOW BAND: q<=delta-1. Certified rotation expansion gives every fixed-entrance state degree at least 4(delta-q)-2. Thus the farther q lies below delta, the more violently its entrance-path state space branches. Any proof in this band should convert branching into either a terminal-label switch, a repeated blocker/cycle contradiction, or a longer path.

BOUNDARY BAND: q=delta. Every state still rotates, but local branching may collapse. Certified boundary normal forms show the only sink-like configurations are exact or almost exact blocker partitions of the entrance path, with only two or three exceptional single blockers. This is the natural finite-width transition layer.

TOP BAND: delta<q<=L. Since delta>2L/3 follows from delta>2ell/3 and L<=ell-1 only up to additive slack, in any putative sharp counterexample this band has width at most roughly L/3. Here entrance paths are long enough that terminal blocker systems become highly saturated. At q=L the punctured-Steiner analysis gives alternating matching systems, exact defect accounting, and low-deficiency strong-rainbow residual shadows. More generally the identity U_v-S_v=2(q-1? / path-relative analogue to be developed) should measure distance from saturation.

Additionally, whenever q<=(L+1)/2, the certified long-terminal-path capture lemma forces every longest L-path ending at either terminal to contain all three vertices of the rank-q edge. Thus the low half of the spectrum is globally visible to longest paths, whereas only ranks above L/2 can evade complete capture.

This yields a four-way proof agenda:
(A) q<=min(delta-1,(L+1)/2): combine high rotation degree with complete capture by longest terminal paths;
(B) (L+1)/2<q<=delta-1: use high fixed-entrance rotation degree without complete capture;
(C) q=delta: eliminate the exact saturated-fan boundary states;
(D) delta<q<=L: prove a stability theorem showing that small rotation defect forces a punctured-Steiner-like alternating-blocker/strong-rainbow residual structure, then eliminate it.

The missing global bridge is no longer 'propagate nonspeciality to maximum rank' in one jump. It is enough to prove that every nonspecial edge in one of these bands either contradicts the corresponding local structure or transfers to a nonspecial edge/state in a strictly higher band. 

## Body

This is a strategic recombination of certified facts rather than a new theorem. The low-band degree bound is 5fd4d3d30625. Boundary recurrence and no-sink behavior are 68593c300c9c and 29164b69be06. Complete capture below half the global rank is 16d45ad1b1b2. The top-rank saturated model is given by efe44a01f2dc, ffbd337476d6, ba1f1d706d77, 04196fff30ca, and ea7f4204e4b1. The rank-propagation fence 61e82a9b70f5 shows that unrestricted direct propagation to rank L is false, motivating monotone band-by-band transfer instead.