# Opposite signed-middle carriers contain a legal bubble repair edge — preserved pre-item development

## Development

## Bubble extraction from a cellular Tucker carrier

Consider a ternary switch-prism product cell containing two genuine state vertices labeled +b and -b by the signed-middle rule. Fix the cut level for the moment; the same argument applies inside a horizontal slice of a minimal product carrier.

The +b state has a selected violating window centered at the physical coordinate b on the pre-switch side. The -b state has a selected violating window centered at the same b on the post-switch side.

Inside the permutohedron face, connect the two endpoint permutations by a path that moves b monotonically by adjacent swaps, while keeping the relative order of all other coordinates fixed. This is the usual bubble path and remains in the same Coxeter face.

At each vertex of the path, whenever b is not at an endpoint position, let nu be the indicator that the unique ternary window centered at b violates the target color prescribed by the cut.

Initially nu=1 and finally nu=1.

### Dichotomy

If nu remains 1 when b crosses from the pre-switch side to the post-switch side, then the crossing edge has b-centered violations on both sides of the cut. This is exactly the signed-middle complementary-edge situation of subsection 118, hence the adjacent swap is a genuine switch-crossing endpoint repair.

Otherwise nu changes value somewhere away from the cut. Consider a same-side adjacent swap
...,a,b,c,d,...  ->  ...,a,c,b,d,...
across which nu toggles. Since both b-centered windows are on the same side of the cut, their target color is the same, say eta.

If the old centered window is violating and the new one is satisfied, then
alpha(a,b,c)=1-eta,
alpha(c,b,d)=eta.
Alternation gives
alpha(a,c,b)=eta.
Hence after the swap the two central consecutive windows are both eta:
alpha(a,c,b)=alpha(c,b,d)=eta.

The reverse toggle is symmetric: if the old window is satisfied and the new one violating, then both new central windows equal 1-eta.

Thus every same-side toggle edge produces a genuine two-window monochromatic repair packet.

### Consequence

Every cellular Tucker carrier containing opposite signed-middle labels yields an actual legal adjacent-transposition edge of one of two concrete types:
1. a switch-crossing endpoint repair;
2. a same-side toggle whose two new central windows agree with each other, and in the violation-to-satisfaction direction agree with the local threshold color.

No artificial triangulation diagonal is needed.

The remaining extraction problem has been reduced to the two outer windows affected by a same-side toggle. If those outer windows do not create new threshold defects, the swap strictly improves the switch state. If they do, their locations are one step farther from the centered coordinate and should be amenable to an extremal-distance or Radon-certificate argument.
