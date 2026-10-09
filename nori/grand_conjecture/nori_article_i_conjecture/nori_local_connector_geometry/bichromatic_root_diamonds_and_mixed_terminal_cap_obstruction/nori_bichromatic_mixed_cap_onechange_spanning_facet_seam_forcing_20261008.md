# Uniform mixed caps impose equivariant opposite-seam constraints on every one-change near-spanning facet path

# One-change codimension-two cores force exact first- and last-seam obstructions

Let \(n\ge6\) and \(c\) be an active NORI coloring of ordered physical three-faces. Suppose we have a pair of omitted distinct directions \((a,c)\), a projected root \(r\) on \(U=[n]\setminus\{a,c\}\), and the **two uniform cap identities**
\[
c(F(x;\{a,c,i\}),(a,c,i))=1,\qquad
c(F(x;\{a,c,i\}),(c,a,i))=0
\quad\forall i\in U,
\tag{1}
\]
for every full root \(x\) with \(x|_U=r\). These identities hold at any no-common-edge bichromatic hub \(z\), with \(a\) in its certified color-0 class and \(c\) in its color-1 class, by Item \`nori_bichromatic_hub_mixed_cap_uniformity_forbids_all_nearspanning_cores_20261008\`.

Let \(P\) be any **actual** \((n-2)\)-edge \(U\)-spanning geodesic from one such root \(x\), with direction order
\[
p=(i,j,\ldots,k,\ell)
\]
and ordered-three-face color word containing at most one change. Denote its *initial* window bit by \(q\), its *final* window bit by \(s\), and its endpoint \(y=x\oplus\chi_U\). These two colors may coincide.

**Theorem (exact first- and last-seam blockers).** If no full one-change antipodal geodesic exists in \(Q_n\), the physical face colors associated with \(P\) must satisfy the following **four implications**:
\[
\begin{array}{rcl}
q=0&\Longrightarrow&c(F(x;\{a,i,j\}),(a,i,j))=1,\\
q=1&\Longrightarrow&c(F(x;\{c,i,j\}),(c,i,j))=0,\\
s=0&\Longrightarrow&c(F(y;\{k,\ell,c\}),(k,\ell,c))=1,\\
s=1&\Longrightarrow&c(F(y;\{k,\ell,a\}),(k,\ell,a))=0.
\end{array}
\tag{2}
\]
These statements are **equivariant under actual antipodal reversal** of \(P\), which sends the initial and final window bits to their complements, reverses the direction order, and exchanges the two exterior-facet roots \(x\mapsto x\oplus e_a\oplus e_c\).

**Proof.** If \(q=0\), prepend omitted directions \((c,a)\) before \(P\), selecting the new root \(x\oplus e_a\oplus e_c\). By (1), the first new window \((c,a,i)\) has color 0. The second new window is \((a,i,j)\) on the actual physical face \(F(x;\{a,i,j\})\): after the first new direction \(c\), the path is at \(x\oplus e_a\), a vertex of that face. The old first window has color \(q=0\). If this middle new color were also 0, *both* inserted windows would be 0 and the full path would retain at most the one old color change, contradicting global failure. Thus its color must be 1. This proves the first implication. If \(q=1\), instead prepend \((a,c)\): the first cap is 1, and its second window is \((c,i,j)\) on the physical face through \(x\); its bit must be 0 or a good full path results.

For a path whose **final** color \(s=0\), append \((c,a)\). The last window \((\ell,c,a)\) is the NORI antipodal-reversal complement of the cap \((a,c,\ell)\) through the initial root, and hence has color \(1-1=0\). The penultimate new window \((k,\ell,c)\) is at the physical face through the original endpoint \(y\). If it had color 0, no extra change would occur, giving a good full path. So it must be 1. For \(s=1\), append \((a,c)\); its final cap is the complement of \((c,a,\ell)\), hence 1, and the penultimate window \((k,\ell,a)\) must instead have color 0. These are the last two implications.

Under antipodal reversal \(\Theta P\), the new root is \(\overline{x\oplus U}=x\oplus\{a,c\}\) and the new endpoint is \(\bar x\). Its window word is the reversed complemented old word. The first implication for \(P\), for example, is carried to the final implication for \(\Theta P\) with \(s'=1-q=1\), because
\[
c(F(\bar x;\{j,i,a\}),(j,i,a))
=1-c(F(x;\{a,i,j\}),(a,i,j)).
\]
The other implications pair analogously, establishing equivariance. \(\square\)

**Corollary (mixed-prefix restrictions on the four-facet bundle).** Now assume the caps come from a no-common-edge bichromatic hub \(z\) with \(a\in A(z)\), \(c\in B(z)\), as above. Let \(i\in A(z)\setminus\{a\}\), \(j\in B(z)\setminus\{c\}\). If a one-change \(U\)-spanning path beginning \((i,j)\) exists from either \(x=z\) or \(x=z\oplus e_a\), its initial color **cannot** be 0: the first implication of (2) would assign 1 to the physical ordered face \((a,i,j)\), which literally equals the corresponding face through \(z\), whose middle-selector color is 0. Similarly, for \(i\in B(z)\setminus\{c\}\), \(j\in A(z)\setminus\{a\}\), a one-change \(U\)-spanning path beginning \((i,j)\) from \(x=z\) or \(x=z\oplus e_c\) **cannot** have initial color 1, since the second implication of (2) demands color 0 for \((c,i,j)\), while the mixed-middle selector assigns 1. In either case, any forbidden initial-color alignment already produces full grand closure by the explicit prepend operation.

**What is still open.** The theorem applies to *one-change* \((n-2)\)-geodesics, not to arbitrary long paths, and the exceptional seam colors in (2) can be simultaneously compatible with antipodal reversal. They constitute a genuine new **endpoint obstruction system**, rather than a stand-alone contradiction. A closure proof could arise by forcing, within one four-facet bundle, two root/path witnesses whose initial or terminal memory constraints assign opposite bits to the same physical ordered face, or from a topological connectedness/odd-holonomy theorem forbidding the consistent seam-blocker field. No such universal forcing theorem has yet been proved.
