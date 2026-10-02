# 43/48 near-extremizers reduce to a dense doubly-terminal-single rainbow graph

## Statement

Let (H_j) be a sequence of finite linear 3-graphs satisfying the 43/48 near-extremal hypotheses of d287da5967d5:
  S_j=sum_v phi(v),  S_j/n_j^+ -> infinity,
  |E(H_j)| >= (43/48)S_j-o(S_j).
Choose the maximum endpoint paths used in a57007500001.

Let U_11 be the set of ascending nonspecial edges e={x,u,v} whose contact multiplicity is one at both terminal endpoint paths P_u and P_v. Form the terminal graph G_11 with vertex set V(H), one graph edge uv for every e={x,u,v} in U_11, colored by its entrance x.

Then:
(1) |U_11|=(11/16-o(1))S_j.
(2) If d_11(v) is the degree of v in G_11, then
    sum_v (beta(phi(v))-d_11(v))_+ = o(S_j).
Consequently, for every fixed epsilon>0, all but o(S_j) endpoint-potential mass lies on vertices v satisfying
    d_11(v) >= (11/8-epsilon)phi(v).
(3) The coloring of G_11 by entrances is proper. A simple graph path lifts to a linear hypergraph path whenever it is strong-rainbow: its edge colors are pairwise distinct and none of those entrance colors is a vertex of the graph path.

Thus any asymptotic 43/48 extremizer contains, after discarding o(S) weighted defect, a properly edge-colored terminal graph whose local degree is asymptotically 11/8 times endpoint potential. Ordinary rainbowness alone is not asserted to guarantee a linear lift.

## Body

Write A for the number of ascending nonspecial edges, D=sum_v D_v for total double-contact incidences, eta=sum_v eta_v, and beta as in a57007500001.

By the exact identity and the 43/48 near-equality hypotheses, all four global defects are o(S), in particular
  D=o(S), eta=o(S), n_+=o(S).                         (1)
Also the exact local-deficit relation summed over vertices is
  sum_v beta(phi(v))=2A-D+eta.
Since beta(p)=(11/8)p+O(1) for p>=7 and bounded-p vertices contribute O(n_+),
  sum_v beta(phi(v))=(11/8)S+o(S).
Using (1),
  A=(11/16)S+o(S).                                    (2)

Now every ascending edge has exactly two terminal incidences. A terminal incidence on the chosen maximum endpoint path has multiplicity at least one. If an ascending edge is not in U_11, at least one of its two terminal incidences has multiplicity at least two, hence contributes at least one unit to D. Therefore
  A-|U_11| <= D.
Together with (1),(2),
  |U_11|=(11/16-o(1))S.                               (3)

For a vertex v let d_11(v) count U_11 edges terminal at v, and let
  m_v=t(v)-d_11(v)>=0.
Summing over v,
  sum_v m_v=2(A-|U_11|)<=2D=o(S).                     (4)
From eta_v=beta(p_v)-t(v)+D_v,
  beta(p_v)-d_11(v)=eta_v-D_v+m_v<=eta_v+m_v.
Hence
  (beta(p_v)-d_11(v))_+ <= eta_v+m_v.
Summing and using eta=o(S) and (4) proves
  sum_v (beta(p_v)-d_11(v))_+=o(S).                   (5)

Fix epsilon>0. For all sufficiently large p,
  beta(p)>=(11/8-epsilon/2)p.
If d_11(v)<(11/8-epsilon)p, then for such p
  (beta(p)-d_11(v))_+ >= (epsilon/2)p.
Equation (5) therefore shows that these bad large-p vertices carry o(S) potential mass. Bounded p contributes O(n_+)=o(S). This proves the degree-stability assertion.

Finally, color uv by the unique entrance x of the corresponding ascending edge {x,u,v}. The coloring is proper: two terminal-pair edges incident with the same terminal u and having the same color x would correspond to two distinct hyperedges both containing u and x, contradicting linearity.

For a simple graph path
  v_0 v_1 ... v_k
with edge colors x_1,...,x_k, consecutive parent hyperedges meet in the intended terminal v_i. For nonconsecutive graph edges, their terminal endpoint sets are disjoint. Their parent triples can therefore intersect only if two entrance colors coincide or if an entrance color of one parent edge is a terminal vertex of the other graph edge. Pairwise distinct colors eliminate the first possibility but not the second. Hence ordinary rainbow is insufficient. If, in addition, every entrance color avoids the graph-path vertex set, then neither obstruction occurs and the parent hyperedges form a linear path. Thus the correct lifting condition is strong-rainbow: pairwise distinct colors, all avoiding the graph-path vertices.