# Independent-window permutation packing makes affine NORI counterexamples exponentially rare

# Exponentially small probability of grand failure among uniformly random valid affine NORI colorings

Let n>=7. Consider the uniform affine-exterior active NORI ensemble: for each unordered three-coordinate set T={i,j,k}, and for one ordered triple orientation in each pair pi,rev(pi), choose independently/uniformly every coefficient on the n−3 exterior bits and the constant intercept; define the reversed orientation by c(bar F,rev pi)=1−c(F,pi). Choices corresponding to distinct UNORDERED triples T are independent. Each such choice yields a valid corner-independent antipodal-reversal-odd binary coloring of ordered physical three-faces.

Put
  t_n=1+floor((n−1)/6),
  q_n=1/8+(4n−14)/2^n.
For n>=7, 0<q_n<=5/16.

**Theorem 1 (packing of independent direction orders).** There are t_n FULL permutations pi^(1),...,pi^(t_n) of [n] such that their unordered consecutive length-three window supports
  W(pi)={ {p_j,p_(j+1),p_(j+2)} : j=1,...,n−2 }
are pairwise disjoint.

Proof. For any fixed triple T and uniformly random permutation pi, probability that its three elements occupy consecutive positions (in any order) is
  P(T in W(pi))= 3! (n−2)! / n! = 6/[n(n−1)].
Each already selected pi uses exactly n−2 distinct unordered triples. If k permutations with disjoint window-support families are already selected, the probability a fresh random permutation hits one of the <=k(n−2) used triples is bounded above by
  k(n−2) * 6/[n(n−1)].
For k<=floor((n−1)/6), this is at most (n−2)/n<1. Therefore some fresh permutation avoids ALL previously used triples. Begin with k=0 and iterate through k=floor((n−1)/6). This selects t_n permutations with mutually disjoint W. QED.

**Theorem 2 (exponential reliability).** For the above ensemble, the probability that the grand NORI conjecture FAILS is at most
   (q_n)^(t_n) <= (5/16)^(1+floor((n−1)/6)).
Equivalently, the proportion of these AFFINE exterior colorings having at least one FULL MONOCHROMATIC antipodal geodesic is at least
   1 − (1/8+(4n−14)/2^n)^(1+floor((n−1)/6)).
The right-hand failure bound behaves as (1/8)^(n/6+O(1)) as n→∞. Thus *asymptotically almost every* coloring of this uniform valid affine NORI ensemble obeys a STRICTLY STRONGER MONOCHROMATIC grand conclusion.

Proof. For a fixed pi, the random-affine full-rank theorem nori_random_affine_full_rank_fixed_permutation_probability_seven_eighth_20261008 gives P(rank M_pi<n−3)<=q_n. If the switch-map M_pi has rank n−3, the affine map to its n−3 color-change bits is onto, so EXACTLY eight roots yield zero switches along that full permutation. Because each M_pi is determined solely by the exterior coefficient vectors attached to ordered triples whose UNORDERED support lies in W(pi), and the t_n chosen W families are disjoint, the events {rank M_pi=n−3} for the packed permutations are mutually independent. Thus the chance that all t_n maps fail to have full rank is at most (q_n)^(t_n). Any GRAND counterexample would force all these maps to have deficient rank, since a full-rank one forces an actual monochromatic full antipodal geodesic. QED.

**Theorem 3 (simultaneously many certified good orders).** For each packed order, the event of full rank guarantees eight monochromatic starting roots, and 8(n−2) roots with <=1 change. These root/order witnesses across different permutations represent distinct directed geodesics. The number of successful packed orders stochastically dominates Binomial(t_n,1−q_n). Therefore, for any integer 0<=s<=t_n, the probability of at least s successful packed orders is >=P(Binomial(t_n,1−q_n)>=s). This provides quantitatively MANY witness orders, not merely one.

**Scope/guardrail.** This is a PROBABILISTIC counting theorem about uniform AFFINE exterior face colorings, not a proof that every affine or every unrestricted NORI coloring has a good path. An adversarial coloring can correlate/order-select low-rank switch maps in every packed order; the argument only shows that such correlation is extremely rare under the independent affine ensemble. The stronger original grand conjecture for arbitrary nonlinear physical ordered-three-face colors remains open.
