# Every globally minimal staircase profile yields order disagreement, strict descent, or a lower-state cross-component edge

## Statement

Let H be a minimum counterexample with a globally Phi-minimal staircase three-cover of component orders (c+2,c+1,c), c>=4. Then at least one of the following occurs: order disagreement; a spanning three-cover in the relevant pairwise-repartition component has strictly smaller quadratic potential Phi; or, when c>=5, in a lower state of a Hamiltonian-four-core two-label path-cover-two square, some two-cover contains an ordinary edge whose endpoints lie in two different components of the corresponding three-path cover.

## Body

If c=4, the profile is 6|5|4 and n=15. The certified theorem global_four_side_order15 applies directly to the globally Phi-minimal three-cover because it has a four-vertex component. It yields order disagreement.

If c>=5, then n=3c+3>=18. Apply staircase_large_disturbance01, which yields order disagreement, strict Phi descent in the relevant pairwise-repartition component, or a lower square state whose two-cover contains an ordinary edge with endpoints in two different components of the corresponding three-path cover.

These two cases cover all staircase profiles with c>=4.