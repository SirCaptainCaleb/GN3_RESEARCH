# Arbitrary flat blocking scans admit a replacement on one side of the switch — preserved pre-item development

Consolidated from Article II §205. This repairs the use of scan uniqueness, while keeping the remaining termination obligation explicit.

Let alpha be alternating with zero tetrahedral coboundary. Let O=(v_1,...,v_m) have word 0^p1^q with p,q>=3, and let an exterior coordinate x block all insertions. Set s_i=alpha(x,v_i,v_{i+1}).

Insert x after v_p. Its new packet (s_{p-1},1-s_p,s_{p+1}) lies between an unchanged zero prefix and one suffix. It must be nonmonotone. For binary a,b,c, the packet (a,1-b,c) is nonmonotone precisely when a>=b>=c: the four scan triples are 000,100,110,111. Thus s_{p-1}>=s_p>=s_{p+1}. Inserting after v_{p+2} similarly gives s_{p+1}>=s_{p+2}>=s_{p+3}. The five-bit scan core is nonincreasing; no assertion about the whole scan is required.

For replacement at coordinate j, flatness gives the packet
B_j=(s_{j-2},1 xor s_{j-1} xor s_j xor w_{j-1},s_{j+1}),
where w is the old carrier word.

If s_{p+1}=1, the core forces s_{p-1}=s_p=1. Replacing v_p by x gives B_p=(s_{p-2},1,1), hence a good deletion order with phases (p-d,q+d), d=3-s_{p-2} in {2,3}.

If s_{p+1}=0, the core forces s_{p+2}=s_{p+3}=0. Replacing v_{p+3} by x gives B_{p+3}=(0,0,s_{p+4}), hence phases (p+d,q-d), d=3-s_{p+4} in {2,3}.

A zero remaining phase is a monochromatic deletion witness and immediately extends to a good full order. Thus every blocking scan with p,q>=3 admits a protected good replacement on one side.

At a globally minimum first-phase witness satisfying p>=3, the left branch is impossible, so the right branch is forced. If its resulting carrier still satisfies the phase-length hypotheses, the subsequent left replacement has an explicitly changed omitted coordinate. The distance-three return restores the original deletion order; distance-two same-profile returns exchange a local triple. These are possible recurrence patterns, not a termination proof. Cases with a phase of length two still require treatment, and an exact backtrack is not an escape from the obstruction.

This theorem replaces the special-scan premise for LOCAL existence of good replacements. It does not validate the earlier unconditional flat closure, nor establish that the resulting dynamics must terminate.
