# Seven-coordinate wing factorization and exact obstruction

# A seven-coordinate wing decomposition

Fix a binary coloring \(c\) of ordered three-faces of \(Q_7\). No antipodal symmetry is required in this subsection. Consider the complete direction order \(p=(a,b,c,d,e,f,g)\), and denote its consecutive window colors by \(w_1,\ldots,w_5\).

**Lemma 1 (two independently controlled wings).** Fix the initial bits at \(a,b,d,f,g\). With \(u=x_e\) and \(v=x_c\), there are Boolean functions \(A,B,D,E\) and a constant \(M\) such that
\[
(w_1,w_2,w_3,w_4,w_5)=(A(u),B(u),M,D(v),E(v)).
\]
Put
\[
\ell(u)=[A(u)\ne B(u)]+[B(u)\ne M],\qquad
r(v)=[M\ne D(v)]+[D(v)\ne E(v)].
\]
Among these four initial vertices a geodesic with at most one color change exists if and only if
\[
\min_{u\in\mathbb F_2}\ell(u)+\min_{v\in\mathbb F_2}r(v)\le1.
\]
If both wing maps \(u\mapsto(A(u),B(u))\) and \(v\mapsto(D(v),E(v))\) are nonconstant, all four starts fail precisely when neither wing assumes the pair \((M,M)\).

**Proof.** The successive free triples are \(abc,bcd,cde,def,efg\). Direction \(e\) is exterior exactly to the first two faces, while \(c\) is exterior exactly to the last two; both are free in the middle face. This proves the displayed separation. The total number of changes is \(\ell(u)+r(v)\), and the independent minimization is exact. The left wing cost equals zero exactly for \((M,M)\) and two exactly for \((M,1-M)\). The right wing cost equals zero exactly for \((M,M)\) and two exactly for \((1-M,M)\). A nonconstant two-point wing map cannot always equal its unique cost-two pair, so each minimum is at most one; their sum is at most one exactly when at least one is zero. \(\square\)

**Theorem 2 (crossed sensitivity and pivot rigidity).** Fix just the four initial bits at \(a,b,f,g\) and vary \(u=x_e\), \(v=x_c\), and \(t=x_d\). Then the color word has the form
\[
(P(u,t),L(u),M,R(v),S(v,t)).
\]
Suppose \(L\) and \(R\) are each nonconstant. Let \(u_*,v_*\) be their respective unique arguments with \(L(u_*)=R(v_*)=M\). If either \(t\mapsto P(u_*,t)\) or \(t\mapsto S(v_*,t)\) is nonconstant, then a full antipodal geodesic in direction order \(p\) has at most one color change. More generally, failure for every one of the eight \((u,v,t)\) forces
\[
P(u_*,0)=P(u_*,1)=S(v_*,0)=S(v_*,1)=1-M.
\]

**Proof.** In addition to the dependencies proved above, the coordinate \(d\) is free in each of the three middle faces and exterior to the first and fifth faces. Hence the stated three-variable factorization holds. Choosing \(u_*,v_*\) makes the word
\[
(P(u_*,t),M,M,M,S(v_*,t)).
\]
Such a word has at most one change whenever either endpoint equals \(M\). Consequently, if both choices of \(t\) fail, both endpoints must equal \(1-M\) for both values of \(t\). The sensitivity conclusion follows. \(\square\)

Theorems 1–2 are local conclusions for unrestricted face colorings. They give a precise necessary condition on every seven-coordinate order in a hypothetical NORI counterexample. To prove dimension-seven closure, one must additionally use the antipodal-reversal relations between *different* orders to contradict the stipulated endpoint rigidity, or find an order whose wing minima sum to at most one.
