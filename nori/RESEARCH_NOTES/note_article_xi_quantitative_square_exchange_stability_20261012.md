# Quantitative square-exchange stability and port intersection energy

- Stable ID: note_article_xi_quantitative_square_exchange_stability_20261012
- Author: unspecified; session provenance retained
- Primary home: article:nori_article_xi_matroidal_turn_geometry
- Labels: proved, all-dimensional, cocircuit-exchange, stability
- Lifecycle: active
- Epistemic status: proved
- Current version: 2
- Retention: current and at most one previous snapshot
- Created session: session_nori_r6379_4
- Updated session: session_nori_r6379_4
- Disposition: none
- Successor: none

## Related references

- None

## Research note

# Quantitative stability of shortest-port cocircuit square exchanges

**Proved all-dimensional result.** Let \(n\ge5\) and let \(W\) denote cyclic turn cost of a uniformly sampled *rooted* full antipodal geodesic of any antipodally odd cube-edge coloring. At cube vertex \(v\), write \(r_v\) for its incident color-one degree. For \(2\le r\le n-2\), set
\[
\Phi_n(r)=\frac{2r(n-r)\{(r-1)\min(r-2,n-r-1)+(n-r-1)\min(r-1,n-r-2)\}}{n(n-1)(n-2)(n-3)},
\]
and let \(\Phi_n(r)=0\) at \(r\in\{0,1,n-1,n\}\).

**Theorem (exchange-energy stability).** Choose a uniformly random rooted geodesic and a uniformly random internal adjacent pair of coordinate directions (one with a preceding and a succeeding direction), and let \(W'\) be the cyclic cost after exchanging that pair. Then
\[
\boxed{\Pr(W\ne W')\ge 2^{-n}\sum_{v\in Q_n}\Phi_n(r_v).}\tag{1}
\]
The cost difference is always in \(\{-2,0,2\}\). If all full antipodal geodesics have odd cyclic cost at least \(L\), then
\[
\boxed{\mathbb EW\ge L+2^{-n}\sum_v\Phi_n(r_v).}\tag{2}
\]
Combined with the incidence identity \(\mathbb EW=\frac{n}{2^n\binom n2}\sum_vr_v(n-r_v)\), this yields an explicit necessary inequality for any hypothetical counterexample with minimum cost at least five.

*Proof.* A uniform ordered quadruple of distinct directions \(h,i,j,k\), a uniform vertex \(v\) and uniform suffix directions define a uniformly random rooted geodesic starting at \(v^h\) with prefix \(h,i,j,k\). Swap \(i,j\) to obtain a second uniformly random rooted geodesic. Write
\[
P_h=c_h(v),\quad A=c_i(v),\quad C=c_j(v),\quad B=c_j(v^i),\quad D=c_i(v^j),\quad Q=c_k(v^{ij})
\]
for the six incident edge colors, and let \(\Delta(x,y)=\mathbf1_{\{x\ne y\}}\). The cost difference is
\[
G_h=\Delta(P_h,A)+\Delta(A,B)+\Delta(B,Q)-\Delta(P_h,C)-\Delta(C,D)-\Delta(D,Q).
\]
All other turn comparisons, including the cyclic seam, cancel. Both turn weights are odd and only three terms can change, hence \(G_h\in\{-2,0,2\}\). If \(A\ne C\), changing the color of \(P_h\) changes \(G_h\) by two. Since its only allowed values are minus two, zero and two, precisely one of the two predecessor color classes yields nonzero \(G_h\); the other yields zero.

Suppose vertex \(v\) has \(r\) one-colored incident edges and \(s=n-r\) zero-colored ones. There are \(2rs\) ordered mixed pairs \(i,j\). Removing them leaves \(r-1\) one-colored and \(s-1\) zero-colored candidate successor directions. For a fixed successor of color one, the number of predecessors producing a nonzero swap is at least \(\min(r-2,s-1)\); for a zero-colored successor, at least \(\min(r-1,s-2)\). Thus among the \(n(n-1)(n-2)(n-3)\) possible distinct ordered quadruples, at least
\[
2rs[(r-1)\min(r-2,s-1)+(s-1)\min(r-1,s-2)]
\]
produce a changed cost. Averaging proves (1).

If all cyclic costs are at least \(L\) and \(W\ne W'\), at least one of them is at least \(L+2\). The two have the same marginal distribution, so
\(2\Pr(W\ge L+2)\ge\Pr(W\ne W')\).
Also \(\mathbb EW\ge L+2\Pr(W\ge L+2)\), proving (2). The star-incidence expectation formula gives the stated numerical necessary condition. \(\square\)

**Consequences and limits.** At a \(4/5\) star in dimension nine, \(\Phi_9(4)=5/21\); the average turn weight is at most five, so the positive exchange slack gives another proof of the nine-dimensional closure. At a balanced \(5/5\) star in dimension ten, \(\Phi_{10}(5)=5/21\); at a \(4/6\) star, \(\Phi_{10}(4)=1/5\). The maximum mean cost in dimension ten is \(50/9\), so this first exchange-energy bound by itself does not exclude a minimum cost of five. The next research task is to combine several separated adjacent exchanges or derive stronger two-point correlations, not to claim the conjecture closed in dimension ten.

This note records the general quantitative inequality rather than a minor finite-dimensional special case. An analogous Hessian-style exchange inequality in the tournament gallery would be a potentially useful shared matroid hypothesis but has not been proved.

**Verified Q10 obstruction to one-step Coxeter descent.** Fix zero-based coordinate indices \(i=0,\ldots,9\), with vertex \(x\in\mathbb F_2^{10}\). For \(r=0,\ldots,4\), color each undirected edge in directions \(2r\) and \(2r+1\) by
\[
c_{2r}(x)=x_{(2r+2)\bmod10},\qquad
c_{2r+1}(x)=1-x_{(2r+2)\bmod10}.
\]
The expressions are constant under toggling the corresponding edge direction, so define undirected edge colors. Complementing all vertex coordinates complements every edge color; the coloring is antipodally odd. At every vertex there are five edges of each color.

Take the full antipodal geodesic with initial vertex represented by integer \(506\) (bit \(i\) is coordinate \(i\)) and direction order
\[
(5,4,3,6,8,0,7,2,9,1).
\]
Its ordered edge-color word is \(0111001000\), of cyclic turn weight \(5\) (including the final antipodal seam). **Every one of the ten possible adjacent swaps in its cyclic direction order preserves cyclic turn weight five**, even when swaps spanning the displayed root are interpreted by cyclically rerooting the geodesic. Nonetheless, the geodesic with initial vertex \(126\) and direction order
\[
(6,1,3,4,2,0,9,7,5,8)
\]
has color word \(0000000111\) and cyclic turn weight \(1\). Thus the first geodesic lies on a nonoptimal plateau for the complete cyclic adjacent-swap neighborhood. A proposed greedy proof asserting that every nonoptimal geodesic has an immediately cost-decreasing adjacent coordinate swap is **false**, even for balanced and antipodally odd colorings.

**Reproducible certificate (Python 3).**
\`\`\`python
n=10
def color(x,i):
    j=(i//2*2+2)%n
    return ((x>>j)&1) ^ (i&1)
def word(x,pi):
    values=[]
    for i in pi:
        values.append(color(x,i))
        x ^= 1<<i
    return values
def cyclic_weight(x,pi):
    a=word(x,pi)
    return sum(a[t]!=a[t+1] for t in range(n-1))+(a[-1]==a[0])
root=506
pi=[5,4,3,6,8,0,7,2,9,1]
assert cyclic_weight(root,pi)==5
for pair_index in range(n):
    rotations=(pair_index-1)%n
    x=root
    for i in pi[:rotations]:
        x ^= 1<<i
    rotated=pi[rotations:]+pi[:rotations]
    neighbor=rotated.copy()
    neighbor[1],neighbor[2]=neighbor[2],neighbor[1]
    assert cyclic_weight(x,neighbor)==5
assert cyclic_weight(126,[6,1,3,4,2,0,9,7,5,8])==1
\`\`\`

The plateau example does not refute the two-switch conjecture: indeed the same coloring admits a monochromatic antipodal geodesic after cyclic rerooting of its weight-one witness. It shows why the positive global exchange-energy inequality must be used with nonlocal or higher-order gallery information rather than as a naive steepest-descent algorithm.
