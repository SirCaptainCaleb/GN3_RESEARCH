# Fixed insertion fibers force either a protected root descent or one pure-sign jump edge

## Composition

(none yet)

## Development


Let h be reversal-odd on ordered r-tuples and let O=(v_1,...,v_m) be a one-change deletion order in a minimum coordinate counterexample, with word 0^p1^q and omitted coordinate x.

For each gap j=0,...,m, let F_j be the full order obtained by inserting x into that gap while keeping the relative order of every v_i fixed. Give F_j the natural threshold target inherited from O: every untouched old 0-window keeps target 0, every untouched old 1-window keeps target 1, and the cut is shifted only by the change in rank caused by the insertion.

All target mismatches of F_j lie in the bounded packet of windows meeting x.

Call a mismatch positive if its target is 0 and its actual color is 1, and negative if its target is 1 and its actual color is 0.

At the left endpoint F_0, the only new endpoint window precedes the old 0-run. If it had color 0, F_0 would be one-change; counterexamplehood therefore forces it to have color 1. Thus F_0 has a positive defect and no negative defect.

Dually, at the right endpoint F_m, the only new endpoint window follows the old 1-run. Counterexamplehood forces it to have color 0. Thus F_m has a negative defect and no positive defect.

Suppose some intermediate F_j has both a positive and a negative defect. Every positive defect occurs on or before the threshold cut, while every negative defect occurs after the cut. Choose the rightmost positive defect and the leftmost negative defect. The corresponding actual bits are 1 and 0, respectively. Hence between them the actual local packet contains an adjacent 10 descent.

Because every mismatch lies in the x-packet, this 10 descent is a protected local descent inside one fixed-deleted-order fiber. It supplies the nonzero root certificate of the protected-bridge program without any permutation-face connectivity assumption.

Therefore, if no fixed-fiber state exposes such a root descent, the defect signs along the insertion fiber are pure: each F_j has defects of only one sign. Since the left endpoint is positive and the right endpoint negative, there exists an adjacent pair F_j,F_{j+1} such that F_j has only positive defects and F_{j+1} has only negative defects.

Thus every fixed insertion fiber satisfies the dichotomy:

1. some state contains a protected 10 root descent; or
2. one adjacent swap of x across a single old coordinate changes the entire local obstruction from pure positive phase to pure negative phase.

The second case is a one-dimensional pure-sign jump edge. It is the exact remaining fixed-fiber carrier-extraction problem. In ternary arity it should be compared directly with the complementary signed-middle switch-transport packet, now with the crucial advantage that the order of every coordinate other than x is fixed by construction.
