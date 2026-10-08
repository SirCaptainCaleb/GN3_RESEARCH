# Cross-wall thickness reversals obey a parity law

## Development

Statement:
Retain the maximal connector and path-normalized tournament gauge of the wall-dominance theorem. Before separately wall-normalizing omitted vertices, write u_k(v)=t(c_k,v). Suppose distinct outside vertices a,b belong to opposite thickness classes at each of two internal gaps i and j. Set ε_k(a,b)=0 when a∈L_k,b∈R_k and ε_k(a,b)=1 when a∈R_k,b∈L_k. Then ε_i(a,b)⊕ε_j(a,b)=u_i(a)⊕u_i(b)⊕u_j(a)⊕u_j(b). In particular if a∈L_i and b∈R_i, then a and b cannot also lie in the same respective classes L_{i+2},R_{i+2} (provided i+2 is an internal gap); if both are opposite-thickness blockers at gap i+2, their types must reverse, a∈R_{i+2} and b∈L_{i+2}. No pair of opposite-thickness blockers at i is simultaneously wall-normalizable at either adjacent gap i−1 or i+1.

Proof:
Let t_0(a,b) denote the a→b bit in any initial gauge of the omitted vertices, while the connector gauge is fixed. To make c_k→v→c_{k+1} at a wall k, switch v precisely when u_k(v)=0, i.e. with bit s_k(v)=1⊕u_k(v). The edge a→b in this k-wall gauge has bit t_k(a,b)=t_0(a,b)⊕s_k(a)⊕s_k(b)=t_0(a,b)⊕u_k(a)⊕u_k(b). The wall-dominance theorem asserts t_k(a,b)=ε_k(a,b) whenever a,b are of opposite thickness. Eliminating t_0(a,b) between k=i and k=j proves the parity identity; it is invariant under arbitrary initial switches of a,b.

For a∈L_i,b∈R_i, in the canonical i-wall gauge their bits on c_{i−1},c_i,c_{i+1},c_{i+2} are respectively 1101 and 0100. They agree at i and disagree at i+2. Consequently the parity right-hand side for j=i+2 equals 1, so ε_{i+2}=1 if both are of opposite thickness there; their types reverse. At i+1 the incidence word of b has 00, hence α(c_{i+1},b,c_{i+2})=1 and b is outside W_{i+1}. At i−1 the word of a has 11, hence α(c_{i−1},a,c_i)=1 and a is outside W_{i−1}. Therefore the pair cannot be opposite-thickness blockers at adjacent walls. QED.
