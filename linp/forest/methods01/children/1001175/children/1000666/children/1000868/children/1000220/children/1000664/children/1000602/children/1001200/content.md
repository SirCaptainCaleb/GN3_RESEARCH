# Lens-free flat cycles have late aligned rails and no distance-two intersections

## Statement

Let R_i be the equal-length maximum entrance rails in a lens-free flat gap-one terminal cycle.

If three such rails are pairwise uniquely intersecting, their three pairwise intersections coincide at one common aligned joint. Consequently the cyclic rail system has only two possible global forms: either every adjacent rail joint lies at level at least ceil((p-2)/2), or all rails share one common early aligned joint. The common-early-joint alternative is impossible in the flat terminal cycle, so every adjacent rail joint lies in the late half.

Moreover every distance-two pair R_i,R_{i+2} is vertex-disjoint. If V(R_i)∩V(R_{i+3})={t_{i+2}} has aligned level h_i, then ceil((p-2)/2)<=h_i<=p-4. In particular a lens-free flat terminal cycle cannot have length five.

## Body

Pairwise unique intersections of equal-length maximum endpoint paths are aligned joints. For three rails A,B,C, the unique pairwise intersections must coincide, giving a common aligned joint.

Applying the three-rail half-gate argument around the cycle yields the late-or-common-hub dichotomy. The flat-cycle distance-three terminal intersection theorem identifies R_i∩R_{i+3} with t_{i+2}; a common early hub would therefore force consecutive terminal vertices of a cycle edge to coincide, impossible. Thus all adjacent joints are late.

If R_{i+1} met R_{i+3}, then in the lens-free state that intersection is unique. Together with the known unique intersections of R_i with R_{i+1} and R_{i+3}, the three-path common-joint conclusion would force two distinct prescribed vertices on R_i to coincide. Hence distance-two rails are disjoint. The three-rail half-gate lemma then forces the prescribed distance-three joint into the late half, while terminal-blocker geometry gives h_i<=p-4. For a 5-cycle, distance three is also distance two in reverse cyclic order, contradiction.