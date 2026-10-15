# Template-free star colorings and limits of matching induction

### A probabilistic obstruction to square-template induction

For d=2r, define an edge coloring of Q_d with one hub bit s and d-1 leaf bits x by f_hub(x,s)=b(x), f_leaf(x,s)=s. The interaction graph is a connected star. The nondecreasing favorable-root set is

A0 = {(0,x): all x} union {(1,x): b(x)=0 or b(complement x)=1}.

**Theorem.** In every even dimension d>=10 some such connected-star coloring has a favorable-root set containing no product of forbidden two-bit corners along any perfect matching of the directions.

*Proof.* Sample the values of b independently as fair bits. A template on 2r directions has r forbidden corners along a perfect matching. Choose one permitted value of the leaf bit paired with the hub, holding the hub bit at one. The other r-1 pairs each have three choices, producing 3^(r-1) leaf assignments. They all share one leaf bit, so no two are complements. For each assignment x the event that its hub-one root is unfavorable equals b(x)=1 and b(complement x)=0, of probability 1/4. These events are independent. Hence a fixed template is fully favorable with probability at most (3/4)^(3^(r-1)). There are (2r-1)!! times 4^r templates. The union bound is therefore (2r-1)!!*4^r*(3/4)^(3^(r-1)), which is below 0.000074 for r=5 and decreases thereafter. QED.

**Explicit small witness.** Already for d=6, setting b's 32-bit truth table to 0x23975ee9 gives the favorable-root mask 0xf7ff7fddfdd7f77d with 54 of 64 roots. Direct path enumeration confirms this mask. The ten unfavorable root indices are 1,7,11,19,21,25,33,37,47,59, with the hub as least significant bit. All 15 perfect matchings and 64 corner assignments for each were independently checked; none yields a template contained in the favorable set.

This theorem does not refute the chordless-cycle-specific template conjecture. It proves that template containment is not a valid general invariant for an induction that adds arbitrary tree branches, even when paired-root existence and cross-favorability are already guaranteed by the star theorem. An induction must carry a less rigid two-orientation relation.
