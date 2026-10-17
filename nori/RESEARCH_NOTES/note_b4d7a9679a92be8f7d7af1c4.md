# Middle-level favorable-root shells and index-one root topology under complete direction interaction

- Stable ID: note_b4d7a9679a92be8f7d7af1c4
- Author: unspecified; session provenance retained
- Primary home: subsection:cartesian_factorization_of_paired_roots_and_interaction_prime_reduction
- Labels: NORI1, middle-levels, antipodal-index, topology, paired-roots, dimension-uniform
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11059_1
- Updated session: session_nori_r11059_1
- Disposition: none
- Successor: none

## Related references

- subsection:cartesian_factorization_of_paired_roots_and_interaction_prime_reduction

## Research note

## Middle-level roots and topology of antipodal favorable sets

Let \(a_i(x)=\bigoplus_{j\ne i}x_j\) define an undirected-edge coloring of \(Q_m\). Each rule ignores its own direction bit and depends on every other direction; the undirected interaction graph is complete. Let \(A(a)\) be the set of starting vertices of full antipodal geodesics with nondecreasing color word \(0^K1^{m-K}\), and \(P(a)=A(a)\cap\overline{A(a)}\).

**Theorem 1 (middle-level root characterization).** For \(m=2h+1\),
\[
A(a)=P(a)=\{x:|x|=h\text{ or }h+1\}.
\tag{ML1}
\]
For \(m=2h\),
\[
A(a)=\begin{cases}
\{x:|x|=h\text{ or }h+1\}&h\text{ even},\\
\{x:|x|=h-1\text{ or }h\}&h\text{ odd},
\end{cases}
\qquad P(a)=\{x:|x|=h\}.
\tag{ML2}
\]
Every admitted root has a witness whose direction order is obtained by arranging its starting vertex bits into a specified alternating pattern.

*Proof.* Let \(p=|x|\bmod2\), and let \(\pi\) be a full direction order. Immediately before step \(k\), the total parity has changed by \(k-1\bmod2\), while the \(\pi_k\)-th starting bit is unchanged. Thus its edge color is \(w_k=p\oplus(k-1\bmod2)\oplus x_{\pi_k}\). The required profile \(w_k=[k>K]\) forces
\[
x_{\pi_k}=p\oplus(k-1\bmod2)\oplus[k>K].
\tag{ML3}
\]
The word \(((k-1\bmod2)\oplus[k>K])_{k=1}^m\) contains \(h+1\) ones for even \(K\), or \(h\) for odd \(K\), when \(m=2h+1\); when \(m=2h\) the respective counts are \(h\) and \(h-1\). For even \(p\) the forced starting word has this weight, while for odd \(p\) its weight is the complement. Requiring \(|x|\equiv p\pmod2\) gives the displayed layers. Conversely, for every weight in the displayed list, choose a permitted cut \(K\) and rearrange the starting bits to satisfy (ML3). In odd dimension, antipodal translation leaves every \(a_i\) unchanged; hence \(A(a)=\overline{A(a)}\). In even dimension, intersecting the two adjacent levels with their antipodal images leaves the central level. \(\square\)

Given any vertex subset \(V\subseteq Q_m\), let \(\mathcal K(V)\) be the cubical complex consisting of all faces of \(Q_m\) whose vertices belong to \(V\).

**Theorem 2 (complete interaction with cohomological index one).** For every odd \(m=2h+1\ge3\), \(\mathcal K(P(a))\) is the connected middle-level graph between the weights \(h\) and \(h+1\). Its vertex number, edge number, and integral first Betti number are
\[
|V|=2\binom{2h+1}{h},\qquad |E|=(h+1)\binom{2h+1}{h},\qquad
b_1=(h-1)\binom{2h+1}{h}+1.
\tag{ML4}
\]
Antipodal complementation acts freely on the realization. Its double-cover characteristic class \(\omega\in H^1(\mathcal K(P(a))/\tau;\mathbb F_2)\) satisfies
\[
\omega\ne0,\qquad \omega^2=0.
\tag{ML5}
\]
In particular the cohomological index stays one, although the cube dimension grows without bound and the direction-interaction graph is complete.

*Proof.* No two-dimensional cube face lies in just two consecutive Hamming-weight levels, so the induced cubical complex is one-dimensional. Each weight-\(h\) vertex has \(h+1\) neighbors of weight \(h+1\), giving the edge count. Two weight-\(h\) subsets differing by one exchange connect through their union; the Johnson exchange graph is connected, hence so is the middle-level graph. Its first Betti number is \(|E|-|V|+1\). For \(m\ge3\), antipodality neither fixes a vertex nor exchanges the endpoints of any graph edge, so its action on the realization is free. The covering is nontrivial because the covering graph is connected. Its quotient is again a graph and has vanishing second cohomology. Therefore its nonzero covering class squares to zero. \(\square\)

**Theorem 3 (arbitrarily high-dimensional torus root complexes).** Let \(b_r\) on \(Q_{3r}\) be the Cartesian product of \(r\) copies of the three-dimensional coloring from Theorem 1. Then
\[
\mathcal K(P(b_r))\cong(S^1)^r,\qquad
H_j(\mathcal K(P(b_r));\mathbb Z)\cong\mathbb Z^{\binom rj}\quad(0\le j\le r).
\tag{ML6}
\]
Antipodality acts as a half-turn in each circle factor; its quotient is a torus, and its associated double-cover class has cohomological index one.

*Proof.* The three-dimensional favorable and paired-root set is \(Q_3\setminus\{000,111\}\), whose induced graph is a six-cycle. The existing Cartesian favorable-root and paired-root factorization shows that the product coloring's paired-root set is the Cartesian product of these six-vertex sets. Faces supported on a vertex Cartesian product are products of supported factor faces, giving the cubical product of \(r\) circles. The homology is obtained by the Kunneth formula. Complementing the three bits moves each six-cycle vertex to the opposite vertex, inducing simultaneous half-turns on the torus. Its quotient is a torus, modeled as \(\mathbb R^r/(\mathbb Z^r+\mathbb Z(\frac12,\ldots,\frac12))\). Its nontrivial degree-one covering class squares to zero in the cohomology ring of a torus. \(\square\)

The theorems provide a constructive family of geodesic witnesses through (ML3). They also show that complete direction interaction and the paired-root property do not force favorable-root complexes to be contractible or to have cohomological index growing with ambient dimension. The results do not prove unrestricted paired-root existence.
