# Cayley two-design conservation

**Theorem (stationary-child regularity).** For a binary generator Cayley lift with m generators and shortest distinguished representation length ell at least three, the shortest odd-monodromy turn cycles have regular stationary-contact offspring: each has ell(m-2) children one turn longer. Contracting the unique stationary contact recovers a unique geodesic parent. For any deck-odd binary edge coloring, every child has integer turn cost equal to its parent cost or two greater. The number of shortest cycles equals F*2^(r-2)*(ell-1)!, where r is the binary representation rank and F the number of shortest distinguished generator subsets. The statements follow by choosing an invariant ell-dimensional subcube for each shortest generator subset, counting its quotient antipodal geodesics, and inserting one of the m-2 unused edge states at each of ell local turns. A changed turn stays changed after the insertion; an unchanged turn either stays unchanged or splits into two changed turns.
**Theorem 2 (shortest-circuit 2-design conservation).** Let S be a spanning family of m distinct binary generator vectors, t a distinguished vector whose minimum generator expression uses ell>=3 labels, and F the set of such minimum expressions. Assume each pair of distinct generator labels belongs to eta members of F. Put E=2^(r-1)*binomial(m,2) for the quotient line graph turn count, and let D denote the number of changed turns of an admissible deck-odd coloring. For each shortest turn cycle C, let R_d(C) count its stationary children whose integer turn weight is two greater. Then

sum_C R_d(C) = (ell-2)! * eta * (m-2) * D / 2.

If one chooses a stationary child uniformly, its color-turn weight equals that of its geodesic parent with probability

1 - D/(2E),

which is at least 1-floor(m*m/4)/(m*(m-1)).

*Proof.* At a fixed quotient-graph vertex and a fixed pair of distinct generator labels s,s', every shortest representation A containing this pair contributes (ell-2)! shortest cycles through the corresponding local turn. By the pair-design assumption this multiplicity is the same, eta*(ell-2)!, for every turn. At a local clique with k edge states of one color and m-k of the other, the number of unchanged pairs with an opposite-colored third state equals

binomial(k,2)*(m-k)+binomial(m-k,2)*k = (m-2)*k*(m-k)/2.

Summing this quantity over stars and multiplying by eta*(ell-2)! gives the first displayed formula, because D is the sum of k*(m-k) over all local stars. The design double-counting identity eta*binomial(m,2)=|F|*binomial(ell,2) combines with the uniform ell*(m-2) stationary children per parent to reduce the fraction of extra-cost children to D/(2E). The inequality follows from k*(m-k)<=floor(m*m/4). QED.

For an arbitrary, non-design shortest-circuit family, the analogous local formula holds with each generator pair weighted by its incidence multiplicity eta_{s,s'}. The design property is precisely what collapses this weighted incidence statistic to the single global turn count D.

**Example (projective-line binary generator matroids).** For every integer d>=2, let V=F2^(d+1), t=(1,0), and S={(1,u):u in F2^d, u nonzero}, with m=2^d-1. Then every shortest representation of t has length three. The shortest generator triples are precisely {(1,u),(1,v),(1,u+v)} with distinct nonzero u,v; every pair occurs in one triple. Thus they form a Steiner triple system (a 2-(m,3,1) design). The Cayley covering graph is the crown graph K_(2^d,2^d) with its matching deleted, and its quotient by the deck involution is K_(2^d). The number of shortest monodromy-odd turn cycles is (m*(m-1)/6)*2^(d-1)*2. In the Fano-plane case d=3, m=7, there are 56 shortest turn cycles and 840 stationary children; the weight-conservation theorem applies to every reversal-odd coloring of this non-cubical covering graph.

**Weight enumerator identity.** If A_d(z) sums z^(turn weight) over shortest cycles and B_d(z) does so over all one-stationary-contact children, while R_d(C) counts the higher-weight children of parent C, then

B_d(z)=ell*(m-2)*A_d(z)+(z*z-1)*sum_C R_d(C)*z^(w_d(C)).

This follows directly from the stationary-child classification, with children changing weight by zero or two.

**Theorem 3 (adjacent two-port minima for arbitrary generator matroids).** The 2-design hypothesis is not needed to compare shortest cocircuit sectors. Add the second port q corresponding to the orientation-curvature class lambda=alpha+kappa. The shortest cocircuits containing both p,q and the shortest cocircuits containing p but excluding q have equal cardinality ell+2 and equal minimum intersection with every admissible coloring cycle. Their turn-cycle representatives are, respectively, shortest length-ell deck-geodesics and length-(ell+1) cycles with a sole stationary contact. Their equal-size parent/child map has ell*(m-2) children per parent. A stationary child has coloring-intersection equal to its parent's or greater by two.

*Proof.* If a monodromy-odd cycle C has r turn edges and s stationary contacts, the moving contacts form a generator walk representing t, so r-s>=ell. Curvature gives lambda(C)=1+s modulo two. In the both-port sector lambda=1, the minimum r=ell forces s=0. In the p-only sector lambda=0, the minimum r=ell+1 forces s=1. A shortest geodesic has odd cyclic turn weight; at any changed turn inserting an unused local edge state produces a length-(ell+1) p-only cycle without increasing the weight. Conversely the sole stationary contact of any p-only minimum cocircuit can be contracted to a geodesic, decreasing or preserving the weight. The stationary child count and coupling follow from the parent map. QED.


### Detailed proof of the stationary-child count

A shortest \(\ell\)-generator representation \(A\in\mathcal F\) contains no nonempty dependent subset: deleting such a subset from its binary sum would give a shorter representation of \(t\). Hence its elements are linearly independent, and their translates generate an invariant \(\ell\)-cube \(Q_\ell\subseteq K\), since their sum is \(t\). The cosets of \(\operatorname{span}(A)\) number \(2^{r-\ell}\), and on each the quotient by translation by \(t\) is the folded \(\ell\)-cube. An antipodal geodesic is an ordering of the \(\ell\) directions with a chosen starting vertex, modulo the two deck choices, cyclic starting turn, and reversal. The count per invariant cube is
\[
\frac{2^\ell\ell!}{4\ell}=2^{\ell-2}(\ell-1)!.
\]
Thus every shortest \(A\) contributes \(2^{r-2}(\ell-1)!\) distinct quotient turn cycles. Different \(A\) have different sets of moving generator directions and produce distinct cycles.

For a cycle \(C'\) of length \(\ell+1\) with one stationary contact, remove its stationary state by the star-triangle shortcut. This gives a simple cycle \(C\) of length \(\ell\) with odd monodromy. Its \(\ell\) moving steps represent \(t\), so they use a shortest generator set with no repeated direction; \(C\) is a geodesic cycle. Contracting the sole stationary contact of \(C'\) determines the parent uniquely.

Conversely, in a quotient geodesic \(C\), each visited quotient base vertex is reached at most once, and its incident-edge star meets the turn cycle in the entering and departing edge states only. At each of its \(\ell\) turns, any one of the other \(m-2\) incident edge states gives a fresh line-graph vertex. Inserting that vertex between the two original states yields a simple cycle of length \(\ell+1\), with one stationary contact at the inserted state and no others. Different choices of the turn and the fresh state give different children, and contracting them recovers \(C\). The stationary-child fiber size is therefore \(\ell(m-2)\). This proves the count asserted in Theorem 1.
