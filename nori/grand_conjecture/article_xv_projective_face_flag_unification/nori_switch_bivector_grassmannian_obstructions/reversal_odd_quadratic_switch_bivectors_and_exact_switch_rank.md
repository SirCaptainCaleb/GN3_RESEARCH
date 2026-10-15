# Reversal-odd quadratic switch bivectors and exact switch rank

### Reversal-odd quadratic switch bivectors and switch rank

The two original existence questions admit a common algebraic zero-detection formula in the type-A reflection space. The construction applies uniformly to centered complete-path color words, with the center offset specifying the intrinsic observational radius. It produces an **odd exterior two-form** that vanishes precisely on paths with at most one color switch, and whose rank measures the number of switches.

Let \(n\ge3\), \(s\ge0\), and \(m=n-2s\ge2\). Fix an ordered list \(\pi=(\pi_1,\ldots,\pi_n)\) of distinct symbols, and an associated binary observation word \(w=(w_1,\ldots,w_m)\), centered at positions \(s+1,\ldots,n-s\). Set
\[
W=\{z\in\mathbb R^n:\sum_i z_i=0\},\qquad
Z_r(\pi)=\sum_{h=1}^r e_{\pi_h}-\frac rn\mathbf1
\quad(1\le r<n),
\tag{1}
\]
and \(\delta_j=w_j\oplus w_{j+1}\in\{0,1\}\) for \(1\le j<m\).

**Definition (quadratic switch bivector).** Put
\[
\boxed{\mathcal B_s(\pi,w)=
\sum_{1\le j<k<m}\delta_j\delta_k\,
Z_{j+s}(\pi)\wedge Z_{k+s}(\pi)
\quad\in\Lambda^2W.}\tag{2}
\]

**Theorem 1 (zero and rank detection).** The bivector \(\mathcal B_s\) vanishes if and only if the observation word has at most one switch. If the word has \(r\) switches, the skew-symmetric linear form defined by \(\mathcal B_s\) has rank
\[
\boxed{\operatorname{rank}\mathcal B_s=2\left\lfloor\frac r2\right\rfloor.}\tag{3}
\]
In particular a two-switch word gives a nonzero decomposable bivector, while at least four switches give a form of rank at least four.

*Proof.* The vectors \(Z_1(\pi),\ldots,Z_{n-1}(\pi)\) form a basis of \(W\): pairing with successive simple roots gives
\[
(e_{\pi_i}-e_{\pi_{i+1}})\cdot Z_j=\mathbf1_{\{i=j\}}.
\tag{4}
\]
Consequently the wedge products \(Z_a\wedge Z_b\), \(a<b\), form a basis of \(\Lambda^2W\). The coefficients of (2) are \(\delta_j\delta_k\); all vanish precisely when at most one \(\delta_j\) equals one. This proves the zero condition.

Restrict to the \(r\) basis vectors indexed by switch positions. In that basis the alternating form has matrix \(A_r\) with entries \((A_r)_{ij}=1\) for \(i<j\), \(-1\) for \(i>j\), and zero for \(i=j\). If \(A_rv=0\), successive row differences give \(v_{i+1}=-v_i\). Hence every null vector must have alternating entries \((a,-a,a,-a,\ldots)\). The first row equation forces \(a=0\) when \(r\) is even, while for odd \(r\) it is satisfied by every such alternating vector. Therefore \(\operatorname{rank}A_r=r\) when \(r\) is even and \(r-1\) when \(r\) is odd, proving (3). \(\square\)

**Theorem 2 (reversal oddness).** Suppose a complete-path system has an involution \(R\) sending
\[
(\pi,w)\longmapsto
\bigl(\pi^{\mathrm{rev}},\mathbf1+\operatorname{rev}w\bigr).
\tag{5}
\]
Then
\[
\boxed{\mathcal B_s(R(\pi,w))=-\mathcal B_s(\pi,w).}\tag{6}
\]

*Proof.* A switch at index \(j\) becomes one at index \(m-j\) after reversal. Since \(m=n-2s\), its centered prefix rank \(j+s\) changes to \((m-j)+s=n-(j+s)\). The first \(n-(j+s)\) symbols of \(\pi^{\mathrm{rev}}\) are the complement of the first \(j+s\) symbols of \(\pi\). Consequently
\[
Z_{n-(j+s)}(\pi^{\mathrm{rev}})=-Z_{j+s}(\pi).
\tag{7}
\]
Under reversal, a pair of switch indices \(j<k\) becomes \(m-k<m-j\). Substitution into (2), followed by interchange of the wedge factors, gives
\[
(-Z_{k+s})\wedge(-Z_{j+s})
=-Z_{j+s}\wedge Z_{k+s}.
\]
Every pair contributes its negative, proving (6). \(\square\)

**Corollary 3 (both original problems have the same bivector zero target).**

1. For an antipodally odd edge coloring of \(Q_n\), take a complete geodesic flag \((x;\pi)\), its true length-\(n\) edge-color word \(w\), and \(s=0\). The cube reversal \(R(x;\pi)=(x;\pi^{\mathrm{rev}})\) has word law (5), as proved earlier in this Article. There exists a complete flag with \(\mathcal B_0=0\) if and only if NORI1 holds for that coloring. Indeed \(\mathcal B_0=0\) gives at most one internal switch, and the antipodal root-slide orbit criterion converts any such flag into a monochromatic full geodesic.
2. For an unrestricted reversal-odd boundary 3-tournament on \(n\) vertices, take a Hamilton order \(\pi\), its length-\(n-2\) consecutive triple-color word, and \(s=1\). Reversing the Hamilton order obeys (5). There exists a full flag with \(\mathcal B_1=0\) if and only if the boundary tournament has a Hamilton tight path with at most one switch.

Thus the same formula (2), the same reversal representation (6), and the same zero criterion describe both full unrestricted existence problems. The observation offset is determined by the centered window: one edge-dimension position in the cube, versus a triple centered at its middle vertex for the boundary tournament.

**Theorem 4 (universal rational bivector contraction).** Fix \(n\ge3\), let \(\vartheta=2^{1/n}\), and set
\[
u_i=\vartheta^{i-1}-\frac1n\sum_{h=1}^n\vartheta^{h-1}
\quad(1\le i\le n),\qquad u\in W.
\tag{8}
\]
Using the standard inner product to contract bivectors, the map \(\mathcal I_u:\Lambda^2W\to W\), \(\Xi\mapsto\iota_u\Xi\), obeys
\[
\boxed{\mathcal I_u(\Xi)\ne0
\quad\text{for every nonzero }\Xi\in\Lambda^2(W\cap\mathbb Q^n).}\tag{9}
\]
Consequently, for the switch bivector \(\mathcal B_s\),
\[
\boxed{\mathcal V_s=\iota_u\mathcal B_s\in W
\quad\text{vanishes precisely on words with at most one switch},}
\tag{10}
\]
and under the reversal law (5) it satisfies \(\mathcal V_s(Rg)=-\mathcal V_s(g)\).

*Proof.* Represent a rational bivector \(\Xi\) by a skew-symmetric matrix \(A\) with rational entries. Since both of its wedge factors lie in \(W\), one has \(A\mathbf1=0\). Therefore \(Au=A(1,\vartheta,\ldots,\vartheta^{n-1})^{\mathsf T}\). The polynomial \(X^n-2\) is irreducible over \(\mathbb Q\) by Eisenstein's criterion at the prime two. Hence \(1,\vartheta,\ldots,\vartheta^{n-1}\) are linearly independent over \(\mathbb Q\). If \(Au=0\), every row of \(A\) gives a rational relation among these numbers and must vanish. Thus \(A=0\), proving (9), with the harmless convention of the sign of interior contraction. The vectors \(Z_j\) have rational entries, so \(\mathcal B_s\) is rational. Theorem 1 now gives (10), and Theorem 2 gives its reversal law. \(\square\)

Theorem 4 provides a **single fixed real \((n-1)\)-dimensional target** for odd switch detection on all complete paths, for every coloring, without losing the bivector zero criterion. For the free punctured-torus reflection carrier of the preceding Subsection, \(W\setminus\{0\}\simeq S^{n-2}\) is precisely the forbidden equivariant target dimension. The unresolved work is the extension of these odd vectors from complete-path chambers over root-changing and rank-two cells. Their nonvanishing on a discrete chamber set supplies no continuity or filling by itself.

**Scope and obstruction.** All four theorems are unconditional algebraic statements for any centered reversal word system. Their zero-detection property does not force a zero: reversal-odd words on unrelated complete flags can all have many switches. Theorem 4 removes the ambient target-dimension barrier **at the finite set of complete-path chambers**. It supplies no continuous extension on the source chamber complex. For the punctured affine cube carrier, a nowhere-zero equivariant extension into \(W\) would contradict the nonzero covering index from the preceding Subsection and thereby prove NORI1. For the boundary type-A sphere, one must additionally reduce the target by one real dimension to obtain an analogous contradiction; generic projections retain nonvanishing on finite chamber sets, yet compatible higher-cell fillings are unproved. The central open step for both problems is coherent color-sensitive continuation across all local exchanges, respecting the original projective incidence descent and complete-path support.
