# Terminal-retained source mass pays quadratically for left-right contact imbalance

## Statement

Let P=(g_1,...,g_p) be a maximum p-edge path ending at v, and let U be a family of ascending nonspecial terminal-only singleton edges
      e_i={x_i,v,u_i},
    where x_i is the unique entrance, x_i is absent from P, and u_i is the unique off-v contact with P.

For each i let a_i be the first path-edge index containing u_i. Define
      k_- = |{i: a_i < (p-1)/2}|,
      k_+ = |{i: a_i > (p-1)/2}|,
      k=|U|,
    with contacts exactly at the midpoint (possible only when p is odd) placed in neither side.

Then
      sum_i phi(x_i)
      >= (p/2)k + k^2/8 + (k_- - k_+)^2/8.

Combining with c48823eea604, one may sharpen this to
      sum_i phi(x_i)
      >= (p/2)k + k^2/8
         + max{k/8,(k_- - k_+)^2/8}.

Consequently, for any sequence with k=Theta(p), if the terminal-retained entrance-potential mass is within o(p^2) of the quadratic minimum (p/2)k+k^2/8, then
      k_- - k_+ = o(p).
Thus a near-minimal terminal-retained packet must be asymptotically balanced across the two halves of its host path.

## Body

Let e_i have rank r_i. By the terminal-only singleton localization 028c2c3f7167,
      p-r_i+1 <= a_i <= r_i-2.
Since phi(x_i)=r_i-1, these two inequalities give
      phi(x_i) >= p-a_i
and
      phi(x_i) >= a_i+1.
Hence
      phi(x_i)
      >= max{p-a_i,a_i+1}
      = (p+1)/2 + |a_i-(p-1)/2|.                (1)

Because every e_i contains v, linearity makes the terminal contacts u_i distinct. For every internal first-occurrence index a>=2, at most two vertices of P have first occurrence a: the private vertex of g_a and the forward joint g_a intersect g_{a+1}. The terminal-only window has a_i>=2, so each integer first-occurrence index supports at most two members of U.

Consider the contacts strictly left of c=(p-1)/2. Among k_- distinct contacts with multiplicity at most two per integer index, the minimum possible sum of distances c-a_i is obtained by filling the nearest indices to c, two at a time. Whether c is integral or half-integral, this minimum is at least k_-^2/4. Similarly,
      sum_{a_i>c}(a_i-c) >= k_+^2/4.
Summing (1) therefore gives
      sum_i phi(x_i)
      >= (p+1)k/2 + (k_-^2+k_+^2)/4.           (2)

Let k_0=k-k_--k_+. Midpoint contacts exist only if c is an integer, and then there are at most two of them, so 0<=k_0<=2. Put k'=k_-+k_+=k-k_0 and d=k_--k_+. Since
      k_-^2+k_+^2=(k'^2+d^2)/2,
(2) becomes
      sum_i phi(x_i)
      >= (p+1)k/2 + k'^2/8+d^2/8.
For k_0=0,1,2 one checks
      (p+1)k/2+k'^2/8 >= (p/2)k+k^2/8;
indeed the difference is respectively k/2, k/4+1/8, and 1/2. This proves
      sum_i phi(x_i)
      >= (p/2)k+k^2/8+d^2/8.

The independent cumulative-rank theorem c48823eea604 gives
      sum_i phi(x_i) >= (p/2)k+k(k+1)/8,
so taking the stronger of the two bounds yields the displayed max-form.

Finally, if k=Theta(p) and the left side differs from (p/2)k+k^2/8 by o(p^2), then d^2/8=o(p^2), hence d=o(p).