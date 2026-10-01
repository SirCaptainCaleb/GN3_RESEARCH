# Two-hole wrong-entrance witnesses carry four edge-disjoint large blocker matchings

## Statement

Let Q=(h_1,...,h_s), s=ell-2, be an alternate wrong-entrance witness in a spanning top-rank core H on 2ell-1 vertices, as in 8e4a8307bc49. Write h_1={u,v,c}, where u,v are the two free opposite endpoints, let W=V(Q)\h_1, and let {a,b}=V(H)\V(Q). Assume delta(H)>=delta.

Then there are four pairwise edge-disjoint matchings on W, naturally centered at a,b,u,v, with sizes at least
  delta-4, delta-4, delta-3, delta-3,
respectively.

Consequently their union F satisfies
  |E(F)| >= 4delta-14
on
  |W|=2ell-6
vertices. In particular, under the dense-core threshold delta>=floor(2ell/3)+1,
  |E(F)| >= 4 floor(2ell/3)-10.
For ell=3m or ell=3m+2 this exceeds |W| by 2m-4. Hence for the good residue classes ell congruent to 0 or 2 mod 3, whenever m>=3 and the excess is positive (ell>=9 in residue 0, ell>=11 in residue 2), some vertex of W is incident with blocker pairs from at least three of the four centers {a,b,u,v}. At ell=6 or 8 the lower bound is exactly |W|, so the extremal no-triple-collision case forces the four-matching union to be 2-regular.

## Body

For the opposite endpoint u, apply 248026eed81e. Every edge through u other than h_1 is a single or double blocker on W, there are at most two single blockers, and the double-blocker pairs form a matching M_u on W. Thus
|M_u|=d_H(u)-1-S_u >= delta-3.
Likewise |M_v|>=delta-3.

Now consider the omitted hole a. By 67989a359cd2, apart from the possible unique edge containing both holes a,b, every a-edge has its other two vertices in V(Q), and those pairs form a matching N_a^* of size d_H(a)-epsilon, epsilon<=1. At most three pairs of this matching meet h_1, because N_a^* is a matching and h_1 has three vertices. Deleting those pairs leaves a matching N_a on W with
|N_a|>=d_H(a)-epsilon-3>=delta-4.
Similarly |N_b|>=delta-4.

Any two of M_u,M_v,N_a,N_b are edge-disjoint. Indeed, if the same pair {r,s} subset W occurred for two distinct centers z,z' in {u,v,a,b}, the corresponding hyperedges {z,r,s} and {z',r,s} would share the two vertices r,s, violating linearity.

Thus the union F is a simple graph on W with maximum degree at most four and
|E(F)|>=2(delta-3)+2(delta-4)=4delta-14.

If |E(F)|>|W|, its average degree is greater than two, so some vertex has degree at least three. Since each color class is a matching, those incident edges come from at least three distinct centers.

At the threshold delta>=floor(2ell/3)+1, substitute to obtain the displayed bound. If ell=3m, the excess over |W| is
(8m-10)-(6m-6)=2m-4.
If ell=3m+2, it is
(8m-6)-(6m-2)=2m-4.
When equality holds and no vertex has degree at least three, every vertex has degree exactly two, so F is 2-regular.
