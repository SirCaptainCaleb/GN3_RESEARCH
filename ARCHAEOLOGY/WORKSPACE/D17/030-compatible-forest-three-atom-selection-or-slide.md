# A DOUBLE recompletion either has a universal crossed atom or an in-class pure pair merge, and rim purity forces a SLIDE

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-three-atom-selection-or-slide`

**Summary:** For any non-Hamiltonian support W partitioned into three nonempty Hamilton atoms A,B,C with pc(W)=2, an atom A is incident to a selected cross-atom edge in every exact two-cover of W iff B union C is non-Hamiltonian. Thus either some atom is universally crossed, or all three pair unions are Hamiltonian and there are pure exact representatives A|H(B union C), B|H(A union C), C|H(A union B). At a DOUBLE portal in a terminal exchange class all such exact recompletions remain in the class. For the shortest-rim source portal K_i=(u1,u0,q_i,q_{i-1}) with residual rim atom R_i=(q_{i+1},...,q_{i-2}), the pure representative K_i|R_i|H(U_i union V) has merge edge h_i=q_{i-1}q_{i+1}; all-chord rigidity makes h_i uniformly SOURCE or SINK, so exactly one of its two merge seams is tight. Hence the pure branch automatically emits a reversible SLIDE inside any closed class containing it.

### 1. Three-atom exact-cover selection equivalence
Let W be a finite boundary tournament with pc(W)=2, and suppose its vertex set is partitioned into three nonempty supports

  W=A disjoint_union B disjoint_union C

each carrying a retained Hamilton tight path. For an exact two-cover T of W, call A TOUCHED when T selects at least one adjacency with exactly one endpoint in A.

Then

  A is touched in EVERY exact two-cover of W
  iff
  B union C is non-Hamiltonian.                         (TA.1)

Proof. If B union C is Hamiltonian, choose a Hamilton path P_BC on it. Together with the retained Hamilton path on A, the cover

  A | P_BC

is an exact two-cover of W and has no selected A|(B union C) crossing, so A is not universally touched.

Conversely suppose some exact two-cover T has no selected crossing incident with A. Any T-rail containing an A-vertex can then contain only A-vertices, because the first selected adjacency leaving A would be such a crossing. Both T-rails cannot contain A-vertices, since then both would lie wholly in A and B union C would be uncovered. Hence exactly one T-rail consists of all of A and the other T-rail consists of all of B union C. The latter is therefore a Hamilton path on B union C. This proves (TA.1).

The same statement holds cyclically for B and C.

### 2. Universal-atom versus pure-pair branch
Equation (TA.1) gives an exact support dichotomy.

If at least one pair union is non-Hamiltonian, the opposite atom is touched in every exact two-cover.

If no atom is universally touched, then all three pair unions are Hamiltonian. Conversely if all three pair unions are Hamiltonian, each atom is avoidable. In that branch there exist the three literal pure exact representatives

  A | H(B union C),
  B | H(A union C),
  C | H(A union B),                                     (TA.2)

where H(X) denotes any retained Hamilton path on support X.

No synchronization of the three Hamilton orders in (TA.2) is asserted.

### 3. Closed exchange-class consequence at a DOUBLE portal
Now work in a hypothetical smallest counterexample and in the finite exchange digraph of literal maximum three-forests used by the current Director guidance. Let F lie in a terminal strongly connected class and let one DOUBLE seed have reverse-P4 carrier K. Write

  H-V(K)=A disjoint_union B disjoint_union C

for the three named nonempty Hamilton residual pieces inherited from that DOUBLE portal.

Every exact two-cover T of H-V(K) gives the permitted successor K|T. Terminality therefore keeps EVERY such successor in the same terminal class. Applying Sections 1-2, the portal has one of two support-level outcomes inside the class:

  UNIVERSAL ATOM: some one of A,B,C is crossed in every exact recompletion;

  PURE PAIR FAMILY: all three pair unions are Hamiltonian, and all three states K|A|H(B union C), K|B|H(A union C), K|C|H(A union B) lie in the class.       (TA.3)

This uses the universal quantifier supplied by terminality. It does not choose one arbitrary crossing per portal.

### 4. On a shortest rim, one pure representative forces a SLIDE
Specialize to the source-side shortest-rim DOUBLE portal of `compatible-forest-rim-double-crossing-fan`. Thus

  K_i=(u_1,u_0,q_i,q_{i-1}),
  R_i=(q_{i+1},q_{i+2},...,q_{i-2}),
  U_i=U[2,a],

and H-V(K_i) has the named three-cover R_i|U_i|V.

Assume the PURE PAIR FAMILY branch. Then in particular U_i union V is Hamiltonian, so the exact successor

  K_i | R_i | H(U_i union V)                            (TA.4)

is available; inside a terminal class it is in-class.

Consider the ordered merge from terminal q_{i-1} of K_i to source q_{i+1} of R_i. Its physical merge edge is the non-rim chord

  h_i={q_{i-1},q_{i+1}}.

The two merge turns are

  alpha_i=(q_i,q_{i-1},q_{i+1}),
  beta_i =(q_{i-1},q_{i+1},q_{i+2}).                    (TA.5)

By the all-chord rigidity of SV24086, h_i is either uniformly SOURCE or uniformly SINK relative to all incident rim edges. If SOURCE(h_i), then alpha_i is bad and beta_i is tight. If SINK(h_i), alpha_i is tight and beta_i is bad. Therefore exactly one hole in (TA.5) is bad.

By the SLIDE/DOUBLE theorem SV22098, (TA.4) consequently has a unique reversible distance-two SLIDE between K_i and R_i. Thus the all-pair-Hamiltonian portal branch is not a static crossing-color residue: on a shortest rim it automatically emits another legal representative switch.       (TA.6)

No claim is made that repeated SLIDEs decrease a global potential or preserve the original rim component. The theorem supplies the realizable in-class successor demanded by the closed-exchange-class strategy.
