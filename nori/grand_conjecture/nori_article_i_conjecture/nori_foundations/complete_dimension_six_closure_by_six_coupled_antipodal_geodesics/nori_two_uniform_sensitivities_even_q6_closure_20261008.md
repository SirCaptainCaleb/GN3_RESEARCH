# Two uniform exterior sensitivities force Q6 closure; affine bad residuals are one-juntas

# Two uniform exterior sensitivities force a good Q6 geodesic

Let \(B=\{a,b,c,d,e,f\}\), and let \(h\) be a binary ordered-three-face coloring on \(Q_B\) satisfying reversal-even antipodality
\[
h(\bar F,\operatorname{rev}\pi)=h(F,\pi).
\]
An ordered triple \((a,b,c)\) is **uniformly sensitive** in an exterior direction \(t\in B\setminus\{a,b,c\}\) if toggling the fixed \(t\)-bit always complements its color, independently of the other exterior bits.

**Theorem (two-flipper sensitivity closure).** If some ordered triple \((a,b,c)\) is uniformly sensitive in two distinct exterior directions \(d,e\), then \(h\) has a full six-coordinate antipodal geodesic with at most one color change.

**Proof.** Suppose instead that *every* complete six-direction geodesic is bad. Let \(f\) be the remaining exterior direction. Apply the previously established uniform complementary-face collapse lemma first with the distinguished exterior direction \(d\), then with \(e\).

The \(d\)-collapse supplies a constant \(K_d\) and, for every exterior assignment,
\[
h(d,a,b)=K_d,\qquad h(d,f,e)=K_d.
\tag{1}
\]
The first equality uses reversal-evenness to reverse the forced triple \((b,a,d)\).

The \(e\)-collapse supplies a constant \(K_e\) and the universal identities
\[
h(d,f,e)=K_e,\qquad
h(b,c,e)=K_e,\qquad
h(c,e,f)=1\oplus K_e.
\tag{2}
\]
Here \((d,f,e)\) is one of the four complementary-triple orientations forced by sensitivity in \(e\). Comparing (1) and (2) gives \(K_d=K_e=:K\).

Now take the complete direction order
\[
(d,a,b,c,e,f).
\tag{3}
\]
Its four window colors, at their actual face positions, are
\[
\big(K,\ h(a,b,c),\ K,\ 1\oplus K\big),
\tag{4}
\]
by (1) and (2), with the displayed constant entries valid for **all** initial bits. The second window has the free directions \(a,b,c\); the previously crossed direction \(d\) is fixed outside it. By uniform \(d\)-sensitivity, toggling the initial \(d\)-bit complements only its second-window color among the four entries in (4), because the other three entries are constants. Choose that bit so the second color equals \(K\). We obtain
\[
(K,K,K,1\oplus K),
\]
with exactly one change, a contradiction. \(\square\)

**Corollary (one-junta rigidity of affine residuals).** Let \(h\) be a reversal-even ordered-three-face coloring of \(Q_6\) such that the color of each ordered face is an affine Boolean function of its three exterior bits. If every six-direction geodesic has at least two color changes, then for each ordered triple \(\pi\), the exterior-bit function \(h(F,\pi)\) depends on **at most one** of its three exterior coordinates.

**Proof.** Every nonzero Boolean derivative of an affine function equals 1 everywhere. Two distinct nonzero exterior coefficients would therefore give two uniform sensitivities, contradicting the theorem. \(\square\)

**Impact on NORI.** A one-universal-flipper NORI coloring of \(Q_7\) has a reversal-even six-dimensional residual. If that residual is affine and no six-direction residual path is good, the residual is necessarily a collection of Boolean one-juntas (one exterior input per oriented triple). Each nonconstant one-junta additionally forces the universal face-constant blocks of the complementary-face collapse lemma. This reduces the affine six-residual frontier to a much more rigid, explicitly finite class. It does not yet prove that all one-junta residuals are coordinate-only or that the general seven-dimensional NORI conjecture holds.
