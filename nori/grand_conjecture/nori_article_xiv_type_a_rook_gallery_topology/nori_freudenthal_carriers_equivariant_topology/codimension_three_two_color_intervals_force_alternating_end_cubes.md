# Codimension-three two-color intervals force alternating end-cubes

Let \(c:E(Q_n)\to\mathbb F_2\) be an arbitrary antipodally odd coloring. Suppose the coloring has no monochromatic full antipodal geodesic. Call an oriented pair \((u,v)\) *bi-monochromatic* if there are dimension-simple geodesics of each color joining \(u\) to \(v\). Let \(D=\{i:u_i\ne v_i\}\) and \(S=[n]\setminus D\). The endpoints agree on all dimensions of \(S\). The restriction to the \(|S|\)-face through \(u\) with directions \(S\) is denoted \(F_u\), and similarly \(F_v\). Antipodal complementation maps \(F_u\) onto \(F_v\).

**Theorem 1 (residual monochromatic-path exclusion).** If \((u,v)\) is bi-monochromatic and \(|S|=k\ge2\), then neither \(F_u\) nor \(F_v\) admits a monochromatic geodesic of length \(k-1\) starting at the respective endpoint \(u\) or \(v\).

*Proof.* Suppose \(F_v\) has a monochromatic color-\(a\) geodesic \(v\to w\) of length \(k-1\), using all but one direction of \(S\). Choose a color-\(a\) geodesic from \(u\) to \(v\), available by bi-monochromaticity. Concatenate it with \(v\to w\) and append the single unused direction of \(S\). The resulting path traverses all \(n\) dimensions once, and its first \(n-1\) edges have color \(a\). Thus it has at most one switch; the established root-slide criterion makes it a monochromatic full antipodal geodesic, contrary to hypothesis. The proof at \(u\) is symmetric: reverse a length-\((k-1)\) monochromatic geodesic starting at \(u\), prepend it to a matching-color geodesic \(u\to v\), and append the remaining direction of \(S\) at \(v\). \(\square\)

The case \(k=2\) recovers the near-spanning bi-monochromatic exclusion of the preceding Subsection, since any positive-length one-step path is monochromatic. The first nontrivial residual case is \(k=3\).

**Lemma 2 (opposite-corner two-step rigidity in a 3-cube).** Let \(F\cong Q_3\) have any binary edge coloring. Suppose that from each of two opposite corners \(p\) and \(p^\dagger\), every geodesic of length two changes color. Then a single bit \(a\) determines the entire coloring of \(F\): an edge whose endpoints have Hamming weights \(r,r+1\) relative to \(p\), for \(r=0,1,2\), has color
\[
\boxed{a+r\pmod2.}
\tag{1}
\]
In particular all six squares of \(F\) have curvature zero, and the three successive Hamming layers of edges have respective colors \(a,1-a,a\).

*Proof.* Label the three directions \(1,2,3\), put \(p=000\), and let \(a_i=c(0,e_i)\). For \(i\ne j\), write \(b_{i,j}=c(e_i,e_i+e_j)\). The no-monochromatic-two-step condition at \(000\) forces
\[
b_{i,j}=1-a_i.
\tag{2}
\]
For each \(k\), let \(t_k\) denote the color of the edge from the doubleton \([3]\setminus\{k\}\) to the top vertex \(111\). Reading a two-step geodesic from \(111\) first in dimension \(k\), then to singleton \(i\), where \(i\ne k\), gives
\[
b_{i,j}=1-t_k,\quad \{i,j,k\}=[3].
\tag{3}
\]
Equations (2)--(3) imply \(a_i=t_k\) whenever \(i\ne k\). With three directions, these equalities force all six values \(a_i,t_k\) to have one common value \(a\). Equation (2) then forces every middle-layer edge to have color \(1-a\). The opposite-layer colors are both \(a\), establishing (1). Every square has two edges of color \(a+r\) and two of color \(1-a-r\), so its edge-color XOR (curvature) vanishes. \(\square\)

**Theorem 3 (codimension-three alternating fence).** Let \(n\ge4\), and suppose \((u,v)\) is bi-monochromatic with \(d(u,v)=n-3\). Under the hypothetical absence of a monochromatic full antipodal geodesic, the colorings of the opposed 3-faces \(F_u,F_v\) are forced into complementary Hamming-layer patterns:
\[
\boxed{
\begin{array}{c|ccc}
\text{layer measured from }u\text{ or }v &0\to1&1\to2&2\to3\\ \hline
F_u &a&1-a&a\\
F_v &1-a&a&1-a
\end{array}}
\tag{4}
\]
for one bit \(a\). Both faces are square-flat: all their 2-face curvatures vanish.

*Proof.* By Theorem 1 with \(k=3\), no length-two geodesic from \(u\) within \(F_u\) is monochromatic. The same holds from \(v\) within \(F_v\). Antipodal oddness maps \(F_u\) onto \(F_v\), and maps \(u^\dagger\), the corner opposite \(u\) within \(F_u\), to \(v\). Therefore the no-monochromatic-two-step property also holds at \(u^\dagger\). Apply Lemma 2 to the two opposite corners of \(F_u\), obtaining its three layer colors \(a,1-a,a\). Antipodal oddness then determines the pattern in \(F_v\): complementation reverses the layer index \(r\mapsto2-r\), and complements the edge bit, giving \(1-a,a,1-a\). Flatness follows from Lemma 2. \(\square\)

**Corollary 4 (local rank-two double-color diamonds).** Under the hypotheses of Theorem 3, for any distinct \(i,j\in S\), the two cube vertices \(u\oplus e_i\) and \(u\oplus e_j\) admit monochromatic geodesics of both colors between them: the route through \(u\) has color \(a\) and the route through \(u\oplus e_i\oplus e_j\) has color \(1-a\). The analogous statement holds on \(F_v\), with its two colors interchanged.

*Proof.* This follows immediately from the three-layer pattern (4). \(\square\)

**Scope and forward implication.** Theorem 3 is an all-dimensional necessary local condition for a hypothetical counterexample possessing a bi-monochromatic interval of rank \(n-3\). It does not show that such an interval exists in every coloring, nor does it contradict the global no-closure hypothesis by itself. Its content is substantially stronger than a switch-count bound: it forces all 24 edges of the two opposed three-faces, and in particular their six square curvatures per face, into an alternating flat pattern. Thus a chain-level Wu--Yang construction can treat high-rank bi-monochromatic intervals as local flat boundary carriers with rigid opposite-polarity phases, rather than arbitrary overlapping red-blue paths. The remaining challenge is to control their attachments to the \((n-3)\)-dimensional interval directions.
