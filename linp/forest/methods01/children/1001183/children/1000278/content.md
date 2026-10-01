# Refined ascending-edge accounting

## Statement

Let A be the number of ascending nonspecial edges and let H_2 be the number of nonascending nonspecial edges e with unique entrance x satisfying φ(x)>2(φ(e)-1). Then 3m-A+H_2 <= Σ_v(2φ(v)-1) <= (2ell-3)n.

## Body

At x, let c(x) be the number of ascending edges with entrance x and h(x) the number counted by H_2. The joint budget gives d_H(x)<=2φ(x)-1+c(x)-h(x): every incident edge is either snake-incoming at x, nonascending with entrance x, or ascending with entrance x, and each strongly decreasing nonascending edge has blocker weight two rather than one. Summing over x gives 3m<=Σ_x(2φ(x)-1)+A-H_2. Since H is P_ell-free, φ(x)<=ell-1 for every x.