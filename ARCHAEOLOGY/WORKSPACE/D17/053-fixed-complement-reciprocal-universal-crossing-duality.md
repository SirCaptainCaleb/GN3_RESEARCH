# Reciprocal Hamilton replacements are exactly the quiet side of a universal-crossing matrix

**Workspace:** D17
**State:** established
**Key:** `fixed-complement-reciprocal-universal-crossing-duality`

**Summary:** In any smallest-counterexample fixed-complement critical block V(H)=Omega disjoint-union Q, fix a Hamilton puncture path P_y on Omega-y. For every y in Omega and q in Q, the reciprocal support Q-q+y is Hamiltonian exactly when the singleton residue H-q has a crossing-free exact representative (Q-q+y)|P_y relative to (Q-q)|(Omega-y). If Q-q+y is non-Hamiltonian, then the accepted exact fixed-hub dichotomy SV4445, applied to the source row Q|P_y of H-y and an arbitrary exact H-q cover, forces every such cover to select a physical (Q-q)|(Omega-y) crossing. Thus the complement of the reciprocal-support incidence matrix is precisely a universal-crossing matrix. If A(y,q) records Hamiltonicity of Omega-y+q, then A and reciprocal-Hamiltonicity cannot coexist in a counterexample, so every active replacement cell is automatically a universal-crossing cell on the reciprocal side. In the anchored quiet-triangle packet, each actual source transfer through q0 therefore makes q0 universally crossing relative to its source row. Two simultaneous transfers force every H-q0 cover either to hit their common active core or to select Q-q0 contacts to both exchanged triangle labels; three transfers force either a Q-q0 to M crossing or contacts to at least two distinct triangle labels.


### 1. Fixed-complement reciprocal cells
Retain the fixed-complement critical-block setting

  V(H)=Omega disjoint_union V(Q),

where H is a hypothetical smallest counterexample, Q is a retained literal Hamilton path, Omega is non-Hamiltonian and deletion-Hamiltonian, and for each y in Omega choose one actual Hamilton puncture path P_y on Omega-y. Then

  P_y | Q

is an exact two-cover of H-y.

For y in Omega and q in V(Q), define the reciprocal support predicate

  C(y,q) : Q-q+y is Hamiltonian.                         (RU.1)

The source row H-y=P_y|Q views q as a deletion label on the Q rail.

### 2. Reciprocal Hamiltonicity is equivalent to a crossing-free target representative
If C(y,q) holds, choose any Hamilton path K_{y,q} on Q-q+y. Then

  K_{y,q} | P_y                                         (RU.2)

is a literal two-cover of H-q. It is exact: if H-q were Hamiltonian, that Hamilton path together with singleton q would two-cover H. Moreover (RU.2) selects no adjacency between Q-q and Omega-y, because those supports lie on different rails.

Conversely assume C(y,q) fails. Let T be an arbitrary exact two-cover of H-q. Apply the accepted exact fixed-hub unit `singleton-fixed-hub-critical-dichotomy` SV4445 to the source row

  C_y = Q | P_y

of H-y, taking the source rail P in SV4445 to be Q, the hub b to be y, and the tested deletion label a to be q. SV4445 says that either T contains a current selected adjacency directly crossing

  (Q-q) | P_y,                                          (RU.3)

or the support Q-q+y is Hamiltonian. The latter is C(y,q), contrary to assumption. Hence every exact H-q cover contains a selected crossing (RU.3).

Therefore

  C(y,q)=1
  iff there exists a crossing-free exact H-q representative relative to (Q-q)|(Omega-y),

while

  C(y,q)=0
  iff q is universally crossing relative to the source row H-y=Q|P_y.       (RU.4)

The reverse implication in the second line is literal: if C(y,q)=1, (RU.2) is an explicit crossing-free witness, so universal crossing is impossible.

### 3. The reciprocal exchange matrix is the complement of a universal-crossing matrix
Define

  U(y,q)=1  iff every exact two-cover of H-q selects a (Q-q)|(Omega-y) adjacency.

Equation (RU.4) gives the exact matrix identity

  U(y,q)=1-C(y,q).                                      (RU.5)

Thus reciprocal support failure is not merely a bad insertion order or a shield. It is a quantified statement about every representative in the opposite singleton-deletion fiber.

Now also define the active replacement predicate

  A(y,q) : Omega-y+q is Hamiltonian.                    (RU.6)

If A(y,q)=C(y,q)=1, choose Hamilton paths on the two supports Omega-y+q and Q-q+y. They are disjoint and partition V(H), giving a spanning two-cover. Hence in a counterexample

  A(y,q)=1  =>  C(y,q)=0  =>  U(y,q)=1.                (RU.7)

So every successful active one-for-one replacement must sit opposite a universal-crossing reciprocal failure. This is the exact support/crossing duality required by Critical-Block Complement Absorption.

### 4. Anchored transfer corollary and simultaneous crossing pressure
In the HHH anchored quiet-triangle packet write

  Omega=Y disjoint_union V(M),
  Y={y_0,y_1,y_2},
  Q=(q_0,q_1,...,q_t),
  Q^-=Q-q_0.

If y_i is a TRANSFER index of SV19956, the actual transfer path proves A(y_i,q_0)=1, while the reciprocal-support argument of SV20713 proves

  C(y_i,q_0)=0.

Therefore by (RU.4), for every exact two-cover T of H-q_0 there is a selected edge between

  Q^-  and  R_i=Omega-y_i.                              (RU.8)

This statement is universal over T; it is stronger than retaining one chosen source-transfer representative.

If two distinct labels y_i,y_j transfer, put

  K=Omega-{y_i,y_j}=R_i cap R_j.

Every exact T of H-q_0 must satisfy both universal crossing requirements. Hence either T selects a Q^-|K edge, which witnesses both requirements simultaneously, or, if no such common-core edge is selected, the R_i requirement can only be met through y_j and the R_j requirement only through y_i. In that case T selects both a Q^-|y_i contact and a Q^-|y_j contact. Thus

  two transfers => common-core crossing, or two named exchanged-label contacts.          (RU.9)

If all three labels transfer, the common core is M. If an exact H-q_0 cover has no Q^-|M selected edge, let S be the set of triangle labels incident with selected Q^-|Y edges. For each i, universal crossing of R_i=M union (Y-{y_i}) requires S to meet Y-{y_i}. A singleton S={y_k} fails the condition for i=k. Therefore |S|>=2. Hence

  three transfers => Q^-|M crossing, or Q^- contacts at least two distinct vertices of Y. (RU.10)

The TTT statement is the exact terminal dual.

### 5. Scope
This does not prove CBCA and does not consume the universal-crossing side of (RU.5). It supplies an exact bridge between the reciprocal-density language and the older universal-crossing language, with representative quantifiers preserved. In particular, an anchored transfer should no longer be treated as only a support move plus inward shields: its reciprocal failure has already universalized the opposite singleton fiber. Multiple transfers create simultaneous universal crossing constraints on one common target residue, which should be consumed before generic balanced-pair/payment abstraction.

