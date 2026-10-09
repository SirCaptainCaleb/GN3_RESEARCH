# Two-cap orientation disagreement on a monochromatic codimension-two core forces NORI grand closure

# Active NORI: both missing-direction cap orientations must agree at EVERY endpoint of a near-spanning mono core

Fix active reversal-antipodally odd ordered-three-face coloring c on Q_n, n>=5. Fix U⊆[n], |U|=n-2, with missing directions a,b, and a projected U-root r. For each i∈U, define two physical ordered-face cap bits
\[
A_i(r)=c(F(x;\{a,b,i\}),(a,b,i)),\qquad
B_i(r)=c(F(x;\{a,b,i\}),(b,a,i)),
\]
where x is any cube vertex with U-projection r. Both bits are independent of x_a,x_b, because a,b are free directions of the physical face. Set
\[
S(r)=\{i∈U:A_i(r)=B_i(r)\},\qquad T(r)=U\setminus S(r).
\]

**THEOREM 1 (oriented-cap disagreement gives immediate grand closure).** Suppose a directed MONOCHROMATIC U-spanning geodesic P exists in ANY of the four parallel U-facets, from projected root r to its U-antipode. Let its first direction be i and its last direction j. If i∈T(r) OR j∈T(r), then the full active NORI one-switch grand conclusion follows. Consequently, in every hypothetical counterexample, i,j∈S(r), and for every such path with monochromatic color q,
\[
\boxed{A_i=B_i=q,\qquad A_j=B_j=1-q.}
\]

**PROOF.** Let x be the physical root of P, y=x⊕U, q the common ordered-three-face window color. Consider the TWO full n-edge antipodal geodesics obtained by PREPENDING the unused directions a,b in orders (a,b) and (b,a), then following P. Their full window words have the form
\[
(A_i,\ s_{b,i},\ q,\ldots,q),\qquad
(B_i,\ s_{a,i},\ q,\ldots,q),
\]
where s_{b,i},s_{a,i} are the respective middle new windows (these values need not be related). For a three-symbol prefix (t,s,q) followed by all q's to exhibit at least TWO switches, it is NECESSARY that t=q and s=1-q. Thus if A_i≠B_i, at least one of them differs from q, and its full extension has AT MOST ONE switch. This proves closure for i∈T.

For the end, APPEND the two unused directions in orders (b,a) and (a,b). The last three window colors are
\[
(q,\ t_{j,b},\ C_j),\qquad(q,\ t_{j,a},\ D_j),
\]
where
\[
C_j=c(F(y;\{a,b,j\}),(j,b,a))=1-A_j,\quad
D_j=c(F(y;\{a,b,j\}),(j,a,b))=1-B_j
\]
by the exact reversal of ordered triples on antipodal physical faces. If A_j≠B_j, then C_j≠D_j, so at least one of the two terminal cap colors C_j,D_j equals 1-q. The corresponding full word, whose first long block is q, has at most one switch (independently of the middle new window). This proves closure for j∈T.

Under the no-closure hypothesis, ALL four full extensions are bad. The same prefix/suffix alternation calculation therefore forces A_i=B_i=q and C_j=D_j=q. Rewriting the latter gives A_j=B_j=1-q. QED.

**THEOREM 2 (four-facet stable-cap bipartite restriction).** Define the COLOR-FREE first/last memory graph H_U(r) as in the canonical four-facet cap theorem, using all directed monochromatic U-spanning geodesics from projected root r over the four exterior (a,b)-facet assignments, omitting their colors. Under grand failure every edge has both endpoints in S(r), and they lie in opposite classes according to their COMMON cap bit A_i=B_i. Thus all vertices of T(r) are isolated, and the nonisolated portion of H_U(r) lies inside the complete bipartite graph of stable-cap classes
\[
S_0(r)=\{i:A_i=B_i=0\},\quad S_1(r)=\{i:A_i=B_i=1\}.
\]
In particular,
\[
|E(H_U(r))|\le |S_0||S_1|\le \big\lfloor |S(r)|^2/4\big\rfloor.
\]
The number of directed monochromatic U-spanning geodesics in the FOUR parallel facets with projected start r is bounded above by
\[
8|S_0||S_1|(n-4)!,
\]
or a proportion at most \(2|S_0||S_1|/[(n-2)(n-3)]\) of all four-facet directed U-geodesics. The bound may be zero if either stable-cap class is empty.

**Proof.** Every actual monochromatic U-spanning witness must begin and end in the stable set and cross the cap-color cut by Theorem 1. There are at most 2|S_0||S_1| ordered distinct first/last direction choices, at most (n-4)! ways to permute the remaining U-directions, and four exterior facet assignments. The claimed counting and graph bounds follow. QED.

**Topological forcing target.** This strengthened cap obstruction uses TWO independently colored orientations on the SAME physical three-face and exploits their simultaneous extension possibilities. For a successful all-root fixed-point/connector proof, one could force a long mono U-path incident to an unstable cap direction i∈T(r), or force nonbipartiteness on the stable-direction memory graph. No arbitrary fixed root is required, and no color is included in the reachability-graph definition.

## Exact eight-cap obstruction: all four two-direction completions are bad iff eight bits are forced

Let P be a monochromatic directed U-spanning path in one of the four U-facets, with direction word (i,k,...,l,j), q-color windows, physical start x and end y=x⊕U, and missing directions a,b. Write h=n-4>=1 for its number of existing three-face windows.

There are exactly FOUR full antipodal paths obtained by adding BOTH missing directions at ONE end:
- Front (a,b,P): window word (A_i,S_b,q^h), where S_b=c(F(x;{b,i,k}),(b,i,k)).
- Front (b,a,P): window word (B_i,S_a,q^h), where S_a=c(F(x;{a,i,k}),(a,i,k)).
- Back (P,a,b): window word (q^h,T_a,1-B_j), where T_a=c(F(y;{l,j,a}),(l,j,a)).
- Back (P,b,a): window word (q^h,T_b,1-A_j), where T_b=c(F(y;{l,j,b}),(l,j,b)).

The initial caps A_i,B_i and terminal-reversed caps A_j,B_j are the ones defined above in the stable-cap theorem.

**EXACT theorem.** ALL FOUR displayed full antipodal paths have at least two color changes IF AND ONLY IF the following EIGHT binary constraints hold simultaneously:
\[
A_i=B_i=q,\qquad A_j=B_j=1-q,\qquad
S_a=S_b=T_a=T_b=1-q.
\]
Equivalently, ANY violation of this rigid eight-window pattern forces an actual full one-switch antipodal NORI geodesic obtained by one of these four explicit completions.

**Proof.** A binary word of the form (t,s,q,...,q) has two changes exactly when t=q and s=1-q. Similarly (q,...,q,s,t) has two changes exactly when s=1-q and t=q. (These four completions have at most two new transitions.) Apply this iff to each of the four displayed words. For the two terminal caps, use c(F(y;{j,a,b}),(j,a,b))=1-B_j and c(F(y;{j,b,a}),(j,b,a))=1-A_j, consequences of the active antipodal-reversal law. This yields the stated eight constraints as an equivalence. QED.

**Strategic significance.** The no-closure regime imposes a local **eight-window 0/1 rigidity system** around EVERY monochromatic codimension-two core, uniformly across all roots and direction supports. Several such cores with overlapping endpoint cap faces can therefore produce immediate algebraic contradictions, even if their first-last direction memory graphs are bipartite. Forcing such incompatible core overlaps is still unresolved.
