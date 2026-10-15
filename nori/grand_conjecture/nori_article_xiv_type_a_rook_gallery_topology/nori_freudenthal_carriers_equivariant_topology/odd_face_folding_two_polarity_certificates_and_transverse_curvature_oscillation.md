# Odd face folding, two-polarity certificates, and transverse curvature oscillation

# Odd face folding, two-polarity certificates, and transverse curvature oscillation

Select distinct dimensions \(a,b\) of a legally antipodally odd binary-colored \(Q_n\), with \(n\ge4\), and set \(m=n-2\). Let \(F_{00}\cong Q_m\) be the face where the \(a,b\) bits are zero and \(F_{11}\) its opposing face. Antipodality sends \((z,00)\) to \((\bar z,11)\). The coloring \(f\) induced on \(F_{00}\) is arbitrary; its opposing face has the color-complemented antipodal image.

## Theorem 1 (odd folding and the two-polarity equivalence)

For any \(q:Q_m\to\mathbb F_2\) satisfying \(q(\bar z)=1-q(z)\), identify the two opposite \(m\)-faces with the two sides of a folded \(Q_{m+1}\), and assign color \(q(z)\) to the formal joining edge \((z,00)(z,11)\). The folded cube coloring is antipodally odd.

For an arbitrary coloring \(f\) of \(Q_m\), set
\[
T_f(u)=\{t\in\mathbb F_2:\text{there is an antipodal geodesic from }u
\text{ to }\bar u\text{ with word }t^*(1-t)^*\}.
\tag{1}
\]
Empty runs are permitted. Then
\[
\boxed{\text{the folded cube has a monochromatic full geodesic}
\ \Longleftrightarrow\ \exists u:\ q(u)\in T_f(u),}
\tag{2}
\]
and
\[
\boxed{T_f(\bar u)=\{1-t:t\in T_f(u)\}.}
\tag{3}
\]
For each fixed \(f\),
\[
\boxed{\text{every odd choice of }q\text{ yields a monochromatic folded geodesic}
\ \Longleftrightarrow\ \exists u:\ T_f(u)=\{0,1\}.}
\tag{4}
\]
Consequently **NORI1 in dimension \(m+1\)** is equivalent to: *Every arbitrary binary edge coloring of \(Q_m\) has some vertex supporting both a \(0^*1^*\) and a \(1^*0^*\) antipodal full geodesic.*

*Proof.* A monochromatic folded geodesic may be reversed so that it begins in \(F_{00}\), crosses its formal joining edge at vertex \(u\), and ends in \(F_{11}\). If its color is \(t=q(u)\), let its first segment in \(F_{00}\) run from \(z\) to \(u\) in color \(t\). Reverse that segment to obtain \(u\to z\) in color \(t\). Its last segment \(u\to\bar z\) in the second face transforms, by antipodal translation and reversal, into a color-\((1-t)\) segment \(z\to\bar u\) in \(F_{00}\). These two segments use disjoint dimension sets and concatenate to the certificate in (1). Conversely, given a face path \(u\to z\to\bar u\) with colors \(t\) then \(1-t\), reverse its first segment, traverse the formal joining edge at \(u\) in color \(t=q(u)\), and translate and reverse the second segment to form a folded monochromatic full path. This proves (2). Reversal of a face path proves (3). If \(T_f(u)=\{0,1\}\), any odd assignment \(q\) matches a certificate at that \(u\). If no \(T_f(u)\) contains both colors, choose \(q(u)\) outside \(T_f(u)\) independently on every antipodal vertex pair; (3) makes these choices compatible with oddness, and (2) yields no monochromatic folded full path. This proves (4). Every legally colored \(Q_{m+1}\) is a folded coloring by taking the two facets opposing across one dimension, proving the final equivalence. \(\square\)

## Theorem 2 (one-exception lifting, conditional on the induction hypothesis)

Assume NORI1 holds in dimension \(n-1=m+1\). Then every legally colored \(Q_n\) has a full dimension-simple geodesic with all but at most one edge of the same color:
\[
\boxed{t^n\quad\text{or}\quad t^p(1-t)t^{n-p-1}.}
\tag{5}
\]
If no monochromatic full geodesic exists, then \(1\le p\le n-2\).

*Proof.* For each \(z\in Q_m\), let \(M(z)\) be the set of colors for which a two-step diagonal path from \((z,00)\) to \((z,11)\) using \(a,b\) once is monochromatic. Antipodal reversal gives \(M(\bar z)=\{1-t:t\in M(z)\}\). Choose the folded joining color \(q(z)\) from \(M(z)\) whenever this set is nonempty, and choose it arbitrarily and oddly elsewhere. The \((n-1)\)-dimensional induction hypothesis gives a folded monochromatic full geodesic of color \(t\) crossing at \(u\), with \(q(u)=t\). If \(M(u)\ne\varnothing\), our choice ensures that a color-\(t\) two-step diagonal path replaces the joining edge, giving an all-\(t\) full geodesic in \(Q_n\). If \(M(u)=\varnothing\), both two-step diagonal paths have one edge of each color, so replacement gives a full geodesic with one exceptional edge, as in (5). The replaced dimensions occur nowhere else in the path. An exceptional edge at the first or last position gives at most one switch, which root-slide rotation converts into a monochromatic full geodesic. \(\square\)

## Theorem 3 (opposite-majority full paths at a common joining square)

Assume the \((n-1)\)-dimensional induction hypothesis, and suppose there is no monochromatic full geodesic in the original \(Q_n\). At some \(u\in F_{00}\) the arbitrary face coloring satisfies \(T_f(u)=\{0,1\}\). Its joining square in dimensions \(a,b\) cannot have a monochromatic diagonal two-step path of **either** color: combining that route with the corresponding face certificate via Theorem 1 would produce a monochromatic full geodesic in \(Q_n\). Therefore both diagonal routes are bichromatic. Applying the construction for the two face polarities separately gives a full \(n\)-geodesic with \(n-1\) red edges and one blue edge, and another with \(n-1\) blue edges and one red edge, traversing the **same** joining square. The two folded color assignments are allowed to differ.

## Theorem 4 (gate and stripe obstruction, with run bounds)

Assume the hypotheses of Theorem 3. Since neither diagonal two-step route across the joining square is monochromatic, the two words are either \(10,10\), or \(01,01\), or \(01,10\). Call these respectively *gate 10*, *gate 01*, and *stripe*. Every such square has curvature zero. The gate has opposite colors on each pair of parallel edges and nonzero corner-root defect transport; the stripe has equal-colored parallel pairs and vanishing corner-root transport.

If the two face-polarity certificates at \(u\) have words
\[
0^r1^{m-r},\qquad 1^s0^{m-s},
\]
then, in the absence of a monochromatic full \(Q_n\) geodesic, **every** such pair obeys
\[
\boxed{
\begin{array}{c|c}
\text{joining square}&\text{required conditions}\\
10,10&r\ge1,\quad s\le m-1\\
01,01&r\le m-1,\quad s\ge1\\
01,10&1\le r,s\le m-1.
\end{array}}
\tag{6}
\]

*Proof.* Each two-step diagonal path is bichromatic, so its word is \(01\) or \(10\). The curvature is the xor of both two-step word parities, hence zero. If the first face certificate has word \(0^r1^{m-r}\), its folded color-zero path expands to \(0^r h_1h_2 0^{m-r}\), where \(h_1h_2\) is either available square word. For \(h=10\) this has at most one switch when \(r=0\); for \(h=01\) it has at most one switch when \(r=m\). Similarly the color-one certificate gives \(1^s h_1h_2 1^{m-s}\), which has at most one switch when \(h=10,s=m\) or when \(h=01,s=0\). The root-slide lemma then forbids the corresponding endpoint cases. When both words occur, all endpoint cases are excluded. The gate/stripe parallel-edge assertions follow by direct inspection of the four square-edge colors and the root-defect identity in Subsection 31. \(\square\)

## Theorem 5 (monochromatic face paths force gates and transverse-curvature oscillation)

Assume no monochromatic full geodesic exists in \(Q_n\). Let \(P=(v_0,\ldots,v_m)\) be a monochromatic **red** full geodesic inside \(F_{00}\), with \(m=n-2\), using all remaining dimensions once. At **every** \(v_j\), the two portions of \(P\), read outward, are red geodesics with disjoint dimension sets partitioning the \(m\) face dimensions. The two-arm residual-square lemma of Article XIV, Subsection 41, therefore forces the joining square in \(a,b\) at each \(v_j\) to be a *gate 10*: both outgoing \(a,b\)-edges are blue, and the two edges entering the opposite corner are red. Stripes are impossible along \(P\).

At either chosen endpoint \(u\) of \(P\), the monochromatic face geodesic supplies **both** face-polarity certificates, by allowing one run to be empty. Choosing \(u=v_0\), the two expansions through the gate may be taken with words
\[
\boxed{0^m10\qquad\text{and}\qquad10\,1^m,}
\tag{7}
\]
whose unique minority edges occur at positions \(n-1\) and \(2\), respectively.

Let \(d_j\) be the dimension of the edge \(v_{j-1}v_j\), and for \(h\in\{a,b\}\) define
\[
W^{(h)}_j=\kappa(F_{\{h,d_j\}}(v_{j-1})),
\qquad 1\le j\le m.
\tag{8}
\]
The gate condition implies that each curvature word \(W^{(h)}\) is the edge-color word of the shifted copy \(P+h\): the side square has one red base edge and two blue connecting edges, whose contributions cancel modulo two. For \(k=\{a,b\}\setminus\{h\}\), adjoining a blue initial \(h\)-edge, traversing \(P+h\), then adjoining the red terminal \(k\)-edge gives a full dimension-simple antipodal geodesic with word
\[
\boxed{1\,W^{(h)}\,0.}
\tag{9}
\]
If \(W^{(h)}\) contains no \(01\), then (9) has at most one switch and gives NORI1 by a root slide. Applying the same construction to reversed \(P\) forces an occurrence of \(10\). Therefore
\[
\boxed{\text{Both }W^{(a)},W^{(b)}\text{ contain }01\text{ and }10.}
\tag{10}
\]
This is the transverse-curvature oscillation theorem from Article XIV, Subsection 47, now shown to be the precise obstruction along the **two transverse paths separating the folded one-exception lifts**. On each side square the red Freudenthal exchange defect is zero and the blue defect equals the curvature, as proved in that subsection.

**Scope.** The folding equivalence does not establish NORI1; Theorems 2–3 require the \((n-1)\)-dimensional NORI1 induction hypothesis. The curvature oscillation in Theorem 5 is conditional on a monochromatic full path within one of the \((n-2)\)-faces, which the induction hypothesis alone does not supply: its two-polarity certificates may have both nonempty color runs. The remaining proof problem is to derive similarly strong strip constraints from two distinct strict one-switch certificates at a common vertex, or to show that the defect-bearing joining squares cannot be compatible across multiple choices of dimension pairs.

## Proposition 7 (the transverse strip identity for arbitrary face paths)

The curvature connection admits a formula without any monochromatic hypothesis. Let \(P=(v_0,\ldots,v_m)\) be any dimension-simple path contained in the \((n-2)\)-face \(F_{00}\), with edge dimensions \(d_1,\ldots,d_m\) and color word \(w_1,\ldots,w_m\). For either unused dimension \(h\in\{a,b\}\), put
\[
h_j=c(\{v_j,v_j\oplus e_h\}),\qquad
w_j^{(h)}=c(\{v_{j-1}\oplus e_h,v_j\oplus e_h\}),
\]
and let \(\kappa_j^{(h)}\) be the square curvature on the \(\{h,d_j\}\)-face joining the two corresponding edges. Then the following **pointwise strip equation** holds:
\[
\boxed{w_j^{(h)}=w_j+\kappa_j^{(h)}+h_{j-1}+h_j\pmod2.}
\tag{11}
\]
Its sum along the entire strip is
\[
\boxed{\sum_{j=1}^m\kappa_j^{(h)}
=\sum_{j=1}^m(w_j+w_j^{(h)})+h_0+h_m\pmod2.}
\tag{12}
\]

*Proof.* The four boundary edges of the \(j\)-th side square have respective bits \(w_j,w_j^{(h)},h_{j-1},h_j\), whose mod-two sum equals \(\kappa_j^{(h)}\). Solving for \(w_j^{(h)}\) gives (11). Summing (11) cancels every interior connecting-edge color \(h_j\) twice, giving (12). \(\square\)

Thus the **corrected transverse curvature word**
\[
\widehat W_j^{(h)}=\kappa_j^{(h)}+h_{j-1}+h_j
\tag{13}
\]
equals the xor \(w_j+w_j^{(h)}\) of the base and translated color words. The gate corridor from Theorem 5 forces every \(h_j=1\) along a red monochromatic \(P\), so \(\widehat W^{(h)}=\kappa^{(h)}=w^{(h)}\). This is why the earlier two-sided oscillation applies directly to ordinary curvature.

For a **strict one-switch** face certificate obtained only from Theorem 1's induction hypothesis, the transverse connecting-edge bits \(h_j\) need not be constant, and the base word \(w\) is not constant. Equation (11) shows the additional information that must be controlled to extend the oscillation theorem: ordinary curvature alone need not equal the translated color word. The required next statement would couple both one-switch face certificates at the common vertex to force compatible restrictions on the transverse connecting-edge profiles. This is an open step, not a consequence of the folding equivalence.

## Adjacent face polarities force stripes and gates force empty roots

The two-polarity construction also couples certificates lying in different adjacent faces. This gives a stronger local condition than paired-root exclusion at a gate's neighboring corners.

Fix two omitted directions \(a,b\), put \(R=[n]\setminus\{a,b\}\), and identify each face \(F_{\alpha\beta}\) with \(Q_R\). Let \(g_{\alpha\beta}\) be its ordinary edge coloring. Antipodal oddness gives
\[
g_{11}(r)=1-g_{00}(\bar r),\qquad
g_{10}(r)=1-g_{01}(\bar r)
\]
on corresponding edges. Ordinary path reversal gives \(A_1(g)=\overline{A_0(g)}\). Consequently
\[
\boxed{
A_t(g_{00})=A_t(g_{11}),\qquad
A_t(g_{01})=A_t(g_{10})\quad(t=0,1).
}
\tag{CP1}
\]

Write \(p_0,p_1\) for the \(a\)-edge colors at \(b=0,1\), and \(q_0,q_1\) for the \(b\)-edge colors at \(a=0,1\), in the residual square over \(r\).

**Lemma (two-step certificate lift).** A full face path from \(r\) with word \(t^*(1-t)^*\), together with a color-\(t\) two-step diagonal route in the residual square from that face to its opposite face, gives a monochromatic color-\(t\) full geodesic of \(Q_n\).

*Proof.* Split the face order at its monotone seam. Reverse the first segment, traverse the two omitted directions along the diagonal route at \(r\), and follow the antipodally translated reversed second segment in the opposing face. The original first segment has color \(t\), and the translated second segment has color \(t\) by oddness. The directions of the two horizontal segments are disjoint and exhaust \(R\), and the middle route uses \(a,b\) once each. The endpoints are antipodal. \(\square\)

**Theorem (cross-profile stripe rigidity).** Suppose \(Q_n\) has no monochromatic full geodesic. If
\[
\boxed{r\in A_0(g_{01})\cap A_1(g_{00}),}
\tag{CP2}
\]
then its residual square is a stripe:
\[
\boxed{p_0=p_1,\qquad q_0=q_1,\qquad p_0\ne q_0.}
\tag{CP3}
\]
The same conclusion holds with the orientations reversed, or with any adjacent pair of faces.

*Proof.* The nondecreasing certificate in \(F_{01}\) excludes both color-zero diagonals from corner \(01\). The nonincreasing certificate in \(F_{00}\) excludes both color-one diagonals from corner \(00\). By the lifting lemma these give
\[
(p_1\lor q_1),\quad(q_0\lor p_0),\quad
(\neg p_0\lor\neg q_1),\quad
(\neg q_0\lor\neg p_1).
\tag{CP4}
\]
If \(p_0=0\), the second clause forces \(q_0=1\), the fourth forces \(p_1=0\), and the first forces \(q_1=1\). If \(p_0=1\), the third forces \(q_1=0\), the first forces \(p_1=1\), and the fourth forces \(q_0=0\). These are the two stripes. Reversing color and face roles proves the other cases. \(\square\)

For a coloring with a nonstripe residual square and certificates (CP2), one of the four forbidden monochromatic routes in (CP4) exists. The proof therefore constructs a full monochromatic path with \(a,b\) consecutive; the theorem does not rely on a dimension induction.

**Corollary (paired-to-empty propagation at a gate).** In a bad odd coloring, suppose \(r\in P(g_{00})\) and its joining square is a gate. Then
\[
\boxed{
r,\bar r\notin A_0(g_{01})\cup A_1(g_{01}).
}
\tag{CP5}
\]
The same conclusion holds for the other adjacent face \(g_{10}\).

*Proof.* A nondecreasing adjacent-face certificate would combine with the nonincreasing \(g_{00}\)-certificate to force a stripe. A nonincreasing adjacent certificate would combine with the nondecreasing \(g_{00}\)-certificate to do the same. A gate is not a stripe, so neither adjacent orientation exists. Reversal makes emptiness antipodally invariant; (CP1) handles the opposing adjacent face. \(\square\)

There is also a direct route interpretation: at a gate's adjacent corners, one diagonal route is monochromatic zero and the other monochromatic one. Either face orientation at that corner would therefore lift to a monochromatic full path. Thus the adjacent root is empty even without first supplying a paired certificate at the gate corner.

**Corollary (empty neighboring roots along a monochromatic face corridor).** Under Theorem 5, every vertex \(v_j\) of its monochromatic face geodesic is a root admitting neither monotone orientation in either adjacent translated face. The gate corridor supplies a monochromatic diagonal of each color from the adjacent face corner, and the lifting lemma excludes both orientations.

This strengthens the earlier statement that adjacent gate corners cannot be paired: they cannot support either full monotone orientation. Their rooted interaction structure must therefore evade the rootwise rooted-tree feedback coverage theorem.

### A local odd-cycle certificate

For a full cube vertex \(x\), make a graph \(K_x\) on the direction set. Join \(a,b\) whenever, at the remaining-bit root of \(x\), the face through \(x\) and an adjacent parallel face have opposite full monotone certificates. By (CP1), toggling \(a\) or \(b\) gives the same adjacent-face profile, so this definition is symmetric in \(a,b\).

In a bad coloring, the stripe theorem forces
\[
\boxed{\{a,b\}\in E(K_x)\Longrightarrow c_a(x)\ne c_b(x).}
\tag{CP6}
\]
Hence \(K_x\) is bipartite, colored by the incident edge bits. Conversely, an odd cycle in some \(K_x\) supplies an edge whose incident bits agree, making its residual square a nonstripe; (CP4) then constructs a monochromatic full path. This is a local contradiction certificate. A proof that such a cycle must occur has not been obtained; full interleaving clauses remain part of the general completion problem.

**Independent reconstruction.** An unrelated evaluator constructed 1338 certificate lifts across two-step routes in odd cubes of dimensions four through six and directly checked their complete direction orders, edge colors, and antipodal endpoints. The stripe and gate statements follow from the four displayed Boolean clauses in every dimension.


**Corollary (antipodal empty-corridor bound).** Put \(m=n-2\ge1\). If a bad odd coloring has a monochromatic full geodesic in one \(m\)-face, then each adjacent parallel \(m\)-face coloring \(g\) satisfies
\[
\boxed{
|\{r:r\notin A_0(g)\cup A_1(g)\}|\ge2m,\qquad
|A_0(g)\cup A_1(g)|\le2^m-2m.
}
\tag{CP7}
\]
In particular \(|A_0(g)|\le2^m-2m\).

*Proof.* Every one of the \(m+1\) corridor vertices is empty by the gate propagation rule. The empty-root set is antipodally invariant. A dimension-simple full geodesic's vertex set intersects its antipodal translate only in its two endpoints: a proper nonempty direction prefix cannot equal the complement of another prefix. Their union therefore has \(2(m+1)-2=2m\) vertices. \(\square\)

Thus an adjacent fiber with every root admitting at least one orientation, including the rootwise rooted-tree feedback class, rules out such a monochromatic corridor in a bad coloring. The bound applies in every dimension and preserves the positions of all corridor roots; it supplies a quantitative constraint for coupling them to the critical repair witnesses.
