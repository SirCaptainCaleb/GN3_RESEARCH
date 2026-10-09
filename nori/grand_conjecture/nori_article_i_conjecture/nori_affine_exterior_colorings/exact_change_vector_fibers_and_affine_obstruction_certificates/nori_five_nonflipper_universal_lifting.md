# Full-dimensional one-change closure with at most five nonflipper directions

# Dimension-free closure with at most five nonflipper directions

Let \(c\) be **any** binary coloring of ordered three-faces of \(Q_n\); no antipodal symmetry is required. Say that a direction \(a\) is a *universal exterior flipper* if whenever \(a\) is fixed outside the free triple of an ordered face, complementing its fixed face bit complements the color, with the other exterior coordinates fixed.

**Theorem.** If there is a set \(A\) of universal exterior flippers such that \(|V\setminus A|\le5\), then some full antipodal geodesic has at most one color change.

**Proof.** Put \(B=V\setminus A\) and write \(r=|A|\), \(m=|B|\). For \(n\le5\), unrestricted dimension-five closure (including the elementary smaller cases) already gives a good geodesic. Assume \(n\ge6\), so \(r\ge1\).

First let \(3\le m\le5\). The flipper property decomposes every face color as
\[
c(F,\pi)=\bigoplus_{a\in A\setminus\mathrm{free}(F)}x_a(F)\ \oplus\
h(\pi,x_{B\setminus\mathrm{free}(F)}),
\]
where \(h\) is an arbitrary ordered-three-face coloring on \(Q_m\). For \(m=5\), the unrestricted five-dimensional lemma supplies an \(m\)-direction order \(\tau\) and a starting \(B\)-vertex \(y\) whose residual window word has at most one change. For \(m=3,4\), any residual word already has at most one change. Choose any order \(\sigma\) of \(A\) and use the full order \(\sigma\tau\). The exact universal-flipper fiber theorem shows that, with \(y\) held fixed, the \(r\) initial change bits can be independently prescribed by the \(r\) initial bits in \(A\), while the final \(m-3\) changes equal the residual change vector of \((\tau,y)\). Prescribe every initial change bit to be zero. The resulting full geodesic has at most one change.

If \(m\le2\), take all \(A\)-directions first. Every difference between successive window colors is of the form
\[
d_i=G_i\oplus G_{i+1}\oplus1\oplus z_i
\oplus\mathbf 1_{i+3\le r}z_{i+3},\qquad i=1,\ldots,n-3,
\]
where \(z_i\) are the initial \(A\)-bits and the \(G_i\) are independent of all of them. Solving successively for \(z_{n-3},\ldots,z_1\) makes every \(d_i=0\), yielding a monochromatic full geodesic. \(\square\)

**Consequence.** A counterexample to NORI must have **at least six directions which fail to be universal exterior flippers**. This necessary condition holds for arbitrary cube dimension. The threshold five is sharp for this particular residual-geodesic lifting argument: unrestricted ordered-three-face colorings on \(Q_6\) can lack a one-change path, although this does not imply that such a coloring admits a NORI counterexample after adding a flipper.
