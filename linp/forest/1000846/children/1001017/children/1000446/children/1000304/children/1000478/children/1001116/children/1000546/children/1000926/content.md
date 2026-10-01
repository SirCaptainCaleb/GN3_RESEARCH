# A bounded excess over host prefixes gives logarithmic-plus-excess contact degree

## Statement

For distinct edges f={x_f,v,u_f} in a finite linear 3-graph, let P be a p-edge path with last vertex v, with f outside P and f intersecting V(P) exactly in {v,x_f}. Let a_f be the first host occurrence of x_f and sigma_f=phi(x_f)-a_f. For every integer s>=0, #{f:sigma_f<=s}<=4s+7+4 floor(log_2(p+2)). The underlying separated-contact recurrence is D_i>=2D_{i+1}+2-sigma_{i+1}. Hence uniformly sublinear prefix excess implies sublinear degree. If k contacts are present and m=(k-7-4 floor(log_2(p+2)))_+, then sum_f sigma_f>=m(m+1)/8.

## Body

Let H be a finite linear 3-graph, let P=(g_1,...,g_p) be a linear path with last vertex v, and let F be distinct edges f={x_f,v,u_f} not used by P such that f intersects V(P) exactly in {v,x_f}. Write a_f and b_f for the first and last indices of P-edges containing x_f. Then b_f is a_f or a_f+1. Put sigma_f=phi(x_f)-a_f, which is nonnegative because the prefix through g_{a_f} can end at x_f. No maximality of P is assumed.

Fix an integer s>=0, and restrict to edges with sigma_f<=s. Distinct such edges have distinct x_f by linearity. At most three contact vertices have first occurrence in g_1; discard them. At every remaining first-occurrence index there is at most one private vertex and at most one forward joint. Partition the remaining contacts into four classes according to private versus joint and the parity of a_f. Within one class write the first indices as a_1<...<a_k; successive indices differ by at least two.

For 1<=i<=k-2, take the path
  g_1,...,g_{a_i}, f_i, f_k, g_{a_k},g_{a_k-1},...,g_{b_{i+1}}.
This is linear. The prefix and suffix are separated by at least one omitted host edge, since b_{i+1}>=a_{i+1}>=a_i+2. Each inserted edge has just its specified source contact on the host besides v, while v occurs only in g_p, which is omitted. The inserted edges meet only at v. A joint contact x_i has its second occurrence in g_{a_i+1}, outside the suffix; a joint contact x_k has its second occurrence in g_{a_k+1}, outside the suffix. The final vertex x_{i+1} occurs in the last edge g_{b_{i+1}} and not in its predecessor, and by linearity it belongs to neither inserted edge. Thus this is a path with last vertex x_{i+1}.

Its length is a_i+a_k-b_{i+1}+3. Maximality in the definition of phi(x_{i+1}) gives
  a_i+a_k-b_{i+1}+3 <= a_{i+1}+sigma_{i+1}.
Set D_i=a_k-a_i. Since b_{i+1}<=a_{i+1}+1, this implies the exact recurrence
  D_i >= 2D_{i+1}+2-sigma_{i+1}.                 (1)
For a private middle contact the constant 2 improves to 3.

Let m be the number of indices among 1,...,k-1 for which D_i>=s. These are the initial m indices. For those indices put E_i=D_i-s+2, so E_i>=2. Equation (1) and sigma_{i+1}<=s imply E_i>=2E_{i+1}. If m>=1, then E_1>=2^m. Since E_1<=p+2, we have m<=floor(log_2(p+2)). There are at most s other indices among 1,...,k-1, since their distinct nonnegative integer deficits are less than s. Adding the last index gives
  k <= s+1+floor(log_2(p+2)).
Summing over the four classes and restoring the at most three discarded contacts proves
  #{f in F: sigma_f<=s} <= 4s+C_p,
  C_p=7+4 floor(log_2(p+2)).                     (2)

Consequently, if every sigma_f<=s(p)=o(p), then |F|=o(p). For fixed s, the bound is logarithmic. More generally, if k=|F| and the sigma values are ordered increasingly, (2), applied at s=sigma_(i), gives sigma_(i)>=(i-C_p)/4 for i>C_p. With m=(k-C_p)_+, summation yields
  sum_f sigma_f >= m(m+1)/8.                    (3)

Application to the paid strict-gap class. Partition any such family at v into U, whose unique host contact is its opposite terminal, and X, whose unique host contact is its entrance x. For f in X, ascendingness gives
  sigma_f=phi(f)-1-a_f.
All hypotheses of (2) hold for X, independently of the paid certificate. Thus, for every integer s>=0,
  |F| <= |U| + #{f in X:sigma_f>s} + 4s+C_p.    (4)
For |F|>=epsilon p, choose s=floor(epsilon p/16). Either |U|>=epsilon p/2, or at least epsilon p/4-C_p source contacts have sigma_f>s. Thus a linear-sized obstruction must have linearly many opposite-terminal contacts or linearly many entrance contacts with linear excess over their visible host prefixes. This is a reduction, not a proof that either remaining class is small.

Strengthening check. The proof uses neither ascendingness nor source-cleanliness, neither the opposite terminal's rank nor terminal-singleness there, and neither payment nor maximum length of the host. The general statement deliberately omits those hypotheses. The project-specific interpretation uses ascendingness only to replace phi(x_f) by phi(f)-1.