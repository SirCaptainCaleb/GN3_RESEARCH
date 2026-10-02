# Branching in a reduced support tree prevents rounding by two selected paths

**Summary:** A branching reduced support tree gives fractional mass two while no pair of selected paths even has spanning union; integral rounding must create a new support.

## Statement

Let H be a finite boundary 3-tournament with pc(H)>2, with one two-cover selected for every deletion. Suppose its selected support graph J is a connected tree, with support S_u at vertex u. For distinct u,v, S_u union S_v=V(H) if and only if the u-v tree path P has even length and every edge outside P is pendant and attached at odd distance from u along P; then S_u intersect S_v is exactly the set of labels outside P. In particular, suppose J has bipartition X,Y with |X|>|Y|, deg(x)<=2 for x in X and deg(y)>=2 for y in Y. Let K be the tree on Y obtained by deleting X-leaves and suppressing remaining degree-two X-vertices. The fractional cover number restricted to {S_u} is two, but a pair of selected supports has spanning union if and only if K is a path. If K branches, no selection and trimming of two displayed paths can give a spanning two-cover. This is a conditional obstruction within the selected family, not a counterexample to general rounding.

## Body


Let H, J, and S_u be as in the connected selected-support tree theorem: pc(H)>2, one deletion cover is selected at every ground label, and J is a tree with those labels as its edges. Let u,v be distinct vertices of J, and let P be their unique tree path.

**Lemma.** S_u union S_v=V(H) if and only if P has even length and every edge outside P is a pendant edge attached to an odd-distance vertex of P, with distance measured from u. In that case S_u intersect S_v is exactly the set of labels of the edges outside P.

**Proof.** Membership of an edge label e in S_w is determined by the parity of the distance from w to the nearer endpoint of e: membership holds precisely when that distance is odd. This is the rooted tree formula of deletion_supports_form_a_forest_or_a_spanning_odd_cycle.

If P has odd length, its first edge has distance zero from u and even distance from v. Its label is therefore absent from both supports, so their union is not V(H).

Suppose P has even length. The symmetric-difference formula in deletion_supports_form_a_forest_or_a_spanning_odd_cycle gives S_u symmetric-difference S_v=labels(P). Thus every edge label on P belongs to exactly one support, while every label off P belongs either to both or to neither.

An off-path branch begins at a path vertex p at distance j from u. The first edge of that branch belongs to both supports exactly when j is odd. If the branch has a second edge, that edge has nearer-endpoint distance j+1, so when the first edge is included, the second is omitted by both supports. Therefore all off-path labels can be covered only when every off-path edge is pendant and attached at an odd-distance path vertex. Conversely, under that condition every off-path edge label belongs to both supports. This proves both claims.

## Consequence for the mass-two tree shapes

Suppose J has bipartition X,Y with |X|>|Y|, every X-vertex of degree at most two, and every Y-vertex of degree at least two. Form a tree K on Y by deleting the X-leaves and suppressing each remaining degree-two X-vertex. The edges of K correspond to two-edge paths of J; this construction is well-defined because every nonleaf X-vertex has degree two. Here |Y|>=3, as each selected deletion component has order at least two.

**Corollary.** Two selected supports have union V(H) if and only if K is a path.

For necessity, the lemma forces every vertex off the path P in J to be a leaf in the same bipartition class as its endpoints. The endpoints cannot lie in Y, since every Y-vertex has degree at least two and the lemma allows no extra edge at either endpoint. Hence the endpoints lie in X, and every Y-vertex lies on P. All the edges of K are therefore on one path, so K is a path.

For sufficiency, if K is a path, each of its two end Y-vertices has at least one adjacent X-leaf in J: its degree in J is at least two, and only one incident edge leads into K. Choose one such leaf at each end. Their path in J has even length, contains every degree-two X-vertex and every Y-vertex, and all its omitted edges are X-leaf edges attached to Y-vertices. These are exactly the odd-distance vertices along the path. The lemma applies.

For these two supports, their intersection is the set of the other leaf-edge labels. The displayed Hamilton orders on that intersection need not agree, and its vertices need not occupy removable end segments. A spanning union therefore still does not establish a spanning two-cover.

In particular, if K branches, NO pair of selected supports has a spanning union, even though the selected-support family has fractional cover number two, as proved below. Any integral two-cover in H would have to use at least one Hamiltonian support outside this selected family. This is a conditional structural obstruction to rounding within the selected family, not a constructed counterexample to the grand conjecture or to general fractional rounding.


## Fractional mass two within the same family

For completeness the fractional claim used in this fence is proved here, so no unpublished premise is needed. Put a=|X|, b=|Y|, r=a-b>0 and s_u=1_{S_u}. There are n=a+b-1 ground labels. Rooting the tree at x in X, the support formula of deletion_supports_form_a_forest_or_a_spanning_odd_cycle identifies S_x with the parent edges of X-{x}. Sum the identities s_u+s_v=1_V-1_d over these edges and move s_x to the left. This gives
sum_X s_x + sum_Y(deg(y)-1)s_y=(a-1)1_V.
Rooting in Y gives
sum_Y s_y + sum_X(deg(x)-1)s_x=(b-1)1_V.
Subtracting,
sum_X(2-deg(x))s_x + sum_Y(deg(y)-2)s_y=r1_V.
All coefficients are nonnegative under the stated degree conditions and their sum is 2r. Division by r gives a fractional cover of mass two using only the selected supports, with each ground vertex covered once.

This is also optimal within that family. Since |Y|>=3 and X has maximum degree two, some X-vertex x has degree two. Give weight one to each of its two incident ground-edge labels and zero to all other labels. S_x contains neither. For every other support vertex u, the nearer-endpoint distances from u to these two edges differ by one, so S_u contains exactly one of their labels by the membership parity formula. Thus no selected support has weight exceeding one, while the ground set has weight two. This supplies a restricted dual lower bound of two.

Scope: this restricted dual weighting is not asserted feasible on all tight paths. Neither existence of a counterexample H with this tree shape nor failure of general fractional rounding is asserted. The conclusion identifies what an integral construction would have to add: when K branches, at least one resulting path must have support outside the selected family, and trimming any two selected paths is insufficient. When K is a path the spanning-union criterion removes this set-theoretic obstruction, but the overlapping Hamilton orders still require a genuine gluing argument.


## Metadata

- ID: a_reduced_support_tree_prevents_rounding_by_two_selected_paths
- Kind: toolkit
- Version: 1
- Math version: 1
- Audit: unaudited
- Refutation: unrefuted
