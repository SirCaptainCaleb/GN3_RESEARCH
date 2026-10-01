# The four transposition alignments reduce to repeated-pair versus split-pair local kernels

## Statement

In the two-core transposition residue of compatswapgeom28, on each core the third label z shares one of the two occupied adjacent gaps with exactly one of x,y. If z follows x on both cores, then the pair {x,z} shares a gap on both cores; if z follows y on both, {y,z} does. If z follows x on one core and y on the other, then {x,z} shares a gap on one core and {y,z} on the other. At any core where the shared gap is internal, the two labels together with the two consecutive core vertices bordering that gap form a Hamiltonian four-set. If the shared gap is an endpoint gap, the two labels are common extenders of that endpoint of the common core order.

## Body

Fix one core K with common Hamilton order L. Two special labels u,v that use the same insertion gap each give a Hamilton path obtained by inserting that label into L. If the shared gap is internal between consecutive core vertices r_i,r_{i+1}, then both triples (r_i,u,r_{i+1}) and (r_i,v,r_{i+1}) are tight. The certified two-parallel-middle local extension lemma yields a Hamiltonian tight path on {r_i,r_{i+1},u,v}. If the shared gap is an endpoint gap, the two chosen Hamilton paths simply show that u and v both extend the same endpoint of L; no four-set Hamiltonicity is claimed. Now apply this observation to the four z-alignment types from compatswapgeom28. In the two same-label-tracking cases the same pair shares a gap on both cores; in the two crossed-tracking cases the repeated pairs differ between the cores. Thus the four bookkeeping cases collapse to two structural classes.
