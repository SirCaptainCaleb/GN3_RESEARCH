# A saturated nested collision chain packs linearly many edge-disjoint linear cycles

## Statement

Under the hypotheses of 65825e12de66, let
I_1 strictly contain I_2 strictly contain ... strictly contain I_m
be a saturated nested chain of backward collision intervals.

Then the hypergraph contains at least
ceil((m-1)/2)
pairwise edge-disjoint linear cycles, each consisting entirely of ascending nonspecial edges and each having length at least three.

## Body

For every level a=1,...,m-1, use 65825e12de66 to choose one witness cycle C_a.

If level a is of shortcut type S_a, then C_a uses exactly the left annulus edges
E_{j_a+1},...,E_{j_{a+1}},
the bridge edge E_{i_{a+1}},
and the right annulus edges
E_{i_{a+1}+1},...,E_{i_a}.

If level a is of flank type F_a, choose the primitive cycle guaranteed there. Its edge set lies entirely in one of the two annuli
{E_{j_a+1},...,E_{j_{a+1}}}
or
{E_{i_{a+1}+1},...,E_{i_a}}.

Therefore in either case C_a is supported inside the level-a annuli together with, possibly, the single inner-boundary edge E_{i_{a+1}}.

For levels a and b with |a-b|>=2, these supports are disjoint. Indeed the left annuli for different levels are disjoint, the right annuli for different levels are disjoint, all left annuli precede all right annuli, and the only extra bridge edge for level a is E_{i_{a+1}}, which can belong only to the immediately adjacent level-(a+1) support.

Hence the witness cycles from all odd levels are pairwise edge-disjoint, and the same is true for all even levels. One parity class has at least ceil((m-1)/2) levels. Choosing that class proves the claim. Each witness cycle has length at least three and consists of ascending nonspecial edges by construction.