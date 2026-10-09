# Opposite-color same-root hub diamonds are automatically two-end-maximal monochromatic paths

# Exact two-ended maximality of every local opposite-color root diamond in the NO-SHARED-EDGE case

Let n>=6 and c be an ACTIVE NORI binary ordered-3-face coloring for which NO physical edge receives monochromatic center-square certificates of both colors (case B of the certified-square edge-shadow dichotomy). The bichromatic-hub theorem guarantees at least one hub z with two nonempty disjoint certified edge-direction color classes A (color 0) and B (color1), each with at least two directions.

The proved **mixed-class middle selector identity** from nori_bichromatic_hub_shadow_mixed_triple_middle_selector_rigidity_20261008 states that for every physical ordered 3-face through z with ordered free directions (u,v,w), whenever v lies in A or B and at least one of its adjacent directions lies in the OPPOSITE class, its color is exactly the color class of v. This is independent of the status/class of the third direction.

Choose distinct a,b∈A, c,d∈B, x=z xor {a,c}, y=z xor {b,d}. As in nori_bichromatic_hub_same_root_reverse_tail_opposite_color_diamond_20261008 there are genuine two-colored same-root same-endpoint length-four mono paths:
  P0=(c,a,b,d), color 0;
  P1=(a,c,d,b), color 1.

**THEOREM (the naive diamond extension route is maximally blocked).** For EVERY fresh direction e∉{a,b,c,d}, ALL FOUR length-five geodesic extensions
  e+P0, P0+e, e+P1, P1+e
are NONMONOCHROMATIC. In each case the only newly added ordered-three-face window has color exactly the COMPLEMENT of that path's original monochromatic color.

**Proof.** The same-physical-face extension lemma nori_opposite_color_four_diamond_same_physical_face_extension_blockers_20261008 gives the new append-window colors
  A_e=c(F(y;{b,d,e}),(b,d,e)),
  B_e=c(F(y;{b,d,e}),(d,b,e)),
and new prepend-window colors
  C_e=c(F(x;{a,c,e}),(e,c,a)),
  D_e=c(F(x;{a,c,e}),(e,a,c)).
Here F(y;{b,d,e})=F(z;{b,d,e}) because y differs from z ONLY in b,d, both free coordinates; similarly F(x;{a,c,e})=F(z;{a,c,e}) because x differs from z only in free a,c. Hence all FOUR colors can be computed via the SAME-HUB mixed-class selector:
   A_e=1  (middle d∈B, first b∈A),
   B_e=0  (middle b∈A, first d∈B),
   C_e=1  (middle c∈B, third a∈A),
   D_e=0  (middle a∈A, third c∈B).
P0 has color0 so both append and prepend add color1. P1 has color1 so both add color0. Thus all four extensions are one-switch paths, and none remains monochromatic. QED.

**Interpretation (very important).** The opposite-color diamond at a bichromatic hub is NOT a facile seed for MONOCHROMATIC growth: in the no-common-edge regime, it is forced to be TWO-ENDED MAXIMAL for all unused coordinates. This obstruction is automatically realized by the very local structure that supplies the diamond, not an accidental adversarial choice.

There is still a valuable positive effect: all four length-five extensions are genuine full ONE-SWITCH paths, simultaneously rooted/ended at closely related vertices; when n=5 they would themselves be grand witnesses, but the two-class diamond requires n>=6. In larger dimensions, arbitrary further extensions may introduce additional switches, and the theorem provides no global closure.

**Research priority.** Any attempt to use opposite-color rank-two diamonds for NORI must avoid naive endpoint extension of a monochromatic witness. Investigate (i) INSERTION of unused directions into its INTERIOR, changing its physical center and preserving a one-switch word, (ii) root-preserving middle-pair exchanges between distinct hub diamonds, (iii) coordinate-complement support transport through a nontrivial equivariant carrier. The blocked endpoint-extension strategy cannot prove full NORI closure.
