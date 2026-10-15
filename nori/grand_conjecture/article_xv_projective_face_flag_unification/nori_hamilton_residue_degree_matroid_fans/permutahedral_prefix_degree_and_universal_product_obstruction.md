# Permutahedral prefix degree and universal product obstruction

### Universal prefix degrees on two-block Coxeter cells

**Lemma 1 (prefix map of a permutahedron).** Let \(m\ge2\) and \(1\le k\le m-1\). In \(W_m=\{z:\sum z_i=0\}\), assign each vertex \(\pi\) of the \((m-1)\)-permutahedron \(P_m\) the centered prefix label
\[
z_k(\pi)=\sum_{j\le k}e_{\pi_j}-\frac{k}{m}\mathbf1.
\]
After affine interpolation on a triangulation of each boundary face, these labels define a zero-free map \(f_k:\partial P_m\to W_m\setminus\{0\}\). Its radial normalization has degree \(\pm1\).

*Proof.* Use the centered permutahedron vertices \(u_\pi=\sum_j((m+1)/2-j)e_{\pi_j}\). A proper boundary face is represented by an ordered partition with first block \(S\) of size \(h\), where \(1\le h<m\). On every vertex \(\pi\) of that face,
\[
\sum_{i\in S}(u_\pi)_i=h(m-h)/2>0,\qquad
\sum_{i\in S}(z_k(\pi))_i=\min(k,h)-kh/m>0.
\]
Consequently every convex combination of the prescribed prefix labels on this face, and every straight-line interpolation from the identity embedding \(u_\pi\), stays in a common strict halfspace avoiding zero. The normalized boundary prefix map is therefore homotopic to the radial boundary map of the centered permutahedron, which has degree \(\pm1\). QED.

**Theorem 2 (product degree for a fixed straddling switch pair).** Partition \([n]=A\sqcup B\), \(|A|=a\ge2\), \(|B|=b\ge2\), and consider the top dual type-A cell \(D=P_a\times P_b\) consisting of Hamilton words listing \(A\) before \(B\). Fix \(1\le k<a\) and \(1\le\ell<b\). For each such word \(\pi\), let \(Z_j(\pi)\) be its centered length-\(j\) prefix vector and put
\[
T=\sum_{i\in A}e_i-\frac an\mathbf1,\quad
E(\pi)=Z_k(\pi)\wedge Z_{a+\ell}(\pi).
\]
The contracted vertex labels \(\iota_T E(\pi)\) extend to a map \(\partial D\to W\cap T^\perp\setminus\{0\}\) of degree \(\pm1\), with \(\dim(W\cap T^\perp)=n-2=\dim D\).

*Proof.* Write \(u_k\in W_A\) for the centered prefix indicator of the first \(k\) members of \(A\), and \(v_\ell\in W_B\) for the first \(\ell\) members of \(B\). One has
\[
Z_k=(k/a)T+u_k,\quad
Z_{a+\ell}=((b-\ell)/b)T+v_\ell,\quad \|T\|^2=ab/n.
\]
Therefore
\[
\iota_T E=\|T\|^2\big((k/a)v_\ell-((b-\ell)/b)u_k\big).
\]
The two summands belong to orthogonal complementary spaces \(W_B\) and \(W_A\) of respective dimensions \(b-1,a-1\). By Lemma 1, the corresponding prefix maps on each permutahedron boundary have degree \(\pm1\). Coning each to zero in the interior gives maps of each ball with a unique zero of degree \(\pm1\). Their weighted direct sum on \(D\) has a single zero, with product degree \(\pm1\), and is nonzero on \(\partial D\). QED.

**Corollary 3 (all switch pairs, six-vertex product example).** For the earlier reversal-odd \(3+3\) coloring, the color word is \((t,1-t,1-s,s)\). Its switch indicators are \((1,\epsilon,1)\), where \(\epsilon=t\mathbin{\mathrm{xor}}s\). Besides the extreme pair, the full quadratic switch bivector is
\[
\mathcal B_1=Z_2\wedge Z_4+\epsilon(Z_2\wedge Z_3+Z_3\wedge Z_4).
\]
With \(T=Z_3\), \(\xi_c=e_c-\frac13\sum_Ae\), and \(\eta_d=e_d-\frac13\sum_Be\),
\[
\boxed{\iota_T\mathcal B_1=(1+\tfrac32\epsilon)(\xi_c+\eta_d).}
\]
Thus its normalized contracted labels agree at every flag with those from the extreme switch pair; the same degree-one boundary extension applies even when the middle switch occurs.

**Qualification.** Theorem 2 is geometric and conditional. For boundary triple colors, the switch ranks \(k-1\) and \(a+\ell-1\) must lie among the legal internal ranks. The theorem does not claim that arbitrary partitions admit reversal-odd colorings imposing these fixed first/last switch positions on all flags. Its conclusion is the persistence of the degree-one obstruction whenever the indicated fixed-pair configuration occurs.
