# Switch-prism Borsuk-Ulam localizes NOR obstruction to r-element Coxeter blocks — preserved pre-item development

## Switch-prism Borsuk--Ulam localization

Fix coordinate arity r and a reversal-odd directed NOR label h on n coordinates. Put m=n-r+1, and assume for contradiction that no coordinate order has at most one color change.

For an order pi=(v_1,...,v_n), a cut k in {0,...,m}, and a fixed threshold orientation eta in {+1,-1}, prescribe the target sign word
q_i=eta for i<=k and q_i=-eta for i>k.
A state (pi,k) is good exactly when the actual sign word epsilon_i=(-1)^{h(v_i,...,v_{i+r-1})} equals q_i for every i. Under counterexamplehood every state is bad.

Choose from each bad state a violating window nearest the cut; break distance ties by any fixed reversal-invariant order on the underlying physical window sets. If the selected window is
(v_i,...,v_{i+r-1}),
attach the type-A root
rho(pi,k)=e_{v_i}-e_{v_{i+r-1}}
in W={x in R^V: sum x_v=0}.

### Reversal symmetry
Reversal sends (pi,k) to (pi^rev,m-k). Because
epsilon_i(pi^rev)=-epsilon_{m+1-i}(pi)
and the threshold target transforms by the same rule with the same eta, violations correspond bijectively, cut-distance is preserved, and the chosen physical window is reversed. Hence
rho(pi^rev,m-k)=-rho(pi,k).

### Geometric switch space
Let P_V be the type-A permutohedron, whose vertices are coordinate orders and whose central inversion sends pi to pi^rev. Subdivide an interval I at the m+1 cut levels and form P_V x I. Its boundary is an (n-1)-sphere, and
(x,t) -> (-x,-t)
is a free antipodal involution.

Take any centrally symmetric triangulation refining the product cell structure. Put rho on state vertices and extend to subdivision vertices by the canonical average over incident state labels, then affinely over simplices. This produces a continuous odd map
F: boundary(P_V x I) -> W,
with dim W=n-1.
By Borsuk--Ulam, F has a zero.

The important point is where such a zero can live.

### Localization theorem
Let G be a face of the permutohedron, represented by an ordered partition
B_1 | B_2 | ... | B_s
of V. Suppose every block has size at most r-1. Then zero does not lie in the convex hull of any switch labels attached to states whose permutation refines G.

Indeed define a block-rank functional phi on W by assigning a strictly increasing real number c_j to every coordinate in B_j. Any selected root is e_a-e_b where a is the first and b the last coordinate of an r-consecutive window in some linear extension of the ordered partition. Since no block contains r coordinates, a and b cannot lie in the same block. Therefore a lies in a strictly earlier block than b, so
phi(e_a-e_b)=c_{block(a)}-c_{block(b)}<0.
Thus all such roots lie in one open halfspace and their convex hull misses zero. The same remains true for averaged subdivision labels.

Consequently every Borsuk--Ulam zero projects to a Coxeter face containing a tied block of size at least r.

### Ternary consequence
For r=3, a zero cannot lie over:
- one chamber (a fixed coordinate order);
- a threshold-only edge;
- an adjacent-swap Coxeter edge, whose unique nontrivial block has size two.

The first possible Coxeter carrier has a three-element tied block. Its chamber residue is the rank-two A_2 braid hexagon on those three coordinates. Hence the switch-aware topological obstruction is forced directly into the same rank-two residues where centered directed triangles, three-element front circuits, and tetrahedral curvature first appear.

This gives a more faithful topology than support-only Sperner labels. The extra interval remembers whether the unique switch has occurred, while the root label remembers the ordered endpoints of an actual violating window. Ordinary Borsuk--Ulam does not yet finish NOR: a zero gives a positive root circulation among violating windows in one higher-rank Coxeter face. The next task is to analyze a minimal zero carrier. In ternary arity the hoped-for strengthening is that its minimal block can be reduced to an A_2 braid hexagon, where the circulation should translate into one of the already classified local surgery obstructions.
