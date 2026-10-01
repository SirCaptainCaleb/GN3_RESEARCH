# Special-edge accounting criterion and the two-thirds ceiling of unweighted snake counting

## Statement

Let H be an n-vertex P_ell-free linear 3-graph with m edges and s special edges in the snake digraph. Then 2m+s <= (2ell-3)n. Hence if s>=epsilon m-Cn for fixed epsilon>0, then m <= ((2ell-3+C)/(2+epsilon))n. Any fixed positive special-edge density improves the leading coefficient below 1, while unchanged unweighted snake-incidence counting cannot cross the 2/3 leading coefficient.

## Body

Let b=m-s. Every nonspecial edge contributes exactly two snake incidences and every special edge contributes three, so |E(D)|=2b+3s=3m-b=2m+s. Since H is P_ell-free, phi(v)<=ell-1, and the snake indegree lemma gives d_D^-(v)<=2ell-3. Summing gives 2m+s<=(2ell-3)n.

If s>=epsilon m-Cn, then (2+epsilon)m-Cn<=(2ell-3)n, yielding m<=((2ell-3+C)/(2+epsilon))n. Since always s<=m, the strongest lower bound on 2m+s available from special-edge counting alone is 3m. Thus the unchanged scheme bottoms out at leading coefficient 2/3, attained asymptotically when b=O(n). Reaching one third requires additional charging, stronger indegree information, weighting, or a different global mechanism.
