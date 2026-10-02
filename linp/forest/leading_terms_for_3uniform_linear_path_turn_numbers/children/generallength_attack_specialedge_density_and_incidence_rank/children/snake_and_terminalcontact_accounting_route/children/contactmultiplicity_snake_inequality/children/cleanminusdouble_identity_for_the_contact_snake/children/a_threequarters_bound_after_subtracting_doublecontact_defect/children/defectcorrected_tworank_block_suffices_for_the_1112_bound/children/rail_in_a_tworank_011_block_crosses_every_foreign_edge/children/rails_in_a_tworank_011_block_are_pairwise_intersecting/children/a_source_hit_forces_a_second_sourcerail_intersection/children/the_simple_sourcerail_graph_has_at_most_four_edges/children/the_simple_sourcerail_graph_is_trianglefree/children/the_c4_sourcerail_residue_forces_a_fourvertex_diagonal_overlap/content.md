# The C4 source-rail residue forces a four-vertex diagonal overlap

## Statement

Assume the simple source-rail graph of a four-edge source-clean 0-1-1 consecutive-rank block is the 4-cycle 01,12,23,30, so the diagonal pairs are 02 and 13. Then one of the two diagonal pairs has source-only foreign contacts in both directions. Consequently that diagonal pair shares at least four distinct distinguished vertices: the two source endpoints of its own edges and the opposite terminals of the other two edges.

## Body

Write e_i={x_i,v,u_i}, with Q_i the chosen maximum source path ending at x_i. Because every cycle pair is simple, the reciprocal-terminal rule implies that along each cycle edge ij the foreign contacts are terminal-only: Q_i meets e_j at u_j and Q_j meets e_i at u_i. Hence Q_0 and Q_2 already share u_1 and u_3, while Q_1 and Q_3 already share u_0 and u_2. For the four directed diagonal contacts define A=1 if Q_0 contains u_2, B=1 if Q_2 contains u_0, C=1 if Q_1 contains u_3, and D=1 if Q_3 contains u_1. Simplicity of Q_0,Q_1 gives A+C<=1; simplicity of Q_1,Q_2 gives B+C<=1; simplicity of Q_2,Q_3 gives B+D<=1; simplicity of Q_3,Q_0 gives D+A<=1. Thus the terminal-containing diagonal contacts form an independent set in the cycle A-C-B-D-A, so they are contained in one opposite pair {A,B} or {C,D}. Therefore either C=D=0 or A=B=0. In the first case complete source-rail transversality forces Q_1 to contain x_3 and Q_3 to contain x_1, so Q_1,Q_3 share x_1,x_3,u_0,u_2. In the second case Q_0,Q_2 share x_0,x_2,u_1,u_3. These four vertices are distinct by linearity.