# Root-slide-invariant twisted switch filtration and uniform quadratic exchange defects

# Twisted switch count: cyclic root slides and quadratic exchange defects

This subsection extends the switch-deformation and Coxeter exchange work in Article XIV, Subsections 53 and 55. The ordinary switch count has linear-order endpoint exceptions. A root-slide-invariant antiperiodic count removes those exceptions, providing a uniform square-exchange formula and a local rigidity theorem for minimum-switch antipodal geodesics.

Let \(n\ge3\) and let \(c\) be any antipodally odd binary edge coloring of \(Q_n\). For a full rooted dimension-simple geodesic flag \(g=(x;d_1,\ldots,d_n)\), let \(w(g)=(w_1,\ldots,w_n)\) be its edge-color word. Define its **twisted cyclic switch count**
\[
\boxed{\sigma(g)=\sum_{j=1}^{n-1}[w_j\ne w_{j+1}]+[w_n=w_1],\qquad
h(g)=\frac{\sigma(g)-1}{2}.}
\tag{1}
\]
The last comparison is between \(w_n\) and the *complement* of \(w_1\), so the indicator of a change is \([w_n=w_1]\).

**Theorem 1 (root-slide invariance).** The count \(\sigma(g)\) is positive and odd, \(h(g)\) is a nonnegative integer, and
\[
\boxed{\sigma(Tg)=\sigma(g)=\sigma(\tau g),}
\tag{2}
\]
where the root slide \(T\) replaces the word by
\((w_2,\ldots,w_n,1-w_1)\) and \(\tau\) antipodally translates the flag. Furthermore
\[
\boxed{h(g)=0\iff\text{some }T^jg\text{ is monochromatic}.}
\tag{3}
\]
Thus NORI1 is equivalent to \(\min_g h(g)=0\).

*Proof.* The mod-two sum of comparisons around the antiperiodically closed word is one; hence their integer sum is odd. Rotating the twisted cycle preserves the comparisons and gives (2). If only one twisted comparison changes, choose the root-slide window cut there: all \(n\) colors in that window coincide. Conversely a monochromatic word has only the twisted seam change. \(\square\)

**Theorem 2 (uniform Lipschitz law for every dimension exchange).** Let \(g'\) be obtained by interchanging the dimensions at adjacent positions \(j,j+1\), \(1\le j<n\). Let \(pq\), respectively \(rs\), be the two edge-color pairs for the original and exchanged routes. Define flanking bits
\[
A=\begin{cases}w_{j-1},&j>1,\\1-w_n,&j=1,\end{cases}
\qquad
B=\begin{cases}w_{j+2},&j<n-1,\\1-w_1,&j=n-1.\end{cases}
\tag{4}
\]
For \(G(A,p,q,B)=[A\ne p]+[p\ne q]+[q\ne B]\), one has
\[
\boxed{\sigma(g')-\sigma(g)
=G(A,r,s,B)-G(A,p,q,B)\in\{-2,0,2\}.}
\tag{5}
\]
In particular \(\boxed{|h(g')-h(g)|\le1}\), including the exchanges at positions \(1,2\) and \(n-1,n\).

*Proof.* Every edge color outside the exchanged two-edge route is unchanged. The only altered twisted comparisons are the three in (4)–(5). Each local comparison count has parity \(A\oplus B\), independently of the route, and lies between zero and three. Thus their difference is zero or plus/minus two. \(\square\)

**Theorem 3 (uniform quadratic defect for twisted Freudenthal chains).** For each rooted cubical \(d\)-face, \(d\ge3\), weight its complete Freudenthal simplex \(\sigma_\pi\) by \((1+u)^{\sigma(\pi)}\), with \(\sigma(\pi)\) the twisted switch count of that face's ordered color word:
\[
\mathfrak F^{\rm tw}_u(F,x)=\sum_\pi(1+u)^{\sigma(\pi)}\sigma_\pi
\quad\text{over }\mathbb F_2[u].
\tag{6}
\]
An internal facet shared by two neighboring dimension orders has coefficient zero when their twisted switch counts agree, and otherwise has coefficient
\[
\boxed{u^2(1+u)^{\min(\sigma,\sigma')}.}
\tag{7}
\]
Therefore *every internal facet cancels modulo \(u^2\)*, without the endpoint exceptions present for the ordinary switch deformation in Subsection 55.

For local two-edge route bits \(pq\) and \(rs\), and flanking bits \(A,B\) chosen as in (4), the quadratic coefficient of the defect is
\[
\boxed{
A(p\oplus r)+B(q\oplus s)
+(p\oplus q\oplus r\oplus s)+pq+rs
\pmod2.
}
\tag{8}
\]
It equals one precisely when the twisted switch count changes by two. Moreover
\[
\boxed{(1+u)^\sigma=(1+u)(1+u^2)^h.}
\tag{9}
\]
This identifies \(h\) as the root-slide-invariant integer defect relevant to the quadratic order.

*Proof.* Equation (5) shows that the two exponents differ by zero or two. In characteristic two,
\((1+u)^{r+2}+(1+u)^r=u^2(1+u)^r\), proving (7). To find the quadratic coefficient, subtract the two local three-comparison counts from the common unaffected comparisons. Equal parity of the local counts cancels the common contribution to the second binomial coefficient. Expanding their remaining \(\binom G2\) terms over \(\mathbb F_2\) gives (8). It is the six-bit expression previously found for interior exchanges, now valid also at the two ends using the twisted flanks. Equation (9) follows from \(\sigma=2h+1\). \(\square\)

**Theorem 4 (gate rigidity for cyclic switch minimizers).** Choose \(g\) minimizing \(h\) over all full rooted geodesics. For every adjacent exchange, with \(A,p,q,B\) as above:

- If \(G(A,p,q,B)=3\), then the alternative route satisfies \((r,s)=(p,q)\). Thus **both routes through the exchanged square have the same alternating bit word**, a gate \(10,10\) or \(01,01\).
- If \(G(A,p,q,B)=2\), then \(A=B=t\) and the alternative route cannot be \((t,t)\).
- If \(G=0\) or \(1\), no adjacent exchange can decrease \(h\).

These two restrictions for \(G=3,2\) also characterize local nondecrease under all adjacent dimension swaps from a given flag.

*Proof.* A global minimizer cannot admit a swap lowering \(\sigma\) by two. If \(G=3\), then \(A\ne B\), and the unique two-bit route achieving all three comparison changes is \((p,q)=(1-A,A)\); every other route has one change, contradicting minimality. If \(G=2\), then \(A=B=t\), and the unique route with zero changes is \((t,t)\). These are the only possibilities for a decrease, since zero and one are already minimal comparison counts at their respective parities. \(\square\)

**Interpretation and limitations.** Unlike the ordinary switch number, the twisted defect is invariant under root slides and its adjacent-exchange variation has no distinguished endpoints. This allows a single local quadratic formula across the complete cyclic flag geometry. But since \(\sigma\) is always odd, the weights \((1+u)^\sigma\) agree modulo \(u^2\); the first-order cancellation by itself is a normalization, not a proof of NORI1. The uniform defect is the relevant input for a root-slide-compatible switch filtration or Rees-chain construction that couples multiple roots and controls the projective obstruction. The unproved step is showing these local constraints force some flag with \(h=0\).
