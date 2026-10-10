# NORI2 sentinel barrier and exact one-switch examples

# NORI2 sentinel barrier: all directed pair rules and sharp one-switch examples

## Stronger theorem: no symmetry of the ordinary pair rule is needed

**Theorem 0 (directed one-sentinel closure).** Fix \(n\ge3\) and one coordinate \(s\), and put \(D=V(Q_n)\setminus\{s\}\). Suppose an arbitrary binary coloring \(c\) of genuine ordered physical two-faces obeys only:

1. On every ordered square \((u,v)\) with \(u,v\in D\) and with the exterior fixed \(s\)-bit equal to 0, its color is some fixed **directed** pair function \(h(u,v)\), independent of all other exterior bits. No relation is assumed between \(h(u,v)\) and \(h(v,u)\).
2. On every ordered square with \(s\) **last**, \(c(F,(u,s))=0\), independent of all exterior bits.

There are **no** conditions on ordered squares with \(s\) first or on ordinary ordered squares with fixed exterior \(s\)-bit 1. Nevertheless, there is a full antipodal geodesic whose consecutive ordered-square color word changes at most **once**. The assertion does not require NORI legality.

More generally, replace the constant 0 in hypothesis 2 by any common bit \(b\); the same conclusion holds, choosing the reverse color-run orientation.

**Proof.** On \(D\) form the complete symmetric digraph with arc \(u\to v\) colored \(h(u,v)\). By Raynaud's 1973 theorem, this two-colored complete symmetric digraph has a directed Hamiltonian cycle which is the union of a color-0 directed path and a color-1 directed path (either color may be absent). Cutting this cycle at a suitable edge yields a Hamiltonian **path** \(q=(q_1,\ldots,q_{n-1})\) whose arc-color word has the **prescribed order**
\[
1,\ldots,1,\;0,\ldots,0.
\tag{D1}
\]
Indeed, if both colors occur, the cyclic arc-color word has exactly two monochromatic runs; delete its last color-0 arc before the start of the color-1 run. The remaining directed path starts with its 1-run and ends with its 0-run. If a color is absent, any cut gives a monochromatic path. For terminal color \(b=1\), reverse the choice of transition, obtaining \(0,\ldots,0,1,\ldots,1\).

Choose a cube root \(x\) with \(x_s=0\) and traverse the full direction order
\[
q_1,\ldots,q_{n-1},s.
\tag{D2}
\]
Every ordinary pair window is a **physical** square with exterior \(s\)-bit still 0, hence has its prescribed \(h\)-color from (D1). The final ordered square \((q_{n-1},s)\) has color 0 by hypothesis 2. The complete physical window word is therefore a block of 1s followed by a block of 0s, including the terminal 0; there is at most one switch. Distinctness of the directions and root consistency are immediate. \(\square\)

**Legal NORI2 corollary.** In particular, for an **arbitrary asymmetric** \(h\) on ordinary directed pairs, define a legal ordered-physical-square coloring by
\[
c(F,(u,v))=
\begin{cases}
h(u,v),& u,v\in D,\ z_s(F)=0,\\
1-h(v,u),&u,v\in D,\ z_s(F)=1,\\
1,&u=s,\\
0,&v=s.
\end{cases}
\tag{D3}
\]
Antipodal complementation flips the fixed exterior \(s\)-bit on ordinary squares and reversal swaps the ordered pair, so these clauses complement. When \(s\) belongs to the face, reversal interchanges its first and last positions and flips 1/0. Thus (D3) satisfies the exact legal law
\(c(\bar F,(v,u))=1-c(F,(u,v))\) on every physical square. Theorem 0 gives a full antipodal geodesic with at most one switch. This strictly strengthens the symmetric \(h\) theorem below.

**Sharpness.** The existing clique-plus-star symmetric \(h\) example of Theorem B below is a member of (D3) and forces at least one switch for \(n\ge5\). Thus one switch is best possible even in the wider asymmetric family.

**Finite independent checks.** Exhaustively enumerate all directed functions \(h:D^{(2)}\to\{0,1\}\) for \(|D|=4\) and \(|D|=5\), all full direction orders, and both choices of the root \(s\)-bit in (D3). In the first case, among \(2^{12}=4096\) functions, 4076 admit a monochromatic full geodesic and the remaining 20 have minimum exactly one switch. In the second, among \(2^{20}=1,048,576\) functions, 1,046,626 admit zero switches and 1950 require exactly one. None requires two; the general proof is independent of these checks.

**Scope.** Theorem 0 improves the previously known \(t+1=2\) bound for the one-exterior-direction NORI2 family when the terminal special-direction square is constant, even if the ordinary pair rule is wholly asymmetric. It does **not** prove the unrestricted NORI2 one-switch conjecture: general ordered squares meeting \(s\) may have arbitrary exterior-bit dependence, and arbitrary ordinary squares may depend on many ordinary exterior bits. Any one-sentinel counterexample within the finite-support framework must violate the uniform terminal-square hypothesis (or the flat ordinary-pair hypothesis) of Theorem 0.

**Literature.** H. Raynaud (1973), *Sur le circuit hamiltonien bi-colore dans les graphes orientés*, Periodica Mathematica Hungarica 3, 289–297; see A. Gyárfás, *Vertex covers by monochromatic pieces — a survey of results and problems*, Theorem 2, for the explicit complete-symmetric-digraph formulation, https://www.renyi.hu/~gyarfas/Cikkek/172_krakowrev3.pdf.

## Earlier symmetric-pair theorem and further subclasses

## Main theorem

**Theorem A (complete one-sentinel family).** Let \(n\ge3\). Fix one distinguished coordinate \(s\), and let \(D=V(Q_n)\setminus\{s\}\) denote the set of the other **coordinate directions**. Let \(h:D^{(2)}\to\{0,1\}\) be any symmetric binary function of two distinct ordinary directions:
\[
h(u,v)=h(v,u).
\]
For an ordered physical two-face \(F\) with ordered free directions \((u,v)\), define
\[
c(F,(u,v))=
\begin{cases}
z_s(F)\oplus h(u,v),&s\notin\{u,v\},\\
1,&u=s,\\
0,&v=s.
\end{cases} \tag{1}
\]
Then (1) satisfies the antipodal-reversal law, and there is a full antipodal geodesic whose consecutive two-face colors change at most **once**.

This applies to arbitrary symmetric direction-pair rules, arbitrary direction multiplicities/classes, and any ambient dimension. Thus the direct one-sentinel mechanism that gives unbounded obligatory changes for NORI3 **cannot disprove the proposed one-switch NORI2 bound**.

**Proof of legality.** For a square avoiding \(s\), its antipodal square has the opposite fixed \(s\)-bit; reversing the ordered pair preserves \(h\). For squares containing \(s\), reversal exchanges the two clauses 1 and 0. The color is independent of traversal corner in all cases. \(\square\)

## Two-color complete-graph path lemma

**Lemma (Gerencsér–Gyárfás, with elementary proof).** Every red/blue coloring of the edges of a finite complete graph admits a Hamiltonian path whose edge-color word changes at most once.

**Proof.** Maintain disjoint red and blue paths \(R\) and \(B\) covering the vertices handled so far; a path of one vertex is permitted, and either path may be empty. The invariant is initially trivial. Let \(v\) be the next vertex. If one path is empty, append \(v\) to the nonempty path when their joining edge has its designated color, otherwise create the other path as singleton \(v\). If both are nonempty, let \(r,b\) be their final vertices. If \(vr\) is red, append \(v\) to \(R\). If \(vb\) is blue, append \(v\) to \(B\). Otherwise \(vr\) is blue and \(vb\) red. If \(rb\) is red, remove \(b\) from the blue path \(B\) and extend \(R\) by the consecutive edges \(rb,bv\), both red. If \(rb\) is blue, remove \(r\) from \(R\) and extend \(B\) by \(br,rv\), both blue. In all cases the paths remain disjoint, monochromatic in their respective colors, and now cover one more vertex. By induction they partition the complete vertex set.

If both paths are nonempty, concatenate \(R\) and \(B\) using their one joining edge. Its color is necessarily red or blue, so the concatenated Hamiltonian path has a red segment followed by a blue segment, with at most one change. If one path is empty, the other is already a monochromatic Hamiltonian path. \(\square\)

This lemma is the classical 1967 Gerencsér–Gyárfás path-partition theorem; the constructive proof above is included to make the NORI consequence self-contained.

**Proof of Theorem A.** Apply the lemma to the complete graph on the ordinary directions \(D\), coloring each edge \(\{u,v\}\) by \(h(u,v)\). Choose an ordering \(q=(q_1,\ldots,q_{n-1})\) whose pair-color word
\[
H=(h(q_1,q_2),\ldots,h(q_{n-2},q_{n-1}))
\]
has at most one change. Traverse the \(n\) coordinates in the order \((s,q_1,\ldots,q_{n-1})\). The first ordered square has free directions \((s,q_1)\) and color 1. After the first step, the fixed \(s\)-bit is \(1-z\), where \(z\) is the root's initial \(s\)-bit. All later square-window colors equal
\[
1\oplus z\oplus H_1,\;\ldots,\;1\oplus z\oplus H_{n-2}.
\]
Choose the starting vertex with \(z=H_1\) (all other root bits arbitrary). The initial two square colors are then both 1, and the remainder has exactly the color changes of \(H\). Hence the full square-color word has at most one change. \(\square\)

## Sharpness inside the one-sentinel family

**Theorem B.** For every \(n\ge5\), there is a coloring of the form (1) for which every full antipodal geodesic has at least one change. Thus the universal bound of Theorem A is exact for this family.

**Proof.** Partition the \(n-1\) ordinary directions into \(A\sqcup\{b\}\) with \(|A|=n-2\ge3\), and set \(h(u,v)=0\) for \(u,v\in A\), and \(h(u,b)=h(b,u)=1\) for \(u\in A\). The color-0 complete-graph edges form a clique on \(A\) and isolate \(b\). The color-1 graph is a star centered at \(b\), with at least three leaves. Neither graph contains a Hamiltonian path, so for **every** order \(q\) of the ordinary directions, its adjacent-pair color word \(H\) has at least one change.

For a full cube geodesic with \(s\) in the first position, its later ordinary pair windows give \(H\) up to uniform complementation, and therefore at least one change. The same holds if \(s\) is last. If \(s\) is at an interior position, the two successive square windows containing \(s\) have free-direction orders \((u,s)\) and \((s,v)\) and colors \(0,1\), giving an unavoidable change. Thus every root and every full direction order has at least one switch. By Theorem A, some full path has exactly one. \(\square\)

## Further comparison: direction-only legal NORI2 colorings

**Theorem C.** Suppose a legal physical ordered-two-face coloring is independent of all fixed exterior face bits, so \(c(F,(u,v))=g(u,v)\) depends only on the ordered free directions. Then there is a **monochromatic** full antipodal geodesic.

**Proof.** Legality gives \(g(v,u)=1-g(u,v)\); hence \(u\to v\) whenever \(g(u,v)=1\) defines a tournament on the coordinate directions. Every tournament has a directed Hamiltonian path (Rédei's theorem). For completeness, the elementary insertion proof starts with one directed path; a new vertex can be inserted at its beginning if it dominates the first vertex, at its end if dominated by the last, or between two successive vertices where the preceding vertex dominates it and it dominates the following vertex. Inserting vertices successively yields a directed Hamiltonian path. Traversing its direction order gives color 1 in every consecutive square, at any root. \(\square\)

## Scope and implications for the proposed switch hierarchy

Theorem B realizes the predicted NORI2 budget of one exactly; Theorem A shows that any attempted amplification based solely on a reversal-even pair rule and a single exterior sentinel bit necessarily collapses to that budget. In contrast, the higher odd-\(k\) construction uses a central triple with a local-minimum run-count obstruction. The obstruction has no analog for a symmetric *pair* rule because the two-colored complete graph admits a Hamiltonian order with at most one color change.

These are exact statements for two explicitly defined subfamilies of legal colorings. They do **not** establish the unrestricted NORI2 conjecture: arbitrary physical two-face colors may depend on many exterior coordinates, and no direction-only complete-graph reduction then applies. Likewise they do not settle unrestricted NORI1; the NORI1 path-rotation mechanism concerns antipodally odd physical edges rather than ordered squares.

Literature: L. Gerencsér and A. Gyárfás (1967), the red/blue vertex-disjoint path-partition theorem; L. Rédei (1934), the tournament Hamiltonian-path theorem.
