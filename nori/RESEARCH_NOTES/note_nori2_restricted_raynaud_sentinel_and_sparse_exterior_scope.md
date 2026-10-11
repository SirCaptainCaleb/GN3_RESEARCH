# Restricted NORI2 Raynaud–sentinel theorems and finite-exterior-support bounds

- Stable ID: note_nori2_restricted_raynaud_sentinel_and_sparse_exterior_scope
- Author: Editorial transfer from exact source manuscripts
- Primary home: section:nori_foundations
- Labels: theorem, approach, scope
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r4593_2
- Updated session: session_nori_r4593_2
- Disposition: none
- Successor: none

## Related references

- subsection:bounded_nori2_switches_from_finite_exterior_coordinate_support, exact version 1
- subsection:nori2_sentinel_barrier_and_exact_one_switch_examples, exact version 2

## Research note

# Restricted NORI2 results: scope and disposition

These complete positive special-family proofs are retained as reference material, not as an independently prioritized universal NORI2 publication line. They do not imply unrestricted NORI1 closure or resolve the ordinary boundary 3-tournament problem. The exact former published compositions follow verbatim.


---

## Transferred Subsection: Bounded NORI2 switches from finite exterior-coordinate support

Exact old composition v1
Original manuscript `bounded_nori2_switches_from_finite_exterior_coordinate_support`

# Bounded NORI2 switches from finite exterior-coordinate support

## Theorem

Let \(V\) be the \(n\) coordinate directions of \(Q_n\), let \(S\subseteq V\) have \(t\) elements, and put \(D=V\setminus S\). Suppose a binary coloring \(c(F,(u,v))\) is defined on **physical ordered squares** and has the following exterior-support property:

**(ES)** For every two ordered distinct directions \(u,v\in D\), the value \(c(F,(u,v))\) depends only on the ordered pair \((u,v)\) and on the \(t\) fixed bits \(z_S(F)\) of \(F\) in directions in \(S\). In particular it is independent of all other exterior fixed bits. There is no condition whatsoever on colors of squares meeting \(S\).

**Theorem (finite-support NORI2 bound).** Under (ES), there exists a full antipodal geodesic whose ordered-square color word has at most
\[
\boxed{t+1}
\]
switches. This holds for every \(n\) and every such physical coloring, with **no antipodal-reversal hypothesis needed**. Consequently it holds for legal NORI2 colorings satisfying (ES).

In particular:
- One distinguished exterior direction, allowing *arbitrary directed* pair rules and arbitrary colors of squares containing that direction, guarantees at most two changes.
- Two distinguished exterior directions, allowing arbitrary nonlinear interactions of their exterior bits and arbitrary square colors meeting either direction, guarantee at most three changes.
- Every family with an exterior dependence support of fixed size \(t\) has a switch budget bounded independently of ambient dimension.

The sharp previously established one-switch theorem for a **symmetric pair rule with one sentinel** is stronger under its additional hypotheses. The present bound is intentionally independent of reversal symmetry of the ordinary pair function.

## Raynaud's directed two-color Hamiltonian path theorem

**Lemma (Raynaud, 1973; Hamilton path consequence).** Let \(D\) be a finite set, and arbitrarily color each **ordered pair** \((u,v)\), \(u\ne v\), red or blue. There is a Hamiltonian vertex order \((q_1,\dots,q_m)\) in which the consecutive arc-color word
\[
h(q_1,q_2),\dots,h(q_{m-1},q_m)
\]
has at most one change.

**Proof from Raynaud's theorem.** Raynaud's directed result says that every red/blue arc coloring of a complete symmetric digraph has a directed Hamiltonian cycle expressible as one red directed path and one blue directed path (monochromatic cases permitted). The edge colors therefore form at most two monochromatic runs cyclically. Delete one arc at a transition between those runs. The remaining directed Hamiltonian path has at most one switch. If the cycle is monochromatic, delete any arc. For \(m\le2\), the claim is immediate.

This directed lemma allows \(h(u,v)\) and \(h(v,u)\) to be completely unrelated; the undirected Gerencsér–Gyárfás path-partition lemma only covers symmetric \(h\). Raynaud's theorem is a published external input. One source explicitly stating it is A. Gyárfás, *Vertex covers by monochromatic pieces — a survey*, Theorem 2, which attributes the directed Hamiltonian-cycle result to Raynaud (1973). The same result appears as Theorem 2.1 in Ben-Eliezer et al., *The size Ramsey number of a directed path*, Journal of Combinatorial Theory, Series B **102** (2012).

## Proof of the NORI2 theorem

Let \(S=(s_1,\dots,s_t)\) be any order of the special directions. Fix any initial cube vertex \(x\). After traversing each member of \(S\) once, the fixed \(S\)-bit vector on subsequent ordinary squares is
\[
 \beta = \bigl(1-x_{s_1},\dots,1-x_{s_t}\bigr).
\]
By (ES), for each ordered pair \(u,v\in D\) the color of **every physical square** with ordered free directions \((u,v)\) and fixed \(S\)-bits \(\beta\) is a well-defined bit
\[
 h_\beta(u,v)\in\{0,1\}. \tag{1}
\]
No symmetry is assumed between \(h_\beta(u,v)\) and \(h_\beta(v,u)\).

Apply Raynaud's lemma to this 2-coloring of all directed arcs on \(D\). Obtain an order \(q=(q_1,\dots,q_m)\) of the \(m=n-t\) ordinary coordinates for which the adjacent-pair color word
\[
 H=(h_\beta(q_1,q_2),\dots,h_\beta(q_{m-1},q_m))
 \tag{2}
\]
has at most one change.

Traverse the complete direction permutation
\[
 p=(s_1,\dots,s_t,q_1,\dots,q_m)
 \tag{3}
\]
from the chosen cube root \(x\). For every consecutive ordered-square window entirely inside the ordinary \(q\)-block, its physical fixed \(S\)-bits are exactly \(\beta\); therefore its color equals the corresponding entry of \(H\) in (2), regardless of exterior bits on the other ordinary directions, by (ES). The suffix of the actual full square-color word thus contributes at most one internal switch.

When \(t\ge1\), precisely the first \(t\) consecutive ordered-square windows in (3) meet \(S\): their free direction pairs are
\[
 (s_1,s_2),\dots,(s_{t-1},s_t),(s_t,q_1).
 \tag{4}
\]
For \(t=1\), only \((s_1,q_1)\) occurs. The colors of these \(t\) windows can be *arbitrary*, contributing at most \(t-1\) internal switches. The transition from the last window in (4) to the first ordinary window contributes at most one further switch. Therefore
\[
 \sigma(c(P)) \le (t-1)+1+1=t+1. \tag{5}
\]
For \(t=0\), the complete word is \(H\) and has at most one switch. If \(D\) has zero or one coordinate, the full word is too short to violate the claimed bound. This covers all cases.

Crucially, the argument evaluates each window as an actual **physical square with its correct fixed exterior bits**; the prefix of special directions is a genuine cube geodesic, and the ordinary suffix is a genuine simple Hamilton order of distinct directions. There is no root or coordinate-interleaving assumption. \(\square\)

## Implications for the NORI hierarchy

The multilevel NORI3 amplification uses a constant number of sentinel directions but a *ternary* local-minimum statistic, whose mandatory changes grow unboundedly with the number of direction classes. The present theorem proves a qualitatively different phenomenon for **square** colorings: the same finite-support architecture has a uniform switch bound, even if the ordinary ordered-pair rule is asymmetric and the colors of special-direction squares are otherwise unconstrained.

Therefore a putative NORI2 coloring forcing an **unbounded** number of switches must have unbounded minimal exterior-coordinate support (in the precise sense (ES)) as \(n\to\infty\). A coloring forcing **two** switches might already exist with one or two exterior directions; (5) does not decide this. The sharp symmetric-pair one-sentinel result rules out a two-switch obstruction in that restricted subfamily. Nor does (5) settle unrestricted NORI2, where ordinary squares can depend on arbitrarily many exterior coordinate bits.

## References

A. Gyárfás, *Vertex covers by monochromatic pieces — a survey*, Theorem 2 (Raynaud's 1973 directed two-color Hamiltonian-cycle theorem), accessible at https://www.renyi.hu/~gyarfas/Cikkek/172_krakowrev3.pdf.

The directed statement is also quoted as Theorem 2.1 in *The size Ramsey number of a directed path*, Journal of Combinatorial Theory, Series B **102** (2012), 743–755.



---

## Transferred Subsection: NORI2 sentinel barrier and exact one-switch examples

Exact old composition v2
Original manuscript `nori2_sentinel_barrier_and_exact_one_switch_examples`

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
