# Positive protection eliminates exclusive disjoint alternating carriers — preserved pre-item development

## Development

## Disjoint alternating terminal carriers are impossible under positive protection

This repairs the alternating elimination without using \(110,100,1010\).

**Theorem.** Let two reflected alternating determining windows be disjoint. Suppose every chamber has exactly one of the two \(0101\) occurrences, both sides occur somewhere, and every strictly inward positive witness is excluded. Then no such ordered-partition face exists.

**Proof.** By [[exclusive_disjoint_terminal_windows_are_adjacent_without_dual_polarity]], the six-vertex windows are adjacent. Translate their twelve vertex positions to \(1,\ldots,12\), with status positions \(1,\ldots,10\). Their alternating starts are 1 and 7. Strictly inward positive protection excludes \(001,011\) at starts \(2,\ldots,7\) and \(0101\) at starts \(2,\ldots,6\).

Write the statuses as \(s_1,\ldots,s_{10}\), and let \(L,R\) be the indicators of \(0101\) at starts 1 and 7.

If \(L=1\), then \(s_3=0,s_4=1\). Exclusion of the span-two witness at start 3 gives \(s_5=0\). Exclusion of \(0101\) at start 3 then gives \(s_6=0\). Exclusion of the span-two witness at start 6 gives \(s_8=0\). Thus
\[
L=1\Longrightarrow s_3=0,\quad s_5=s_6=0,\quad s_8=0.
\]

If \(R=1\), then \(s_7=0,s_8=1\). Exclusion of the span-two witness at start 6 gives \(s_6=1\). Exclusion of \(0101\) at start 5 gives \(s_5=1\). Exclusion of the span-two witnesses at starts 3 and 4 gives \(s_3=s_4=1\). Thus
\[
R=1\Longrightarrow s_3=s_4=s_5=s_6=1,\quad s_8=1.
\]

The tuple and footprint lemmas give a unique common block \(B\), with
\[
|B|=\alpha+\beta,\qquad 1\le\alpha,\beta\le2.
\]
Fix exterior orders from a left-positive chamber on the left and a right-positive chamber on the right, as in the adjacency proof. In this context both indicators still attain one.

If \(\alpha=1\), the left intersection with \(B\) is only vertex position 6, so \(s_3\), on positions \(3,4,5\), is fixed by the exterior context. A left-positive chamber makes it zero, whereas a right-positive chamber would make it one. This is impossible. Symmetrically, if \(\beta=1\), status \(s_8\), on positions \(8,9,10\), is exterior and fixed; right positivity makes it one and left positivity makes it zero. Therefore
\[
\alpha=\beta=2,\qquad |B|=4,
\]
and \(B\) occupies positions \(5,6,7,8\).

For any order \((x,y,z,w)\) of \(B\), the left indicator depends only on \((x,y)\), and the right indicator only on \((z,w)\). Since exactly one occurs, the preceding implications show
\[
h(x,y,z)=h(y,z,w)=1-L(x,y).
\]
Apply the same identity to the rotated order \((y,z,w,x)\). The shared triple gives
\[
L(x,y)=L(y,z)
\]
for every three distinct \(x,y,z\in B\).

For fixed \(y\), any two choices \(x_1,x_2\ne y\) have a fourth vertex \(z\) distinct from \(y,x_1,x_2\). Hence
\[
L(x_1,y)=L(y,z)=L(x_2,y).
\]
Thus \(L(x,y)\) depends only on \(y\). The equality \(L(x,y)=L(y,z)\) now forces that function to be constant. This contradicts the existence of both \(L=1\) and \(R=1\), together with \(L+R=1\). \(\square\)

The proof uses only positive forbidden patterns and independently variable face-block orders. It does not identify cyclic rotations of a tight triple: equality under rotation is deduced from protectedness and the exclusive-indicator equations, not assumed from the boundary-tournament axiom.

Consequently the twelve-position upper bound for the exclusive disjoint alternating branch is unnecessary: that branch is eliminated. The exclusive disjoint span-two branch survives, but its determining span is at most ten vertices. Centered and overlapping supports already have their elementary bounded union sizes.

The unresolved one-polarity compression branch is reflected-double occupation, where both occurrences coexist and \(L+R=1\) fails. The theorem makes no claim about that branch, terminal outwardness, or the global nested carrier assignment.
