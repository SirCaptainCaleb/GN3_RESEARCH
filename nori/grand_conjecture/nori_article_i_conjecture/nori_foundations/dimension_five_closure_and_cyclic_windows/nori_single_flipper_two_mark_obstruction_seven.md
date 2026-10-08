# Seven-dimensional closure for the two-mark obstruction with arbitrary g-face dependence

# Seven-dimensional closure for a universal flipper over the two-mark obstruction

Let \(Q_7\) have directions \(A\sqcup M\sqcup\{g\}\), where \(A=\{a,b,c,d\}\) has four unmarked directions and \(M=\{u,v\}\) has two marked directions. On ordered triples of the six directions \(B=A\sqcup M\), put
\[
 h(r,s,t)=
 \begin{cases}
 1,&s\in A\text{ and }(r\in M\text{ or }t\in M),\\
 0,&\text{otherwise}.
 \end{cases}
\]
This is reversal-even and gives the known sharp unrestricted \(Q_6\) obstruction: every full order of \(B\) has at least two changes.

**Theorem (face-dependent single-flipper lift is always good).** Suppose \(c\) colors ordered three-faces of \(Q_7\), satisfies \(c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi)\), and satisfies
\[
 c(F,\pi)=x_g(F)\oplus h(\pi)\qquad
 \text{whenever the free triple }\pi\text{ excludes }g.
\]
On triples containing \(g\), the coloring is completely arbitrary subject to antipodal-reversal oddness, and may depend on all four fixed exterior face bits. Then \(c\) has a full seven-edge antipodal geodesic with at most one color change.

**Proof.** Suppose for contradiction that every seven-edge geodesic is bad. Write \(m=(x_u,x_v)\in\mathbb F_2^2\) for the initial marked bits, and \(\bar m=(1\oplus x_u,1\oplus x_v)\). Denote the color of an ordered face whose free triple contains \(g\) by \(H\), retaining its dependence on the exterior face position.

*First forcing family.* Let \(a,b,c\) be distinct members of \(A\), \(d\) the fourth member, and consider the direction order
\[
 (a,g,b,c,u,v,d).
\]
Its final three windows, with free orders \((b,c,u),(c,u,v),(u,v,d)\), have \(h\)-colors \((1,0,0)\). Since \(g\) has already been flipped, their actual colors are \((x_g,x_g\oplus1,x_g\oplus1)\). The initial two window colors \(H(a,g,b)\) and \(H(g,b,c)\) are independent of \(x_g\). If they agreed, choosing \(x_g\) so the third window matched them would produce a good full geodesic. Hence
\[
 H(a,g,b)\ne H(g,b,c) \tag{1}
\]
for **every** assignment of the other six starting bits, with the appropriate face positions along this path.

For fixed \(a,b\), the face \((a,g,b)\) has the two other unmarked bits as exterior bits. In (1), \(x_c\) affects the first face but is free in the second face \((g,b,c)\), so the first color is independent of \(x_c\). We may choose \(c\) to be either member of \(A\setminus\{a,b\}\); thus the \((a,g,b)\)-face color is independent of both exterior unmarked bits. Write its value as \(F_{ab}(m)\). Similarly, in (1), \(x_a\) is free in the first face but (already toggled) is exterior to the second; varying \(a\) over \(A\setminus\{b,c\}\) shows that the \((g,b,c)\)-face color is independent of both exterior unmarked bits. Write it as \(G_{bc}(m)\). Therefore
\[
 F_{ab}(m)\ne G_{bc}(m)
 \quad\text{for every pairwise distinct }a,b,c\in A
 \text{ and every }m. \tag{2}
\]
For each fixed \(b,m\), the three values \(F_{ab}(m)\) with \(a\in A\setminus\{b\}\) are equal: given two choices \(a,a'\), use the remaining \(c\in A\setminus\{a,a',b\}\) in (2). Call their common value \(K_b(m)\). Equation (2) then gives \(G_{bc}(m)=1\oplus K_b(m)\) for every \(c\ne b\).

Apply the antipodal-reversal rule to the ordered face \((a,g,b)\), whose reversed triple is \((b,g,a)\). Reversal complements both marked exterior bits, and we have already proved independence of the other exterior bits. Hence
\[
 K_a(\bar m)=1\oplus K_b(m)
 \quad (a\ne b,\ a,b\in A). \tag{3}
\]
Fix one \(a\) and compare (3) for two other choices \(b,c\); then \(K_b(m)=K_c(m)\). Since \(|A|=4\), this forces a common function \(K(m)\) for all four subscripts. Equation (3) becomes
\[
 K(\bar m)=1\oplus K(m). \tag{4}
\]
We have proved, for any distinct unmarked \(r,s\in A\) and arbitrary exterior unmarked bits:
\[
 H(r,g,s)=K(m),\quad H(g,r,s)=1\oplus K(m).
\]
Antipodal reversal and (4) also give
\[
 H(r,s,g)=1\oplus K(m). \tag{5}
\]
Here \(m\) always means the marked exterior bits **at the window in question**.

*Second forcing family.* Fix an ordering \((a,b,c,d)\) of \(A\) and the full direction order
\[
 (a,b,c,g,d,u,v).
\]
By the forced identities and the definition of \(h\), its complete five-window color word is
\[
 \bigl(x_g,\;1\oplus K(m),\;K(m),\;T_u,\;x_g\oplus1\bigr), \tag{6}
\]
where \(T_u\) is the color of the ordered face \((g,d,u)\) reached in the fourth window. None of \(u,v\) has yet been traversed when the second and third windows occur, so both use the same \(m\). Choose \(x_g=1\oplus K(m)\). Then (6) becomes
\[
 (1\oplus K,\;1\oplus K,\;K,\;T_u,\;K).
\]
If \(T_u=K(m)\), this word has exactly one change. Thus the assumed universal failure forces
\[
 T_u=1\oplus K(m) \tag{7}
\]
for every choice of starting bits. Yet the direction \(u\) is free in the face \((g,d,u)\), so \(T_u\) is independent of the starting bit \(x_u\), whereas all its other exterior face bits are unchanged when \(x_u\) varies. It follows from (7) that \(K(x_u,x_v)\) is independent of \(x_u\).

Now interchange \(u,v\) in the last two positions, using the order \((a,b,c,g,d,v,u)\). Exactly the same argument, with the face \((g,d,v)\) in the fourth window and with \(h(d,v,u)=0\), shows that \(K\) is independent of \(x_v\). Therefore \(K\) is constant, contradicting (4). This establishes the theorem. \(\square\)

**Corollary.** The sharp reversal-even two-mark counterexample in six dimensions cannot be converted into a seven-dimensional NORI counterexample by adding a universal-flipper coordinate, **even when every ordered three-face containing that coordinate is allowed arbitrary dependence on its four fixed exterior bits**.

**Proof status and frontier.** This is a complete, local proof for the specified, highly structured class of seven-dimensional odd colorings. It is strictly stronger than the coordinate-only-on-\(g\)-faces suffix-rich theorem: the latter's pointwise triple-label contradiction does not survive arbitrary exterior dependence, while the two forcing families above use the available marked-bit freedom to recover a contradiction. No statement of general \(Q_7\) closure or all-dimensional NORI closure follows.
