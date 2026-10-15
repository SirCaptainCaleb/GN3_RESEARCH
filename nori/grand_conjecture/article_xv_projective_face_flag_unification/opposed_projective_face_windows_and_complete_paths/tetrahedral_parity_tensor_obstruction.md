# Tetrahedral parity tensor obstruction

### Tetrahedral parity obstruction for the complete quadratic switch tensor

**Theorem 1 (four-point cancellation).** For each \(n\ge6\), there is an unrestricted reversal-odd boundary triple coloring and a rank-three Coxeter cell \(D\cong P_4\) whose 24 Hamilton flags all have at least two switches, yet the convex hull of their **complete quadratic switch bivectors** contains zero. More strongly, each of the six Klein-four orbits of four flags has bivectors summing to zero.

*Proof.* Let \(A=\{1,2,3,4\}\) be the variable first block, and fix the remaining symbols in a suffix beginning \(e,f\). For any distinct \(a,b,c\in A\), let \(t(a,b,c)\) be the parity of \((a,b,c,d)\), where \(d\) is the omitted fourth member. Set \(b(a,b,c)=t(a,b,c)\). Cyclically rotating four symbols changes parity, and reversing the first and third positions changes parity. Prescribe \(b(c,d,e)=1\) whenever \(c,d\in A\) are the last two symbols of a first-block order, and \(b(d,e,f)=0\) for \(d\in A\). Set subsequent colors on the fixed suffix to zero. These prescriptions are consistent with reversal oddness and extend to all unused ordered triples.

Thus every full order \(\pi=(a,b,c,d,e,f,\ldots)\) in \(D\) has consecutive triple-color word \((t,1-t,1,0,0,\ldots)\). Its switch-prefix ranks are \(\{2,4\}\) for \(t=0\), or \(\{2,3,4\}\) for \(t=1\). Consequently
\[
\mathcal B(\pi)=
\begin{cases}
Z_2\wedge Z_4,& t=0,\\
Z_2\wedge Z_3+Z_2\wedge Z_4+Z_3\wedge Z_4,&t=1.
\end{cases}
\tag{1}
\]
Let \(T=Z_4=\mathbf1_A-(4/n)\mathbf1\) and let \(W_A\) consist of vectors supported on \(A\) whose entries sum to zero. All vectors \(Z_2,Z_3,Z_4\) lie in \(U=\mathbb RT\oplus W_A\).

Consider the Klein four-group \(K=\{1,(12)(34),(13)(24),(14)(23)\}\) acting on \(A\). As a real \(K\)-module, \(W_A\) splits into the three distinct nontrivial one-dimensional characters. Therefore
\[
\Lambda^2 U=T\wedge W_A\oplus\Lambda^2W_A
\]
is a sum of six nontrivial one-dimensional \(K\)-modules, and \((\Lambda^2 U)^K=\{0\}\). Hence the group average \(\frac14\sum_{h\in K}hX\) vanishes for every \(X\in\Lambda^2U\).

Each \(h\) is even, preserving parity \(t\). The tensor formula (1) is equivariant under relabeling the four symbols, so \(\mathcal B(h\pi)=h\mathcal B(\pi)\). Thus
\[
\boxed{\frac14\sum_{h\in K}\mathcal B(h\pi)=0.}
\tag{2}
\]
All four coefficients are positive and all four flags have at least two switches. The same conclusion survives every linear map on bivectors, including generic critical contractions. QED.

**Theorem 2 (symmetry-forced zero and external escape).** There is no continuous \(K\)-equivariant map \(D\to\Lambda^2U\setminus\{0\}\). However, if at least two suffix symbols \(e,f\) exist, any nonvanishing \(K\)-equivariant boundary map \(\partial D\to\Lambda^2 U\setminus\{0\}\) extends to a nonvanishing \(K\)-equivariant map \(D\to\Lambda^2W\setminus\{0\}\) that uses a bivector involving the suffix.

*Proof.* The barycenter of \(D=P_4\) is fixed by \(K\). A \(K\)-equivariant map into \(\Lambda^2U\) must send this barycenter into the fixed subspace, which is zero. For the extension, choose \(L=T\wedge(e_e-e_f)\in\Lambda^2W\), a nonzero \(K\)-fixed bivector perpendicular to \(\Lambda^2U\). Cone the boundary map radially to \(L\) at the barycenter. Every interior value is \((1-s)L+sX\), with \(X\in\Lambda^2U\setminus\{0\}\), and is nonzero by orthogonality. The cone is equivariant. QED.

**Proposition 3 (forced global symmetry breaking).** The triple-color data encountered on the 24 flags of \(D\) is \(K\)-invariant, but no globally reversal-odd triple coloring can be \(K\)-invariant on all ordered triples.

*Proof.* The encountered colors are either the four-symbol parity, invariant under even permutations, or the constant mixed-triple prescriptions. But for distinct \(a,c\in A\), a double transposition \(h=(a\,c)(a'\,c')\in K\), where \(\{a',c'\}=A\setminus\{a,c\}\), sends the unused ordered triple \((a,e,c)\) to its reversal \((c,e,a)\). A globally invariant coloring would give equal bits, contradicting reversal oddness. QED.

**Implication.** The full quadratic tensor improves rank-two convex fillings but does not remove the rank-three convex obstruction. No nonlinear *equivariant* filling confined to the local four-symbol tensor module can remove it, either. The extra ambient directions and off-cell coloring constraints are mathematically necessary ingredients for a symmetric filling mechanism; the results do not resolve the global one-switch conjecture.
