# The transposition already collapses at four vertices: Hamiltonian kernel or both transport triples

## Statement

In the two-core opposite-orientation transposition residue, with distinct special labels x,y and core witnesses r,s satisfying (y,r,x) and (x,s,y) tight, put X={x,y,r,s}. Then either H[X] is Hamiltonian, in which case in a minimum counterexample H-X is non-Hamiltonian with path-cover number exactly two, or H[X] is non-Hamiltonian and both cross-core transport triples (r,y,s) and (s,x,r) are tight. Thus the third special label z is unnecessary for reaching the Hamiltonian-kernel/transport frontier.

## Body

If H[X] is Hamiltonian, then X is a proper Hamiltonian support in the minimum-counterexample setting, so the complement principle mincex01 gives pc(H-X)=2 and H-X non-Hamiltonian. Suppose instead H[X] is non-Hamiltonian. The certified four-kernel classification compatkernelclass27 applies directly to the two base reverse-cross triples (y,r,x) and (x,s,y). Its proof forces both additional triples: because (y,r,x,s) cannot be a Hamilton path, (r,x,s) is non-tight and boundary antisymmetry gives (s,x,r) tight; because (x,s,y,r) cannot be Hamiltonian, (s,y,r) is non-tight and hence (r,y,s) is tight. Therefore both core-to-core transport orientations hold simultaneously. The later five-vertex theorem d17da9c70a4c remains useful for incorporating z, but the basic cocycle frontier already reduces at order four.
