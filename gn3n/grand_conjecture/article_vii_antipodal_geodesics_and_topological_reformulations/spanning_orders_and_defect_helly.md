# Spanning orders and defect Helly theory

## Inversion windows, positive witnesses, and minimum holes

For a spanning order \(\pi\), let \(p(\pi)\) be the first non-tight status and \(q(\pi)\) the last tight status. The two-cover problem is equivalent to the single inequality
\[
q(\pi)\le p(\pi)+1.
\]
Thus
\[
\operatorname{pc}(H)\le2
\iff
\exists\pi\quad q(\pi)\le p(\pi)+1.
\]
The corresponding order-level deficiency
\[
d_2(\pi)=\max\{0,q(\pi)-p(\pi)-1\}
\]
has the global interpretation
\[
\boxed{\kappa_2(H)=\min_\pi d_2(\pi)}.
\]

Failure is local: an order has positive deficiency if and only if its status word contains one of
\[
\mathcal W_+=\{001,011,0101\}.
\]
These witnesses use at most six consecutive vertices and are closed under reverse-complement.

Minimum deletion sets carry substantially more structure. If \(|X|=\kappa_2(H)\) and \(H-X=P\mid Q\), then every \(Y\subseteq X\) satisfies
\[
\kappa_2(H-(X\setminus Y))=|Y|.
\]
In particular no nonempty subfamily of \(X\) can be absorbed into \(P\) and \(Q\), even after splitting that subfamily between the two sides. This hereditary exactness is the deletion-theoretic invariant used throughout the remainder of the article.
