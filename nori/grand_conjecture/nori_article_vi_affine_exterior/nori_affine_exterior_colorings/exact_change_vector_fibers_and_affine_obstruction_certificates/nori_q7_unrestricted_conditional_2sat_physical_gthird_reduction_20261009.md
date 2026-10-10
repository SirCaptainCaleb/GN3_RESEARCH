# Unrestricted Q7 exact conditional 2-SAT and implication-cycle obstruction

# Exact conditional 2-SAT reduction for unrestricted physical Q7

Fix a direction g in any antipodally reversal-odd binary coloring of ordered physical three-faces of Q7. Let R be the six other directions. Prescribe an arbitrary legal coloring h of the g-containing ordered physical three-faces; h has 720 free Boolean reversal-orbit variables. The no-g faces have exactly 960 free Boolean variables: write f(F,π) for the face with fixed g-bit 0, where F is a physical ordered residual Q6 three-face (20 free supports × 6 orders × 8 exterior assignments). Every no-g face with fixed g-bit 1 is then forced to have color 1−f(bar F,reverse π), where bar F complements all residual coordinates. Thus f is completely unrestricted on its 960 variables.

For each residual starting root y and residual direction order p=(a,b,c,d,e,f), take the genuine full direction order (a,b,g,c,d,e,f). Let G=(G1,G2,G3) be its g-containing first three window colors; G does not depend on the initial g-bit. Let A,B be the **actual** trailing ordered residual faces with direction lists (c,d,e),(d,e,f), including prefix-flipped residual exterior coordinates. For initial g-bit 1 (so g is 0 after its traversal) the two final window colors are f(A),f(B). For initial g-bit 0 (so g is 1 after traversal) they are 1−f(A*),1−f(B*), where A*,B* denote the residual antipodal faces with reversed three-direction orders. Each f(·) is one of the 960 independent Boolean variables.

**Theorem (exact conditional 2-SAT formulation).** For this prescribed h, an assignment of no-g face colors avoiding every good full Q7 geodesic with g in the third move exists if and only if the following 2-CNF is satisfiable, taking all residual roots y and orders p:

• If G is alternating (G1=G3≠G2), insert no clause.

• If G is constant ttt, insert four unit clauses
  f(A)=1−t, f(B)=t, f(A*)=t, f(B*)=1−t.

• If G has exactly one change and ends in color t, insert two binary clauses
  (f(A)≠t) OR (f(B)≠t),
  (f(A*)=t) OR (f(B*)=t).

**Proof.** The first three window colors are fixed G. A constant G permits exactly the four bad-last-pair constraints listed: a trailing pair produces two changes iff it is (1−t,t). An exactly-one-change G is good iff both trailing colors equal its terminal bit t, so each g-start bit requires the indicated clause to block it. An alternating G already has two changes. The antipodal-reversal equation supplies precisely the two trailing color pairs used above, and all 960 f-variables are independent because their antipodal mates have the other fixed g-bit. Taking conjunction over every packet is equivalent to blocking every g-third full geodesic. QED.

**Certificate form.** Conditional on h, the test is linear-time 2-SAT via the implication digraph; UNSAT is equivalent to a variable and its negation belonging to the same strongly connected component. Thus **every** h admits a g-third good path if and only if **every** legal 720-bit h assignment produces a contradictory implication cycle. Establishing this universally would prove unrestricted Q7 closure; the grand n-dimensional conjecture additionally requires a dimension-independent mechanism. This reduction is fully exact for actual physical faces and arbitrary exterior dependence; it assumes no universal flipper.

**Link to special case.** Under a universal exterior flipper g, the 960 independent f-variables collapse to 480 complement-reversal-even orbits, and the resulting 2-SAT simplifies to the odd-cycle/bipartiteness formulation in nori_q7_flipper_odd_cycle_bipartite_reduction_20261009.
