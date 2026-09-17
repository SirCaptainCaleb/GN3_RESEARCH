# Rigid defect-one exchange has at most three augmenting components

**Workspace:** D17
**State:** established
**Key:** `g33-rigid-augmenting-component-count-bound`

**Summary:** Retain SV103932 in its DUAL RIGIDITY branch for one cut three-forest J. Let d=tau(F)-tau(J)>=1 and let P,N be the numbers of delta=+1 and delta=-1 symmetric-difference components. Since sum delta=1, P=N+1, and SV103932 gives w(C)>=d for every +1 component. Negative transition weight outside the augmenters is bounded below by -tau(J), because it can only be paid for by J-selected X|B edges and tau(J)<=2. Hence d>=Pd-tau(J), so (P-1)d<=tau(J)<=2. Therefore P<=3 always; d>=3 forces P=1; d=2 gives P<=2; d=1 gives P<=3. If equality (P-1)d=tau(J) holds, every inequality saturates: each augmenter carries exactly d F-transitions and no J-transition, each loser carries exactly d J-transitions and no F-transition, every delta-zero component is transition-free, and no X|B transition is common to F and J. Thus the extremal rigid kernels are pure transition-polarized finite packets. Physical collision implications, mixed turns and cycle debt remain downstream.

### 1. Setup
Retain the defect-one normal form SV103530 and the transition-weighted duality SV103932 for one of the two cut forests J. Thus F is the actual old exact two-cover of the top fiber G, J is a literal spanning three-path forest, and

  d := tau(F)-tau(J) >= 1.

Let the connected components of the bipartite matching symmetric difference M_F triangle M_J carry the exact weights

  delta(C)=|M_F intersect C|-|M_J intersect C| in {-1,0,1},
  w(C)=tau(M_F intersect C)-tau(M_J intersect C).

Their totals are

  sum_C delta(C)=1,
  sum_C w(C)=d.                                           (RC.1)

Assume the DUAL RIGIDITY branch of SV103932, i.e. no delta-one component subfamily has transition weight below d. Then every F-heavy component C with delta(C)=+1 satisfies

  w(C) >= d.                                             (RC.2)

Write P for the number of delta=+1 components and N for the number of delta=-1 components. Equation (RC.1) gives

  P=N+1.                                                 (RC.3)

### 2. Negative transition weight has a two-edge budget
For any symmetric-difference component C, write

  f_C = number of X|B edges of M_F in C,
  j_C = number of X|B edges of M_J in C.

Then w(C)=f_C-j_C with f_C,j_C nonnegative. Therefore

  w(C) >= -j_C.                                         (RC.4)

Summing (RC.4) over every component that is NOT delta=+1 gives

  sum_{delta(C)<=0} w(C) >= - sum_{delta(C)<=0} j_C
                           >= - tau(J).                  (RC.5)

The last inequality is literal: the symmetric-difference components partition all changed matching copies, and the total number of J-selected X|B edges over all components is at most the total number tau(J) of such edges in J. Common F/J transition edges are outside the symmetric difference and contribute zero to every w(C).

By SV103530,

  tau(J) <= 2.                                          (RC.6)

### 3. Augmenting-component count bound
Using (RC.2), (RC.5), and the total transition discrepancy in (RC.1),

  d = sum_C w(C)
    = sum_{delta(C)=+1} w(C) + sum_{delta(C)<=0} w(C)
    >= P d - tau(J).                                    (RC.7)

Hence

  (P-1)d <= tau(J) <= 2.                                (RC.8)

This gives the exact finite alternatives:

- P <= 3 always;
- if d >= 3, then P=1;
- if d=2, then P<=2;
- if d=1, then P<=1+tau(J)<=3.

Since N=P-1 by (RC.3), there are at most two delta=-1 components. Thus the transition-active defect-one exchange never has an unbounded family of augmenting/losing paths.

### 4. Negative neutral components are also bounded
If delta(C)=0 and w(C)<0, then j_C>=1. Distinct symmetric-difference components are edge-disjoint, so distinct negative-weight neutral components consume distinct J-selected X|B transitions. Therefore there are at most

  tau(J) <=2                                             (RC.9)

such components. Delta-zero components with w(C)=0 may remain numerous, but they are transition-inert. Positive-weight delta-zero components are impossible in DUAL RIGIDITY by SV103932.

Consequently every component carrying nonzero transition discrepancy belongs to a bounded kernel consisting of at most three augmenters, at most two losers, and at most two negative neutral components. All remaining symmetric-difference components have delta=w=0.

### 5. Equality gives pure transition polarization
Assume the count bound is sharp:

  (P-1)d = tau(J).                                      (RC.10)

Then N=P-1 and every inequality in the derivation of (RC.8) must be equality. First, every augmenter has

  w(C_+)=d.                                             (RC.11)

For every loser C_- and any augmenter C_+, DUAL RIGIDITY applied to the zero-delta pair gives

  w(C_-)+w(C_+) <=0,

so (RC.11) forces w(C_-)<=-d. There are N=P-1 losers, hence their total weight is at most

  -Nd=-(P-1)d=-tau(J).

But (RC.5) says the total weight of ALL nonaugmenting components is at least -tau(J). Therefore equality holds everywhere. In particular:

- every loser has w(C_-)=-d;
- every delta-zero component has w=0;
- the nonaugmenting components collectively contain exactly tau(J) J-transitions and zero F-transitions.

Since each loser has w=f_C-j_C=-d with f_C>=0 and j_C>=d, and the N losers together already require Nd=tau(J) J-transitions, every loser has exactly

  j_C=d,  f_C=0.                                        (RC.12)

All J-transitions are exhausted by the losers. Hence no augmenter contains a J-transition and no X|B transition is common to F and J. Equation (RC.11) then gives for every augmenter

  f_C=d,  j_C=0.                                        (RC.13)

Finally every delta-zero component is transition-free. Thus the sharp rigid packet is PURELY TRANSITION-POLARIZED: the P augmenters partition all

  tau(F)=d+tau(J)=Pd

old F-transitions into d per augmenter, while the N=P-1 losers partition all tau(J)=Nd new J-transitions into d per loser.

The two largest finite kernels are therefore completely explicit numerically:

- d=2,P=2: tau(F)=4,tau(J)=2; two augmenters each carry exactly two F-transitions, one loser carries exactly the two J-transitions, and every neutral component is transition-free.
- d=1,P=3: tau(F)=3,tau(J)=2; three augmenters each carry one F-transition, two losers each carry one J-transition, and every neutral component is transition-free.

The analogous d=1,P=2,tau(J)=1 equality cell has two one-F-transition augmenters and one one-J-transition loser.

### 6. Consequence for the G33 physical consumer
The most rigid regime is d>=3: there is exactly ONE F-heavy augmenting component. Any failure of direct source descent must therefore be concentrated on one alternating path together with transition-inert neutral exchange components. For d=2 there are at most two augmenters, and the P=2 extreme is the pure 2+2 versus 2 transition packet above. For d=1 there are at most three, with the P=3 extreme the pure three-versus-two packet above. This makes the next physical task finite: consume mixed-turn collision implications and directed-cycle debt on a bounded transition-bearing core rather than on an arbitrary symmetric-difference forest.

No claim is made that a unique augmenter is already locally tight, acyclic, collision-closed, or contains the retained source incidence s-h. The result is a static counting contraction only.

### 7. Scope
This section uses only the exact F,J matching coordinates and DUAL RIGIDITY conclusions of SV103530/SV103932 plus nonnegativity of transition-edge counts. It does not use R24, R5, payment/replay lineage, or any edge-order representation. Physical realization remains the downstream G33 obligation.
