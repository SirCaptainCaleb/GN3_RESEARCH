# Actual antipodally odd NORI coloring has connected certified-square carrier of sharp equivariant index one

# Actual NORI coloring attains antipodal index exactly one on the certified square complex

Fix \(n\ge5\) and **two distinguished directions** \(i,j\). Define a coordinate-only binary coloring of all ordered three-faces by the following function of their ordered free triple \((a,b,c)\):
\[
h(a,b,c)=
\begin{cases}
1,&\text{if }\{i,j\}=\{a,b\}\quad\text{(the distinguished pair occupies the first two positions)},\\
0,&\text{if }\{i,j\}=\{b,c\}\quad\text{(the distinguished pair occupies the last two positions)},\\
\mathbf1_{\{a<c\}},&\text{otherwise,}
\end{cases}
\tag{1}
\]
where \(<\) is any fixed total order on cube directions. Write \(c(F,(a,b,c))=h(a,b,c)\) for every physical face \(F\) with these free directions.

**Theorem 1 (exact global missing-square class).** The coloring (1) obeys the active NORI law
\[
c(\bar F,\operatorname{rev}\pi)=1\oplus c(F,\pi).
\]
No monochromatic centered four-edge connector in any part of \(Q_n\) has unordered **middle pair \(\{i,j\}\)**. Consequently the *actual* certified-square complex \(X_c\) is an antipodally invariant subcomplex of the full cubical 2-skeleton with all \(\{i,j\}\)-direction squares deleted. It admits a continuous antipodally equivariant map
\[
X_c\ \longrightarrow\ \partial[0,1]^2\cong S^1
\tag{2}
\]
given by physical coordinate projection to directions \(i,j\). Hence \(w_1(X_c/\tau)^2=0\).

**Proof.** Reversing a triple interchanges the first-two and last-two cases of (1); their values 1 and 0 complement. For every other triple and its reverse, neither belongs to those two cases, and the comparison \(\mathbf1_{\{a<c\}}\) complements under swapping first and last distinct directions. Thus \(h(c,b,a)=1\oplus h(a,b,c)\). Since \(h\) is independent of exterior face coordinates, the full face-reversal-odd law follows.

If a four-edge centered geodesic has direction order \((a,i,j,d)\), with all four directions distinct, its first window \((a,i,j)\) has color 0 and its second window \((i,j,d)\) has color 1. If it has order \((a,j,i,d)\), the corresponding colors are again 0 and 1. Hence no such connector is monochromatic, at any center or exterior assignment. This is exactly the assertion that **no** physical square with free directions \(i,j\) belongs to the certified complex.

Every remaining cubical cell in \(X_c\) has dimension at most two and has at least one of its \(i,j\) coordinates fixed at 0 or 1 (the only cells with both these coordinates free are the missing \(\{i,j\}\)-squares). Therefore projecting to the geometric \((i,j)\)-coordinate square lands in its **boundary**. The projection commutes with physical complementation, which induces the free half-turn on the boundary square. It is consequently equivariant and yields the map (2). Its quotient map classifies the antipodal cover, so \(w_1\) pulls back from the one-dimensional circle quotient. Therefore \(w_1^2=0\). \(\square\)

**Theorem 2 (sharp universal index-one bound).** In this example, \(X_c\) is nevertheless **connected** and its first antipodal class is **nonzero**:
\[
\boxed{w_1\ne0,\qquad w_1^2=0.}
\tag{3}
\]
Thus the universal nonzero one-class from Item \`nori_certified_square_complex_connected_antipodal_one_class_20261008\` is **sharp**: there is no general theorem that the square complex constructed merely by forgetting all but each certified middle pair always has second equivariant index.

**Proof.** The connectivity and \(w_1\ne0\) theorem applies to **every** active NORI coloring in dimensions \(n\ge5\); the coloring (1) is one of them. Theorem 1 gives \(w_1^2=0\). \(\square\)

**Explicit full monochromatic geodesic, confirming no grand counterexample.** Take \(i\) and \(j\) as the first and last directions in the fixed total order (thus \(i<j\)), and follow the directions in increasing order. Because \(n\ge5\), no three consecutive positions contain both \(i\) and \(j\); every ordered-three-face window therefore falls in the final case of (1), and its first direction is less than its third. Hence every window has color 1. This gives a full **monochromatic antipodal geodesic from every root**, even though the genuine certified-square carrier has equivariant index exactly one.

**Impact on fixed-point research.** The previously recorded abstract deletion-of-one-square-class model can actually be **covered by** the certified-square carrier of an active NORI coloring: it is not an irrelevant ambient possibility. Any strategy attempting to force grand closure by showing \(w_1^2(X_c/\tau)\ne0\) for *all* NORI colorings is false. This does **not** refute a refined topological construction with ordered initial/terminal memory, a relative curvature class, or a legitimate proof that either low index already gives a full good geodesic or high index forces a complementary-label collision. It shows precisely which information is lost by forgetting to the middle-pair square complex.
