# Longest-path pair-capacity reduction with outside extremal defect

## Statement

Assume the target inequality 3m<=ell n is being proved inductively for P_ell-free linear 3-graphs. Let H be a minimal counterexample candidate, let P be a longest k-edge linear path, put X=V(P), Y=V(H)\X, m_Y=|E(H[Y])|, and e_X=|E(H)|-m_Y. Define the outside defect D_Y=ell|Y|-3m_Y, which is nonnegative by the inductive hypothesis. Then 3|E(H)|<=ell|V(H)| is equivalent to
3e_X <= ell|X|+D_Y.
Since |X|=2k+1,
ell|X| = binom(|X|,2)+(ell-k)|X|.
Hence it is enough, and under the inductive hypothesis equivalent, to prove
3e_X <= binom(|X|,2)+(ell-k)|X|+D_Y.
In the saturated case k=ell-1 this becomes
3e_X <= binom(|X|,2)+|X|+D_Y.

## Body

By the inductive hypothesis applied to H[Y], D_Y=ell|Y|-3m_Y>=0. Writing m=m_Y+e_X, the desired inequality 3m<=ell(|X|+|Y|) is equivalent to
3e_X <= ell|X| + ell|Y|-3m_Y = ell|X|+D_Y.
A k-edge linear 3-uniform path has |X|=2k+1 vertices, so
binom(|X|,2)=k(2k+1)=k|X|.
Therefore
ell|X|=binom(|X|,2)+(ell-k)|X|,
which gives the displayed pair-capacity form. No structural claim about how to realize this charge is asserted here; the value of the reduction is that it isolates the exact local payment problem around one longest path. Internal pairs of X provide binom(|X|,2) units, the path-length slack provides (ell-k)|X| further units, and any unused extremal capacity of H[Y] appears exactly as D_Y.