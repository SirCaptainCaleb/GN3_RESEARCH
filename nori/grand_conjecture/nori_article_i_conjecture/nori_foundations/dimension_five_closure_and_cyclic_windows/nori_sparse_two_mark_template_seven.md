# Sparse ordered-face template forces one-change closure in dimension seven

# Sparse-template seven-dimensional forcing

Let \(V=A\sqcup M\sqcup\{g\}\), \(|A|=4\), \(M=\{u,v\}\). Suppose \(c\) is an antipodal-reversal-odd coloring of ordered three-faces of \(Q_7\), and for **every** exterior face position, a free triple avoiding \(g\) has color
\[
c(F,\pi)=x_g(F)\oplus h(\pi),\qquad
h(AAA)=0,\ h(AAM)=h(MAA)=1,\ h(AMM)=h(MMA)=0. \tag{1}
\]
Only the indicated five membership patterns are prescribed. Colors for triples of types \(AMA\), \(MAM\), and all triples containing \(g\) are arbitrary subject to oddness, with unrestricted nonlinear exterior dependence.

**Theorem.** There is a full antipodal geodesic whose five-window color word changes at most once.

**Proof.** Suppose every full geodesic fails. For distinct \(a,b,c\in A\), and \(d=A\setminus\{a,b,c\}\), use the complete order \((a,g,b,c,u,v,d)\). Its final three window colors are \((x_g,1\oplus x_g,1\oplus x_g)\) by (1), while the initial two are independent of \(x_g\). If they agreed, choose \(x_g\) to match their color, producing a good path. Thus always
\[
c(a,g,b)\ne c(g,b,c). \tag{2}
\]
Varying the initial \(x_c\) in (2) shows that \(c(a,g,b)\) is independent of \(x_c\), since \(c\) is free in the right window. As \(c\) ranges over both elements of \(A\setminus\{a,b\}\), the left color is independent of both unmarked exterior bits and becomes \(F_{ab}(m)\), where \(m=(x_u,x_v)\). Dually, varying \(a\) shows that the right color is independent of its unmarked exterior bits and becomes \(G_{bc}(m)\). Consequently
\[
F_{ab}(m)=1\oplus G_{bc}(m) \tag{3}
\]
for pairwise distinct \(a,b,c\). For fixed \(b,m\), any two choices \(a,a'\) admit a common third \(c\); therefore all \(F_{ab}(m)\) coincide, say \(K_b(m)\), and \(G_{bc}(m)=1\oplus K_b(m)\). Oddness of the antipodally reversed \((a,g,b)\)-face gives
\[
K_a(\bar m)=1\oplus K_b(m)\quad(a\ne b).
\]
Comparing different indices yields a common \(K(m)\) and \(K(\bar m)=1\oplus K(m)\). Therefore for any distinct \(r,s\in A\), at every face position,
\[
c(r,g,s)=K(m),\quad c(g,r,s)=c(r,s,g)=1\oplus K(m), \tag{4}
\]
with \(m\) evaluated at the face. The third equality follows by oddness and the oddness of \(K\).

Now use the complete order \((a,b,c,g,d,u,v)\), with \((a,b,c,d)\) any order of \(A\). By (1) and (4), its word is
\[
(x_g,1\oplus K(m),K(m),T_u,1\oplus x_g),
\]
where \(T_u\) is the color of the fourth face \((g,d,u)\). Taking \(x_g=1\oplus K(m)\) yields
\[
(1\oplus K,1\oplus K,K,T_u,K).
\]
A good path results if \(T_u=K(m)\). Thus failure forces \(T_u=1\oplus K(m)\) for all starts. Since \(u\) is free in this face, \(T_u\) is independent of \(x_u\), so \(K\) is independent of \(x_u\). Repeating with \((a,b,c,g,d,v,u)\) forces independence of \(x_v\). Hence \(K\) is constant, contradicting \(K(\bar m)=1\oplus K(m)\). \(\square\)

**Scope.** This strictly strengthens the prior two-mark/universal-flipper \(Q_7\) result by permitting arbitrary position-dependent coloring of the \(AMA\) and \(MAM\) triples (as well as every \(g\)-containing triple). It gives closure for a larger structured class; unrestricted NORI in dimension seven and higher remains unresolved.
