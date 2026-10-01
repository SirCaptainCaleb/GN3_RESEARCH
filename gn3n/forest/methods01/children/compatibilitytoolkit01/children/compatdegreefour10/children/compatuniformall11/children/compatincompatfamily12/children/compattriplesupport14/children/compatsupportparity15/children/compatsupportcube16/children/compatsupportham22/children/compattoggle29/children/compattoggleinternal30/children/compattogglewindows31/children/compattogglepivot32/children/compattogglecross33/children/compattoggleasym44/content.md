# Asymmetric one-split pivots force order disagreement or reversed endpoint four-paths on both cores

## Statement

In the interior-pivot branch of compattogglecross33, let A=(u_0,...,u_m), B=(v_0,...,v_s), with omitted label c and second-type pivots at u_i|u_{i+1}, v_j|v_{j+1}. If exactly one of the two forward central cross-joins (u_i,c,v_{j+1}) and (v_j,c,u_{i+1}) is tight, then either A or B admits a second Hamilton order and hence an explicit relative-order-disagreement witness, or both reversed endpoint four-paths (u_1,u_0,u_m,u_{m-1}) and (v_1,v_0,v_s,v_{s-1}) are tight.

## Body

# Proof

This is the certified asymmetric interior pivot theorem f31a8c6d920e applied to the deletion cover

H-c=A|B

identified in compattogglecross33.

All hypotheses match: c has second-type insertion obstructions at interior gaps of both displayed components, and the present assumption says exactly one of the two forward central cross-joins is tight.

Therefore f31a8c6d920e gives exactly the stated dichotomy: either one component has a Hamilton order different from its displayed order, yielding the standard ordered-path disagreement witness, or both endpoint-pair reversing four-paths are tight simultaneously.
