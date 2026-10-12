# Discrete Hodge stability and the asymptotically sharp two-thirds turn theorem

# Discrete Hodge stability and the asymptotically sharp two-thirds turn theorem

Let \(V_n\) denote the real functions on distinct ordered triples satisfying \(f(c,b,a)=-f(a,b,c)\). Use one representative of each reversal pair for the inner product, and write \(N=n\binom{n-1}{2}\), \(E=N(n-3)\). Recall from the preceding signed-adjacency theorem the self-adjoint operator
\[
(Af)(a,b,c)=\sum_{d\notin\{a,b,c\}}[f(b,c,d)+f(d,a,b)]
\]
with spectrum contained in \(\{-(n-2),-2,0,1,n-2\}\), for \(n\ge6\).

**Lemma 1 (minimum eigenspace).** The eigenspace at \(-(n-2)\) is
\[
\mathcal E_-=\{f_s(a,b,c)=s_{ab}-s_{bc}:s_{ab}=s_{ba},\quad
\sum_{b\ne a}s_{ab}=0\ \forall a\}. \tag{1}
\]
It has dimension \(n(n-3)/2\), and is contained in
\[
\mathcal G=\{f:f(a,b,c)=u_b(a)-u_b(c)\}, \tag{2}
\]
the direct sum of gradient spaces on the neighbor sets of the \(n\) centers.

*Proof.* For any \(f\in V_n\), set
\[
U_{ab}=\sum_{d\notin\{a,b\}}f(d,a,b),\quad
H_{ab}=\sum_{d\notin\{a,b\}}f(a,d,b),\quad
W_a=\sum_{c\ne a}U_{ca},
\quad \sigma(a,b,c)=f(a,b,c)+f(b,c,a)+f(c,a,b).
\]
Here \(H_{ba}=-H_{ab}\), \(\sigma\) is alternating, and \(\sum_{b\ne a}U_{ab}=0\). Rearrangement gives
\[
Af=f-\sigma+U_{ab}-U_{cb},\qquad
U(Af)_{ab}=W_a+H_{ab}-(n-2)U_{ba}. \tag{3}
\]
Suppose \(Af=-rf\), with \(r=n-2\). The second equation gives
\(H_{ab}=r(U_{ba}-U_{ab})-W_a\).
Antisymmetry of \(H\) forces \(W_a=-W_b\) for every \(a\ne b\), hence every \(W_a=0\).
From the first equation,
\[
(r+1)f(a,b,c)=\sigma(a,b,c)-U_{ab}+U_{cb}. \tag{4}
\]
Summing (4) over \(f(a,d,b)\), and using the zero row sums of \(U\) and
\(\sum_d\sigma(a,d,b)=-(U_{ab}-U_{ba}-H_{ab})\), yields
\((r+1)H_{ab}=H_{ab}\). Thus \(H=0\), so \(U\) is symmetric. Cyclically summing (4) then gives \((r+1)\sigma=3\sigma\). Since \(n\ge6\), \(\sigma=0\). Equation (4) becomes \(f(a,b,c)=(-U_{ab}+U_{bc})/(n-1)\), establishing (1) with \(s=-U/(n-1)\).
Conversely, the stated symmetric zero-row-sum \(s\) satisfies
\(U_{ab}=-(n-1)s_{ab}\), \(\sigma=0\), and consequently \(Af_s=-(n-2)f_s\) by (3). The \(n\) row-sum constraints on the \(\binom n2\) symmetric edge variables are independent, and \(s\mapsto f_s\) is injective, giving the dimension. \(\square\)

For an antisymmetric edge array \(z_{ac}\) on \(K_m\), write \(\operatorname{div}_a z=\sum_{c\ne a}z_{ac}\) and
\(\gamma_{acd}=z_{ac}+z_{cd}+z_{da}\).

**Lemma 2 (complete-graph Hodge identity).** Orthogonal projection onto the gradients \(z_{ac}=u_a-u_c\) satisfies
\[
(\Pi z)_{ac}=\frac{\operatorname{div}_a z-\operatorname{div}_c z}{m},\qquad
\sum_{\{a,c,d\}}\gamma_{acd}^{\,2}=m\|z-\Pi z\|^2. \tag{5}
\]
*Proof.* Expand the squares:
\(\sum_{\triangle}\gamma^2=m\sum_{\{a,c\}}z_{ac}^2-\sum_a(\operatorname{div}_a z)^2\).
The displayed projection has squared norm \(\frac1m\sum_a(\operatorname{div}_a z)^2\), proving (5). \(\square\)

**Theorem 3 (sharp asymptotic turn density with stability).**
Let \(b(a,b,c)\in\mathbb F_2\) satisfy \(b(c,b,a)=1-b(a,b,c)\). Among the \(E=n(n-1)(n-2)(n-3)/2\) legal-turn reversal orbits let \(D(b)\) be the number on which consecutive triple colors differ. At each center \(v\), interpret \(b(a,v,c)\) as a tournament orientation on the remaining \(n-1\) labels; let \(t_v\) be its number of directed cyclic triangles and \(T(b)=\sum_v t_v\). Then
\[
\boxed{\frac{D(b)}E\le
\frac23+\frac{n-2}{2(n-3)(n-1)}
-\frac{2(n-4)T(b)}{(n-1)E}.} \tag{6}
\]
In particular
\[
\boxed{\frac23\le\max_b\frac{D(b)}E
\le\frac23+\frac{n-2}{2(n-3)(n-1)},}
\qquad
\lim_{n\to\infty}\max_b\frac{D(b)}E=\frac23. \tag{7}
\]
The upper estimates apply to every induced \(m\)-label restriction with \(m\ge6\).

*Proof.* Put \(x(a,b,c)=(-1)^{b(a,b,c)}\). It is reversal-skew and \(\|x\|^2=N\). For every center \(v\), the triangle curl of the \(\{\pm1\}\)-edge array \(x(a,v,c)\) has square \(1\) on a transitive triangle and \(9\) on a cyclic triangle. Applying (5) with \(m=n-1\) separately at all centers yields
\[
\|x-\Pi_{\mathcal G}x\|^2
=\frac1{n-1}\left(n\binom{n-1}{3}+8T(b)\right)
=\frac{n(n-2)(n-3)}6+\frac{8T(b)}{n-1}. \tag{8}
\]
By Lemma 1, \(\mathcal E_-\subseteq\mathcal G\). Every eigenvalue of \(A\) other than \(-(n-2)\) is at least \(-2\). Thus
\[
\langle x,Ax\rangle\ge
-(n-2)N+(n-4)\|x-\Pi_{\mathcal G}x\|^2. \tag{9}
\]
Signed adjacency gives \(\langle x,Ax\rangle=2E-4D(b)\). Substituting (8) into (9) and simplifying proves (6) and the upper bound in (7).

For the matching lower bound, assign independent continuous real labels \(s_{uv}=s_{vu}\) to all edges of \(K_n\), and set
\[
(-1)^{b(a,b,c)}=\operatorname{sgn}(s_{ab}-s_{bc}).
\]
This is reversal-skew. For every legal quadruple \((a,b,c,d)\), the three labels \(s_{ab},s_{bc},s_{cd}\) are independent and identically distributed. The colors of the two overlapping triples differ precisely when the middle label is their minimum or maximum, an event of probability \(2/3\). Hence \(\mathbb E D(b)=2E/3\), so some edge ordering has \(D(b)\ge2E/3\). Finally every restriction retains reversal oddness and the argument applies with its own number of labels. \(\square\)

The stability term in (6) penalizes cyclic triangles in the local tournaments. The upper bound covers all reversal-odd boundary 3-tournaments, while the asymptotically extremal construction belongs to the edge-ordered subclass. The theorem is a global constraint on coloring-cycle support in the pointed binary turn matroid. Extracting a resource-simple long path still requires a cocircuit selector.

**Corollary 5 (abundance of six-resource low-intersection port cocircuits).**
Let \(n\ge6\), and consider the six-resource twisted-cycle construction in the preceding Subsection. For every injective ordered six-vertex word \(v=(v_1,\ldots,v_6)\), let \(Y_v=C_v\cup\{p\}\) be its seven-element marked port cocircuit and put
\[
w(v)=|X_b\cap Y_v|-1.
\]
The six-turn odd-monodromy construction gives \(w(v)\in\{1,3,5\}\). Then the proportion \(q_n(b)\) of injective words satisfying \(|X_b\cap Y_v|\le4\) obeys
\[
\boxed{
q_n(b)\ge
\frac14-\frac{3(n-2)}{4(n-3)(n-1)}
+\frac{3(n-4)T(b)}{(n-1)E_n}.
}\tag{16}
\]
In particular
\[
q_n(b)\ge\frac14-\frac{3(n-2)}{4(n-3)(n-1)}
=\frac14-O(n^{-1}).
\]
At \(n=6\) this recovers the established \(36/720=1/20\) uniform six-resource guarantee; as \(n\to\infty\) it gives a lower bound approaching one quarter of all ordered six-vertex words, independently of the coloring.

*Proof.* Each of the six edges of the marked turn cycle is uniformly distributed over the \(E_n\) legal-turn reversal orbits when \(v\) is uniformly distributed over injective ordered six-tuples. Hence
\[
\mathbb E_v w(v)=6D_n(b)/E_n.
\]
Writing \(q=\Pr(w\le3)\), the parity restriction \(w\in\{1,3,5\}\) gives
\[
\mathbb E_v w(v)\ge q\cdot1+(1-q)\cdot5=5-4q.
\]
Thus \(q\ge(5-6D_n(b)/E_n)/4\). Substitution of the stability bound (11) proves (16). \(\square\)

This is a global marked-cocircuit counting statement; the stronger assertion that every prescribed six-element resource set has at least one such cocircuit follows separately from the five-cycle averaging theorem.
