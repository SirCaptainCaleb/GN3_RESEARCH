# All odd affine edge colorings with disjoint supports and loopless functional block dependencies admit every antipodal geodesic color vector

# Complete geodesic closure for disjoint odd affine supports on arbitrary LOOPLESS FUNCTIONAL BLOCK GRAPHS

**Setup and exact class.** Let [n] be partitioned into m>=2 NONEMPTY blocks of coordinate directions B_1,...,B_m. For each block j choose a nonempty ODD-cardinality support M_j⊆[n]. Assume:
(1) the M_j are PAIRWISE DISJOINT;
(2) for each j there exists a block index sigma(j) DIFFERENT FROM j such that M_j⊆B_(sigma(j)).
Thus sigma:[m]->[m] is an arbitrary LOOPLESS FUNCTION, permitted to have directed cycles with branching in-trees, and need not be injective. Let b_v∈F2 be arbitrary. Color the ACTUAL undirected physical edge of direction v∈B_j at vertex x by
    c_v(x)=b_v + Σ_{u∈M_j} x_u.
Since M_j∩B_j=empty, c_v is independent of x_v and hence is an undirected physical edge coloring. Since |M_j| is odd, c_v(bar x)=1+c_v(x), so this is a valid antipodally odd k=1 edge coloring. Each support may involve arbitrarily many exterior bits.

**THEOREM.** For every SUCH coloring, for EVERY target T=(T_v)∈F2^n, there are an ACTUAL root x∈Q_n and a direction permutation p of all n coordinates such that the genuine FULL x-rooted n-edge antipodal geodesic has color T_v on its direction-v edge for every v. In particular both constant target vectors give monochromatic antipodal geodesics. The m distinct nonzero row forms have disjoint supports and hence rank exactly m, so this gives all-dimensional closure at ANY rank m attainable by this class and arbitrarily large nullity n−m.

**Lemma 1 (functional-graph base ordering).** Let sigma:[m]->[m] be ANY loopless function, and choose arbitrary bits d_j∈F2. Then there exist initial register bits alpha_j∈F2 and a total order pi of the m distinct labels such that
    alpha_(sigma(j)) = d_j + 1{j precedes sigma(j) in pi}
for EVERY j simultaneously.

*Proof.* Each directed component of a finite loopless functional graph j->sigma(j) has one directed cycle of length at least two, with rooted in-trees attached. Choose an arbitrary strict total ordering of the cycle vertices. For every cycle arrow j->sigma(j), define alpha_(sigma(j)) by the displayed equality; each cycle vertex has a UNIQUE predecessor on its cycle, so these assignments are consistent. For every NONCYCLE vertex k choose alpha_k arbitrarily. For each tree arrow j->sigma(j), impose the precedence relation j<sigma(j) if alpha_(sigma(j))+d_j=1, and sigma(j)<j otherwise. These precedence constraints form a DAG: a directed cycle would have to contain an undirected cycle, while every undirected cycle lies wholly inside one functional cycle, whose edges were oriented consistently with the initially fixed strict total order. Choose a topological ordering of this DAG extending the chosen cycle order in each component. The displayed identities hold for every tree and cycle arrow by construction. QED.

**Lemma 2 (ODD functional interleaving with exact statistics).** Fix any loopless sigma:[m]->[m] and any POSITIVE ODD integers p_j. Fix any strict total order pi on the m labels, and put
    eps_j=1{j precedes sigma(j) in pi}.
For a word over these labels with exactly p_j copies of label j, define
    a_j=# {copies of j with an EVEN number of earlier copies of sigma(j)}.
Then for EVERY vector of integer targets 0<=a_j<=p_j satisfying a_j=eps_j mod2, there is a word with exactly these block counts and statistics.

*Proof.* Begin with the length-m word pi, containing one copy of each label and statistic eps_j. Add copies to each label in PAIRS. While all block counts remain odd, adding two copies of label j at the very FRONT contributes 2 to a_j, because the sigma(j) predecessor count is then zero. Adding two copies of j at the very END contributes 0 to a_j, because sigma(j) !=j and its current total number of letters remains odd. Either choice leaves every other statistic unchanged: the only possible effect on predecessors of another label i occurs if sigma(i)=j, and the number of extra j predecessors is either 0 or 2, preserving parity. For prescribed p_j and a_j, induction in steps of two works as follows: if a_j<=p_j-2, solve the smaller case p_j-2 with the SAME a_j and append two j letters; if a_j>=2, solve the smaller case with a_j-2 and prepend two j letters. These two cases cover every 0<=a_j<=p_j for odd p_j>=3. The initial p_j=1 forces a_j=eps_j. Adjust the different labels in any sequence; the other statistics are unchanged. QED.

**PROOF OF THE THEOREM.** Fix an arbitrary target T, and write q_v=b_v+T_v. For a root x put
    alpha_j=Σ_{u∈M_j}x_u.
Because supports M_j are nonempty and PAIRWISE DISJOINT, every prescribed alpha∈F2^m is attainable by some actual root x (set one coordinate within each M_j accordingly, others arbitrary).

A direction v∈B_j traversed in a full direction order p has exact physical color
  C_v=b_v+alpha_j + #{M_j directions traversed before v} mod2.
Thus C_v=T_v iff the parity of preceding M_j directions equals alpha_j+q_v.

Now restrict attention to the MARKED directions in M_1∪...∪M_m. Every M_k lies in class B_(sigma(k)), so every direction v∈M_k is colored according to register alpha_(sigma(k)) and the preceding parity of M_(sigma(k)). Let p_k=|M_k|, positive odd, and let
  d_k= #{v∈M_k: q_v=0} mod2.
For any chosen alpha_(sigma(k)), put
  a_k= #{v∈M_k: q_v=alpha_(sigma(k))}.
Since p_k is odd, the parity identity is
  a_k mod2 = d_k+alpha_(sigma(k)).
Apply Lemma1 to the loopless functional graph sigma and these prescribed d_k. It gives a base total order pi and independently realizable register bits alpha such that
  d_k+alpha_(sigma(k))=1{k precedes sigma(k) in pi}=eps_k.
Hence each exact integer a_k has the parity eps_k required by Lemma2.

Apply Lemma2 to construct an interleaving of the m MARKER-TYPES k, with exactly p_k copies of each k and precisely a_k occurrences of k at an even preceding M_(sigma(k)) parity. For each type k, assign the ACTUAL named directions v∈M_k with q_v=alpha_(sigma(k)) to those even-parity slots, and those with q_v=1+alpha_(sigma(k)) to its odd-parity slots. The numbers match by definition of a_k. Thus every MARKED direction traverses at exactly its required physical color.

For each remaining UNMARKED coordinate v∈B_j\(∪_k M_k), its traversal toggles NONE of the support-register parities, since v lies in no M_k. The marked interleaving contains an odd, hence nonzero, number of directions from M_j; therefore there is a genuine insertion gap with preceding M_j parity0 (before the first M_j marker) and one with parity1 (after it). Insert v in any gap with parity alpha_j+q_v. Multiple unmarked insertions may share any gaps; they change no parity checks. The marked and unmarked directions now form a permutation p of ALL n coordinates satisfying the target conditions. Choose the actual root x with the alpha-register values already fixed by Lemma1. The corresponding direction-distinct length-n cube path is a GENUINE antipodal GEODESIC, with every direction-edge color exactly T_v. QED.

**Recovery and strict extension of existing NORI edge results.**
- If every M_j is a singleton, grouping directions into the B_j by their common driver coordinate recovers EVERY valid functional single-bit-dependency edge coloring c_i(x)=x_(j(i))+b_i, including branching functional graphs, as in nori_k1_functional_single_bit_dependency_all_pattern_geodesic_closure_20261009.
- If sigma is a permutation (no branching), one recovers ALL cyclic block-dependence odd-affine colorings nori_k1_odd_block_cyclic_affine_all_rank_all_pattern_interleaving_20261009; there the supports M_j are automatically disjoint because each lives in a distinct block. The present result newly permits an arbitrarily branching sigma when its different marked support sets remain disjoint inside shared driver blocks.
- The rank-two theorem is the special m=2 case: odd row classes I,J and their supports lie in the opposite block.
- Supports M_j can each have size 3,5,7,..., so the theorem resolves high-arity affine dependence patterns that are not 2-juntas and need not have rank>=n-2.

**Algorithm.** Determine the directed cycles and in-trees of sigma; assign cycle register bits and orient tree precedence edges by Lemma1; topologically sort the m marker types; grow the odd exact marked multiplicities using Lemma2's pair-front/pair-back construction; assign named coordinate directions to slots by target colors; insert unmarked coordinates at appropriate parity gaps; solve independent support parity equations for root x. All operations are finite and polynomial-time (one can implement them in O(n²) straightforwardly).

**Exact remaining difficulty.** The proof relies on DISJOINT supports M_j, guaranteeing independent root registers, and on each support living in one driver block so that marker type k has one well-defined successor sigma(k). If supports overlap, one physical direction can change several registers simultaneously; if a support spreads over multiple blocks, one marker type has conflicting color requirements. General odd affine matrices and arbitrary nonlinear edge colorings still require new coupled order/root topology.

**Gauge equivalence for the unrestricted original edge conjecture (useful context).** In ANY family of antipodally odd UNDIRECTED cube-edge colorings closed under independently XOR-flipping all edges of each fixed coordinate direction, the following universal assertions are EXACTLY EQUIVALENT:
 (a) Every coloring in the family admits at least one monochromatic FULL antipodal geodesic.
 (b) For every coloring c in the family and EVERY target direction-indexed bit vector T, some FULL antipodal geodesic has actual direction-i color T_i for all i.
Proof: (b) trivially implies (a) with T=0. For (a)->(b), define a modified coloring c'_i(x)=c_i(x)+T_i; this preserves the antipodal oddness and belongs to the same family by directional gauge closure. Assumption (a) gives a monochromatic antipodal geodesic in c' of some color q. Its physically antipodal image is also a monochromatic antipodal geodesic, of the complementary color 1+q. Select whichever witness has c'-color 0. Along that witness the ORIGINAL c_i equals T_i in its unique direction-i edge. QED. The affine families in this item, and the entire class of arbitrary antipodally odd edge colorings, are closed under these directional gauges. Thus all-target surjectivity is a useful equivalent FORMULATION of universal monochromatic edge-geodesic closure, while the new solved subclasses still represent genuine advances.
