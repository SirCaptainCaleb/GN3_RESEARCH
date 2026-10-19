# All-state four-gate feedback rigidity and paired-flat eight-cube compatibility dichotomy

- Stable ID: note_nori_rank_four_pointwise_sensitivity_cycle_r11510
- Author: unspecified; session provenance retained
- Primary home: subsection:obstruction_compatibility_and_a_programme_for_nori1_closure
- Labels: NORI1, paired-flat, Q8, Boolean-network, local-Jacobian, cycle-rigidity, two-pair-face, sensitivity, simultaneous-compatibility, positive-structural
- Lifecycle: active
- Epistemic status: proved
- Current version: 1
- Retention: current and at most one previous snapshot
- Created session: session_nori_r11510_3
- Updated session: session_nori_r11510_3
- Disposition: none
- Successor: none

## Related references

- note:note_nori_three_pair_obstruction_compatibility_r11510
- note:note_nori_pair_sensitivity_product_irreducible_cycles_r11510

## Research note

# Pointwise feedback rigidity of four self-dual gates

Let h:F2^4->F2^4 satisfy h_i(q+e_i)=h_i(q) and h_i(q+1111)=1+h_i(q). Suppose for all i!=j and q that D_jh_i(q)D_ih_j(q)=0, where D_jh_i(q)=h_i(q)+h_i(q+e_j).

**THEOREM.** At EVERY q the local digraph j->i iff D_jh_i(q)=1 contains a directed three- or four-cycle. The only possibilities are (a) four signed unary readers, containing a permanent directed 3- or 4-cycle; (b) three unary readers forming a permanent directed 3-cycle and one gate depending on all three other inputs; or (c) four three-input signed-majority gates, in which case the local digraph at every q is a tournament with indegrees (0,2,2,2), and the three nonsource vertices form a directed 3-cycle.

**PROOF.** An antipodally odd Boolean function of three inputs is one of six signed unary projections, two signed parities of three bits, or eight signed-input majority functions. Its essential input count is one or three. If a unary h_j reads i, then D_ih_j is identically one, so h_i cannot depend on q_j under the no-reciprocal hypothesis. Hence unary gates must read other unary gates. A nonempty closed functional reader network without loops or two-cycles on four labels has at least three unary vertices and a 3- or 4-cycle. In the remaining case, all gates use all three inputs. A full parity gate is impossible because all its derivatives are one while every other gate depends on its bit, creating a reciprocal pair. Hence all gates are signed majority functions. For each pair {i,j}, the two reciprocal sensitivities are balanced affine parity functions of the same remaining two bits, and disjoint activation requires them to be complementary. Thus precisely one direction per pair is active at every q. Each majority gate has local indegree zero or two. Since a tournament on four nodes has six arcs, its indegree multiset is (0,2,2,2). The unique source points to the other three; within their induced tournament each has indegree one, so they form a directed triangle. QED.

**PAIRED-FLAT APPLICATION IN DIMENSION EIGHT.** For any legal antipodally odd paired-flat Q8 coloring, let p_i=x_(a_i)+x_(b_i) and q_i=x_(a_i). The induced h_i^p(q)=f_i(x(q,p)) is self-dual and ignores q_i. If every four-face retaining two entire paired direction groups lacks monochromatic full geodesics, no local reciprocal derivative pair can appear: such a pair would make both gates nonconstant on the same four-face, so the established two-pair identity R=2E(a)E(b)>0 would give a red full geodesic there. Therefore all 16 q-states in each of the 16 parity fibers have an active directed cycle of length at least three.

**UNCONDITIONAL DICHOTOMY.** Every legal paired-flat Q8 coloring either has a monochromatic full geodesic in some two-pair four-face, or has an active local directed three- or four-cycle at all 256 vertices. In any four-majority parity fiber the local Jacobian is a tournament with one source and a directed triangle at every q.

**VERIFICATION.** A standalone exhaustive script nori_rank_four_local_cycles.py checks all 65536 self-dual four-gate networks. Of them 1248 avoid reciprocal derivatives at all 16 states: 480 all-unary, 640 with one three-input gate, and 128 with four three-input gates. Every one has the stated pointwise cycle property. Complete proof: nori_rank_four_pointwise_cycle.md.

**SCOPE.** This theorem improves the prior at-least-two-cycle-states-per-parity-fiber bound in the face-free four-pair branch. It does not itself construct a full red geodesic: activation can change when a red step changes the pair-parity fiber. The rank-four Boolean classification does not extend automatically to arbitrarily many paired directions, and unrestricted NORI1 remains open.
