# Flat transfer triangles force all three entrances onto every rail

## Statement

Let e_1,e_2,e_3 be rank-q ascending nonspecial edges forming a flat terminal-transfer triangle: write e_i={x_i,v_{i-1},v_i} with indices modulo 3, and suppose each transfer e_i->e_{i+1} is of entrance-joint type. Let R_i be the associated (q-2)-edge entrance-to-entrance rail from x_i to x_{i+1} given by 932e2a9de86d. Then every rail R_i contains all three entrance vertices x_1,x_2,x_3.

## Body

Fix i and consider the next rail R_{i+1}, arising from the transfer e_{i+1}->e_{i+2}. The q-edge longest witness for e_{i+1} obtained by adjoining e_{i+1} to its canonical entrance precursor has R_{i+1} as its final q-2 precursor edges. By the one-edge blocker-memory lemma 6ff5b5590ee3 applied to the preceding flat transfer e_i->e_{i+1}, R_{i+1} contains either the entrance x_i of e_i or the other terminal v_{i-1} of e_i. But in a 3-cycle v_{i-1}=v_{i+2}. The rail R_{i+1} avoids both terminal pairs of e_{i+1} and e_{i+2}, hence in particular avoids v_{i+2}=v_{i-1}. Therefore R_{i+1} must contain x_i. By construction its two last vertices are x_{i+1} and x_{i+2}. Thus it contains all three entrances. Cyclically this holds for every rail.