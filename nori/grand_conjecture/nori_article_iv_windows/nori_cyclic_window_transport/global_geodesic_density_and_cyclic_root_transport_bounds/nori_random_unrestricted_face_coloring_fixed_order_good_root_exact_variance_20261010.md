# Random unrestricted NORI coloring: exact variance and high-probability good roots for every fixed direction order

# Exact second-moment concentration: random unrestricted NORI colorings have good roots for any prescribed direction order

Let n>=5 and fix ANY permutation p=(p_1,...,p_n) of the coordinate directions. Choose a legal antipodally reversal-odd coloring of ALL physical ORDERED three-faces of Q_n uniformly at random: select independent fair bits on the 3*binom(n,3)*2^(n−3) orbits of (F,t)↦(bar F,reverse t), and determine each paired orbit member by opposite color.

For every cube root x let W(x) be the genuine (n−2)-letter ordered-three-face word of its full n-edge antipodal geodesic in the FIXED order p. Set L=n−2, N=2^n, and define X=sum_x 1[W(x) has at most one change], and M=sum_x 1[W(x) is monochromatic].

**THEOREM (exact moments and high-probability fixed-order closure).**
E[X]=8(n−2), E[M]=8.

Write q=2L/2^L, and
r_2=2*((L−1)^2+1)/L^2,
r_3=4*((L−2)^2+2)/L^2.
Then the EXACT variances are

Var(X) = N*q*(1−q) + N*q^2*((n−1)*(r_2−1)+(n−4)*(r_3−1)),

Var(M) = 8+64*(4n−14)/2^n.

Consequently
  P(X=0) <= 1/(8(n−2)) + (4n−14)/2^n,
so the probability that this FIXED direction order admits at least one genuine good full antipodal geodesic approaches 1, with failure probability O(1/n). In fact, X/(8(n−2)) converges in probability to 1 as n→∞. This holds with completely unrestricted nonlinear dependence on the actual exterior-face bits.

**Proof of single-root distribution.** The n−2 forward ordered direction triples t_i=(p_i,p_(i+1),p_(i+2)) are distinct, and none is the reverse of another. For one fixed root x, their actual physical face colors therefore occupy distinct antipodal-reversal orbits. Thus W(x) is a uniform word in F_2^L. There are precisely 2L binary length-L words with at most one switch and two constant words. Accordingly q=P(W(x) good)=2L/2^L, giving E[X]=Nq=8L and E[M]=N*2/2^L=8.

**Root-pair dependency classification.** Let S be the set of coordinate positions where two distinct starting roots x,y differ. For the i-th ordered window, the physical face addressed from x equals that addressed from y exactly when S⊆{i,i+1,i+2} in direction-position notation, since the window's three free-coordinate root bits are invisible and prefix flips act identically on both roots. Distinct forward indices never share an antipodal-reversal orbit. Thus the two random color words are two independent uniform length-L words conditioned to agree at exactly
    k(S)=|{i: S⊆{i,i+1,i+2}}|
corresponding positions, and are independent if k(S)=0.

There are exactly:
- n−4 nonzero differences S for which k=3 (one interior coordinate position);
- n−1 nonzero S with k=2 (two near-end singleton positions, plus n−3 adjacent interior pairs);
- 2n nonzero S with k=1 (two endpoint singles, two endpoint adjacent pairs, n−2 pairs at distance two, and n−2 consecutive triples).
Every other S has k=0. The total number of potentially overlapping nonzero root differences is 4n−5.

**Exact good-word correlations.** For two independent uniform binary L-words conditioned to agree on k consecutive positions, let P_k be the probability that BOTH are good. For k=1, complement symmetry of the good-word set gives P_1=q^2, so sharing exactly one window bit leaves the two good indicators independent.

For k=2, the numbers of good words having any prescribed pair of consecutive bits 00,11,01,10 are respectively L−1,L−1,1,1. The number of compatible ordered pairs of good words is therefore C_2=2*((L−1)^2+1). As the conditioned joint sample space has 2^(2L−2) equally likely outcomes,
    P_2=C_2/2^(2L−2)=r_2*q^2.

For k=3, the corresponding counts for 000,111 are L−2,L−2; each of 001,011,100,110 occurs exactly once, and 010,101 never occur. Hence C_3=2*((L−2)^2+2),
    P_3=C_3/2^(2L−3)=r_3*q^2.

The analogous mono-word probabilities are P_1^mono=q_mono^2, P_2^mono=2*q_mono^2, P_3^mono=4*q_mono^2.

**Variance computation.** In Var(X), for each of the N ordered choices of x there are n−1 choices of y with k=2 and n−4 with k=3. The k≤1 covariances vanish. Substitution gives the displayed exact formula. Substituting q_mono=8/N and the two mono ratios gives
 Var(M)=N*q_mono*(1−q_mono)+N*q_mono^2*((n−1)+3*(n−4))
       =8+64*(4n−14)/N.
Since r_2<=2 and r_3<=4, Chebyshev's inequality yields
 P(X=0)<=Var(X)/(8L)^2
         <=1/(8L)+(4n−14)/N.
The relative variance tends to zero, proving concentration. QED.

**Research implication.** For random unrestricted physical NORI colorings, one fixed direction order has linearly many good roots with high probability; difficulties are driven by exceptional structured colorings whose root-words correlate far more strongly than independent face-orbit bits. Contrast Item nori_even_paired_root_exact_arbitrary_face_fiber_chart_universality_20261010: using only 2^(n/2) paired roots on one fixed order has expected (n−2)*2^(3−n/2) good paths and hence typically finds NONE, by Markov's inequality. Full root freedom changes the fixed-order witness expectation from exponentially small to 8(n−2).

This is a probabilistic theorem about generic colorings; the universal NORI conjecture for every legal coloring remains open. A decisive deterministic extension would convert the identified O(n)-degree root-compatibility graph into a path-extraction principle robust under adversarial correlations.
