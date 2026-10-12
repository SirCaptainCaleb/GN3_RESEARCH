# Antipodal Boolean-lattice terminal polarity and spanning one-turn paths

# Antipodal Boolean-lattice terminal polarity and spanning one-turn paths

The preceding Subsection formulates the spanning one-turn boundary-tournament conjecture as opposite-terminal packing of two same-colored vertex-simple tight paths. Here we introduce a **resource-subset state graph** that carries a canonical complement-reversal involution. The key theorem is a color-reversing anti-isomorphism of its two directed reachability graphs, yielding a single antipodal reachability-intersection formulation that parallels the endpoint-coincidence approaches to NORI1. The proof is valid in all orders and preserves vertex simplicity at every step.

## 1. The ordered-terminal Boolean-lattice graph

Let \(V\) have \(n\ge3\) vertices, and let \(b:V_{\ne}^3\to\mathbb F_2\) be a reversal-odd boundary coloring:
\[
b(v,u,x)=1+b(x,u,v).
\tag{1}
\]
Define the state set
\[
\mathscr S(V)=\{(A,u,v):\{u,v\}\subseteq A\subseteq V,\ u\ne v\}.
\tag{2}
\]
The first component remembers the set of original vertices used, and the last two components remember the ordered terminal pair. For each color \(\epsilon\in\mathbb F_2\), define an acyclic digraph \(\mathscr D_\epsilon(b)\) on \(\mathscr S(V)\): there is a directed arc
\[
\boxed{(A\setminus\{v\},x,u)\longrightarrow(A,u,v)}
\tag{3}
\]
whenever \(x,u,v\) are distinct members of \(A\) and \(b(x,u,v)=\epsilon\). The arc increases resource-set cardinality by one. The sources are the ordered two-vertex states \((\{u,v\},u,v)\), considered admissible in either color because a two-vertex path has no ordered-triple window.

Let \(\mathscr R_\epsilon\subseteq\mathscr S(V)\) be the union of states reachable from any source in \(\mathscr D_\epsilon(b)\).

**Lemma 1 (terminal-state reachability).** A state \((A,u,v)\) belongs to \(\mathscr R_\epsilon\) if and only if there is a vertex-simple \(\epsilon\)-monochromatic tight path whose vertex set is \(A\) and final ordered pair is \((u,v)\).

*Proof.* A path on two vertices corresponds to a source. Each extension adds a fresh vertex \(v\) to a previously constructed path ending in \((x,u)\), and the new final triple is \((x,u,v)\). The arc rule (3) requires the new triple color to be \(\epsilon\), and the increasing set \(A\) rules out repeated original vertices. Conversely, delete the last vertex of any positive-length witness to recover its predecessor. Induction on \(|A|\) proves the equivalence. \(\square\)

For a fixed ordered pair \((u,v)\), write \(U=V\setminus\{u,v\}\), and let
\[
\mathscr F_{uv}^\epsilon
=\{S\subseteq U:(S\cup\{u,v\},u,v)\in\mathscr R_\epsilon\}.
\tag{4}
\]
Then the recursion is
\[
\boxed{
\mathscr F_{uv}^\epsilon(\varnothing)=1,\qquad
\mathscr F_{uv}^\epsilon(S)=
\bigvee_{x\in S}
\left(
[b(x,u,v)=\epsilon]\land
\mathscr F_{xu}^\epsilon(S\setminus\{x\})
\right)
}
\tag{5}
\]
for \(S\ne\varnothing\), with each \(\mathscr F\) read as a Boolean indicator. The state count is
\[
\boxed{|\mathscr S(V)|=n(n-1)2^{n-2};}
\tag{6}
\]
all values of (5) can be calculated in \(O(n^3 2^n)\) Boolean operations. This is an all-dimensional subset-state representation rather than an enumeration of \(n!\) complete orders.

## 2. The color-reversing antipodal polarity

Define
\[
\boxed{
\mathcal J(A,u,v)
=\bigl((V\setminus A)\cup\{u,v\},\,v,u\bigr).
}
\tag{7}
\]
This complements the *used* resources other than the terminal pair, retaining the two shared vertices while reversing their order. It satisfies \(\mathcal J^2=1\), has no fixed state, and carries resource-set cardinality \(r\) to \(n-r+2\).

**Theorem 2 (complement-reversal anti-isomorphism).** For every reversal-odd boundary coloring and each \(\epsilon\in\mathbb F_2\), the involution (7) induces a directed-graph anti-isomorphism
\[
\boxed{
\mathcal J:\mathscr D_\epsilon(b)\longrightarrow
\mathscr D_{1-\epsilon}(b)^{\mathrm{op}}.
}
\tag{8}
\]
In other words, whenever \(P\to Q\) is a color-\(\epsilon\) arc, then
\[
\boxed{\mathcal J(Q)\to\mathcal J(P)}
\tag{9}
\]
is a color-\((1-\epsilon)\) arc.

*Proof.* Consider a typical arc (3) with \(b(x,u,v)=\epsilon\). Write \(T=V\setminus A\). Then
\[
\begin{aligned}
\mathcal J(A,u,v)&=(T\cup\{u,v\},v,u),\\
\mathcal J(A\setminus\{v\},x,u)&=(T\cup\{u,v,x\},u,x).
\end{aligned}
\]
The second state is obtained from the first by appending the fresh vertex \(x\) to the terminal pair \((v,u)\). The corresponding new triple is \((v,u,x)\), and by (1)
\[
b(v,u,x)=1+b(x,u,v)=1-\epsilon.
\]
Thus (9) is an arc of \(\mathscr D_{1-\epsilon}(b)\). Applying \(\mathcal J\) again proves the converse and hence (8). \(\square\)

**Corollary 3 (reachability/co-reachability duality).** A state \(s\) lies in \(\mathcal J(\mathscr R_\epsilon)\) precisely when there is a path in \(\mathscr D_{1-\epsilon}(b)\) from \(s\) to some full-resource state \((V,u,v)\). Thus
\[
\boxed{
\mathcal J(\text{color-}\epsilon\text{ source reachability})
=\text{color-}(1-\epsilon)\text{ full-state co-reachability}.
}
\tag{10}
\]

*Proof.* Apply the arc anti-isomorphism to a color-\(\epsilon\) path from a two-vertex source to \(\mathcal J(s)\). Its reverse image starts at \(s\), follows color-\((1-\epsilon)\) arcs, and ends at the image of the two-vertex source, which is a full-resource state. The argument reverses. \(\square\)

## 3. Antipodal reachability-intersection equivalence

**Theorem 4 (spanning one-turn iff antipodal reachability intersects).** An ordinary reversal-odd boundary 3-tournament admits a spanning vertex-simple tight path with at most one internal color change if and only if
\[
\boxed{
\mathscr R_\epsilon\cap\mathcal J(\mathscr R_\epsilon)
\ne\varnothing
\quad\text{for some }\epsilon\in\mathbb F_2.
}
\tag{11}
\]
Equivalently, for some distinct \(u,v\), a subset \(S\subseteq U=V\setminus\{u,v\}\), and a color \(\epsilon\),
\[
\boxed{
S\in\mathscr F_{uv}^\epsilon,\qquad
U\setminus S\in\mathscr F_{vu}^\epsilon.
}
\tag{12}
\]

*Proof.* The latter condition gives two vertex-simple same-colored tight paths ending at \((u,v)\) and \((v,u)\) whose sets of other vertices are complementary. Reversing the second arm and identifying the shared terminal pair produces a spanning path with at most one change, as proved by the opposite-terminal packing theorem of the preceding Subsection. Conversely, splitting a spanning one-turn path at its color change and reversing its suffix produces these two arms; if the original path is monochromatic, allow the first arm to consist only of its first two vertices. Under the state encoding, the two conditions in (12) say precisely that \(s=(S\cup\{u,v\},u,v)\) and \(\mathcal J(s)\) both belong to \(\mathscr R_\epsilon\), establishing (11). \(\square\)

Thus the principal boundary conjecture can be stated intrinsically as:

**Conjecture 5 (antipodal terminal-reachability intersection).** Every reversal-odd colored ordered-terminal subset-state system (2)–(3) has
\[
\boxed{
\mathscr R_0\cap\mathcal J(\mathscr R_0)\ne\varnothing
\quad\text{or}\quad
\mathscr R_1\cap\mathcal J(\mathscr R_1)\ne\varnothing.
}
\tag{13}
\]
By Theorem 4 this is equivalent to the spanning one-turn boundary-tournament conjecture, not a new independent assumption.

For comparison, the cube's full geodesic is likewise a resource-injective chain in a Boolean subset lattice; its antipodal endpoint construction seeks complementary color-compatible partial chains. The common missing theorem concerns the **reachability geometry under a free antipodal polarity**, rather than bare binary-matroid parity.

## 4. Sharp complement counting criteria

Let
\[
r_{uv}^{\epsilon}(k)
=\#\{S\in\mathscr F_{uv}^\epsilon:|S|=k\},
\qquad 0\le k\le n-2.
\tag{14}
\]

**Proposition 6 (complementary-layer density suffices).** If there are distinct \(u,v\), \(\epsilon\), and \(k\) with
\[
\boxed{
r_{uv}^{\epsilon}(k)+
r_{vu}^{\epsilon}(n-2-k)>
\binom{n-2}{k},
}
\tag{15}
\]
then the boundary tournament has a spanning at-most-one-turn tight path. Consequently, a hypothetical counterexample to (13) must satisfy **all** the reverse inequalities
\[
\boxed{
r_{uv}^{\epsilon}(k)+
r_{vu}^{\epsilon}(n-2-k)
\le\binom{n-2}{k}
}
\tag{16}
\]
for every ordered pair, color and layer; in particular
\[
|\mathscr F_{uv}^\epsilon|+|\mathscr F_{vu}^\epsilon|
\le2^{n-2}.
\tag{17}
\]

*Proof.* The complement map \(S\mapsto U\setminus S\) bijects the \(k\)-subsets of \(U\) with its \((n-2-k)\)-subsets. If the two cardinalities in (15) exceed the number of complementary pairs, their supports must overlap after complementation. This gives (12). The contrapositives and sum over \(k\) prove (16)–(17). \(\square\)

These counting inequalities are sufficient certificates, not asserted universal density bounds. Establishing an exchange, connectivity, parity or topological principle forcing a violation of (16) for some pair/color/layer would prove the spanning conjecture. A basic accessible-set argument is insufficient: the fixed-terminal reachability families are accessible but need not satisfy greedoid augmentation (a verified five-vertex counterexample is preserved as a research note attached to this Section).

## 5. Research significance

Theorem 2 introduces a mathematically intrinsic **anti-isomorphism between the two color-specific terminal extension systems**. Together with the resource-set polarity (7), Theorem 4 expresses the full-spanning one-turn assertion as a complement-intersection problem over an ordered-pair bundle of Boolean lattices. Unlike an unmarked cocircuit intersection bound, this representation preserves (i) all original vertices, (ii) the order and orientation of both terminal vertices, (iii) the path's single color-change seam, and (iv) the precise opposite-arm compatibility demanded by the original problem.

The next substantive goal is a global topological or exchange theorem establishing (13) from reversal oddness, perhaps by forcing opposing reachable families to intersect on complementary ranks. The present results provide the encoding, duality, and a transparent target; they do **not** prove the conjectural intersection in general.
