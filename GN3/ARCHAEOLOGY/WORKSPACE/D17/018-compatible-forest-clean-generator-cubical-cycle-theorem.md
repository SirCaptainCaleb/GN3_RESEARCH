# Pairwise clean one-edge generators are cubical until one physical cycle portal appears

**Workspace:** D17
**State:** established
**Key:** `compatible-forest-clean-generator-cubical-cycle-theorem`

**Summary:** Let F be a literal maximum spanning three-forest in a hypothetical smallest counterexample and let tau_i=(a_i->b_i) be finitely many distinct reversible support-changing one-edge generators from F. Assume every pair of generators has the SQUARE outcome of the complete one-edge diamond theorem SV38940. Then for every subset S of generators the simultaneous selected-edge set M_S=(M(F)-{a_i:i in S}) union {b_i:i in S} is automatically a bipartite matching of size n-3 and every selected predecessor-successor turn is tight: any local turn uses either zero, one, or two new edges and is inherited respectively from F, one single-generator forest F_i, or one pairwise square endpoint F_ij. Hence every M_S is a tight directed pseudoforest. If every M_S is acyclic, the entire Boolean cube of simultaneous switches consists of literal maximum three-forests, so all generators commute in arbitrary order at base-representative level. More generally, if S is inclusion-minimal with M_S not a forest, then |S|>=3 and M_S has one unique proper tight directed cycle C containing every added edge b_i for i in S. Indeed any cycle omitting b_i would survive after undoing switch i, contradicting minimality; therefore all cycles contain every b_i and uniqueness follows from indegree/outdegree at most one. Breaking C at any edge and applying smallest-counterexample minimality to that proper tight path currentizes the obstruction as a maximum-three-forest cycle portal. Thus the clean support-changing exchange geometry is cubical in every arity until the first missing cube face, and every inclusion-minimal missing face is exactly one all-generator physical cycle-debt portal. A six-vertex three-switch local model shows this higher-arity cycle datum is genuinely missing from pairwise square information: all three pairwise square corners exist while the triple corner is a directed tight 3-cycle. Consequently ordinary matroid/delta-matroid/median/CAT(0)-cube conclusions cannot be deduced from pairwise square axioms alone; the right abstract structure must retain physical cycle debt or quotient it through a portal consumer.

### 1. Setup: a pairwise-clean star of support-changing generators
Let H be a hypothetical smallest counterexample and let

  F=P_1|P_2|P_3

be a literal maximum spanning three-forest. Write M for its directed bipartite selected matching in V_out disjoint_union V_in, so |M|=|V(H)|-3.

Retain a finite family of distinct reversible SUPPORT-CHANGING one-edge generators from F,

  tau_i=(a_i -> b_i),   i in I,

meaning that

  M_i=(M-{a_i}) union {b_i}

is the selected matching of a literal maximum three-forest F_i. Assume moreover that EVERY pair i!=j has the SQUARE outcome of SV38940. Thus the simultaneous replacement

  M_{ij}=(M-{a_i,a_j}) union {b_i,b_j}

is the selected matching of a literal maximum three-forest F_{ij}.

The purpose is to determine all higher simultaneous replacements without adding any new local taxonomy.

### 2. Pairwise square coherence forces simultaneous matching compatibility in every arity
First, the deleted edges a_i are pairwise distinct. If a_i=a_j, the common-deletion branch of SV38940 cannot have the SQUARE outcome: adding both b_i,b_j after one deletion changes the selected-edge count by +1 and therefore either augments, emits a trimer, or carries shared cycle debt.

Second, because F_i is a bipartite matching, b_i conflicts with no old selected edge of M except possibly the deleted edge a_i. Third, because F_{ij} is a bipartite matching, b_i and b_j do not compete for one out-copy or one in-copy.

Therefore for EVERY subset S subseteq I the simultaneous edge set

  M_S=(M-{a_i:i in S}) union {b_i:i in S}                 (HC.1)

is a bipartite matching. Since every switch removes and adds one edge,

  |M_S|=|M|=|V(H)|-3.                                    (HC.2)

So all higher obstruction is physical turn/cycle geometry, not matching collision.

### 3. Every higher simultaneous replacement is locally tight
Consider any physical predecessor-successor pair

  x -> v -> y

selected by M_S. There are only three possibilities.

1. Both selected states are old M-edges. The turn is inherited from F.
2. Exactly one selected state is a new edge b_i. The turn occurs already in F_i and is tight there.
3. The two selected states are distinct new edges b_i,b_j. The turn occurs already in the literal pairwise-square endpoint F_{ij} and is tight there.

The same argument excludes a physical two-edge backtrack: such a backtrack would already occur in the corresponding one- or two-generator endpoint.

Hence EVERY M_S is a directed tight pseudoforest: its physical components are vertex-simple tight paths, singleton vertices, or vertex-simple directed tight cycles. Combining this with (HC.2),

  M_S is a literal maximum three-forest  iff  M_S is acyclic.   (HC.3)

In particular, if every M_S is acyclic, the whole Boolean cube 2^I is realized by literal maximum-three-forest representatives. Any ordering of the switches reaches the same simultaneous endpoint, and every face is an actual cubical commutation relation.

### 4. An inclusion-minimal missing face is one all-generator cycle
Suppose some M_S is not a forest and choose S inclusion-minimal with that property. Every singleton and every pair is a forest by hypothesis, so

  |S|>=3.                                                 (HC.4)

Let C be a directed physical cycle of M_S. Fix i in S. I claim b_i lies on C. If not, C uses neither b_i nor a_i: the edge a_i was removed from M_S, while b_i is absent from C. Undoing switch i replaces b_i by a_i but changes no edge of C. Thus the same directed cycle C survives in M_{S-{i}}, contradicting minimality. Therefore

  {b_i:i in S} subseteq E(C).                            (HC.5)

Because M_S has physical indegree and outdegree at most one, distinct directed cycles are vertex-disjoint. But by (HC.5) every directed cycle would contain every b_i. Hence there is exactly ONE cycle C.

It is proper. A spanning directed cycle on n vertices contains n selected edges, whereas M_S contains only n-3. Every turn of C is tight by Section 3. Thus C is one proper vertex-simple tight cycle containing every new edge of the minimal bad face.

Break C at any one selected edge. The remaining cyclic order is a proper graph-intrinsic tight Hamilton path K on V(C). Accepted smallest-counterexample minimality R4 gives an exact two-cover of H-V(C); adjoining K gives a literal maximum spanning three-forest. Varying the broken edge gives the usual current movable-break family. Thus the failure of the higher cube is not anonymous: it is an explicit CURRENT CYCLE PORTAL carrying all generators in S.

We have proved the parent theorem:

  PAIRWISE SQUARES => FULL BOOLEAN CUBE
  unless an inclusion-minimal missing face is exactly one unique
  proper tight cycle containing every new edge of that face.        (HC.6)

This is the higher-arity analogue of the two-generator shared-cycle branch, but its proof uses only the pairwise square endpoints and the literal physical matching. No new pair classification is required.

### 5. Sharp local three-generator model: pairwise diamonds do not imply a full cube
The cycle-debt alternative in (HC.6) is not a formal nuisance. It already appears in the smallest three-generator local model.

Take six physical vertices

  a_1,a_2,a_3,x_1,x_2,x_3

and the base three-dimer forest

  F=(a_1,x_1)|(a_2,x_2)|(a_3,x_3).

Write d_i=a_i->x_i. Define three switches

  tau_1: d_1 -> b_1=a_1->a_2,
  tau_2: d_2 -> b_2=a_2->a_3,
  tau_3: d_3 -> b_3=a_3->a_1.                           (HC.7)

Prescribe the following turns tight:

  (a_1,a_2,x_2), (a_2,a_3,x_3), (a_3,a_1,x_1),
  (a_1,a_2,a_3), (a_2,a_3,a_1), (a_3,a_1,a_2).          (HC.8)

These prescriptions occupy distinct complete-reversal pairs, so they extend to a Strong Level-(1) boundary tournament by orienting all remaining reversal pairs arbitrarily.

Every singleton switch gives a literal three-forest, for example

  tau_1: (a_1,a_2,x_2)|{x_1}|(a_3,x_3).

Every pair gives a literal three-forest, for example

  tau_1 tau_2: (a_1,a_2,a_3,x_3)|{x_1}|{x_2},

and cyclically. Thus all three pairwise diamonds exist. But the triple replacement is

  (a_1->a_2->a_3->a_1) plus {x_1},{x_2},{x_3},          (HC.9)

so the missing 111 corner is exactly one directed tight 3-cycle.

This model is a LOCAL AXIOM FENCE, not a claim that these six vertices form a smallest counterexample. It proves that pairwise square geometry by itself cannot force a full cube; the higher physical cycle datum is indispensable.

The same seven-corner switch system also blocks several naive abstract identifications if they are supposed to follow only from the pairwise one-edge axioms. In switch coordinates its state graph is Q_3 with the 111 corner removed, so the three states 110,101,011 have their cube median 111 missing. Hence pairwise-square axioms alone do not imply a median graph or CAT(0)-cube graph. On the selected-edge ground set, the feasible equal-size edge sets of this model also violate ordinary basis exchange: compare the 011 state containing d_1,b_2,b_3 with the 100 state containing b_1,d_2,d_3 and try to exchange d_1. Replacing it by b_1 gives the forbidden triple corner; replacing it by d_2 or d_3 conflicts with the already selected b_2 or b_3. The same paired-edge check defeats the symmetric-exchange axiom for this equal-cardinality family, so pairwise square geometry alone does not imply a delta-matroid either.

### 6. Abstract exchange consequence and remaining datum
The one-edge support-changing state space therefore has a precise higher-dimensional skeleton. At a fixed literal representative F, declare a k-cube whenever k support-changing generators are simultaneously realizable for every subset. Section 3 says pairwise-clean stars automatically satisfy all LOCAL turn constraints in every dimension. Section 4 says the first absent cube face can fail only through one unique physical tight cycle that contains every generator of that face.

Thus the natural bespoke structure is not an ordinary matroid/median cube system. It is a CUBICAL EXCHANGE SYSTEM WITH CYCLE-CIRCUIT DEFECTS: clean generators commute in arbitrary dimension, and every minimal higher nonface carries one explicit current cycle portal.

For G15 this sharply relocates the global problem. Base one-edge curvature is zero on every realized cube. The surviving sources of nontrivial history are:

1. transport of a genuinely history-bearing mark around an otherwise realized cube;
2. passage through one of the explicit higher cycle-circuit portals;
3. non-one-edge component recompletions and other portal generators.

No claim is made that arbitrary ancestry marks are automatically coherent around the cubes, that cycle portals are already absorbed globally, or that the full maximum-three-forest space is median/CAT(0)/matroidal. The theorem isolates exactly why those stronger structures can fail and identifies the additional datum the correct exchange theory must remember.

## References

```json
[
    {"relation":"dependency","revision_id":"R4"}
]
```
