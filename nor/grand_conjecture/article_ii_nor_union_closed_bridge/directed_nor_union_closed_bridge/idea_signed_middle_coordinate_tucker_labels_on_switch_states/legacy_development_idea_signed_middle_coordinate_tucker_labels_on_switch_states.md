# Idea: signed middle-coordinate Tucker labels on switch states — preserved pre-item development

## Composition

(none yet)

## Development

## Signed middle-coordinate Tucker label for ternary switch states

Idea / research direction, not yet a theorem.

In ternary arity, consider a completed coordinate order pi together with a proposed switch cut k. Relative to that cut, prescribe one color before the cut and the opposite color after it. Under counterexamplehood every switch state has at least one violating triple.

Choose a violating triple nearest the cut. If several tie, use a reversal-compatible deterministic rule on the full ordered triple rather than only its support. Let b be the middle coordinate of the selected violating triple. Attach a sign according to whether the violation lies on the pre-switch side or the post-switch side:
lambda(pi,k)=+b or -b.

Why this is attractive:
- reversing the coordinate order keeps the physical middle coordinate b fixed;
- reversal sends the cut to the complementary cut and interchanges pre/post sides;
- therefore lambda(rev(pi),m-k)=-lambda(pi,k).

So the label has exactly the antipodal form required by Tucker/Ky Fan: signed coordinate labels ±v, rather than type-A roots.

This avoids the tautological A_2 root circulation
(e_a-e_c)+(e_c-e_b)+(e_b-e_a)=0,
which can occur on a braid hexagon without giving a NOR repair.

Potential geometry: use either the separator-symbol Coxeter complex or the two-layer memory-state flag prism, refined enough that nearest-violation labels have controlled behavior on cells. A Tucker complementary edge would then be two adjacent switch states labeled +b and -b. Such a pair says that the same physical coordinate b is the middle of nearest violations on opposite sides of the proposed switch.

This is potentially powerful because an adjacent chamber move changes only a bounded packet of windows. If the same middle coordinate b becomes the nearest violation on opposite sides across one elementary move, then the two local ordered triples overlap heavily. The hoped-for local conclusion is one of:
1. the switch can be moved through b, producing a legal one-change state;
2. the adjacent move exposes a shifted two-circuit / protected-front wedge;
3. the corresponding rank-two Coxeter residue contains the centered directed-triangle or tetrahedral-curvature obstruction already classified elsewhere in Article II.

A Ky Fan version may be even more natural than plain Tucker: an alternating simplex of signed labels could encode a chain of violations crossing the switch, and the sign alternation would correspond directly to repeated attempted switch transport.

What is still missing:
- a precise triangulation on which the label is simplicial/admissible;
- verification that boundary labels satisfy the chosen Tucker/Ky Fan hypothesis;
- a local theorem translating the forced complementary edge or alternating simplex into an actual NOR repair.

This should be treated as a serious candidate labeling, not as an established reduction.
