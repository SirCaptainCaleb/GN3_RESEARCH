# Arm-U parity leakage either collides into a three-witness wall or compresses to a seven-vertex double-defect nucleus

**Workspace:** D17
**State:** established
**Key:** `universal-source-parity-leakage-or-double-defect-nucleus`

**Summary:** Fix one Arm-U universe V(H)=Omega disjoint B and retain one actual Hamilton puncture path P_q for each good q. Outside same-complement R435 output and the one-edge transfer/cycle portals of SV48512, every bad endpoint incidence q--r gives the same bidirectional two-probe wall on the literal fixed rail B. Form the bipartite incidence graph between good labels and bad labels, joining q to each bad endpoint of its retained P_q. If some bad r has two good neighbors q,s, then q,s,r simultaneously witness both reverse boundary dimers of B; hence the exact three-witness common-crossing machinery SV44176/SV44695 is available at both ends of the same literal B. If every bad vertex has incidence degree at most one, then |D(Omega)|>=|G(Omega)|. Moreover some retained puncture word contains two consecutive bad labels: otherwise the bad labels form an independent set in each path P_q, forcing |D|<=|G|; equality then forces exact bad/good alternation with both endpoints bad in every P_q, producing 2|G| bad-endpoint incidences on only |D|=|G| bad vertices, contradicting degree at most one. For such a consecutive bad pair z,w on P_q, the source-local substitution mechanism at z and w supplies two q-labelled reverse trimers whose union is contained in the seven-vertex window consisting of q and source positions from two steps before z through two steps after w. Thus the genuinely Arm-U-specific leakage residue is bounded local double-defect curvature. Finally, when B is a largest source rail of order at least six, define chi_B(u) by the cross-B turn (b0,u,bt). Equal chi on any bad-endpoint incidence gives, by R584 and the two-probe wall, an explicit maximum-three-forest whose largest rail is at most |B|-1. Hence a no-local-dip sparse residue is an injective parity-reversing leakage G_i -> D_{1-i}. This local dip is not promoted to global phased-Morse descent.

### 1. Fixed-universe endpoint incidence
Let H be a hypothetical smallest counterexample and retain the Arm-U fixed-universe setting

  V(H)=Omega disjoint_union V(B),
  B=(b_0,b_1,...,b_t),

with B a literal Hamilton tight path and Omega non-Hamiltonian. Put

  G={q in Omega : Omega-q is Hamiltonian},
  D={z in Omega : Omega-z is non-Hamiltonian}.

For every q in G choose and retain one ACTUAL Hamilton puncture path

  P_q=(p^q_0,...,p^q_m)                                  (PL.1)

on Omega-q. Assume first that the common-B puncture family is in the R435-quiet branch of SV51259. Then every P_q has at least one endpoint in D.

Define the BAD-ENDPOINT INCIDENCE GRAPH Gamma with bipartition G|D by

  q--r in E(Gamma)

exactly when r is a physical endpoint of the retained word P_q and r lies in D. Thus every q in G has degree at least one. We retain the actual puncture word certifying every incidence.

Now also exclude, for the moment, the current one-edge support-transfer and tight-cycle portals of SV51539. For every incidence q--r, applying SV51539 to that exact good-bad endpoint cell therefore lands in its portal-free branch and gives the graph-intrinsic wall

  (b_1,b_0,q), (b_1,b_0,r) tight,                        (PL.2)
  (q,b_t,b_{t-1}), (r,b_t,b_{t-1}) tight.                (PL.3)

Thus every Gamma-edge is literally a two-probe wall on the SAME physical rail B.

### 2. Endpoint collision gives the full three-witness wall
Suppose some bad label r has two distinct good neighbors q,s in Gamma. Applying (PL.2)-(PL.3) to q--r and s--r and retaining the graph-intrinsic turns simultaneously gives

  (b_1,b_0,u) tight for u in {q,s,r},                     (PL.4)
  (u,b_t,b_{t-1}) tight for u in {q,s,r}.                 (PL.5)

Hence the reverse initial B-dimer has three distinct same-tail witnesses q,s,r and the reverse terminal B-dimer has the SAME three distinct same-head witnesses.

This is exactly the physical witness multiplicity used in the Arm-M wall, without requiring deletion-Hamiltonicity of all of Omega. In particular, take the carrier K=B and either tested reverse boundary dimer as S. Accepted R429 supplies an exact two-cover of H-V(S), and the hypotheses of the same-parent three-witness compiler SV44176 are met: all three witnesses lie outside B. Therefore each boundary is immediately eligible for the refined SV44176/SV44695 output

  literal P4/P5,
  or direct mass-four balanced pair,
  or the accepted R407 bidirectional same-witness interaction.       (PL.6)

No witness-indexed payment descendants are asserted to coexist; this is precisely the common-parent use proved in those sections.

Thus a repeated bad endpoint is not an Arm-U-specific residue. It has already rejoined the Arm-M three-witness interface.

### 3. If bad endpoints do not collide, defects are at least half the universe
Assume from now on that every r in D has Gamma-degree at most one. Since every q in G has Gamma-degree at least one,

  |E(Gamma)| >= |G|,
  |E(Gamma)| <= |D|,

and therefore

  |D| >= |G|.                                             (PL.7)

This is the first structural difference from the Arm-M deletion-Hamiltonian block: endpoint flow is allowed to leak from good labels into genuinely bad sinks.

### 4. Sparse leakage forces a consecutive bad-bad state
We claim that under the degree-at-most-one assumption, at least one retained puncture word P_q contains two consecutive vertices of D.

Suppose not. Fix q in G. The word P_q contains every bad label, hence exactly |D| bad vertices, and every remaining vertex of P_q is good, hence exactly |G|-1 good vertices. If no two bad labels are consecutive in this linear word, the elementary independent-set bound for a path word gives

  |D| <= (|G|-1)+1 = |G|.                                (PL.8)

Together with (PL.7), equality holds:

  |D|=|G|.                                                (PL.9)

Equality in (PL.8) forces exact alternation along EVERY retained P_q, beginning and ending with bad labels. Consequently every q in G contributes TWO distinct bad endpoints to Gamma. Hence

  |E(Gamma)| >= 2|G| = 2|D|,                             (PL.10)

contradicting the assumption that every bad vertex has degree at most one, which gives |E(Gamma)|<=|D|.

Therefore some retained actual puncture path contains a selected state

  z w                                                       (PL.11)

with z,w both in D.

### 5. The leakage residue is a bounded double-defect curvature nucleus
Fix q in G and an actual puncture word

  P_q=(...,z,w,...)                                       (PL.12)

with consecutive bad labels z,w. Let z occupy position i and w position i+1.

Apply the source-local substitution argument of SV45572/SV44785 to the pair (q,z) in this SAME retained word. Because Omega-z is non-Hamiltonian, replacing z in place by q fails in one of at most three turns involving q; R3 reverses one failed turn to a proper q-labelled tight trimer

  J_z.                                                     (PL.13)

Apply the same literal argument to (q,w). It gives another proper q-labelled tight trimer

  J_w.                                                     (PL.14)

No synchronization of the two failure types is assumed. Nevertheless their physical supports are bounded. J_z uses q and source vertices whose P_q-indices lie between i-2 and i+2, excluding z as appropriate. J_w uses q and indices between i-1 and i+3, excluding w as appropriate. Hence

  V(J_z) union V(J_w)
    subseteq {q, p^q_{i-2},p^q_{i-1},z,w,p^q_{i+2},p^q_{i+3}},       (PL.15)

with nonexistent endpoint positions omitted. In particular the entire double curvature packet lives on AT MOST SEVEN physical vertices.

Thus the endpoint-leakage escape from the three-witness wall does not remain an unbounded source-fan phenomenon. It compresses to one selected bad-bad dimer together with two overlapping source-labelled curvature trimers in a bounded local nucleus.

This section does not claim that the two trimers interact automatically by R435 or that the seven-set is itself contradictory. The exact failed windows and both trimer orders must be retained for the next finite consumer.

### 6. Cross-B parity: equal parity gives a genuine local largest-rail dip
There is an additional rank-sensitive refinement when B is the marked largest source rail. Put

  b=|B|=t+1,
  a=|P_q|=|Omega|-1,

and assume

  b>=a,  b>=6.                                             (PL.16)

For every u in Omega define the cross-B bit

  chi_B(u)=1 iff (b_0,u,b_t) is tight.                    (PL.17)

Fix any bad-endpoint incidence q--r. In its portal-free two-probe wall, if

  chi_B(q)=chi_B(r)=1,                                    (PL.18)

accepted R584 gives one of the tight P4s

  (b_0,q,b_t,r), (b_0,r,b_t,q).                          (PL.19)

Prepend b_1 using the matching wall turn from (PL.2). This gives a literal tight P5 S. Its complement is exactly the two literal paths

  B[2,t-1] | (P_q-r),                                     (PL.20)

where the first path may be short but is nonempty or vacuous only at the harmless small boundary; under b>=6 it has order b-3. Restoring S gives a spanning maximum three-forest with rail orders

  5, b-3, a-1.                                            (PL.21)

By (PL.16) all three are at most b-1.

If instead

  chi_B(q)=chi_B(r)=0,                                    (PL.22)

R3 gives (b_t,q,b_0) and (b_t,r,b_0). R584 gives a tight P4 on {b_t,b_0,q,r}; its complement is

  B[1,t-1] | (P_q-r),                                     (PL.23)

and the resulting maximum forest has rail orders

  4, b-2, a-1,                                            (PL.24)

again all at most b-1.

Therefore, when B is a largest source rail of order at least six, EQUAL cross-B parity on any bad-endpoint incidence gives an explicit strict drop of the current largest-rail order from b to at most b-1.

This is a real current representative improvement, but it is NOT by itself the G18 global phased-Morse cancellation theorem: a later A-growth normalization can move the largest-rail coordinate in the opposite direction. The cross-portal rank comparison remains open.

### 7. The final quiet leakage form is an injective parity-reversing matching
Suppose Sections 2 and 6 both fail to fire: no bad endpoint is shared by two good labels, and in the largest-B regime no equal-parity incidence is allowed. Choose for each q in G any one bad endpoint f(q) of P_q. Because bad endpoint degrees are at most one, f is injective. Because equal parity is excluded,

  chi_B(f(q))=1-chi_B(q).                                 (PL.25)

Writing

  G_i={q in G: chi_B(q)=i},
  D_i={z in D: chi_B(z)=i},

we obtain the parity leakage injections

  f:G_0 -> D_1,
  f:G_1 -> D_0,                                           (PL.26)

and hence

  |G_0|<=|D_1|,
  |G_1|<=|D_0|.                                           (PL.27)

This pinpoints exactly why the Arm-M odd-cycle argument SV46809 has no immediate Arm-U analogue. In Arm M every exterior label is Hamilton-deletable, so endpoint-return parity cannot disappear into a defect set and is forced around a return cycle. In Arm U, the only surviving quiet mechanism is PARITY LEAKAGE INTO BAD SINKS. Sections 3-5 show that enough leakage to avoid witness collision necessarily creates a selected bad-bad dimer and a bounded double-curvature nucleus.

### 8. G18 parent target
The Arm-U stress test therefore leaves two parent cells, not an amorphous universal-crossing branch:

1. THREE-WITNESS FIXED-RAIL WALL, already identical to the Arm-M common-parent interface and already compiled upstream by SV44176/SV44695;
2. SEVEN-VERTEX DOUBLE-DEFECT NUCLEUS, consisting of one good source q, one selected adjacent bad pair z,w in an actual puncture word, and the two exact source-substitution curvature trimers J_z,J_w with their failed-window ancestry.

The second cell is the genuinely new Arm-U obstruction. A parent curvature-cancellation theorem broad enough to close both R927 arms must either consume this bounded nucleus directly, or prove that its parity leakage can be canonically returned to the three-witness/fixed-cap interface.

Status: complete internal working mathematics, unreviewed exposition. The local largest-rail dip in Section 6 is deliberately not promoted to a global phased-Morse descent.

## References

```json
[
    {
        "relation": "dependency",
        "revision_id": "R3"
    },
    {
        "relation": "dependency",
        "revision_id": "R4"
    },
    {
        "relation": "dependency",
        "revision_id": "R429"
    },
    {
        "relation": "dependency",
        "revision_id": "R584"
    }
]
```