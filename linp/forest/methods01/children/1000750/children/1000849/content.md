# Porting map from the external toolkit into LINP constructions

## Statement

The imported tools suggest four concrete construction/obstruction interfaces for improving the lower bound: algebraic ordered transitions, antipodal state complexes, disjoint-representative connector packing, and fixed-point direction labels. These are proposals for experiments, not established LINP implications.

## Body

1. Chung-style algebraic transition labels.
Target: a dense linear 3-graph component H built from a vector space or recursively split vertex set. Assign each legal transition between intersecting hyperedges a label in F_2^k or another ordered group. Seek a canonical orientation/order so that any linear path induces a monotone label sequence. The dream identity is an analogue of
  sum_{i=r}^s a_i = state_{r-1}-state_s,
so repeated/forbidden path states become zero interval sums. If this works, finite projections can bound path length while density remains quadratic in the base size. The existing one-factorization lift fence d2b4ebd1c7fd shows that the naive color-as-third-vertex realization is too path-rich; the algebraic ordering must actually constrain traversal, not merely label it.

2. Cube/antipodal state space.
For a product or blow-up construction with d binary local choices, define a state graph on {0,1}^d. Opposite states should correspond to reversing all local choices or exchanging two complementary endpoint/blocker roles. Color a state transition by which obstruction type prevents the desired continuation. If antipodal transitions receive complementary types, Norine/Tucker becomes relevant. Before invoking the full theorem, inspect Q_2,Q_3,Q_4 patterns: a local square rule may already force a splice.

3. Aharoni--Haxell/Ryser connector packing.
At a partial path state, let H_i be the family of legal connector gadgets serving obligation i (for example, entering a module, leaving it, bypassing an old intersection, or choosing a fresh joint). If every subfamily has large matching width, Aharoni--Haxell selects globally disjoint gadgets and tends to create a longer path. Therefore a P_ell-free construction must exhibit a subfamily with low matching width: a small pinning set controls many potential connectors. That contrapositive can be used as a DESIGN PRINCIPLE: deliberately engineer a small global pinning architecture that kills long traversals while preserving many edges.

For genuinely tripartite connector systems, Ryser gives an especially simple certificate. If connectors are triples (state choice, left resource, right resource), then tau<=2nu. To prevent a large disjoint connector matching it suffices to build a small transversal; conversely a large unavoidable transversal forces many disjoint connectors.

4. Pouzet/Tucker direction labels.
Parameterize a family of partial paths/construction states by an integer box or sign-vector poset. Assign to each state a coordinate direction saying which local move would extend/repair the path. If boundary conditions force moves inward, Pouzet gives adjacent states with opposite directions. If reversal gives antipodality, Tucker gives a complementary adjacent pair. The remaining LINP-specific task is to make an opposite pair algebraically splice into either a forbidden P_ell or a contradiction to the construction''s state definition.

Priority experiments.
(A) Revisit the binary-projective STS path obstruction branch (10428aea5095, 1b544fabb813, cdfc7cea9915): its F_2 structure is the best current host for Chung/Tucker ideas.
(B) For any new product/blow-up component, build the local-choice cube explicitly and enumerate square types before global search.
(C) When a path-extension search stalls because many candidate edges intersect, compute the associated matching-width/pinning problem rather than only ordinary matching number.

Success criterion. A useful new lower-bound component on N=N(ell) vertices and M edges must prove maximum linear-path length <ell while M/(N ell)>1/3 asymptotically (or improve the additive term on an infinite set of ell). The imported machinery is valuable only insofar as it certifies that path cap without destroying density.
