# Every nonpath additive triple is balanced over path-even bit colorings

## Statement

Let B be an additive domain of size 2r+1 and let P be a spanning P_r in H(B). Let Sigma(P) be the F_2-vector space of functions sigma:B->F_2 for which every edge e of P has sum_{v in e}sigma(v)=0. Then dim Sigma(P)=r+1. For every additive triple e in E(H(B))\E(P), exactly half of sigma in Sigma(P) satisfy sum_{v in e}sigma(v)=1. Consequently some P-even coloring has at least (|E(H(B))|-r)/2 odd triples, all edge-disjoint from P.

## Body

Write the spanning path as
  e_i={a_{i-1},d_i,a_i},  1<=i<=r,
where a_0,...,a_r are its successive joint/end vertices and d_1,...,d_r are its private vertices. These 2r+1 labels are exactly B.

A function sigma is P-even exactly when
  sigma(d_i)=sigma(a_{i-1})+sigma(a_i)
for every i. Hence the r+1 values
  s_i=sigma(a_i)
are free and determine sigma uniquely. Thus Sigma(P) has dimension r+1.

Introduce formal basis vectors f_0,...,f_r of F_2^{r+1}, and define
  h(a_i)=f_i,
  h(d_i)=f_{i-1}+f_i.
For s=(s_0,...,s_r), the corresponding P-even coloring satisfies
  sigma_s(u)=s dot h(u)
for all u in B.

The only zero-sum triples in the formal label set h(B) are the path triples
  {f_{i-1}, f_{i-1}+f_i, f_i}.
Indeed, h(B) consists precisely of all weight-one basis vectors f_i and all adjacent weight-two vectors f_{i-1}+f_i. The sum of two distinct weight-one vectors lies in h(B) only when their indices are adjacent, giving the displayed path triple. The sum of a weight-one vector and an adjacent weight-two vector lies in h(B) only when the weight-one vector is one endpoint of that pair, again giving the same path triple. The sum of two distinct adjacent weight-two vectors has weight two with nonadjacent support when they overlap and weight four when they are disjoint, hence is not in h(B).

Now let e={u,v,w} be any additive triple of H(B), so u+v+w=0 in the ambient group. Put
  lambda_P(e)=h(u)+h(v)+h(w).
For e in P, lambda_P(e)=0. Conversely, by the preceding classification, lambda_P(e)=0 implies e is one of the path triples. Thus every e outside P has lambda_P(e) nonzero.

For sigma_s in Sigma(P),
  sum_{z in e}sigma_s(z)
  = s dot lambda_P(e).
When e is outside P, lambda_P(e) is a nonzero vector, so this linear functional of s is balanced: exactly half of the 2^{r+1} choices of s give value one.

Averaging the number of odd non-P triples over sigma in Sigma(P) therefore gives
  (|E(H(B))|-r)/2.
Hence at least one P-even coloring has at least this many odd triples. Every P-edge is even by definition, so the odd subhypergraph is edge-disjoint from P.

Combined with 47949910006a, a one-bit Hamiltonian lift exists whenever for some spanning P one of these path-even colorings has an odd-triple subhypergraph containing a spanning path Q with a common endpoint with P. Thus any non-Hamiltonian one-bit lift must defeat every such parity split.