# Same-root reversal produces internally disjoint antipodal geodesics with complementary reversed color words

# Every geodesic has a disjoint antipodally color-conjugate partner

Let \(c\) satisfy the active NORI condition \(c(\bar F,\operatorname{rev}\pi)=1-c(F,\pi)\). For root \(x\in Q_n\) and coordinate order \(p=(p_1,\ldots,p_n)\), write \(P(x,p)\) for the directed antipodal geodesic and \(w(x,p)\) for its \((n-2)\)-symbol binary ordered-three-face color word.

**Theorem (same-root reversal duality).** For every root \(x\) and every permutation \(p\),
\[
w(x,\operatorname{rev}p)
=\mathbf 1-\operatorname{rev}w(x,p).
\]
The two geodesics \(P(x,p)\) and \(P(x,\operatorname{rev}p)\) have precisely their endpoints \(x,\bar x\) in common; their interior vertex sets are disjoint. Consequently they have identical numbers of color changes. A monochromatic \(q\)-geodesic always has an internally disjoint monochromatic \((1-q)\)-partner with the same endpoints. Every one-switch geodesic has an internally disjoint one-switch partner.

**Proof.** The three free directions of window \(i\) along \(P(x,p)\) are \((p_i,p_{i+1},p_{i+2})\). Window \(n-1-i\) along \(P(x,\operatorname{rev}p)\) has those same free directions in reverse order. If \(j\notin\{p_i,p_{i+1},p_{i+2}\}\), then its exterior coordinate is flipped in exactly one of the two paths by the start of these respective windows: the first path has flipped \(p_1,\ldots,p_{i-1}\), whereas the reversed-order path has flipped \(p_n,\ldots,p_{i+3}\). These sets partition the exterior coordinates. Hence these two windows occupy antipodal three-faces and have reversed direction orders, so the NORI axiom gives complementary colors. This proves the word identity and equality of switch counts.

The interior vertices of \(P(x,p)\) have the form \(x\oplus\{p_1,\ldots,p_k\}\) for \(1\le k<n\). Those of \(P(x,\operatorname{rev}p)\) have the form \(x\oplus\{p_{n-\ell+1},\ldots,p_n\}\) for \(1\le\ell<n\). A nonempty proper prefix of a permutation cannot equal a nonempty proper suffix, because the former contains \(p_1\) and excludes \(p_n\) if proper, whereas the suffix contains \(p_n\) and excludes \(p_1\) if proper, except that suffixes of length n-1 contain \(p_1\)? For a suffix of length n-1, it excludes only \(p_1\), so still distinct. More abstractly, equality of prefix and suffix of the same cardinality \(k=\ell\) would require the first \(k\) and last \(k\) distinct direction sets to coincide, impossible for \(0<k<n\) (their complements would also coincide). Thus their only common vertices are the endpoints. \(\square\)

**Structural meaning.** The global NORI claim is equivalent to the existence of a *pair of internally disjoint conjugate* one-switch antipodal geodesics, since any single witness automatically supplies its partner. The symmetry does not imply that a bad prescribed root becomes good; both paths retain the same root and number of switches. Its usefulness lies in converting any prospective closure witness into a two-corridor connector with complementary reversed color profiles, which may support symmetric exchange arguments or directed reachability extraction.
