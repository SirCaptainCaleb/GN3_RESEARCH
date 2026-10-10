# All-even physical paired-root subspace and sparse-defect one-switch extraction

# Explicit paired-root cubical realization and an exact sparse defect criterion

Let n=2m≥4 be even, k=m−2, and let p=(p_1,...,p_(2m)) be any full direction order. Suppose a coloring of ACTUAL ordered three-faces is constant within each of the two central exterior-weight layers and switches across them:
 c(F,π)=a(π) for exterior weight k, and c(F,π)=1+a(π) for exterior weight k+1,
with arbitrary dependence elsewhere subject to antipodal-reversal oddness. Let a_i=a(p_i,p_(i+1),p_(i+2)), 1≤i≤2m−2.

**THEOREM A (all-even-dimensional paired physical root subspace).** For every bit vector b=(b_1,...,b_m) construct a genuine cube starting vertex x, in p-position coordinates, by

 x_(2j−1)=1−b_j,   x_(2j)=b_j,   1≤j≤m.

Along the actual n-edge geodesic from x in order p, EVERY three-face window has exterior weight k or k+1, with the exact profile t_i=K_i−k given by

 t_(2j−1)=b_(j+1),   t_(2j)=b_j,   1≤j≤m−1.

Thus the set H_m of such realizable profiles is the m-dimensional LINEAR subspace of F2^(2m−2) determined by the m−2 equations

 t_(2j−1)=t_(2j+2),   1≤j≤m−2.

Proof. Every adjacent starting pair (x_(2j−1),x_(2j)) has one 1. For window 2j−1 the earlier j−1 pairs have been flipped and each still contributes one exterior 1; the later m−j−1 full pairs likewise each contribute one; the remaining exterior bit is x_(2j+2)=b_(j+1). Hence K_(2j−1)=(j−1)+(m−j−1)+b_(j+1)=m−2+b_(j+1). For window 2j the same full-pair count m−2 remains; the earlier singleton x_(2j−1), already flipped, is b_j. Hence K_(2j)=m−2+b_j. Every b gives its stated t; conversely its even positions recover b_1,...,b_(m−1) and its last odd position recovers b_m. Thus the image has dimension m, and exactly the m−2 displayed independent equalities describe it.

**THEOREM B (dimension-independent sparse defect extraction).** Define the (m−2)-bit defect vector of the direction order by

 d_j = a_(2j−1)+a_(2j+2)  (mod 2), 1≤j≤m−2.

If d is either the zero vector, a singleton 1 at one position, or two 1s at adjacent positions, then at least TWO distinct paired cube starting vertices produce a full antipodal n-geodesic with at most one three-face color change.

Proof. Let G be all constant or one-switch binary words g=(g_1,...,g_(2m−2)). For a word g changing between indices h and h+1, the differences g_(2j−1)+g_(2j+2) equal1 precisely if the cut h lies among the three positions 2j−1,2j,2j+1. Consequently the set of attainable defect vectors D(G) is EXACTLY {0} ∪ {e_j} ∪ {e_j+e_(j+1)}, with indices in 1,...,m−2. (Use an even cut h=2j for singleton e_j, and an odd cut h=2j+1 for neighboring pair; endpoint cases are immediate.) Under the hypothesis choose g∈G with D(g)=D(a), so t=a+g obeys all H_m equalities. Theorem A supplies b and a REAL full cube geodesic with profile t. Every window has actual color a_i+t_i=g_i and therefore ≤1 change. Replacing b by its bitwise complement changes t by the all-ones word and hence the actual color word to 1−g, yielding another distinct good root with the same order. QED.

**Corollary Q8 (analytic every-order closure).** At n=8, m−2=2, and EVERY possible defect vector of length 2 is on the admissible list. Thus every order p has at least two explicit good physical starting roots. This replaces the prior fixed-order finite root-profile certificate with a uniform all-orders proof.

**Corollary Q12 (analytic four-block certificate).** At n=12, m−2=4. If a_1=a_4 and a_7=a_10, then d_1=d_4=0. The remaining (d_2,d_3) may have any values; d is zero, singleton, or a pair of adjacent ones, so Theorem B produces two actual good paired roots. Grouping the direction order into four disjoint ordered triples, an even-parity four-triple partition can be ordered to force precisely these equalities. The separately proved partition-parity rigidity theorem handles the opposite case where every partition has odd parity. Thus the Q12 two-layer switching theorem has a COMPLETE PURELY ALGEBRAIC proof, without numerical root enumeration.

**All-dimensional frontier.** The paired-root method reduces the full two-layer subclass to finding a direction order p whose physical coordinate-triple intercept defect vector d has support zero, one, or two consecutive positions. For n≥14, arbitrary fixed direction orders need not have sparse defects. For the unrestricted grand NORI conjecture, actual face colors within the central exterior layers may vary with fixed exterior coordinates, and the same-root paired bit construction alone does not erase that dependence.
