# A unique intersection of two maximum endpoint paths is an aligned joint

## Statement

Let Q=(e_1,...,e_a) and R=(f_1,...,f_b) be maximum endpoint paths ending at distinct vertices x and y, with phi(x)=a and phi(y)=b. If V(Q) intersect V(R)={w}, then w is a joint on both paths at the same index: there exists t with 1<=t<min(a,b) such that w=e_t intersect e_{t+1}=f_t intersect f_{t+1}. No hypothesis relating a and b is needed.

## Body

Let i and ell be the first and last edge indices of Q containing w, and let k and j be the first and last edge indices of R containing w. Because Q and R have only w in common, the splice e_1,...,e_i,f_j,...,f_b is a linear path ending at y. Its length is i+b-j+1, so maximality at y gives j>=i+1. Conversely f_1,...,f_k,e_ell,...,e_a is a linear path ending at x, of length k+a-ell+1, so maximality at x gives ell>=k+1. In a linear path a vertex belongs either to one path edge or to two consecutive path edges. If w belonged to only one edge of Q, then ell=i, hence k<=i-1; but j<=k+1<=i, contradicting j>=i+1. Thus w is a Q-joint and ell=i+1. Similarly, if w belonged to only one edge of R, then j=k; the two inequalities would give k>=i+1 and k<=i, impossible. Hence w is also an R-joint and j=k+1. Substitution gives k>=i and i>=k, so k=i. Therefore w=e_i intersect e_{i+1}=f_i intersect f_{i+1}. This also shows why the previously stated endpoint exception was spurious: when w is a last vertex, the opposite prefix can still be followed by the last edge of that endpoint path, gaining one edge and contradicting maximality.
