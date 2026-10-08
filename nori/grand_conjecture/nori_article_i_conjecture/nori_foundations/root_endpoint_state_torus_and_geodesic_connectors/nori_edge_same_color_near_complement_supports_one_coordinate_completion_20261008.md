# One-coordinate completion for almost-complementary monochromatic reachability branches

# Near-complementary monochromatic branches: the one-coordinate completion law

Let \(Q_n\) have an antipodally odd binary UNDIRECTED edge coloring \(c(\bar e)=1-c(e)\). Let x be a root. Suppose two monochromatic geodesics \(P_S:x\to x\oplus S\) and \(P_T:x\to x\oplus T\) use DISJOINT coordinate supports, and
\[
S\cap T=\varnothing,\qquad S\cup T=[n]\setminus\{i\}.
\]
Thus the two paths form a geodesic from \(x\oplus S\) to \(x\oplus T\) of length n-1 through x, with a single missing direction i. Denote its two end-edges toward antipodal completion by
\[
e_S=\{x\oplus S,\overline{x\oplus T}\},\qquad
e_T=\{x\oplus T,\overline{x\oplus S}\}.
\]
They are antipodal edges and have complementary colors.

**Theorem (same-color case).** If \(P_S\) and \(P_T\) have the SAME monochromatic edge color q, then a monochromatic full antipodal geodesic exists. Precisely one of the two completion edges has color q. Appending that edge to its corresponding monochromatic branch from x reaches the antipode of the other branch's endpoint. Thus the uncolored region R(x) contains an antipodal pair and yields closure.

**Theorem (opposite-color case).** If the branch colors are q and \(1-q\), then the \((n-1)\)-geodesic through x has exactly one switch (assuming both paths have positive length). Its two full antipodal completions either BOTH have at most one switch or BOTH have two switches. The former occurs iff \(c(e_S)=q\), equivalently \(c(e_T)=1-q\). In the latter case \(c(e_S)=1-q\) and \(c(e_T)=q\). This isolates a SINGLE binary obstruction at the exposed coordinate i.

**Proof.** The disjointness of supports makes the two-arm concatenation a geodesic, and omission of only i makes both e_S and e_T legitimate geodesic endpoint extensions. The edges are antipodes because \(\overline{x\oplus S}=(x\oplus T)\oplus e_i\) and \(\overline{x\oplus T}=(x\oplus S)\oplus e_i\), so their colors are opposite. When branch colors match, precisely one edge extends the corresponding branch monochromatically; the new endpoint is antipodal to the other reachable branch endpoint. When colors differ, adding e_S before the q-block preserves one switch exactly when it has color q; adding e_T after the (1-q)-block preserves one switch exactly when it has color 1-q. The antipodal oddness makes these conditions equivalent. QED.

**Interpretation respecting COLOR-FREE R.** The main reachability set remains \(R(x)=R_0(x)\cup R_1(x)\), with no color specified in its topological labels. If two representatives of R(x) have disjoint supports covering n-1 coordinates, examining the EXISTENCE of same-color witnesses or the unique exposed bridge bit provides an exact extraction. Any reachability-label coincidence that forces same-color witnesses for such a near-partition immediately proves grand closure in the edge case. The full antipodal-support partition (covering n coordinates) already yields closure for arbitrary witness colors.
