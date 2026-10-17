# Poisson profile occupancy and covariance laws for uniform legal cube colorings

- Stable ID: note_09c2afedfed635c4842cd6ff
- Author: unspecified; session provenance retained
- Primary home: subsection:full_geodesic_color_profiles_span_the_entire_binary_space
- Labels: NORI1, unrestricted, Poisson, random-coloring, fixed-direction-order, root-profile-incidence, covariance, concentration
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11254_5
- Updated session: session_nori_r11254_5
- Disposition: none
- Successor: none

## Related references

- None

## Research note

# Poisson root-profile occupancy and multinomial covariance for random unrestricted cube colorings

**Setting.** Fix n>=3 and any permutation pi of the n direction labels. Choose a legal antipodally odd edge coloring c of Q_n uniformly at random. Equivalently, its n 2^(n-2) antipodal orbits of undirected edges carry independent uniform fair bits; the opposite member of each orbit carries the complementary bit. For each starting root x, let W_pi(x) in F_2^n denote the full direction-indexed color profile in the prescribed order. For a target word w define X_w=|{x in F_2^n: W_pi(x)=w}|. Put N=2^n and S_pi=|{W_pi(x):x in F_2^n}|.

**Theorem 1 (full second-order occupancy law).** For every target profile w, E X_w=1. For all target profiles u,v,
Cov(X_u,X_v) = 1_(u=v) + 1_(v=u+1) - 2/N.
In particular Var(X_w)=1-2/N. One also has the deterministic identity X_w=X_(w+1), since the profile from an antipodal root is the bitwise complement. Thus the whole family has the same mean vector and covariance matrix as placing N/2 independent balls uniformly into N/2 boxes indexed by the unordered complementary profile pairs {w,w+1}, recording the box occupancy as X_w. This comparison is of first and second moments, not a statement that the higher-order distributions coincide.

**Proof.** The edge sets of two full paths with the same order pi and roots x,y have antipodal edge orbits in common in direction i if and only if y+x belongs to {0,e_i,1,1+e_i}. This follows because the prefix mask prior to direction i is common to all roots, and antipodal orbit equality of direction-i edges is equivalence modulo the four-element subgroup spanned by e_i and the all-one vector 1. For n>=3, the four displacement types listed below are disjoint.

Every full path uses n different antipodal edge-orbit bits, one per direction, so each fixed word has probability 2^(-n)=1/N. Let delta=x+y. When delta=0, both target events coincide if and only if u=v, with joint probability 1/N. When delta=1, the two color words are complements, so joint probability is 1/N if v=u+1 and zero otherwise. For delta=e_i, the two paths share one undirected edge of direction i and otherwise use disjoint orbit bits; their target events have joint probability 2/N^2 if u_i=v_i, and zero otherwise. For delta=1+e_i, the shared direction-i orbit occurs with opposite color, so the joint probability is 2/N^2 when u_i!=v_i and zero otherwise. For every other delta, the two sets of orbit bits are disjoint and the joint probability is 1/N^2.

There are N choices of x for each delta. For every i, precisely one of delta=e_i and delta=1+e_i is compatible with u_i,v_i, contributing 2/N in total after summing over roots. The remaining N-2n-2 nonspecial displacement values contribute (N-2n-2)/N. Consequently
E(X_u X_v)= 1_(u=v)+1_(v=u+1)+2n/N+(N-2n-2)/N
= 1_(u=v)+1_(v=u+1)+1-2/N.
Subtracting E X_u E X_v=1 proves the covariance formula. Translation of the root by 1 flips all path edge colors, yielding X_w=X_(w+1).

**Theorem 2 (Poisson-one law with quantitative error).** For every n>=3, every pi, and every target w, the total variation distance between X_w and a Poisson random variable with mean one satisfies
d_TV(Law(X_w),Poisson(1)) <= (8n+4)/2^n.
Consequently Pr(X_w>0) = 1-e^(-1)+O(n/2^n), with the absolute error bounded by (8n+4)/2^n.

**Proof.** For each root x set A_x=1_(W_pi(x)=w). This is a Bernoulli variable with mean 1/N, and X_w=sum_x A_x. It depends only on the n orbit bits along the prescribed path. The other A_y sharing any orbit bit are among the 2n+1 roots x+1, x+e_i, x+1+e_i. Hence a valid dependency neighborhood B_x consists of these roots and x, size 2n+2. Outside B_x, A_x is independent jointly of all other A_y because their defining orbit-bit sets are collectively disjoint from its own.

In the Stein--Chen dependency-graph Poisson approximation bound
d_TV <= 2(b1+b2)
when b3=0, one has
b1=sum_x sum_(y in B_x) E A_x E A_y = (2n+2)/N.
Among y in B_x minus {x}, only y=x+e_i can occur jointly with A_x, each with probability 2/N^2; the n roots x+1+e_i and x+1 give contradictory shared-orbit color requirements. Thus
b2=sum_x sum_(y in B_x minus {x}) E(A_x A_y)=2n/N.
Substituting proves the displayed bound.

**Theorem 3 (profile support concentration).** The number S_pi of distinct target profiles attained using the fixed direction order pi satisfies
|E S_pi -(1-e^(-1))N| <= 8n+4.
For every real t>0,
Pr(|S_pi-E S_pi|>=t) <= 2 exp(-t^2/(2nN)).
In particular S_pi/2^n converges in probability, as n grows, to 1-e^(-1), with deviations epsilon having probability exponentially small in 2^n/n.

**Proof.** Directionwise color complements act transitively on target profiles and preserve the uniform coloring distribution. Therefore E S_pi =sum_w Pr(X_w>0) =N Pr(X_0>0), and Theorem 2 supplies the expectation bound.

The random coloring is generated by M=nN/4 independent fair edge-orbit bits. For a fixed order pi, any specified edge orbit is visited by just four rooted full paths, with roots of the form x,x+e_i,x+1,x+1+e_i. Flipping this orbit bit changes four profile outputs, so it can change their support size S_pi by at most four. The bounded-difference (McDiarmid) inequality with M variables and sensitivity four gives
Pr(|S_pi-E S_pi|>=t)<=2exp(-2t^2/(16M))=2exp(-t^2/(2nN)).
Combining the expectation and concentration bounds proves the limit.

**Corollary (typical complete interaction).** The full directed influence graph of a uniform legal coloring is complete with probability at least 1-n(n-1)2^(-2^(n-3)), as already established in note_5739508f9d16ac93522b9c9c. Hence the fixed-order Poisson and 1-e^(-1) support phenomena hold with asymptotically probability one even among colorings with complete directed influence. The statistical claim concerns the random full-class distribution, not a deterministic theorem asserting that every coloring has a monochromatic path in the fixed order.

**Finite census and verification.** All 65,536 legal Q4 colorings were enumerated for the direction order (0,1,2,3), giving the histogram for X_0:
X_0=0:22416 colorings; 1:26064; 2:12576; 3:3616; 4:848; 5:16.
This gives E X_0=1, Var(X_0)=7/8, Cov(X_0,X_1)=-1/8, and Cov(X_0,X_15)=7/8, confirming the formula. The distribution differs from the binomial occupancy model at higher moments, confirming the qualification in Theorem 1. Independent random legal colorings sampled in Q6,Q8,Q10 gave mean fractions of fixed-order profiles 0.6376, 0.6328, 0.6325 respectively, converging toward 1-e^(-1) approximately 0.63212. Reproducible verifier: /mnt/data/nori_fixed_order_poisson_verifier.py.

**Relevance to NORI1.** This produces a quantitative global law for the unrestricted ensemble without linearity, locality, or other coloring restrictions. For a single prescribed order the chance of obtaining a red full geodesic converges to 1-e^(-1); the same chance applies to a blue path and the red/blue witness counts agree by antipodal translation. Thus a single-order witness exists with positive limiting probability but not with probability tending to one. The main open conjecture asks for an appropriate order for every fixed legal coloring. Correlations between different direction orders, rather than within-order first or second moments, are the remaining obstruction to upgrading this probabilistic result to a deterministic proof.

THEOREM 4 (full empirical Poisson multiplicity spectrum). Fix a direction permutation pi and choose a legal antipodally odd coloring uniformly at random. Put N=2^n, X_w=number of roots realizing profile w, and H_k=number of targets w having X_w=k. For every nonnegative integer k:
|E H_k - N exp(-1)/k!| <= 8n+4,
and for all t>0:
Pr(|H_k-E H_k|>=t) <= 2 exp(-t^2/(8nN)).
Consequently the probability distribution H_k/N on nonnegative integers converges in probability in total variation to Poisson(1) as n grows. Thus proportions of profiles attained from zero, one and two roots tend to exp(-1), exp(-1), exp(-1)/2 respectively.

PROOF. Every target w has the same distribution of X_w by independent directionwise output complementation. Hence E H_k=N Pr(X_0=k), and the earlier Stein-Chen theorem supplies the stated expectation error. Changing the color of one antipodal edge orbit changes only four rooted profiles in the fixed direction order. Altering one rooted profile changes H_k by at most two, so the bounded-difference sensitivity is eight per orbit. There are nN/4 independent orbit bits. McDiarmid's inequality gives Pr(|H_k-E H_k|>=t) <=2 exp(-2t^2/(64*nN/4)) =2 exp(-t^2/(8nN)). Thus for every fixed k, H_k/N converges in probability to exp(-1)/k!, with exponential concentration.

To obtain convergence of the entire histogram, note for every coloring sum_k H_k=N and sum_k k H_k=N. Consequently sum_(k>K) H_k/N <=1/(K+1) for each integer K>=1. The Poisson law also has a vanishing tail. Choose K large to control both tails and use the finite union bound on k<=K to conclude convergence in total variation.

SCOPE. The empirical multinomial resemblance is a rigorous Poisson limit despite dependencies between rooted path profiles. This is a full-ensemble probabilistic theorem, not a proof of deterministic NORI1.
