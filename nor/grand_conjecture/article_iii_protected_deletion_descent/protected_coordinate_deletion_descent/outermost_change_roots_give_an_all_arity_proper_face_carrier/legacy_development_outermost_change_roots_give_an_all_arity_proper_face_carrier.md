# Outermost-change roots give an all-arity proper-face carrier — preserved pre-item development

## Development

Combination of Article I's all-arity two-change reduction and Article III root §243.

Let h be reversal-odd on ordered r-tuples, r≥2. For a full coordinate order π=(v_1,...,v_n), write its window word as c_1...c_L, L=n−r+1. If this word has at least two changes, let p<q be the first and last change indices, and define D_r(π)=e_{v_p}−e_{v_{q+r}}. Set D_r(π)=0 on NOR-good orders.

The endpoints are distinct, so D_r(π)=0 exactly on good orders. Reversal reflects change index i to L−i and complements the word. Consequently D_r(π^rev)=−D_r(π). Color complementation preserves D_r. Every nonzero root spans q−p+r+1≥r+2 consecutive coordinates. In a minimum counterexample the existing endpoint theorem supplies a full witness with exactly two changes, and this descriptor spans that entire two-change region.

Proper-face theorem. Let F=B_1|...|B_s be a proper ordered partition and choose a good order g(B_i) on each proper block, using minimum-counterexamplehood. Concatenate them to π_F. If π_F is bad, the two endpoints of D_r(π_F) occupy distinct ordered blocks: were both in one block, the interval from v_p to v_{q+r} would be inside that block and would contain both changes, contrary to goodness of g(B_i). A block-rank functional φ_F, strictly increasing across the blocks, therefore satisfies φ_F(D_r(π_F))<0.

If a chamber refines F, every root D_r from that chamber is weakly forward under the same functional, since its source precedes its target in the chamber. Thus on a flag F_0<...<F_t, with F_0 the coarsest ordered partition, the label at F_0 is strictly negative and all other labels weakly negative under φ_F0. Every convex combination with positive F_0 weight avoids zero. Applying the same argument to the first active vertex handles all faces of the flag simplex. Hence the barycentric proper-face carrier is zero-free in every arity.

This proves the all-arity boundary certificate underlying the ternary construction without assuming a coherent repair graph. Its labels are outermost-change roots, distinct from individual window-slide roots and omitted-coordinate exchange roots. Any degree extension or extraction theorem must use the corresponding witness provenance.
