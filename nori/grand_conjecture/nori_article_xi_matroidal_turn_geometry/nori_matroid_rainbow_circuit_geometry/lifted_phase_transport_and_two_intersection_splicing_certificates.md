# Lifted phase transport and two-intersection splicing certificates

# Lifted phase transport and two-intersection splicing certificates

Let \(n\ge4\), \(G_n=Q_n/\langle\tau\rangle\), and \(H_n=L(G_n)\). Let \(X\) be a binary cycle of the pointed matroid \(D_n\) containing \(p\), with turn label \(d=\mathbf1_{X\setminus\{p\}}\). By the monodromy condition, the pullback of \(d\) to the connected graph \(L(Q_n)\) is a coboundary.

For two undirected cube edges \(e,f\), choose any turn path \(\gamma\) from \(e\) to \(f\) in \(L(Q_n)\) and put
\[
\rho_X(e,f)=\sum_{t\in\gamma}d([t])\pmod2.
\tag{1}
\]
Here \([t]\) denotes projection of a cube turn to \(H_n\). The result is independent of \(\gamma\), because every closed turn walk in \(L(Q_n)\) has zero pulled-back \(d\)-sum. Equivalently, if \(c\) is any recovered antipodally odd cube-edge coloring, then
\[
\boxed{\rho_X(e,f)=c(e)+c(f)\pmod2.}
\tag{2}
\]
In particular, \(\rho_X(e,\tau e)=1\), and for incident cube edges \(\rho_X(e,f)\) is their turn label \(d\). Thus \(\rho_X\) expresses relative color phases using the pointed-matroid cycle \(X\), independently of the global color complement.

For a cube geodesic \(P\), let \(A(P)\subseteq E(H_n)\) denote the projected consecutive turns, so that \(|A(P)\cap X|\) is its number of switches. Its edge-color phase on a monochromatic subpath can be compared to another such path by \(\rho_X\) between any one edge of each subpath.

**Lemma 1 (one missing direction).** If a cube geodesic traverses \(n-1\) distinct directions and all its edge turns lie outside \(X\), then some full antipodal cube geodesic has all its turn edges outside \(X\). Equivalently, the minimum shortest-port-cocircuit intersection \(I(X)\) equals two.

*Proof.* Let the \((n-1)\)-edge path run from \(u\) to \(v=\tau u^{\,b}\), missing direction \(b\), and have constant color \(s\). The \(b\)-edges at \(u\) and \(v\) are antipodal and therefore have complementary colors. One has color \(s\). Append it at \(v\) or prepend it at \(u\), choosing the endpoint where agreement occurs; the result is a monochromatic full antipodal geodesic. Its projected turn cycle has one labeled turn, hence its port cocircuit meets \(X\) in two elements. Every port intersection is a positive even integer, so this is minimal. \(\square\)

Fix distinct exterior directions \(a,b\), let \(D=[n]\setminus\{a,b\}\), and let \(F,F^a\) be adjacent \((n-2)\)-faces. For any \(u,x\in F\), let \(u^a,x^a\in F^a\) be the corresponding vertices.

**Theorem 2 (opposite-phase aligned switch certificate).** Suppose \(P\subset F\) and \(Q\subset F^a\) are geodesics spanning their faces, from \(u\) to \(x\) and from \(u^a\) to \(x^a\). Suppose both have precisely one turn in \(X\), at respective vertices \(z\in P\) and \(z^a\in Q\), and the sets \(A,B\) of directions used before and after these switch vertices agree between the two paths. Each set is nonempty; their internal orders may differ. If \(e_P,e_Q\) are their initial edges and
\[
\boxed{\rho_X(e_P,e_Q)=1,}
\tag{3}
\]
then
\[
\boxed{I(X)=2.}
\tag{4}
\]

*Proof.* Recover a coloring \(c\), and write \(s=c(e_P)\). Since \(P,Q\) each have one switch and (3) holds, their two blocks have colors
\[
P:\quad s^{|A|}(1+s)^{|B|},
\qquad
Q:\quad (1+s)^{|A|}s^{|B|}.
\tag{5}
\]
Let \(h=c(zz^a)\). If \(h=s\), the concatenation of the \(A\)-prefix of \(P\), the \(a\)-edge \(zz^a\), and the \(B\)-suffix of \(Q\) is a monochromatic geodesic from \(u\) to \(x^a\). If \(h=1+s\), concatenate the \(A\)-prefix of \(Q\), the reverse \(a\)-edge \(z^az\), and the \(B\)-suffix of \(P\), producing a monochromatic geodesic from \(u^a\) to \(x\). In either case the path uses every direction in \(D\cup\{a\}\) once and omits only \(b\). Apply Lemma 1. \(\square\)

The next certificate needs only monochromatic arms and the geometry of their meeting vertices.

**Theorem 3 (two-arm interface transport).** Let \(P\subset F\) and \(Q\subset F^a\) be spanning geodesics with corresponding initial and terminal vertices as above. Suppose \(w\) is an interior vertex of \(P\), and \(w^a\) is an interior vertex of \(Q\). The following implications hold.

(i) If the prefix \(P[u,w]\) and the suffix \(Q[w^a,x^a]\) have no turns in \(X\), and one edge \(e\) of the first and one edge \(f\) of the second satisfy \(\rho_X(e,f)=0\), then either \(I(X)=2\), or
\[
\boxed{\rho_X(e,ww^a)=1.}
\tag{6}
\]

(ii) If the prefix \(Q[u^a,w^a]\) and suffix \(P[w,x]\) have no turns in \(X\), and their chosen edges \(e',f'\) satisfy \(\rho_X(e',f')=0\), then either \(I(X)=2\), or
\[
\boxed{\rho_X(e',ww^a)=1.}
\tag{7}
\]

If both (i) and (ii) hold and \(\rho_X(e,e')=1\), then \(I(X)=2\).

*Proof.* The coordinate sets traversed by \(P[u,w]\) and \(Q[w^a,x^a]\) are disjoint and cover \(D\), because the two paths have corresponding start and end vertices, and the intermediate vertices are related by the \(a\)-translation. Under the first two hypotheses of (i), these arms have the same constant edge color, say \(s\). If the connecting \(a\)-edge \(ww^a\) had color \(s\), their concatenation would be a monochromatic geodesic using \(D\cup\{a\}\), and Lemma 1 would give \(I(X)=2\). If \(I(X)>2\), the joining edge must have color \(1+s\), which is (6) by (2).

The same argument, interchanging \(P,Q\), proves (ii). If both conclusions were required while \(\rho_X(e,e')=1\), the single joining \(a\)-edge would have to be opposite in color to two edges of opposite colors. This is impossible, so \(I(X)=2\). \(\square\)

**Corollary 4 (phase coherence in a high-intersection cycle).** Assume \(I(X)\ge4\). Two one-turn spanning geodesics on adjacent codimension-two faces with corresponding starting vertices, terminal vertices and switch vertices cannot have opposite initial phases. Likewise, any pair of interface configurations of Theorem 3 whose two monochromatic phases disagree cannot coexist at the same projected vertex.

*Proof.* The first assertion is the contrapositive of Theorem 2. The second is the last assertion of Theorem 3. \(\square\)

The transport \(\rho_X\) is a cocycle primitive on the lifted line graph. It expresses the phase information needed in the adjacent-face splicing theorems of Article VIII directly through the binary cycle \(X\). Theorems 2--3 give checkable geometric certificates forcing a shortest port cocircuit \(Y\) with \(|X\cap Y|=2\), the monochromatic intersection target.
