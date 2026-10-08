# Active NORI: matched first-last monochromatic codimension-two cores force opposite colors; odd memory cycle closes

# Active NORI: antipodally forced opposite colors for matched first/last near-spanning monochromatic cores

Let n>=5, and let c be a binary coloring of physical ORDERED three-faces satisfying the ACTIVE reversal-odd axiom
\[
c(\bar F,\operatorname{rev}\pi)=1-c(F,\pi).
\]
Fix a set U⊂[n] of size n-2, write [n]\U={a,b}, and fix a physical U-facet with endpoints x,y=x⊕U. Consider directed MONOCHROMATIC U-geodesics P,Q from x to y; their direction orders may differ, and their colors are arbitrary.

**THEOREM 1 (two-cap antipodal synchronization).** Suppose the FIRST direction of P equals the LAST direction of Q, say i∈U. If P and Q have the SAME monochromatic ordered-three-face-window color, then there exists a full n-edge antipodal geodesic with AT MOST ONE ordered-three-face color change. Equivalently, under a hypothetical NORI counterexample, EVERY such matched pair P,Q must have OPPOSITE witness colors.

**Proof.** Suppose no full good antipodal geodesic exists, and write q for the monochromatic window color of P. For each unused direction j∈{a,b}, prepending j to P creates a length-(n-1) geodesic whose word consists of one new first color followed by q's. If that first color equaled q, it would be a MONOCHROMATIC (n-1)-edge geodesic, whose remaining unused coordinate could be appended to obtain a FULL good n-geodesic with at most one change. Hence EVERY such new first window has color 1-q. In particular, prepending b yields the ordered three-face (b,i,p_2) at x of color 1-q.

Now prepend BOTH a and b in that order to P. This full antipodal path has window color word
\[
(t,\ 1-q,\ q,\ldots,q),
\]
where \(t=c(F(x;\{a,b,i\}),(a,b,i))\). The only way this word can have at least TWO color changes is \(t=q\). Therefore
\[
c(F(x;\{a,b,i\}),(a,b,i))=q. \tag{1}
\]

Similarly write r for the monochromatic color of Q, whose LAST direction is i. Append b and then a to Q. By the symmetric one-coordinate argument, its penultimate new window (last two old directions, b) has color 1-r. To avoid a good full path, its final ordered window, (i,b,a), must have color r:
\[
c(F(y;\{i,b,a\}),(i,b,a))=r. \tag{2}
\]

Because y=x⊕U and U=[n]\{a,b}, one has \bar x=y⊕e_a⊕e_b. The free coordinate set of both (1) and (2) is {a,b,i}. The vertices \bar x and y differ only in free coordinates a,b, so the physical three-face through y with free {a,b,i} is EXACTLY the antipodal physical face of F(x;{a,b,i}). The ordered triples (a,b,i) and (i,b,a) are reversals. By the NORI axiom, the left sides of (1),(2) sum to 1 mod2. Hence
\[
\boxed{r=1-q.}
\]
If q=r this is impossible, proving grand closure. QED.

**THEOREM 2 (COLOR-FREE odd directed cycle extraction).** For each such fixed facet and projected endpoint pair {x,y}, construct a directed multigraph \(G_{U,x}\) on the n-2 free coordinate directions U as follows. For EVERY monochromatic directed U-geodesic P from x to y, introduce a directed edge
\[
\operatorname{first}(P)\longrightarrow\operatorname{last}(P).
\]
The graph is defined by EXISTENCE of monochromatic paths and their geometric endpoint memories; omit every path's monochromatic color from the graph. If this directed multigraph contains a directed cycle of ODD length, then the active NORI grand conjecture holds.

**Proof.** Under a hypothetical no-closure coloring, assign to each graph edge its monochromatic witness color q(P). By Theorem 1, consecutive edges in a directed walk (whose adjoining coordinate is the last direction of the first and first direction of the second) MUST have opposite witness colors. Thus around a directed cycle these colors alternate. An odd directed cycle demands q=1-q at its starting edge, impossible. Multiple differently colored witnesses of one geometric edge may be treated as distinct parallel edges; the same argument applies to any chosen directed cycle of witnesses. Contraposition proves the assertion. QED.

**An explicit compatibility criterion.** A directed 3-cycle
\[
a_1\to a_2\to a_3\to a_1
\]
of three monochromatic U-spanning geodesics with matched first/last coordinate memories is ALREADY enough for full grand closure. No matching of internal direction orders, path colors, or starting vertex colors is required. The witness paths share only their physical U-facet endpoints x,y.

**Important scope.** The result uses the *actual ordered-three-face NORI antipodal-reversal condition*, not merely the simpler edge-geodesic proving ground. It is a dimension-independent sufficient condition, conditional on existence of two or more monochromatic n-2-edge facet cores. It does NOT assert such cores exist in arbitrary high dimension or force an odd directed cycle. The new structural target is to obtain one nonbipartite/odd-cycle first–last-memory digraph from the full family of color-free monochromatic facet reachability witnesses.

## Strengthening: the two cores may start at neighboring roots

**Theorem 3 (root-mobile first/last pivot).** Retain the same fixed U-facet and complement {a,b}. Let P be a monochromatic U-spanning geodesic from x to x⊕U whose first direction is i. Let Q be a monochromatic U-spanning geodesic from x' to x'⊕U whose last direction is i, where
\[
x'\in\{x,\ x\oplus e_i\}.
\]
Under a hypothetical NO-grand-closure coloring the two monochromatic colors MUST differ. Hence a matching-color pair of such geodesics, even with the two roots shifted by i, forces a full one-switch antipodal n-geodesic.

**Proof.** The front two-coordinate extension argument from Theorem 1 gives the forced cap color q(P) at the physical face F(x;{a,b,i}) in order (a,b,i). The back extension of Q gives its color q(Q) at F(x'⊕U;{a,b,i}) in reversed order (i,b,a). Since x' equals x or x⊕i, the physical endpoints x'⊕U and x⊕U differ only possibly in i; and \bar x=(x⊕U)⊕a⊕b. Thus the physical face through x'⊕U with free coordinates {a,b,i} is exactly the antipodal face of F(x;{a,b,i}): their bits on all exterior coordinates U\{i} are complements. Applying the active NORI antipodal-reversal law gives q(Q)=1-q(P). QED.

**Root-mobile color-free signed connector.** Let \mathscr P_U collect ALL monochromatic directed U-spanning geodesics across all physical U-facets and all roots, recording their ordered first and last directions but not their color. Introduce a sign-1 (potential-flipping) directed edge P→Q whenever P,Q are in the SAME physical U-facet, first(P)=last(Q)=i, and root(Q) equals root(P) or root(P)⊕e_i. By Theorem 3, in a hypothetical counterexample every such connector enforces q(Q)=1-q(P). Add the actual global antipodal-reversal involution ΘP, which lives in the opposite U-facet and also has q(ΘP)=1-q(P), as sign-1 edges P↔ΘP. Any undirected closed walk in the resulting signed multigraph containing an ODD number of these potential-flipping edges yields a full NORI witness (contradiction to binary color consistency). The graph's vertices and edges are defined entirely by existence and geometric memories of genuine monochromatic geodesics, with colors entering only in the proof of the signed extraction.

This enriches the fixed-root endpoint-memory digraph by a genuine single-coordinate root slide. The unsettled topological obligation is to force an odd signed cycle in this root-mobile graph, or an alternative complementary-tail overlap, for every active NORI coloring.
