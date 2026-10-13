# Two-step rainbow-resource diversity and monochromatic two-step counting

- Stable ID: note_c12cd5a8ceac4f8a596a3186
- Author: unspecified; session provenance retained
- Primary home: article:nori_article_ix_unification
- Labels: ordered-pair-cover, resource-rainbow, second-neighborhood, boundary-tournament, two-step-walks
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r7130_6
- Updated session: session_nori_r7130_6
- Disposition: none
- Successor: none

## Related references

- None

## Research note

# Two-step resource expansion and a global monochromatic-walk count

Let V be an n-element set, n>=3. Let S(V) have ordered-pair states (a,b) and undirected edges joining (a,b) to (b,c) for a,b,c pairwise distinct. Define edge resource label lambda((a,b),(b,c))=b. A boundary binary coloring B(a,b,c) satisfying B(c,b,a)=1-B(a,b,c) gives an edge coloring of S(V) with the deck flip tau(a,b)=(b,a).

**Local resource observation.** A state (a,b) has only two labels a,b incident upon it, each with multiplicity n-2. An alternating-label two-edge walk from this state must follow either two consecutive forward transitions or two consecutive reverse transitions. It has resource word (b,c) forward or (a,c) backward, where c runs over all n-2 symbols outside {a,b}. Thus every state has n-2 distinct possible second-edge resource labels in a two-step rainbow walk. This is *unrestricted* by binary color.

**Global two-step monochromatic abundance theorem.** For each fixed binary color eps, the number W_eps of directed coherent length-two covering walks (a,b)->(b,c)->(c,d) whose two covering edges both have binary color eps, with a,b,c pairwise distinct and b,c,d pairwise distinct (allowing d=a), satisfies
W_eps >= n(n-1)(n-2)(n-3)/6.
Moreover at least
max(0,n(n-1)(n-2)(n-6)/6)
such walks have four pairwise distinct original symbols a,b,c,d.

*Proof.* Define D=n-2 and d(a,b)=#{c outside {a,b}: B(a,b,c)=eps}. At each fixed center b, the d(a,b) are outdegrees of a tournament on s=n-1 vertices. Hence sum_{a!=b}d(a,b)=binom(s,2). Its sum of squares is at most binom(s,2)+2binom(s,3)=sD(2D+1)/6: each centered two-out-star is a transitive triple with a unique dominating vertex, and each three-element set contributes at most one such star. Sum over b to get sum_{a!=b}d(a,b)^2 <= n sD(2D+1)/6.

The positive indegree of state (b,c) is D-d(c,b), by reversal oddness of B. Consequently
W_eps=sum_{b!=c}d(b,c)(D-d(c,b))
= D*n*binom(s,2) - sum_{b!=c} d(b,c)d(c,b).
Using xy<= (x^2+y^2)/2 and the preceding score-square bound gives
W_eps>=n sD[D/2-(2D+1)/6]=n sD(D-1)/6.
For a length-two coherent walk, failure of four distinct symbols means d=a; there is at most one such closing continuation per initial monochromatic covering arc, and the total number of monochromatic covering arcs is n*binom(s,2). Subtracting proves the second assertion. QED.

**Important limitation.** This is an aggregate bound on two-step walks, not a per-terminal extension theorem. A rainbow path ending in (a,b) with used resource set R must next use b (the other incident label a was used on the preceding edge). If b belongs to R, no rainbow extension exists, regardless of the n-2 possible second-hop labels. Even with b new, the prescribed binary edge color might forbid all two-step monochromatic continuations. Any improvement to long monochromatic rainbow paths needs rerouting, endpoint rotations, or a global abundance-to-extension argument; the theorem alone does not strengthen the known square-root bound.

This is a graph-only observation in the corrected boundary covering representation.
