# Arbitrary complementary Tucker cells still contain a controlled local repair event — preserved pre-item development

## Composition

(none yet)

## Development

The same-deleted-order hypothesis from the cellular bubble audit is sufficient for the old b-only path argument, but it is not necessary for local extraction. Along an arbitrary product-cell edge, every possible first disappearance of a selected b-centered violation has a controlled local repair law.

Consider a product-cell 1-skeleton path beginning at a state carrying +b and ending at a state carrying -b. Track the unique ternary window centered at b whenever b is not at a global endpoint. Stop at the first edge on which either the b-centered violation disappears or its side relative to the switch changes while remaining a violation.

There are five edge types.

1. Vertical cut edge.
The coordinate order and actual window colors are unchanged and only one threshold target bit flips. If that bit is the b-centered violating window, it becomes satisfied. Thus threshold defect count E drops by exactly one.

2. Horizontal edge moving b on one constant-color side.
This is the valid same-side bubble event already analyzed in roots 143-144. In the violation-to-satisfaction direction the two central defects disappear. Either E strictly drops or equality transports the defect pair to the two outer affected windows.

3. Horizontal edge moving b across the switch.
Write the old local order as (a,b,c,d), with the old b-centered pre-switch window (a,b,c) violating target eta, so alpha(a,b,c)=1-eta. After swapping b,c, the new b-centered post-switch window is (c,b,d).
If it remains violating, alpha(c,b,d)=eta and alternation gives alpha(a,c,b)=eta; moving the cut one level then makes both central windows matched, exactly as in the phase-compatible transport theorem.
If instead the new b-window is satisfied, alpha(c,b,d)=1-eta while alternation still gives alpha(a,c,b)=eta. Then the two central windows already equal the two threshold colors eta,1-eta with the cut unchanged. Thus either subcase is a legal switch-crossing repair.

4. Horizontal edge not moving b but changing one immediate neighbor.
All swaps farther from b leave its centered window unchanged. Up to reversal the only new event is
(w,a,b,c) -> (a,w,b,c).
The b-centered window changes from (a,b,c) to (w,b,c). Suppose it toggles from violating to satisfied for its fixed target eta:
alpha(a,b,c)=1-eta and alpha(w,b,c)=eta.
The adjacent old window (w,a,b) is replaced by (a,w,b), whose color is its complement by alternation. Therefore its defect status toggles as well. If it was violating, both defects disappear and E drops by two. If it was satisfied, the old b-defect is replaced by one defect at the adjacent outer rank and E is unchanged. Thus a neighbor-replacement disappearance is again strict improvement or one-slot defect transport. The right-neighbor case is symmetric.

5. Horizontal edge moving b to a global endpoint.
The old centered b-window is a defect and disappears. An adjacent transposition can change at most one additional surviving ternary window besides the flipped old centered window. Hence at worst one new defect replaces the lost centered defect; E cannot increase. Equality is again a one-step endpoint transport.

Therefore every complementary signed-middle product cell contains a path event yielding one of:
- a phase-compatible switch-crossing repair;
- strict decrease of threshold defect count;
- an equality transport of defects to neighboring outer windows.

This repairs the local-extraction scope of roots 143,150,154 after audit 174. What remains global is termination of the equality transports, not existence of a legal local repair event. The existing threshold-band and defect-moment potentials may be applied only after checking that the particular equality event lies in their stated class; neighbor-replacement and endpoint transports are additional classes and should not be silently identified with the old two-central-window bubble packet.
