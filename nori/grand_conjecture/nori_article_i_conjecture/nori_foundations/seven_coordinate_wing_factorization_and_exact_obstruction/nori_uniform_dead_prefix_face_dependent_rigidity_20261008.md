# Uniformly dead six-dimensional prefixes force position-independent alternating blocks

# Uniform dead-prefix rigidity in a face-dependent reversal-even six-cube

Let \(B=\{a,b,c\}\sqcup D\), where \(|D|=3\). Let \(h\) color *ordered three-dimensional faces* of \(Q_B\) and satisfy reversal-even antipodality,
\[
 h(\bar F,\operatorname{rev}\pi)=h(F,\pi).
\]
For a six-direction geodesic with initial vertex \(x\in Q_B\) and coordinate order \((a,b,c,d,e,f)\), denote its final three window colors by
\[
U_d(x)=h(b,c,d),\quad V_{d,e}(x)=h(c,d,e),\quad W_{d,e,f}(x)=h(d,e,f),
\]
where each face is evaluated at its actual position along the geodesic and \((d,e,f)\) is a permutation of \(D\). Note that \(U_d\) is independent of the ordering of the other two members of \(D\).

**Theorem (uniform dead-prefix rigidity).** Suppose that for *every* starting vertex \(x\in Q_B\) and *every* permutation \((d,e,f)\) of \(D\), the tail word \((U_d(x),V_{d,e}(x),W_{d,e,f}(x))\) has exactly two color changes. Then there exists one constant bit \(K\) such that, **for every exterior face assignment**,
\[
\begin{aligned}
 h(F,(b,c,d))&=K &&(d\in D),\\
 h(F,(c,d,e))&=1\oplus K &&(d,e\in D,\ d\ne e),\\
 h(F,(d,e,f))&=K &&((d,e,f)\text{ a permutation of }D).
\end{aligned}\tag{1}
\]
The reversal-even involution gives the same constants on all reversed triples. Conversely, if (1) holds then every listed tail is alternating, for every starting vertex and every completion.

**Proof.** Put \(t=1\oplus x_a\), the fixed exterior \(a\)-bit seen by all three tail faces after the first move \(a\). Every tail is alternating, so
\[
U_d(x)=W_{d,e,f}(x),\qquad V_{d,e}(x)=1\oplus U_d(x)\tag{2}
\]
for every \(x,d,e,f\).

For fixed \(d\), the free directions of the first tail face are \(b,c,d\). Its exterior face coordinates are \(a,e,f\), so \(U_d\) depends only on \(t,x_e,x_f\). The last tail face has free directions \(d,e,f\), with exterior coordinates \(a,b,c\), so \(W_{d,e,f}\) depends only on \(t,1\oplus x_b,1\oplus x_c\). Since the first equality in (2) holds for **all six initial bits**, the disjoint sets of variables \(x_e,x_f\) and \(x_b,x_c\) must drop out. Thus for every \(d\) there is a Boolean function \(K_d(t)\) such that
\[
U_d(x)=W_{d,e,f}(x)=K_d(t)
\]
for all \(x\) and both permutations of \(\{e,f\}=D\setminus\{d\}\). Equation (2) then gives \(V_{d,e}(x)=1\oplus K_d(t)\), independently of its other exterior bits. All these conclusions concern **every possible exterior face assignment**, since the unrestricted initial bits range over the entire cube.

Now use reversal-even antipodality on the last tail face. For distinct \(d,f\in D\), let \(e\) be the third member. The opposite ordered face has free order \((f,e,d)\), with all three exterior coordinates \(a,b,c\) complemented. Hence
\[
K_d(t)=K_f(1\oplus t)\qquad(d,f\in D,\ d\ne f).\tag{3}
\]
Fix \(t\) and choose three distinct members \(d,e,f\) of \(D\). Comparing (3) for the pairs \((d,e)\) and \((d,f)\) gives \(K_e(1\oplus t)=K_f(1\oplus t)\). Varying indices shows all three \(K_d\) are the same function \(K(t)\). Equation (3) now reduces to \(K(t)=K(1\oplus t)\); since \(t\) is Boolean, \(K\) is constant. Substitution into (2) proves (1). Conversely, (1) gives the tail word \((K,1\oplus K,K)\) everywhere, proving the reverse implication. \(\square\)

**Use for NORI.** In a hypothetical seven-dimensional NORI counterexample with one universal exterior flipper, the six-dimensional induced residual is reversal-even. If a fixed ordered prefix \((a,b,c)\) admits **no** one-change five-direction tail for any of the 64 starting vertices, then the residual has the exact constant block (1), despite initially allowing arbitrary nonlinear dependence on three exterior coordinates. This strengthens the existing coordinate-only dead-prefix rigidity lemma. A counterexample need only have a dead prefix at *one* starting vertex, so the uniform hypothesis must be established separately before invoking the theorem.
