# Exact change-vector fibers and affine obstruction certificates

Let \(Q_n=\{0,1\}^n\). Each ordered three-face \((F,\pi)\) has a binary color depending on its free-coordinate order \(\pi\) and the fixed exterior coordinate bits. For a coordinate order \(p=(p_1,\ldots,p_n)\) and an initial vertex \(x\), write \(w_1(x),\ldots,w_{n-2}(x)\) for the consecutive ordered-three-face colors and \(d_i(x)=w_i(x)\oplus w_{i+1}(x)\) for \(1\le i\le n-3\). A good antipodal geodesic is exactly one with Hamming weight \(|d(x)|\le1\).

**Theorem 1 (exact universal-flipper fiber law).** Partition the coordinate set as \(V=A\sqcup B\), with \(|A|=r\) and \(|B|=m\ge3\). Suppose that whenever an \(a\in A\) is fixed outside an ordered three-face, complementing its fixed bit complements the face color. Fix arbitrary coordinate orders \(\sigma\) of \(A\), \(\tau\) of \(B\), and an arbitrary starting vertex \(y\) in the \(B\)-coordinates. As the \(r\) initial \(A\)-bits vary, the complete change vectors on the full direction order \(\sigma\tau\) are **exactly**
\[
\bigl\{(u,\delta(\tau,y)):u\in\mathbb F_2^r\bigr\},
\]
each occurring exactly once. Here \(\delta(\tau,y)\in\mathbb F_2^{m-3}\) is the change vector along the induced \(B\)-geodesic, with \(A\)-bits omitted (their common fixed parity does not affect changes).

**Proof.** Write \(A=(a_1,\ldots,a_r)\), and let \(z_i\) be the initial bit at \(a_i\). The universal-flipper hypothesis implies
\[
 c(F,\pi)=\bigoplus_{a\in A\setminus\mathrm{free}(F)}x_a(F)\ \oplus\ g(\pi,x_{B\setminus\mathrm{free}(F)})
\]
for a function \(g\) independent of every fixed \(A\)-bit. The \(g\)-contribution \(G_i\) to window \(i\) is therefore determined by \(\sigma,\tau,y\) and independent of \(z\). For \(1\le i\le r\), shifting the three-coordinate window one position to the right fixes the departing \(a_i\) at its already toggled value \(1\oplus z_i\), and removes the untoggled arriving \(a_{i+3}\) if \(i+3\le r\). Consequently
\[
 d_i=G_i\oplus G_{i+1}\oplus 1\oplus z_i
 \oplus\mathbf1_{i+3\le r}z_{i+3}.
\]
For prescribed \(d_1,\ldots,d_r\), solve successively for \(z_r,z_{r-1},\ldots,z_1\). Each equation has coefficient one at the currently solved variable and only uses previously solved higher-index \(A\)-bits. The correspondence \(z\mapsto(d_1,\ldots,d_r)\) is bijective. For \(i>r\), both windows lie within \(B\); all \(A\)-bits have been toggled and contribute the same common parity to both colors. Thus \((d_{r+1},\ldots,d_{r+m-3})=\delta(\tau,y)\). This proves the claim. \(\square\)

**Corollary 1 (exact lifting count).** Put \(q=|\delta(\tau,y)|\). The number of choices of initial \(A\)-bits giving a full geodesic with at most one change is exactly \(r+1\) when \(q=0\), exactly \(1\) when \(q=1\), and \(0\) when \(q\ge2\). Thus a monochromatic residual geodesic admits \(r+1\) distinct good lifts, and a one-change residual geodesic admits one canonical good lift.

**Corollary 2 (complete equidistribution).** If \(m\le3\), then for every prescribed full change vector \(d\in\mathbb F_2^{n-3}\) and fixed coordinate order with \(A\) first, **exactly eight** of the \(2^n\) starting vertices realize \(d\). For \(m=3\), apply Theorem 1 and vary the eight \(B\)-starts. For \(m<3\), the same descending equations freely prescribe all \(n-3\) changes; the remaining \(3-m\) unused \(A\)-bits and the \(m\) \(B\)-bits supply exactly \(2^{3-m+m}=8\) starts. In particular there are exactly \(8(n-2)\) good starts and eight monochromatic starts per such order. The exterior-parity theorem is the special case \(A=V\).

**Theorem 2 (exact affine syndrome criterion).** More generally, suppose the ordered-face colors are affine Boolean functions of their fixed exterior bits. For each fixed direction order \(p\), write its change map as \(d(x)=Mx\oplus b\in\mathbb F_2^s\), where \(s=n-3\) and \(M\) has rank \(\rho\). Let \(H\) be any \((s-\rho)\times s\) matrix of full row rank with \(HM=0\), so \(\ker H=\mathrm{im}M\). Then a good geodesic with this direction order exists **if and only if**
\[
 Hb\in\{0,He_1,\ldots,He_s\}.
\]
Its number of good starting vertices is exactly
\[
 2^{n-\rho}\Bigl|\{0,e_1,\ldots,e_s\}\cap(b+\mathrm{im}M)\Bigr|.
\]
**Proof.** An attainable change vector is precisely an element of the affine coset \(b+\mathrm{im}M=\{v:Hv=Hb\}\), and every such vector has \(2^{n-\rho}\) preimages. The words of Hamming weight at most one are exactly \(0,e_1,\ldots,e_s\). \(\square\)

The syndrome test proves the codimension-at-most-one affine criterion immediately: when \(s-\rho\le1\), the syndromes of zero and the unit vectors cover the entire syndrome space. In dimension six, an affine coloring failing every antipodal geodesic must therefore have \(\mathrm{rank}(M_p)\le1\) for **every** direction order \(p\), an explicit rank-rigidity condition. For larger codimension, the missing syndrome \(Hb\) is the exact linear obstruction for a specified order.

All assertions here are unconditional on antipodal oddness. They concern the stated subclasses and per-order certificates; the grand ordered-three-face conjecture remains unresolved.

## Recent consequences and compatibility conditions

# Reduction of the odd-flipper frontier to seven dimensions

Suppose \(c\) is an antipodal-reversal-odd ordered-three-face coloring of \(Q_n\) and all but exactly six coordinates are universal exterior flippers. Write the six remaining coordinates \(B\), and \(r=n-6\). If \(r\) is even, the earlier parity-six closure theorem applies.

If \(r\) is odd, choose one flipper \(g\in A\) and put \(A'=A\setminus\{g\}\), so \(|A'|=r-1\) is even. Restrict to the seven-dimensional subcube with directions \(B\cup\{g\}\), fixing all \(A'\)-coordinates to zero, to define \(c'\). By the universal-flipper identity and even parity of \(|A'|\), the induced \(c'\) is antipodal-reversal-odd: reversing within the seven-dimensional subcube and complementing all fixed \(A'\)-bits changes the color by \(1\oplus |A'|=1\). The direction \(g\) remains a universal exterior flipper in \(c'\).

Apply the exact flipper lifting lemma to the set \(A'\): any one-change antipodal geodesic in \(c'\) lifts to a one-change antipodal geodesic in \(c\).

**Seven-dimensional bottleneck theorem.** To prove NORI for every coloring in every dimension having at most six nonflipper coordinates, it suffices to prove NORI for the class of \(Q_7\) colorings with *one universal exterior flipper*. Combined with the already proved even-flipper and five-nonflipper theorems, this is the sole outstanding configuration for that entire structured class.

The restriction is a sufficient reduction; it does not assert that arbitrary NORI counterexamples possess any universal flipper.



*Exact scoped proof in note* note_rooted_restriction_and_good_root_density_limitations.
