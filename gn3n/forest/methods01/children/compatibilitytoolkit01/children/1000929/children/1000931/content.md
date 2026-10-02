# An odd deletion-support cycle gives fractional mass-two certificates and a dual obstruction

## Statement

Assume the selected support graph of deletion covers is an odd cycle on n=2k+1 supports S_i, with edge S_i S_{i+1} labeled d_i. For every nonempty tight-path support T, let I(T),O(T),C(T) be the ground-cycle edges with respectively two, zero, or one endpoint in T. Then the exact nonnegative incidence identity 1_T+2 sum_{i in I(T)}1_{S_i}+sum_{i in C(T)}1_{S_i}=|T| 1_V holds. Hence T together with the selected supports gives a fractional path cover of total mass exactly 2+1/|T|. In particular, if lambda is the maximum tight-path order, tau*(H)<=2+1/lambda (and the selected cycle alone gives 2+1/k). If T is a vertex cover of the ground cycle, the sharper identity from the proof gives fractional mass two; when |T|=k+1 this is an integral two-cover. More generally tau*(H)<=2 iff there is a distribution of tight-path supports with adjacent marginal sums at least one, and every dual obstruction above two has the exact sigma-description proved below.

## Body

Let n=2k+1, and suppose the selected support graph is the cycle with support vertices S_0,...,S_{n-1} and deletion labels d_i on S_i S_{i+1}. Indices are modulo n. Each S_i is a Hamiltonian k-set, and

    1_{S_i}+1_{S_{i+1}} = 1_V-1_{d_i},
    sum_i 1_{S_i} = k 1_V.

Define the ordinary cycle C on the ground vertices d_0,...,d_{n-1}, with edges {d_{i-1},d_i}. This ground-vertex cycle is distinct from the support graph, although their indices naturally correspond.

### A Hamiltonian vertex cover of C gives a fractional cover of mass two

**Theorem.** Suppose T is the support of a tight path and is a vertex cover of C. Write |T|=k+r; necessarily r>=1. Let

    I(T)={i : d_{i-1} and d_i both belong to T}.

Then |I(T)|=2r-1 and

    1_T + sum_{i in I(T)} 1_{S_i} = r 1_V.

Consequently the tight path on T and the tight paths on S_i for i in I(T), each with weight 1/r, form a fractional path cover with every vertex covered exactly once and total mass exactly two. When r=1, these are two disjoint spanning paths, so this case directly gives an integral two-cover.

**Proof.** Put t_i=1_T(d_i) and a_i=t_{i-1}+t_i. Since T covers every edge of C, a_i is either one or two, and a_i-1 is the indicator of I(T). Using the cycle identities,

    sum_i a_i 1_{S_i}
      = sum_j t_j (1_{S_j}+1_{S_{j+1}})
      = |T| 1_V-1_T.

Subtract sum_i 1_{S_i}=k 1_V. This gives

    sum_{i in I(T)} 1_{S_i}=(|T|-k)1_V-1_T=r1_V-1_T.

Also sum_i a_i=2|T|, while sum_i a_i=n+|I(T)|. Therefore |I(T)|=2(k+r)-(2k+1)=2r-1. There are 2r path supports in the displayed cover, each with weight 1/r, proving mass two and exact vertex coverage. For r=1 the incidence identity says that T and the single selected S_i are disjoint and cover V.

No agreement between Hamilton orders on different supports is needed for this fractional construction. In a hypothetical counterexample the r=1 case is impossible; the theorem does not assume that a Hamiltonian vertex cover exists for r>=2.

### The signed identity for an arbitrary additional path

For any subset T, including one which does not cover C, define

    I(T)={i : both d_{i-1},d_i are in T},
    O(T)={i : neither d_{i-1},d_i is in T}.

The same calculation gives

    1_T + sum_{i in I(T)}1_{S_i}
      = (|T|-k)1_V + sum_{i in O(T)}1_{S_i}.

Thus the edges of C missed by T identify exactly the negative coefficients that obstruct the preceding positive fractional-cover construction. This keeps the particular cyclic support configuration visible.

### A distributional version and an exact criterion for fractional mass two

Let P be a random tight-path support, with marginal inclusion probabilities p_i=Pr(d_i in P), and put L=E|P|=sum_i p_i. Suppose

    p_{i-1}+p_i >= 1 for every i.

Summing these inequalities gives L>=n/2=k+1/2, so r=L-k>0. Taking expectations in the signed identity shows

    E 1_P + sum_i (p_{i-1}+p_i-1)1_{S_i} = r 1_V.

Give each path in the distribution its probability divided by r, and give S_i the additional weight (p_{i-1}+p_i-1)/r. These weights are nonnegative. They cover every vertex exactly once, and their total mass is

    [1+sum_i(p_{i-1}+p_i-1)]/r
      = [1+2L-n]/(L-k)
      = 2.

Conversely, if H has a fractional path cover of mass at most two, add weight on any nonempty tight path until the mass is two and normalize the weights to a probability distribution. Every vertex then has inclusion probability at least one half, so the adjacent marginal inequalities hold. Therefore, in the presence of the selected odd support cycle, fractional path-cover number at most two is equivalent to the existence of a distribution of tight paths satisfying just these adjacent marginal inequalities. The single Hamiltonian vertex-cover theorem is the deterministic special case.

This is a constructive equivalence. It does not assert that the required distribution exists.

### Every dual certificate above two has an explicit form on C

Let w be any nonnegative dual-feasible vertex weighting, so w(P)<=1 for every tight path P, and suppose w(V)=2+eta with eta>0. Put

    sigma_i=1-w(S_i)>=0.

The deletion-cover identity S_i disjoint-union S_{i+1}=V-{d_i} gives

    w(d_i)=eta+sigma_i+sigma_{i+1}.

Summing the path slacks, or summing this formula, gives

    sum_i sigma_i=1-k eta.

For any tight-path support T, with a_i=1_T(d_{i-1})+1_T(d_i),

    w(T)=1+eta(|T|-k)+sum_i sigma_i(a_i-1).

Dual feasibility is therefore equivalent, for each such T, to

    sum_{i in O(T)} sigma_i
      >= eta(|T|-k)+sum_{i in I(T)} sigma_i.

In particular, every tight path of order greater than k must miss a cycle edge with positive sigma-weight; the missed-edge weight must pay both its size surplus and the sigma-weight of the cycle edges wholly contained in the path. A Hamiltonian vertex cover has O(T) empty and |T|>k, immediately contradicting this inequality. This is the dual proof of the fractional two-cover criterion.

Conversely, eta>0 and nonnegative sigma_i with sum sigma_i=1-k eta define w(d_i)=eta+sigma_i+sigma_{i+1}; if the displayed inequalities hold for all tight paths, w is dual feasible and has total mass 2+eta. Thus this is an exact description of dual obstructions above two in this cyclic configuration, not merely a necessary estimate.


Scope: neither existence of the qualifying path/distribution nor integral rounding for r>1 is proved. The cycle is not eliminated. The incidence identities follow from 1000929; the remaining calculations are elementary and require no unproved rounding or uncrossing premise.