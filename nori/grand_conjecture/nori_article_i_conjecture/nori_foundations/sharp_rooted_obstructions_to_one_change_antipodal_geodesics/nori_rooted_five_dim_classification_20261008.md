# Exact 2^15 classification of five-dimensional rooted obstructions

# Classification of rooted obstructions in dimension five

Let \(V\) have five coordinates, and let \(S(F)\) be the set of exterior coordinates fixed to \(1\) in an ordered three-face \(F\).

**Theorem.** The antipodal-reversal-odd colorings \(c\) for which **every** five-direction geodesic from \(0^V\) has two color changes are exactly the colorings
\[
c(F,(a,b,c))=
\begin{cases}
H(\{a,b\},c),&S(F)=\varnothing,\\
1-H(S(F)\cup\{a\},b),&|S(F)|=1,\\
H(S(F),a),&|S(F)|=2,
\end{cases}\tag{2}
\]
where \(H(P,t)\in\{0,1\}\) is defined for \(t\in V\) and \(|P|=2\), \(P\subseteq V\setminus\{t\}\), and satisfies
\[
H((V\setminus\{t\})\setminus P,t)=1-H(P,t).\tag{1}
\]
There are exactly \(2^{15}\) such colorings.

**Proof.** Suppose every rooted path is bad. Its color word has length three, so is \(010\) or \(101\). Define \(h(a,b,c)\) as the first-window color of a rooted path in direction order \((a,b,c,d,e)\). This color does not depend on the later ordering of \(d,e\). The last-window face has ordered free triple \((c,d,e)\) and exterior-one set \(\{a,b\}\); exchanging the first two directions \(a,b\) leaves that face unchanged. Since first and last colors agree in every bad rooted path, \(h(a,b,c)=h(b,a,c)\). Write \(h(a,b,c)=H(\{a,b\},c)\).

The middle-window color must then be \(1-H(\{a,b\},c)\), and the last-window color \(H(\{a,b\},c)\). Every ordered three-face of \(Q_5\) occurs in a rooted geodesic by placing its exterior-one coordinates before its ordered free triple and its exterior-zero coordinates after it. Hence the three formulas (2) determine the *entire* coloring.

Antipodal reversal pairs the rank-zero face with free triple \((a,b,c)\) with the rank-two face of free triple \((c,b,a)\) and exterior-one set \(\{d,e\}\). The oddness condition is exactly \(H(\{d,e\},c)=1-H(\{a,b\},c)\), equivalent to (1).

Conversely, let \(H\) satisfy (1) and define \(c\) by (2). The rank-zero and rank-two cases satisfy oddness by (1). For rank one, let the exterior-one direction be \(u\) and the exterior-zero direction be \(v\). Antipodality and reversal take \((a,b,c)\) to \((c,b,a)\) and swap the exterior-one direction from \(u\) to \(v\). Their colors are \(1-H(\{u,a\},b)\) and \(1-H(\{v,c\},b)\), which are complementary by (1). Every rooted direction order \((a,b,c,d,e)\) now has word
\[
\bigl(H(\{a,b\},c),\;1-H(\{a,b\},c),\;H(\{a,b\},c)\bigr),
\]
with exactly two changes.

For each \(t\), the six two-element subsets of \(V\setminus\{t\}\) form three complementary pairs, and (1) assigns one free bit per pair. With five choices of \(t\), this gives fifteen independent bits. The rank-zero face colors recover \(H\) uniquely, so these give exactly \(2^{15}\) distinct colorings. \(\square\)

This is a complete classification of the rooted obstruction. It is compatible with the unconditional existence of an *unrooted* good geodesic in dimension five.
