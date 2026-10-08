# Theorem 8 — preserved pre-item development

If
\[
\frac{|E(H)|}{|V(H)|}>\frac{\ell}{3},
\]
then the binary incidence code of \(H\) contains a word of weight \(\ell+2\).

#### Proof
Pass to the \(>\ell/3\)-core. It is nonempty, has the same or larger density, and has minimum degree greater than \(\ell/3\). Its average degree exceeds \(\ell\), so some vertex \(v\) has degree at least \(\ell+1\). The edges through \(v\) form a linear star, whose \(2d\) vertices outside \(v\) are all distinct.

The sum of \(k\) star edges has weight \(2k\) when \(k\) is even and \(2k+1\) when \(k\) is odd.

If \(\ell\equiv2\pmod4\), take \(k=(\ell+2)/2\). If \(\ell\equiv1\pmod4\), take \(k=(\ell+1)/2\). These give the required weight directly.

If \(\ell\equiv0\pmod4\), choose an edge \(f\) not containing \(v\). It meets at most three star edges. Choose
\[
k=\frac{\ell-2}{2}
\]
star edges disjoint from \(f\); their sum has weight \(\ell-1\), and adding \(f\) gives weight \(\ell+2\).

If \(\ell\equiv3\pmod4\), choose a star edge \(e=\{v,a,b\}\) and another edge \(f\ne e\) through \(a\). Choose
\[
k-1=\frac{\ell-1}{2}
\]
further star edges disjoint from \(f\). The sum of these \(k\) star edges has weight \(\ell+1\), and adding \(f\), which meets the support exactly in \(a\), changes the weight to \(\ell+2\). ∎

Therefore a code construction must use more information than the absence of one support size.
