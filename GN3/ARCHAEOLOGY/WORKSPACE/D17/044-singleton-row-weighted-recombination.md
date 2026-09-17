# Singleton-fiber energy: selected-edge row weights and exact incoming cut cost

**Workspace:** D17
**State:** established
**Key:** `singleton-row-weighted-recombination`

**Summary:** Total K change under an arbitrary one-fiber replacement is exactly the change in selected-edge weight plus a labelled multigraph cut cost. Fixed-support order optimization remains collateral-free; support-changing repairs now have an explicit incoming-cost ledger. Includes weighted cycle-cost optimality and a seam-free bridge repair candidate, without asserting descent or global closure.

### Setup and row linearization
Retain the singleton-cover family and the ordered substitution defects of `codimension-one-coherence`. Thus for each deletion label x an actual exact two-cover C_x of H-x has unordered support partition sigma_x, and for distinct a,b the target partition tau_{a<-b} of H-a is obtained from sigma_b by replacing the deleted label a in its sigma_b block by b.

Fix a. Hold all support partitions sigma_x fixed. For an ordinary directed selected adjacency e=uv of any exact two-cover C of H-a having support partition sigma_a, define

  w_a(e) = |{ b != a : u and v lie in different blocks of tau_{a<-b} }|.

This is a nonnegative integer depending only on the fixed support family and the physical adjacency e, not on the rest of the path order. Let

  R_a(C)=sum_{b != a} kappa_C(a<-b)

be the outgoing defect row of C. Interchanging the two finite sums gives the exact identity

  R_a(C)=sum_{e selected in C} w_a(e).

Now replace C_a by another exact two-cover C'_a of H-a with the SAME unordered support partition sigma_a. Every target partition tau_{c<-a} occurring in an incoming term kappa(c<-a) depends only on sigma_a, so every incoming term is unchanged. No ordered comparison not involving a changes at all. Therefore

  K(C'_a,{C_x}_{x!=a})-K(C_a,{C_x}_{x!=a}) = R_a(C'_a)-R_a(C_a).

Consequently, once the support partitions are fixed, minimization of total K over path-order representatives factorizes fiber by fiber: every globally K-minimal family may be assumed to minimize R_a independently among all exact covers of H-a with support sigma_a. This is the requested collateral-free part of the K program. Support-changing replacements also alter incoming comparisons; their exact cost is given below.

### Weighted cycle-cost certificate inside one fixed support partition
Let F_0,F_1 be two exact two-covers of H-a with the same support partition A|B, and suppose F_0 is row-minimal for R_a among all such representatives. Encode their directed path adjacencies by the bipartite matchings M_0,M_1 used in `cycle-cost-cover-recombination`. Every selected adjacency of either matching has both endpoints in A or both endpoints in B.

For each alternating symmetric-difference component D define

  eta_a(D)=sum_{e in M_1 cap D} w_a(e)-sum_{e in M_0 cap D} w_a(e).

For a locally admissible preorder upper set W put eta_a(W)=sum_{D in W} eta_a(D), and retain the cycle-cost notation Delta(W) and c(W). Before breaking directed cycles, the recombined selected digraph has row weight exactly

  R_a(F_0)+eta_a(W).

Because every selected edge remains inside A or inside B, after breaking all directed cycles the resulting path cover still has no A|B selected adjacency. Hence it has at least one path on A and at least one path on B. The cycle-cost formula gives exactly

  2-Delta(W)+c(W)

paths. Therefore every locally admissible W necessarily satisfies

  Delta(W) <= c(W).

Suppose equality holds. Breaking the c(W) directed cycles then leaves exactly two paths. Since no selected edge crosses A|B and both supports are nonempty, those two paths are necessarily one Hamilton path on A and one Hamilton path on B, hence another exact same-support representative.

For each directed cycle Z of the recombined selected digraph choose a selected adjacency of maximum w_a-weight and delete it. Put

  mu_a(W)=sum_Z max_{e in E(Z)} w_a(e),

with mu_a(W)=0 when there are no cycles. The resulting exact same-support two-cover has row defect at most

  R_a(F_0)+eta_a(W)-mu_a(W).

Row minimality of F_0 therefore forces the weighted certificate

  eta_a(W) >= mu_a(W)

for every locally admissible upper set W with Delta(W)=c(W).

In particular a zero-or-negative symmetric-difference row change cannot hide behind a positive-weight cycle tax: if any resulting cycle contains a selected adjacency carrying positive K-weight, equality Delta=c already contradicts row minimality unless the flipped components contribute enough positive eta to pay for that removable edge.

### Exact incoming cut cost for arbitrary support changes
Fix the actual covers C_b for all b != a; do not fix the support partition of the replacement C of H-a. The weights w_a(uv) above are still defined for EVERY pair u,v in V-a using only those fixed other covers.

Construct a labelled undirected multigraph J_a on V-a as follows. For each b != a and each selected adjacency uv of C_b, replace its occurrence of a, if present, by b, and retain the resulting edge with its provenance (b,uv). In formulas let rho_b(a)=b and rho_b(v)=v for v != a on V-b, and add rho_b(u)rho_b(v). The map rho_b:V-b -> V-a is a bijection, so there are no loops. Parallel edges must retain multiplicity and their physical source labels.

For any actual exact two-cover C of H-a let sigma(C)=A|B and let cut_Ja(A,B) count J_a edges between A and B, with multiplicity. Then the FULL part of K involving a is exactly
  E_a(C) = sum_{uv selected in C} w_a(uv) + cut_Ja(A,B).
Consequently for any replacement C' of C_a, including a support-changing one,
  K(new)-K(old) = E_a(C')-E_a(C_a).

Proof. The first term is the outgoing row by interchanging finite sums, with no restriction on sigma(C). For the incoming term kappa(b<-a), the target partition of V-b is sigma(C) with b replaced in its block by a. Equivalently the block label of v in that target is the sigma(C) block label of rho_b(v). Thus a selected adjacency uv of C_b contributes to kappa(b<-a) precisely when its labelled image edge rho_b(u)rho_b(v) crosses A|B. Sum over all selected adjacencies and b != a. These are exactly the incoming terms. All comparisons with neither index a are unchanged. This proves both identities.

This also gives an exact finite certificate for one-fiber optimality. For a nonempty proper A subset V-a put B=(V-a)-A and let h_a(A) be the minimum total w_a weight of an actual Hamilton tight path on A, or infinity if none exists (the singleton value is zero). Then
  min_C E_a(C) = min_{A|B} [ h_a(A)+h_a(B)+cut_Ja(A,B) ],
where the left minimum is over actual exact two-covers of H-a and the right is over unordered nonempty bipartitions. For each fixed partition, the two path orders can be optimized independently and their concatenation as two disjoint rails realizes the displayed sum. Conversely every actual two-cover supplies such two Hamilton paths. This proves the equality. It is not an unconstrained minimum-cut problem: the Hamilton path costs and their realizing orders are essential.

One immediate physical candidate comes from the no-interior-crossing bridge in codimension-one-coherence. Retain C_b=Q|T with Q on {a}+S and T on T_0, and C_a with literal mixed rail S-b-T_1 (or its reverse) and other rail T_2, where T_1,T_2 partition T_0. The contiguous S-through-b subpath of the mixed rail, together with the untouched source rail T, is an actual replacement C'_a on (S+b)|T_0. No new junction is introduced. It makes kappa(a<-b)=0, but global improvement holds ONLY if its explicitly computed E_a cost is smaller; the cut term counts all collateral incoming changes. A tie is a neutral replacement, not strict descent.

### Scope
The incoming cut representation extends the order-only lemma to exact collateral accounting for ANY one-fiber replacement. It does not force a profitable replacement, make support changes independent across fibers, or prove that a coordinatewise minimum is a global minimum. A fixed-witness defect fan still needs an actual cheaper cover, a fully costed simultaneous replacement, or a direct spanning two-cover. Directed-cycle recombinations still require the cycle and junction checks above.

Status: complete internal arguments, including the incoming-cut identity and the seam-free bridge candidate; not independently reviewed or canonically certified. The global K-repair theorem remains open.
