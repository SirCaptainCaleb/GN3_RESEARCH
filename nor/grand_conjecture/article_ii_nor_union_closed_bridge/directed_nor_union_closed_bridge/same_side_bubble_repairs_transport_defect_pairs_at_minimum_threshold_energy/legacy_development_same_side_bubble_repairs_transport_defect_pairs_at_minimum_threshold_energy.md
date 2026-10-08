# Same-side bubble repairs transport defect pairs at minimum threshold energy — preserved pre-item development

## Development

## Same-side bubble toggles are nonincreasing for threshold defect count

Fix a ternary coordinate order and a switch cut. Let E be the number of ternary windows whose actual color disagrees with the threshold target prescribed by the cut.

Consider an adjacent swap on one side of the cut:
...,w,a,b,c,d,e,... -> ...,w,a,c,b,d,e,...
and suppose the b-centered violation predicate toggles from violating to satisfied while both centered windows lie on the same threshold side with target color eta.

Then
alpha(a,b,c)=1-eta
and
alpha(c,b,d)=eta.
By alternation,
alpha(b,c,d)=1-alpha(c,b,d)=1-eta,
and
alpha(a,c,b)=1-alpha(a,b,c)=eta.

Therefore before the swap the two central consecutive windows
(a,b,c), (b,c,d)
are both violations, while after the swap the two replacement central windows
(a,c,b), (c,b,d)
are both satisfied.

An adjacent swap affects only two additional outer windows:
(w,a,b) -> (w,a,c)
and
(c,d,e) -> (b,d,e).

Hence the central defect count drops by exactly two, while the two outer positions can create at most two new defects. Therefore
E(new) <= E(old).

Moreover equality holds if and only if both outer windows were satisfied before the swap and both become violations afterward. In that equality case the swap does not destroy defects; it transports the defect pair one step outward from the two central positions to the two outer positions.

The reverse satisfied-to-violating toggle has the reverse inequality.

### Consequence for extremal switch states

At a switch state minimizing E globally (or within a carrier on which no lower-E state is available), every violation-to-satisfaction same-side bubble toggle must be an equality move. Thus every such local repair is forced to export both defects outward.

This gives a concrete carrier-extraction dynamics:
- strict inequality improves the threshold state;
- equality is a deterministic defect-pair transport away from the repaired middle coordinate.

A closed minimal-defect carrier must therefore support repeated outward transport of defect pairs without allowing them to annihilate, cross into a favorable switch configuration, or reach a boundary where fewer than two replacement defects are possible.
