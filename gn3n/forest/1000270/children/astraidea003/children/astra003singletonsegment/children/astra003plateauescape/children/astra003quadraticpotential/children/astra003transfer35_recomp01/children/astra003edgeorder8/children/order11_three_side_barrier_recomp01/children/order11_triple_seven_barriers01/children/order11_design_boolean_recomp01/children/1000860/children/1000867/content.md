# Every extendable center in the order-eleven design has a matched blocked 4|4 frame

## Statement

Let H be a hypothetical order-eleven minimum counterexample in the no-blocked-overlap design branch, with prescribed three-set X, U=V(H)-X, and blocked 14-block 3-(8,4,1) family F. Let C be any Hamiltonian four-set in U outside F and put D=U-C. Then there is a unique bijection phi:C->D such that for every c in C the set A_c=(C-{c}) union {phi(c)} belongs to F. The complementary set B_c={c} union (D-{phi(c)}) also belongs to F. Hence A_c|B_c is a Hamiltonian 4|4 partition of U for every c, and both X union A_c and X union B_c are non-Hamiltonian, while X union C is Hamiltonian. Thus every extendable center C is surrounded by four explicitly matched blocked balanced complements.

## Body

Work in the design branch and fix a Hamiltonian four-set C outside F. Put D=U-C.

For each c in C, the triple T_c=C-{c} lies in a unique block A_c of the 3-(8,4,1) family F. Since C is not itself a block, A_c=T_c union {d_c} for some d_c in D. Define phi(c)=d_c.

The map phi is injective. Indeed, if c!=c' but phi(c)=phi(c')=d, then the two distinct blocks A_c and A_c' both contain the three-set (C-{c,c'}) union {d}, contradicting the lambda=1 property of the 3-design. Since |C|=|D|=4, phi is a bijection.

It remains to identify the complementary blocks. Any 3-(8,4,1) family has fourteen blocks and is closed under complements. To see this, fix a block A. No other block meets A in three vertices. Every pair of A lies in exactly lambda_2=(8-2)/(4-2)=3 blocks, so besides A the six pairs of A contribute 12 incidences with blocks meeting A in exactly two vertices. Hence twelve of the thirteen other blocks meet A in two vertices. Each vertex of A lies in lambda_1=C(7,2)/C(3,2)=7 blocks, so the twelve two-intersection blocks already account for all 4*6=24 incidences of A-vertices with blocks other than A. The remaining block is therefore disjoint from A and must equal U-A.

Applying this to A_c shows that
B_c=U-A_c={c} union (D-{phi(c)})
also belongs to F.

Every block of F is Hamiltonian and blocked by X, so A_c and B_c form a Hamiltonian 4|4 partition of U with both X union A_c and X union B_c non-Hamiltonian. By 1000860, because C is Hamiltonian and outside F, X union C is Hamiltonian. Thus the four matched partitions are explicit blocked neighbors around the extendable center C.
