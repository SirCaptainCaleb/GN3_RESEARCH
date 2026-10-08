# Quadratic switch distance also terminates neighbor-replacement equality transport — preserved pre-item development

Extend the quadratic distance potential of root 86 to the neighbor-replacement equality events from root 81.

Fix a switch cut k and let E be threshold defect count. For each defective window rank r let d_k(r) be its nonnegative distance from the switch, and put Q_k=sum d_k(r)^2.

Consider a horizontal adjacent transposition that does not move the tracked middle coordinate b but replaces its immediate left neighbor:
(w,a,b,c) -> (a,w,b,c).
Assume the b-centered window lies strictly on one constant-color side of the switch and toggles from violating to satisfied.

The old b-centered window (a,b,c) and new b-centered window (w,b,c) occupy the same window rank r+1. The adjacent window (w,a,b), at rank r, is replaced by (a,w,b), whose color is the complement by alternation. Hence in the equality case described in root 81, the old adjacent window is satisfied and the new adjacent window is violating. Thus the defect set changes locally from
{r+1} to {r}.
On the pre-switch side r<r+1<=k, so
d_k(r)=d_k(r+1)+1.
Therefore Q_k strictly increases by
2 d_k(r+1)+1.
The right-side neighbor-replacement event is the reflected statement: equality moves the unique defect from rank r to r+1, again one step farther from the switch and strictly increases Q_k.

Consequently, at fixed cut k, every interior violation-to-satisfaction repair event now satisfies one common alternative:

1. E strictly decreases; or
2. E is unchanged and Q_k strictly increases.

This includes:
- the ordinary b-moving same-side bubble equality of root 86, where two defects move outward;
- the non-b neighbor-replacement equality of root 81, where one defect moves outward.

Hence the lexicographic potential (E,-Q_k) strictly decreases along every non-strict INTERIOR repair event of these two classes at fixed cut. Such events cannot cycle.

The remaining event types in arbitrary Tucker-cell extraction are genuinely different:
- vertical moves and some endpoint events may lower E directly;
- switch-crossing moves change k and should be measured by phase-compatible band progress;
- a global-endpoint equality event still requires its own audit because the replacement defect need not be farther from the old fixed cut.

Thus the arbitrary-cell extraction gap has narrowed to cut-changing and endpoint boundary events; interior same-side motion has a unified terminating potential.
