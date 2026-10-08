# Actual-root face averages are zero-free on ternary faces with blocks of size at most five — preserved pre-item development

## Actual-root face averages are zero-free on ternary faces with blocks of size at most five

This strengthens root §32 for its particular all-refinements averaged carrier. It does not strengthen strict coorientation of arbitrary root sets: raw positive circuits still exist in four-coordinate A3 blocks.

### Local rotation lemma

Let h be ANY binary label on ordered r-tuples of distinct coordinates. On a set B of r+1 coordinates there is an order whose internal r-window word has no 10 transition. If r is odd, the same conclusion holds on r+2 coordinates. No reversal or alternating symmetry is required for this local lemma.

For |B|<=r the conclusion is immediate because there is at most one internal window.

#### Proof for |B|=r+1

Fix any cyclic coordinate order v_1,...,v_b, with b=r+1. Put
\[
c_j=h(v_j,v_{j+1},\ldots,v_{j+r-1}),
\]
where coordinate subscripts are cyclic modulo b. Cutting this cyclic coordinate order at v_j gives a linear order whose internal word is c_j,c_{j+1}. If every cut had a 10 transition, every cyclic adjacent color pair would equal 10. Consecutive pairs make incompatible demands on their common entry. Thus some cut has no 10.

#### Proof for |B|=r+2 when r is odd

Now b=r+2 is odd, and the word of each cut consists of c_j,c_{j+1},c_{j+2}. Suppose every cut contained 10. Let D be the set of cyclic transition indices j at which c_jc_{j+1}=10. Every two consecutive cyclic transition indices must meet D. But D contains no consecutive indices, since two overlapping transitions cannot both be 10.

Counting the b pairs of consecutive indices, each element of D lies in exactly two pairs. Thus 2|D|>=b. On the other hand, a subset of an odd cycle with no consecutive indices has size at most (b-1)/2. These inequalities contradict one another. Some cut therefore has no 10.

For ternary arity r=3, every set of at most five coordinates has an order with no internal 10 descent.

### Theorem for the averaged face carrier

Assume h is reversal-odd and every full order is bad, as in root §32. Let G be its continuous odd carrier obtained by averaging ALL actual 10 slide-root occurrences over every proper permutahedron face and interpolating over barycentric flags.

In ternary arity, G has strictly positive pairing with the inward normal of the largest face in each positive barycentric flag, hence is nonzero on the subcomplex of faces whose blocks all have size at most five. More generally the same statement holds for blocks of size at most r+1, and for size at most r+2 when r is odd.

Thus any zero of this particular averaged carrier, in ternary arity, has a face with a block of at least six coordinates. An A3 or A4 block cannot alone support such a zero, even though A3 supports positive dependences of selected individual roots.

### Proof: a crossing descent must occur

Let F=B_1|...|B_s be a proper face with blocks satisfying the stated bounds. Every root carried by an order refining F has its dropped endpoint no later in block order than its entering endpoint.

Suppose no refining order had a 10 root crossing between distinct blocks. Choose independently in each block an order with no internal 10 by the rotation lemma, and concatenate them in the face's fixed block order. Any 10 slide root in this full order would have both endpoints in one block by the supposition. Since blocks are contiguous, the entire r+1-coordinate slide support would then lie in that block, contradicting the chosen internal order.

Hence the concatenated full word has no 10. Such a binary word is 0^*1^* and is NOR-good, contradicting the hypothesis that every full order is bad. Therefore R_10(F) contains at least one root with endpoints in distinct blocks.

### Inward face-normal pairing

Realize the centered permutahedron with coordinate ranks 1,...,n minus their common mean. For F let mu_F(v) be the mean centered rank of the block containing v, and put
\[
L_F(z)=-\langle \mu_F,z\rangle.
\]
This is an inward FACE normal, not necessarily the radial direction of a point in F. Actual points inside a permutahedron face need not have equal coordinates inside its blocks.

Every root rho=e_a-e_b carried by F satisfies
\[
L_F(\rho)=\mu_F(b)-\mu_F(a)\ge0,
\]
with strict inequality for a crossing root. Because g_F averages every occurrence with a positive coefficient, L_F(g_F)>0.

For a barycentric point x take F to be the largest face whose barycenter has positive coefficient. Every smaller-face average contributing to G(x) is a convex combination of roots refining F, so its L_F value is nonnegative. The g_F coefficient is positive and its value strict. Hence
\[
L_F(G(x))>0.
\]
This proves nonvanishing.

For every H subset F, the sum of coordinates of b_H over each block of F equals the sum of the centered ranks occupied by that block. Therefore
\[
\langle\mu_F,b_H\rangle=\|\mu_F\|^2>0.
\]
The strict inequality holds because F is proper and has at least two ordered blocks. By convexity the same identity holds for x in F, giving L_F(-x)=||mu_F||^2>0.

### Topological consequence and limitation

On this larger subcomplex, the homotopy
\[
G_t(x)=(1-t)G(x)-t x,\qquad 0\le t\le1,
\]
never vanishes, by its strictly positive pairing with the inward face normal L_F. After normalization it is an odd homotopy to the inward radial map.

Thus the small-block part of this carrier has a controlled zero-free fill; a putative zero cannot be blamed on an automatic A3 reversal pair. This is stronger than mere root-set coorientation, because all-refinements averaging forces a crossing root whenever each individual block admits an internally descent-free order.

The local rotation lemma does not prove a descent-free order on an arbitrary large block. No theorem here forces G to vanish anywhere, or validates the radial-sign premise used in root §35. An inward face-normal inequality must not be substituted for a radial inequality. Also G still averages raw roots; protected deletion-witness admissibility is a separate condition. The new six-coordinate lower bound applies to zeros of THIS averaged carrier, not to arbitrary positive protected-root circuits or arbitrary choices of a single root per chamber.
