# Paired midpoint collisions: unrestricted tensor identity and raw critical-scarcity barrier

- Stable ID: note_nori_xvi_midpoint_tensor_product_and_scarcity_barrier_20261018_r11755
- Author: unspecified; session provenance retained
- Primary home: subsection:gauge_critical_switches_and_clustered_witnesses_on_full_paths
- Labels: NORI1, paired-flat, midpoint-collision, tensor-product, square-switch, method-obstruction, dimension-uniform, proved
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11755_1
- Updated session: session_nori_r11755_1
- Disposition: none
- Successor: none

## Related references

- note:note_dd297b14828b049d0221340b
- subsection:obstruction_compatibility_and_a_programme_for_nori1_closure

## Research note

# Paired-midpoint collision tensor identity and sharp raw-scarcity obstruction

Use the paired-flat red matching involutions T_i from note_dd297b14828b049d0221340b. For each root x and two full orders pi,rho of the m direction pairs, count a collision when T_pi(x)=T_rho(bar x). Write W(c) for this number of triples. Every collision yields a red full antipodal geodesic: the joined two halfpaths use each pair twice and reach the antipode, so the two different original directions in each pair each appear once.

**Theorem 1 (dimension-uniform tensor identity).** For arbitrary paired-flat legal c on Q_(2m), d on Q_(2k), their disjoint-block product c box d satisfies W(c box d)=binom(m+k,m)^2 W(c)W(d). Hence w(c):=W(c)/(m!)^2 obeys w(c box d)=w(c)w(d).

**Proof.** A full pair ordering in the product restricts to one ordering of the m labels of c and one of the k labels of d. Any such pair of restricted orders has binom(m+k,m) interleavings. The complete red sweep endpoint in the product is the ordered pair of restricted endpoints, independent of the interleaving. Therefore a collision between two product sweeps holds precisely when both restricted collisions hold. Independent interleavings of the two sweep words contribute the square of binom(m+k,m). QED.

**Theorem 2 (two-pair base).** Every paired-flat Q4 coloring has W=8.

**Proof.** Put p_i=x_(2i)+x_(2i+1) and t_i=x_(2i), in F2. Its two gates are f_0=t_1+a(p_1), f_1=t_0+b(p_0); antipodal oddness forces this form, with arbitrary functions a,b on one bit. The red matching T_0 flips p_0 and adds t_1+1+a(p_1) to t_0; T_1 flips p_1 and adds t_0+1+b(p_0) to t_1. Their linear parts on t=(t_0,t_1) are L_0=[[1,1],[0,1]], L_1=[[1,0],[1,1]]. Accordingly the two complete sweep orders have affine linear parts A=L_1 L_0=[[1,1],[1,0]], B=L_0 L_1=[[0,1],[1,1]], satisfying A+B=I over F2. The affine constants depend on the initial p, independently of t. The antipodal map fixes p and changes t to t+(1,1). Equal orders cannot collide since each sweep is bijective. For each of the four p values, each of the opposite-order equations A(t)+a_p=B(t+(1,1))+b_p and B(t)+b_p=A(t+(1,1))+a_p has a unique solution t, because A+B=I. Hence W=4*2=8. QED.

**Corollary (the raw critical-scarcity threshold cannot ensure survival).** The disjoint-block product of any two paired-flat Q4 colorings is legal and paired-flat on Q8, with W=binom(4,2)^2*8^2=2304 and w=4. The established critical-square scarcity bound in note_dd297b14828b049d0221340b yields at m=4 the necessary inequality W<=16(1-1/4)*(4!)^2=6912, equivalently w<=12. Thus even a good paired-flat Q8 coloring can lie well below this threshold. A universal lower bound W>6912 across all paired-flat Q8 colorings is false. Any contradiction based on that critical-scarcity bound must use additional hypotheses of a first good-to-bad boundary rather than collision count alone. In Q_(4r), products of r Q4 colorings have normalized collision count w=2^r.

**Independent check.** Enumeration of all 16 legal Q4 gate assignments gives W=8 each, and enumeration of a two-block Q8 product gives W=2304, verified by nori_midpoint_tensor_verifier.py. The symbolic proofs above establish the statements in their stated scopes.

**Closure scope.** The tensor identity works in every dimension and with nonlinear gates. Theorem 2 and the exhibited barrier are finite-dimensional. Nothing here proves arbitrary square-switch witness preservation or the boundary-tournament simplicity implication.

**Theorem 3 (tensor amplification cannot outrun the aggregate flip-Lipschitz budget).** For every k>=2 and every paired-flat legal d on Q_(2k),

w(d) <= 2^(2k) (1-1/k!).

If c on Q_(2m) is a hypothetical critical good-side coloring for one paired-square switch, the known scarcity bound gives w(c)<=16(1-1/m). In the product c box d, that square switch replicates as 2^(2k) antipodally paired alternating-square switches: pair the copy of the first face over y with the copy of its antipodal face over bar y. Their switched sets partition all changed edges and preserve legality. The normalized collision-count gap between c box d and the product of the bad neighbor with d is w(c)w(d), at most

16 (1-1/m) 2^(2k)(1-1/k!) < 16 * 2^(2k).

The established single paired-square Lipschitz bound is |Delta W|<=16((m+k)!)^2. Summing it over 2^(2k) replicated switches gives allowance 16*2^(2k)((m+k)!)^2, strictly larger than the total required drop. Consequently a contradiction cannot follow solely from the product identity, critical-scarcity inequality, and telescoped unweighted Lipschitz estimate, for any choice of padding d.

**Proof of the universal upper bound.** For each root, there are k!^2 ordered pairs of full pair sweep orders, but the k! diagonal pairs pi=rho never collide because T_pi is a bijection and x!=bar x. Thus W(d)<=2^(2k)k!(k!-1), giving the bound after dividing by (k!)^2. The displayed implications now follow by multiplication and the stated decomposition of the copied switched faces. QED.

**Scope of Theorem 3.** It excludes this particular aggregate counting argument. Intermediate colorings on the replication path may carry nonlinear information and may admit stronger conditional estimates. The theorem makes no claim that more refined local transport is impossible.
