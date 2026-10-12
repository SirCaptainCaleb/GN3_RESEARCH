# Graphic-nullity interval extraction and defect-weighted port cocircuit decoding

# Graphic-nullity extraction from polarized turn galleries

## 1. A matroid interval-partition lemma

Let \(N\) be a loopless matroid and let \(e_1,\ldots,e_m\) be an ordered sequence of distinct ground-set elements. Parallel resource occurrences are represented by separate parallel elements. Put
\[
\nu=m-r_N(\{e_1,\ldots,e_m\}).
\]

**Lemma 1.** The index interval \([m]\) admits a partition into at most \(\nu+1\) nonempty consecutive intervals, each of whose elements are independent in \(N\).

*Proof.* Traverse the sequence, extending the current independent block whenever possible. If \(e_j\) is dependent on the current block, cut immediately before \(j\) and restart with \(e_j\). The element \(e_j\) lies in the closure of the global prefix \(\{e_1,\ldots,e_{j-1}\}\), so the global rank does not increase at \(j\). Among the \(m\) positions there are precisely \(\nu\) non-rank-increasing indices, since \(N\) is loopless and the first position increases rank. Thus the number of cuts is at most \(\nu\). Each singleton restart is independent by looplessness. \(\square\)

## 2. Boundary-tournament path defects

Let \(t_1,\ldots,t_m\) be distinct ordered-triple states with legal consecutive transitions: each is either a forward transition
\[
(a,b,c)\longrightarrow(b,c,d),
\]
or a backward transition
\[
(a,b,c)\longrightarrow(d,a,b),
\]
where the four letters displayed in a transition are pairwise distinct. A binary coloring \(c(t_i)\) is arbitrary. Let \(s\) be the number of changes in the state-color word, and let \(h\) be the number of changes between forward and backward transition polarities, with \(h=0\) for \(m\le2\).

Cut at each polarity change, leaving at most \(h+1\) blocks of states. Reverse the order of every backward block. Each resulting block is the sequence of consecutive length-three windows of a word \(w\), of length equal to the number of states plus two. For each occurrence of a consecutive pair of letters in \(w\), use a separately labelled edge of the multigraph on the original resource alphabet. Since the word is a walk, its graphic nullity is
\[
\nu(w)=(|w|-1)-(|\operatorname{supp}(w)|-1)=|w|-|\operatorname{supp}(w)|.
\]
Let \(R\) be the sum of these nullities over all polarity-homogeneous blocks.

**Theorem 2 (lossless defect extraction).** The gallery contains a contiguous state interval of length at least
\[
\boxed{\left\lceil\frac{m}{1+s+h+R}\right\rceil}
\tag{1}
\]
whose states are monochromatic, whose transitions all have the same polarity, and whose decoded resource word has no repeated letter. Consequently, for an ordinary reversal-odd boundary tournament, there is a monochromatic forward vertex-simple tight path on at least
\[
\boxed{2+\left\lceil\frac{m}{1+s+h+R}\right\rceil}
\tag{2}
\]
original vertices.

*Proof.* Within each polarity block, orient its states forward. Greedily append triple windows to a current segment as long as the newly appended last letter is not already among that segment's resource letters. If repetition would occur, cut immediately before the new triple and restart at that triple. The new triple has three distinct letters. Every greedy cut is charged to a non-rank-increasing edge occurrence of the full resource walk, hence at most \(\nu(w)\) cuts are required in that block, by Lemma 1. Across all blocks there are at most \(h+R\) cuts. Additionally cut at the \(s\) color changes, obtaining at most \(1+s+h+R\) nonempty contiguous state segments. Every original state is retained; there is no deduction from the numerator \(m\). The largest segment has at least (1) states. Reversing a backward segment yields a forward triple-window word on the same distinct resources. Under reversal oddness, reversing the complete resource word complements every triple color, so a negative monochromatic word yields a positive one of the same length if needed. \(\square\)

## 3. Port-cocircuit extraction

Let \(D_{\rm BT}\) be the pointed binary dual of the alternating-port ordered-triple covering graph, and let \(X\in Z(D_{\rm BT})\) contain its port \(p\). Every port cocircuit is \(Y=C\cup\{p\}\), with \(C\) a simple odd-monodromy quotient-state cycle. Put \(r=|C|=|Y|-1\).

Every cyclic root and orientation \(\rho\) of \(C\) lifts to a state walk
\[
t_0,t_1,\ldots,t_r=Jt_0
\]
with \(r\) distinct quotient-state representatives \(t_0,\ldots,t_{r-1}\). Let \(s_\rho\) be the number of color changes among these \(r\) states, and let \(h_\rho,R_\rho\) be the polarity-change and resource-nullity defects of Theorem 2. Put
\[
\Delta(C)=\min_\rho(h_\rho+R_\rho).
\]

**Corollary 3 (defect-weighted port-cocircuit decoding).** Every \(Y\) and \(X\) as above yield a monochromatic vertex-simple tight path on at least
\[
\boxed{
2+\left\lceil\frac{|Y|-1}{|X\cap Y|+\Delta(C)}\right\rceil
}
\tag{3}
\]
original vertices.

*Proof.* The integer intersection \(w=|X\cap Y|-1\) counts all changed turns on the odd-monodromy closed cycle, while the rooted \(r\)-state path omits the closing turn. Hence \(s_\rho\le w\). Choose a root minimizing \(h_\rho+R_\rho\); Theorem 2 supplies a segment of length at least
\[
\left\lceil\frac r{1+s_\rho+h_\rho+R_\rho}\right\rceil
\ge \left\lceil\frac r{|X\cap Y|+\Delta(C)}\right\rceil.
\]
Translate triple-state count into the two additional vertices of its resource word. \(\square\)

The defect \(\Delta(C)\) depends on the directed resource-labelled covering presentation and is not an invariant of the abstract pointed matroid alone. Thus optimizing \(|X\cap Y|\) over all shortest port cocircuits cannot substitute for optimizing over admissible long-path representatives.

## 4. Parallel cube decoding

Let \(D_n\) denote the pointed matroid for an antipodally odd cube-edge coloring. For any port cocircuit \(Y=C\cup\{p\}\), put \(r=|C|\) and lift a cyclic root of \(C\) to \(r\) colored cube-edge states \(e_0,\ldots,e_{r-1}\), followed by the deck translate of \(e_0\). A consecutive turn specifies which endpoint its two cube-edge states share.

An internal edge state is a **stationary contact** if its preceding and following turns use the same endpoint of that cube edge. Let \(h_\rho\) be the number of such contacts in a rooted lift. Splitting the state sequence at the contacts yields coherent cube walks. For each coherent block, regard each occurrence of a coordinate direction as a different element in a parallel class of the partition matroid having capacity one for every coordinate. Let \(\nu_\rho\) be the sum of the nullities of these coordinate sequences. Let \(s_\rho\) be the number of internal color changes.

**Theorem 4 (common defect extraction).** For either the cube or the boundary covering, every port cocircuit \(Y=C\cup\{p\}\) and every admissible port cycle \(X\) yield a monochromatic resource-simple path of at least
\[
\boxed{\left\lceil\frac{|C|}{1+\min_\rho(s_\rho+h_\rho+\nu_\rho)}\right\rceil}
\tag{4}
\]
colored states. In the cube, this is a geodesic with that many edges; in the boundary model, this is a vertex-simple tight path with that many triple windows, hence two additional original vertices.

*Proof.* For the cube, divide the lifted sequence at stationary contacts to obtain coherent cube walks, with at most \(h_\rho\) cuts. The partition-matroid version of Lemma 1 divides each walk into at most one plus its coordinate-nullity many direction-distinct subwalks. Cuts at the \(s_\rho\) color changes complete a partition into no more than \(1+s_\rho+h_\rho+\nu_\rho\) nonempty monochromatic geodesic segments. The boundary case is Theorem 2, with its graphic resource matroid and transition-polarity defect. Optimize over cyclic roots and orientations. \(\square\)

**Corollary 5 (shortest cube port cocircuit).** If \(Y\) is a shortest port cocircuit of \(D_n\), so \(|C|=n\), then its lift is an antipodal geodesic: the cube-distance lower bound eliminates stationary contacts and repeated directions. Thus \(h_\rho=\nu_\rho=0\). If \(|X\cap Y|=2\), the cyclic turn word has one changed turn; root the cycle at that turn, leaving \(n\) consecutive monochromatic cube edges. This is the monochromatic-geodesic conclusion of NORI1 for that \(X\).

Theorem 4 and Corollary 3 are unconditional extraction statements. They do not establish the existence of a sufficiently long, sufficiently low-defect port cocircuit.

## 5. Defect-bounded selector target

The pair of canonical systems motivates a pointed signed-cover matroid equipped with an oriented path language and an auxiliary resource matroid. A proposed global selector principle asks for port cocircuits with growing turn length while controlling the sum
\[
\boxed{\text{color intersection}+\text{coherence defect}+\text{resource nullity}.}
\]
Its substantive missing component is an existence theorem producing such cocircuits uniformly in ambient size. The auxiliary data cannot simply be discarded: the marked-cocircuit counterexamples in Article XI show that low intersection without forward coherence and resource simplicity does not produce the desired boundary tight path.

## 6. Cyclic seam optimization and contact-curvature coupling

The defect extraction of Theorem 4 can be sharpened by treating cyclic roots as choices of an omitted closing turn, rather than bounding the number of internal switches independently.

Let \(Y=C\cup\{p\}\) be any port cocircuit of a signed line-cover dual, let \(r=|C|\), and lift its odd-monodromy cycle to edge states
\[
e_0,e_1,\ldots,e_{r-1},e_r=Je_0.
\]
Indices of projected states and turns are taken modulo \(r\). Write \(\omega_i\in\{0,1\}\) for the color disagreement on the turn \(e_i--e_{i+1}\) and \(w=\sum_i\omega_i=|X\cap Y|-1\). Let \(v_i\) denote the contact vertex of that turn; set \(v_{-1}=Jv_{r-1}\). Define
\[
z_i=\mathbf 1_{\{v_{i-1}=v_i\}},\qquad
\sigma=\sum_{i=0}^{r-1}z_i.
\tag{5}
\]
Thus \(z_i=1\) when the two cyclic contacts of the edge state \(e_i\) use the same endpoint.

**Theorem 6 (cyclic seam-defect identity).** Root the lifted cycle immediately after turn \(i\), omitting that turn from the resulting \(r\)-state path. Let \(s_i\) be its internal color-change count, and \(h_i\) its internal stationary-contact count. Then
\[
\boxed{s_i=w-\omega_i,\qquad
h_i=\sigma-z_i-z_{i+1},}
\tag{6}
\]
and therefore
\[
\boxed{
\min_i(s_i+h_i)
=w+\sigma-\max_i(\omega_i+z_i+z_{i+1}).}
\tag{7}
\]
Consequently
\[
\min_i(s_i+h_i)\le
w+\sigma-
\left\lceil\frac{w+2\sigma}{r}\right\rceil.
\tag{8}
\]
The formula holds in either canonical model. In the ordered-triple covering, the internal stationary-contact count \(h_i\) equals the number of changes between forward and backward transition polarities.

*Proof.* Omitting turn \(i\) deletes its color-change contribution \(\omega_i\) from the cyclic sum \(w\). The rooted state path begins at \(e_{i+1}\) and ends at a deck translate of \(e_i\); its internal states are all the other \(r-2\) cyclic states. Precisely the two endpoint-state stationary indicators \(z_{i+1}\) and \(z_i\) are excluded, proving (6). Taking minima proves (7). Summing the seam benefits over all \(i\) gives \(\sum_i(\omega_i+z_i+z_{i+1})=w+2\sigma\), so their maximum is at least the ceiling of their mean, yielding (8).

For the boundary model, a forward triple-overlap transition traverses the middle covering edge from its tail to its head, while a backward transition traverses it oppositely. At an internal triple state, successive transition polarities agree if and only if the preceding and following contacts use opposite endpoints. Thus a polarity change is equivalent to a stationary contact. \(\square\)

The two-port orientation-curvature construction already present in Article XI records \(\sigma\bmod2\) as the intrinsic line-graph contact-curvature class \(\kappa_G(C)\). Equations (6)–(8) refine that parity-only invariant to an integer contact profile and isolate the role of the closing seam. If \(\nu_i\) is the resource-matroid nullity defect at root \(i\), the sharp denominator supplied by Theorem 4 is
\[
\boxed{1+w+\sigma-\max_i(\omega_i+z_i+z_{i+1}-\nu_i).}
\tag{9}
\]
This equality is a restatement of the optimized color/coherence/nullity defect, but it is useful because the first three contributions to the seam score are local and the global obstruction is concentrated in \(\nu_i\).

## 7. Trimmed-defect extraction and recovery of the marked-seam bound

In the tournament model, a distinguished twisted-closing cocircuit of length \(m\) contains \(m-2\) forward, resource-simple triple states and two auxiliary seam states. Computing the nullity of the full \(m\)-state lift can charge resource repetitions introduced solely by these seams. The following interval variant removes that avoidable loss.

**Corollary 7 (cyclic-interval selector bound).** Let \(Y=C\cup\{p\}\) be a port cocircuit in either canonical model, and let \(X\) be a port cycle. Choose any cyclic lift and any contiguous interval \(I\) of \(\ell\le |C|\) lifted colored states, with \(\ell\ge1\). Define \(s(I)\), \(h(I)\), and \(\nu(I)\) by the same color, stationary-contact/polarity, and resource-matroid rules as Theorem 4, but counting only the selected interval. Then the instance has a monochromatic resource-simple path with at least
\[
\boxed{
\left\lceil\frac{\ell}{1+s(I)+h(I)+\nu(I)}\right\rceil
}
\tag{10}
\]
colored states. Accordingly one may maximize this quantity over all cyclic roots, orientations, and contiguous intervals of any length.

*Proof.* The chosen interval is itself an admissible state walk, so the partition proof of Theorem 4 applies without change. \(\square\)

**Corollary 8 (the marked boundary seam estimate is retained).** For a twisted closing cycle associated with an injective \(m\)-vertex word \(v\), choose the original \(m-2\) forward triple states and omit the two auxiliary seam states. The selected interval has \(h(I)=\nu(I)=0\), and its internal color changes are at most
\[
w=|X\cap Y|-1.
\]
Therefore it contains a monochromatic vertex-simple tight path on at least
\[
\boxed{2+\left\lceil\frac{m-2}{|X\cap Y|}\right\rceil}
\tag{11}
\]
vertices. In particular intersection at most four implies the earlier bound \(2+\lceil(m-2)/4\rceil\). The full-cycle defect-weighted estimate and the trimmed estimate are complementary: neither should replace the other when optimizing a family of cocircuits.

*Proof.* The original word has distinct resources, and its forward triple states are consecutive windows. No polarity changes or resource dependencies occur inside this interval. Its internal color changes are a subset of the nonzero turn labels of the sealed cycle. Apply (10) and translate state count to vertex count. \(\square\)

This interval formulation suggests a more flexible global selector target: rather than demanding low defect for an entire long port cocircuit, seek a cocircuit that contains a **long low-defect resource interval**. In particular the same criterion incorporates NORI1's full-geodesic interval after removing the unique switched closing seam and the tournament's forward tight subword after discarding its auxiliary closing states.
