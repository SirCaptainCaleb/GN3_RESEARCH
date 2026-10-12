# Flat-graded resource automata and antipodal reachability certificates

Let A be a directed graph whose arcs carry labels in a loopless resource matroid N. Starting from a vertex v and the closure F of an independent resource set, construct a flat-graded automaton with states (v,F). For an arc from v to w labeled e outside F, advance to (w,cl(F union {e})). Every transition increases matroid rank by one. The resulting automaton paths are in bijection with coherent directed walks whose resource labels, together with the initial independent set, remain independent. The automaton is acyclic. This follows immediately from the matroid independence exchange criterion: appending e preserves independence if and only if e is outside the closure of the previously chosen elements.

**Corollary 2 (canonical specializations).** For the cube, take the bidirected Q_n and the free matroid on n coordinate directions; label each cube edge by its direction and begin with the empty flat. From root x a state is (x XOR S,S) with S a subset of directions. Rank n forces every coordinate to be used once, producing an antipodal geodesic.

For ordinary boundary 3-tournaments, take directed ordered-pair states (u,v) and transitions (u,v) to (v,w) for three distinct letters. Use the graphic matroid of K_V. Label each transition by the new resource edge {v,w}, and begin at (u,v) with the flat of {u,v}. After a forward prefix the selected graphic edges form a connected vertex path; its closure contains all edges between previously visited vertices. Thus the next resource {v,w} increases rank if and only if w is new. This automaton recognizes precisely forward vertex-injective tight paths. Reaching graphic rank h means the underlying word uses h+1 original vertices and h-1 ordered triples.

*Proof.* In the cube, free-matroid independence is nonrepetition of coordinate directions. In the boundary model, the graphic closure of a connected tree on a visited vertex set is the set of all complete-graph edges internal to that set. Rank-increasing ordered-pair transitions therefore append a fresh vertex, and the converse holds for every injective tight-path word. QED.

**Theorem 3 (antipodal Boolean reachability criterion for NORI1).** Fix an antipodally odd coloring \(c\) of \(Q_n\) and a root \(x\). Identify its free-resource automaton with the Boolean lattice \(2^{[n]}\), where the directed arc \(S\to S\cup\{i\}\) has the color of the cube edge from \(x+\mathbf1_S\) in direction \(i\). Define
\[
R_x=\{S\subseteq[n]:\text{a color-zero directed path runs from }\varnothing\text{ to }S\}.
\tag{1}
\]
Then, for every \(S\subseteq[n]\), the rooted cube has a geodesic whose edge colors are first zero and then one, with the switch at the vertex \(x+\mathbf1_S\), if and only if
\[
\boxed{S\in R_x\ \text{and}\ [n]\setminus S\in R_x.}\tag{2}
\]
Empty initial or terminal color blocks are allowed. Consequently unrestricted NORI1 is equivalent to
\[
\boxed{\exists x\in Q_n:\ R_x\text{ contains a complementary pair of subsets}.}\tag{3}
\]
A hypothetical NORI1 counterexample would have \(R_x\cap\{[n]\setminus S:S\in R_x\}=\varnothing\) for every root, and hence \(|R_x|\le2^{n-1}\) for every root.

*Proof.* Antipodal oddness makes the arc
\[
S\to S\cup\{i\}
\]
opposite in color to its complemented reverse
\[
[n]\setminus(S\cup\{i\})\to[n]\setminus S.
\]
Therefore reversing and complementing a color-zero path from \(\varnothing\) to \([n]\setminus S\) yields a color-one path from \(S\) to \([n]\). Concatenate with the zero path from \(\varnothing\) to \(S\) to obtain the specified one-switch geodesic. The converse follows by reversing and complementing the color-one suffix. A geodesic with one linear color switch has precisely one cyclic turn disagreement: its closing turn compares the terminal color with the deck complement of the initial color. Cyclically rerooting at the changed turn therefore gives a monochromatic antipodal geodesic. Conversely any monochromatic geodesic, after deck reversal if necessary, is a color-zero geodesic rooted at some \(x\), and gives the complementary pair \(\varnothing,[n]\). Finally a family of subsets avoiding complementary pairs has size at most \(2^{n-1}\), by pairing every subset with its complement. \(\square\)

**Theorem 4 (antipodal cut duality).** For a fixed rooted cube \(x\), let \(R_x\) be as in Theorem 3. The absence of a color-zero-then-color-one antipodal geodesic rooted at \(x\) is equivalent to the existence of a set \(\mathcal U_x\subseteq2^{[n]}\) satisfying all three conditions:
\[
\varnothing\in\mathcal U_x,\qquad
\mathcal U_x\cap\{\bar S:S\in\mathcal U_x\}=\varnothing,\qquad
\text{every outward Boolean-lattice arc of }\mathcal U_x\text{ has color one.}
\tag{4}
\]
Here \(\bar S=[n]\setminus S\). Accordingly, failure of unrestricted NORI1 is equivalent to the existence of such a family \(\mathcal U_x\) for every root \(x\), all arising from the same antipodally odd cube-edge coloring.

*Proof.* If no one-switch geodesic exists from \(x\), Theorem 3 shows that \(R_x\) contains no complementary pair; it contains the empty set, and any outward arc of \(R_x\) must have color one by the definition of color-zero reachability. Thus \(\mathcal U_x=R_x\) works. Conversely, if \(\mathcal U_x\) satisfies (4), no color-zero directed path from the empty set can leave \(\mathcal U_x\), because its first outward arc would have color one. Hence \(R_x\subseteq\mathcal U_x\) and is complement-free, so Theorem 3 excludes the rooted one-switch witness. Apply this for all roots, using Theorem 3's equivalence with global NORI1. \(\square\)

The families in (4) need not be order ideals: directed monochromatic reachability can omit a subset even while reaching some of its supersets by another coordinate order. This is an antipodal-cut certificate, not an ordinary monotone Boolean-lattice ideal.

**Corollary 5 (resource-flat groupoid constraints).** For every root \(x\), the reachability families also satisfy:
\[
\begin{aligned}
&S\in R_x\Longrightarrow S\in R_{x+\mathbf1_S},\\
&S\in R_x,\quad T\in R_{x+\mathbf1_S},\quad S\cap T=\varnothing
\Longrightarrow S\cup T\in R_x .
\end{aligned}
\tag{5}
\]
The first property comes from reversing a color-zero geodesic, and the second from concatenating two coordinate-disjoint color-zero geodesics. Thus the root-indexed antipodal cuts of a hypothetical counterexample cannot be chosen independently: their reachable families obey the symmetric partial-composition laws (5).

The formulation supplies a precise target for Tucker-, Sperner-, or KKM-type arguments. To prove unrestricted NORI1 it suffices to show that no deck-odd cube-edge coloring supports a compatible system of complement-free, color-one-boundary families as in (4) and (5). Theorem 4 does not establish that impossibility.

**Theorem 6 (factorial-free SAT obstruction certificate).** For \(n\ge3\), introduce one Boolean coloring variable per antipodal orbit of cube edges, and one Boolean membership variable \(r_{x,S}\) for every cube root \(x\) and coordinate subset \(S\subseteq[n]\). Let \(\gamma_{x,S,i}\) denote the color-one Boolean expression of the edge from \(x+\mathbf1_S\) in unused coordinate direction \(i\). Consider the clauses
\[
\begin{array}{ll}
r_{x,\varnothing},&\text{all }x,\\
\neg r_{x,S}\vee\gamma_{x,S,i}\vee r_{x,S\cup\{i\}},&
\text{all }x,S,i\notin S,\\
\neg r_{x,S}\vee\neg r_{x,\bar S},&
\text{all }x,\text{ one representative per complement pair }S,\bar S.
\end{array}
\tag{6}
\]
This formula is satisfiable if and only if an antipodally odd coloring of \(Q_n\) exists with no monochromatic antipodal geodesic. Its size is
\[
\boxed{n2^{n-2}+4^n\text{ variables},\qquad
(n+1)2^{2n-1}+2^n\text{ clauses}.}\tag{7}
\]

*Proof.* The coloring variables determine one deck-odd coloring by giving opposite colors to paired antipodal edges. For each root, the first two clause families make \(U_x=\{S:r_{x,S}=1\}\) contain the empty subset and be closed under every color-zero forward transition. The third clause family makes it free of complementary pairs. By Theorem 4 this excludes a NORI1 witness. Conversely, if a counterexample coloring exists, take \(U_x\) to be the true zero-reachable family \(R_x\). Theorem 4 guarantees every clause. There are \(n2^{n-2}\) edge orbits and \(4^n\) root-subset memberships; the forward transitions number \(n2^{2n-1}\), complement pairs \(2^{2n-1}\), and initial-root clauses \(2^n\). \(\square\)

**Corollary 7 (resource-groupoid strengthening).** Adding
\[
r_{x,S}\Longrightarrow r_{x+\mathbf1_S,S},\qquad
r_{x,S}\wedge r_{x+\mathbf1_S,T}
\Longrightarrow r_{x,S\cup T}\quad(S\cap T=\varnothing)
\tag{8}
\]
does not change satisfiability. Indeed the true reachable sets satisfy these implications by path reversal and disjoint-resource concatenation, so they still witness the converse direction.

This gives a finite resource-sensitive dual certificate of a potential counterexample, with a clause count growing as \(O(n4^n)\) instead of the factorial number of rooted geodesics. It is not a uniform proof of unsatisfiability.

**Corollary 8 (antipodal root reduction).** In Theorem 6 the rooted membership variables and clauses may be imposed only for a transversal \(T\) of antipodal vertex pairs. The smaller formula is satisfiable if and only if a counterexample coloring exists. Its size is
\[
\boxed{n2^{n-2}+2^{2n-1}\text{ Boolean variables},\qquad
(n+1)2^{2n-2}+2^{n-1}\text{ clauses}.}\tag{9}
\]
For \(n=7\), this is 224 coloring variables, 8192 rooted variables, and 32,832 clauses before symmetry constraints.

*Proof.* Any counterexample coloring has complement-free true reachable families at every root, so restrict to \(T\). Conversely, if a monochromatic antipodal geodesic existed, reversing it and translating by the deck involution would give geodesics of both colors rooted at both antipodal endpoints. One endpoint lies in \(T\), and its color-zero path forces both the empty set and its complement into that root's SAT membership family, contradicting the complementary-pair clauses. Thus the restricted formula excludes all counterexample witnesses if unsatisfiable. Halving the roots halves the reachability variables and clauses. \(\square\)

This is an equivalent finite-dimensional decision procedure, not a uniform proof over all dimensions.
