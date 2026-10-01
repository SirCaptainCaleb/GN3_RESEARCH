# A distance-one four-side endpoint replacement gives a neutral support swap or a full-path lock

## Statement

Let H be a boundary tournament and let W|P|Q be a spanning three-cover, where |W|=4 and P=(p_1,...,p_m) is a displayed tight path. Let e be either displayed endpoint of P and w in W. Suppose W'=(W-{w}) union {e} is Hamiltonian. Put R=V(P)-{e}, with its inherited displayed path. Then either H[R union {w}] is Hamiltonian, in which case W|P can be legally repartitioned as W' | (R union {w}) with exactly the same component orders 4,m and hence the same quadratic potential, or H[R union {w}] is non-Hamiltonian. In the latter case w is not insertable at any position of the inherited path R.

## Body

The support sets W' and R union {w} are disjoint and partition V(W) union V(P). If R union {w} is Hamiltonian, choose Hamilton paths on W' and R union {w}; replacing W|P by these two paths is one legal pairwise repartition. Their orders remain 4 and m, so Phi is unchanged. Otherwise R union {w} is non-Hamiltonian. If w were insertable anywhere into the inherited tight path R, that insertion would itself be a Hamilton path on R union {w}, contradiction. Thus w is noninsertable into the entire displayed inherited path R.