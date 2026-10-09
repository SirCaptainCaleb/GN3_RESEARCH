# All-dimensional monochromatic closure from one central Hamming layer

# One central exterior-weight layer suffices for tournament-factorized colorings

Let \(n\ge5\), \(V=[n]\), and, for an ordered three-face \((F,(a,b,c))\), write \(S(F)\subseteq V\setminus\{a,b,c\}\) for the directions fixed to \(1\). Put \(q=n-3\) and \(k\in\{\lfloor q/2\rfloor,\lceil q/2\rceil\}\).

**Theorem (central-layer tournament closure).** Let \(\chi\) be an *arbitrary* binary coloring of ordered three-faces of \(Q_n\), without any antipodal hypothesis. Suppose its restriction to the one exterior-weight layer \(|S(F)|=k\) is independent of the *identity* of \(S(F)\) and satisfies
\[
\chi(F,(a,b,c))=t(a,c)\oplus s(b)
\quad\text{whenever }|S(F)|=k,\tag{1}
\]
where \(t(a,c)=1\oplus t(c,a)\) is the edge orientation function of an arbitrary tournament on \(V\), and \(s:V\to\mathbb F_2\) is constant outside at most one distinguished vertex. The colors on all other exterior-weight layers are unrestricted, potentially nonlinear functions of every exterior face bit. Then \(Q_n\) has a **monochromatic full antipodal geodesic**.

In particular, the theorem gives an all-dimensional NORI subclass of genuinely face-dependent colorings, with arbitrary dependence on exterior positions away from the middle weight layer. For odd \(n\), the central layer \(k=(n-3)/2\) is self-antipodal; for even \(n\), either of its two central layers suffices.

**Proof.**

*Alternating-root lemma.* Fix any permutation \(p=(p_1,\ldots,p_n)\) of the directions. Assign the starting bits in the order \(p\) alternately \(0,1,0,1,\ldots\), or alternately \(1,0,1,0,\ldots\). The exterior-one set of window \(i\) is
\[
S_i=\{p_j:j<i,\ 1-x_{p_j}=1\}\cup\{p_j:j>i+2,\ x_{p_j}=1\}.
\]
When advancing from window \(i\) to \(i+1\), the exiting direction \(p_i\) joins the exterior in state \(1-x_{p_i}\), while the entering direction \(p_{i+3}\) leaves the exterior from state \(x_{p_{i+3}}\). Because \(x_{p_{i+3}}=1-x_{p_i}\), the cardinality \(|S_i|\) is constant. In the initial window, with the \(0,1,0,\ldots\) start, the exterior-one count is \(\lfloor n/2\rfloor-1\); with the complementary start it is \(\lceil n/2\rceil-2\). These are precisely the two central values \(\lceil(n-3)/2\rceil\) and \(\lfloor(n-3)/2\rfloor\) (coinciding when \(n\) is odd). Thus either admissible \(k\) can be realized, for *every* direction order \(p\), by an alternating start.

*Tournament ordering lemma.* For any tournament \(T\) on \(n\) directions and any vertex \(v\), some permutation \(p\) satisfies \(p_i\to p_{i+2}\) for every \(i=1,\ldots,n-2\) and places \(v\) at one end of \(p\). To prove this, let \(q_1\to q_2\to\cdots\to q_n\) be a directed Hamilton path of the tournament, whose existence follows by inserting vertices greedily into a shorter directed Hamilton path. If \(n=2m+1\), at least one side of the location of \(v\) within \(q\) has \(m\) successors or predecessors; take the \(m+1\)-vertex directed segment beginning or ending at \(v\) as the *odd-position* subsequence of \(p\), and take any directed Hamilton path on the other \(m\) vertices as its even-position subsequence. If \(n=2m\), at least one side has \(m-1\) successors or predecessors; take the corresponding directed segment of \(m\) vertices as an odd-position subsequence starting at \(v\) or an even-position subsequence ending at \(v\), and take a Hamilton path on the complement in the other parity positions. In all cases both parity subsequences are directed, so all skip-two arcs point forward, and \(v\) is extreme.

Apply this lemma to the tournament \(t\) and the possible exceptional vertex \(v\) of \(s\). The resulting order \(p\) has \(t(p_i,p_{i+2})=0\) for all \(i\), and the middle directions \(p_2,\ldots,p_{n-1}\) all avoid \(v\). Take an alternating starting vertex which keeps every window in the chosen central layer \(k\). Every window has color
\[
\chi(F_i,(p_i,p_{i+1},p_{i+2}))
=t(p_i,p_{i+2})\oplus s(p_{i+1})=s(p_{i+1}),
\]
which is constant. Therefore this full antipodal geodesic is monochromatic. \(\square\)

**Scope.** This eliminates all obstructions for colorings whose *single middle-weight layer* is tournament-factorized with at most one exceptional center, even if every other layer is arbitrary. It extends both the coordinate-only tournament theorem and the alternating-root constant-layer method. It does not address the unrestricted middle-layer coloring, which is the remaining obstruction to using this reduction for general NORI.
