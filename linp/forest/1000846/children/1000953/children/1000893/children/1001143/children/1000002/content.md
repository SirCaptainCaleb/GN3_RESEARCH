# Set-sequential paths close the critical induced-Boolean construction route

## Statement

Assume the near-Steiner classification fb1725da2cc8. For critical components |A|=2ell+1 in induced Boolean Schur hypergraphs H(A), strict improvement over the generic (ell-1)/3 density can occur only at ell=3 or ell=7. More precisely, all full projective candidates A=F_2^r\{0} are Hamiltonian for r>=5 by the Mehta--Vijayakumar set-sequential path theorem, and all two-point-deleted projective candidates A=F_2^r\{0,a,b} are Hamiltonian for r>=5 by deleting an endpoint vertex and its adjacent edge-label from such a set-sequential path and applying GL(r,2) 2-transitivity. The small two-point cases r=3,4 are also Hamiltonian; the full r=3,4 systems are the Fano P3-free and PG(3,2) P7-free exceptions.

## Body

A spanning linear path in the additive triple system on a domain A is equivalent to a set-sequential labeling of an ordinary path. Indeed, write the successive joint/end vertices of an ell-edge loose path as x_0,...,x_ell. The i-th hyperedge is
{x_{i-1}, x_i, d_i},  d_i=x_{i-1}+x_i.
The loose path is spanning precisely when the ell+1 vertex labels x_i and the ell edge labels d_i are all distinct and together equal A. Thus for A=F_2^r\{0}, a spanning P_{2^{r-1}-1} is exactly a set-sequential labeling of the ordinary path on 2^{r-1} vertices by the nonzero vectors of F_2^r.

Mehta, Vijayakumar and Arumugam, "A Note on Ternary Sequences of Strings of 0 and 1", AKCE Int. J. Graphs Comb. 5(2) (2008), 175-179, prove that these paths are set-sequential for r>=5 (equivalently their sequentially ternary permutation exists for dimension greater than four). This is also quoted explicitly in Golowich--Kim, Discrete Math. 343 (2020), 111741: all paths with at least 16 vertices of the admissible power-of-two orders are set-sequential. Therefore PG(r-1,2) contains a spanning P_{2^{r-1}-1} for every r>=5.

For the two-point deletion A=F_2^r\{0,a,b}, take any full set-sequential path for r>=5. Delete one endpoint vertex label u and the label v of its incident ordinary path edge. What remains is an ordinary path on 2^{r-1}-1 vertices whose vertex and edge labels partition F_2^r\{0,u,v}; equivalently the two-point-deleted additive triple system contains a spanning P_{2^{r-1}-2}. Since u and v are distinct nonzero vectors, and over F_2 every two distinct nonzero vectors are linearly independent, GL(r,2) is transitive on ordered distinct pairs. Hence for any prescribed distinct nonzero a,b, a linear automorphism sends (u,v) to (a,b), giving a spanning path in F_2^r\{0,a,b}.

It remains only to inspect dimensions below five. For r=3 the full Fano system is P3-free because any two projective lines intersect, while every two-point deletion contains P2. For r=4 the full PG(3,2) system is P7-free by the repaired theorem d593f8024a92, while every two-point deletion contains P6: PG(3,2) has a linear C7 (8a41aa9f3ecc); deleting one cycle edge leaves a P6 omitting two points, and GL(4,2) moves that omitted ordered pair to any prescribed pair.

Combining this with fb1725da2cc8 and 711446f37882, every critical odd induced Boolean domain that strictly beats the generic density is therefore eliminated except the full projective exceptions r=3 and r=4, corresponding to ell=3 and ell=7.
