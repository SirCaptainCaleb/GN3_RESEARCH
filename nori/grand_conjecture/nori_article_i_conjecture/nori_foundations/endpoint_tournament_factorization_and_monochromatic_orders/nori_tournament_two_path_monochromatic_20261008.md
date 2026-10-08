# Tournament endpoint factorization admits a monochromatic geodesic

# Endpoint-tournament factorization yields monochromatic antipodal geodesics

Let \(V\) be a set of \(n\ge3\) coordinate directions, \(T\) an arbitrary tournament on \(V\), and \(s:V\to\mathbb F_2\) a function constant on \(V\setminus\{v\}\) for some \(v\in V\). Let \(t(a,c)\in\mathbb F_2\) be 0 when \(a\to c\) in \(T\) and 1 when \(c\to a\). Define the position-independent ordered-face coloring
\[
c(F,(a,b,c'))=t(a,c')\oplus s(b).
\]
(Here \(c'\) names the third direction, to distinguish it from the coloring \(c\).)

**Theorem (monochromatic tournament-factorized NORI).** This coloring satisfies antipodal-reversal oddness and admits a monochromatic full antipodal geodesic, for every \(n\ge3\).

**Balanced two-path lemma.** For every tournament \(T\) on \(n\ge3\) vertices and any distinguished vertex \(v\), there is an ordering \(p=(p_1,\dots,p_n)\) such that \(p_i\to p_{i+2}\) for all \(1\le i\le n-2\) and \(v\in\{p_1,p_n\}\).

**Proof of the lemma.** Every tournament has a directed Hamilton path: inductively insert a new vertex immediately before the first existing path vertex it dominates, or append it if it dominates none. Choose such a path \(q=(q_1,\ldots,q_n)\), with \(v=q_j\).

If \(n=2k\), at least one of the numbers \(j-1,n-j\) is at least \(k-1\). If \(n-j\ge k-1\), take the consecutive directed path \(q_j,\ldots,q_{j+k-1}\) as the odd-position subsequence \(p_1,p_3,\ldots,p_{2k-1}\). Then \(p_1=v\). If \(j-1\ge k-1\), take \(q_{j-k+1},\ldots,q_j\) as the even-position subsequence \(p_2,p_4,\ldots,p_{2k}\). Then \(p_n=v\). In either case, order the other \(k\) vertices by any directed Hamilton path in their induced tournament and place them in the vacant parity positions.

If \(n=2k+1\), at least one of \(j-1,n-j\) is at least \(k\). Take a directed consecutive \(q\)-segment of \(k+1\) vertices beginning or ending at \(v\), and place it in the odd positions \(p_1,p_3,\ldots,p_{2k+1}\); place a directed Hamilton path on the other \(k\) vertices in the even positions. Then \(v=p_1\) or \(v=p_n\), respectively.

In every case, each parity subsequence is a directed path, hence \(p_i\to p_{i+2}\) for all \(i\). \(\square\)

**Proof of the theorem.** Reversing an ordered triple swaps its outer directions; since \(t(c',a)=1\oplus t(a,c')\), we have
\[
c(\bar F,(c',b,a))=t(c',a)\oplus s(b)=1\oplus c(F,(a,b,c')).
\]
Apply the balanced two-path lemma to \(T\) with distinguished vertex \(v\). Along the resulting full coordinate order \(p\), the window at index \(i\) has color
\[
t(p_i,p_{i+2})\oplus s(p_{i+1})=s(p_{i+1}).
\]
All middle positions \(p_2,\ldots,p_{n-1}\) avoid \(v\), so this value is constant. Since the face coloring ignores exterior fixed bits, the starting cube vertex is arbitrary; every such starting vertex yields a monochromatic antipodal geodesic. \(\square\)

**Scope.** This solves a nontrivial all-dimensional subclass of coordinate-only, reversal-odd ternary colorings, including every endpoint-tournament labeling \(t(a,c)\) and every perturbation by a single exceptional middle direction. It does not treat general triangle-dependent ternary colorings or exterior-face-dependent NORI. The proof exhibits the potential usefulness of balanced two-path covers with prescribed extreme vertices as a replacement for one-switch endpoint repairs.
